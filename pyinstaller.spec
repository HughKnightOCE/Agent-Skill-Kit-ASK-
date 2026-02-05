# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Agent-Skill-Kit
Builds a standalone executable for Windows
"""

import sys
from PyInstaller.utils.hooks import collect_data_files, get_module_file_attribute

# Collect data files from Rich and PyYAML
datas = [
    ('skills', 'skills'),
    ('requirements.txt', '.'),
]

# Add Rich unicode data
rich_data = collect_data_files('rich')
datas.extend(rich_data)

a = Analysis(
    ['core/ask.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=['rich', 'yaml', 'rich._unicode_data'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludedimports=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ask',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
