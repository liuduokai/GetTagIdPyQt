# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['callMainWindow.py'],
             pathex=['E:\\PyProjects\\QT_test'],
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
          a.binaries+[('oraociei11.dll','oraociei11.dll','BINARY'),
          ('oci.dll','oci.dll','BINARY'),
          ('orasql11.dll','orasql11.dll','BINARY'),
          ('oraocci11.dll','oraocci11.dll','BINARY'),
          ('orannzsbb11.dll','orannzsbb11.dll','BINARY'),
          ('ociw32.dll','ociw32.dll','BINARY'),
          ('ocijdbc11.dll','ocijdbc11.dll','BINARY'),
          ('msvcr71.dll','msvcr71.dll','BINARY'),
          ('mfc71.dll','mfc71.dll','BINARY')],
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
          console=True )
