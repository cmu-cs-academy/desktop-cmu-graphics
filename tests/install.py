import os
import shutil
import subprocess
import sys

mode = sys.argv[1]
base_path = sys.argv[2]

if mode == 'zip':
    cmd = f"{sys.executable} -m zipfile -e {os.path.join(base_path, 'cmu_graphics_installer.zip')} ."
    subprocess.run(cmd, check=True, shell=True)
    shutil.move(os.path.join('cmu_graphics_installer', 'cmu_graphics'), '.')
    shutil.rmtree('cmu_graphics_installer')
else:
    dist_dir = os.path.join(base_path, 'pypi_upload', 'dist')
    for path in os.listdir(dist_dir):
        if path.endswith('.whl'):
            subprocess.run(['pip', 'install', os.path.join(dist_dir, path)], check=True)
