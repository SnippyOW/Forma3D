# PyInstaller spec: builds Forma.exe on Windows and Forma.app on macOS (native arm64 on Apple Silicon).
#   pyinstaller --noconfirm forma.spec
import sys

from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs, collect_submodules

block_cipher = None
IS_MAC = sys.platform == 'darwin'

# Qt modules Forma never uses; excluding them keeps the bundle small.
EXCLUDES = ['PySide6.QtWebEngineCore', 'PySide6.QtWebEngineWidgets', 'PySide6.QtWebEngineQuick',
            'PySide6.Qt3DCore', 'PySide6.Qt3DRender', 'PySide6.QtCharts', 'PySide6.QtDataVisualization',
            'PySide6.QtQuick', 'PySide6.QtQml', 'PySide6.QtPdf', 'PySide6.QtBluetooth',
            'PySide6.QtSql', 'PySide6.QtTest', 'tkinter', 'pytest']

a = Analysis(
    ['run_forma.py'],
    pathex=['.'],
    binaries=collect_dynamic_libs('wgpu'),     # wgpu-native (Vulkan / D3D12 / Metal)
    datas=[('forma/render/worker.py', 'forma/render'), ('forma/render/bake_worker.py', 'forma/render'),
           ('forma/render/layers_worker.py', 'forma/render'),
           ('forma/data/shader_nodes.json', 'forma/data'), ('forma/fbx_worker.py', 'forma'),
           ('plug-ins', 'plug-ins')] + collect_data_files('wgpu'),   # workers run by Blender; bundled plug-ins
    hiddenimports=['OpenGL.platform.win32', 'OpenGL.platform.darwin', 'OpenGL.arrays.numpymodule',
                   'OpenGL.arrays.ctypesarrays', 'OpenGL.arrays.numbers', 'OpenGL.arrays.strings',
                   'OpenGL.arrays.lists', 'OpenGL.arrays.nones']
                  + collect_submodules('wgpu.backends.wgpu_native') + ['wgpu.utils', 'cffi']
                  + collect_submodules('forma'),             # modes / tools imported on first use
    excludes=EXCLUDES,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz, a.scripts, [],
    exclude_binaries=True,
    name='Forma',
    console=False,
    argv_emulation=IS_MAC,
    target_arch=None,          # build for the host architecture (arm64 on Apple Silicon)
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(exe, a.binaries, a.datas, strip=False, upx=False, name='Forma')

if IS_MAC:
    app = BUNDLE(
        coll,
        name='Forma.app',
        bundle_identifier='org.forma.app',
        info_plist={
            'CFBundleName': 'Forma',
            'CFBundleDisplayName': 'Forma',
            'CFBundleShortVersionString': '0.1.0',
            'NSHighResolutionCapable': True,
            'LSMinimumSystemVersion': '12.0',
            'CFBundleDocumentTypes': [{
                'CFBundleTypeName': 'Forma Scene',
                'CFBundleTypeExtensions': ['forma'],
                'CFBundleTypeRole': 'Editor',
            }],
        },
    )
