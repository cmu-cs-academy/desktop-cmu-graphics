#!/usr/bin/env python3

import sys
import os
import subprocess

BINARY_EXTENSIONS = ['.so', '.dylib']

def sign(path, identity):
    res = subprocess.run(['codesign', '-s', identity, path])
    if res.returncode != 0: os._exit(1)
    print(f'Successfully signed {path}')

def is_binary(path):
    _, extension = os.path.splitext(path)
    return extension in BINARY_EXTENSIONS

def main(identity, root):
    for dir, _, files in os.walk(root):
        for file in files:
            filepath = os.path.join(dir, file)
            print(filepath)
            if is_binary(filepath):
                print(f"Signing {filepath}")
                # sign(filepath, identity)

print('file ran')

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) != 3:
        print('Usage: find-and-sign-binaries.py [identity] [root_path]')
        os._exit(1)
    main(sys.argv[1], sys.argv[2])
    os._exit(0)

# python3 .travis/find-and-sign-binaries.py "$(.travis/setup-keychain.sh)" "$(pwd)/yeet"
