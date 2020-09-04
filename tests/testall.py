import subprocess
import datetime
import sys
import os

PYTHON_PATHS = {
    'win32': ['C:\Python35', 'C:\Python36', 'C:\Python37', 'C:\Python38'],
    'darwin': ['~/venv3.5', '~/venv3.6', '~/venv3.7', '~/venv3.8']
}

def log(*args):
    new_args = [datetime.datetime.now()] + list(args)
    print(*new_args)
    sys.stdout.flush()

def run_command(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    resultBytes = None

    resultBytes = result.stdout
    resultText = resultBytes.decode('iso-8859-1')
    if '\n' in resultText:
        log('%s --> %s [ + %d more lines ]' % (
            cmd, resultText[:resultText.index('\n')], len(resultText.splitlines())))
    else:
        log('%s --> %s' % (cmd, resultText))

    if result.returncode != 0:
        log(f'FAILURE OUTPUT FROM: {cmd}')
        log(resultText)
        log(f'*** {cmd} FAILED')
        os._exit(1)

def main():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'

    for python_path in PYTHON_PATHS[sys.platform]:
        os.environ['PATH'] =  python_path + os.pathsep + os.environ['PATH']
        log('Running with Python path', python_path)
        run_command('python3 --version')

        run_command('python3 test_image_gen.py')
        run_command('python3 test_get_text_input.py')
        run_command('python3 test_sound.py')
        run_command('python3 test_autoupdate.py')

if __name__ == '__main__':
    main()
