# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Agent-Skill-Kit
Builds a standalone executable for Windows
"""

# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Agent-Skill-Kit
Builds a standalone executable for Windows
Workaround: Disable Rich unicode rendering in bundled exe
"""

import sys
from PyInstaller.utils.hooks import collect_data_files

# Collect all Rich package files (not just specific ones)
datas = [
    ('skills', 'skills'),
    ('requirements.txt', '.'),
]

# Collect all data files from rich module
try:
    from pathlib import Path
    rich_path = Path(__import__('rich').__file__).parent
    datas.append((str(rich_path), 'rich'))
except:
    pass

a = Analysis(
    ['core/ask.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'rich',
        'rich.console',
        'rich.table',
        'rich.panel',
        'rich.progress',
        'yaml',
        'urllib3',
        'requests',
    ],
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
