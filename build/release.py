# Run me from the build/ directory!

import os
import shutil
import subprocess
import re
import zipfile

# Regex used to remove the zip version code from the pip version and vice versa
ZIP_REGEX=r"### ZIPFILE VERSION ###.*### END ZIPFILE VERSION ###"
PYPI_REGEX=r"### PYPI VERSION ###.*### END PYPI VERSION ###"
VERSION_REGEX=r'version="\d+.\d+.\d+"'

ZIPFILE_NAME = "cmu_graphics_installer.zip"

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

def add_files_to_zip(path, new_zip, counter=1):
    print(counter)
    for filename in os.listdir(path):
        new_path = f"{path}/{filename}"
        new_zip.write(new_path)
        if os.path.isdir(new_path):
            add_files_to_zip(new_path, new_zip, counter+1)

def make_zip_file(src, name, dest):
    new_zip = zipfile.ZipFile(
        f"{dest}/{name}", 
        "w", 
        compression=zipfile.ZIP_DEFLATED, 
        allowZip64=True
        )
    add_files_to_zip(src, new_zip)
    new_zip.close()

def get_filename(path):
    return path.split("/")[-1]

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
        shutil.copy2(f"../samples/{sample_path}", f"{zip_dest}/cmu_graphics/{sample_path}")
    # Meta files and docs
    for path in ["../LICENSE", "../INSTRUCTIONS.pdf"]:
        shutil.copy2(path, f"{zip_dest}/{get_filename(path)}")
    for path in ["../LICENSE", "../README.md", "../setup.py", "../pyproject.toml"]:
        shutil.copy2(path, f"../pypi_upload/{get_filename(path)}") 
        # Note that those files are in a different location than src, where the
        # actual package is

    # Separate the PyPI and zip versions of cmu_graphics from each other
    pypi_source_dirs = [
        "../pypi_upload/src/cmu_graphics",
        "../pypi_upload/src/cmu_graphics/libs"
        ]
    for dir in pypi_source_dirs:
        for path in os.listdir(dir):
            full_path = f"{dir}/{path}"
            if os.path.isfile(full_path):
                replace_file_text(full_path, ZIP_REGEX, "")
    zip_source_dirs = [
        "../cmu_graphics_installer/cmu_graphics",
        "../cmu_graphics_installer/cmu_graphics/libs"
        ]
    for dir in zip_source_dirs:
        for path in os.listdir(dir):
            full_path = f"{dir}/{path}"
            if os.path.isfile(full_path):
                replace_file_text(full_path, PYPI_REGEX, "")
    
    subprocess.run(["zip", "-rq", ZIPFILE_NAME, "../cmu_graphics_installer/*"])

    # Wait for zip file to be created
    while not os.path.exists(f"../cmu_graphics_installer/{ZIPFILE_NAME}"):
        pass

    make_all_dirs("../deploy")
    for path in [
        f"../cmu_graphics_installer/{ZIPFILE_NAME}", 
        "../cmu_graphics/meta/version.txt"
        ]:
        shutil.copy2(path, f"../deploy/{get_filename(path)}")
    os.rmdir("../cmu_graphics_installer")
    
    if "APPVEYOR" in os.environ:
        # Push the zip file to AppVeyor
        for path in os.listdir("../deploy"):
            subprocess.run(["appveyor", "PushArtifact", f"../deploy/{path}"])
        
        # Deploy to PyPI 
        # TODO: Might need to use a different deployment-specific script for this
        # subprocess.run(["source", "helpers/pypi_push.sh"])
    
    # os.rmdir("../deploy")
    # os.rmdir("../pypi_upload")

main()