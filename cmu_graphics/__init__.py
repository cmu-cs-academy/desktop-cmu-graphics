import __main__
import os
import sys


def check_for_shadowing():
    #   If the current working directory or the __main__ script's directory
    # are in sys.path and contain files with the same name as modules used
    # by cmu_graphics, complain.
    #   Note that there could be other directories in sys.path that contain
    # files that shadow installed modules that cmu_graphics imports. We are
    # currently not aware of a way to distinguish between "user" directories
    # in sys.path and "system" directories in sys.path, so we just consider
    # the two directories mentioned above.

    directories_to_look_for_shadowing = []

    # If the current working directory is in sys.path, consider it for shadowing
    if '' in sys.path:
        directories_to_look_for_shadowing.append(os.path.abspath('.'))

    # If the __main__ file's directory is in sys.path, consider it for shadowing
    # (When running in the Python 3.13 REPL, __main__.__file__ is not in sys.path.)
    if main_file := getattr(__main__, '__file__', None):
        main_directory = os.path.dirname(main_file)
        if main_directory in sys.path:
            directories_to_look_for_shadowing.append(main_directory)

    # disallowed_filenames was generated by running this code at the end of cmu_graphics.py:
    # import sys
    # print('\n'.join(sorted(f"'{x}'," for x in list(sys.modules.keys()) if '.' not in x)))
    disallowed_filenames = {
        f'{x}.py'
        for x in [
            '__future__',
            '__main__',
            '_abc',
            '_ast',
            '_bisect',
            '_blake2',
            '_bz2',
            '_codecs',
            '_collections',
            '_collections_abc',
            '_compression',
            '_datetime',
            '_decimal',
            '_frozen_importlib',
            '_frozen_importlib_external',
            '_functools',
            '_hashlib',
            '_heapq',
            '_imp',
            '_io',
            '_json',
            '_locale',
            '_lzma',
            '_opcode',
            '_operator',
            '_posixsubprocess',
            '_queue',
            '_random',
            '_scproxy',
            '_sha2',
            '_signal',
            '_sitebuiltins',
            '_socket',
            '_sre',
            '_ssl',
            '_stat',
            '_string',
            '_struct',
            '_thread',
            '_tokenize',
            '_uuid',
            '_warnings',
            '_weakref',
            '_weakrefset',
            'abc',
            'array',
            'ast',
            'atexit',
            'base64',
            'binascii',
            'bisect',
            'builtins',
            'bz2',
            'cairo',
            'calendar',
            'cmu_graphics',
            'code',
            'codecs',
            'codeop',
            'collections',
            'contextlib',
            'copy',
            'copyreg',
            'datetime',
            'decimal',
            'dis',
            'email',
            'encodings',
            'enum',
            'errno',
            'fcntl',
            'fnmatch',
            'functools',
            'genericpath',
            'hashlib',
            'heapq',
            'http',
            'importlib',
            'inspect',
            'io',
            'ipaddress',
            'itertools',
            'json',
            'keyword',
            'linecache',
            'locale',
            'lzma',
            'marshal',
            'math',
            'numbers',
            'opcode',
            'operator',
            'os',
            'platform',
            'posix',
            'posixpath',
            'pygame',
            'queue',
            'quopri',
            'random',
            're',
            'reprlib',
            'select',
            'selectors',
            'shutil',
            'signal',
            'site',
            'socket',
            'ssl',
            'stat',
            'string',
            'struct',
            'subprocess',
            'sys',
            'tempfile',
            'textwrap',
            'threading',
            'time',
            'token',
            'tokenize',
            'traceback',
            'types',
            'unicodedata',
            'urllib',
            'uuid',
            'warnings',
            'weakref',
            'zipimport',
            'zlib',
        ]
    }

    for directory in directories_to_look_for_shadowing:
        sibling_filenames = set(os.listdir(directory))
        overlap_filenames = sorted(list(sibling_filenames & disallowed_filenames))

        if overlap_filenames:
            raise Exception(f"""

        ******************************************************************************
        * The following files in {directory}
        * may prevent your program from running correctly. Please rename or remove
        * these files:
        *
        * {', '.join(overlap_filenames)}
        ******************************************************************************
        """)


check_for_shadowing()

from .libs import loader_util

loader_util.verify_support()

from cmu_graphics.cmu_graphics import (
    app,
    Arc,
    Circle,
    Group,
    Image,
    Label,
    Line,
    Oval,
    Polygon,
    Rect,
    RegularPolygon,
    Star,
    drawArc,
    drawCircle,
    drawImage,
    drawLabel,
    drawLine,
    drawOval,
    drawPolygon,
    drawRect,
    drawRegularPolygon,
    drawStar,
    ArcShape,
    CircleShape,
    ImageShape,
    LabelShape,
    LineShape,
    OvalShape,
    PolygonShape,
    RectShape,
    RegularPolygonShape,
    StarShape,
    Sound,
    gradient,
    rgb,
    almostEqual,
    rounded,
    round,
    dcos,
    dsin,
    onSteps,
    onKeyHolds,
    onKeyPresses,
    setLanguage,
    print,
    assertEqual,
    Robot,
    runApp,
    runAppWithScreens,
    setActiveScreen,
    getImageSize,
    pygameEvent,
    onStepEvent,
    onMainLoopEvent,
)

from cmu_graphics.utils import (
    angleTo,
    distance,
    fromPythonAngle,
    getPointInDir,
    makeList,
    pythonRound,
    toPythonAngle,
)

from random import (
    choice,
    random,
    randrange,
    seed,
)

from cmu_graphics.shape_logic import (
    TRANSLATED_GLOBALS,
    TRANSLATED_BOOLEANS,
    TRANSLATED_KEY_NAMES,
    accentCombinations,
    PILWrapper as CMUImage,
)

__all__ = TRANSLATED_GLOBALS['keys']
__all__.extend(
    [
        'setLanguage',
        'cmu_graphics',
        'runApp',
        'runAppWithScreens',
        'setActiveScreen',
        'getImageSize',
        'dcos',
        'dsin',
    ]
)
__all__.extend(
    [
        'drawArc',
        'ArcShape',
        'drawCircle',
        'CircleShape',
        'drawImage',
        'ImageShape',
        'drawLabel',
        'LabelShape',
        'drawLine',
        'LineShape',
        'drawOval',
        'OvalShape',
        'drawPolygon',
        'PolygonShape',
        'drawRect',
        'RectShape',
        'drawRegularPolygon',
        'RegularPolygonShape',
        'drawStar',
        'StarShape',
    ]
)

g = globals()
for language in TRANSLATED_GLOBALS:
    if language != 'keys':
        for en_name, trans_name in TRANSLATED_GLOBALS[language].items():
            if trans_name and trans_name != en_name and en_name in g:
                for accent_combination in accentCombinations(trans_name):
                    g[accent_combination] = g[en_name]
                    __all__.append(accent_combination)

for language in TRANSLATED_BOOLEANS:
    if language != 'keys':
        for en_name, trans_name in TRANSLATED_BOOLEANS[language].items():
            globals()[trans_name] = en_name == 'True'
            __all__.append(trans_name)

__all__ = list(set(__all__))
