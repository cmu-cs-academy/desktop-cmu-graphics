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
    success = True
    base_path = os.path.join('..', 'cmu_graphics')
    for path, _, files in os.walk(base_path):
        for filename in files:
            _, extension = os.path.splitext(filename)
            if extension in ('.so', '.dylib'):
                filepath = os.path.abspath(os.path.join(base_path, path, filename))
                if not is_properly_signed(filepath):
                    print(f'{filepath} was not appropriately signed')
                    success = False

                if not has_correct_architecture(filepath):
                    print(f'{filepath} does not have the correct architecture')
                    success = False
    if not success:
        sys.exit(1)

def main():
    if platform.system() != 'Darwin':
        print('Not on a mac. Skipping ...')
        return
    verify_codesignatures()

if __name__ == '__main__':
    main()

