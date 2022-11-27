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
)

from cmu_graphics.utils import (
    angleTo,
    distance,
    fromPythonAngle,
    getPointInDir,
    makeList,
    rounded,
    pythonRound,
    toPythonAngle
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
    PILWrapper as CMUImage
)

__all__ = TRANSLATED_GLOBALS['keys']
__all__.extend(['setLanguage', 'cmu_graphics', 'runApp', 'runAppWithScreens', 'setActiveScreen', 'getImageSize'])
__all__.extend(['drawArc', 'ArcShape', 'drawCircle', 'CircleShape', 'drawImage', 'ImageShape', 'drawLabel', 'LabelShape', 'drawLine', 'LineShape', 'drawOval', 'OvalShape', 'drawPolygon', 'PolygonShape', 'drawRect', 'RectShape', 'drawRegularPolygon', 'RegularPolygonShape', 'drawStar', 'StarShape'])

g = globals()
for language in TRANSLATED_GLOBALS:
    if language != 'keys':
        for (en_name, trans_name) in TRANSLATED_GLOBALS[language].items():
            if trans_name and trans_name != en_name and en_name in g:
                for accent_combination in accentCombinations(trans_name):
                    g[accent_combination] = g[en_name]
                    __all__.append(accent_combination)

for language in TRANSLATED_BOOLEANS:
    if language != 'keys':
        for (en_name, trans_name) in TRANSLATED_BOOLEANS[language].items():
            globals()[trans_name] = en_name == 'True'
            __all__.append(trans_name)

__all__ = list(set(__all__))