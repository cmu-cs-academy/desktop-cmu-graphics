import subprocess
import datetime
import sys
import os

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
        log('FAILURE OUTPUT FROM: %s' % cmd)
        log(resultText)
        log('*** %s FAILED' % cmd)
        os._exit(1)

def main():
    os.environ['SDL_VIDEODRIVER'] = 'dummy'

    run_command('python --version')
    # run_command('python test_image_gen.py')
    # run_command('python test_get_text_input.py')
    # run_command('python test_sound.py')
    # run_command('python test_autoupdate.py')

if __name__ == '__main__':
    main()
