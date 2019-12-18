import os
import sys
import time

from utils import setup_driver, copy_file, FRONTEND_HOST

from random import choice

import boto3
import imageio

import re

'''
The following imports are imported inline because they need to be imported
after the venv is initialized.
'''

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait

# import yaml
# try:
#     from yaml import CLoader as YamlLoader
# except:
#     from yaml import Loader as YamlLoader

# import virtualenv

DEFAULT_EXERCISE_DIR = '../../cs-academy/content/cs1-19'
VENV_DIR = '../../cs-academy/venv/'

NON_SPACE_RE = r'[^ ]'
TEST_SPLITTER = '\n# -\n'

SIZE = 400

WAIT = None


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
            print(f'_SOLN used outside of an if statement on line {i+1} of {exercise_code_path}', -1)

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
                    print(f'Line "{line}" has bad indentation', -1)

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
            try:
                path = current_path + '/' + filename
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
                soln_text = None

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
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait

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

def main():
    activate_script = '%s/%s/activate_this.py' % (VENV_DIR, 'Scripts' if sys.platform.startswith('win') else 'bin')
    with open(activate_script, 'r') as ActivateObject:
        exec(ActivateObject.read(), dict(__file__=activate_script))

    generate_py_files()
    try:
        generate_brython_images()
    except Exception as e:
        print(e)

    print('---END SUBPROCESS---')



if __name__ == '__main__':
    main()
    exit(1)
