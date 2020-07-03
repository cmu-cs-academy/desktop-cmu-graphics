#!/usr/bin/env python3

import sys
import os
import subprocess

BINARY_EXTENSIONS = ['.so', '.dylib']

def sign(path, identity, keychain):
    args = ['codesign', '-vfs', '"%s"' % identity, '"%s"' % path, '--keychain', keychain]
    print(' '.join(args))
    res = subprocess.run(args)
    if res.returncode != 0: os._exit(1)
    print(f'Successfully signed {path}')

def is_binary(path):
    _, extension = os.path.splitext(path)
    return extension in BINARY_EXTENSIONS

def main(identity, root, keychain):
    for dir, _, files in os.walk(root):
        for file in files:
            filepath = os.path.join(dir, file)
            if is_binary(filepath):
                print(f"About to sign {filepath}")
                sign(filepath, identity, keychain)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print('Usage: find-and-sign-binaries.py [identity] [root_path] [keychain]')
        os._exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
    os._exit(0)
