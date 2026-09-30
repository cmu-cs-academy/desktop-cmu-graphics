"""
Set up a tox zip environment: replace the installed pip distribution with the
zip distribution built from the same wheel.

tox has already installed the wheel under test -- one it built, or the one
passed with --installpkg -- and says where it is in TOX_PACKAGE. This builds a
zip distribution from that wheel with build/build.py, unpacks it into the
current directory (the environment's temp dir, which tox.ini puts on
PYTHONPATH), and uninstalls the wheel, so the tests can only import the zip
distribution's copy.
"""

import os
import shutil
import subprocess
import sys
import tempfile
import zipfile

repo_root = sys.argv[1]

wheel = os.environ['TOX_PACKAGE']
if os.pathsep in wheel:
    sys.exit(f'Expected one package in TOX_PACKAGE, got {wheel}')

zip_path = os.path.abspath('cmu_graphics_installer.zip')
with tempfile.TemporaryDirectory() as wheels_dir:
    shutil.copy(wheel, wheels_dir)
    subprocess.run(
        [
            sys.executable,
            os.path.join(repo_root, 'build', 'build.py'),
            '--wheels',
            wheels_dir,
            '--output',
            zip_path,
        ],
        check=True,
    )

uv = shutil.which('uv')
if uv is None:
    sys.exit(
        'uv was not found on PATH. tox-uv runs these environments with uv, '
        'and this script needs it to uninstall the pip distribution.'
    )
# --python pins the operation to the interpreter running this script rather
# than whatever uv would discover on its own.
subprocess.run(
    [uv, 'pip', 'uninstall', 'cmu-graphics', '--python', sys.executable], check=True
)

# build.py leaves its staging directory here; unpack the zip itself instead, so
# that it is what gets tested.
shutil.rmtree('cmu_graphics_installer')
with zipfile.ZipFile(zip_path) as zf:
    zf.extractall('.')
shutil.move(os.path.join('cmu_graphics_installer', 'cmu_graphics'), '.')
shutil.move(os.path.join('cmu_graphics_installer', 'cmu_cpcs_utils.py'), '.')
shutil.rmtree('cmu_graphics_installer')
