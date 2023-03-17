# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:\\Users\\Uzair Aalam\\Desktop\\Python3Code\\main.py'],
    pathex=['C:\\Users\\Uzair Aalam\\Desktop\\Python3Code'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

a.datas+=[('.\\Pictures\\icon1.ico','C:\\Users\\Uzair Aalam\\Desktop\\Python3Code\\Pictures\\icon1.ico','DATA'),
          ('.\\Pictures\\slopeCondition1.gif','C:\\Users\\Uzair Aalam\\Desktop\\Python3Code\\Pictures\\slopeCondition1.gif','DATA'),
          ('.\\Pictures\\slopeCondition2.gif','C:\\Users\\Uzair Aalam\\Desktop\\Python3Code\\Pictures\\slopeCondition2.gif','DATA'),
	  ('.\\Pictures\\slopeCondition3.gif','C:\\Users\\Uzair Aalam\\Desktop\\Python3Code\\Pictures\\slopeCondition3.gif','DATA'),
	  ('.\\Pictures\\slopeCondition4.gif','C:\\Users\\Uzair Aalam\\Desktop\\Python3Code\\Pictures\\slopeCondition4.gif','DATA'),
	  ('.\\Pictures\\slopeCondition5.gif','C:\\Users\\Uzair Aalam\\Desktop\\Python3Code\\Pictures\\slopeCondition5.gif','DATA')]
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='C:\\Users\\Uzair Aalam\\Desktop\\Python3Code\\Pictures\\icon2.ico'
)
