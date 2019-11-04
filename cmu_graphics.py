import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import math
import cairo
import shape_logic
from random import *
from utils import *
import subprocess
import sys
import json
import atexit

pygame = None # defer module load until run
# pygame takes a few seconds to load. when a getTextInput happens before we
# get a chance to render the screen, we don't want to wait a few seconds
# for a pygame load here _and_ a few seconds for a pygame load there

sli = shape_logic.ShapeLogicInterface()
slInitShape = sli.slInitShape
slGet = sli.slGet
slSet = sli.slSet
rgb = sli.rgb
gradient = sli.gradient
slNewSound = sli.newSound

def makeList(rows, cols, value=None):
    if rows < 0 or cols < 0:
        raise Exception('Both rows and cols must be >= 0')
    return [[value for _ in range(cols)] for _ in range(rows)]

class Shape(object):
    def __init__(self, clsName, argNames, args, kwargs):
        self._shape = slInitShape(clsName, argNames, args, kwargs)
        self._shape.studentShape = self

    def __setattr__(self, attr, val):
        if (attr[0] == '_'):
            self.__dict__[attr] = val
        else:
            slSet(self._shape, attr, val)
        return val

    def __getattr__(self, attr):
        return slGet(self._shape, attr)

    def __repr__(self):
        return self._toString()

