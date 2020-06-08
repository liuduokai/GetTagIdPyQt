# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['callMainWindow.py'],
             pathex=['C:\\projects\\python\\GetTagIdPyQt'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries+[('oraociei11.dll','oraociei11.dll','BINARY')],
          a.binaries+[('oci.dll','oci.dll','BINARY')],
          a.zipfiles,
          a.datas,
          [],
          name='callMainWindow',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='C:\\projects\\python\\GetTagIdPyQt\\angh9-giaqj-002.ico')
