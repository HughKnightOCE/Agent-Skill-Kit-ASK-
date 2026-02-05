#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Repo-Visualizer Skill: Generates a Mermaid.js class diagram of project structure.
No API keys required - uses local file system scanning.
"""

import sys
import io
import os
import json
from pathlib import Path
from typing import Dict, List

# Set UTF-8 encoding on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def scan_directory(root_path: str, max_depth: int = 3, current_depth: int = 0, ignore_dirs: set = None) -> Dict:
    """
    Recursively scan directory structure and build a tree.
    """
    if ignore_dirs is None:
        ignore_dirs = {'.git', '__pycache__', '.venv', 'venv', 'node_modules', '.pytest_cache', '.egg-info'}
    
    if current_depth >= max_depth:
        return {}
    
    structure = {}
    try:
        for item in sorted(os.listdir(root_path)):
            if item.startswith('.') and item not in {'.github', '.gitignore'}:
                continue
            
            item_path = os.path.join(root_path, item)
            
            if os.path.isdir(item_path):
                if item in ignore_dirs:
                    continue
                structure[item] = scan_directory(item_path, max_depth, current_depth + 1, ignore_dirs)
            else:
                structure[item] = "file"
    except PermissionError:
        pass
    
    return structure

def generate_mermaid_diagram(structure: Dict, root_name: str = "ASK") -> str:
    """
    Convert directory structure to Mermaid graph syntax.
    """
    mermaid_lines = ["graph TD"]
    mermaid_lines.append(f'    Root["{root_name}"]')
    
    def add_nodes(tree: Dict, parent: str, prefix: str = ""):
        for idx, (name, content) in enumerate(tree.items()):
            node_id = f"{parent}_{idx}".replace('-', '_').replace(' ', '_')
            
            if isinstance(content, dict):
                mermaid_lines.append(f'    {node_id}["📁 {name}"]')
                mermaid_lines.append(f'    {parent} --> {node_id}')
                add_nodes(content, node_id, prefix + "  ")
            else:
                icon = get_file_icon(name)
                mermaid_lines.append(f'    {node_id}["{icon} {name}"]')
                mermaid_lines.append(f'    {parent} --> {node_id}')
    
    add_nodes(structure, "Root")
    return "\n".join(mermaid_lines)

def get_file_icon(filename: str) -> str:
    """Return emoji icon based on file type."""
    ext = Path(filename).suffix.lower()
    icons = {
        '.py': '🐍',
        '.js': '📜',
        '.ts': '📘',
        '.yaml': '⚙️',
        '.yml': '⚙️',
        '.md': '📄',
        '.txt': '📝',
        '.json': '📊',
        '.xml': '🏷️',
        '.html': '🌐',
        '.css': '🎨',
        '.sh': '🔧',
        '.git': '🔗',
    }
    return icons.get(ext, '📄')

def main(repo_path: str = "."):
    """Main execution function."""
    repo_path = os.path.abspath(repo_path)
    repo_name = os.path.basename(repo_path)
    
    print(f"🔍 Scanning repository: {repo_name}")
    print(f"📍 Path: {repo_path}\n")
    
    structure = scan_directory(repo_path)
    diagram = generate_mermaid_diagram(structure, repo_name)
    
    print("📊 Mermaid.js Diagram:\n")
    print(diagram)
    print("\n✅ Copy the diagram above into: https://mermaid.live")

if __name__ == "__main__":
    import sys
    repo_path = sys.argv[1] if len(sys.argv) > 1 else "."
    main(repo_path)
