# Run me from the root of the repo!

import argparse
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
    # copy. The source is checked in as VENDORED = True (used by the zip
    # installer and local development); this flips it for the pip build.
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

    # The zip copy keeps the checked-in VENDORED = True; only the pip copy
    # needs flipping to load dependencies from the system instead of libs.
    set_vendored(f"{pypi_dest}/cmu_graphics/dist.py", False)

    print('Running python -m build...')
    subprocess.run([sys.executable, '-m', 'build'], cwd=pypi_dest, check=True)

def publish(pypi_dest, zip_dest, zipfile_name, is_prod):
    pypi_repo_args = [] if is_prod else ['--repository', 'testpypi']

    subprocess.run([sys.executable, '-m', 'twine', 'upload',
        'dist/*', '--verbose', '-u', '__token__', '-p', os.environ['PYPI_TOKEN' if is_prod else 'PYPI_TEST_TOKEN']] + pypi_repo_args,
        cwd=pypi_dest, check=True)

    s3_dest = ('s3://cmu-cs-academy.lib.prod/desktop-cmu-graphics/' if is_prod else 's3://cmu-cs-academy.lib.prod/desktop-cmu-graphics-test/'
        )
    subprocess.run(['aws', 's3', 'cp', zip_dest + '/cmu_graphics/meta/version.txt',
        s3_dest], check=True)
    subprocess.run(['aws', 's3', 'cp', zipfile_name, s3_dest], check=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--prod", action="store_true")
    args = parser.parse_args()

    zip_dest = "cmu_graphics_installer"
    pypi_dest= "pypi_upload"
    zipfile_name = "cmu_graphics_installer.zip"

    build_zip_file(zip_dest, zipfile_name)
    build_pypi_package(pypi_dest)

    if args.publish:
        publish(pypi_dest, zip_dest, zipfile_name, args.prod)

main()
