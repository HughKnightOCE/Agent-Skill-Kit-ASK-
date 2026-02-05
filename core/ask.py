#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ASK (Agent-Skill-Kit) Manager
A beautiful, agent-native CLI for running local, keyless skills.
2026 Edition: Enhanced TUI with system health, ASCII art, and live displays.
"""

import os
import sys
import subprocess
import shutil
import yaml
import time
from pathlib import Path
from typing import Dict, List, Optional

# Detect if running as PyInstaller exe
RUNNING_AS_EXE = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')

# Set UTF-8 encoding on Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.syntax import Syntax
    from rich.markdown import Markdown
    from rich.text import Text
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.layout import Layout
    from rich.live import Live
except ImportError:
    print("Error: 'rich' is required. Install with: pip install rich")
    sys.exit(1)

# Use simpler console options if running as exe to avoid unicode issues
if RUNNING_AS_EXE:
    console = Console(force_terminal=True, width=100, legacy_windows=True, no_color=False)
else:
    console = Console(force_terminal=True, width=100, legacy_windows=False)

class SkillManager:
    """Manage and execute skills."""
    
    def __init__(self, skills_dir: str = None):
        if skills_dir is None:
            # When installed via pip, skills are in the package directory
            # When running directly, skills are in the local 'skills' folder
            package_skills = Path(__file__).parent.parent / "skills"
            if package_skills.exists():
                skills_dir = package_skills
            else:
                skills_dir = "skills"
        
        self.skills_dir = Path(skills_dir)
        self.skills = self._load_skills()
    
    def _load_skills(self) -> Dict[str, Dict]:
        """Load all available skills and their manifests."""
        skills = {}
        
        if not self.skills_dir.exists():
            return skills
        
        for skill_folder in self.skills_dir.iterdir():
            if not skill_folder.is_dir():
                continue
            
            manifest_path = skill_folder / "manifest.yaml"
            if not manifest_path.exists():
                continue
            
            try:
                with open(manifest_path, 'r', encoding='utf-8') as f:
                    manifest = yaml.safe_load(f)
                    skills[skill_folder.name] = {
                        'path': skill_folder,
                        'manifest': manifest,
                        'script': skill_folder / "script.py"
                    }
            except Exception as e:
                try:
                    console.print(f"[red]Error loading {skill_folder.name}: {e}[/red]")
                except:
                    print(f"Error loading {skill_folder.name}: {e}")
        
        return skills
    
    def display_banner(self):
        """Display ASK-2026 banner."""
        if RUNNING_AS_EXE:
            # Simplified banner for exe to avoid unicode issues
            print("\n" + "="*60)
            print("  AGENT-SKILL-KIT v2.0 (ASK-2026)")
            print("  Zero Keys | Agent-Native | Zero Maintenance")
            print("="*60 + "\n")
        else:
            # Full fancy banner for normal Python
            banner = """
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║          🤖 AGENT-SKILL-KIT v2.0 (ASK-2026)                 ║
║                                                               ║
║        Zero Keys | Agent-Native | Zero Maintenance           ║
║                                                               ║
║   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   ║
║                                                               ║
║   Local Power Unleashed for AI Agents                        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""
            console.print(banner)
    
    def display_system_health(self):
        """Display system health dashboard."""
        # Check Python version
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        
        # Check Git
        git_available = bool(shutil.which('git'))
        git_status = "✅ Installed" if git_available else "⚠️  Not Found"
        
        # Check dependencies
        try:
            import yaml as _
            yaml_status = "✅ OK"
        except:
            yaml_status = "⚠️  Missing"
        
        # Create health table
        table = Table(title="System Health Dashboard", show_header=True, header_style="bold cyan")
        table.add_column("Component", style="cyan")
        table.add_column("Status", style="green")
        
        table.add_row("Python Version", python_version)
        table.add_row("Git", git_status)
        table.add_row("PyYAML", yaml_status)
        table.add_row("Skills Loaded", f"{len(self.skills)} active")
        
        console.print(table)
        console.print()
        
    
    def display_dashboard(self):
        """Display the beautiful skill dashboard with system health."""
        console.print("\n")
        title = Text("Agent-Skill-Kit Dashboard", style="bold cyan", justify="center")
        console.print(Panel(title, expand=False))
        
        # Show system health
        self.display_system_health()
        
        # Create skill table
        table = Table(title="Available Skills", show_header=True, header_style="bold magenta")
        table.add_column("Skill", style="cyan")
        table.add_column("Description", style="white")
        table.add_column("Version", style="green")
        table.add_column("Keys?", style="yellow")
        
        for skill_name, skill_data in sorted(self.skills.items()):
            manifest = skill_data['manifest']
            name = manifest.get('name', skill_name)
            description = manifest.get('description', 'N/A')
            version = manifest.get('version', '?')
            requires_keys = "✅ No" if not manifest.get('api_keys_required', False) else "❌ Yes"
            
            table.add_row(name, description[:50] + "..." if len(description) > 50 else description, version, requires_keys)
        
        console.print(table)
        console.print("\n")
    
    def run_skill(self, skill_name: str, args: List[str] = None) -> int:
        """Execute a skill and display results with live output."""
        if skill_name not in self.skills:
            console.print(f"[red]Skill '{skill_name}' not found![/red]")
            return 1
        
        skill = self.skills[skill_name]
        manifest = skill['manifest']
        script_path = skill['script']
        
        if not script_path.exists():
            console.print(f"[red]Script not found: {script_path}[/red]")
            return 1
        
        # Display skill info with styling
        console.print(f"\n[bold cyan]▶ Executing: {manifest.get('name', skill_name)}[/bold cyan]")
        console.print(f"[dim]{manifest.get('description', '')}[/dim]\n")
        
        # Build command
        cmd = [sys.executable, str(script_path)]
        if args:
            cmd.extend(args)
        
        try:
            # Run skill with live output display
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
                transient=True
            ) as progress:
                task = progress.add_task("[cyan]Running skill...", start=False)
                
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=30,
                    encoding='utf-8',
                    errors='replace'
                )
            
            # Display output in panel
            if result.stdout:
                console.print(Panel(result.stdout, title="Output", border_style="green"))
            
            if result.stderr:
                console.print(Panel(result.stderr, title="Warnings", border_style="yellow"))
            
            return result.returncode
        
        except subprocess.TimeoutExpired:
            console.print("[red]Skill execution timed out![/red]")
            return 1
        except Exception as e:
            console.print(f"[red]Error running skill: {e}[/red]")
            return 1
    
    def doctor(self) -> int:
        """Check system dependencies."""
        console.print("\n")
        title = Text("System Doctor", style="bold cyan", justify="center")
        console.print(Panel(title, expand=False))
        
        checks = {
            'Python': (sys.executable, sys.version.split()[0]),
            'Git': (shutil.which('git'), 'installed'),
            'Rich': ('rich', 'installed'),
        }
        
        all_good = True
        
        for name, (check_cmd, expected) in checks.items():
            if name == 'Rich':
                try:
                    import rich
                    status = "OK"
                    version = "installed"
                except ImportError:
                    status = "Missing"
                    version = "Install: pip install rich"
                    all_good = False
            else:
                if check_cmd:
                    status = "OK"
                    version = expected
                else:
                    status = "Missing"
                    version = f"Install {name}"
                    all_good = False
            
            console.print(f"[bold]{name}:[/bold] {status} [dim]({version})[/dim]")
        
        console.print()
        
        if all_good:
            console.print("[green]All systems operational![/green]\n")
            return 0
        else:
            console.print("[yellow]Some dependencies missing. Install with: pip install rich[/yellow]\n")
            return 1

