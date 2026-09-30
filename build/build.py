"""
Build the zip distribution from cmu-graphics wheels.

The zip distribution is the cmu_graphics package out of the pip distribution's
wheels, with each platform's native extension side by side in it: _native.pyd
for Windows and a universal2 _native.abi3.so for macOS. Python picks the one for
the running platform by its file extension, so no loader is needed. Linux
shares macOS's extension, so the zip distribution can't support it.

    python build/build.py
        Build this platform's wheel into dist/ with uv, then the zip from it.
        That zip only runs on this platform.

    python build/build.py --wheels DIR [--all-platforms] [--sign]
        Make the zip from wheels that are already built, such as CI's.
        --all-platforms fails unless DIR has both a Windows and a macOS wheel.
        --sign signs and notarizes the macOS native extension (on macOS only;
        see notarize.py).

Run it from anywhere. The zip is written to cmu_graphics_installer.zip at the
root of the repo, unless --output says otherwise.
"""

import argparse
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BUILD_DIR = Path(__file__).resolve().parent

# The directory the zip unpacks to. tests/install_zip.py relies on this name.
ZIP_ROOT = 'cmu_graphics_installer'

NATIVE_PREFIX = 'cmu_graphics/_native.'


def log(message):
    print(message, flush=True)


def build_local_wheel(dist_dir):
    """Build this platform's wheel into dist_dir, replacing any older ones."""
    dist_dir.mkdir(exist_ok=True)
    for old in dist_dir.glob('cmu_graphics-*.whl'):
        old.unlink()

    uv = shutil.which('uv')
    if uv is None:
        sys.exit('uv was not found on PATH. Run this with `uv run build/build.py`.')

    log(f'Building the wheel into {dist_dir} ...')
    subprocess.run(
        [uv, 'build', '--wheel', '--out-dir', str(dist_dir), str(REPO_ROOT)],
        check=True,
    )


def platform_of_wheel(path):
    """'windows' or 'macos' for a wheel the zip ships, or None."""
    # The platform tag ends the filename, e.g.
    # cmu_graphics-3.0.0-cp311-abi3-macosx_11_0_universal2.whl
    tag = path.stem.split('-')[-1]
    if tag == 'win_amd64':
        return 'windows'
    if tag.startswith('macosx_'):
        return 'macos'
    return None


def find_wheels(wheels_dir, all_platforms):
    wheels = {}
    for path in sorted(wheels_dir.glob('cmu_graphics-*.whl')):
        platform = platform_of_wheel(path)
        if platform is None:
            log(f'Skipping {path.name}: the zip distribution does not ship it.')
            continue
        if platform in wheels:
            sys.exit(
                f'Found more than one {platform} wheel in {wheels_dir}: '
                f'{wheels[platform].name} and {path.name}'
            )
        wheels[platform] = path

    if not wheels:
        sys.exit(f'No Windows or macOS cmu_graphics wheels found in {wheels_dir}')

    if all_platforms:
        missing = {'windows', 'macos'} - wheels.keys()
        if missing:
            sys.exit(f'No {" or ".join(sorted(missing))} wheel found in {wheels_dir}')

    return list(wheels.values())


def unpack_wheels(wheels, stage):
    """
    Unpack the first wheel into stage, then just the native extension from each
    of the others. They were all built from the same source, so their Python
    files are the same.
    """
    for i, wheel in enumerate(wheels):
        log(f'Unpacking {wheel.name} ...')
        with zipfile.ZipFile(wheel) as zf:
            for name in zf.namelist():
                if '.dist-info/' in name:
                    continue
                if i > 0 and not name.startswith(NATIVE_PREFIX):
                    continue
                zf.extract(name, stage)


def set_zip_distribution(dist_py_path):
    # Bake the distribution switch (see cmu_graphics/dist.py) into the zip's
    # copy. The source is checked in as False, which the pip distribution uses.
    old_text = dist_py_path.read_text(encoding='utf-8')
    new_text, n = re.subn(
        r'^ZIP_DISTRIBUTION = .*$',
        'ZIP_DISTRIBUTION = True',
        old_text,
        flags=re.MULTILINE,
    )
    if n != 1:
        sys.exit(f"Expected one 'ZIP_DISTRIBUTION =' line in {dist_py_path}, found {n}")
    dist_py_path.write_text(new_text, encoding='utf-8')


def stage_zip(wheels, stage):
    if stage.exists():
        shutil.rmtree(stage)
    stage.mkdir(parents=True)

    unpack_wheels(wheels, stage)

    # Students find the samples at the top of the zip, next to their own code.
    shutil.move(stage / 'cmu_graphics' / 'samples', stage / 'samples')

    set_zip_distribution(stage / 'cmu_graphics' / 'dist.py')

    for name in ['LICENSE', 'INSTRUCTIONS.pdf']:
        shutil.copy2(REPO_ROOT / name, stage / name)


def make_zip(stage, output):
    log(f'Creating {output} ...')
    if output.exists():
        output.unlink()
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(stage.rglob('*')):
            zf.write(path, Path(ZIP_ROOT) / path.relative_to(stage))


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('--wheels', type=Path, help='directory of built wheels')
    parser.add_argument('--all-platforms', action='store_true')
    parser.add_argument('--sign', action='store_true')
    parser.add_argument(
        '--output', type=Path, default=REPO_ROOT / 'cmu_graphics_installer.zip'
    )
    args = parser.parse_args()

    if args.wheels is None:
        args.wheels = REPO_ROOT / 'dist'
        build_local_wheel(args.wheels)

    wheels = find_wheels(args.wheels, args.all_platforms)

    # Stage next to the zip, so that builds with different outputs (like the
    # parallel tox environments) don't share a staging directory.
    output = args.output.resolve()
    stage = output.parent / ZIP_ROOT
    stage_zip(wheels, stage)

    if args.sign:
        sys.path.insert(0, str(BUILD_DIR))
        import check_binaries
        import notarize

        notarize.sign_and_notarize(stage / 'cmu_graphics')
        check_binaries.verify(stage / 'cmu_graphics')

    make_zip(stage, output)
    log('Done.')


if __name__ == '__main__':
    main()
