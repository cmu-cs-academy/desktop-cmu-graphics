import re
import subprocess
import sys
import tomli
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HELPERS_DIR = 'cmu_graphics_helpers'

MAIN_REF = 'origin/main'


def cargo_version():
    with open(ROOT / 'cmu_graphics_helpers' / 'Cargo.toml', 'rb') as f:
        return tomli.load(f)['package']['version']


def pyproject_pin():
    with open(ROOT / 'pyproject.toml', 'rb') as f:
        data = tomli.load(f)

    for dep in data['project']['dependencies']:
        match = re.fullmatch(r'cmu-graphics-helpers==(.+)', dep)
        if match:
            return match.group(1)

    raise SystemExit('cmu-graphics-helpers dependency not found in pyproject.toml')


def tox_ini_pin():
    text = (ROOT / 'tox.ini').read_text()
    match = re.search(r'cmu-graphics-helpers==(\S+)', text)
    if not match:
        raise SystemExit('cmu-graphics-helpers dependency not found in tox.ini')
    return match.group(1)


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
    """Files under cmu_graphics_helpers/ that differ between main and this tree."""
    changed = git('diff', '--name-only', MAIN_REF, '--', HELPERS_DIR)
    if changed is None:
        raise SystemExit(f'could not diff {HELPERS_DIR}/ against {MAIN_REF}')
    return changed.split()


def main_version():
    """The cmu-graphics-helpers version in Cargo.toml on main."""
    cargo_toml = git('show', f'{MAIN_REF}:{HELPERS_DIR}/Cargo.toml')
    if cargo_toml is None:
        raise SystemExit(f'could not read {HELPERS_DIR}/Cargo.toml at {MAIN_REF}')
    try:
        return tomli.loads(cargo_toml)['package']['version']
    except (tomli.TOMLDecodeError, KeyError):
        raise SystemExit(
            f'could not parse the version out of {HELPERS_DIR}/Cargo.toml at {MAIN_REF}'
        )


def release_sort_key(version):
    """A comparable key for a plain X.Y.Z version, or None if it isn't one."""
    if not re.fullmatch(r'\d+(\.\d+)*', version):
        return None
    return tuple(int(part) for part in version.split('.'))


def check_versions_in_sync():
    versions = {
        'cmu_graphics_helpers/Cargo.toml': cargo_version(),
        'pyproject.toml': pyproject_pin(),
        'tox.ini': tox_ini_pin(),
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
    Fail if the helpers changed relative to main without the version being bumped.

    Once a version has been published, pip is free to install that wheel from PyPI
    rather than the one built locally from cmu_graphics_helpers/. That's fine as
    long as they're the same code, so any change to the helpers has to come with a
    new version number. main's version is the one that gets published, so it's
    enough to require that we're ahead of main whenever we've changed the helpers.
    """
    require_main_ref()

    if not helpers_changes():
        return

    published = main_version()
    current_key = release_sort_key(version)
    main_key = release_sort_key(published)

    if current_key is not None and main_key is not None and current_key > main_key:
        return

    if version == published:
        problem = f'the version is still {version}'
        fix = 'Bump it'
    elif current_key is None or main_key is None:
        unparsed = version if current_key is None else published
        problem = (
            f"the version went from {published} to {version}, and {unparsed} isn't a "
            f"plain X.Y.Z release, so this check can't tell whether that's ahead"
        )
        fix = 'Use a plain X.Y.Z version'
    else:
        problem = f'the version went backwards, from {published} to {version}'
        fix = 'Bump it'

    print(
        f'{HELPERS_DIR}/ differs from main, but {problem}.\n'
        f'{fix} in {HELPERS_DIR}/Cargo.toml (and pyproject.toml and tox.ini to '
        f'match), so that installs use the wheel built from this source instead of '
        f'the published {published} from PyPI.',
        file=sys.stderr,
    )
    sys.exit(1)


def main():
    check_versions_in_sync()
    check_version_bumped(cargo_version())


if __name__ == '__main__':
    main()
