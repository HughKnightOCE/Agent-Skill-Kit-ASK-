#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MCP Gateway Server
Exposes Agent-Skill-Kit skills as MCP (Model Context Protocol) tools.
Allows Claude, Copilot, and other agents to discover and execute skills natively.
"""

import sys
import io
import os
import json
import subprocess
import asyncio
from pathlib import Path
from typing import Any, Optional

# Set UTF-8 encoding on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

try:
    import yaml
    from mcp.server.models import InitializationOptions
    from mcp.types import Tool, TextContent
    from mcp.server import Server
except ImportError as e:
    print(f"Error: Required package not installed: {e}")
    print("Install with: pip install mcp pyyaml")
    sys.exit(1)


class SkillMCPServer:
    """MCP Server that exposes ASK skills as tools."""
    
    def __init__(self, skills_dir: str = "skills"):
        self.skills_dir = Path(skills_dir)
        self.server = Server("agent-skill-kit")
        self.skills = self._load_skills()
        self._setup_handlers()
    
    def _load_skills(self) -> dict:
        """Load all available skills and create MCP tool definitions."""
        skills = {}
        
        if not self.skills_dir.exists():
            print(f"Warning: Skills directory not found: {self.skills_dir}")
            return skills
        
        for skill_folder in sorted(self.skills_dir.iterdir()):
            if not skill_folder.is_dir():
                continue
            
            manifest_path = skill_folder / "manifest.yaml"
            if not manifest_path.exists():
                continue
            
            try:
                with open(manifest_path, 'r', encoding='utf-8') as f:
                    manifest = yaml.safe_load(f)
                    skill_name = skill_folder.name
                    
                    # Create MCP tool definition from manifest
                    skills[skill_name] = {
                        'path': skill_folder,
                        'script': skill_folder / "script.py",
                        'manifest': manifest,
                        'tool': Tool(
                            name=manifest.get('name', skill_name),
                            description=manifest.get('description', f'Run {skill_name} skill'),
                            inputSchema={
                                "type": "object",
                                "properties": self._build_properties(manifest),
                                "required": self._get_required_args(manifest)
                            }
                        )
                    }
            except Exception as e:
                print(f"Warning: Failed to load {skill_folder.name}: {e}")
        
        return skills
    
    def _build_properties(self, manifest: dict) -> dict:
        """Build JSON schema properties from manifest."""
        properties = {}
        
        # Add required arguments
        if manifest.get('usage', {}).get('args_required'):
            for arg in manifest['usage']['args_required']:
                properties[arg['name']] = {
                    "type": "string",
                    "description": arg.get('description', 'Argument')
                }
        
        # Add optional arguments
        if manifest.get('usage', {}).get('args_optional'):
            for arg in manifest['usage']['args_optional']:
                properties[arg['name']] = {
                    "type": "string",
                    "description": arg.get('description', 'Optional argument')
                }
        
        return properties
    
    def _get_required_args(self, manifest: dict) -> list:
        """Get list of required argument names."""
        required = []
        if manifest.get('usage', {}).get('args_required'):
            required = [arg['name'] for arg in manifest['usage']['args_required']]
        return required
    
    def _setup_handlers(self):
        """Setup MCP request handlers."""
        
        @self.server.list_tools()
        async def list_tools() -> list[Tool]:
            """List all available skills as MCP tools."""
            return [skill['tool'] for skill in self.skills.values()]
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: dict) -> list[TextContent]:
            """Execute a skill and return results."""
            if name not in self.skills:
                return [TextContent(
                    type="text",
                    text=f"Error: Skill '{name}' not found"
                )]
            
            skill = self.skills[name]
            script_path = skill['script']
            
            if not script_path.exists():
                return [TextContent(
                    type="text",
                    text=f"Error: Script not found for skill '{name}'"
                )]
            
            # Build command with arguments
            cmd = [sys.executable, str(script_path)]
            cmd.extend(str(v) for v in arguments.values())
            
            try:
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=30,
                    encoding='utf-8',
                    errors='replace'
                )
                
                output = result.stdout
                if result.stderr:
                    output += f"\n\nErrors:\n{result.stderr}"
                
                return [TextContent(
                    type="text",
                    text=output or "Skill executed successfully (no output)"
                )]
            
            except subprocess.TimeoutExpired:
                return [TextContent(
                    type="text",
                    text=f"Error: Skill '{name}' execution timed out"
                )]
            except Exception as e:
                return [TextContent(
                    type="text",
                    text=f"Error executing skill '{name}': {str(e)}"
                )]
    
    async def run(self):
        """Run the MCP server."""
        async with self.server:
            # Server will run and accept JSON-RPC requests
            print(f"MCP Server running with {len(self.skills)} skills available")
            print("Skills:", list(self.skills.keys()))
            await asyncio.Future()  # Run forever


def main():
    """Main entry point for MCP gateway."""
    server = SkillMCPServer()
    
    # Run the server
    asyncio.run(server.run())


if __name__ == "__main__":
    main()
