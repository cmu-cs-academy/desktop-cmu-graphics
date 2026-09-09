import json
import os
import subprocess
import sys
import tqdm

ZIPNAME = 'cmu_graphics_notarize.zip'
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

def notarize():
    print("Zipping the cmu_graphics directory ...")
    # Apple recommends ditto for notarization submissions
    zip_path = os.path.join('..', ZIPNAME)
    if os.path.exists(zip_path):
        os.remove(zip_path)
    subprocess.check_call(
        ['ditto', '-c', '-k', '--keepParent', 'cmu_graphics', ZIPNAME], cwd='..')
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


def main():
    sign_files()
    notarize()

    print()
    print('All done!')

if __name__ == '__main__':
    main()