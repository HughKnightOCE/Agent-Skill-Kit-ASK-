#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The Architect Skill: Generates skeleton skills from natural language descriptions.
Uses AI-style reasoning to create new skill templates with script.py and manifest.yaml.
"""

import sys
import io
import os
from pathlib import Path
from typing import Tuple

# Set UTF-8 encoding on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def slugify(text: str) -> str:
    """Convert text to slug format (lowercase, dashes)."""
    return text.lower().replace(' ', '-').replace('_', '-')


def generate_skill_template(description: str, skill_name: str) -> Tuple[str, str]:
    """
    Generate Python script and YAML manifest from description.
    Uses pattern matching to infer skill requirements.
    """
    
    # Analyze description to infer requirements
    description_lower = description.lower()
    requires_network = any(word in description_lower for word in ['api', 'fetch', 'download', 'web', 'http', 'remote'])
    requires_files = any(word in description_lower for word in ['file', 'scan', 'read', 'write', 'directory', 'folder'])
    requires_parsing = any(word in description_lower for word in ['parse', 'extract', 'format', 'convert', 'transform'])
    
    # Generate Python script template
    script_template = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
{skill_name.replace('-', ' ').title()} Skill
{description}
"""

import sys
import io

# Set UTF-8 encoding on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def main(input_arg: str = None):
    """Main execution function."""
    if input_arg:
        print(f"🚀 Processing: {{input_arg}}")
    else:
        print(f"🚀 {skill_name.replace('-', ' ').title()} is running")
    
    # TODO: Implement your skill logic here
    # This is a skeleton - add your code below
    
    print("✅ Skill execution completed successfully")


if __name__ == "__main__":
    import sys
    input_arg = sys.argv[1] if len(sys.argv) > 1 else None
    main(input_arg)
'''
    
    # Generate YAML manifest
    category = "development" if requires_files else "information" if requires_network else "utility"
    
    manifest_template = f'''name: {skill_name.replace('-', ' ').title()}
version: "1.0.0"
description: "{description}"

author: "Agent-Skill-Kit Contributors"
category: "{category}"

requirements:
  - name: "python"
    version: ">=3.8"

api_keys_required: false
dependencies: []

usage:
  command: "python script.py"
  args_optional:
    - name: "input"
      description: "Input argument"
      example: "python script.py example"

output_format: "markdown"

tags:
  - "keyless"
  - "local"
  - "{category}"
'''
    
    return script_template, manifest_template


def main(description: str, output_dir: str = "."):
    """Generate a new skill from natural language description."""
    
    print(f"🏗️  The Architect: Building New Skills\n")
    print(f"📝 Description: {description}\n")
    
    # Derive skill name from description
    words = description.split()[:3]
    skill_name = slugify('-'.join(words))
    
    # Create skill directory
    skill_path = Path(output_dir) / "skills" / skill_name
    
    if skill_path.exists():
        print(f"⚠️  Skill directory already exists: {skill_path}")
        return 1
    
    try:
        skill_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {skill_path}\n")
        
        # Generate and save script
        script_content, manifest_content = generate_skill_template(description, skill_name)
        
        script_file = skill_path / "script.py"
        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(script_content)
        script_file.chmod(0o755)
        print(f"✅ Created: {script_file.name}")
        
        # Save manifest
        manifest_file = skill_path / "manifest.yaml"
        with open(manifest_file, 'w', encoding='utf-8') as f:
            f.write(manifest_content)
        print(f"✅ Created: {manifest_file.name}\n")
        
        print(f"🎉 New skill created successfully!")
        print(f"\n📍 Skill Location: {skill_path}")
        print(f"\n🚀 Next Steps:")
        print(f"   1. Edit {script_file}")
        print(f"   2. Run: ask run {skill_name}")
        print(f"   3. Update manifest.yaml as needed\n")
        
        return 0
    
    except Exception as e:
        print(f"❌ Error creating skill: {e}")
        return 1


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python script.py '<skill-description>' [output-dir]")
        print("\nExample:")
        print("  python script.py 'Convert CSV to JSON format'")
        print("  python script.py 'Analyze code quality metrics' /path/to/project")
        sys.exit(1)
    
    description = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    
    sys.exit(main(description, output_dir))
