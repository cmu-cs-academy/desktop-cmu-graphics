import os
import platform
import subprocess
import sys

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
    if 'Authority=Developer ID Application: Evan Mallory (LXH25PRRZ2)' not in result_lines:
        return False

    return True

def has_correct_architecture(path):
    is_arm = 'mac_arm' in path
    is_x86 = not is_arm

    result_bytes = subprocess.check_output(['file', path])
    result = result_bytes.decode('iso-8859-1')

    if is_x86 and not 'x86_64' in result:
        return False

    if is_arm and not 'arm64' in result:
        return False

    return True

def verify_codesignatures():
    # tox only runs this in the zip envs, from {envtmpdir}, where
    # tests/install.py has unpacked the installer into ./cmu_graphics.
    base_path = 'cmu_graphics'

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

                if not has_correct_architecture(filepath):
                    print(f'{filepath} does not have the correct architecture')
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
    if platform.system() != 'Darwin':
        print('Not on a mac. Skipping ...')
        return
    verify_codesignatures()

if __name__ == '__main__':
    main()

