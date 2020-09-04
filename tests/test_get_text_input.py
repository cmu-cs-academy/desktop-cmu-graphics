# Exits with a 0 return code if the text input modal opens without errors
# within 5 seconds. Exits with a 1 return code otherwise.

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import psutil
import time
from datetime import datetime, timedelta
from threading import Thread
from cmu_graphics import *

def get_modal_pid():
    for proc in psutil.process_iter([]):
        if (proc.info['cmdline'] is not None and
            'modal.py' in ' '.join(proc.info['cmdline'])):
            return proc.info['pid']
    return None

def wait_for_modal():
    try:
        time.sleep(1)
        start_time = datetime.now()
        while True:
            if datetime.now() - start_time > timedelta(seconds=5):
                os._exit(1)
            modal_pid = get_modal_pid()
            if modal_pid is not None:
                psutil.Process(modal_pid).terminate()
                os._exit(0)
    except:
        os._exit(1)

def onStep():
    Thread(target=wait_for_modal).start()
    app.getTextInput()

cmu_graphics.loop()
