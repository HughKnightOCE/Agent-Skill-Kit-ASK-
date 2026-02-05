#!/usr/bin/env python3
"""
Setup configuration for Agent-Skill-Kit.
Allows installation via: pip install .
Or: pip install agent-skill-kit
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_file.exists():
    requirements = [
        line.strip()
        for line in requirements_file.read_text(encoding="utf-8").split("\n")
        if line.strip() and not line.startswith("#")
    ]

setup(
    name="agent-skill-kit",
    version="2.0.0",
    description="Zero-config, agent-native skill framework with MCP integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Hugh Knight",
    author_email="hugh@example.com",
    url="https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-",
    license="MIT",
    packages=find_packages(include=["core", "skills"]),
    package_data={
        "": ["*.yaml", "*.yml", "*.py"],
        "skills": ["*/*.yaml", "*/*.py"],
    },
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ask=core.ask:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    python_requires=">=3.8",
    keywords="agent skills mcp claude copilot automation",
    project_urls={
        "Documentation": "https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-#readme",
        "Source": "https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-",
        "Issues": "https://github.com/HughKnightOCE/Agent-Skill-Kit-ASK-/issues",
    },
)
