import argparse
import html
import os
import shutil
import sys
import time
import platform

from PIL import Image

import subprocess
import functools

print = functools.partial(print, flush=True)

SIZE = 400

# Seconds before a test's app is assumed to be hung
TEST_TIMEOUT = 60

# Error threshold for tests that draw images, when the screenshot had to be
# scaled down. Images are sampled from their source at a higher resolution on
# a HiDPI screen, so they can't match a 1x render as closely as shapes do.
DOWNSCALED_IMAGE_THRESHOLD = 75

REPORT_FILE = None

TEST_FILE_PATH = 'runner.py'

# The checked-in image_gen directory, as opposed to the copy main() makes in the
# working directory.
SOURCE_IMAGE_GEN_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image_gen')

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

def normalize_screenshot(path):
    """
    Scale a screenshot taken on a HiDPI screen (e.g. 800x800 physical pixels
    on a Retina Mac) down to the app's SIZExSIZE logical size, in place.
    Averaging each block of physical pixels is what a 1x render of the same
    shapes would produce. Returns whether the screenshot was scaled.

    A screenshot smaller than SIZE is left alone, so it fails comparison.
    """
    image = Image.open(path)
    width, height = image.size
    if width <= SIZE or height <= SIZE:
        return False
    image = image.convert('RGB').resize((SIZE, SIZE), Image.BOX)
    image.save(path)
    return True

def compare_images(path_1, path_2, test_name, test_piece_i, threshold=25):
    image_1 = Image.open(path_1)
    image_1 = image_1.convert("RGB")
    image_1.save(path_1)

    image_2 = Image.open(path_2)
    image_2 = image_2.convert("RGB")
    image_2.save(path_2)

    assert image_1.size == (SIZE, SIZE)
    assert image_2.size == (SIZE, SIZE)
    assert image_1.size == image_2.size

    pixels_1 = image_1.load()
    pixels_2 = image_2.load()

    mean_squared_error = 0

    pixel_errors = [[0] * SIZE for _ in range(SIZE)]

    for y in range(SIZE):
        for x in range(SIZE):
            r1, g1, b1 = pixels_1[x, y]
            r2, g2, b2 = pixels_2[x, y]

            error = (
                (r1 - r2) ** 2 +
                (g1 - g2) ** 2 +
                (b1 - b2) ** 2
            )

            pixel_errors[y][x] = error
            mean_squared_error += error

    mean_squared_error /= float(SIZE * SIZE)

    if mean_squared_error >= threshold:
        diff_image_path = 'image_gen/%s/diff_%d.png' % (test_name, test_piece_i)

        visual_diff = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
        diff_pixels = visual_diff.load()

        for y in range(SIZE):
            for x in range(SIZE):
                this_error = pixel_errors[y][x]

                if this_error > 0:
                    if this_error < threshold:
                        diff_pixels[x, y] = (0, 0, 255, 128)  # blue
                    else:
                        diff_pixels[x, y] = (255, 0, 0, 128)  # red

        visual_diff.save(diff_image_path)

        print("Part %d MSE %.0f" % (test_piece_i, mean_squared_error))
        REPORT_FILE.write("<div class='error'><p>Part %d MSE %.0f</p>" %
            (test_piece_i, mean_squared_error))
        for path in [path_1, path_2, diff_image_path]:
            REPORT_FILE.write("<img src='%s' />" % path)

    return mean_squared_error < threshold

# Helpers available to events_* tests, which run like a normal app and decide
# for themselves when to take their screenshot.
EVENTS_TEST_HELPERS = '''
import cmu_graphics.cmu_graphics as _cg
from cmu_graphics.deps import wyvern as _wyvern

def screenshotAndQuit():
    # Takes the screenshot on the next redraw, then quits
    _cg.app._app._takeScreenshotPath = SCREENSHOT_PATH
    _cg.app._app._screenshotTriggered = True

# Injected events go through the event loop's real handling of OS input.
# Coordinates and sizes are logical, like app.width and mouse events.
injectMouseMove = _wyvern._inject_mouse_move
injectResize = _wyvern._inject_resize

def injectMousePress(button=0):
    _wyvern._inject_mouse_button(button, True)

def injectMouseRelease(button=0):
    _wyvern._inject_mouse_button(button, False)
'''

