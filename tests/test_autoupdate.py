import os
import shutil
import zipfile
from http.server import HTTPServer, CGIHTTPRequestHandler
import threading
import subprocess
import sys
import traceback
import platform
import argparse

PORT = 3000

os.chdir('autoupdate')

def create_folder_and_zip(pyversion):
    def zipdir(path, ziph):
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))

    os.mkdir(f'cmu_graphics_installer{pyversion}')
    shutil.copytree('../../cmu_graphics', f'cmu_graphics_installer{pyversion}/cmu_graphics')

    with zipfile.ZipFile('cmu_graphics_installer.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(f'cmu_graphics_installer{pyversion}', zipf)

    shutil.move(f'cmu_graphics_installer{pyversion}/cmu_graphics', 'cmu_graphics')
    os.rmdir(f'cmu_graphics_installer{pyversion}')

    os.mkdir('srv')
    shutil.move('cmu_graphics_installer.zip', 'srv/cmu_graphics_installer.zip')

    # server version
    with open('srv/version.txt', 'w+') as f:
        f.write('0.0.1')

    # local version
    with open('cmu_graphics/meta/version.txt', 'w') as f:
        f.write('0.0.0')

def set_mock_urls():
    def replace_in_file(filename, old_string, new_string):
        content = None
        with open(filename, 'r') as f:
            content = f.read()
        with open(filename, 'w') as f:
            f.write(content.replace(old_string, new_string))

    replace_in_file(
        'cmu_graphics/updater.py',
        'https://s3.amazonaws.com/cmu-cs-academy.lib.prod/desktop-cmu-graphics/cmu_graphics_installer.zip',
        'http://localhost:%d/srv/cmu_graphics_installer.zip' % PORT
    )

    replace_in_file(
        'cmu_graphics/cmu_graphics.py',
        'https://s3.amazonaws.com/cmu-cs-academy.lib.prod/desktop-cmu-graphics/version.txt',
        'http://localhost:%d/srv/version.txt' % PORT
    )

def run_server():
    httpd = HTTPServer(('', PORT), CGIHTTPRequestHandler)
    httpd.serve_forever()

def spawn_server():
    daemon = threading.Thread(target=run_server)
    daemon.setDaemon(True)
    daemon.start()

def run_student_code():
    p = subprocess.Popen(
        [sys.executable, 'update_trigger.py'],
        env={**os.environ, 'CMU_GRAPHICS_AUTO_UPDATE': 'YES'}
    )
    assert(p.wait() == 0)

def assert_update_succeeded():
    with open('cmu_graphics/meta/version.txt', 'r') as f:
        assert f.read() != '0.0.0'
    run_student_code()

def cleanup(pyversion):
    for dir in ('cmu_graphics', f'cmu_graphics_installer{pyversion}', 'srv'):
        if os.path.exists(dir):
            shutil.rmtree(dir)
    for file in ('cmu_graphics_installer.zip', 'version.txt'):
        if os.path.exists(file):
            os.remove(file)

def main(args):
    exit_code = 0
    IS_ZIP = None
    python_major, python_minor, _ = platform.python_version_tuple()
    pyversion = str(python_major) + str(python_minor)
    if args.pkg_version == "zip":
        IS_ZIP = True
        try:
            if IS_ZIP:
                create_folder_and_zip(pyversion)
            set_mock_urls()
            spawn_server()
            run_student_code() # causes an update
            assert_update_succeeded()
        except:
            traceback.print_exc()
            exit_code = 1
        finally:
            cleanup(pyversion)
    # TODO: Finish pip part!
    elif args.pkg_version == "pip":
        IS_ZIP = False
        print("""Pip part of test_autoupdate.py under construction. Please 
just use the 'zip' version flag for now.""")
        exit_code = 1
    else:
        print("Invalid version. Please provide either 'zip' or 'pip' as the package version")
        exit_code = 1

    os._exit(exit_code)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # pkg_version must be either zip or pip
    parser.add_argument(
        'pkg_version', 
        type=str, 
        help='The specific version of the package (either zip or pip) to test'
    )
    args = parser.parse_args()
    main(args)
