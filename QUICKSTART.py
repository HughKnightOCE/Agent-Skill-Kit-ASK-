#!/usr/bin/env python3
"""
Quick reference guide generator.
Shows all available skills and commands.
"""

def generate_guide():
    guide = """
╔════════════════════════════════════════════════════════════════╗
║          🤖 Agent-Skill-Kit - Quick Reference                 ║
╚════════════════════════════════════════════════════════════════╝

INSTALLATION:
─────────────
python setup.py
pip install -r requirements.txt

QUICK START:
────────────
python core/ask.py dashboard              # View all skills
python core/ask.py run repo-visualizer    # Generate project diagram
python core/ask.py run agent-identity "MyProject"  # Create avatar
python core/ask.py run tech-pulse         # Get trending tech news
python core/ask.py doctor                 # Check dependencies

SKILLS OVERVIEW:
────────────────

1. repo-visualizer
   ├─ Generates Mermaid.js diagrams of project structure
   ├─ No API keys required
   └─ Usage: python core/ask.py run repo-visualizer [path]

2. agent-identity
   ├─ Creates unique SVG avatars via DiceBear API
   ├─ Uses free, public endpoint (no auth)
   └─ Usage: python core/ask.py run agent-identity "ProjectName"

3. tech-pulse
   ├─ Fetches top 5 trending stories from HackerNews
   ├─ Uses free, public API (no auth)
   └─ Usage: python core/ask.py run tech-pulse

KEY CONCEPTS:
─────────────
✅ Zero API Keys      - All skills work without authentication
✅ Local-First        - Processing happens on your machine
✅ Agent-Native       - Output formatted for AI consumption
✅ Modular            - Easy to add new skills
✅ Open Source        - MIT licensed, free to use

ADDING YOUR OWN SKILL:
──────────────────────
1. mkdir -p skills/my-skill
2. Create script.py (main execution logic)
3. Create manifest.yaml (metadata)
4. Test: python core/ask.py run my-skill
5. Submit PR to contribute!

FILE STRUCTURE:
───────────────
Agent-Skill-Kit/
├── core/ask.py                 # Main CLI manager
├── skills/
│   ├── repo-visualizer/
│   ├── agent-identity/
│   └── tech-pulse/
├── README.md                   # Full documentation
├── CONTRIBUTING.md             # Skill creation guide
├── setup.py                    # Installation script
└── requirements.txt            # Python dependencies

TROUBLESHOOTING:
────────────────
ImportError: rich/yaml
  → pip install -r requirements.txt

Skill not found
  → python core/ask.py dashboard

API errors
  → Some APIs rate-limit. Try again in a few seconds.

RESOURCES:
──────────
📖 Documentation: README.md
🤝 Contributing: CONTRIBUTING.md
⚙️  Skill Template: See skills/tech-pulse/
🐛 Issues: GitHub Issues

════════════════════════════════════════════════════════════════

Built for AI agents. Built by developers. Built for the future.

Repository: https://github.com/yourusername/Agent-Skill-Kit
License: MIT

════════════════════════════════════════════════════════════════
"""
    print(guide)

if __name__ == "__main__":
    generate_guide()
