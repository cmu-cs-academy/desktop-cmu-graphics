from libs import webrequest
import json
import io
### ZIPFILE VERSION ###
from libs.pygame_loader import mixer
### END ZIPFILE VERSION ###
### PYPI VERSION ###
from pygame import mixer
### END PYPI VERSION ###
from threading import Timer, Lock

class Sound(object):
    def __init__(self, file):
        mixer.init()
        mixer.music.load(file)
        self.playing = False
        self.currentPos = 0
        self.loop = False
        self._quit = False
        self.musicLock = Lock()
        self.queueCheckDone()

    def queueCheckDone(self):
        timer = Timer(0.1, self.checkDone)
        timer.daemon = True
        timer.start()

    def play(self, doLoop=False, doRestart=False):
        with self.musicLock:
            if self.playing and not doRestart: return
            self.playing = True
            self.loop = doLoop
            if doRestart: self.currentPos = 0
            mixer.music.play(start=self.currentPos)

    def pause(self):
        with self.musicLock:
            if not self.playing: return
            self.playing = False
            self.currentPos += (mixer.music.get_pos() / 1000)
            mixer.music.pause()

    def checkDone(self):
        with self.musicLock:
            if mixer.music.get_pos() == -1:
                self.playing = False
                self.currentPos = 0
                if self.loop:
                    mixer.music.play()

        self.queueCheckDone()

import sys

def main():
    soundUrl = json.loads(sys.stdin.readline())['url']
    response = webrequest.get(soundUrl)
    s = Sound(io.BytesIO(response.read()))
    print('done')

    while True:
        # input() will raise an EOFError after the parent dies,
        # which will cause the program to end
        request = json.loads(input())
        command = request['command']
        kwargs = request['kwargs']
        commandMap = {'pause': s.pause, 'play': s.play}
        commandMap[command](**kwargs)
        print('done')

if __name__ == "__main__":
    main()
