"""
Vendor built cmu_graphics_helpers wheels into the zip distribution's module tree.

The zip distribution can't pip-install anything, so it carries a copy of the
compiled helpers for each supported platform under

    cmu_graphics/libs/cmu_graphics_helpers_loader/modules/<platform>/

This script fills those directories from built wheels. It used to download the
published wheels from PyPI using links pasted in by hand; the build workflow now
builds them and calls this script directly (see .github/workflows/buildwheels.yml),
so the wheels come from a directory instead.

Run it from anywhere:

    python build/helpers/build_cmuhelp_modules.py --wheels <dir of .whl files>

Wheels for platforms the zip distribution doesn't ship (Linux) and any sdists in
the directory are ignored. Note that the macOS binaries this produces are not
signed or notarized -- see build/README.md.
"""

import argparse
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

MODULES_DIR = Path(
    'cmu_graphics', 'libs', 'cmu_graphics_helpers_loader', 'modules'
)

PACKAGE_NAME = 'cmu_graphics_helpers'


def module_for_wheel(filename):
    """
    The module directory a wheel belongs in, or None if we don't ship it.

    Wheel filenames end in the platform tag, e.g.
    cmu_graphics_helpers-0.1.6-cp38-abi3-win_amd64.whl.
    """
    name = filename.lower()
    if not name.endswith('.whl'):
        return None
    if 'win_amd64' in name:
        return 'cmu_graphics_helpers_win_64'
    if 'macosx' in name:
        if 'arm64' in name:
            return 'cmu_graphics_helpers_mac_arm'
        if 'x86_64' in name:
            return 'cmu_graphics_helpers_mac'
    return None


def vendor_wheel(wheel_path, module_dir):
    """Replace module_dir's package directory with the one inside wheel_path."""
    with tempfile.TemporaryDirectory() as unpacked:
        with zipfile.ZipFile(wheel_path) as zf:
            zf.extractall(unpacked)

        if not Path(unpacked, PACKAGE_NAME).is_dir():
            raise SystemExit(f'{wheel_path.name} does not contain a {PACKAGE_NAME}/ directory')

        # The module directories are checked in; creating one here would mean a
        # platform name that does not match what the loader looks for.
        if not module_dir.is_dir():
            raise SystemExit(f'{module_dir} does not exist')

        destination = module_dir / PACKAGE_NAME
        # Replace rather than merge, so a file that is no longer shipped does
        # not survive in the vendored copy.
        if destination.exists():
            shutil.rmtree(destination)
        shutil.move(str(Path(unpacked, PACKAGE_NAME)), str(destination))

    print(f'{wheel_path.name} -> {module_dir}')
    for path in sorted(module_dir.rglob('*')):
        if path.is_file():
            print(f'    {path.relative_to(module_dir)}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--wheels',
        default=str(REPO_ROOT / 'cmu_graphics_helpers' / 'target' / 'wheels'),
        help='directory holding the built wheels (default: the local maturin output)',
    )
    parser.add_argument(
        '--repo-root',
        default=str(REPO_ROOT),
        help='repository to vendor into (default: the one holding this script)',
    )
    args = parser.parse_args()

    wheels_dir = Path(args.wheels)
    if not wheels_dir.is_dir():
        raise SystemExit(f'{wheels_dir} is not a directory')

    modules_dir = Path(args.repo_root) / MODULES_DIR

    vendored = []
    skipped = []
    for wheel_path in sorted(wheels_dir.iterdir()):
        module = module_for_wheel(wheel_path.name)
        if module is None:
            skipped.append(wheel_path.name)
            continue
        vendor_wheel(wheel_path, modules_dir / module)
        vendored.append(module)

    if skipped:
        print('\nSkipped (no module ships this platform):')
        for name in skipped:
            print(f'    {name}')

    if not vendored:
        raise SystemExit(
            f'no wheels for a platform the zip distribution ships were found in '
            f'{wheels_dir}. Expected win_amd64 and/or macosx wheels.'
        )

    duplicates = {module for module in vendored if vendored.count(module) > 1}
    if duplicates:
        raise SystemExit(
            f'more than one wheel mapped to {", ".join(sorted(duplicates))}. '
            f'Clear out old builds from {wheels_dir} and try again.'
        )

    print(f'\nVendored {len(vendored)} module(s).')


if __name__ == '__main__':
    sys.exit(main())
