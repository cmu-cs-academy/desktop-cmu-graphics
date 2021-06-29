import shutil
import os
import re
from file_io_util import *

# Regex used to remove the zip version code from the pip version and vice versa
ZIP_REGEX=r"### ZIPFILE VERSION ###.*### END ZIPFILE VERSION ###"
PYPI_REGEX=r"### PYPI VERSION ###.*### END PYPI VERSION ###"

def split_versions(zip_dest, pypi_dest, ignore_fn):
    make_all_dirs(zip_dest, pypi_dest)
    
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
    pypi_parent = "/".join(pypi_dest.split("/")[:-1])
    for path in ["../LICENSE", "../README.md", "../setup.py", "../pyproject.toml"]:
        shutil.copy2(path, f"{pypi_parent}/{get_filename(path)}") 
        # Note that those files are in a different location than src, where the
        # actual package is

    # Separate the PyPI and zip versions of cmu_graphics from each other
    pypi_source_dirs = [
        f"{pypi_dest}/cmu_graphics",
        f"{pypi_dest}/cmu_graphics/libs"
        ]
    for dir in pypi_source_dirs:
        for path in os.listdir(dir):
            full_path = f"{dir}/{path}"
            if os.path.isfile(full_path):
                replace_file_text(full_path, ZIP_REGEX, "", re.DOTALL)
    zip_source_dirs = [
        f"{zip_dest}/cmu_graphics",
        f"{zip_dest}/cmu_graphics/libs"
        ]
    for dir in zip_source_dirs:
        for path in os.listdir(dir):
            full_path = f"{dir}/{path}"
            if os.path.isfile(full_path):
                replace_file_text(full_path, PYPI_REGEX, "", re.DOTALL)