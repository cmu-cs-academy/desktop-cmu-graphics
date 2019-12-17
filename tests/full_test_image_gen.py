#!/usr/bin/env python

import argparse
import os
import sys
import time
import traceback

import boto3
import imageio
from PIL import Image
import numpy

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from utils import setup_driver, copy_file, FRONTEND_HOST

import subprocess

import re
from random import choice

import virtualenv

'''
The following imports are done inline in the needed functions
as they require the venv to be activated.
'''

# import yaml
# try:
#     from yaml import CLoader as YamlLoader
# except:
#    from yaml import Loader as YamlLoader


DEFAULT_EXERCISE_DIR = '../../cs-academy/content/cs1-19'
VENV_DIR = '../../cs-academy/venv/'

NON_SPACE_RE = r'[^ ]'
TEST_SPLITTER = '\n# -\n'

SIZE = 400

WAIT = None
REPORT_FILE = None

TEST_FILE_PATH = './runner.py'

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

IS_CI = True#os.environ.get('CI', 'false') == 'true'

def split_exercise_code(exercise_code):
    '''
    This function was copied with slight changes from the build_content.py file.
    '''
    copy_to_soln = True
    copy_to_starter = True
    if_level = None

    starter_content = []
    soln_content = []

    def get_if_level(i, line):
        try:
            return line.index('if')
        except ValueError:
            throwErr(f'_SOLN used outside of an if statement on line {i+1} of {exercise_code_path}', -1)

    for (i, line) in enumerate(exercise_code):
        if copy_to_starter and copy_to_soln:
            if 'not _SOLN' in line:
                if_level = get_if_level(i, line)
                copy_to_soln = False
            elif '_SOLN' in line:
                if_level = get_if_level(i, line)
                copy_to_starter = False
            else:
                starter_content.append(line)
                soln_content.append(line)
        else:
            if line.startswith('%selse:' % (' ' * if_level)):
                copy_to_starter = not copy_to_starter
                copy_to_soln = not copy_to_soln
            else:
                first_non_space = re.search(NON_SPACE_RE, line)
                if len(line.strip()) > 0 and first_non_space and first_non_space.start() <= if_level:
                    copy_to_soln = copy_to_starter = True
                    if_level = None

                if line.strip() and if_level is not None and line[0:4] != '    ':
                    throwErr(f'Line "{line}" has bad indentation', -1)

                if copy_to_starter:
                    starter_content.append(line[4 if if_level is not None else 0:])
                if copy_to_soln:
                    soln_content.append(line[4 if if_level is not None else 0:])

    return soln_content


def get_test_cases(test_cases_path):
    '''
    This function was copied with slight changes from the build_content.py file.
    '''
    import yaml
    try:
        from yaml import CLoader as YamlLoader
    except:
        from yaml import Loader as YamlLoader

    test_cases = []

    def read_file(path):
        with open(path, 'rb') as f:
            result = f.read().decode('utf-8')
            return result

    if test_cases_path is not None:
        test_cases = yaml.load(read_file(test_cases_path), Loader=YamlLoader)
        all_test_code = set()
        for item in test_cases:
            extra_keys = item.keys() - {'title', 'tests', 'showOverEditor'}
            if extra_keys:
                report_error(f'Unexpected key(s) in checklist item: {extra_keys}')
            if 'showOverEditor' not in item:
                item['showOverEditor'] = True
            if item['showOverEditor'] not in (True, False):
                report_error(f'Unexpected value for showOverEditor: {item}')
            for test in item['tests']:
                if test['test'] is None:
                    test['test'] = ''
                test_code = test['test']
                if test_code in all_test_code:
                    report_error(f'{test_cases_path} contains two tests with the same code: {test_code}')
                all_test_code.add(test_code)

    return all_test_code


def generate_py_files():
    import os
    print('Generating python files...')
    max_tests_per_exercise = 3
    for (current_path, _, file_list) in os.walk(DEFAULT_EXERCISE_DIR):
        current_path = current_path.replace('\\', '/')
        soln_text = None
        test_cases = None
        for filename in file_list:
            path = current_path + '/' + filename
            try:
                if (filename.startswith('sample_solution')):
                    with open(path, 'r') as fileObject:
                        soln_text = fileObject.read()
                elif (filename.startswith('exercise_code.py')):
                    with open(path, 'r') as fileObject:
                        lines = fileObject.readlines()
                    soln_text = split_exercise_code(lines)
                elif (filename.startswith('test_cases.yml')):
                    test_cases = list(get_test_cases(path))
                else:
                    continue
            except:
                print(path)

        if (soln_text != None) and (test_cases != None):
            output = ''
            for i in range(min(len(test_cases), max_tests_per_exercise)):
                if i != 0:
                    output += TEST_SPLITTER
                output += ''.join(soln_text) + '\n' + choice(test_cases) + '\n'

            with open('image_gen/' + current_path.split('/')[-1] + '.py', 'w') as fileObject:
                fileObject.write(output)

    print('Python file generation has finished!')

