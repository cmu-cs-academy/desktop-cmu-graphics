import os
import shutil
import subprocess
import sys

mode = sys.argv[1]
base_path = sys.argv[2]

def uv_pip(*args):
    """
    Run `uv pip` against this tox environment.

    --python pins the operation to
    the interpreter running this script rather than whatever uv would discover
    on its own. UV_FIND_LINKS comes from tox.ini's set_env and is inherited
    here, so uv resolves cmu-graphics-helpers from the locally built wheel.
    """
    uv = shutil.which('uv')
    if uv is None:
        sys.exit(
            'uv was not found on PATH. tox-uv runs these environments with uv, '
            'and this script needs it to install the built package.'
        )
    subprocess.run([uv, 'pip', *args, '--python', sys.executable], check=True)

if mode == 'zip':
    cmd = f"{sys.executable} -m zipfile -e {os.path.join(base_path, 'cmu_graphics_installer.zip')} ."
    subprocess.run(cmd, check=True, shell=True)
    shutil.move(os.path.join('cmu_graphics_installer', 'cmu_graphics'), '.')
    shutil.move(os.path.join('cmu_graphics_installer', 'cmu_cpcs_utils.py'), '.')
    shutil.rmtree('cmu_graphics_installer')
else:
    # Remove any old version installed
    uv_pip('uninstall', 'cmu-graphics')

    dist_dir = os.path.join(base_path, 'pypi_upload', 'dist')
    for path in os.listdir(dist_dir):
        if path.endswith('.whl'):
            # --no-cache because this install is what pulls cmu-graphics-helpers
            # out of UV_FIND_LINKS, and uv caches wheels from there by name and
            # version, ignoring size and mtime -- so a cached wheel from an
            # earlier build of the same version would win over the one just
            # built.
            uv_pip('install', '--no-cache', os.path.join(dist_dir, path))
