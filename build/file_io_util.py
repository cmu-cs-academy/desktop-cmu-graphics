import os
import re

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def replace_file_text(path, regex, repl, flags=0):
    old_text = ""
    with open(path, "r", encoding="utf-8") as f:
        old_text = f.read()
        print(old_text)

    new_text = re.sub(regex, repl, old_text, flags=flags)

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)

def make_all_dirs(*dirs):
    for dir in dirs:
        os.makedirs(dir)

def get_filename(path):
    return path.split("/")[-1]