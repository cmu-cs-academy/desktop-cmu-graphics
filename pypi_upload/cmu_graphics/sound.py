from libs import webrequest
import json
import io

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
        Timer(0.1, self.checkDone).start()

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

        Timer(0.1, self.checkDone).start()

import os
import sys

def main():
    soundUrl = json.loads(sys.stdin.readline())['url']
    response = webrequest.get(soundUrl)
    s = Sound(io.BytesIO(response.read()))
    print('done')

    while True:
        request = json.loads(input())
        command = request['command']
        kwargs = request['kwargs']
        commandMap = {'pause': s.pause, 'play': s.play}
        commandMap[command](**kwargs)
        print('done')

if __name__ == "__main__":
    main()
