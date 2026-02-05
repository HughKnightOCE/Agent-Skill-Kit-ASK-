#!/usr/bin/env python3
"""
Setup script for Agent-Skill-Kit.
Installs dependencies and verifies the environment.
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a shell command and report status."""
    print(f"\n📦 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - Done!")
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
    ╔════════════════════════════════════════╗
    ║   🤖 Agent-Skill-Kit Setup Script     ║
    ╚════════════════════════════════════════╝
    """)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required!")
        sys.exit(1)
    
    print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Install requirements
    success = True
    success &= run_command(
        f"{sys.executable} -m pip install --upgrade pip",
        "Upgrading pip"
    )
    
    success &= run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Installing dependencies"
    )
    
    # Test CLI
    print(f"\n🧪 Testing CLI...")
    result = subprocess.run(
        [sys.executable, "core/ask.py", "help"],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print("✅ CLI test passed!")
    else:
        print("❌ CLI test failed!")
        print(result.stderr)
        success = False
    
    # Final message
    print(f"\n{'='*40}")
    if success:
        print("✅ Setup complete! You're ready to go!")
        print("\n🚀 Quick start:")
        print("   python core/ask.py dashboard")
        print("   python core/ask.py run repo-visualizer")
        print("   python core/ask.py doctor")
    else:
        print("⚠️  Setup completed with warnings.")
        print("   Please fix any errors above.")
    print(f"{'='*40}\n")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
