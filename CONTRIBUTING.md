# Contributing to Agent-Skill-Kit

Thank you for your interest in contributing! ASK is built on community contributions.

## Creating a New Skill

### 1. Fork & Clone
```bash
git clone https://github.com/yourusername/Agent-Skill-Kit.git
cd Agent-Skill-Kit
```

### 2. Create Your Skill

```bash
mkdir -p skills/your-skill-name
cd skills/your-skill-name
```

### 3. Write `script.py`

Your script should:
- Have a `main()` function
- Accept command-line arguments via `sys.argv`
- Print clean, Markdown-formatted output
- Require **NO API keys** or handle free/keyless APIs
- Handle errors gracefully

**Example:**
```python
#!/usr/bin/env python3
"""Your skill description."""

def main(arg1, arg2=None):
    print("🎉 Your output here")

if __name__ == "__main__":
    import sys
    arg1 = sys.argv[1] if len(sys.argv) > 1 else "default"
    main(arg1)
```

### 4. Create `manifest.yaml`

```yaml
name: Your Skill Name
version: "1.0.0"
description: "What does this skill do?"

author: "Your Name"
category: "category"

requirements:
  - name: "python"
    version: ">=3.8"

api_keys_required: false
dependencies: []

usage:
  command: "python script.py"
  args_required: []

output_format: "markdown"

tags:
  - "keyless"
```

### 5. Test Locally

```bash
python ../../core/ask.py run your-skill-name arg1 arg2
python ../../core/ask.py dashboard
```

### 6. Submit PR

Include:
- ✅ Working skill
- ✅ manifest.yaml
- ✅ Usage example
- ✅ Clear description

## Skill Guidelines

### ✅ Good Skill Qualities
- Uses **local logic** primarily
- Leverages **free, keyless APIs** (HackerNews, DiceBear, etc.)
- Outputs **clean Markdown**
- **No interactive prompts** (AI-friendly)
- **Minimal dependencies**
- **Fast execution** (<5s ideally)

### ❌ What NOT to Do
- Don't require API keys
- Don't require sign-ups
- Don't output JSON (use Markdown)
- Don't have complex setup
- Don't make blocking network calls

## Code Style

- Python 3.8+
- Type hints where applicable
- Docstrings for functions
- Clean, readable code
- Proper error handling

## Testing Your Skill

```bash
# Check it loads
python core/ask.py dashboard

# Run with test args
python core/ask.py run your-skill test

# Verify output is readable
```

---

**Questions?** Open an issue or ask in discussions.

**Let's build the future of local AI tools together! 🚀**
