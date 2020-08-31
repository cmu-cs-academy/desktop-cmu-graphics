import os
import shutil
import zipfile
from http.server import HTTPServer, CGIHTTPRequestHandler
import threading
import subprocess

PORT = 3000

def create_folder_and_zip():
    def zipdir(path, ziph):
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))

    os.mkdir('cmu_graphics_installer')
    shutil.copytree('../../cmu_graphics', 'cmu_graphics_installer/cmu_graphics')

    with zipfile.ZipFile('cmu_graphics_installer.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir('cmu_graphics_installer', zipf)

    shutil.move('cmu_graphics_installer/cmu_graphics', 'cmu_graphics')
    os.rmdir('cmu_graphics_installer')

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
        'https://s3.amazonaws.com/cmu-cs-academy.lib.prod/cpython-cmu-graphics-binaries/cmu_graphics_installer.zip',
        'localhost:%d/cmu_graphics_installer.zip' % PORT
    )

    replace_in_file(
        'cmu_graphics/cmu_graphics.py',
        'https://raw.githubusercontent.com/cmu-cs-academy/cpython-cmu-graphics/master/cmu_graphics/meta/version.txt',
        'localhost:%d/cmu_graphics/meta/version.txt' % PORT
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
        env={**os.environ, 'CMU_GRAPHICS_AUTO_UPDATE': 1}
    )
    assert(p.wait() == 0)

def assert_update_succeeded():
    with open('cmu_graphics/meta/version.txt', 'r') as f:
        assert f.read() != '0.0.0'
    run_student_code()

def main():
    create_folder_and_zip()
    set_mock_urls()
    spawn_server()
    run_student_code()
    assert_update_succeeded()

if __name__ == "__main__":
    main()
