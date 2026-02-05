#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build script for Agent-Skill-Kit
Creates both:
1. Standalone .exe (Windows)
2. pip-installable wheel
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
import io

# Fix encoding on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def run_cmd(cmd, description):
    """Run a command and report status."""
    print(f"\n📦 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - Success!")
            return True
        else:
            print(f"❌ {description} - Failed!")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ {description} - Error: {e}")
        return False

def main():
    print("""
    ╔══════════════════════════════════════════════╗
    ║  🤖 Agent-Skill-Kit Distribution Builder    ║
    ╚══════════════════════════════════════════════╝
    """)
    
    # Check if we're in the right directory
    if not os.path.exists('core/ask.py'):
        print("❌ Error: Must run from ASK project root directory")
        sys.exit(1)
    
    # Install build dependencies
    print("\n🔧 Installing build tools...")
    run_cmd(
        f"{sys.executable} -m pip install pyinstaller wheel setuptools",
        "Installing PyInstaller and wheel"
    )
    
    # Clean old builds
    print("\n🧹 Cleaning old builds...")
    for folder in ['build', 'dist']:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"   Removed {folder}/")
    
    # Build executable with PyInstaller
    print("\n" + "="*50)
    print("BUILDING STANDALONE EXECUTABLE (.exe)")
    print("="*50)
    
    if run_cmd(
        f"{sys.executable} -m PyInstaller pyinstaller.spec",
        "Building standalone executable"
    ):
        print("\n✅ Executable built: dist/ask.exe")
        print("   Users can run without Python installed!")
    
    # Build wheel for pip install
    print("\n" + "="*50)
    print("BUILDING PIP PACKAGE (.whl)")
    print("="*50)
    
    if run_cmd(
        f"{sys.executable} setup.py bdist_wheel",
        "Building wheel distribution"
    ):
        print("\n✅ Wheel built in dist/")
        print("   Users can install with: pip install agent-skill-kit.whl")
    
    # Summary
    print("\n" + "="*50)
    print("BUILD COMPLETE!")
    print("="*50)
    print("""
    Distribution options:
    
    1️⃣  Standalone .exe (for Windows users):
        ▸ Location: dist/ask.exe
        ▸ Usage: ask.exe dashboard
        ▸ No Python required!
    
    2️⃣  pip Package (for Python users):
        ▸ Location: dist/*.whl
        ▸ Install: pip install agent-skill-kit.whl
        ▸ Usage: ask dashboard
    
    3️⃣  Source Distribution (full package):
        ▸ git clone + pip install -e .
        ▸ Best for developers
    """)

if __name__ == '__main__':
    main()
