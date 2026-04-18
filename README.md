# 🤖 Agent-Skill-Kit (ASK) v2.0

> **Zero API Keys. Zero Signups. Zero Friction.**  
> **Agent-Native. MCP-Ready. Living & Breathing.**  
> Local-first skills framework for AI agents. Clone. Run. Integrate.

[![GitHub Stars](https://img.shields.io/github/stars/HughKnightOCE/Agent-Skill-Kit-ASK-?style=flat-square)](https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-)
[![GitHub License](https://img.shields.io/github/license/HughKnightOCE/Agent-Skill-Kit-ASK-?style=flat-square)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue?style=flat-square)](https://www.python.org/)
[![Downloads](https://img.shields.io/github/downloads/HughKnightOCE/Agent-Skill-Kit-ASK-/total?style=flat-square)](https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-/releases)

---

## 🚀 Today's Agent Intelligence

> **Last Updated:** April 18, 2026

### 📊 Top 5 Trending Tech Stories

**#1. Category Theory Illustrated – Orders**
- 🔗 [Read on HackerNews](https://abuseofnotation.github.io/category-theory-illustrated/04_order/)
- 👤 By boris_m | 📈 67 points | 💬 13 comments

**#2. Amiga Graphics**
- 🔗 [Read on HackerNews](https://amiga.lychesis.net/)
- 👤 By sph | 📈 67 points | 💬 4 comments

**#3. Claude Design**
- 🔗 [Read on HackerNews](https://www.anthropic.com/news/claude-design-anthropic-labs)
- 👤 By meetpateltech | 📈 1047 points | 💬 683 comments

**#4. Michael Rabin Has Died**
- 🔗 [Read on HackerNews](https://en.wikipedia.org/wiki/Michael_O._Rabin)
- 👤 By tkhattra | 📈 40 points | 💬 1 comments

**#5. Show HN: I made a calculator that works over disjoint sets of intervals**
- 🔗 [Read on HackerNews](https://victorpoughon.github.io/interval-calculator/)
- 👤 By fouronnes3 | 📈 156 points | 💬 28 comments



> *This section is auto-updated daily with trending tech intelligence.*








































































## ⚡ What is ASK?

**Agent-Skill-Kit** is a modern, AI-native framework that gives agents (Claude, Copilot, custom bots) **local, keyless superpowers** through the Model Context Protocol (MCP).

ASK provides **self-contained skills** that run on your machine using:
- ✅ **Local logic** only (no cloud required)
- ✅ **FREE public APIs** (no auth, no keys)
- ✅ **MCP Integration** (native agent support)
- ✅ **Beautiful Live CLI** (professional TUI)
- ✅ **YAML manifests** (easy skill discovery)
- ✅ **Dynamic skill generation** (The Architect)

Think of it as a "turbo-charged plugin system for AI agents—2026 edition."

---

## ⚡ Quick Start (30 seconds)

```bash
# Install from GitHub
pip install git+https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-.git

# View available skills  
ask dashboard

# Run a skill
ask run tech-pulse
ask run repo-visualizer
ask run architect "Your idea"
```

**That's it!** No `.env` files. No API key hunting. No OAuth redirects.

---

## 📥 Installation Options

Choose the option that fits your needs:

### **Option 1: pip Package - Recommended (Works everywhere)**
Best for: All users (Windows, Mac, Linux)

```bash
# Install from GitHub
pip install git+https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-.git

# Or install from wheel file
pip install agent_skill_kit-2.0.0-py3-none-any.whl

# Then use the global command
ask dashboard
ask run tech-pulse
ask run repo-visualizer
```

### **Option 2: Source Installation - Best for Contributors**
Best for: Developers, customization, contributing

```bash
git clone https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-.git
cd Agent-Skill-Kit-ASK-
pip install -e .

# Use the global command
ask dashboard
ask run architect "Convert CSV to JSON"
```

### **Option 3: Desktop GUI - Modern Interface**
Best for: Visual users, no command-line needed

```bash
# Install with GUI support
pip install git+https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-.git

# Launch the beautiful desktop application
ask-gui
```

This opens a professional PyQt6 desktop application with:
- 🎨 Modern, intuitive interface
- 🔍 Skill browser and search
- 📊 Real-time execution dashboard  
- 📜 Execution history tracking
- ⚡ One-click skill execution with argument forms

[Learn more about the GUI →](gui/README.md)

### **Option 4: Run Source Directly - No Installation**
Best for: Quick testing, trying it out

```bash
git clone https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-.git
cd Agent-Skill-Kit-ASK-

# Run directly via CLI
ask dashboard
ask run tech-pulse
ask run architect "Your skill description"

# Or launch GUI (requires PyQt6)
pip install PyQt6
ask-gui
```

### **Option 5: Standalone Executable - Zero Dependencies**
Best for: No Python installed, portable use

Download pre-built executables from [Releases](https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-/releases):

- **Windows**: `ask-gui.exe` - Double-click to run
- **macOS**: `ask-gui` - Run from terminal
- **Linux**: `ask-gui` - Run from terminal

No Python installation required!

### **Windows Command Prompt Troubleshooting**

If `ask` doesn't work in Command Prompt (cmd), use one of these alternatives:

**Option A: Use PowerShell instead** (Recommended)
```powershell
ask dashboard
ask run tech-pulse
ask-gui  # GUI also works great in PowerShell
```

**Option B: Use Python directly** (Works everywhere)
```cmd
python -m core.ask dashboard
python -m core.ask run tech-pulse
```

**Option C: Add Scripts to PATH manually**
```cmd
setx PATH "%PATH%;%APPDATA%\Python\Python314\Scripts"
```
Then restart Command Prompt and try `ask` again.

---

## 📦 What's Included?

### ✨ **V2.0 Features**

#### 🔌 **MCP Server Integration**
Skills are now exposed as **native MCP tools** via `core/mcp_gateway.py`. Claude and Copilot can discover and execute skills directly without custom integration.

```python
# Claude can now see all skills as native tools
python core/mcp_gateway.py
```

#### 🏗️ **The Architect Skill**
Generate new skills from natural language descriptions. The Architect creates skeleton Python scripts and YAML manifests instantly.

```bash
ask run architect "Convert CSV to JSON format"
```

#### 💫 **Living README**
GitHub Actions automatically run Tech-Pulse every 24 hours and update this README's "Today's Agent Intelligence" section, proving the repo is alive and functional.

#### 🎨 **High-End Terminal UI**
Enhanced TUI with:
- ASCII art banner (ASK-2026)
- System health dashboard
- Live progress displays
- Professional color-coded output

#### 🖥️ **Desktop GUI Application (NEW!)**
Modern PyQt6 desktop interface featuring:
- **Skill Browser** - Search and filter all available skills
- **Visual Executor** - Execute skills with beautiful form inputs
- **Real-Time Output** - Watch skill execution live
- **History Tracking** - Review past skill executions
- **Dashboard** - See system statistics and skill categories
- **Professional Design** - Polished, native desktop application feel

Launch with: `ask-gui`

---

### 🎯 **Four Zero-Config Skills**

#### 1. **Repo-Visualizer** 📊
Generates **Mermaid.js class diagrams** of your project structure instantly.

```bash
ask run repo-visualizer /path/to/project
```

**Output:** A clean Mermaid diagram ready to paste into documentation or feed to AI agents.

```
graph TD
    Root["MyProject"]
    Root --> skills["📁 skills"]
    Root --> core["📁 core"]
    skills --> visualizer["📁 repo-visualizer"]
```

---

#### 2. **Agent-Identity** 🎭
Generates a **unique SVG avatar** for your project using the free DiceBear API.

```bash
ask run agent-identity "Agent-Skill-Kit"
```

**Output:** A beautiful, deterministic SVG avatar saved to disk and displayed.

```svg
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <!-- Unique avatar based on project name -->
</svg>
```

---

#### 3. **Tech-Pulse** 🔥
Fetches **top 5 trending tech stories** from HackerNews so your AI agent stays contextually aware.

```bash
ask run tech-pulse
```

**Output:** Markdown-formatted stories with links, scores, and comment counts.

```
#1. Breakthrough in AI Reasoning Model
- 🔗 URL: https://news.ycombinator.com/item/...
- 👤 Author: username
- 📈 Score: 1,234 | 💬 Comments: 456
```

---

#### 4. **The Architect** 🏗️
**NEW!** Generate new skills from descriptions. The Architect creates starter templates automatically.

```bash
ask run architect "Analyze code complexity"
```

**Output:** A complete skill directory with `script.py` and `manifest.yaml`.

---

## 🎯 The Philosophy: **Agent-Native + MCP-Ready**

ASK is built **specifically for AI agents.** Each skill outputs:

1. **Clean Markdown** (AI-readable format)
2. **Structured data** (JSON, YAML in comments)
3. **Minimal noise** (no interactive prompts)
4. **Error handling** (graceful failures)

### Perfect for:
- 🤖 **Claude Code** - MCP integration for native skill access
- 🧠 **GitHub Copilot CLI** - Custom MCP commands
- 🔧 **Custom agents** - Extend with dynamic skill generation
- 📡 **LLM chains** - Multi-step workflows without external APIs
- 🏗️ **AI frameworks** - Drop-in MCP server for any agent

---

## 🔧 CLI Manager: `ask` (2026 Edition)

The **high-performance TUI** with ASK-2026 styling and live displays.

```bash
# Dashboard with system health (NEW!)
ask dashboard

# Run a skill with live progress
ask run <skill-name> [args...]

# System diagnostics
ask doctor

# Help
ask help
```

**Features:**
- ✨ ASCII art banner (ASK-2026)
- 📊 System health dashboard (Python version, Git status, dependencies)
- 🎬 Live progress spinners
- 🎨 Professional color-coded output

---

## 🌐 MCP Server Integration (NEW!)

Expose all skills as native MCP tools:

```python
from core.mcp_gateway import SkillMCPServer

# Claude, Copilot, and other agents see skills as native tools
server = SkillMCPServer()
await server.run()
```

Claude can now:
```
User: "Use the repo-visualizer tool to analyze my project"
Claude: [invokes repo-visualizer via MCP] → sees complete output
```

---

## 🏗️ The Architect: Generate New Skills (NEW!)

Turn ideas into skills instantly:

```bash
# Create from natural language
ask run architect "Convert YAML to JSON"

# Output:
# ✅ Created: skills/convert-yaml-to-json/
# ✅ Created: script.py
# ✅ Created: manifest.yaml
# 🚀 Next: Edit and run your new skill!
```

---

## 💫 Living README (NEW!)

This README is **automatically updated every 24 hours** with trending tech intelligence via GitHub Actions. The "Today's Agent Intelligence" section proves ASK is:
- ✅ Alive and functional
- ✅ Running real workflows
- ✅ Connected to real data
- ✅ Production-grade

---

## 🔧 CLI Manager: `ask.py`

The **Rust-inspired TUI** powered by `rich`.

---

## 📁 Project Structure

```
Agent-Skill-Kit/
├── core/
│   └── ask.py                 # ⭐ Main CLI manager
├── skills/
│   ├── repo-visualizer/
│   │   ├── script.py          # Implementation
│   │   └── manifest.yaml      # Metadata
│   ├── agent-identity/
│   │   ├── script.py
│   │   └── manifest.yaml
│   └── tech-pulse/
│       ├── script.py
│       └── manifest.yaml
├── README.md                  # You are here
├── requirements.txt           # Dependencies
└── .github/
    └── workflows/             # CI/CD (optional)
```

---

## 🛠️ Dependencies

Minimal and lightweight:

```
PyYAML>=6.0        # For manifest parsing
rich>=12.0         # For beautiful CLI
```

**Installation:**

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing: Add Your Own Skill

ASK is designed for **community contributions**. Creating a skill takes **5 minutes**.

### Skill Template

Each skill needs:
1. **`script.py`** - The logic
2. **`manifest.yaml`** - Metadata

### Step 1: Create the Skill Directory

```bash
mkdir -p skills/my-awesome-skill
cd skills/my-awesome-skill
```

### Step 2: Write `script.py`

```python
#!/usr/bin/env python3
"""My awesome skill that does X without any API key."""

def main(arg1, arg2=None):
    """Main execution function."""
    print("🎉 My skill output")
    print("✅ Ready for AI agents!")

if __name__ == "__main__":
    import sys
    arg1 = sys.argv[1] if len(sys.argv) > 1 else "default"
    main(arg1)
```

### Step 3: Write `manifest.yaml`

```yaml
name: My Awesome Skill
version: "1.0.0"
description: "Does X without requiring any API keys"

author: "Your Name"
category: "utility"

requirements:
  - name: "python"
    version: ">=3.8"

api_keys_required: false
dependencies: []

usage:
  command: "python script.py"
  args_required:
    - name: "arg1"
      description: "Description of argument"

output_format: "markdown"

tags:
  - "keyless"
  - "local"
```

### Step 4: Test It

```bash
python ../core/ask.py dashboard
python ../core/ask.py run my-awesome-skill
```

### Step 5: Submit a PR

We love contributions! Submit a PR with:
- ✅ Working skill code
- ✅ Proper manifest.yaml
- ✅ Usage example in description
- ✅ No external API keys required

---

## 🎁 Use Cases

### For Individual Developers
```bash
# Morning ritual: Check tech news while coding
python ask.py run tech-pulse

# Visualize your codebase for documentation
python ask.py run repo-visualizer
```

### For AI Agents (Claude Code, Copilot CLI)
```python
# In your agent flow
subprocess.run(["python", "ask.py", "run", "repo-visualizer"])
# Parse the Mermaid output and feed to LLM
```

### For Teams
```bash
# Onboarding: Generate project overview
python ask.py run repo-visualizer /monorepo/service-a

# Team branding: Create consistent avatar
python ask.py run agent-identity "TeamName"
```

---

## 🔐 Security & Privacy

✅ **All processing is local** - No data leaves your machine (except API calls)  
✅ **No authentication required** - Zero credentials to manage  
✅ **Open source** - Review the code, audit the logic  
✅ **Minimal dependencies** - Less code = less risk  

---

## 📊 Roadmap

- [ ] More skills:
  - `code-metrics`: Analyze code complexity
  - `dependency-graph`: Visualize package dependencies
  - `api-docs-generator`: Auto-generate OpenAPI specs
- [ ] Skill marketplace: Discover community skills
- [ ] Skill templates: One-click skill generation
- [ ] Agent integrations: Official Claude Code plugin
- [ ] Performance: Caching layer for API calls

---

## 🐛 Troubleshooting

### "ImportError: No module named 'rich'"
```bash
pip install rich pyyaml
```

### "Skill not found"
```bash
ask dashboard  # Check installed skills
```

### "API call failed"
Some free APIs have rate limits. Try again in a few seconds.

---

## 📄 License

MIT License - Free to use, modify, and distribute.

---

## 🌟 Show Your Support

- ⭐ **Star this repo** if you find it useful
- 🔗 **Share it** with other developers building AI tools
- 📝 **Contribute** skills for the community
- 💬 **Open issues** with feature requests

---

## 🤖 Made for Agents, By Developers

**Agent-Skill-Kit** is built with the belief that AI agents should have **powerful, local tools** without the friction of OAuth, API keys, and sign-ups.

Whether you're building a personal automation tool, a team assistant, or integrating with Claude Code, ASK is your **zero-friction** gateway to local intelligence.

---

**Built with ❤️ for the AI-native future.**

```
█████████████████████████████████████████████████████
█ Agent-Skill-Kit: Local Power. Zero Keys. Pure Joy. █
█████████████████████████████████████████████████████
```
