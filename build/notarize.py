import os
import subprocess
import tqdm

ZIPNAME = 'cmu_graphics_installer.zip'
TEAM_ID = 'LXH25PRRZ2'

################################################################################
# Signing
################################################################################

def get_signing_identity():
    signing_identities = subprocess.check_output(
        ["security", "find-identity", "-p", "codesigning", "-v"]
    ).strip().decode('utf-8')

    signing_identity = signing_identities.splitlines()[0].split('"')[1]

    return signing_identity

def is_signed(path):
    signing_info = subprocess.run(
        ['codesign', '-dv', path],
        stderr=subprocess.PIPE
    ).stderr.decode('utf-8')

    return f'TeamIdentifier={TEAM_ID}' in signing_info

def get_unsigned_binaries():
    unsigned_files = []

    for root, _, files in tqdm.tqdm(list(os.walk("../cmu_graphics")), unit='directories'):
        for filename in files:
            if filename.endswith('.so') or filename.endswith('.dylib'):
                path = os.path.join(root, filename)
                if not is_signed(path):
                    unsigned_files.append(path)

    return unsigned_files

def sign_files():
    print("Finding unsigned binaries ...")
    unsigned_binaries = get_unsigned_binaries()
    print()

    signing_identity = get_signing_identity()
    print(f"Using signing identity: {signing_identity}")
    print()

    print("Signing binaries ...")

    for path in tqdm.tqdm(unsigned_binaries, unit='binaries'):
        subprocess.check_call(
            ['codesign', '--timestamp', '-vfs', signing_identity, path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    print('Done signing!')

################################################################################
# Notarization
################################################################################

def notarize():
    print("Zipping the cmu_graphics directory ...")
    subprocess.check_call(['zip', '-r', ZIPNAME, 'cmu_graphics'], cwd='..')
    print()

    print("Notarizing ...")
    subprocess.check_call([
        'xcrun', 'notarytool', 'submit',
        '--apple-id', os.environ['APPLE_ID'], '--password', os.environ['APPLE_PASSWORD'],
        '--team-id', TEAM_ID,
        '--wait',
         f'../{ZIPNAME}',
    ])
    print()

    print('Deleting zip file ...')
    os.remove(f'../{ZIPNAME}')
    print()

    print('Done notarizing!')

################################################################################
# Main
################################################################################


def main():
    sign_files()
    notarize()

    print()
    print('All done!')

if __name__ == '__main__':
    main()