import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def cargo_version():
    with open(ROOT / 'cmu_graphics_helpers' / 'Cargo.toml', 'rb') as f:
        return tomllib.load(f)['package']['version']


def pyproject_pin():
    with open(ROOT / 'pyproject.toml', 'rb') as f:
        data = tomllib.load(f)

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


def main():
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


if __name__ == '__main__':
    main()
