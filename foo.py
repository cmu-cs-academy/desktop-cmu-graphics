import sys
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from cmu_graphics import *
setLanguage('en')
def assertRaises(fn, message_substring=None):
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

def redrawAll(app):
    drawRect(0,0,200,200,fill='blue')


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
            raw_app.callUserFn("onMousePress", (200,200))
        while not raw_app.frameworkRedrew:
            time.sleep(0.01)
        raw_app.getScreenshot('/Users/austin-work/cs-academy/desktop-cmu-graphics/image_gen/cs3_basic/output_1.png')
        raw_app.quit()
    except:
        traceback.print_exc()
        os._exit(1)

Thread(target=screenshotAndExit).start()

runApp()