def show_help():
    """Display help information."""
    help_text = """
# 🤖 ASK (Agent-Skill-Kit) - CLI Commands

## Usage

```bash
 ask [COMMAND] [OPTIONS]
```

## Commands

**dashboard**
  Display available skills and their status
  Example: `ask dashboard`

**run <skill-name> [args]**
  Execute a specific skill
  Example: `ask run repo-visualizer .`
  Example: `ask run agent-identity MyProject`

**doctor**
  Check system dependencies and configuration
  Example: `ask doctor`

**help**
  Show this help message
  Example: `ask help` (or `ask --help`)

## Available Skills

- **repo-visualizer**: Generate Mermaid.js diagrams of your project structure
- **agent-identity**: Create unique SVG avatars using DiceBear API
- **tech-pulse**: Fetch top 5 trending tech stories from HackerNews

## Zero Config Features

✅ No API keys required
✅ No sign-ups needed
✅ Works offline (except API calls)
✅ Local-first architecture
✅ Perfect for AI agents

## Examples

```bash
# View all available skills
python ask.py dashboard

# Generate a project diagram
python ask.py run repo-visualizer

# Create an agent avatar
python ask.py run agent-identity "My Project"

# Stay updated on tech trends
python ask.py run tech-pulse

# Check if everything is installed
python ask.py doctor
```
"""
    console.print(Markdown(help_text))

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        manager = SkillManager()
        manager.display_banner()
        manager.display_dashboard()
        console.print("[dim]Tip: Run 'ask help' for commands[/dim]\n")
        return 0
    
    command = sys.argv[1].lower()
    
    if command in ('help', '--help', '-h'):
        show_help()
        return 0
    
    manager = SkillManager()
    
    if command == 'dashboard':
        manager.display_banner()
        manager.display_dashboard()
        return 0
    
    elif command == 'doctor':
        return manager.doctor()
    
    elif command == 'run':
        if len(sys.argv) < 3:
            console.print("[red]Usage: ask run <skill-name> [args][/red]")
            return 1
        
        skill_name = sys.argv[2]
        args = sys.argv[3:] if len(sys.argv) > 3 else None
        return manager.run_skill(skill_name, args)
    
    else:
        console.print(f"[red]Unknown command: {command}[/red]")
        console.print("[dim]Run 'ask help' for available commands[/dim]\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
