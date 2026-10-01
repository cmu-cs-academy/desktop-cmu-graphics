"""
Check the macOS binaries in the zip distribution before it's released.

    python build/check_binaries.py [DIR]

Every .so/.dylib under DIR must be signed with our Developer ID and be a
universal2 binary (x86_64 and arm64), since the zip distribution has one macOS
native extension for both kinds of Mac. DIR defaults to the cmu_graphics package
that build/build.py stages. `build/build.py --sign` runs this after signing.
"""

import os
import platform
import subprocess
import sys

AUTHORITY = 'Authority=Developer ID Application: Evan Mallory (LXH25PRRZ2)'


def is_properly_signed(path):
    try:
        result_bytes = subprocess.check_output(
            [
                'codesign',
                '-dv',
                '--verbose=4',
                path,
            ],
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError:
        return False

    result_lines = result_bytes.decode('iso-8859-1').splitlines()
    return AUTHORITY in result_lines


def is_universal(path):
    archs = subprocess.check_output(['lipo', '-archs', path]).decode().split()
    return 'x86_64' in archs and 'arm64' in archs


def verify(base_path):
    if platform.system() != 'Darwin':
        sys.exit('Checking macOS binaries needs macOS (codesign and lipo).')

    success = True
    checked = 0
    for path, _, files in os.walk(base_path):
        for filename in files:
            _, extension = os.path.splitext(filename)
            if extension in ('.so', '.dylib'):
                filepath = os.path.abspath(os.path.join(path, filename))
                checked += 1
                if not is_properly_signed(filepath):
                    print(f'{filepath} was not appropriately signed')
                    success = False

                if not is_universal(filepath):
                    print(f'{filepath} is not a universal2 (x86_64 and arm64) binary')
                    success = False

    # Guard against this check silently passing because it was looking in the
    # wrong place, which is how it went unnoticed that for a long time it
    # checked nothing at all.
    if checked == 0:
        sys.exit(f'no .so or .dylib files were found under '
                 f'{os.path.abspath(base_path)}')

    print(f'Checked {checked} binaries.')
    if not success:
        sys.exit(1)


def main():
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..',
            'cmu_graphics_installer', 'cmu_graphics')
    verify(base_path)


if __name__ == '__main__':
    main()
