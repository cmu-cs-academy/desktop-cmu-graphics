from cmu_graphics.shape_logic import TRANSLATED_KEY_NAMES

EPSILON = 10e-7
def almostEqual(x, y, epsilon=EPSILON):
    return abs(x - y) <= epsilon

def rounded(d):
    sign = 1 if (d >= 0) else -1
    d = abs(d)
    n = int(d)
    if (d - n >= 0.5): n += 1
    return sign * n

def round(*args):
    raise Exception(t("Use our rounded(n) instead of Python 3's round(n)\n  Python 3's round(n) does not work as one might expect!\n  If you still want Python 3's round, use pythonRound"))

def dsin(angle):
    return math.sin(math.radians(angle))

def dcos(angle):
    return math.cos(math.radians(angle))

def setLanguage(language):
    sli.setLanguage(language)

_print = print
def print(*args, **kwargs):
    return _print(*args, **kwargs)

def Robot(*args, **kwargs):
    raise NotImplementedError()

def assertEqual(*args, **kwargs):
    raise NotImplementedError()

class Shape(object):
    # This represents the attributes and methods handled by JS that the user
    # can call/get/set
    _js_attrs = {
        'left', 'right', 'top', 'bottom', 'centerX', 'centerY',
        'width', 'height', 'fill', 'opacity', 'border', 'borderWidth', 'dashes',
        'align', 'rotateAngle', 'visible',
        'group', # Not sure if this should be documented?
        'toBack', 'toFront', 'contains', 'hits', 'containsShape', 'hitsShape'
    }

    # This represents the valid keyword arguments passed to the constructor
    _init_attrs = {'fill', 'border', 'borderWidth', 'opacity', 'rotateAngle', 'dashes', 'align', 'visible', 'db'}

    def __init__(self, clsName, argNames, args, kwargs):
        for attr in list(kwargs.keys()):
            en_attr = toEnglish(attr, 'shape-attr')
            if attr != en_attr and en_attr is not None:
                kwargs[en_attr] = kwargs[attr]
                del kwargs[attr]

            if not en_attr in self._init_attrs:
                raise Exception(t("{{error}}: {{callSpec}} got an unexpected keyword argument '{{arg}}'",
                                { 'error': t('TypeError'), 'callSpec': t(clsName) + '()', 'arg': attr }))

        self._shape = slInitShape(clsName, argNames, args, kwargs)
        self._shape.studentShape = self

    def __setattr__(self, attr, val):
        if (attr[0] == '_'):
            self.__dict__[attr] = val
        else:
            en_attr = toEnglish(attr, 'shape-attr')
            if en_attr in self._js_attrs:
                sli.slSetWithTypeCheck(self._shape, en_attr, val)
            else:
                self.__dict__[attr] = val
        return val

    def __getattr__(self, attr):
        if (attr[0] == '_'):
            return self.__dict__[attr]
            
        en_attr = toEnglish(attr, 'shape-attr')
        if en_attr in self._js_attrs:
            return slGet(self._shape, en_attr)
        else:
            return self.__dict__[attr]

    def __repr__(self):
        return self._shape._toString()

