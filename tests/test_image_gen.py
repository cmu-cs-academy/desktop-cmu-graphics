#!/usr/bin/env python

import argparse
import os
import sys
import time
import traceback
import platform
import shutil

import imageio
from PIL import Image
import numpy

import subprocess

SIZE = 400

REPORT_FILE = None

TEST_FILE_PATH = 'runner.py'

REPORT_HEADER = '''
<html>
<head>
<style>
div.error {
    padding-bottom: 10px;
    margin-bottom: 60px;
    background: #eee;
}
div.error img {
    margin-right: 10px;
    border: 1px solid black;
}
</style>
</head>
<body>
'''
REPORT_FOOTER = '</body></html>'

def compare_images(path_1, path_2, test_name, test_piece_i, pyversion, threshold=25):
    image_1 = Image.open(path_1)
    image_1 = image_1.convert("RGB")
    image_1.save(path_1)
    image_1_data = imageio.imread(path_1)

    image_2 = Image.open(path_2)
    image_2 = image_2.convert("RGB")
    image_2.save(path_2)
    image_2_data = imageio.imread(path_2)

    assert image_1_data.shape == (SIZE, SIZE, 3)
    assert image_2_data.shape == (SIZE, SIZE, 3)
    assert image_1_data.shape == image_2_data.shape, image_2_data.shape

    error_array = (image_1_data.astype('float') - image_2_data.astype('float')) ** 2
    mean_squared_error = numpy.sum(error_array) / float(SIZE * SIZE)

    if mean_squared_error >= threshold:
        diff_image_path = f'image_gen{pyversion}/{test_name}/diff_{test_piece_i}.png'

        per_pixel_error = error_array.sum(axis=2)

        visual_diff = numpy.zeros((SIZE, SIZE, 4), dtype=numpy.uint8)
        for i in range(SIZE):
            for j in range(SIZE):
                this_error = per_pixel_error[i][j]
                if this_error > 0:
                    if this_error < threshold:
                        visual_diff[i][j][2] = 255  # blue
                    else:
                        visual_diff[i][j][0] = 255  # red
                    visual_diff[i][j][3] = 128  # half alpha

        imageio.imwrite(diff_image_path, visual_diff)
        print("Part %d MSE %.0f" % (test_piece_i, mean_squared_error))
        REPORT_FILE.write("<div class='error'><p>Part %d MSE %.0f</p>" %
            (test_piece_i, mean_squared_error))
        for path in [path_1, path_2, diff_image_path]:
            REPORT_FILE.write("<img src='%s' />" % path)

    return mean_squared_error < threshold

