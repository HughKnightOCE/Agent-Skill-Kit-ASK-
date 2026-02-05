# 🖥️ Agent-Skill-Kit Desktop GUI

A professional PyQt6 desktop application for managing and executing ASK skills with a modern, intuitive interface.

## Features

✨ **Beautiful Interface**
- Modern desktop application built with PyQt6
- Intuitive skill browser and executor
- Dark-mode friendly styling

🎯 **Skill Management**
- Browse all available skills with descriptions
- Search and filter skills
- View detailed skill information
- See API key requirements

⚡ **Execution**
- Execute skills with custom arguments
- Real-time output display
- Professional execution dialog
- Error handling and feedback

📊 **Dashboard**
- View system statistics
- Track skill categories
- See free vs paid API skills
- Execution history tracking

📜 **History**
- Track all skill executions
- View execution timestamp
- Clear history as needed

## Installation

### Via pip
```bash
pip install agent-skill-kit
ask-gui  # Launch the GUI
```

### From source
```bash
git clone https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-.git
cd "Agent-Skill-Kit-ASK-"
pip install -e .
ask-gui
```

### Standalone Executable
Download pre-built executable from [Releases](https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-/releases):
```bash
ask-gui.exe  # Windows
./ask-gui    # macOS/Linux
```

## Building Standalone Executable

Requires: PyInstaller

```bash
pip install pyinstaller
pyinstaller pyinstaller_gui.spec
```

Output: `dist/ask-gui/ask-gui.exe` (Windows) or equivalent

## Usage

### Launch Application
```bash
ask-gui
```

### Main Interface
1. **Left Panel**: Browse and search all available skills
2. **Details Tab**: View skill information and execute
3. **History Tab**: Track previous executions
4. **Dashboard Tab**: View system statistics

### Running a Skill
1. Click a skill in the list
2. Review skill details in the Details tab
3. Click "▶ Run Selected Skill"
4. Fill in any required arguments
5. Click "▶ Execute Skill"
6. View real-time output

### Navigation
- **Search**: Type in "🔍 Search Skills" to filter
- **Details**: Click skill name to view full info
- **History**: View past executions and timestamps
- **Dashboard**: See overall statistics

## Features

### Skill Details
- Skill name and version
- Full description
- API key requirements
- Required arguments with types
- Category information

### Execution
- Custom argument input fields
- Real-time output streaming
- Error messages
- Execution status indicator

### History
- Timestamped execution log
- Skill name and arguments
- Success/failure status
- Clear history button

### Dashboard
- Total skills count
- Free skills count
- Skill categories list
- System information

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Enter` | Execute selected skill |
| `Escape` | Close dialog |
| `Ctrl+F` | Focus search |

## Troubleshooting

### GUI Won't Launch
```bash
# Verify installation
ask --help  # CLI should work first

# Reinstall GUI dependencies
pip install --upgrade PyQt6
ask-gui
```

### Missing Skills
```bash
# Verify skills are installed
ask dashboard

# Check skills directory
python -c "from core.ask import SkillManager; print(SkillManager().skills_dir)"
```

### PyQt6 Issues on Linux
```bash
# Install dependencies
sudo apt-get install python3-pyqt6 libqt6gui6
pip install PyQt6
```

## Screenshots

(Add screenshots here)

## Architecture

```
gui/
├── main.py              # Main application window
├── __init__.py          # Package initialization

Core Integration:
├── SkillManager         # Skill loading and execution
├── Thread Execution     # Non-blocking skill runs
├── Live Output          # Real-time result display
```

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md)

## License

MIT - See [LICENSE](../LICENSE)

## Support

- 📖 [Documentation](https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-)
- 🐛 [Report Issues](https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-/issues)
- 💬 [Discussions](https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-/discussions)