class Rect(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__('Rect', ['left', 'top', 'width', 'height'], args, kwargs)

class Image(Shape):
    _js_attrs = Shape._js_attrs | {'url'}
    _init_attrs = Shape._init_attrs | {'height', 'width'}

    def __init__(self, *args, **kwargs):
        super().__init__('Image', ['url', 'left', 'top'], args, kwargs)

class Oval(Shape):
    def __init__(self, *args, **kwargs):
        super().__init__('Oval', ['centerX', 'centerY', 'width', 'height'], args, kwargs)

class Circle(Shape):
    _js_attrs = Shape._js_attrs | {'radius'}

    def __init__(self, *args, **kwargs):
        super().__init__('Circle', ['centerX', 'centerY', 'radius'], args, kwargs)

class RegularPolygon(Shape):
    _js_attrs = Shape._js_attrs | {'radius', 'points'}

    def __init__(self, *args, **kwargs):
        super().__init__('RegularPolygon', ['centerX', 'centerY', 'radius', 'points'], args, kwargs)

class Star(Shape):
    _js_attrs = Shape._js_attrs | {'radius', 'points', 'roundness'}
    _init_attrs = Shape._init_attrs | {'roundness'}

    def __init__(self, *args, **kwargs):
        super().__init__('Star', ['centerX', 'centerY', 'radius', 'points'], args, kwargs)

class Line(Shape):
    _js_attrs = Shape._js_attrs | {
        'x1', 'y1', 'x2', 'y2', 'lineWidth', 'arrowStart', 'arrowEnd'
    }
    _init_attrs = Shape._init_attrs | {'lineWidth', 'arrowStart', 'arrowEnd'}

    def __init__(self, *args, **kwargs):
        super().__init__('Line', ['x1', 'y1', 'x2', 'y2'], args, kwargs)

class Polygon(Shape):
    _js_attrs = Shape._js_attrs | {'addPoint', 'pointList'}

    def __init__(self, *args, **kwargs):
        super().__init__('Polygon', [ 'initialPoints' ], [args], kwargs)

class Arc(Shape):
    _js_attrs = Shape._js_attrs | {'startAngle', 'sweepAngle'}

    def __init__(self, *args, **kwargs):
        super().__init__('Arc', ['centerX', 'centerY', 'width', 'height',
                                 'startAngle', 'sweepAngle'], args, kwargs)

class Label(Shape):
    _js_attrs = Shape._js_attrs | {'value', 'font', 'size', 'bold', 'italic'}
    _init_attrs = Shape._init_attrs | {'bold', 'italic', 'size', 'font'}

    def __init__(self, *args, **kwargs):
        super().__init__('Label', ['value', 'centerX', 'centerY'], args, kwargs)

class Group(Shape):
    _js_attrs = Shape._js_attrs | {'children', 'add', 'clear', 'remove', 'hitTest',
        # these attributes are not pass-through, so will throw an error if used
        'arrowEnd', 'arrowStart', 'url', 'radius', 'points', 'roundness',
        'x1', 'y1', 'x2', 'y2', 'lineWidth', 'startAngle', 'sweepAngle',
        'value', 'font', 'size', 'bold', 'italic'
    }
    _init_attrs = {'visible', 'db'}

    def __init__(self, *args, **kwargs):
        super().__init__('Group', [ ], [ ], kwargs)
        for shape in args: self.add(shape)

    def __iter__(self): return iter(self._shape)
    
    def __len__(self): return len(self._shape._shapes)

class Sound(object):
    def __init__(self, url):
        self.sound = slNewSound(url)

    def play(self, **kwargs):
        default_kwargs = {'loop': False, 'restart': False}

        for keyword in kwargs:
            english_keyword = toEnglish(keyword, 'shape-attr')
            if english_keyword not in default_kwargs:
                raise Exception("TypeError: %s.%s() got an unexpected keyword argument '%s'" % (t('Sound'), t('play'), keyword))
            default_kwargs[english_keyword] = kwargs[keyword]

        loop = default_kwargs['loop']
        restart = default_kwargs['restart']

        if not isinstance(loop, bool):
            raise Exception('The loop argument to Sound.play must be True or False, got ' + repr(loop))
        if not isinstance(restart, bool):
            raise Exception('The restart argument to Sound.play must be True or False, got ' + repr(restart))
        self.sound.play(loop, restart)

    def pause(self):
        self.sound.pause()

class KeyName(str):
    def __init__(self, baseKey):
        self.__dict__['accentCombinations'] = accentCombinations(str(self))

    def __eq__(self, other):
        return other in self.accentCombinations

    def __setattr__(self, attr, value):
        raise AttributeError(f"'str' object has no attribute '{attr}'")

def translateKeyName(keyName, originalLanguage):
    if originalLanguage not in TRANSLATED_KEY_NAMES: return keyName
    return KeyName(TRANSLATED_KEY_NAMES[originalLanguage].get(keyName, keyName))

# Based on Lukas Peraza's pygame framework
# https://github.com/LBPeraza/Pygame-Asteroids
class App(object):
    def printFullTracebacks(self):
        shape_logic.printFullTracebacks()

    def getScreenshot(self, path):
        with DRAWING_LOCK:
            pygame.image.save(self._screen, path)

    def quit(self):
        self._running = False

    def callUserFn(self, fnName, args):
        if fnName in self.userGlobals:
            (self.userGlobals[fnName])(*args)

        for language in shape_logic.TRANSLATED_USER_FUNCTION_NAMES:
            if language == 'keys': continue
            if fnName in shape_logic.TRANSLATED_USER_FUNCTION_NAMES[language]:
                fnTranslations = shape_logic.TRANSLATED_USER_FUNCTION_NAMES[language][fnName]
                for fnTranslation in fnTranslations:
                    if (fnTranslation in self.userGlobals):
                        if fnName == 'onKeyHold':
                            args = ([translateKeyName(x, language) for x in args[0]], )
                        elif fnName in ['onKeyPress', 'onKeyRelease']:
                            args = (translateKeyName(args[0], language), )
                        return self.userGlobals[fnTranslation](*args)

    @staticmethod
    def getKey(keyCode, modifier):
        keyNameMap = { pygame.K_TAB: 'tab', pygame.K_RETURN: 'enter', pygame.K_BACKSPACE: 'backspace',
                       pygame.K_DELETE: 'delete', pygame.K_ESCAPE: 'escape', pygame.K_SPACE: 'space',
                       pygame.K_RIGHT: 'right', pygame.K_LEFT: 'left', pygame.K_UP: 'up', pygame.K_DOWN: 'down',
                       pygame.K_RCTRL: 'ctrl', pygame.K_LCTRL: 'ctrl'}

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

        if key == 'ctrl':
            self.isCtrlKeyDown = True
            return
        if key is None: return
        if key == 'space' and (modifier & pygame.KMOD_SHIFT):
            self.paused = not self.paused
            return

        self._allKeysDown.add(key)

        self.callUserFn('onKeyPress', (key,))

    def handleKeyRelease(self, keyCode, modifier):
        key = App.getKey(keyCode, modifier)

        if key == 'ctrl':
            self.isCtrlKeyDown = False
            return
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
        })
        shape.draw(ctx)

        ctx.save()
        try:
            self._tlg._shape.draw(ctx)
        finally:
            ctx.restore()

        ctx.save()
        try:
            if self.shouldDrawInspector():
                self.inspector.draw(ctx)
        finally:
            ctx.restore()

        # Get the cairo buffer and convert it from BGRA to RGBA
        data_string = cairo_surface.get_data()

        # Create PyGame surface
        pygame_surface = pygame.image.frombuffer(data_string, (self.width, self.height), 'RGBA')

        # Show PyGame surface
        screen.blit(pygame_surface, (0,0))

    def shouldDrawInspector(self):
        return (
            self.inspectorEnabled and
            (self.paused or
                self.stopped or
                self.alwaysShowInspector or
                self.isCtrlKeyDown)
        )

    def __init__(self, width=400, height=400, title=None):
        self.userGlobals = __main__.__dict__
        if title is None:
            try:
                self.title, _ = os.path.splitext(os.path.basename(os.path.realpath(__main__.__file__)))
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
        self.background = 'white'

        self.stepsPerSecond = 30

        self._tlg = Group()
        sli.setTopLevelGroup(self._tlg)

        self.paused = False
        self._stopped = False
        self.textInputs = []

        self.inspector = shape_logic.Inspector(self)
        self.inspectorEnabled = True
        self.alwaysShowInspector = False
        self.isCtrlKeyDown = False

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

    def getBackground(self):
        return sli.slGetAppProperty('background')
    def setBackground(self, value):
        return sli.slSetAppProperty('background', value)
    background = property(getBackground, setBackground)

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
        p = self.spawnModalProcess()
        packet = bytes(json.dumps({'title': self.title, 'prompt': prompt}) + '\n', encoding='utf-8')
        result, errors = p.communicate(packet)
        if p.returncode is not None and p.returncode != 0:
            print(errors.decode('utf-8'))
            raise Exception('Exception in getTextInput.')
        return result.decode('utf-8')

    def setTextInputs(self, *args):
        for arg in args:
            if not isinstance(arg, str):
                raise Exception('Arguments to setTextInputs must be strings. %r is not a string.' % arg)
        self.textInputs = list(args)

    def spawnModalProcess(self):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        modal_path = os.path.join(current_directory, 'modal.py')
        p = subprocess.Popen(
            [sys.executable, modal_path], stdout=subprocess.PIPE,
            stdin=subprocess.PIPE, stderr=subprocess.PIPE,
            cwd=current_directory)
        return p

    def run(self):
        from cmu_graphics.libs import pygame_loader as pg
        global pygame
        pygame = pg

        pygame.init()
        pygame.display.set_caption(self.title)

        # Make antialiasing possible
        self._screen = pygame.display.set_mode((self.width,self.height))
        cairo_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.width, self.height)
        ctx = cairo.Context(cairo_surface)

        lastTick = 0
        self._running = True
        while self._running:
            sys.stdout.flush()
            with DRAWING_LOCK:
                ran_user_code = True # assume we're going to run code
                for event in pygame.event.get():
                    if not self.stopped:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            self.callUserFn('onMousePress', event.pos)
                        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                            self.callUserFn('onMouseRelease', event.pos)
                        elif (event.type == pygame.MOUSEMOTION):
                            self.inspector.setMousePosition(*event.pos)
                            if event.buttons == (0, 0, 0):
                                self.callUserFn('onMouseMove', event.pos)
                            elif event.buttons[0] == 1:
                                self.callUserFn('onMouseDrag', event.pos)
                        elif event.type == pygame.KEYDOWN:
                            self.handleKeyPress(event.key, event.mod)
                        elif event.type == pygame.KEYUP:
                            self.handleKeyRelease(event.key, event.mod)
                        else:
                            ran_user_code = False
                    if event.type == pygame.QUIT:
                        self._running = False

                msPassed = pygame.time.get_ticks() - lastTick
                if (math.floor(1000 / self.stepsPerSecond) - msPassed < 10):
                    lastTick = pygame.time.get_ticks()
                    if not self.paused and not self.stopped:
                        self.callUserFn('onStep', ())
                        if len(self._allKeysDown) > 0:
                            self.callUserFn('onKeyHold', (list(self._allKeysDown),))
                        ran_user_code = True

                if ran_user_code:
                    self.redrawAll(self._screen, cairo_surface, ctx)
                    pygame.display.flip()
                    self.frameworkRedrew = True

                pygame.time.wait(1)

        pygame.quit()
        os._exit(0)

