# Run me from the build/ directory!

import os
import shutil
import subprocess
import re

# Regex used to remove the zip version code from the pip version and vice versa
ZIP_REGEX=r"### ZIPFILE VERSION ###.*### END ZIPFILE VERSION ###"
PYPI_REGEX=r"### PYPI VERSION ###.*### END PYPI VERSION ###"
VERSION_REGEX=r'version="\d+.\d+.\d+"'

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def replace_file_text(path, regex, repl, flags=0):
    old_text = ""
    with open(path, "r", encoding="utf-8") as f:
        old_text = f.read()

    new_text = re.sub(regex, repl, old_text, flags=flags)

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)

def make_all_dirs(*dirs):
    for dir in dirs:
        os.makedirs(dir)

def main():
    # Update the version inside of setup.py based on version.txt
    version_text = read_file("../cmu_graphics/meta/version.txt").strip()
    # TODO: Re-enable this once it's time to upload the actual version
    # replace_file_text("../setup.py", VERSION_REGEX, f'version="{version_text}"')

    # Copy all necessary files to zip installer and PyPI installer
    zip_dest = "../cmu_graphics_installer"
    pypi_dest= "../pypi_upload/src"
    # Source code for PyPI version must be in a src/ directory
    make_all_dirs(zip_dest, pypi_dest)
    ignore_fn = shutil.ignore_patterns("*loader", "certifi")
    # cmu_graphics package
    print("Copying cmu_graphics package to pypi_upload/src/ ...")
    shutil.copytree("../cmu_graphics", f"{pypi_dest}/cmu_graphics", ignore=ignore_fn)
    print("Copying cmu_graphics package to cmu_graphics_installer/ ...")
    shutil.copytree("../cmu_graphics", f"{zip_dest}/cmu_graphics")
    # sample files
    print("Copying sample files to pypi_upload/src/cmu_graphics ...")
    shutil.copytree("../samples", f"{pypi_dest}/cmu_graphics/samples")
    print("Copying sample files to pypi_upload/src/cmu_graphics ...")
    for sample_path in os.listdir("../samples"):
        shutil.copy2(sample_path, f"{zip_dest}/cmu_graphics/{sample_path}")
    # Meta files and docs
    for path in ["../LICENSE", "../INSTRUCTIONS.pdf"]:
        shutil.copy2(path, f"{zip_dest}/{path}")
    for path in ["../LICENSE", "../README.md", "../setup.py", "../pyproject.toml"]:
        shutil.copy2(path, f"../pypi_upload/{path}") 
        # Note that those files are in a different location than src, where the
        # actual package is

    # Separate the PyPI and zip versions of cmu_graphics from each other
    

main()