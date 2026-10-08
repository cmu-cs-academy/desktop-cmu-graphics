"""
Record, and later check, which helpers source the committed wheels were built from.

buildwheels.yml commits the cmu_graphics_helpers wheels to wheels/ and vendors
the same build into the zip distribution's module tree. Tests install from
those committed files rather than building the helpers, so they're only
meaningful when the files were built from the source in the same commit.
buildwheels.yml writes a stamp next to the wheels:

    python build/helpers/wheel_stamp.py write --rev <commit the wheels were built from>

and tests.yml fails fast when the stamp doesn't match:

    python build/helpers/wheel_stamp.py check

The stamp lists the git object ID of each path in STAMPED_PATHS. Git object IDs
hash content only, so the stamp ignores untracked build output (e.g. target/)
and only needs git, not the file contents -- it works in a blob:none checkout.
"""

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

WHEELS_DIR = REPO_ROOT / 'wheels'
STAMP_PATH = WHEELS_DIR / 'source-stamp.txt'

# Keep in sync with the push paths in .github/workflows/buildwheels.yml.
# Every push that changes one of these starts buildwheels, and tests fail until
# its commit of new wheels lands -- so this must never include a path that
# doesn't start buildwheels, or tests would wait on wheels that never come.
STAMPED_PATHS = [
    'cmu_graphics_helpers',
    '.cargo/config.toml',
    'build/helpers/build_cmuhelp_modules.py',
    'build/helpers/wheel_stamp.py',
    '.github/workflows/buildwheels.yml',
    '.github/actions/linux-helpers-wheel',
    '.github/actions/rust-build-env',
]

HEADER = (
    '# Written by build/helpers/wheel_stamp.py: the source the wheels in this\n'
    '# directory, and the vendored modules, were built from.\n'
)


def object_id(rev, path):
    """The git object ID of path at rev, or 'missing' if it isn't there."""
    result = subprocess.run(
        ['git', 'rev-parse', '--verify', '--quiet', f'{rev}:{path}'],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return 'missing'
    return result.stdout.strip()


def stamp_for(rev):
    """{path: object ID} for STAMPED_PATHS at rev."""
    return {path: object_id(rev, path) for path in STAMPED_PATHS}


def read_stamp():
    """The {path: object ID} recorded in STAMP_PATH, or None if there isn't one."""
    if not STAMP_PATH.exists():
        return None
    stamp = {}
    for line in STAMP_PATH.read_text().splitlines():
        if not line or line.startswith('#'):
            continue
        oid, path = line.split(' ', 1)
        stamp[path] = oid
    return stamp


def write(rev):
    lines = [f'{oid} {path}' for path, oid in stamp_for(rev).items()]
    STAMP_PATH.write_text(HEADER + '\n'.join(lines) + '\n')
    print(f'Wrote {STAMP_PATH.relative_to(REPO_ROOT)} for {rev}')


def check(rev):
    recorded = read_stamp()
    if recorded is None:
        sys.exit(
            f'{STAMP_PATH.relative_to(REPO_ROOT)} is missing, so there is no telling '
            f'what the committed wheels were built from. buildwheels.yml writes it.'
        )

    current = stamp_for(rev)
    stale = [path for path in STAMPED_PATHS if recorded.get(path) != current[path]]
    if stale:
        sys.exit(
            f'The committed cmu_graphics_helpers wheels and vendored modules are '
            f'stale: {", ".join(stale)} changed since they were built. Wait for '
            f'buildwheels.yml to commit new ones, then run the tests on that commit.'
        )

    wheels = sorted(WHEELS_DIR.glob('*.whl'))
    if not wheels:
        sys.exit(f'{WHEELS_DIR.relative_to(REPO_ROOT)} has no wheels in it')

    print('The committed wheels match the helpers source:')
    for wheel in wheels:
        print(f'  {wheel.name}')


def main():
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument('mode', choices=['write', 'check'])
    parser.add_argument('--rev', default='HEAD', help='commit to stamp or check against')
    args = parser.parse_args()

    if args.mode == 'write':
        write(args.rev)
    else:
        check(args.rev)


if __name__ == '__main__':
    main()
