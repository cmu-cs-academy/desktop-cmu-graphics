"""
Verify that cmu_graphics_helpers imports on a Windows machine that does NOT have
the Microsoft Visual C++ Redistributable installed.

This cannot be tested on a normal CI runner: every GitHub Actions and AppVeyor
Windows image has Visual Studio, and therefore MSVCP140.dll, installed. An import
test there passes whether or not we bundled anything. So instead we run the import
inside a Windows Server Core container, which has no redistributable, against a
Python embeddable distribution -- roughly what a student's machine looks like.

The test has two halves, and the second is the important one:

  1. Positive: import cmu_graphics_helpers from the wheel. Must succeed.
  2. Negative: delete the bundled msvcp140.dll and import again. Must FAIL.

Without (2), a green run would not distinguish "we bundled the DLL correctly" from
"the container had the DLL all along", which would make the whole test worthless.

Run from the repo root on a Windows host with Docker in Windows-container mode:

    python tests/clean_windows_import_test.py --wheel path/to/wheels
"""

import argparse
import io
import os
import shutil
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path

# The container OS build has to match the host's for process isolation, so this
# pairs with runs-on: windows-2022. windows-2022 also pre-caches this image, so
# there is no multi-gigabyte pull.
CONTAINER_IMAGE = 'mcr.microsoft.com/windows/servercore:ltsc2022'

# The embeddable distribution is a plain zip of CPython -- no installer, no
# registry, and it carries its own vcruntime140.dll, which is exactly the
# situation a student's python.org install is in.
PYTHON_VERSION = os.environ.get('CLEAN_WINDOWS_PYTHON_VERSION', '3.14.0')
EMBED_URL = (
    'https://www.python.org/ftp/python/{v}/python-{v}-embed-amd64.zip'
)

MOUNT = 'C:\\work'


def stage_python(staging):
    """Download and unpack the Python embeddable distribution into staging."""
    url = EMBED_URL.format(v=PYTHON_VERSION)
    print(f'Downloading {url}')
    with urllib.request.urlopen(url, timeout=120) as response:
        data = response.read()
    target = staging / 'python'
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        zf.extractall(target)
    return target


def stage_wheel(staging, wheel_path):
    """Unpack the wheel into a directory we can put on sys.path."""
    target = staging / 'site'
    with zipfile.ZipFile(wheel_path) as zf:
        zf.extractall(target)

    matches = [p for p in (target / 'cmu_graphics_helpers').iterdir()
               if p.name.lower() == 'msvcp140.dll']
    if not matches:
        raise SystemExit(
            f'{wheel_path} does not contain cmu_graphics_helpers/msvcp140.dll. '
            f'See the [tool.maturin] include section of cmu_graphics_helpers/pyproject.toml.'
        )
    return target, matches[0]


def run_import_in_container(staging):
    """Import cmu_graphics_helpers inside the container. Returns (rc, output)."""
    code = (
        "import sys; sys.path.insert(0, r'{mount}\\site'); "
        "import cmu_graphics_helpers; print('import OK')"
    ).format(mount=MOUNT)

    result = subprocess.run(
        [
            'docker', 'run', '--rm',
            '--isolation=process',
            '-v', f'{staging}:{MOUNT}',
            CONTAINER_IMAGE,
            f'{MOUNT}\\python\\python.exe', '-c', code,
        ],
        capture_output=True, text=True,
    )
    return result.returncode, (result.stdout + result.stderr).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--wheel', required=True,
                        help='the built Windows wheel, or a directory containing it')
    parser.add_argument('--staging', default='clean-windows-staging',
                        help='scratch directory for the container mount')
    args = parser.parse_args()

    if sys.platform != 'win32':
        print('This test needs a Windows host running Windows containers.')
        return 1

    wheel = Path(args.wheel)
    if wheel.is_dir():
        wheels = sorted(wheel.glob('*win_amd64.whl'), key=lambda p: p.stat().st_mtime)
        if not wheels:
            raise SystemExit(f'no win_amd64 wheel found in {wheel}')
        wheel = wheels[-1]
    print(f'Testing {wheel.name}')

    staging = Path(args.staging).resolve()
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    stage_python(staging)
    _, bundled_dll = stage_wheel(staging, wheel)

    print(f'\n--- Positive: importing with the bundled DLLs, in {CONTAINER_IMAGE} ---')
    returncode, output = run_import_in_container(staging)
    print(output)
    if returncode != 0:
        print(
            '\nFAILED: cmu_graphics_helpers could not be imported on a machine without '
            'the Visual C++ Redistributable. This is the bug students hit.'
        )
        return 1

    # If this half passes, the container is not actually missing MSVCP140.dll, and
    # the positive result above proves nothing about what students experience.
    print('\n--- Negative control: same import with msvcp140.dll removed ---')
    bundled_dll.unlink()
    returncode, output = run_import_in_container(staging)
    print(output)
    if returncode == 0:
        print(
            '\nFAILED: the import still succeeded after msvcp140.dll was removed, so the '
            'container already has the Visual C++ runtime and this test is not measuring '
            'anything. Check that CONTAINER_IMAGE is a clean base image.'
        )
        return 1
    if 'DLL load failed' not in output:
        print(
            '\nFAILED: the import failed without the expected "DLL load failed" error, so '
            'something other than the missing DLL broke. See the output above.'
        )
        return 1

    print('\nPASSED: the wheel imports on a clean Windows, and does not without the bundled DLL.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
