import os
import shutil
import subprocess
import sys

mode = sys.argv[1]
base_path = sys.argv[2]

def uv_pip(*args):
    """
    Run `uv pip` against this tox environment.

    tox-uv builds these environments with uv, which does not install pip into
    them, so this script can't shell out to pip. --python pins the operation to
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
    # Remove any old version installed. uv exits 0 when the package isn't
    # present, the same as `pip uninstall -y` did.
    uv_pip('uninstall', 'cmu-graphics')

    dist_dir = os.path.join(base_path, 'pypi_upload', 'dist')
    for path in os.listdir(dist_dir):
        if path.endswith('.whl'):
            uv_pip('install', os.path.join(dist_dir, path))