def generate_test_source(test, run_fn, language='en', screenshot_path=None):
    source_code = ''
    source_code += 'import sys'
    source_code += '\nimport os'
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
    if screenshot_path is not None:
        source_code += 'SCREENSHOT_PATH = %s\n' % screenshot_path
        source_code += EVENTS_TEST_HELPERS

    source_code += '\n' + test
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

        is_translation = test_name[-3:] in ('_es', '_de')
        baseline_test_name = test_name[:-3] if is_translation else test_name
        correct_path = 'image_gen/%s/correct_%d.png' % (baseline_test_name, i)

        # Linux renders text with different fonts than the shared baselines
        # were made with, so a test can have a Linux-specific baseline.
        linux_correct_name = 'linux_correct_%d.png' % i
        linux_correct_path = 'image_gen/%s/%s' % (baseline_test_name, linux_correct_name)
        if sys.platform == 'linux' and os.path.exists(linux_correct_path):
            correct_path = linux_correct_path

        output_path = 'image_gen/%s/output_%d.png' % (test_name, i)

        test = ''
        screenshot_path = repr(os.path.abspath(output_path))
        run_fn = 'cmu_graphics.run(takeScreenshotPath=%s)' % screenshot_path
        is_events_test = test_name.startswith('events')
        if is_events_test:
            # The test calls runApp itself, and screenshotAndQuit when done
            test += source_code_pieces[piece_i]
            run_fn = ''
        elif not test_name.startswith('cs3'):
            test += '\n######\n'.join(source_code_pieces[:piece_i])
            test += '\ndef onMousePress(x, y):\n'
            test += '\n'.join([('    ' + s) for s in source_code_pieces[piece_i].split('\n')])
            test += '\n    app.background = "honeydew"'
        else:
            test += source_code_pieces[piece_i]
            run_fn = 'runApp(takeScreenshotPath=%s)' % screenshot_path

        if '_screens' in test_name:
            run_fn = "runAppWithScreens('a', takeScreenshotPath=%s)" % screenshot_path

        source_code = generate_test_source(
            test,
            run_fn,
            'es' if test_name.endswith('_es') else 'en',
            screenshot_path=screenshot_path if is_events_test else None,
        )

        with open(TEST_FILE_PATH, 'w', encoding='utf-8') as f:
            f.write(source_code)

        if os.path.exists(output_path):
            os.remove(output_path)

        p = subprocess.Popen(
            [sys.executable, f'../{TEST_FILE_PATH}'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd='image_gen'
        )
        try:
            stdout, stderr = p.communicate(timeout=TEST_TIMEOUT)
        except subprocess.TimeoutExpired:
            p.kill()
            stdout, stderr = p.communicate()
            print('Timed out after %ds' % TEST_TIMEOUT)
            print(stdout.decode('utf-8'))
            print(stderr.decode('utf-8'))
            os._exit(1)
        console_output = stdout + stderr

        if p.returncode != 0:
            print('Return code', p.returncode)
            print(stdout.decode('utf-8'))
            print(stderr.decode('utf-8'))
            os._exit(1)

        if not os.path.exists(output_path):
            print('Part %d did not save a screenshot' % i)
            REPORT_FILE.write(
                '<div class="error"><p>Part %d did not save a screenshot</p>'
                '<p>Console output:</p><pre>%s</pre><p>Source code:</p><pre>%s</pre>' %
                (i, html.escape(console_output.decode('utf-8')), html.escape(source_code)))
            all_passed = False
            continue

        downscaled = normalize_screenshot(output_path)

        output_size = Image.open(output_path).size
        if output_size != (SIZE, SIZE):
            print('Part %d screenshot is %dx%d, not %dx%d' % (i, *output_size, SIZE, SIZE))
            REPORT_FILE.write(
                '<div class="error"><p>Part %d screenshot is %dx%d, not %dx%d</p>'
                "<img src='%s' /><p>Source code:</p><pre>%s</pre>" %
                (i, *output_size, SIZE, SIZE, output_path, html.escape(source_code)))
            all_passed = False
            continue

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
                elif int(python_minor) >= 13:
                    threshold = 150
                else:
                    threshold = 50
            draws_image = any(
                name in source_code for name in ('Image(', 'Imagen(', 'Bild('))
            if downscaled and draws_image:
                threshold = max(threshold, DOWNSCALED_IMAGE_THRESHOLD)
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
            'You called drawRect (a CPCS Mode function) outside of redrawAll.'
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
        "You defined the event handler redrawAll which works with CPCS Mode, and then called cmu_graphics.run(), which doesn't work with CPCS Mode. Did you mean to call runApp instead?"
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

# Timing checks, which report numbers rather than pictures. Each prints PASS or
# FAIL lines; the test passes if there are exactly EXPECTED_PASSES of the
# former and none of the latter.
STEP_RATE_TEST = '''\
import time
import cmu_graphics.cmu_graphics as _cg

STEP_RATES = [10, 30, 60]
IDLE_RATE = 30
WARMUP = 0.25
DURATION = 1.5
# Allowed error in the measured step rate, as a fraction of stepsPerSecond
STEP_RATE_TOLERANCE = 0.15
# Allowed redraws while idle, as a multiple of the steps in the same period
MAX_REDRAWS_PER_STEP = 1.1

phases = STEP_RATES + ['idle']
state = {'phase': 0, 'phaseStart': None, 'stepTimes': [], 'redraws': 0}

def report(passed, message):
    print(('PASS ' if passed else 'FAIL ') + message, flush=True)

def startPhase(app, i):
    state['phase'] = i
    state['phaseStart'] = None
    state['stepTimes'] = []
    state['redraws'] = 0
    rate = phases[i]
    app.stepsPerSecond = IDLE_RATE if rate == 'idle' else rate

def onAppStart(app):
    startPhase(app, 0)

# Count redraws of the window, not calls to the app's redrawAll, which only
# runs after event handlers
_frameworkRedrawAll = _cg.App.redrawAll

def countingRedrawAll(self, ctx):
    if state['stepTimes']:
        state['redraws'] += 1
    return _frameworkRedrawAll(self, ctx)

_cg.App.redrawAll = countingRedrawAll

def redrawAll(app):
    pass

def onStep(app):
    now = time.monotonic()
    if state['phaseStart'] is None:
        state['phaseStart'] = now
    elapsed = now - state['phaseStart']
    if elapsed < WARMUP:
        return
    state['stepTimes'].append(now)
    if elapsed < WARMUP + DURATION:
        return

    times = state['stepTimes']
    steps = len(times) - 1
    rate = steps / (times[-1] - times[0])
    phase = phases[state['phase']]
    if phase == 'idle':
        # The redraw after the final step hasn't happened yet
        redraws = state['redraws']
        report(redraws <= steps * MAX_REDRAWS_PER_STEP,
               'idle redraws: %d redraws for %d steps' % (redraws, steps))
    else:
        report(abs(rate - phase) <= phase * STEP_RATE_TOLERANCE,
               'step rate: stepsPerSecond=%d measured %.1f' % (phase, rate))

    if state['phase'] + 1 < len(phases):
        startPhase(app, state['phase'] + 1)
    else:
        app.quit()
'''

BEHAVIOR_TESTS = [
    # (name, source, run_fn, expected number of PASS lines)
    ('step rate and idle redraws', STEP_RATE_TEST, 'runApp()', 4),
]

def run_behavior_tests():
    print('behavior tests')

    all_passed = True
    for name, test, run_fn, expected_passes in BEHAVIOR_TESTS:
        source_code = generate_test_source(test, run_fn)

        with open(TEST_FILE_PATH, 'w', encoding='utf-8') as f:
            f.write(source_code)

        p = subprocess.Popen(
            [sys.executable, '-u', f'../{TEST_FILE_PATH}'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd='image_gen'
        )
        try:
            stdout, stderr = p.communicate(timeout=TEST_TIMEOUT)
        except subprocess.TimeoutExpired:
            p.kill()
            stdout, stderr = p.communicate()
        console_output = (stdout + stderr).decode('utf-8')
        lines = console_output.splitlines()
        passes = [line for line in lines if line.startswith('PASS ')]
        failures = [line for line in lines if line.startswith('FAIL ')]

        for line in passes + failures:
            print('  ' + line)

        if failures or len(passes) != expected_passes:
            print('%s failed (expected %d PASS lines). Console output:' %
                  (name, expected_passes))
            print(console_output)
            REPORT_FILE.write(
                '<div class="error"><p>Behavior test "%s" failed</p><pre>%s</pre></div>' %
                (html.escape(name), html.escape(console_output)))
            all_passed = False

    return all_passed

def main():
    global REPORT_FILE, WAIT

    parser = argparse.ArgumentParser()
    parser.add_argument('--only', type=str, help='The name of a single python file to run')
    parser.add_argument(
        '--show-windows', action='store_true',
        help="Show each test's window, instead of running it hidden")

    args = parser.parse_args()

    # Test apps inherit this. Hidden windows don't take focus, so the
    # computer stays usable while the tests run.
    if args.show_windows:
        os.environ.pop('CMU_GRAPHICS_HIDDEN_WINDOW', None)
    else:
        os.environ['CMU_GRAPHICS_HIDDEN_WINDOW'] = '1'

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

        if not args.only:
            if run_behavior_tests():
                num_successes += 1
            else:
                num_failures += 1

        for test_py_name in (args.only and [args.only] or os.listdir('image_gen')):
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