class AppWrapper(object):
    attrs = ['background', 'group', 'stepsPerSecond', 'paused', 'stop',
             'getTextInput', 'top', 'bottom', 'left', 'right', 'centerX',
             'centerY', 'width', 'height', 'title', 'maxShapeCount', 
             'setMaxShapeCount', 'beatsPerMinute', 'printFullTracebacks']

    def __init__(self, app):
        self._app = app

    def __dir__(self):
        fields = set(AppWrapper.attrs)
        for field in self.__dict__:
            if field != '_app':
                fields.add(field)
        return sorted(fields)

    def __getattribute__(self, attr):
        attr = toEnglish(attr, 'app-attr')
        if (attr == '_app' or not attr in AppWrapper.attrs):
            return super().__getattribute__(attr)
        return self._app.__getattribute__(attr)

    def __setattr__(self, attr, value):
        attr = toEnglish(attr, 'app-attr')
        if attr in AppWrapper.attrs:
            return self._app.__setattr__(attr, value)
        return super().__setattr__(attr, value)

def onSteps(n):
    for _ in range(n):
        callUserFn('onStep')

def onKeyHolds(keys, n):
    assert isinstance(keys, list), t('keys must be a list')
    for _ in range(n):
        callUserFn('onKeyHold', keys)

def onKeyPresses(key, n):
    for _ in range(n):
        callUserFn('onKeyPress', key)

