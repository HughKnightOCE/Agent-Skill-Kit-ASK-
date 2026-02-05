#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agent-Identity Skill: Generates a unique SVG avatar for your project using DiceBear API.
No API key required - uses free, public endpoint.
"""

import sys
import io
import urllib.request
import json
import hashlib
from pathlib import Path
from typing import Optional

# Set UTF-8 encoding on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

DICEBEAR_API = "https://api.dicebear.com/7.x/avataaars/svg"

def generate_seed(project_name: str) -> str:
    """Generate a deterministic seed from project name."""
    return hashlib.md5(project_name.encode()).hexdigest()[:8]

def fetch_avatar(project_name: str, seed: Optional[str] = None) -> str:
    """
    Fetch avatar SVG from DiceBear API.
    
    Args:
        project_name: Name of the project for seeding
        seed: Optional custom seed (defaults to hash of project_name)
    
    Returns:
        SVG string content
    """
    if seed is None:
        seed = generate_seed(project_name)
    
    # Build DiceBear URL with proper parameter encoding
    url = f"https://api.dicebear.com/7.x/avataaars/svg"
    
    # Build query parameters properly
    params = {
        'seed': seed,
        'backgroundColor': 'random',
        'scale': '80',
    }
    
    from urllib.parse import urlencode
    url_with_params = f"{url}?{urlencode(params)}"
    
    print(f"🎲 Generating avatar for: {project_name}")
    print(f"🔗 API Call: {url_with_params}\n")
    
    try:
        request = urllib.request.Request(url_with_params)
        request.add_header('User-Agent', 'Agent-Skill-Kit/1.0')
        with urllib.request.urlopen(request, timeout=10) as response:
            svg_content = response.read().decode('utf-8')
            return svg_content
    except urllib.error.HTTPError as e:
        print(f"⚠️  HTTP Error {e.code}: {e.reason}")
        # Return a simple fallback SVG with project name
        return generate_fallback_avatar(project_name)
    except Exception as e:
        raise Exception(f"Failed to fetch avatar: {e}")

def generate_fallback_avatar(project_name: str) -> str:
    """Generate a simple fallback SVG avatar."""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <rect width="200" height="200" fill="#667eea"/>
  <circle cx="100" cy="80" r="40" fill="#fff"/>
  <text x="100" y="150" font-size="24" fill="#fff" text-anchor="middle" font-weight="bold">
    {project_name[:3].upper()}
  </text>
</svg>"""

def save_avatar(svg_content: str, output_path: str = "avatar.svg") -> None:
    """Save SVG to file."""
    with open(output_path, 'w') as f:
        f.write(svg_content)
    print(f"✅ Avatar saved to: {output_path}")

def main(project_name: str, output_path: str = "avatar.svg"):
    """Main execution function."""
    print(f"🤖 Agent-Identity Generator\n")
    
    svg_content = fetch_avatar(project_name)
    save_avatar(svg_content, output_path)
    
    # Also return SVG for display
    print(f"\n📊 SVG Avatar Content:\n")
    print(svg_content)

if __name__ == "__main__":
    import sys
    project_name = sys.argv[1] if len(sys.argv) > 1 else "Agent-Skill-Kit"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "avatar.svg"
    main(project_name, output_path)
