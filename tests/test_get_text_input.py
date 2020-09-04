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

def get_children_pids():
    return {child.pid for child in psutil.Process().children(recursive=True)}

def wait_for_modal(initial_children_pids):
    try:
        time.sleep(1)
        start_time = datetime.now()
        while True:
            if datetime.now() - start_time > timedelta(seconds=5):
                os._exit(1)
            current_children_pids = get_children_pids()
            if len(current_children_pids) > len(initial_children_pids):
                modal_pid = list(current_children_pids - initial_children_pids)[0]
                psutil.Process(modal_pid).terminate()
                os._exit(0)
    except:
        os._exit(1)

def onStep():
    Thread(target=wait_for_modal, args=(get_children_pids(),)).start()
    app.getTextInput()

cmu_graphics.loop()
