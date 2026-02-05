# 🚀 GitHub Releases Guide

This guide shows how to create official releases with all 3 distribution options.

---

## 📋 Pre-Release Checklist

Before creating a release:

- [ ] Update version in `setup.py` (e.g., `2.0.0` → `2.1.0`)
- [ ] Update `README.md` with new features
- [ ] Test all 3 distribution methods locally
- [ ] Commit all changes: `git commit -am "release: v2.1.0"`
- [ ] Tag the release: `git tag v2.1.0`
- [ ] Push: `git push origin main && git push origin v2.1.0`

---

## 🏗️ Build Distributions

Run the build script to create all distributions:

```bash
python build.py
```

This creates:
- `dist/ask.exe` - Standalone executable (~80MB)
- `dist/agent_skill_kit-2.1.0-py3-none-any.whl` - pip package (~5MB)
- `dist/agent-skill-kit-2.1.0.tar.gz` - Source archive

---

## 📤 Create GitHub Release

### Via GitHub Web Interface

1. Go to **Code** tab
2. Click **Releases** (right sidebar)
3. Click **"Create a new release"**
4. Fill in:
   - **Tag version**: `v2.1.0`
   - **Release title**: `Agent-Skill-Kit v2.1.0`
   - **Description**: (see template below)
5. **Attach files**: Drag & drop:
   - `ask.exe`
   - `agent_skill_kit-2.1.0-py3-none-any.whl`
   - `agent-skill-kit-2.1.0.tar.gz`
6. Click **"Publish release"**

### Via Command Line (GitHub CLI)

```bash
# Create and push tag
git tag v2.1.0
git push origin v2.1.0

# Create release with files
gh release create v2.1.0 dist/ask.exe dist/*.whl \
  --title "Agent-Skill-Kit v2.1.0" \
  --notes "See CHANGELOG.md for details"
```

---

## 📝 Release Description Template

```markdown
# Agent-Skill-Kit v2.1.0 - 2026 Edition

**Zero Config. Agent Native. Zero Maintenance.**

## 🎉 What's New

- [List major features]
- [Bug fixes]
- [Improvements]

## 📥 Installation

### Windows Users (Easiest)
Download `ask.exe` and run directly - no Python needed!

```bash
ask.exe dashboard
ask.exe run tech-pulse
```

### Python Developers
```bash
pip install agent_skill_kit-2.1.0-py3-none-any.whl
ask dashboard
```

### Source Installation
```bash
git clone https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-.git
pip install -e .
```

## 📚 Documentation

- [README](https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-#readme)
- [Distribution Guide](DISTRIBUTION.md)
- [Contributing](CONTRIBUTING.md)

## 🙏 Thanks

Built with ❤️ for AI agents everywhere.
```

---

## 🎯 Release Naming Convention

- **v2.0.0** - Major version (breaking changes)
- **v2.1.0** - Minor version (new features)
- **v2.1.1** - Patch version (bug fixes)

---

## 📊 Distribution Summary

When you create a release with all 3 options:

| Option | File | Users | Size |
|--------|------|-------|------|
| **Standalone** | `ask.exe` | Windows non-devs | ~80MB |
| **pip Package** | `*.whl` | Python devs | ~5MB |
| **Source** | `.tar.gz` | Contributors | ~1MB |

---

## ✅ After Release

1. **GitHub Actions**: Your daily Tech-Pulse workflow runs automatically
2. **PyPI** (optional): `twine upload dist/*.whl` to publish on PyPI
3. **Announce**: Share release on Twitter, Hacker News, etc.

---

## 🔗 Useful Links

- [GitHub Releases Docs](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
- [GitHub CLI Docs](https://cli.github.com/)
- [PyPI Publishing](https://packaging.python.org/tutorials/packaging-projects/)

Your Agent-Skill-Kit is now **production-ready for distribution**! 🚀
