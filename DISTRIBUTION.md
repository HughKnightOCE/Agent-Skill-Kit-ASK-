# 📦 Distribution Guide - Agent-Skill-Kit

Your ASK framework now supports **3 distribution methods** for different user types.

---

## 🚀 Quick Build

```bash
python build.py
```

This creates:
- `dist/ask.exe` - Standalone executable
- `dist/*.whl` - pip-installable package

---

## 📋 Distribution Options

### Option 1: Standalone Executable (.exe) - Best for Non-Developers

**For:** Windows users without Python

**Build:**
```bash
python build.py
```

**Distribute:**
- Share `dist/ask.exe` directly
- Users can run immediately: `ask.exe dashboard`
- No Python installation needed
- File size: ~50-100 MB (includes Python runtime)

**User Instructions:**
```
1. Download ask.exe
2. Run: ask.exe dashboard
3. Run skills: ask.exe run tech-pulse
```

---

### Option 2: pip Package (.whl) - Best for Python Developers

**For:** Python developers who use pip

**Build:**
```bash
python build.py
```

**Distribute:**
- Upload to PyPI (optional): `pip install agent-skill-kit`
- Or share wheel: `pip install agent-skill-kit.whl`

**User Installation:**
```bash
pip install agent-skill-kit
ask dashboard
ask run tech-pulse
```

**Features:**
- Installed as command-line tool
- Works across Windows/Mac/Linux
- Symlink entry point: `ask` command available globally

---

### Option 3: Source Distribution - Best for Developers

**For:** Contributors and advanced users

**Build:**
```bash
git clone https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-.git
cd Agent-Skill-Kit-ASK-
pip install -e .
```

**Usage:**
```bash
ask dashboard
ask run architect "your description"
```

**Developer Benefits:**
- Edit code directly
- Contributions easy
- Full source access

---

## 🔧 Build Process Details

### PyInstaller (.exe)
```bash
pyinstaller pyinstaller.spec --onefile
```
- Bundles Python + dependencies + code
- Creates single executable
- Windows users don't need Python

### Wheel (.whl)
```bash
python setup.py bdist_wheel
```
- Python package format
- Installs via pip
- Cross-platform compatible

---

## 📊 Comparison

| Method | Users | Size | Setup | Requirements |
|--------|-------|------|-------|--------------|
| **EXE** | Non-developers | ~80MB | Drag & drop | Windows only |
| **Wheel** | Python devs | ~5MB | `pip install` | Python 3.8+ |
| **Source** | Contributors | ~1MB | `git clone` | Python 3.8+ + git |

---

## 🎯 Recommended Distribution Strategy

1. **Primary:** Share `.exe` on GitHub Releases (easy for end users)
2. **Secondary:** Publish wheel to PyPI (convenient for developers)
3. **Developer:** Link to GitHub repo (for contributors)

---

## 📝 GitHub Release Checklist

When publishing a new version:

```bash
# 1. Update version in setup.py
# 2. Build distributions
python build.py

# 3. Create Git tag
git tag v2.0.0
git push origin v2.0.0

# 4. Create GitHub Release
# Upload: dist/ask.exe and dist/*.whl

# 5. (Optional) Publish to PyPI
twine upload dist/*.whl
```

---

## ✅ Verify Distribution Works

### Test .exe
```bash
dist/ask.exe dashboard
dist/ask.exe run tech-pulse
```

### Test .whl
```bash
pip install dist/agent_skill_kit-2.0.0-py3-none-any.whl
ask dashboard
ask run tech-pulse
```

---

## 🚀 Next Steps

1. Run `python build.py` to create distributions
2. Test both .exe and .whl
3. Upload to GitHub Releases
4. Share with users!

Your Agent-Skill-Kit is now **enterprise-ready for distribution**! 🎉
