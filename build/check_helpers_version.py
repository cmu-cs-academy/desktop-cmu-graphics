import json
import re
import subprocess
import sys
import tomllib
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HELPERS_DIR = 'cmu_graphics_helpers'

# Paths whose contents change the wheel that gets built from this tree. A change
# to any of them needs a version bump, or installs may silently resolve the
# published wheel from PyPI instead of the one built here.
# Values in this list should also be in .github/workflows/buildwheels.yml's
# push paths.
WATCHED_PATHS = [HELPERS_DIR, '.cargo/config.toml']

MAIN_REF = 'origin/main'

PYPI_URL = 'https://pypi.org/pypi/cmu-graphics-helpers/json'


def cargo_version():
    with open(ROOT / 'cmu_graphics_helpers' / 'Cargo.toml', 'rb') as f:
        return tomllib.load(f)['package']['version']


def pyproject_pin():
    with open(ROOT / 'pyproject.toml', 'rb') as f:
        data = tomllib.load(f)

    for dep in data['project']['dependencies']:
        # Ignore any environment marker, e.g. "; platform_machine != 'ARM64'"
        requirement = dep.split(';')[0].strip()
        match = re.fullmatch(r'cmu-graphics-helpers==(.+)', requirement)
        if match:
            return match.group(1)

    raise SystemExit('cmu-graphics-helpers dependency not found in pyproject.toml')


def git(*args):
    """Run a git command in ROOT, returning its stdout, or None if it failed."""
    try:
        result = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True)
    except OSError:
        return None
    if result.returncode != 0:
        return None
    return result.stdout


def require_main_ref():
    """Check that MAIN_REF exists, since every comparison below is against it."""
    if not git('rev-parse', '--verify', '--quiet', MAIN_REF):
        raise SystemExit(
            f'could not find {MAIN_REF}, so the cmu-graphics-helpers version cannot '
            f'be compared against main. Run `git fetch origin main` (a full, '
            f'non-shallow clone with an origin remote is required).'
        )


def helpers_changes():
    """Watched files that differ between main and this tree."""
    changed = git('diff', '--name-only', MAIN_REF, '--', *WATCHED_PATHS)
    if changed is None:
        raise SystemExit(
            f'could not diff {", ".join(WATCHED_PATHS)} against {MAIN_REF}'
        )
    return changed.split()


def pypi_version():
    """The newest plain X.Y.Z cmu-graphics-helpers version published on PyPI."""
    try:
        with urllib.request.urlopen(PYPI_URL, timeout=30) as response:
            releases = json.load(response)['releases']
    except (urllib.error.URLError, OSError, ValueError, KeyError) as e:
        raise SystemExit(
            f'could not read the published cmu-graphics-helpers versions from '
            f'{PYPI_URL}: {e}'
        )

    # Skip versions whose files were all deleted, and anything that isn't a
    # plain release, like a pre-release
    published = [
        version
        for version, files in releases.items()
        if files and release_sort_key(version) is not None
    ]
    if not published:
        raise SystemExit(f'no published cmu-graphics-helpers versions at {PYPI_URL}')
    return max(published, key=release_sort_key)


def release_sort_key(version):
    """A comparable key for a plain X.Y.Z version, or None if it isn't one."""
    if not re.fullmatch(r'\d+(\.\d+)*', version):
        return None
    return tuple(int(part) for part in version.split('.'))


def check_versions_in_sync():
    versions = {
        'cmu_graphics_helpers/Cargo.toml': cargo_version(),
        'pyproject.toml': pyproject_pin(),
    }

    if len(set(versions.values())) > 1:
        details = ', '.join(f'{path}={v}' for path, v in versions.items())
        print(
            f'cmu-graphics-helpers version mismatch: {details}. Keep these in sync.',
            file=sys.stderr,
        )
        sys.exit(1)


def check_version_bumped(version):
    """
    Fail if the helpers changed relative to main without a version newer than PyPI's.

    Once a version has been published, the installer is free to resolve that wheel
    from PyPI rather than the one built locally -- it will, in fact, even with
    UV_FIND_LINKS pointing at the local build. That's fine as long as they're the
    same code, so any change that alters the built wheel needs a version that
    hasn't been published yet. Unpublished versions can be reused, so a branch
    and main can both be on the same unreleased version.

    See WATCHED_PATHS for what counts as altering the wheel.
    """
    require_main_ref()

    changed = helpers_changes()
    if not changed:
        return

    changed_summary = ', '.join(sorted(changed)[:4])
    if len(changed) > 4:
        changed_summary += f' (+{len(changed) - 4} more)'

    published = pypi_version()
    current_key = release_sort_key(version)

    if current_key is not None and current_key > release_sort_key(published):
        return

    if version == published:
        problem = f'the version is still {version}, which is published on PyPI'
        fix = 'Bump it'
    elif current_key is None:
        problem = (
            f"the version is {version}, which isn't a plain X.Y.Z release, so this "
            f"check can't tell whether it's newer than {published} on PyPI"
        )
        fix = 'Use a plain X.Y.Z version'
    else:
        problem = f'the version {version} is behind {published} on PyPI'
        fix = 'Bump it'

    print(
        f'{changed_summary} differs from main, but {problem}.\n'
        f'{fix} in {HELPERS_DIR}/Cargo.toml (and pyproject.toml to match), so '
        f'that installs use the wheel built from this source instead of the '
        f'published {published} from PyPI.',
        file=sys.stderr,
    )
    sys.exit(1)


def main():
    check_versions_in_sync()
    check_version_bumped(cargo_version())


if __name__ == '__main__':
    main()
