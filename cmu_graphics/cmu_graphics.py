import inspect
import types

from cmu_graphics.shape_logic import TRANSLATED_KEY_NAMES, _ShapeMetaclass
from cmu_graphics import shape_logic

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

class Shape(object, metaclass=_ShapeMetaclass):
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
        if app is not None and app._app._isMvc:
            shapeName = self.__class__.__name__
            raise NotImplementedError(f"Whoops! {shapeName} objects are not available in CS3 Mode. Did you want draw{shapeName}?")

        global SHAPES_CREATED
        SHAPES_CREATED += 1

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
    _init_attrs = (Shape._init_attrs | {'lineWidth', 'arrowStart', 'arrowEnd'}) - {'align', 'border', 'borderWidth'}

    def __init__(self, *args, **kwargs):
        super().__init__('Line', ['x1', 'y1', 'x2', 'y2'], args, kwargs)

class Polygon(Shape):
    _js_attrs = Shape._js_attrs | {'addPoint', 'pointList'}
    _init_attrs = Shape._init_attrs - {'align'}

    def __init__(self, *args, **kwargs):
        super().__init__('Polygon', [ 'initialPoints' ], [args], kwargs)

class Arc(Shape):
    _js_attrs = Shape._js_attrs | {'startAngle', 'sweepAngle'}
    _init_attrs = Shape._init_attrs - {'align'}

    def __init__(self, *args, **kwargs):
        super().__init__('Arc', ['centerX', 'centerY', 'width', 'height',
                                 'startAngle', 'sweepAngle'], args, kwargs)

class Label(Shape):
    _js_attrs = Shape._js_attrs | {'value', 'font', 'size', 'bold', 'italic'}
    _init_attrs = (Shape._init_attrs | {'bold', 'italic', 'size', 'font'}) - {'dashes'}

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
        if app is not None and app._app._isMvc:
            raise NotImplementedError("Whoops! Group objects are not available in CS3 Mode.")
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

SHAPES = [ Arc, Circle, Image, Label, Line, Oval,
            Polygon, Rect, RegularPolygon, Star, ]

APP_FN_NAMES = ['onAppStart',
                  'onKeyPress', 'onKeyHold', 'onKeyRelease',
                  'onMousePress', 'onMouseDrag', 'onMouseRelease',
                  'onMouseMove', 'onStep', 'redrawAll']

class NoMvc():
    def __enter__(self):
        self.oldMvc = app._app._isMvc
        app._app._isMvc = False

    def __exit__(self, excType, excValue, tb):
        app._app._isMvc = self.oldMvc

def makeDrawFn(shape):
    def drawFn(*args, **kwargs):
        if (not app._app._isMvc):
            raise Exception(f'You called draw{shape.__name__} (a CS3 Mode function) outside of redrawAll.')
        if (not app._app.inRedrawAll):
            raise MvcException('Cannot draw (modify the view) outside of redrawAll')
        with NoMvc():
            shape(*args, **kwargs)
    return drawFn

def makeInvisibleConstructor(shape):
    def constructor(*args, **kwargs):
        if (not app._app._isMvc):
            raise Exception(f'You called {shape.__name__}Shape (a CS3 Mode function) outside of CS3 Mode. To run your app in CS3 Mode, use runApp().')
        with NoMvc():
            result = shape(*args, **kwargs)
        result.visible = False
        return result
    return constructor

def createDrawingFunctions():
    g = globals()
    for shape in SHAPES:
        shapeName = shape.__name__
        if shapeName == 'Group':
            continue
        g['draw' + shapeName] = makeDrawFn(shape)
        g[shapeName + 'Shape'] = makeInvisibleConstructor(shape)

createDrawingFunctions()

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

def cleanAndClose():
    shape_logic.cleanSoundProcesses()
    os._exit(0)