def check_for_update():
    try:
        from .updater import get_update_info
        import shutil
        update_info = get_update_info()

        if 'last_attempt' in update_info:
            last_attempt = datetime.fromtimestamp(update_info['last_attempt'])
            if datetime.now() - last_attempt < timedelta(days=1):
                return

        most_recent_version = webrequest.get(
            'https://s3.amazonaws.com/cmu-cs-academy.lib.prod/desktop-cmu-graphics/version.txt'
        ).read().decode('ascii').strip()
        current_directory = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(current_directory, 'meta/version.txt')) as f:
            version = f.read().strip()

        if 'skip_past' in update_info and version <= update_info['skip_past']:
            return

        def call_updater_with_args(args):
            updater_path = os.path.join(current_directory, 'updater.py')
            p = subprocess.Popen([sys.executable, updater_path],
                stdin=subprocess.PIPE, stderr=subprocess.PIPE, cwd=current_directory
            )
            p.communicate(bytes(json.dumps(args) + '\n', encoding='utf-8'))
            if p.returncode != 0:
                os._exit(1)

        if most_recent_version > version:
            call_updater_with_args({'type': 'request_update', 'most_recent_version': most_recent_version})

            parent_directory = os.path.dirname(current_directory)
            installer_dir = os.path.join(parent_directory, 'cmu_graphics_installer')
            shutil.rmtree(current_directory)
            shutil.move(os.path.join(installer_dir, 'cmu_graphics'), current_directory)
            shutil.rmtree(installer_dir)

            call_updater_with_args({'type': 'complete_update'})

            os._exit(0)

    except:
        pass

