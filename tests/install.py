import email.parser
import os
import re
import shutil
import subprocess
import sys
import zipfile

mode = sys.argv[1]
base_path = sys.argv[2]

def uv_pip(*args):
    """
    Run `uv pip` against this tox environment.

    --python pins the operation to
    the interpreter running this script rather than whatever uv would discover
    on its own. UV_FIND_LINKS comes from tox.ini's set_env and is inherited
    here, so uv resolves cmu-graphics-helpers from the committed wheels.
    """
    uv = shutil.which('uv')
    if uv is None:
        sys.exit(
            'uv was not found on PATH. tox-uv runs these environments with uv, '
            'and this script needs it to install the built package.'
        )
    subprocess.run([uv, 'pip', *args, '--python', sys.executable], check=True)

def pypi_requirements(wheel_path):
    """
    The wheel's Requires-Dist entries, other than cmu-graphics-helpers, which
    has to come from the committed wheels instead.
    """
    with zipfile.ZipFile(wheel_path) as wheel:
        metadata_path = next(
            name for name in wheel.namelist()
            if name.endswith('.dist-info/METADATA')
        )
        metadata = email.parser.Parser().parsestr(
            wheel.read(metadata_path).decode('utf-8')
        )

    requirements = []
    for requirement in metadata.get_all('Requires-Dist', []):
        name = re.match(r'[A-Za-z0-9._-]+', requirement).group()
        # Normalize the name, as in PEP 503
        if re.sub(r'[-_.]+', '-', name).lower() != 'cmu-graphics-helpers':
            requirements.append(requirement)
    return requirements

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
            wheel_path = os.path.join(dist_dir, path)
            # The --no-index install below can only see the committed
            # cmu-graphics-helpers wheels, so the other dependencies come from
            # PyPI first
            requirements = pypi_requirements(wheel_path)
            if requirements:
                uv_pip('install', *requirements)

            # --no-cache because this install is what pulls cmu-graphics-helpers
            # out of UV_FIND_LINKS, and uv caches wheels from there by name and
            # version, ignoring size and mtime -- so a cached wheel from an
            # earlier build of the same version would win over the committed
            # one. --no-index so that a missing wheel fails the install instead
            # of uv quietly testing the one published on PyPI.
            uv_pip('install', '--no-cache', '--no-index', wheel_path)