def _safeMethod(appMethod):
    def m(*args, **kwargs):
        app = args[0]
        try:
            return appMethod(*args, **kwargs)
        except Exception as e:
            sys.excepthook(*sys.exc_info())
            app.stop()
            if app._running:
                app.drawErrorScreen()
            else:
                cleanAndClose()
    return m

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

    def getPosArgCount(self, fn):
        fn_code = fn.__code__
        pos_count = fn_code.co_argcount
        arg_names = fn_code.co_varnames
        return len(arg_names[:pos_count])

    def usesControl(self, fn):
        fn_code = fn.__code__
        return 'control' in fn_code.co_consts

    def getFnNameAndLanguage(self, enFnName):
        if enFnName in self.userGlobals:
            return enFnName, 'en'

        for language in shape_logic.TRANSLATED_USER_FUNCTION_NAMES:
            if language == 'keys': continue
            if enFnName in shape_logic.TRANSLATED_USER_FUNCTION_NAMES[language]:
                fnTranslations = shape_logic.TRANSLATED_USER_FUNCTION_NAMES[language][enFnName]
                for fnTranslation in fnTranslations:
                    if (fnTranslation in self.userGlobals):
                        return fnTranslation, language

        return None, None

    def translateEventHandlerArgs(self, enFnName, language, args):
        if enFnName == 'onKeyHold':
            args = ([translateKeyName(x, language) for x in args[0]], )
        elif enFnName in ('onKeyPress', 'onKeyRelease'):
            args = (translateKeyName(args[0], language), args[1])

        return args

    def getEventHandlerArgs(self, enFnName, language, fn, args, kwargs):
        if language != 'en':
            args = self.translateEventHandlerArgs(enFnName, language, args)

        if self._isMvc:
            args = (self._wrapper,) + args

        if enFnName in ('onKeyPress', 'onKeyRelease', 'onKeyHold'):
            if self.getPosArgCount(fn) < len(args):
                args = args[:-1]
            elif self.shouldPrintCtrlWarning and self.usesControl(fn):
                print('INFO: To use the control key in your app without')
                print('enabling the inspector, set app.inspectorEnabled')
                print('to False. To stop this message from printing,')
                print('set app.inspectorEnabled to True.')
                self.shouldPrintCtrlWarning = False

        return args, kwargs

    @_safeMethod
    def callUserFn(self, enFnName, args, kwargs=None):
        if kwargs is None:
            kwargs = dict()

        fnName, language = self.getFnNameAndLanguage(enFnName)
        if fnName is None:
            return

        fn = self.userGlobals[fnName]
        args, kwargs = self.getEventHandlerArgs(enFnName, language, fn, args, kwargs)

        fn(*args, **kwargs)

        if self._isMvc and enFnName != 'redrawAll':
            self.redrawAllWrapper()

    def redrawAllWrapper(self):
        self.group.clear()

        self.inRedrawAll = True
        self.callUserFn('redrawAll', ())
        self.inRedrawAll = False

    @staticmethod
    def getKey(keyCode, modifierMask):
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
            if (modifierMask & pygame.KMOD_SHIFT):
                key = shiftMap.get(key, key).upper()
            return key
        return keyNameMap.get(keyCode, None)

    def drawErrorScreen(self):
        cairo_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.width, self.height)
        ctx = cairo.Context(cairo_surface)

        with NoMvc():
            Rect(0, 0, self.width, self.height, fill=None, border='red', borderWidth=2)
            Rect(10, self.height - 60, self.width - 20, 50, fill='white', border='red', borderWidth=4)
            Label('Exception! App Stopped!', self.width / 2, self.height - 45, size=12, bold=True, font='Arial', fill='red')
            Label('See console for details', self.width / 2, self.height - 25, size=12, bold=True, font='Arial', fill='red')

        self.redrawAll(self._screen, cairo_surface, ctx)

    def getModifiers(self, modifierMask):
        modifiers = list()
        if (modifierMask & pygame.KMOD_SHIFT):
            modifiers.append('shift')
        if (modifierMask & pygame.KMOD_CTRL):
            modifiers.append('control')
        if (modifierMask & pygame.KMOD_META):
            modifiers.append('meta')
        return modifiers

    def handleKeyPress(self, keyCode, modifierMask):
        self._modifiers = self.getModifiers(modifierMask)
        key = App.getKey(keyCode, modifierMask)

        if key is None: return
        if key == 'ctrl':
            self.isCtrlKeyDown = True
            return
        if key == 'space' and (modifierMask & pygame.KMOD_SHIFT):
            self.paused = not self.paused
            return

        self._allKeysDown.add(key)

        modifiers = self.getModifiers(modifierMask)
        self.callUserFn('onKeyPress', (key, modifiers))

    def handleKeyRelease(self, keyCode, modifierMask):
        self._modifiers = self.getModifiers(modifierMask)
        key = App.getKey(keyCode, modifierMask)

        if key is None: return
        if key == 'ctrl':
            self.isCtrlKeyDown = False
            return
        if key.upper() in self._allKeysDown: self._allKeysDown.remove(key.upper())
        if key.lower() in self._allKeysDown: self._allKeysDown.remove(key.lower())

        modifiers = self.getModifiers(modifierMask)
        self.callUserFn('onKeyRelease', (key, modifiers))

    def redrawAll(self, screen, cairo_surface, ctx):
        shape = shape_logic.Rect({
            'noGroup': True,
            'top': 0,
            'left': 0,
            'width': self.width,
            'height': self.height,
            'fill': self.background or 'white',
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
        pygame.display.flip()
        
        self.frameworkRedrew = True

    def shouldDrawInspector(self):
        return (
            self.inspectorEnabled and
            (self.paused or
                self.alwaysShowInspector or
                self.isCtrlKeyDown)
        )

    def __init__(self):
        self.userGlobals = __main__.__dict__
        try:
            self.title, _ = os.path.splitext(os.path.basename(os.path.realpath(__main__.__file__)))
        except:
            self.title = "CMU CS Academy"

        self._width = 400
        self._height = 400
        self._allKeysDown = set()
        self._modifiers = set()
        self.background = None

        self._stepsPerSecond = 30

        self._tlg = Group()
        sli.setTopLevelGroup(self._tlg)

        self.paused = False
        self._stopped = False
        self._running = False
        self.textInputs = []

        self.inspector = shape_logic.Inspector(self)
        self._inspectorEnabled = True
        self.shouldPrintCtrlWarning = True
        self.alwaysShowInspector = False
        self.isCtrlKeyDown = False

        self._isMvc = False
        self._ranWithScreens = False

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

    def getStepsPerSecond(self):
        return self._stepsPerSecond
    def setStepsPerSecond(self, value):
        shape_logic.checkNumber(sli.t('app'), 'stepsPerSecond', value, False)
        self._stepsPerSecond = value
    stepsPerSecond = property(getStepsPerSecond, setStepsPerSecond)

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

    def onResize(self, newScreen=True):
        if not self._running:
            return
        self.updateScreen(newScreen)
        self.callUserFn('onResize', ())
        self.redrawAllWrapper()

    def getLeft(self):
        return 0
    def setLeft(self, value):
        raise Exception('App.left is readonly')
    left = property(getLeft, setLeft)

    def getRight(self):
        return self._width
    def setRight(self, value):
        if not self._isMvc:
            raise Exception('App.right is readonly')
        self._width = value
        self.onResize()
    right = property(getRight, setRight)

    def getTop(self):
        return 0
    def setTop(self, value):
        raise Exception(t('App.top is readonly'))
    top = property(getTop, setTop)

    def getBottom(self):
        return self._height
    def setBottom(self, value):
        if not self._isMvc:
            raise Exception('App.bottom is readonly')
        self._height = value
        self.onResize()
    bottom = property(getBottom, setBottom)

    def getWidth(self):
        return self._width
    def setWidth(self, value):
        if not self._isMvc:
            raise Exception('App.width is readonly')
        self._width = value
        self.onResize()
    width = property(getWidth, setWidth)

    def getHeight(self):
        return self._height
    def setHeight(self, value):
        if not self._isMvc:
            raise Exception('App.height is readonly')
        self._height = value
        self.onResize()
    height = property(getHeight, setHeight)

    def get_inspectorEnabled(self):
        return self._inspectorEnabled
    def set_inspectorEnabled(self, value):
        self.shouldPrintCtrlWarning = False
        self._inspectorEnabled = value
    inspectorEnabled = property(get_inspectorEnabled, set_inspectorEnabled)

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

    def updateScreen(self, newScreen):
        if newScreen:
            self._screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        self._cairo_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.width, self.height)
        self._ctx = cairo.Context(self._cairo_surface)

    @_safeMethod
    def run(self):
        ### ZIPFILE VERSION ###
        from cmu_graphics.libs import pygame_loader as pg
        ### END ZIPFILE VERSION ###
        ### PYPI VERSION ###
        import pygame as pg
        ### END PYPI VERSION ###
        global pygame
        pygame = pg

        pygame.init()
        pygame.display.set_caption(self.title)

        self._screen = None
        self.updateScreen(True)

        lastTick = 0
        self._running = True

        while self._running:
            sys.stdout.flush()
            with DRAWING_LOCK:
                had_event = False
                for event in pygame.event.get():
                    had_event = True
                    if not self.stopped:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            self.callUserFn('onMousePress', event.pos)
                        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                            self.callUserFn('onMouseRelease', event.pos)
                        elif event.type == pygame.MOUSEMOTION:
                            if event.buttons == (0, 0, 0):
                                self.callUserFn('onMouseMove', event.pos)
                            elif event.buttons[0] == 1:
                                self.callUserFn('onMouseDrag', event.pos)
                        elif event.type == pygame.KEYDOWN:
                            self.handleKeyPress(event.key, event.mod)
                        elif event.type == pygame.KEYUP:
                            self.handleKeyRelease(event.key, event.mod)
                    if event.type == pygame.QUIT:
                        self._running = False
                    elif event.type == pygame.MOUSEMOTION:
                        self.inspector.setMousePosition(*event.pos)
                    elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
                        key = App.getKey(event.key, event.mod)
                        if key == 'ctrl':
                            self.isCtrlKeyDown = (event.type == pygame.KEYDOWN)
                    elif event.type == pygame.VIDEORESIZE:
                        self._width = event.w
                        self._height = event.h
                        self.onResize(False)

                should_redraw = had_event

                msPassed = pygame.time.get_ticks() - lastTick
                if (math.floor(1000 / self.stepsPerSecond) - msPassed < 10):
                    lastTick = pygame.time.get_ticks()
                    if not (self.paused or self.stopped):
                        self.callUserFn('onStep', ())
                        if len(self._allKeysDown) > 0:
                            self.callUserFn('onKeyHold', (list(self._allKeysDown), list(self._modifiers)))
                        should_redraw = True

                if should_redraw:
                    self.redrawAll(self._screen, self._cairo_surface, self._ctx)

                pygame.time.wait(1)

        pygame.quit()
        cleanAndClose()

class MvcException(Exception): pass

class AppWrapper(object):
    readOnlyAttrs = set(['bottom','centerX', 'centerY',
                         'getTextInput', 'left', 'quit', 'right',
                         'run', 'stop', 'top', 'setMaxShapeCount',
                         'printFullTracebacks'])
    readWriteAttrs = set(['height', 'paused', 'stepsPerSecond', 'group',
                          'title', 'width', 'mode', 'background',
                          'beatsPerMinute', 'maxShapeCount', 'inspectorEnabled' ])
    allAttrs = readOnlyAttrs | readWriteAttrs

    def __init__(self, app):
        self._app = app
        app._wrapper = self
        app.mode = ''

    def __dir__(self):
        fields = set(AppWrapper.allAttrs)
        for field in self.__dict__:
            if field not in self._app.__dict__:
                fields.add(field)
        return sorted(fields)

    def __getattribute__(self, attr):
        attr = toEnglish(attr, 'app-attr')
        if (attr == '_app' or not attr in AppWrapper.allAttrs):
            return super().__getattribute__(attr)
        return self._app.__getattribute__(attr)

    def __setattr__(self, attr, value):
        attr = toEnglish(attr, 'app-attr')
        if (attr != '_app') and (getattr(self._app, 'inRedrawAll', False)):
            raise MvcException(f'Cannot change app.{attr} in redrawAll')
        if (attr in AppWrapper.readOnlyAttrs):
            raise Exception(f'app.{attr} is read-only')
        if (attr in AppWrapper.readWriteAttrs):
            return self._app.__setattr__(attr, value)
        return super().__setattr__(attr, value)

def runApp(width=400, height=400, **kwargs):
    if not app._app._ranWithScreens:
        for appFnName in APP_FN_NAMES:
            screenAppSuffix = f'_{appFnName}'
            for globalVarName in app._app.userGlobals:
                if globalVarName.endswith(screenAppSuffix):
                    raise Exception(f'The name of your function "{globalVarName}" ends with "{screenAppSuffix}", which is only allowed if you are using "screens" in CS3 Mode. To run an app with screens, call runAppWithScreens() instead of runApp().')

    setupMvc()
    app.width = width
    app.height = height

    if SHAPES_CREATED > 1:
        raise Exception('''
****************************************************************************
Your code created a shape object (Rect, Oval, etc.) before calling runApp().

runApp (CS3 Mode) is not compatible with shape objects.

If you'd like to use CS3 Mode, please use drawing functions 
(drawRect, drawOval, etc) in redrawAll.

Otherwise, please call cmu_graphics.run() in place of runApp.
****************************************************************************''')

    app._app.callUserFn('onAppStart', (), kwargs)
    app._app.redrawAllWrapper() # Draw even if there are no events

    run()

def setActiveScreen(screen):
    if (not app._app._isMvc):
        raise Exception('You called setActiveScreen (a CS3 Mode function) outside of CS3 Mode. To run your app in CS3 Mode, use runApp() or runAppWithScreens().')
    if (screen in [None, '']) or (not isinstance(screen, str)):
        raise Exception(f'{repr(screen)} is not a valid screen')
    redrawAllFnName = f'{screen}_redrawAll'
    if redrawAllFnName not in app._app.userGlobals:
        raise Exception(f'Screen {screen} requires {redrawAllFnName}()')
    app._app.activeScreen = screen

def runAppWithScreens(initialScreen, *args, **kwargs):
    userGlobals = app._app.userGlobals

    def checkForAppFns():
        for appFnName in APP_FN_NAMES:
            if appFnName in userGlobals:
                raise Exception(f'Do not define {appFnName} when using screens')

    def getScreenFnNames(appFnName):
        screenFnNames = [ ]
        for globalVarName in userGlobals:
            screenAppSuffix = f'_{appFnName}'
            if globalVarName.endswith(screenAppSuffix):
                screenFnNames.append(globalVarName)
        return screenFnNames

    def makeAppFnWrapper(appFnName):
        if appFnName == 'onAppStart':
            def onAppStartWrapper(app):
                for screenFnName in getScreenFnNames('onScreenStart'):
                    screenFn = userGlobals[screenFnName]
                    screenFn(app)
            return onAppStartWrapper
        else:
            def appFnWrapper(*args):
                screen = app._app.activeScreen
                screenFnName = f'{screen}_{appFnName}'
                if screenFnName in userGlobals:
                    screenFn = userGlobals[screenFnName]
                    return screenFn(*args)
            return appFnWrapper

    def wrapScreenFns():
        for appFnName in APP_FN_NAMES:
            screenFnNames = getScreenFnNames(appFnName)
            if (screenFnNames != [ ]) or (appFnName == 'onAppStart'):
                userGlobals[appFnName] = makeAppFnWrapper(appFnName)

    def go():
        app._app._ranWithScreens = True
        checkForAppFns()
        wrapScreenFns()
        app._app._isMvc = True
        setActiveScreen(initialScreen)
        runApp(*args, **kwargs)

    go()

def getImageSize(url):
    image = Image(url, 0, 0, visible=False)
    return (image.width, image.height)

def setupMvc():
    app._app._isMvc = True
    app._app.inRedrawAll = False
    del app._app.userGlobals['app']
    AppWrapper.readWriteAttrs.remove('paused')
    AppWrapper.allAttrs.remove('paused')

def processArgs(fname, params, args):
    # Check for too many positional arguments
    if len(args) > len(params):
        argStr = 'argument' if len(params) == 1 else 'arguments'
        raise TypeError(f'{fname}() takes {len(params)} positional {argStr} but more were given')

    # Check for not enough positional arguments
    if len(params) > len(args):
        missingCount = len(params) - len(args)
        argStr = 'argument' if missingCount == 1 else 'arguments'
        paramsStr = ', '.join([repr(param) for param in params[len(args):]])
        raise TypeError(f'{fname}() missing {missingCount} required positional {argStr}: {paramsStr}')

def eventHandlerRepeater(f):
    sig = inspect.signature(f)
    params = tuple(sig.parameters.keys())
    def g(*args):
        testParams = params
        if app._app._isMvc:
            testParams = ('app',) + testParams
        processArgs(f.__name__, testParams, args)
        if app._app._isMvc:
            args = args[1:]
        f(*args)
    return g

@eventHandlerRepeater
def onSteps(n):
    for _ in range(n):
        app._app.callUserFn('onStep', ())

@eventHandlerRepeater
def onKeyHolds(keys, n):
    assert isinstance(keys, list), t('keys must be a list')
    for _ in range(n):
        app._app.callUserFn('onKeyHold', (keys, []))

@eventHandlerRepeater
def onKeyPresses(key, n):
    for _ in range(n):
        app._app.callUserFn('onKeyPress', (key, []))

def loop():
    run()

def run():
    if not app._app._isMvc:
        for cs3ModeHandler in ('onAppStart', 'redrawAll'):
            if cs3ModeHandler in __main__.__dict__:
                raise Exception(f"You defined the event handler {cs3ModeHandler} which works with CS3 mode, and then called cmu_graphics.run(), which doesn't work with CS3 mode. Did you mean to call runApp instead?")

    global MAINLOOP_RUN
    MAINLOOP_RUN = True

    if not os.environ.get('CI', False):
        t = threading.Thread(target=CSAcademyConsole().interact).start()

    try:
        app._app.run()
    except KeyboardInterrupt:
        cleanAndClose()

from code import InteractiveConsole
class CSAcademyConsole(InteractiveConsole):
    def __init__(self):
        self.__class__.__name__ = "CS Academy Console"
        __main__.__dict__['exit'] = lambda: cleanAndClose()
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

    # Override interact so we can exit on EOF
    def interact(self):
        super().interact()
        cleanAndClose()

import os
import sys
from datetime import datetime
from datetime import timedelta
import json
import subprocess
from cmu_graphics.libs import webrequest
import __main__


UPDATE_CONFIG_FILE_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'meta',
    'updates.json',
)