class Rect(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__('Rect', ['left', 'top', 'width', 'height'], args, kwargs)

class Image(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__('Image', ['url', 'left', 'top'], args, kwargs)

class Oval(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__('Oval', ['centerX', 'centerY', 'width', 'height'], args, kwargs)

class Circle(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__('Circle', ['centerX', 'centerY', 'radius'], args, kwargs)

class RegularPolygon(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__('RegularPolygon', ['centerX', 'centerY', 'radius', 'points'], args, kwargs)

class Star(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__('Star', ['centerX', 'centerY', 'radius', 'points'], args, kwargs)

class Line(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__('Line', ['x1', 'y1', 'x2', 'y2'], args, kwargs)

class Polygon(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__('Polygon', [ 'initialPoints' ], [args], kwargs)

class Arc(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__('Arc', ['centerX', 'centerY', 'width', 'height',
                                 'startAngle', 'sweepAngle'], args, kwargs)

class Label(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__('Label', ['value', 'centerX', 'centerY'], args, kwargs)

class Group(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__('Group', [ ], [ ], kwargs)
        for shape in args: self.add(shape)

    def __iter__(self): return iter(self._shape)

class Sound(object):
    def __init__(self, url):
        self.sound = slNewSound(url)

    def play(self, loop=False, restart=False):
        if not isinstance(loop, bool):
            raise Exception('The loop argument to Sound.play must be True or False, got ' + repr(loop))
        if not isinstance(restart, bool):
            raise Exception('The restart argument to Sound.play must be True or False, got ' + repr(restart))
        self.sound.play(loop, restart)

    def pause(self):
        self.sound.pause()

# Based on Lukas Peraza's pygame framework
# https://github.com/LBPeraza/Pygame-Asteroids
class App(object):
    def printFullTracebacks(self):
        shape_logic.printFullTracebacks()

    def callUserFn(self, fnName, args):
        if fnName in self.userGlobals:
            (self.userGlobals[fnName])(*args)
        else:
            pass

    @staticmethod
    def getKey(keyCode, modifier):
        keyNameMap = { pygame.K_TAB: 'tab', pygame.K_RETURN: 'enter', pygame.K_BACKSPACE: 'backspace',
                       pygame.K_DELETE: 'delete', pygame.K_ESCAPE: 'escape', pygame.K_SPACE: 'space',
                       pygame.K_RIGHT: 'right', pygame.K_LEFT: 'left', pygame.K_UP: 'up', pygame.K_DOWN: 'down'}

        shiftMap = { '1':'!', '2':'@', '3':'#', '4':'$', '5':'%', '6':'^', '7':'&', '8':'*',
                     '9':'(', '0':')', '[':'{', ']':'}', '/':'?', '=':'+', '\\':'|', '\'':'"',
                     ',':'<', '.':'>', '-':'_', ';':':', '`':'~' }

        # Punctuation, numbers, and letters
        if 33 < keyCode < 127:
            key = chr(keyCode)
            if (modifier & pygame.KMOD_SHIFT):
                key = shiftMap.get(key, key).upper()
            return key
        return keyNameMap.get(keyCode, None)

    def handleKeyPress(self, keyCode, modifier):
        key = App.getKey(keyCode, modifier)

        if key is None: return
        if key == 'space' and (modifier & pygame.KMOD_SHIFT):
            self.paused = not self.paused
            return

        self._allKeysDown.add(key)

        self.callUserFn('onKeyPress', (key,))

    def handleKeyRelease(self, keyCode, modifier):
        key = App.getKey(keyCode, modifier)
        if key is None: return

        if key.upper() in self._allKeysDown: self._allKeysDown.remove(key.upper())
        if key.lower() in self._allKeysDown: self._allKeysDown.remove(key.lower())

        self.callUserFn('onKeyRelease', (key,))

    def redrawAll(self, screen, cairo_surface, ctx):
        shape = shape_logic.Rect({
            'noGroup': True,
            'top': 0,
            'left': 0,
            'width': self.width,
            'height': self.height,
            'fill': self.background,
        });
        shape.draw(ctx)
        self._tlg.draw(ctx)

        # Get the cairo buffer and convert it from BGRA to RGBA
        data_string = cairo_surface.get_data()

        # Create PyGame surface
        pygame_surface = pygame.image.frombuffer(data_string, (self.width, self.height), 'RGBA')

        # Show PyGame surface
        screen.blit(pygame_surface, (0,0))

    def __init__(self, width=400, height=400, title=None):
        import __main__
        self.userGlobals = __main__.__dict__
        self.userGlobals['app'] = self
        if title is None:
            try:
                self.title, _ = os.path.splitext(os.path.basename(__main__.__file__))
            except:
                self.title = "CMU CS Academy"
        else:
            self.title = title

        self.left = self.top = 0
        self.centerX = width / 2
        self.centerY = height / 2
        self.width = self.right = width
        self.height = self.bottom = height
        self._allKeysDown = set()
        self._runningKeyMap = dict()
        self.background = 'white'

        self._refreshDelay = 60
        self.stepsPerSecond = 30
        self._msPassed = 0

        self._tlg = Group()
        sli.setTopLevelGroup(self._tlg)

        self.paused = False
        self._stopped = False
        self.textInputs = []

        self._modalProcesses = []
        # clean up processes when the interpreter closes
        atexit.register(self.cleanModalProcesses)
        for i in range(3): self.spawnModalProcess()

    def get_group(self):
        return self._tlg
    def set_group(self, _):
        raise Exception('App.group is readonly')
    group = property(get_group, set_group)

    def get_stopped(self):
        return self._stopped
    def set_stopped(self, _):
        raise Exception('App.stopped is readonly')
    stopped = property(get_stopped, set_stopped)

    def getMaxShapeCount(self):
        return sli.slGetAppProperty('maxShapeCount')
    def setMaxShapeCount(self, value):
        return sli.slSetAppProperty('maxShapeCount', value)
    maxShapeCount = property(getMaxShapeCount, setMaxShapeCount)

    def stop(self):
        self._stopped = True

    def getTextInput(self, prompt='Enter some text'):
        if self.textInputs:
            return self.textInputs.pop(0)
        p = self._modalProcesses.pop()
        packet = bytes(json.dumps({'title': self.title, 'prompt': prompt}) + '\n', encoding='utf-8')
        result, _ = p.communicate(packet)
        self.spawnModalProcess()
        return result.decode('utf-8')

    def setTextInputs(self, *args):
        for arg in args:
            if not isinstance(arg, str):
                raise Exception('Arguments to setTextInputs must be strings. %r is not a string.' % arg)
        self.textInputs = list(args)

    def spawnModalProcess(self):
        p = subprocess.Popen([sys.executable, 'modal.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        self._modalProcesses.insert(0, p)

    def cleanModalProcesses(self):
        for p in self._modalProcesses: p.kill()

    def run(self):
        import pygame as pg
        global pygame
        pygame = pg

        clock = pygame.time.Clock()

        pygame.display.set_icon(pygame.image.load('scs_dragon.gif'))
        pygame.display.set_caption(self.title)
        pygame.init()

        # Make antialiasing possible
        screen = pygame.display.set_mode((self.width,self.height))
        cairo_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.width, self.height)
        ctx = cairo.Context(cairo_surface)

        lastTick = 0
        running = True
        while running:
            for event in pygame.event.get():
                if not self.stopped:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.callUserFn('onMousePress', event.pos)
                    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                        self.callUserFn('onMouseRelease', event.pos)
                    elif (event.type == pygame.MOUSEMOTION and
                          event.buttons == (0, 0, 0)):
                        self.callUserFn('onMouseMove', event.pos)
                    elif (event.type == pygame.MOUSEMOTION and
                          event.buttons[0] == 1):
                        self.callUserFn('onMouseDrag', event.pos)
                    elif event.type == pygame.KEYDOWN:
                        self.handleKeyPress(event.key, event.mod)
                    elif event.type == pygame.KEYUP:
                        self.handleKeyRelease(event.key, event.mod)
                if event.type == pygame.QUIT:
                    running = False

            msPassed = pygame.time.get_ticks() - lastTick
            if (math.floor(1000 / self.stepsPerSecond) - msPassed < 10):
                lastTick = pygame.time.get_ticks()
                if not self.paused and not self.stopped:
                    self.callUserFn('onStep', ())
                    if len(self._allKeysDown) > 0:
                        self.callUserFn('onKeyHold', (list(self._allKeysDown),))

            self.redrawAll(screen, cairo_surface, ctx)
            pygame.display.flip()

        pygame.quit()

app = App()

def loop():
    app.run()