def is_image_blank(path):
    '''
    This function was copied with slight changes from the cs-academy
    test_image_gen file.
    '''
    image_data = imageio.imread(path)
    assert image_data.shape == (SIZE, SIZE, 4)

    for i in range(SIZE):
        for j in range(SIZE):
            for k in range(3):
                if image_data[i][j][k] != 255:
                    return False

    return True


def save_screenshot(driver, element, path):
    '''
    This function was copied with slight changes from the cs-academy
    test_image_gen file.
    '''
    if os.path.exists(path):
        os.remove(path)
    driver.get_screenshot_as_file(path)

    # If your monitor is double resolution, you may need to run this code
    # to scale down the screenshot.
    # from PIL import Image
    # img = Image.open(path)
    # img.thumbnail((img.width / 2, img.height / 2))
    # img.save(path)

    image_data = imageio.imread(path)
    x = int(element.location['x'])
    y = int(element.location['y'])
    width = int(element.size['width'])
    height = int(element.size['height'])
    image_data = image_data[y:y+height, x:x+width]
    imageio.imwrite(path, image_data)


def generate_image(driver, test_name, all_source_code):
    '''
    This function was copied with slight changes from the cs-academy
    test_image_gen file.
    '''
    source_code_pieces = all_source_code.split(TEST_SPLITTER)
    source_code = ''
    i = 0
    all_passed = True

    for piece_i in source_code_pieces:
        tries = 0
        i += 1
        while True:
            source_code = piece_i
            source_code += '\napp.background = "honeydew"'
            source_code += '\napp.paused=True'
            correct_path = 'image_gen/%s/correct_%d.png' % (test_name, i)
            output_path = 'image_gen/%s/output_%d.png' % (test_name, i)

            # Add the code to the editor
            driver.execute_script(
                'var editor = ace.edit("text-editor");editor.setValue(%r)' % (
                    source_code))

            driver.execute_script('window.frameworkRedrew = false;');
            run_button = driver.find_element_by_class_name('run-button')
            run_button.click()
            WAIT.until(lambda d: d.execute_script('return window.frameworkRedrew;') is True)

            console_output = driver.find_element_by_class_name('console-output').text

            download_path = 'cs-academy-canvas.png'
            save_screenshot(driver, driver.find_element_by_css_selector('canvas'), download_path)
            tries += 1
            if tries >= 5 or not is_image_blank(download_path):
                break
            print('Image is blank -- waiting and retrying')
            time.sleep(1)

        if not os.path.exists('image_gen/%s' % test_name):
            os.mkdir('image_gen/%s' % test_name)

        copy_file(download_path, correct_path)

    return all_passed


def generate_brython_images():
    '''
    This function was copied with changes from the cs-academy
    test_image_gen file.
    '''
    global WAIT
    print('Generating brython images...')

    start_time = time.time()
    driver = None

    try:
        driver = setup_driver(headless=IS_CI, use_firefox=not IS_CI)
        driver.get(FRONTEND_HOST + '/ide')
        WAIT = WebDriverWait(driver, 20)
        # Wait for the ace editor to load
        WAIT.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ace_content')))

        driver.execute_script(
            'document.getElementById("application-target").addEventListener("frameworkErrored", function() {'
            'window.frameworkErrored = true;'
            '})')
        driver.execute_script(
            'document.getElementById("application-target").addEventListener("frameworkRedrew", function() {'
            'window.frameworkRedrew = true;'
            '})')

        for test_py_name in os.listdir('image_gen'):
            if not test_py_name.endswith('.py'):
                continue
            print("File Name: %s" % test_py_name)
            with open('image_gen/%s' % test_py_name) as f:
                if not generate_image(driver, test_py_name[:-3], f.read()):
                    print('image_gen/%s failed' % test_py_name)

    except KeyboardInterrupt:
        pass
    finally:
        try:
            driver.close()
        except:
            pass

    print('Image generation has finished!')

def compare_images(path_1, path_2, test_name, test_piece_i, threshold=25):
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
        diff_image_path = 'image_gen/%s/diff_%d.png' % (test_name, test_piece_i)

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