def get_update_info():
    if os.path.exists(UPDATE_CONFIG_FILE_PATH):
        with open(UPDATE_CONFIG_FILE_PATH, 'r') as f:
            return json.loads(f.read())
    return {}

def save_update_info(update_info):
    with open(UPDATE_CONFIG_FILE_PATH, 'w') as f:
        f.write(json.dumps(update_info))

def check_for_update():
    try:
        update_info = get_update_info()

        current_directory = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(current_directory, 'meta', 'version.txt')) as f:
            version = f.read().strip()

        last_attempt = None
        if 'last_attempt' in update_info:
            last_attempt = datetime.fromtimestamp(update_info['last_attempt'])

        if last_attempt is None or (datetime.now() - last_attempt > timedelta(days=1)):
            most_recent_version = webrequest.get(
                'https://s3.amazonaws.com/cmu-cs-academy.lib.prod/desktop-cmu-graphics/version.txt'
            ).read().decode('ascii').strip()

            update_info['last_attempt'] = datetime.now().timestamp()
            update_info['most_recent_version'] = most_recent_version
            save_update_info(update_info)
        else:
            most_recent_version = update_info.get('most_recent_version', version)

        if most_recent_version > version:
            print(f'\n\nYou are running cmu-graphics version {version}, but a newer version {most_recent_version} is available.')
            ### ZIPFILE VERSION ###
            print('Visit https://academy.cs.cmu.edu/desktop to upgrade.')
            ### END ZIPFILE VERSION ###
            ### PYPI VERSION ###
            print('Run "pip install --upgrade cmu-graphics" to upgrade.')
            ### END PYPI VERSION ###
            print('\n\n')
    except:
        pass

