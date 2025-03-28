import argparse
import html
import os
import shutil
import sys
import time
import platform

import imageio.v2 as imageio
from PIL import Image
import numpy

import subprocess
import functools

print = functools.partial(print, flush=True)

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

def is_mac_pip_ci():
    is_mac = sys.platform == 'darwin'
    is_pip = 'pip' in os.getenv('TOX_ENV_NAME', '')
    is_ci = os.environ.get('CI', False)
    return is_ci and is_mac and is_pip

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

def generate_test_source(test, run_fn, extras='', language='en'):
    source_code = ''
    source_code += 'import sys'
    source_code += '\nimport os'
    source_code += '\nos.environ["SDL_VIDEODRIVER"] = "dummy"'
    source_code += '\nos.environ["SDL_AUDIODRIVER"] = "dummy"'
    source_code += '\nsys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))'
    source_code += '\nfrom cmu_graphics import *\n'
    source_code += "setLanguage('%s')\n" % (language)
    source_code += '''def assertRaises(fn, message_substring=None):
    raised = True
    try:
        fn()
        raised = False
    except Exception as e:
        actual_message = str(e)
        if message_substring is not None and message_substring not in actual_message:
            raise Exception(f'fn raised exception, but message "{actual_message}" does not contain "{message_substring}"')
    if not raised:
        raise Exception('fn failed to raise an exception')
'''

    source_code += '\n' + test
    source_code += '\n' + extras
    source_code += '\n' + run_fn

    return source_code

def run_test(test_name, all_source_code):
    source_code_pieces = all_source_code.split('\n# -\n')
    source_code = ''
    i = 0
    all_passed = True

    for piece_i in range(len(source_code_pieces)):
        i += 1

        if not os.path.exists('image_gen/%s' % test_name):
            os.mkdir('image_gen/%s' % test_name)

        correct_path_fmt = 'image_gen/%s/correct_%d.png'
        correct_path = correct_path_fmt % (test_name, i)
        if (test_name[-3:] in ('_es', '_de')):
            correct_path = correct_path_fmt % (test_name[:-3], i)

        output_path = 'image_gen/%s/output_%d.png' % (test_name, i)

        test = ''
        run_fn = 'cmu_graphics.run()'
        if not test_name.startswith('cs3'):
            test += '\n######\n'.join(source_code_pieces[:piece_i])
            test += '\ndef onMousePress(x, y):\n'
            test += '\n'.join([('    ' + s) for s in source_code_pieces[piece_i].split('\n')])
            test += '\n    app.background = "honeydew"'
        else:
            test += source_code_pieces[piece_i]
            run_fn = 'runApp()'

        if test_name.endswith('_screens'):
            run_fn = "runAppWithScreens('a')"

        screenshot_thread = '''
from threading import Thread
import time
import traceback

def screenshotAndExit():
    try:
        raw_app = app._app
        while not raw_app._running:
            time.sleep(0.01)
        with cmu_graphics.DRAWING_LOCK:
            raw_app.frameworkRedrew = False
            raw_app.callUserFn("onMousePress", (200,200,0))
        while not raw_app.frameworkRedrew:
            time.sleep(0.01)
        raw_app.getScreenshot(%s)
        raw_app.quit()
    except:
        traceback.print_exc()
        os._exit(1)

Thread(target=screenshotAndExit, daemon=True).start()
''' % repr(os.path.abspath(output_path))

        source_code = generate_test_source(test, run_fn, screenshot_thread, 'es' if test_name.endswith('_es') else 'en')

        with open(TEST_FILE_PATH, 'w', encoding='utf-8') as f:
            f.write(source_code)

        p = subprocess.Popen(
            [sys.executable, f'../{TEST_FILE_PATH}'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd='image_gen'
        )
        stdout, stderr = p.communicate()
        console_output = stdout + stderr

        if p.returncode != 0:
            print('Return code', p.returncode)
            print(stdout.decode('utf-8'))
            print(stderr.decode('utf-8'))
            os._exit(1)

        if not os.path.exists(correct_path):
            print('Generating new %s' % correct_path)
            shutil.copy(output_path, correct_path)
            continue
        else:
            threshold = 25
            _, python_minor, _ = platform.python_version_tuple()
            if 'Label' in source_code or 'Rótulo' in source_code:
                if sys.platform == 'win32':
                    threshold = 2500
                # The newer version of cairo we're compiling with in Python 3.13+
                # has slightly different kerning in inspector labels
                elif int(python_minor) >= 13: 
                    threshold = 150
                else:
                    threshold = 50
            if not compare_images(correct_path, output_path, test_name, i,
                    threshold=threshold):
                if console_output.strip():
                    REPORT_FILE.write(
                        '<p>Console output for part %d:</p><pre>%s</pre>' %
                        (i, html.escape(console_output.decode('utf-8'))))
                REPORT_FILE.write(
                    '<p>Source code for part %d:</p><pre>%s</pre>' % (i, html.escape(source_code)))
                all_passed = False

    return all_passed



def run_cs3_exception_tests():
    print('cs3 exception tests')

    tests = [
        (
            'drawRect(0,0,200,200)',
            'runApp()',
            'You called drawRect (a CS3 Mode function) outside of redrawAll.'
        ),
        ('''\
def onAppStart(app):
    raise Exception()
''',
            'runApp()',
            'Exception:'
        ),
        ('''\
def redrawAll(app):
    raise Exception()
''',
            'runApp()',
            'Exception:'
        ),
        ('''\
def redrawAll(app):
    drawRect(0,0,200,200)
''',
        'cmu_graphics.run()',
        "You defined the event handler redrawAll which works with CS3 mode, and then called cmu_graphics.run(), which doesn't work with CS3 mode. Did you mean to call runApp instead?"
        )
    ]

    for test, run_fn, expected_output in tests:
        source_code = generate_test_source(test, run_fn)

        with open(TEST_FILE_PATH, 'w', encoding='utf-8') as f:
            f.write(source_code)

        p = subprocess.Popen(
            [sys.executable, '-u', f'../{TEST_FILE_PATH}'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd='image_gen'
        )
        stdout, stderr = p.communicate()
        console_output = (stdout + stderr).decode('utf-8')

        if expected_output not in console_output:
            print('Console output:')
            print(console_output)
            print('Does not contain expected output:')
            print(expected_output)
            print('For test:')
            print(test)
            return False

    return True

def main():
    global REPORT_FILE, WAIT

    parser = argparse.ArgumentParser()
    parser.add_argument('--only', type=str, help='The name of a single python file to run')

    args = parser.parse_args()

    num_failures = 0
    num_successes = 0
    start_time = time.time()

    # Duplicate the image_gen directory into the current working directory so that
    # the parallel Python version tests don't step on each other and cause
    # errors.
    shutil.copytree(os.path.join(os.path.dirname(__file__), 'image_gen'), 'image_gen')

    try:
        REPORT_FILE = open('report.html', 'w')
        REPORT_FILE.write(REPORT_HEADER)

        if run_cs3_exception_tests():
            num_successes += 1
        else:
            num_failures += 1

        for test_py_name in (args.only and [args.only] or os.listdir('image_gen')):
            if test_py_name in ('inspector.py', 'cs3_basic.py') and is_mac_pip_ci():
                continue

            if not test_py_name.endswith('.py'):
                continue

            if test_py_name.startswith('web_only'):
                continue

            REPORT_FILE.flush()
            print(test_py_name)
            with open('image_gen/%s' % test_py_name, encoding='utf-8') as f:
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