def run_test(driver, test_name, all_source_code, pkg_dir, pyversion):
    source_code_pieces = all_source_code.split('\n# -\n')
    source_code = ''
    i = 0
    all_passed = True

    for piece_i in range(len(source_code_pieces)):
        i += 1

        if not os.path.exists(f'image_gen{pyversion}/{test_name}'):
            os.mkdir(f'image_gen{pyversion}/{test_name}')

        correct_path = f'image_gen{pyversion}/{test_name}/correct_{i}.png'
        output_path = f'image_gen{pyversion}/{test_name}/output_{i}.png'

        global_pieces = '\n######\n'.join(source_code_pieces[:piece_i])
        mouse_press_pieces = '\n'.join([('    ' + s) for s in source_code_pieces[piece_i].split('\n')])
        source_code = (
f'''import sys
import os

{'os.environ["SDL_VIDEODRIVER"] = "dummy"' if sys.platform == 'darwin' else ''}
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '{pkg_dir}')

from cmu_graphics import *

{global_pieces}

def onMousePress(x, y):
{mouse_press_pieces}
    app.background = "honeydew"

from threading import Thread
import time

def screenshotAndExit():
    raw_app = app._app
    while not getattr(raw_app, '_running', False):
        time.sleep(0.01)
    with cmu_graphics.DRAWING_LOCK:
        raw_app.callUserFn("onMousePress", (200,200))
        raw_app.frameworkRedrew = False
    while not raw_app.frameworkRedrew:
        time.sleep(0.01)
    raw_app.getScreenshot({repr(os.path.abspath(output_path))})
    raw_app.quit()

Thread(target=screenshotAndExit).start()
cmu_graphics.loop()
''')

        with open(TEST_FILE_PATH, 'w') as f:
            f.write(source_code)

        p = subprocess.Popen(
            [sys.executable, TEST_FILE_PATH],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = p.communicate()
        console_output = stdout + stderr

        if p.returncode != 0 or stderr != b'':
            print('Return code', p.returncode)
            print(stdout.decode('utf-8'))
            print(stderr.decode('utf-8'))
            os._exit(1)

        if not os.path.exists(correct_path):
            print('Generating new %s' % correct_path)
            os.system('cp %s %s' % (download_path, correct_path))
            continue
        else:
            threshold = 25
            if 'Label' in source_code:
                if sys.platform == 'win32':
                    threshold = 2500
                else:
                    threshold = 50
            if not compare_images(correct_path, output_path, test_name, i,
                    pyversion, threshold=threshold):
                if console_output.strip():
                    REPORT_FILE.write(
                        '<p>Console output for part %d:</p><pre>%s</pre>' %
                        (i, console_output))
                REPORT_FILE.write(
                    '<p>Source code for part %d:</p><pre>%s</pre>' % (i, source_code))
                all_passed = False

    return all_passed

def main():
    global REPORT_FILE, WAIT
    parser = argparse.ArgumentParser()
    # pkg_version must be either zip or pip
    parser.add_argument(
        'pkg_version', 
        type=str, 
        help='The specific version of the package (either zip or pip) to test'
    )
    parser.add_argument('directory', type=str, default='../CMU_CS_Academy_CS_1/', nargs='?')
    parser.add_argument('--only', type=str, help='The name of a single python file to run')
    
    args = parser.parse_args()
    
    python_major, python_minor, _ = platform.python_version_tuple()
    pyversion = str(python_major) + str(python_minor)
    pkg_dir = ''
    if args.pkg_version == "zip":
        pkg_dir = f"/cmu_graphics_installer{pyversion}"
    elif args.pkg_version == "pip":
        pkg_dir = f"/pypi_upload{pyversion}/src"
    else:
        print(f"""Invalid pkg_version argument: {args.pkg_version}. Please specify 
a package version of either zip or pip.""")
        os._exit(1)

    num_failures = 0
    num_successes = 0
    start_time = time.time()
    driver = None

    # Have to copy the image_gen directory for each of the tests so that
    # the parallel Python version tests don't step on each other and cause
    # errors
    shutil.copytree('image_gen', f'image_gen{pyversion}')

    try:
        REPORT_FILE = open(f'report{pyversion}.html', 'w')
        REPORT_FILE.write(REPORT_HEADER)

        for test_py_name in (args.only and [args.only] or os.listdir(f'image_gen{pyversion}')):
            if not test_py_name.endswith('.py'):
                continue
            REPORT_FILE.flush()
            print(test_py_name)
            with open(f'image_gen{pyversion}/{test_py_name}') as f:
                if not run_test(driver, test_py_name[:-3], f.read(), pkg_dir, pyversion):
                    print(f'image_gen{pyversion}/{test_py_name} failed')
                    REPORT_FILE.write(f'<p>image_gen{pyversion}/{test_py_name} failed')
                    REPORT_FILE.write('</div>')
                    num_failures += 1
                else:
                    num_successes += 1

        if num_failures > 0:
            shutil.rmtree(f'image_gen{pyversion}')
            sys.exit(1)
    except KeyboardInterrupt:
        pass
    finally:
        shutil.rmtree(f'image_gen{pyversion}')
        try:
            REPORT_FILE.write(REPORT_FOOTER)
            REPORT_FILE.close()
        except:
            pass
        try:
            if driver:
                print('Saving screenshot in final_screenshot.png')
                driver.save_screenshot('final_screenshot.png')
        except:
            print('Exception saving screenshot')
            traceback.print_exc()
        try:
            driver.close()
        except:
            pass
        try:
            os.remove(TEST_FILE_PATH)
        except:
            pass
        print('\n\n%d successes and %d failures in %.1fs' % (
            num_successes, num_failures, time.time() - start_time))
        print('See report.html for details')

if __name__ == '__main__':
    main()