if 'CMU_GRAPHICS_NO_UPDATE' not in __main__.__dict__:
    check_for_update()

def print_debug_info():
    import platform
    current_directory = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(current_directory, 'meta', 'version.txt')) as f:
        version = f.read().strip()
    print('='*80)
    print('CMU Graphics Version:', version)
    print('Platform:', sys.platform)
    print('Python Version:', '.'.join(platform.python_version_tuple()))
    print('Executable Path:', sys.executable)
    print('Working Directory:', current_directory)
    print('='*80)

if 'CMU_GRAPHICS_DEBUG' in __main__.__dict__:
    print_debug_info()

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import math
### ZIPFILE VERSION ###
from cmu_graphics.libs import cairo_loader as cairo
### END ZIPFILE VERSION ###
### PYPI VERSION ###
import cairo
### END PYPI VERSION ###
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

SHAPES_CREATED = 0
MAINLOOP_RUN = False

# Checks to see if a user created shapes but did not call
# cmu_graphics.run()
def check_for_exit_without_run():
    global SHAPES_CREATED, MAINLOOP_RUN

    # The app's top level group is created even if the user creates no
    # shapes on their own
    if SHAPES_CREATED > 1 and not MAINLOOP_RUN:
        print("""
                         (
                    (    (
                    ((  (*(
                    (*( (*/
                    (**.***,
                    (***************((((((((((((((((
                    (********************************
                    (*******************************(
                    (*******************************(
                    (*******************************(
                    /*******************************(
                    (/******************(((((((     ((
                (*****(****************,
                /**********(************(
            ((***************(*********
                (*****(/*********(*****(
                    (**********/(/***(*/
                    (****************(
                        (/***********(
                            (*******(
                            (**(
""")
        print(" ** To run your animation, add cmu_graphics.run() to the bottom of your file **\n")

app = None
app = AppWrapper(App())
atexit.register(check_for_exit_without_run)