def loop():
    app._app.run()

from code import InteractiveConsole
class CSAcademyConsole(InteractiveConsole):
    def __init__(self):
        self.__class__.__name__ = "CS Academy Console"
        __main__.__dict__['exit'] = lambda: os._exit(0)
        super().__init__(locals=__main__.__dict__, filename = '<%s>' % self.__class__.__name__)

    # Override the default error handling functions to avoid using our own
    # excepthook function
    def showsyntaxerror(self, filename=None):
        type, value, tb = sys.exc_info()
        sys.last_type = type
        sys.last_value = value
        sys.last_traceback = tb
        if filename and type is SyntaxError:
            # Work hard to stuff the correct filename in the exception
            try:
                msg, (dummy_filename, lineno, offset, line) = value.args
            except ValueError:
                # Not the format we expect; leave it alone
                pass
            else:
                # Stuff in the right filename
                value = SyntaxError(msg, (filename, lineno, offset, line))
                sys.last_value = value

        lines = traceback.format_exception_only(type, value)
        self.write(''.join(lines))

    def showtraceback(self):
        sys.last_type, sys.last_value, last_tb = ei = sys.exc_info()
        sys.last_traceback = last_tb
        try:
            lines = traceback.format_exception(ei[0], ei[1], last_tb.tb_next)
            self.write(''.join(lines))
        finally:
            last_tb = ei = None

    # Override interact so we can os._exit on EOF
    def interact(self):
        super().interact()
        os._exit(0)

def run():
    t = threading.Thread(target=CSAcademyConsole().interact).start()
    try:
        app._app.run()
    except KeyboardInterrupt:
        os._exit(0)

import os
import sys
from datetime import datetime
from datetime import timedelta
import json
import subprocess
from cmu_graphics.libs import webrequest
import __main__

if 'CMU_GRAPHICS_NO_UPDATE' not in __main__.__dict__:
    check_for_update()

if 'CMU_GRAPHICS_DEBUG' in __main__.__dict__:
    import platform
    current_directory = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(current_directory, 'meta/version.txt')) as f:
        version = f.read().strip()
    print('='*80)
    print('CMU Graphics Version:', version)
    print('Platform:', sys.platform)
    print('Python Version:', '.'.join(platform.python_version_tuple()))
    print('Executable Path:', sys.executable)
    print('Working Directory:', current_directory)
    print('='*80)

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import math
from cmu_graphics.libs import cairo_loader as cairo
from cmu_graphics import shape_logic
from random import *
from cmu_graphics.utils import *
import json
import atexit
import threading
import traceback
import copy

DRAWING_LOCK = threading.RLock()

pygame = None # defer module load until run
# pygame takes a few seconds to load. when a getTextInput happens before we
# get a chance to render the screen, we don't want to wait a few seconds
# for a pygame load here _and_ a few seconds for a pygame load there

sli = shape_logic.ShapeLogicInterface()
slInitShape = sli.slInitShape
slGet = sli.slGet
rgb = sli.rgb
gradient = sli.gradient
slNewSound = sli.newSound
toEnglish = sli.toEnglish
accentCombinations = sli.accentCombinations
t = sli.t

app = AppWrapper(App())
atexit.register(run)
