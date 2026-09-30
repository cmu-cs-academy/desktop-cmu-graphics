"""
Sign and notarize the macOS binaries in a directory.

    python build/notarize.py [DIR]

DIR defaults to the cmu_graphics package of the zip distribution that
build/build.py stages. The release workflow runs this through
`build/build.py --sign` instead.

Needs a Developer ID Application certificate in the keychain, and APPLE_ID and
APPLE_PASSWORD (an app-specific password) in the environment. Set
CODESIGN_IDENTITY to pick a certificate; otherwise the first valid one is used.
"""

import json
import os
import subprocess
import sys
import tempfile
import tqdm

TEAM_ID = 'LXH25PRRZ2'

################################################################################
# Signing
################################################################################

def get_signing_identity():
    if os.environ.get('CODESIGN_IDENTITY'):
        return os.environ['CODESIGN_IDENTITY']

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

def get_unsigned_binaries(directory):
    unsigned_files = []

    for root, _, files in tqdm.tqdm(list(os.walk(directory)), unit='directories'):
        for filename in files:
            if filename.endswith('.so') or filename.endswith('.dylib'):
                path = os.path.join(root, filename)
                if not is_signed(path):
                    unsigned_files.append(path)

    return unsigned_files

def sign_files(directory):
    print("Finding unsigned binaries ...")
    unsigned_binaries = get_unsigned_binaries(directory)
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

def fail(reason, zip_path, submission_id=None):
    print()
    print('*' * 79)
    print('*** NOTARIZATION FAILED')
    print('***')
    print(f'*** {reason}')
    print('***')
    print('*** The binaries are NOT notarized. Do not ship them.')
    if submission_id is not None:
        print('***')
        print('*** For the reason each binary was rejected, run:')
        print('***')
        print(f'***   xcrun notarytool log {submission_id} \\')
        print(f'***     --apple-id "$APPLE_ID" --password "$APPLE_PASSWORD" \\')
        print(f'***     --team-id {TEAM_ID}')
    print('***')
    print(f'*** {zip_path} was kept so you can inspect what was submitted.')
    print('*' * 79)
    print()
    sys.exit(1)

def notarize(directory):
    print("Zipping the binaries ...")
    # Apple recommends ditto for notarization submissions
    zip_path = os.path.join(tempfile.mkdtemp(), 'cmu_graphics_notarize.zip')
    subprocess.check_call(
        ['ditto', '-c', '-k', '--keepParent', os.path.abspath(directory), zip_path])
    print()

    print("Notarizing ...")
    # notarytool exits 0 even when it comes back Invalid, so the status has to be
    # read out of the response rather than inferred from the exit code.
    result = subprocess.run([
        'xcrun', 'notarytool', 'submit',
        '--apple-id', os.environ['APPLE_ID'], '--password', os.environ['APPLE_PASSWORD'],
        '--team-id', TEAM_ID,
        '--wait',
        '--output-format', 'json',
        zip_path,
    ], capture_output=True, text=True)

    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        fail(f'notarytool exited with status {result.returncode}.', zip_path)

    try:
        submission = json.loads(result.stdout)
    except json.JSONDecodeError:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        fail('could not parse the response from notarytool.', zip_path)

    status = submission.get('status')
    submission_id = submission.get('id')
    print(f'Submission {submission_id} finished with status: {status}')
    print()

    if status != 'Accepted':
        fail(f'notarization came back {status}, not Accepted.', zip_path, submission_id)

    print('Deleting zip file ...')
    os.remove(zip_path)
    print()

    print('Done notarizing!')

################################################################################
# Main
################################################################################


def sign_and_notarize(directory):
    sign_files(directory)
    notarize(directory)


def main():
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..',
            'cmu_graphics_installer', 'cmu_graphics')
    sign_and_notarize(directory)

    print()
    print('All done!')

if __name__ == '__main__':
    main()
