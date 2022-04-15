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

g = globals()
for language in TRANSLATED_GLOBALS:
    if language != 'keys':
        for (en_name, trans_name) in TRANSLATED_GLOBALS[language].items():
            if trans_name and trans_name != en_name and en_name in g:
                for accent_combination in accentCombinations(trans_name):
                    g[accent_combination] = g[en_name]
                    __all__.append(accent_combination)

__all__.append('setLanguage')
__all__.append('cmu_graphics')

for language in TRANSLATED_BOOLEANS:
    if language != 'keys':
        for (en_name, trans_name) in TRANSLATED_BOOLEANS[language].items():
            globals()[trans_name] = en_name == 'True'
            __all__.append(trans_name)

__all__ = list(set(__all__))