#!/usr/bin/env python3

import sys
import os
import subprocess

BINARY_EXTENSIONS = ['.so', '.dylib']

def sign(path, identity):
    res = subprocess.run(['codesign', '-vfs', identity, path])
    if res.returncode != 0: os._exit(1)
    print(f'Successfully signed {path}')

def is_binary(path):
    _, extension = os.path.splitext(path)
    return extension in BINARY_EXTENSIONS

def main(identity, root):
    for dir, _, files in os.walk(root):
        for file in files:
            filepath = os.path.join(dir, file)
            if is_binary(filepath):
                print(f"About to sign {filepath}")
                sign(filepath, identity)

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) != 3:
        print('Usage: find-and-sign-binaries.py [identity] [root_path]')
        os._exit(1)
    main(sys.argv[1], sys.argv[2])
    os._exit(0)