def run_test(test_name, all_source_code):
    source_code_pieces = all_source_code.split(TEST_SPLITTER)
    source_code = ''
    i = 0
    all_passed = True
    addEventFnCaller = {
        'onKeyHolds': '\ndef onKeyHolds(keys, n):\n    for i in range(n):\n        onKeyHold(keys)\n',
        'onSteps': '\ndef onSteps(n):\n    for i in range(n):\n        onStep()\n',
        'onKeyPresses': '\ndef onKeyPresses(key, n):\n    for i in range(n):\n        onKeyPress(key)\n',
        'onMousePresses': '\ndef onMousePresses(mouseX, mouseY, n):\n    for i in range(n):\n        onMousePress(mouseX, mouseY)\n'
    }

    for piece_i in source_code_pieces:
        # skip exercises with random or onMouseMove calls
        if 'randrange' in piece_i or 'onMouseMove' in piece_i:
            continue

        i += 1

        if not os.path.exists('image_gen/%s' % test_name):
            os.mkdir('image_gen/%s' % test_name)

        correct_path = 'image_gen/%s/correct_%d.png' % (test_name, i)
        output_path = 'image_gen/%s/output_%d.png' % (test_name, i)
        if not os.path.exists(output_path):
            print('Generating new %s' % output_path)
            copy_file('cs-academy-canvas.png', output_path)

        source_code = r'import sys'
        source_code += '\nsys.path.insert(0, "..")'
        source_code += '\nfrom cmu_graphics import *\n'
        source_code += piece_i

        # if any event wrapper is called, insert a definition for it above the first line it appears.
        for val in addEventFnCaller.keys():
            ind = 0
            source_code_lines = source_code.split('\n')
            for line in source_code_lines:
                if (line.find(val) != -1):
                    break
                ind += 1

            if ind != len(source_code.split('\n')):
                addedStr = addEventFnCaller[val]
                source_code_lines.insert(ind-1, addedStr)
                source_code = '\n\n'.join(list(source_code_lines))

        source_code += '\napp.background = "honeydew"'
        source_code += '\napp.paused = True'
        source_code += '\nfrom threading import Timer\n'
        source_code += '\nimport time\n'
        source_code += 'def screenshotAndExit():\n'
        source_code += '    time.sleep(1)\n'
        source_code += '    app.getScreenshot("%s")\n' % os.path.abspath(output_path).replace('\\', '/')
        source_code += '    app.quit()\n'
        source_code += 'Timer(3, screenshotAndExit).start()\n'
        source_code += 'cmu_graphics.loop()'

        with open(TEST_FILE_PATH, 'w') as f:
            f.write(source_code)

        p = subprocess.Popen(
            [sys.executable, TEST_FILE_PATH],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = p.communicate()
        console_output = stdout + stderr

        if stderr != b'':
            print(stdout.decode('utf-8'))
            print(stderr.decode('utf-8'))
            os._exit(0)

        if not os.path.exists(correct_path):
            print('Generating new %s' % correct_path)
            copy_file(output_path, correct_path)
            continue
        else:
            if not compare_images(correct_path, output_path, test_name, i,
                    threshold=50 if 'Label' in source_code else 25):
                if console_output.strip():
                    REPORT_FILE.write(
                        '<p>Console output for part %d:</p><pre>%s</pre>' %
                        (i, console_output))
                REPORT_FILE.write(
                    '<p>Source code for part %d:</p><pre>%s</pre>' % (i, source_code))
                all_passed = False

    return all_passed


def main():
    global REPORT_FILE

    parser = argparse.ArgumentParser()
    parser.add_argument('generate_tests', type=bool, default=False, nargs='?')
    if (parser.parse_args().generate_tests):
        # venv activate file on windows is in Scripts not bin.
        if sys.platform.startswith('win'):
            activate_script = os.path.join(VENV_DIR, "Scripts", "activate_this.py")
        else:
            activate_script = os.path.join(VENV_DIR, "bin", "activate_this.py").replace('\\','/')

        with open(activate_script, 'r') as ActivateObject:
            code = compile(ActivateObject.read(), activate_script, 'exec')
            exec(code, dict(__file__=activate_script))



        os.system('pip -V')
        generate_py_files()
        generate_brython_images()

        sys.path[:0] = prev_sys_path #will also revert the added site-packages
        sys.prefix = sys.real_prefix
        os.setenv('PATH', old_os_path)

        os.system('pip -V')

    num_failures = 0
    num_successes = 0
    start_time = time.time()

    try:
        REPORT_FILE = open('report.html', 'w')
        REPORT_FILE.write(REPORT_HEADER)

        print('Running cpython-cmu-graphics tests...')
        for test_py_name in os.listdir('image_gen'):
            if not test_py_name.endswith('.py'):
                continue
            REPORT_FILE.flush()
            with open('image_gen/%s' % test_py_name) as f:
                if not run_test(test_py_name[:-3], f.read()):
                    print('image_gen/%s failed' % test_py_name)
                    REPORT_FILE.write('<p>image_gen/%s failed' % (test_py_name))
                    REPORT_FILE.write('</div>')
                    num_failures += 1
                else:
                    num_successes += 1

        if num_failures > 0:
            sys.exit(1)
    except KeyboardInterrupt:
        pass
    finally:
        try:
            REPORT_FILE.write(REPORT_FOOTER)
            REPORT_FILE.close()
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
