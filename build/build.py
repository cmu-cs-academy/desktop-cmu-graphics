# Run me from the root of the repo!

import os
import re
import sys
import subprocess
import shutil

def copytree_log(src, dest, **kwargs):
    print(f"Copying {src} to {dest} ...")
    shutil.copytree(src, dest, **kwargs)

def copyfile_log(src, dest, **kwargs):
    print(f"Copying {src} to {dest} ...")
    shutil.copy2(src, dest, **kwargs)

def set_vendored(dist_py_path, vendored):
    # Bake the distribution switch (see cmu_graphics/dist.py) into a build
    # copy. The source is checked in as VENDORED = False (used by local
    # development and the pip build); this sets it for the zip installer.
    with open(dist_py_path, "r", encoding="utf-8") as f:
        old_text = f.read()

    new_text, n = re.subn(
        r"^VENDORED = .*$", f"VENDORED = {vendored}", old_text, flags=re.MULTILINE)
    if n != 1:
        raise Exception(
            f"Expected exactly one 'VENDORED =' line in {dist_py_path}, found {n}")

    with open(dist_py_path, "w", encoding="utf-8") as f:
        f.write(new_text)


def build_zip_file(zip_dest, zipfile_name):
    if os.path.exists(zip_dest):
        shutil.rmtree(zip_dest)
    os.makedirs(zip_dest)

    # The zip is a copy of the working tree, so local artifacts have to be
    # filtered out here. (The wheel doesn't need this -- `python -m build` only
    # packages what pyproject declares, so it ignores these regardless.)
    local_artifacts = shutil.ignore_patterns(".DS_Store", "__pycache__", "updates.json")

    copytree_log("cmu_graphics", f"{zip_dest}/cmu_graphics", ignore=local_artifacts)
    copytree_log("samples", f"{zip_dest}/samples", ignore=local_artifacts)
    copyfile_log("cmu_cpcs_utils.py", f"{zip_dest}/")

    # The zip loads the binaries vendored under cmu_graphics/libs
    set_vendored(f"{zip_dest}/cmu_graphics/dist.py", True)

    for path in ["LICENSE", "INSTRUCTIONS.pdf"]:
        copyfile_log(path, f"{zip_dest}/{os.path.basename(path)}")

    print('Creating zip file...')
    subprocess.run([sys.executable, '-m', 'zipfile', '-c', zipfile_name, zip_dest], check=True)

def build_pypi_package(pypi_dest):
    if os.path.exists(pypi_dest):
        shutil.rmtree(pypi_dest)
    os.makedirs(pypi_dest)

    vendored_packages = shutil.ignore_patterns("*loader")

    copytree_log("cmu_graphics", f"{pypi_dest}/cmu_graphics", ignore=vendored_packages)
    copytree_log("samples", f"{pypi_dest}/cmu_graphics/samples")
    copyfile_log("cmu_cpcs_utils.py", f"{pypi_dest}/")

    for path in ["LICENSE", "README.md", "pyproject.toml"]:
        copyfile_log(path, f"{pypi_dest}/{os.path.basename(path)}")

    # The checked-in value already is False, but set it explicitly, so the
    # pip build doesn't depend on what happens to be checked in.
    set_vendored(f"{pypi_dest}/cmu_graphics/dist.py", False)

    print('Running python -m build...')
    subprocess.run([sys.executable, '-m', 'build'], cwd=pypi_dest, check=True)

def main():
    zip_dest = "cmu_graphics_installer"
    pypi_dest= "pypi_upload"
    zipfile_name = "cmu_graphics_installer.zip"

    build_zip_file(zip_dest, zipfile_name)
    build_pypi_package(pypi_dest)

main()
