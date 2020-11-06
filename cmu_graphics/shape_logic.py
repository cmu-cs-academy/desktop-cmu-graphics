import math
import copy
import os
from cmu_graphics import utils
from cmu_graphics.libs import cairo_loader as cairo
from cmu_graphics.libs import pil_image_loader as Image
from cmu_graphics.libs import webrequest
from io import BytesIO
import array
import sys
import traceback
import atexit
import subprocess
import json

class CMUException(Exception): pass

def printTraceback(exceptionType, exception, tb):
    stack = traceback.extract_tb(tb)
    lines = (''.join(traceback.format_list(stack))).splitlines()

    print('An error occurred. Here is the stack trace:')
    hasSourceLines = False

    while (lines):
        try:
            line = lines.pop(0)
            if ', in ' in line:
                line = line[:line.index(', in ')]
            lineNumberLineParts = line.split()
            module = lineNumberLineParts[1]
            lineNumber = int(lineNumberLineParts[-1])
            if (lines and lines[0].startswith('    ')):
                codeLine = lines.pop(0)

            if not (('loop()' in codeLine)
                or ('cmu_graphics.py' in module)
                or ('shape_logic.py' in module)):

                print('  %s line %d:\n    %s' % (module, lineNumber, codeLine))
        except:
            pass

    # Remove 'shape_logic.' from the name of any exceptions being printed
    if exceptionType != CMUException:
        print(exceptionType.__name__ + ': ' + str(exception))
    else:
        print('Exception: ' + str(exception))

import __main__
if 'CMU_GRAPHICS_DEBUG' not in __main__.__dict__:
    sys.excepthook = printTraceback

def printFullTracebacks():
    sys.excepthook = sys.__excepthook__

def pyThrow(err): raise CMUException(err)

def typeError(obj, attr, value, typeName):
    if (type(obj) == str):
        callSpec = '{attr} in {obj}'.format(attr=attr, obj=obj)
    else:
        callSpec = '{className}.{attr}'.format(className=obj.__class__.__name__, attr=attr)
    valueType = type(value).__name__
    err = 'Type Error: {callSpec} should be {typeName} (but {value} is of type {valueType})'.format(
        callSpec=callSpec, typeName=typeName, value=value, valueType=valueType
    )
    pyThrow(err)

def checkArgCount(clsName, fnName, argNames, args):
    if (len(argNames) != len(args)):
        if (clsName and fnName):
            callSpec = '{clsName}.{fnName}'.format(clsName=clsName, fnName=fnName)
        else:
            callSpec = (clsName or fnName)
        pyThrow('Arg Count Error: {callSpec}() takes {argNamesLength} arguments ({args}), not {argLength}'.format(
            callSpec=callSpec, argNamesLength=len(argNames), args=",".join(argNames), argLength=len(args)
        ))

def checkInt(obj, attr, value):
    if type(value) != int: typeError(obj, attr, value, 'integer')

def checkNumber(obj, attr, value):
    if type(value) != int and type(value) != float:
        typeError(obj, attr, value, 'Number')

def checkPositive(obj, attr, value):
    checkNumber(obj, attr, value);
    if (value <= 0): typeError(obj, attr, value, 'positive-number')

def checkNonNegative(obj, attr, value):
    checkNumber(obj, attr, value)
    if (value < 0): typeError(obj, attr, value, 'non-negative number')

def checkRange(obj, attr, value, lo, hi):
    if ((value < lo) or (value > hi)): typeError(obj, attr, value, 'number-in-range-{lo}-{hi}'.format(lo=lo,hi=hi))

def checkValue(obj, attr, value): pass

def checkIntInRange(obj, attr, value, lo, hi):
    checkInt(obj, attr, value)
    checkRange(obj, attr, value, lo, hi)

def checkNumberInRange(obj, attr, value, lo, hi):
    checkNumber(obj, attr, value)
    checkRange(obj, attr, value, lo, hi)

def checkNumberIn0To100(obj, attr, value):
    checkNumberInRange(obj, attr, value, 0, 100)

def checkShape(obj, attr, value):
    if not isinstance(value, Shape):
        typeError(obj, attr, value, 'Shape')

def checkWidthHeight(obj, attr, value):
    if (isinstance(obj, Rect)
        or isinstance(obj, Oval)
        or isinstance(obj, PolygonInCircle)):

        return checkPositive(obj, attr, value)
    return checkNonNegative(obj, attr, value)

def checkColor(obj, attr, value):
    if value == None: return
    if isinstance(value, RGB): return
    if isinstance(value, Gradient): return
    if not isinstance(value, str):
        typeError(obj, attr, value, 'color')

    if any(color.lower() == value.lower() for color in CSS3_COLORS_TO_RGB):
        return

    objName = obj if isinstance(obj, str) else obj.__class__.__name__
    pyThrow('Type Error: {objName} {attr} should be a color, and {value} is not a legal color name'.format(
        objName=objName, attr=attr, value=value
    ))

def checkBoolean(obj, attr, value):
    if type(value) != bool: typeError(obj, attr, value, 'bool')

def checkArray(obj, attr, value):
    if type(value) != list and type(value) != tuple: typeError(obj, attr, value, 'list')

def checkString(obj, attr, value):
    if type(value) != str: typeError(obj, attr, value, 'string')

def checkBooleanOrArray(obj, attr, value):
    if type(value) != list and type(value) != tuple: checkBoolean(obj, attr, value)

def checkAlign(obj, attr, value):
    if value == None: return # None is a legal align
    if not value in aligns:
        pyThrow('Type Error: in {className} {attr}, {value} is not a legal align value'.format(
            className=obj.__class__.__name__,attr=attr,value=value
        ))

def checkNumPoints(obj, attr, value):
    checkInt(obj, attr, value)
    if (value < 3): typeError(obj, attr, value, 'number-greater-than-2')

def checkRoundness(obj, attr, value):
    if (value is None): return # None is a legal roundness
    checkNumberIn0To100(obj, attr, value)

def checkSweepAngle(obj, attr, value):
    checkNumberInRange(obj, attr, value, 0, 360)

def toColorObject(v):
    if not v: return 'None'
    if isinstance(v, str): return CSS3_COLORS_TO_RGB[v.lower()] or v
    if isinstance(v, RGB) or isinstance(v, Gradient): return v
    raise Exception('toColorObject: unknown color type: {t}'.format(t=type(v)))

def RGBAlmostEqual(v1, v2, epsilon = None):
    if epsilon == None: epsilon = 2
    colorPairs = [[v1.red, v2.red], [v1.green, v2.green], [v1.blue, v2.blue]]
    return all(abs(pair[0] - pair[1]) <= epsilon for pair in colorPairs)

def RGBListAlmostEqual(v1, v2, epsilon):
    if len(v1) != len(v2): return False
    for i in range(len(v1)):
        if type(v1[i]) != type(v2[i]): return False
        if isinstance(v1[i], RGB):
            if not RGBAlmostEqual(v1[i], v2[i], epsilon): return False
        elif isinstance(v1[i], list) or isinstance(v[i], tuple):
            if not RGBListAlmostEqual(v1[i], v2[i], epsilon): return False
        else:
            raise Exception('RGBListAlmostEqual: invalid type: {t}'.format(t=v1[i]))
    return True

def reflectGradientStart(start):
    def toggle(s, a, b):
        if a in s and b in s: raise Exception('Illegal start format: {s}'.format(s=s))
        return s.replace(a, b) if a in s else s.replace(b, a)
    return toggle(toggle(start, 'top', 'bottom'), 'left', 'right')

def colorTest(v1, v2, epsilon):
    v1 = toColorObject(v1)
    v2 = toColorObject(v2)
    if (type(v1) != type(v2)): return 0
    if isinstance(v1, RGB): return 1 if RGBAlmostEqual(v1, v2, epsilon) else 0
    if isinstance(v1, Gradient):
        start1 = canonicalizeGradientStart(v1.start)
        start2 = canonicalizeGradientStart(v2.start)
        if (start1 != start2 and start1 != reflectGradientStart(start2)): return 0
        colors2 = v2.getRGBColors()
        if (start1 != start2):
            colors2.reverse()
        return 1 if RGBListAlmostEqual(v1.getRGBColors(), colors2, epsilon) else 0
    return 1 if v1 == v2 else 0

def eqTest(v1, v2):
    if isinstance(v1, int) or isinstance(v2, float) or isinstance(v2, int) or isinstance(v2, float):
        return 1 if abs(v1 - v2) < 0.005 else 0
    if (isinstance(v1, list) or isinstance(v1, tuple)) and (isinstance(v2, list) or isinstance(v2, tuple)):
        if len(v1) != len(v2): return 0
        for i in range(len(v1)):
            if (eqTest(v1[i], v2[i]) == 0): return 0
        return 1
    return 1 if v1 == v2 else 0

def opacityTest(v1, v2): return eqTest(v1, v2)

aligns = set(['left-top', 'top', 'right-top',
              'left', 'center', 'right',
              'left-bottom', 'bottom', 'right-bottom',
              'top-left', 'top-right', 'bottom-left', 'bottom-right'])

def getAlignAttrs(align):
    if 'left' in align: xattr = 'left'
    elif 'right' in align: xattr = 'right'
    else: xattr = 'centerX'
    if 'top' in align: yattr = 'top'
    elif 'bottom' in align: yattr = 'bottom'
    else: yattr = 'centerY'
    return [xattr, yattr]

def loadImage(path):
    if (path.startswith('http')):
        try:
            response = webrequest.get(path)
            image = Image.open(response)
        except:
            pyThrow('Failed to load image data')
    else:
        image = Image.open(path)

    image = image.convert('RGBA') # ensure we have the correct number of channels
    a = array.array('B', image.tobytes('raw', 'RGBA'))
    surface = cairo.ImageSurface.create_for_data(a, cairo.FORMAT_ARGB32, image.size[0], image.size[1])
    activeDrawing.images[path] = surface
    return {'width': surface.get_width(), 'height': surface.get_height()}

shapeAttrs = dict()
shapeAttrDefaults = dict()

class ShapeAttr(object):
    def __init__(self, name, typeCheckFn, defaultValue):
        self.name = name
        self.typeCheckFn = typeCheckFn
        self.default = defaultValue
        shapeAttrs[name] = self
        shapeAttrDefaults[name] = defaultValue

def initShapeAttrs():
  ShapeAttr('left', checkNumber, 0)
  ShapeAttr('top', checkNumber, 0)
  ShapeAttr('centerX', checkNumber, 0)
  ShapeAttr('centerY', checkNumber, 0)
  ShapeAttr('right', checkNumber, 0)
  ShapeAttr('bottom', checkNumber, 0)
  ShapeAttr('width', checkWidthHeight, 10)
  ShapeAttr('height', checkWidthHeight, 10)
  ShapeAttr('fill', checkColor, 'black')
  ShapeAttr('border', checkColor, None)
  ShapeAttr('borderWidth', checkNonNegative, 2)
  ShapeAttr('dashes', checkBooleanOrArray, False)
  ShapeAttr('opacity', checkNumberIn0To100, 100)
  ShapeAttr('align', checkAlign, None)
  ShapeAttr('rotateAngle', checkNumber, 0)
  ShapeAttr('radius', checkNonNegative, 5)
  ShapeAttr('points', checkNumPoints, 5)
  ShapeAttr('roundness', checkRoundness, 'default')
  ShapeAttr('x1', checkNumber, 0)
  ShapeAttr('y1', checkNumber, 0)
  ShapeAttr('x2', checkNumber, 10)
  ShapeAttr('y2', checkNumber, 10)
  ShapeAttr('arrowStart', checkBoolean, False)
  ShapeAttr('arrowEnd', checkBoolean, False)
  ShapeAttr('lineWidth', checkPositive, 2)
  ShapeAttr('initialPoints', checkArray, [])
  ShapeAttr('closed', checkBoolean, True)
  ShapeAttr('startAngle', checkNumber, 0)
  ShapeAttr('sweepAngle', checkSweepAngle, 360)
  ShapeAttr('value', checkValue, '')
  ShapeAttr('font', checkString, 'arial')
  ShapeAttr('size', checkNonNegative, 12)
  ShapeAttr('bold', checkBoolean, False)
  ShapeAttr('italic', checkBoolean, False)
  ShapeAttr('visible', checkBoolean, True)
  ShapeAttr('url', checkString, None)
  ShapeAttr('db', checkValue, '')
initShapeAttrs()

class RGB(object):
    def __init__(self, red, green, blue):
        self.attrs = {'class': self.__class__.__name__}
        self.red = red
        self.green = green
        self.blue = blue

    def get(self, attr): return self.attrs.get(attr, None)

    def set(self, attr, value):
        checkIntInRange(self, attr, value, 0, 255)
        attrs = self.attrs
        attrs[attr] = value
        attrs['strVal'] = "rgb({red}, {green}, {blue})".format(
            red = self.get('red'), green = self.get('green'), blue = self.get('blue')
        )

    def get_red(self): return self.get('red')
    def set_red(self, v): return self.set('red', v)
    red = property(get_red, set_red)
    def get_green(self): return self.get('green')
    def set_green(self, v): return self.set('green', v)
    green = property(get_green, set_green)
    def get_blue(self): return self.get('blue')
    def set_blue(self, v): return self.set('blue', v)
    blue = property(get_blue, set_blue)

    def darker(self):
        k = 0.85
        return RGB(
            round(k * self.red),
            round(k * self.green),
            round(k * self.blue)
        )

    def lighter(self):
        k = 0.85
        return RGB(
            round(255 - k * (255 - self.red)),
            round(255 - k * (255 - self.green)),
            round(255 - k * (255 - self.blue))
        )

    def toString(self): return self.attrs['strVal']

    def __eq__(self, other):
        if not isinstance(other, RGB): return False
        return self.red == other.red and self.green == other.green and self.blue == other.blue

class Gradient(object): pass

CSS3_COLORS_TO_RGB = {
    "aliceblue": RGB(240, 248, 255),
    "antiquewhite": RGB(250, 235, 215),
    "aqua": RGB(0, 255, 255),
    "aquamarine": RGB(127, 255, 212),
    "azure": RGB(240, 255, 255),
    "beige": RGB(245, 245, 220),
    "bisque": RGB(255, 228, 196),
    "black": RGB(0, 0, 0),
    "blanchedalmond": RGB(255, 235, 205),
    "blue": RGB(0, 0, 255),
    "blueviolet": RGB(138, 43, 226),
    "brown": RGB(165, 42, 42),
    "burlywood": RGB(222, 184, 135),
    "cadetblue": RGB(95, 158, 160),
    "chartreuse": RGB(127, 255, 0),
    "chocolate": RGB(210, 105, 30),
    "coral": RGB(255, 127, 80),
    "cornsilk": RGB(255, 248, 220),
    "cornflowerblue": RGB(100, 149, 237),
    "crimson": RGB(220, 20, 60),
    "cyan": RGB(0, 255, 255),
    "darkblue": RGB(0, 0, 139),
    "darkcyan": RGB(0, 139, 139),
    "darkgoldenrod": RGB(184, 134, 11),
    "darkgray": RGB(169, 169, 169),
    "darkgreen": RGB(0, 100, 0),
    "darkgrey": RGB(169, 169, 169),
    "darkkhaki": RGB(189, 183, 107),
    "darkmagenta": RGB(139, 0, 139),
    "darkolivegreen": RGB(85, 107, 47),
    "darkorange": RGB(255, 140, 0),
    "darkorchid": RGB(153, 50, 204),
    "darkred": RGB(139, 0, 0),
    "darksalmon": RGB(233, 150, 122),
    "darkseagreen": RGB(143, 188, 143),
    "darkslateblue": RGB(72, 61, 139),
    "darkslategray": RGB(47, 79, 79),
    "darkslategrey": RGB(47, 79, 79),
    "darkturquoise": RGB(0, 206, 209),
    "darkviolet": RGB(148, 0, 211),
    "deeppink": RGB(255, 20, 147),
    "deepskyblue": RGB(0, 191, 255),
    "dimgray": RGB(105, 105, 105),
    "dimgrey": RGB(105, 105, 105),
    "dodgerblue": RGB(30, 144, 255),
    "firebrick": RGB(178, 34, 34),
    "floralwhite": RGB(255, 250, 240),
    "forestgreen": RGB(34, 139, 34),
    "fuchsia": RGB(255, 0, 255),
    "gainsboro": RGB(220, 220, 220),
    "ghostwhite": RGB(248, 248, 255),
    "gold": RGB(255, 215, 0),
    "goldenrod": RGB(218, 165, 32),
    "gray": RGB(128, 128, 128),
    "green": RGB(0, 128, 0),
    "greenyellow": RGB(173, 255, 47),
    "grey": RGB(128, 128, 128),
    "honeydew": RGB(240, 255, 240),
    "hotpink": RGB(255, 105, 180),
    "indianred": RGB(205, 92, 92),
    "indigo": RGB(75, 0, 130),
    "ivory": RGB(255, 255, 240),
    "khaki": RGB(240, 230, 140),
    "lavender": RGB(230, 230, 250),
    "lavenderblush": RGB(255, 240, 245),
    "lawngreen": RGB(124, 252, 0),
    "lemonchiffon": RGB(255, 250, 205),
    "lightblue": RGB(173, 216, 230),
    "lightcoral": RGB(240, 128, 128),
    "lightcyan": RGB(224, 255, 255),
    "lightgoldenrodyellow": RGB(250, 250, 210),
    "lightgray": RGB(211, 211, 211),
    "lightgreen": RGB(144, 238, 144),
    "lightgrey": RGB(211, 211, 211),
    "lightpink": RGB(255, 182, 193),
    "lightsalmon": RGB(255, 160, 122),
    "lightseagreen": RGB(32, 178, 170),
    "lightskyblue": RGB(135, 206, 250),
    "lightslategray": RGB(119, 136, 153),
    "lightslategrey": RGB(119, 136, 153),
    "lightsteelblue": RGB(176, 196, 222),
    "lightyellow": RGB(255, 255, 224),
    "lime": RGB(0, 255, 0),
    "limegreen": RGB(50, 205, 50),
    "linen": RGB(250, 240, 230),
    "magenta": RGB(255, 0, 255),
    "maroon": RGB(128, 0, 0),
    "mediumaquamarine": RGB(102, 205, 170),
    "mediumblue": RGB(0, 0, 205),
    "mediumorchid": RGB(186, 85, 211),
    "mediumpurple": RGB(147, 112, 216),
    "mediumseagreen": RGB(60, 179, 113),
    "mediumslateblue": RGB(123, 104, 238),
    "mediumspringgreen": RGB(0, 250, 154),
    "mediumturquoise": RGB(72, 209, 204),
    "mediumvioletred": RGB(199, 21, 133),
    "midnightblue": RGB(25, 25, 112),
    "mintcream": RGB(245, 255, 250),
    "mistyrose": RGB(255, 228, 225),
    "moccasin": RGB(255, 228, 181),
    "navajowhite": RGB(255, 222, 173),
    "navy": RGB(0, 0, 128),
    "oldlace": RGB(253, 245, 230),
    "olive": RGB(128, 128, 0),
    "olivedrab": RGB(107, 142, 35),
    "orange": RGB(255, 165, 0),
    "orangered": RGB(255, 69, 0),
    "orchid": RGB(218, 112, 214),
    "palegoldenrod": RGB(238, 232, 170),
    "palegreen": RGB(152, 251, 152),
    "paleturquoise": RGB(175, 238, 238),
    "palevioletred": RGB(216, 112, 147),
    "papayawhip": RGB(255, 239, 213),
    "peachpuff": RGB(255, 218, 185),
    "peru": RGB(205, 133, 63),
    "pink": RGB(255, 192, 203),
    "plum": RGB(221, 160, 221),
    "powderblue": RGB(176, 224, 230),
    "purple": RGB(128, 0, 128),
    "red": RGB(255, 0, 0),
    "rosybrown": RGB(188, 143, 143),
    "royalblue": RGB(65, 105, 225),
    "saddlebrown": RGB(139, 69, 19),
    "salmon": RGB(250, 128, 114),
    "sandybrown": RGB(244, 164, 96),
    "seagreen": RGB(46, 139, 87),
    "seashell": RGB(255, 245, 238),
    "sienna": RGB(160, 82, 45),
    "silver": RGB(192, 192, 192),
    "skyblue": RGB(135, 206, 235),
    "slateblue": RGB(106, 90, 205),
    "slategray": RGB(112, 128, 144),
    "slategrey": RGB(112, 128, 144),
    "snow": RGB(255, 250, 250),
    "springgreen": RGB(0, 255, 127),
    "steelblue": RGB(70, 130, 180),
    "tan": RGB(210, 180, 140),
    "teal": RGB(0, 128, 128),
    "thistle": RGB(216, 191, 216),
    "tomato": RGB(255, 99, 71),
    "turquoise": RGB(64, 224, 208),
    "violet": RGB(238, 130, 238),
    "wheat": RGB(245, 222, 179),
    "white": RGB(255, 255, 255),
    "whitesmoke": RGB(245, 245, 245),
    "yellow": RGB(255, 255, 0),
    "yellowgreen": RGB(154, 205, 50),
}

gradientStarts = [ 'left-top',     'top',    'right-top',
                   'left',        'center',    'right',
                   'left-bottom', 'bottom', 'right-bottom' ];

alternateGradientStarts = {
  'top-left': 'left-top',
  'top-right': 'right-top',
  'bottom-left': 'left-bottom',
  'bottom-right': 'right-bottom',
}

def canonicalizeGradientStart(start):
    if start in alternateGradientStarts: return alternateGradientStarts[start]
    return start

class Gradient(object):
    def __init__(self, colors, start):
        checkArray(self, 'colors', colors)
        if len(colors) < 2:
            pyThrow('Need to pass at least 2 colors to gradient(); you gave {colorLen}'.format(colorLen=v1[i]))
        for color in colors:
            if color is None:
                pyThrow('Type Error: None cannot be used inside gradient.colors')
            if isinstance(color, Gradient):
                pyThrow('Type Error: {color} cannot be used inside gradient.colors'.format(color=color))
        checkString(self, 'start', start)
        if start not in gradientStarts and start not in alternateGradientStarts:
            pyThrow('Illegal gradient start {start}'.format(start=start))
        self.attrs = {'class': self.__class__.__name__, 'colors': colors, 'start': start}

    def toString(self):
        def quoted(s): return "'{s}'".format(s=s)
        return "gradient({colors}, start='{start}')".format(
            colors = '.'.join(v.toString() if isinstance(v, RGB) else quoted(v) for v in self.colors),
            start = self.start
        )

    def getRGBColors(self):
        return list(map(lambda v: v if isinstance(v, RGB) else CSS3_COLORS_TO_RGB[v.lower()]))

    def toRGBList(self):
        if (self.start == 'center'):
            return self.getRGBColors()
        return sorted([self.getRGBColors(), reversed(self.getRGBColors())])

    def __eq__(self, other):
        if not isinstance(other, Gradient):
            return False
        if len(self.colors) != len(other.colors):
            return False
        if self.start != other.start:
            return False
        for i in range(len(self.colors)):
            c1 = self.colors[i]
            c2 = other.colors[i]
            if type(c1) != type(c2):
                return False
            if c1 != c2:
                return False
        return True

    def __repr__(self):
        return self.toString()

    def __str__(self):
        return self.toString()

    def get_colors(self): return self.attrs['colors']
    colors = property(get_colors)

    def get_start(self): return self.attrs['start']
    start = property(get_start)

class Drawing(object):
    def __init__(self):
        self.tlg = None
        self.images = {}
        self.addCounter = 0
        self.appProperties = {
            'maxShapeCount': 2000
        }

activeDrawing = Drawing()

'''
 Shape
 ├ Group
 ├ Label
 └ Polygon
    ├ Rect
    ├ Line
    ├ PolygonInCircle
    │ ├ RegularPolygon
    │ └ Star
    └ PolygonWithTransform
      ├ CMUImage
      └ Oval
        ├ Arc
        └ Circle
'''

class Shape(object):
    def __init__(self, attrs = None):
        self.group = self.oldGroup = None
        # A list of shapes that this shape was in front of its current/previous group
        self.shapesToBeInFrontOf = []
        self.isGroup = False
        # zIndex is global across all groups
        self.zindex = -1
        self.attrs = {'class': self.__class__.__name__}
        if (not attrs is None):
            if 'defaultAlign' in attrs:
                self.defaultAlign = attrs['defaultAlign']
                del attrs['defaultAlign']
            else:
                self.defaultAlign = 'center'
        self.attrDefaults = shapeAttrDefaults
        if (not attrs is None):
            self.set(attrs)
        if (not attrs or not attrs.get('noGroup', False)) and (activeDrawing.tlg is not None):
            activeDrawing.tlg.add(self)

    def get(self, attr):
        if attr in self.attrs: return self.attrs[attr]
        return self.attrDefaults[attr]

    def setAttr(self, attr, value):
        self.attrs[attr] = value
        return value

    def set(self, attrs):
        result = None
        for attr in attrs:
            value = attrs[attr]
            attrSpec = shapeAttrs.get(attr, None)
            if attrSpec is not None:
                attrSpec.typeCheckFn(self, attr, value)
            result = self.setAttr(attr, value)
            # TODO: Handle labels
        return result

    def get_align(self): pyThrow("You can't get or set the align property")
    def set_align(self, v): pyThrow("You can't get or set the align property")
    align = property(get_align, set_align)

    def get_doNotInspect(self): return self.attrs.get('doNotInspect', None)
    def set_doNotInspect(self, v): self.attrs['doNotInspect'] = v; return v
    doNotInspect = property(get_doNotInspect, set_doNotInspect)

    def get_centerX(self): return self.get('centerX', None)
    def set_centerX(self, v): self.set({'centerX', v}); return v
    centerX = property(get_centerX, set_centerX)

    def get_centerY(self): return self.get('centerY', None)
    def set_centerY(self, v): self.set({'centerY', v}); return v
    centerY = property(get_centerY, set_centerY)

    def get_left(self): return self.centerX - self.width / 2
    def set_left(self, v): self.addx(v - self.left); return v
    left = property(get_left, set_left)

    def get_top(self): return self.centerY - self.height / 2
    def set_top(self, v): self.centerY = v + self.height / 2; return v
    top = property(get_top, set_top)

    def get_right(self): return self.centerX + self.width / 2
    def set_right(self, v): self.centerX = v - self.width / 2; return v
    right = property(get_right, set_right)

    def get_bottom(self): return self.centerY + self.height / 2
    def set_bottom(self, v): self.centerY = v - self.height / 2; return v
    bottom = property(get_bottom, set_bottom)

    def addxy(self, varName = None, d = None):
        if (d == 0): return
        if (varName == 'x'): self.centerX += d
        else: self.centerY += d

    def addx(self, dx): self.addxy('x', dx)
    def addy(self, dy): self.addxy('y', dy)

    def get_centroidX(self): return self.centroid[0]
    def set_centroidX(self, v):
        self.addx(v - self.centroidX)
    centroidX = property(get_centroidX, set_centroidX)

    def get_centroidY(self): return self.centroid[1]
    def set_centroidY(self, v):
        self.addy(v - self.centroidY)
    centroidY = property(get_centroidY, set_centroidY)

    def get_width(self): return self.get('width')
    def set_width(self, v):
        checkPositive(self, 'width', v)
        self.scalexy('x', v / self.width)
        self.set({'width': v})
    width = property(get_width, set_width)

    def get_height(self): return self.get('height')
    def set_height(self, v):
        checkPositive(self, 'height', v)
        self.scalexy('y', v / self.height)
        self.set({'height': v})
    height = property(get_height, set_height)

    def get_fill(self): return self.get('fill')
    def set_fill(self, v): return self.set({'fill': v})
    fill = property(get_fill, set_fill)
    def get_border(self): return self.get('border')
    def set_border(self, v): return self.set({'border': v})
    border = property(get_border, set_border)
    def get_borderWidth(self): return self.get('borderWidth')
    def set_borderWidth(self, v): return self.set({'borderWidth': v})
    borderWidth = property(get_borderWidth, set_borderWidth)
    def get_dashes(self): return self.get('dashes')
    def set_dashes(self, v): return self.set({'dashes': v})
    dashes = property(get_dashes, set_dashes)
    def get_opacity(self): return self.get('opacity')
    def set_opacity(self, v): return self.set({'opacity': v})
    opacity = property(get_opacity, set_opacity)
    def get_closed(self): return self.get('closed')
    def set_closed(self, v): return self.set({'closed': v})
    closed = property(get_closed, set_closed)
    def get_db(self): return self.get('db')
    def set_db(self, v): return self.set({'db': v})
    db = property(get_db, set_db)

    def get_visible(self): return self.get('visible')
    def set_visible(self, v):
        if v == self.visible: return
        self.set({'visible': v})
        if (v):
            if (self.oldGroup):
                self.oldGroup.insert(self)
            else:
                activeDrawing.tlg.add(this)
        else:
            self.group.remove(self)
    visible = property(get_visible, set_visible)

    def doAlign(self, x, y, v):
        [xattr, yattr] = getAlignAttrs(v)
        setattr(self, xattr, x)
        setattr(self, yattr, y)

    def get_centroid(self): return [self.centerX, self.centerY]
    def set_centroid(self, v): pyThrow("Centroid cannot be set")
    centroid = property(get_centroid, set_centroid)

    def getRotateAnchor(self): return self.centroid

    def get_rotateAngle(self): return self.get('rotateAngle')
    def set_rotateAngle(self, v): self.rotate(v - self.rotateAngle)
    rotateAngle = property(get_rotateAngle, set_rotateAngle)

    def rotate(self, degrees = None, cx = None, cy = None):
        if (cx is None and cy is None):
            cx, cy = self.getRotateAnchor()
        checkNumber(self, 'rotate.degrees', degrees)
        checkNumber(self, 'rotate.cx', cx)
        checkNumber(self, 'rotate.cy', cy)
        self.set({'rotateAngle': self.rotateAngle + degrees})
        self.doRotate(degrees, cx, cy)

    def doRotate(self, degrees, cx, cy):
        pyThrow("Must override doRotate method!")

    def toString(self): return 'Shape()'
    def _toString(self): return self.toString() # so cmu_graphics can access toString

    def contains(self, *arguments): # contains(x,y)
        checkArgCount(self.__class__.__name__, 'contains', ['x', 'y'], arguments)
        x, y = arguments
        checkNumber('contains(x, y)', 'x', x)
        checkNumber('contains(x, y)', 'y', y)
        return utils.polygonContainsPoint(self.pointList, x, y)

    def hits(self, *arguments): # hits(x,y)
        checkArgCount(self.__class__.__name__, 'hits', ['x', 'y'], arguments)
        x, y = arguments
        checkNumber('hits(x, y)', 'x', x)
        checkNumber('hits(x, y)', 'y', y)
        pts = self.getApproxPoints()
        if (not utils.polygonContainsPoint(pts, x, y)): return False;
        if (self.fill): return True
        border = self.border
        if (not border): return False;
        # ok, so we have a border, but no fill, so we 'hit' if we
        # are within a borderWidth of the border
        bw = self.borderWidth if border else 0
        return utils.pointNearPolygonBorder(pts, x, y, bw)

    def edgesIntersect(self, shape):
        pts1 = self.getApproxPoints()
        pts2 = shape.getApproxPoints()
        k = None
        for i in range(len(pts1)):
            x1, y1 = pts1[i];
            k = (i + 1) % (len(pts1));
            x2, y2 = pts1[k];
            for j in range(len(pts2)):
                x3, y3 = pts2[j];
                k = (j + 1) % (len(pts2))
                x4, y4 = pts2[k];
                if (utils.segmentsIntersect(x1, y1, x2, y2, x3, y3, x4, y4)):
                    return True
        return False

    def containsShape(self, targetShape):
        checkArgCount(self.__class__.__name__, 'containsShape', ['targetShape'], arguments);
        checkShape('containsShape(targetShape)', 'targetShape', targetShape);

        if (isinstance(targetShape, Group)):
            return all([self.containsShape(shape) for shape in targetShape.children])

        # This shapes fully contains the target shape if their
        # edges do not intersect, but (any point of / all points of)
        # the targetShape are inside this shape
        x = targetShape.centerX
        y = targetShape.centerY
        return (not self.edgesIntersect(targetShape) and self.contains(x, y))

    def getBounds(self):
        return { 'left': self.left, 'top': self.top, 'width': self.width, 'height': self.height }

    def boundsIntersect(self, targetShape, margin = None):
        # Symmetric.  Fast pre-test for hitsShape.  If this is False, hitsShape
        # must be False.  If this is True, hitsShape *may* be True.
        if (margin is None): margin = 0
        b1 = self.getBounds()
        b2 = targetShape.getBounds()
        return ((b1['left'] + margin <= b2['left'] + b2['width']) and
                (b2['left'] + margin <= b1['left'] + b1['width']) and
                (b1['top']  + margin <= b2['top'] + b2['height']) and
                (b2['top']  + margin <= b1['top'] + b1['height']))

    def hitsShape(self, *arguments):
        checkArgCount(self.__class__.__name__, 'hitsShape', ['targetShape'], arguments);
        (targetShape,) = arguments
        checkShape('hitsShape(targetShape)', 'targetShape', targetShape);
        # Symmetric.  Two shapes hit each other if any of their
        # vertices hit the other or their edges intersect.
        myShapes = utils.getChildShapes(self);
        targetShapes = utils.getChildShapes(targetShape);

        for i in range(len(myShapes)):
            for j in range(len(targetShapes)):
                if (myShapes[i].edgesIntersect(targetShapes[j])):
                    return True

        for i in range(len(myShapes)):
            for j in range(len(targetShapes)):
                shape1 = myShapes[i]
                shape2 = targetShapes[j]
                if any((shape2.hits(pt[0], pt[1]) for pt in shape1.getApproxPoints())):
                    return True
                if any((shape1.hits(pt[0], pt[1]) for pt in shape2.getApproxPoints())):
                    return True
                if myShapes[i].edgesIntersect(targetShapes[j]):
                    return True

        return False

    def toFront(self):
        if self.group is not None:
            self.group._toFront(self)

    def toBack(self):
        if  self.group is not None:
            self.group._toBack(self)

    def setFillOrStrokeStyle(self, ctx, fillOrBorder):
        style = self.getFillOrStrokeStyle(fillOrBorder)
        if isinstance(style, cairo.Gradient):
            ctx.set_source(style)
        else:
            ctx.set_source_rgba(*style)

    def getFillOrStrokeStyle(self, fillOrBorder):
        if fillOrBorder is None: return (0,0,0,1)
        if isinstance(fillOrBorder, Gradient):
            gradient = fillOrBorder
            g = self.createBaseGradient(gradient)
            n = len(gradient.colors)
            for i in range(n):
                color = gradient.colors[i]
                g.add_color_stop_rgba(i/(n-1), *self.getFillOrStrokeStyle(color))
            return g
        if isinstance(fillOrBorder, str):
            fillOrBorder = CSS3_COLORS_TO_RGB[fillOrBorder.lower()]
        # Flips RGBA to BGRA because Cairo is going to flip it back
        rgba = (fillOrBorder.blue/255, fillOrBorder.green/255, fillOrBorder.red/255,  self.opacity / 100)
        return rgba

    def setDashes(self, ctx):
        if isinstance(self.dashes, bool):
            ctx.set_dash([5,5] if self.dashes else [])
        else:
            ctx.set_dash(self.dashes)

    def drawDbPoint(self, ctx, x, y, color):
        ctx.save()
        color_list = list(self.getFillOrStrokeStyle(color))
        color_list[3] = 1 # ignore our own opacity when drawing db points
        ctx.set_source_rgba(*color_list)
        r = 3
        ctx.new_path()
        ctx.arc(x, y, r, 0, 2 * math.pi)
        ctx.close_path()
        ctx.fill()
        ctx.restore()

    def drawDbCenter(self, ctx):
        self.drawDbPoint(ctx, self.centerX, self.centerY, 'red')

    def drawDbCentroid(self, ctx):
        if isinstance(self, Polygon):
            centroid = utils.getPolygonCentroid(self.pointList)
            self.drawDbPoint(ctx, centroid[0], centroid[1], 'magenta')
        else:
            self.drawDbCenter(ctx)

    def drawDbBox(self, ctx):
        ctx.save()
        ctx.new_path()
        ctx.rectangle(self.left, self.top, self.width, self.height)
        ctx.close_path()
        ctx.set_line_width(2)
        color_list = list(self.getFillOrStrokeStyle('red'))
        color_list[3] = 1 # ignore our own opacity when drawing db points
        ctx.set_source_rgba(*color_list)
        ctx.set_dash([2, 2])
        ctx.stroke()
        ctx.restore()

    def drawDbPoints(self, ctx):
        pts = self.getApproxPoints()
        ctx.save()
        r = 4
        self.setFillOrStrokeStyle(ctx, 'magenta')
        # dots at corners
        for pt in pts:
            x, y = pt
            ctx.new_path()
            ctx.arc(x, y, r, 0, 2 * math.pi)
            ctx.close_path()
            ctx.fill()
        # now connect the dots
        ctx.new_path
        utils.makePolygonPath(pts, ctx)
        ctx.close_path()
        ctx.set_line_width(3)
        self.setFillOrStrokeStyle(ctx, 'magenta')
        ctx.set_dash([7, 7])
        ctx.stroke()
        ctx.restore()

    def draw(self, ctx):
        ctx.save()
        if (self.isGroup):
            for s in self._shapes: s.draw(ctx)
        else:
            bw = self.borderWidth if self.border else 0
            if isinstance(self, Label):
                [targetX, targetY] = self.getApproxPoints()[6] # target start,top of text
                # rotate around targetX, targetY
                if self.rotateAngle != 0:
                    ctx.translate(targetX, targetY)
                    ctx.rotate(utils.toRadians(self.rotateAngle))
                    ctx.translate(-targetX, -targetY)

                ctx.select_font_face(*getFont(self.font, self.bold, self.italic))
                ctx.set_font_size(self.size)
                text = str(self.value)

                ctx.new_path()
                ctx.move_to(targetX - self.attrs['xAdjust'], targetY)

                ctx.text_path(text)

                self.setFillOrStrokeStyle(ctx, self.fill)
                ctx.fill_preserve()
                if bw:
                    self.setFillOrStrokeStyle(ctx, self.border)
                    ctx.set_line_width(bw)
                    ctx.stroke()
            elif isinstance(self, Line):
                if self.fill:
                    ctx.new_path()
                    self.setFillOrStrokeStyle(ctx, self.fill)
                    self.setDashes(ctx)
                    ctx.set_line_width(self.lineWidth)
                    ctx.move_to(self.x1, self.y1)
                    ctx.line_to(self.x2, self.y2)
                    ctx.stroke()

                    self.drawArrows(ctx)
            else:
                self.makePath(ctx)
                if (self.closed): ctx.close_path()
                if (self.fill and len(self.pointList) > 2):
                    self.setFillOrStrokeStyle(ctx, self.fill)
                    ctx.fill_preserve()
                if bw:
                    # (*note) if there is a border, draw with 2x borderWidth,
                    # but clipped to shape so only 1x inner border is drawn
                    bw *= 2
                    ctx.clip_preserve()
                    self.setFillOrStrokeStyle(ctx, self.border)
                    # @TODO
                    self.setDashes(ctx)
                    if isinstance(self, Arc):
                        ctx.set_line_join(cairo.LINE_JOIN_ROUND)
                    ctx.set_line_width(bw)
                    ctx.stroke()
            if isinstance(self, CMUImage):
                self.drawImage(ctx)
            ctx.restore()

            db = self.db
            if db != '' and type(db) == str:
                if db == 'all' or 'points' in db: self.drawDbPoints(ctx)
                if db == 'all' or 'box' in db: self.drawDbBox(ctx)
                if db == 'all' or 'center' in db: self.drawDbCenter(ctx)
                if db == 'all' or 'centroid' in db: self.drawDbCentroid(ctx)

def countShapesInGroup(shape):
    # First make it a sl shape so hasattr doesn't call getattr and crash
    if hasattr(shape, '_shape'):
        shape = shape._shape
    if not hasattr(shape, '_shapes') or not shape._shapes:
        return 1
    return sum(map(countShapesInGroup, shape))

class Group(Shape):
    def __init__(self, attrs):
        super().__init__(attrs)
        self.isGroup = True
        self._shapes = []

    def toString(self): return 'Group()'

    def __iter__(self):
        return iter(self.children)

    def get_children(self):
        return list(map(lambda s: s.studentShape, self._shapes))
    children = property(get_children)

    def insert(self, shape):
        if shape.group:
            shape.group.remove(shape)
        # By default, put this shape at the top of the group
        newIndex = len(self._shapes)
        # But if it was in this group before, put it back in front of all the
        # shapes that it was in front of before
        if (shape.oldGroup == self):
            newIndex = 0
            for s2 in shape.shapesToBeInFrontOf:
                s2Index = self._shapes.index(s2) if s2 in self._shapes else -1
                if (s2Index >= 0):
                    newIndex = max(newIndex, s2Index + 1)
        self._shapes.insert(newIndex, shape)
        shape.group = self
        shape.zindex = -1
        shape.oldGroup = None
        shape.shapesToBeInFrontOf = []

    def add(self, *shapes):
        for i in range(len(shapes)):
            checkShape('Group.add(shape)', 'shape', shapes[i])
            activeDrawing.addCounter += 1
            if activeDrawing.addCounter % 100 == 0:
                if countShapesInGroup(activeDrawing.tlg) > activeDrawing.appProperties['maxShapeCount']:
                    pyThrow('Too many shapes: Your code created more than ' + str(activeDrawing.appProperties['maxShapeCount']) +
                            ' shapes. If you would like to increase this limit even though it may cause' +
                            ' your code to run slowly, call app.setMaxShapeCount(n).')
            self.insert(shapes[i])

    def _toFront(self, shape):
        self.remove(shape)
        shape.oldGroup = None
        self.add(shape)

    def _toBack(self, shape):
        self.remove(shape)
        shape.shapesToBeInFrontOf = []
        self.add(shape)

    def remove(self, shape):
        checkShape('Group.remove(shape)', 'shape', shape)
        currentIndex = self._shapes.index(shape) if shape in self._shapes else -1
        shape.shapesToBeInFrontOf = shape.shapesToBeInFrontOf + self._shapes[:currentIndex]

        for i in range(currentIndex + 1, len(self._shapes)):
            self._shapes[i].shapesToBeInFrontOf.append(shape)

        if shape in self._shapes: self._shapes.remove(shape)
        shape.oldGroup = self
        shape.group = None
        shape.zindex = -1

        def f(shape):
            if shape.isGroup:
                for s in shape._shapes: f(s)
            else:
                shape.zindex = -1

        f(shape)

    def clear(self):
        shapes = self._shapes
        self._shapes = []
        for shape in shapes: self.remove(shape)

    def hits(self, x, y):
        return self.hitTest(x, y) != None

    def hitTest(self, x, y):
        for i in range(len(self._shapes)-1, -1, -1):
            shape = self._shapes[i]
            if (shape.hits(x, y)):
                return shape.studentShape
        return None

    def contains(self, x, y):
        return any(shape.contains(x, y) for shape in self._shapes)

    def containsShape(self, target):
        return any(shape.containsShape(shape) for shape in self._shapes)

    def addx(self, dx):
        for shape in self._shapes: shape.left += dx
    def get_left(self):
        if len(self._shapes) == 0: return 0
        return min(map(lambda s: s.left, self._shapes))
    def set_left(self, v): self.addx(v - self.left)
    left = property(get_left, set_left)
    def get_right(self):
        if len(self._shapes) == 0: return 0
        return max(map(lambda s: s.right, self._shapes))
    def set_right(self, v): self.addx(v - self.right)
    right = property(get_right, set_right)
    def get_centerX(self): return (self.left + self.right) / 2
    def set_centerX(self, v): self.addx(v - self.centerX)
    centerX = property(get_centerX, set_centerX)

    def addy(self, dy):
        for shape in self._shapes: shape.top += dy
    def get_top(self):
        if (len(self._shapes) == 0):
            return 0
        return min(map(lambda s: s.top, self._shapes))
    def set_top(self, v): self.addy(v - self.top)
    top = property(get_top, set_top)
    def get_bottom(self):
        if len(self._shapes) == 0: return 0
        return max(map(lambda s: s.bottom, self._shapes))
    def set_bottom(self, v): self.addy(v - self.bottom)
    bottom = property(get_bottom, set_bottom)
    def get_centerY(self): return (self.top + self.bottom) / 2
    def set_centerY(self, v): self.addy(v - self.centerY)
    centerY = property(get_centerY, set_centerY)

    def scalexy(self, varName, k, scaleAnchor = None):
        if (k == 1): return
        checkPositive(self, 'scale{varName}'.format(varName=varName), k)
        if (scaleAnchor is None):
            scaleAnchor = self.centroid
        for s in self._shapes: s.scalexy(varName, k, scaleAnchor)

    def get_width(self): return self.right - self.left
    def set_width(self, v):
        checkPositive(self, 'width', v)
        self.scalexy('x', (v / self.width) if self.width != 0 else math.inf)
    width = property(get_width, set_width)
    def get_height(self): return self.bottom - self.top
    def set_height(self, v):
        checkPositive(self, 'height', v)
        self.scalexy('y', (v / self.height) if self.height != 0 else math.inf)
    height = property(get_height, set_height)

    def rotate(self, degrees = None, cx = None, cy = None):
        if (len(self._shapes) == 0):
            self.set({'rotateAngle': self.rotateAngle + degrees})
            return

        super().rotate(degrees, cx, cy)

    def doRotate(self, degrees, cx, cy):
        for s in self._shapes: s.rotate(degrees, cx, cy)

    def get_area(self):
        result = 0
        for s in self._shapes: result += s.area
        return result
    area = property(get_area)

    def get_centroid(self):
        x, y, A = 0, 0, 0
        for s in self._shapes:
            c = s.centroid
            a = s.area
            cx, cy = c[0], c[1]
            x += a * cx
            y += a * cy
            A += a
        return [math.inf, math.inf] if A == 0 else [x / A, y / A]
    centroid = property(get_centroid)

    # pass-through attrs (PTA's)

    def getPTA(self, attr):
        val = None
        for shape in self._shapes:
            if val is None:
                val = getattr(shape, attr)
            else:
                if ((attr == 'fill' and not colorTest(getattr(shape, attr), val, 0.005))
                    or (attr == 'opacity' and not opacityTest(getattr(shape, attr), val))):
                    pyThrow("Group.{attr} has no value because its children don't all have the same value for {attr}".format(attr=attr))
        return val

    def setPTA(self, attr, v):
        for shape in self._shapes:
            setattr(shape, attr, v)
        return v

    def get_fill(self): return self.getPTA('fill')
    def set_fill(self, v): return self.setPTA('fill', v)
    fill = property(get_fill, set_fill)
    def get_opacity(self): return self.getPTA('opacity')
    def set_opacity(self, v): return self.setPTA('opacity', v)
    opacity = property(get_opacity, set_opacity)

    def noPTA(self, attr):
        pyThrow('Group.{attr} cannot be read or modified'.format(attr=attr))

    def get_border(self): return self.noPTA('border')
    def set_border(self, v): return self.noPTA('border', v)
    border = property(get_border, set_border)
    def get_borderWidth(self): return self.noPTA('borderWidth')
    def set_borderWidth(self, v): return self.noPTA('borderWidth', v)
    borderWidth = property(get_borderWidth, set_borderWidth)
    def get_dashes(self): return self.noPTA('dashes')
    def set_dashes(self, v): return self.noPTA('dashes', v)
    dashes = property(get_dashes, set_dashes)
    def get_arrowEnd(self): return self.noPTA('arrowEnd')
    def set_arrowEnd(self, v): return self.noPTA('arrowEnd', v)
    arrowEnd = property(get_arrowEnd, set_arrowEnd)
    def get_arrowStart(self): return self.noPTA('arrowStart')
    def set_arrowStart(self, v): return self.noPTA('arrowStart', v)
    arrowStart = property(get_arrowStart, set_arrowStart)
    def get_url(self): return self.noPTA('url')
    def set_url(self, v): return self.noPTA('url', v)
    url = property(get_url, set_url)
    def get_radius(self): return self.noPTA('radius')
    def set_radius(self, v): return self.noPTA('radius', v)
    radius = property(get_radius, set_radius)
    def get_points(self): return self.noPTA('points')
    def set_points(self, v): return self.noPTA('points', v)
    points = property(get_points, set_points)
    def get_roundness(self): return self.noPTA('roundness')
    def set_roundness(self, v): return self.noPTA('roundness', v)
    roundness = property(get_roundness, set_roundness)
    def get_x1(self): return self.noPTA('x1')
    def set_x1(self, v): return self.noPTA('x1', v)
    x1 = property(get_x1, set_x1)
    def get_y1(self): return self.noPTA('y1')
    def set_y1(self, v): return self.noPTA('y1', v)
    y1 = property(get_y1, set_y1)
    def get_x2(self): return self.noPTA('x2')
    def set_x2(self, v): return self.noPTA('x2', v)
    x2 = property(get_x2, set_x2)
    def get_y2(self): return self.noPTA('y2')
    def set_y2(self, v): return self.noPTA('y2', v)
    y2 = property(get_y2, set_y2)
    def get_lineWidth(self): return self.noPTA('lineWidth')
    def set_lineWidth(self, v): return self.noPTA('lineWidth', v)
    lineWidth = property(get_lineWidth, set_lineWidth)
    def get_closed(self): return self.noPTA('closed')
    def set_closed(self, v): return self.noPTA('closed', v)
    closed = property(get_closed, set_closed)
    def get_startAngle(self): return self.noPTA('startAngle')
    def set_startAngle(self, v): return self.noPTA('startAngle', v)
    startAngle = property(get_startAngle, set_startAngle)
    def get_sweepAngle(self): return self.noPTA('sweepAngle')
    def set_sweepAngle(self, v): return self.noPTA('sweepAngle', v)
    sweepAngle = property(get_sweepAngle, set_sweepAngle)
    def get_value(self): return self.noPTA('value')
    def set_value(self, v): return self.noPTA('value', v)
    value = property(get_value, set_value)
    def get_font(self): return self.noPTA('font')
    def set_font(self, v): return self.noPTA('font', v)
    font = property(get_font, set_font)
    def get_size(self): return self.noPTA('size')
    def set_size(self, v): return self.noPTA('size', v)
    size = property(get_size, set_size)
    def get_bold(self): return self.noPTA('bold')
    def set_bold(self, v): return self.noPTA('bold', v)
    bold = property(get_bold, set_bold)
    def get_italic(self): return self.noPTA('italic')
    def set_italic(self, v): return self.noPTA('italic', v)
    italic = property(get_italic, set_italic)

fontCtx = cairo.Context(cairo.ImageSurface(cairo.FORMAT_ARGB32, 0, 0))

def getFont(baseFontName, isBold=False, isItalic=False):
    ok = True
    if 'mono' in baseFontName or 'courier' in baseFontName:
        fontName = 'Courier New'
    elif 'arial' in baseFontName or 'sans' in baseFontName:
        fontName = 'Arial'
    else:
        fontName = 'Arial'

    bold = cairo.FONT_WEIGHT_BOLD if isBold else cairo.FONT_WEIGHT_NORMAL
    italic = cairo.FONT_SLANT_ITALIC if isItalic else cairo.FONT_SLANT_NORMAL

    return (fontName, italic, bold)

class Label(Shape):
    def __init__(self, attrs):
        super().__init__(attrs)
        if attrs is not None:
            self.setDims()

    def getApproxPoints(self): return self.attrs['approxPoints']

    def doRotate(self, degrees, cx, cy):
        newCenter = utils.rotatePoint([self.centerX, self.centerY], utils.toRadians(degrees), cx, cy)
        self.set({
            'centerX': newCenter[0],
            'centerY': newCenter[1]
        })
        self.setDims()

    def setDims(self):
        fontCtx.save()
        fontCtx.select_font_face(*getFont(self.font, self.bold, self.italic))
        fontCtx.set_font_size(self.size)

        cx = self.attrs['centerX']
        cy = self.attrs['centerY']
        stringValue = utils.convertLabelValue(self.value)
        xBearing, yBearing, width, height, xAdvance, yAdvance = fontCtx.text_extents(stringValue)
        height = -yBearing
        unrotatedWidth = width
        hasOuterSpaces = len(stringValue) > 0 and (stringValue[0] == ' ' or stringValue[-1] == ' ')
        if hasOuterSpaces:
            unrotatedWidth = max(unrotatedWidth, xAdvance)
        #unrotatedHeight = -height
        unrotatedHeight = height
        x0 = cx - unrotatedWidth / 2
        y0 = cy - unrotatedHeight / 2
        x1 = cx + unrotatedWidth / 2
        y1 = cy + unrotatedHeight / 2
        pts = [[x0, y0], [(x0 + x1) / 2, y0], [x1, y0],
               [x1, (y0 + y1) / 2],
               [x1, y1], [(x0 + x1) / 2, y1], [x0, y1],
               [x0, (y0 + y1) / 2]]
        a = self.rotateAngle
        if a: pts = utils.rotatePoints(pts, utils.toRadians(a), self.centerX, self.centerY)
        self.set({
            'approxPoints': pts,
            'xAdjust': 0 if hasOuterSpaces else xBearing
        })
        box = utils.getBoxDims(pts)
        self.set({
            'width': box['width'],
            'height': box['height']
        })
        fontCtx.restore()

    def get_area(self): return self.width * self.height
    area = property(get_area)

    def createBaseGradient(self, gradient):
        # The approxPoints of a Label are positioned correctly (self.rotateAngle has
        # already been applied to them). However, when we draw the text, we
        # rotate the canvas around the start,bottom point of the text. So, we have to make a
        # gradient that is positioned such that it will be in the correct place after
        # being rotated around start,bottom by self.rotateAngle.
        start = canonicalizeGradientStart(gradient.start)
        [targetX, targetY] = self.getApproxPoints()[6] # target start,top of text
        if (start == 'center'):
            cx = self.centerX;
            cy = self.centerY;
            r = utils.distance(cx, cy, self.right, self.top);
            [[cx, cy]] = utils.rotatePoints([[cx, cy]], utils.toRadians(-self.rotateAngle), targetX, targetY);
            return cairo.RadialGradient(cx, cy, 0, cx, cy, r);


        startToPointIndex = {
            'left-top': 0,
            'top': 1,
            'right-top': 2,
            'right': 3,
            'right-bottom': 4,
            'bottom': 5,
            'left-bottom': 6,
            'left': 7,
        }

        if (startToPointIndex.get(start) is None):
            pyThrow('Illegal gradient start {start}'.format(start=start))

        [x0, y0] = self.getApproxPoints()[startToPointIndex[start]]
        endIndex = (startToPointIndex[start] + 4) % 8
        [x1, y1] = self.getApproxPoints()[endIndex]

        if (self.rotateAngle != 0):
            [[x0, y0], [x1, y1]] = utils.rotatePoints(
                [[x0, y0], [x1, y1]],
                utils.toRadians(-self.rotateAngle),
                targetX,
                targetY
            )

        return cairo.LinearGradient(x0, y0, x1, y1)

    def get_width(self): return self.get('width')
    def set_width(self, v): pyThrow("Cannot set Label's width")
    width = property(get_width, set_width)
    def get_height(self): return self.get('height')
    def set_height(self, v): pyThrow("Cannot set Label's height")
    height = property(get_height, set_height)

    def get_centerX(self): return self.get('centerX')
    def set_centerX(self, v):
        self.set({'centerX': v})
        self.setDims()
        return v
    centerX = property(get_centerX, set_centerX)

    def get_centerY(self): return self.get('centerY')
    def set_centerY(self, v):
        self.set({'centerY': v})
        self.setDims()
        return v
    centerY = property(get_centerY, set_centerY)

    def get_value(self): return self.get('value')
    def set_value(self, v):
        self.set({'value': v})
        self.setDims()
        return v
    value = property(get_value, set_value)
    def get_font(self): return self.get('font')
    def set_font(self, v):
        self.set({'font': v})
        self.setDims()
        return v
    font = property(get_font, set_font)
    def get_size(self): return self.get('size')
    def set_size(self, v):
        self.set({'size': v})
        self.setDims()
        return v
    size = property(get_size, set_size)
    def get_bold(self): return self.get('bold')
    def set_bold(self, v):
        self.set({'bold': v})
        self.setDims()
        return v
    bold = property(get_bold, set_bold)
    def get_italic(self): return self.get('italic')
    def set_italic(self, v):
        self.set({'italic': v})
        self.setDims()
        return v
    italic = property(get_italic, set_italic)

    def toString(self):
        return 'Label({value},{centerX},{centerY})'.format(
            value=self.value, centerX=self.centerX, centerY = self.centerY
        )

class Polygon(Shape):
    def __init__(self, attrs=None):
        if (not attrs is None and 'initialPoints' in attrs):
            if (len(attrs['initialPoints']) % 2 != 0):
                pyThrow('Must have an even number of x,y values in initialPoints list')
            for i in range(0, len(attrs['initialPoints']), 2):
                x, y = attrs['initialPoints'][i], attrs['initialPoints'][i+1]
                checkNumber('Polygon', 'initialPoints (x value)', x)
                checkNumber('Polygon', 'initialPoints (y value)', y)

        super().__init__(attrs)
        self._cachedCentroid = self._cachedArea = None

        if (not attrs is None and 'initialPoints' in attrs):
            pts = attrs['initialPoints']
            pointList = []
            for i in range(0, len(pts), 2):
                x, y = pts[i], pts[i+1]
                pointList.append([x,y])
            self.pointList = pointList

    def get_pointList(self): return self.get('pointList')
    def set_pointList(self, pl):
        self.set({'pointList': pl})
        self.setDims()
    pointList = property(get_pointList, set_pointList)

    def get_area(self):
        if (self._cachedArea is None):
            self._cachedArea = abs(utils.getPolygonArea(self.pointList))
        return self._cachedArea
    area = property(get_area)

    def get_centroid(self):
        if self._cachedCentroid is None:
            self._cachedCentroid = utils.getPolygonCentroid(self.pointList)
        return self._cachedCentroid
    centroid = property(get_centroid)

    def addPoint(self, x, y):
        checkNumber('addPoint', 'x', x)
        checkNumber('addPoint', 'y', y)
        self.pointList.append([x, y])
        self.pointList = self.pointList # alert to change

    def makePath(self, ctx):
        return utils.makePolygonPath(self.pointList, ctx)

    def setDims(self):
        self._cachedCentroid = self._cachedArea = None
        if len(self.pointList) == 0:
            self.set({
                'centerX': 0,
                'centerY': 0,
                'width': 0,
                'height': 0,
            })
            return
        boxDims = utils.getBoxDims(self.pointList)
        self.set({
            'centerX': boxDims['left'] + boxDims['width'] / 2,
            'centerY': boxDims['top'] + boxDims['height'] / 2,
            'width': boxDims['width'],
            'height': boxDims['height']
        })

    def get_centerX(self): return self.get('centerX')
    def set_centerX(self, v):
        self.addx(v - self.centerX)
        # centerX will get set by setDims(), but we overwrite the value
        # with what the user gave so that there are no rounding errors.
        self.set({'centerX': v})
    centerX = property(get_centerX, set_centerX)

    def get_centerY(self): return self.get('centerY')
    def set_centerY(self, v):
        self.addy(v - self.centerY)
        # centerY will get set by setDims(), but we overwrite the value
        # with what the user gave so that there are no rounding errors.
        self.set({'centerY': v})
    centerY = property(get_centerY, set_centerY)

    def get_left(self): return min(map(lambda point: point[0], self.pointList))
    def set_left(self, v): self.addx(v - self.left); return v
    left = property(get_left, set_left)

    def get_top(self): return min(map(lambda point: point[1], self.pointList))
    def set_top(self, v): self.addy(v - self.top); return v
    top = property(get_top, set_top)

    def get_right(self): return max(map(lambda point: point[0], self.pointList))
    def set_right(self, v): self.addx(v - self.right); return v
    right = property(get_right, set_right)

    def get_bottom(self): return max(map(lambda point: point[1], self.pointList))
    def set_bottom(self, v): self.addy(v - self.bottom); return v
    bottom = property(get_bottom, set_bottom)

    def addxy(self, varName, d):
        if d == 0: return
        varIndex = 0 if varName == 'x' else 1
        checkNumber(self, 'add{varName}'.format(varName=varName), d)
        pointList = self.pointList
        for i in range(len(pointList)):
            pointList[i][varIndex] += d
        self.pointList = pointList # alert to change

    def scalexy(self, varName, k, scaleAnchor = None):
        if k == 1: return
        varIndex = 0 if varName == 'x' else 1
        checkPositive(self, 'scale{varName}'.format(varName=varName), k)
        pointList = self.pointList
        cxy = (scaleAnchor or self.getScaleAnchor())[varIndex]
        for i in range(len(pointList)):
            dxy = pointList[i][varIndex] - cxy
            pointList[i][varIndex] = cxy + k * dxy
        self.pointList = pointList # alert to change

    def getScaleAnchor(self): return [self.centerX, self.centerY]

    def doRotate(self, degrees, cx, cy):
        self.pointList = utils.rotatePoints(self.pointList, utils.toRadians(degrees), cx, cy)

    def getApproxPoints(self):
        return self.pointList

    def toString(self):
        args = utils.flatten(self.pointList)
        return 'Polygon{args}'.format(args=utils.roundedTupleString(args, 2))

    def createBaseGradient(self, fillOrBorder):
        gradient = fillOrBorder
        start = gradient.start
        rotateAnchor = self.getRotateAnchor()

        unrotatedPoints = self.pointList
        if self.rotateAngle != 0:
            unrotatedPoints = utils.rotatePoints(
                self.pointList, utils.toRadians(-self.rotateAngle), rotateAnchor[0], rotateAnchor[1]
            )
        dims = utils.getBoxDims(unrotatedPoints)

        if start == 'center':
            if isinstance(self, Oval):
                r = max(dims['width'], dims['height']) / 2
            else:
                r = utils.distance(
                    dims['left'] + dims['width'] / 2, dims['top'] + dims['height'] / 2,
                    dims['left'], dims['top']
                )

            if isinstance(self, Star):
                r *= 0.8

            return cairo.RadialGradient(
                rotateAnchor[0], rotateAnchor[1], 0,
                rotateAnchor[0], rotateAnchor[1], r,
            )

        left, top = dims['left'], dims['top']
        right = left + dims['width']
        bottom = top + dims['height']
        centerX = left + dims['width'] / 2
        centerY = top + dims['height'] / 2
        if (start == 'left-top'):
          x0 = left; x1 = right; y0 = top; y1 = bottom
        elif (start == 'left'):
          x0 = left; x1 = right; y0 = y1 = centerY
        elif (start == 'left-bottom'):
          x0 = left; x1 = right; y0 = bottom; y1 = top
        elif (start == 'top'):
          x0 = x1 = centerX; y0 = top; y1 = bottom
        elif (start == 'bottom'):
          x0 = x1 = centerX; y0 = bottom; y1 = top
        elif (start == 'right-top'):
          x0 = right; x1 = left; y0 = top; y1 = bottom
        elif (start == 'right'):
          x0 = right; x1 = left; y0 = y1 = centerY
        elif (start == 'right-bottom'):
          x0 = right; x1 = left; y0 = bottom; y1 = top
        else:
          pyThrow('Illegal gradient start ({start})'.format(start=start))

        if self.rotateAngle != 0:
            [[x0, y0], [x1, y1]] = utils.rotatePoints([[x0, y0], [x1, y1]], utils.toRadians(self.rotateAngle),
                rotateAnchor[0], rotateAnchor[1]
            )

        return cairo.LinearGradient(x0, y0, x1, y1)

class Rect(Polygon):
    def __init__(self, attrs=None):
        if not attrs is None:
            right = attrs['left'] + attrs['width']
            bottom = attrs['top'] + attrs['height']
            attrs['defaultAlign'] = 'left-top'
            attrs['initialPoints'] = [
                attrs['left'], attrs['top'],
                right, attrs['top'],
                right, bottom,
                attrs['left'], bottom,
            ]
        super().__init__(attrs)

    def getScaleAnchor(self): return [self.left, self.top]

    def toString(self):
        args = [self.left, self.top, self.width, self.height]
        return 'Rect{args}'.format(args=utils.roundedTupleString(args, 2))

class Line(Polygon):
    def __init__(self, attrs):
        checkNumber('Line', 'x1', attrs['x1'])
        checkNumber('Line', 'x2', attrs['x2'])
        checkNumber('Line', 'y1', attrs['y1'])
        checkNumber('Line', 'y2', attrs['y2'])
        attrs['initialPoints'] = utils.flatten(utils.getLinePoints(attrs['x1'], attrs['y1'], attrs['x2'], attrs['y2'], 2))
        del attrs['x1']
        del attrs['y1']
        del attrs['x2']
        del attrs['y2']
        super().__init__(attrs)

    def getXY(self, i0, i1, j):
        p = self.pointList
        return (p[i0][j] + p[i1][j]) / 2

    def setXY(self, i0, i1, j, v, name):
        checkNumber(self, name, v)
        p = self.pointList
        oldv = (p[i0][j] + p[i1][j]) / 2
        dv = v - oldv
        p[i0][j] += dv
        p[i1][j] += dv
        self.pointList = self.pointList; # alert to change
        return v

    def get_x1(self): return self.getXY(0, 3, 0) # x1,y1 at points 0 and 3, 0=x
    def set_x1(self, v): return self.setXY(0, 3, 0, v, 'x1') # x1,y1 at points 0 and 3, 0=x
    x1 = property(get_x1, set_x1)
    def get_y1(self): return self.getXY(0, 3, 1)  # x1,y1 at points 0 and 3, 1=y
    def set_y1(self, v): return self.setXY(0, 3, 1, v, 'y1') # x1,y1 at points 0 and 3, 1=y
    y1 = property(get_y1, set_y1)
    def get_x2(self): return self.getXY(1, 2, 0) # x2,y2 at points 1 and 2, 0=x
    def set_x2(self, v): return self.setXY(1, 2, 0, v, 'x2') # x2,y2 at points 1 and 2, 0=x
    x2 = property(get_x2, set_x2)
    def get_y2(self): return self.getXY(1, 2, 1) # x2,y2 at points 1 and 2, 1=y
    def set_y2(self, v): return self.setXY(1, 2, 1, v, 'y2') # x2,y2 at points 1 and 2, 1=y
    y2 = property(get_y2, set_y2)

    def get_arrowStart(self): return self.get('arrowStart')
    def set_arrowStart(self, v): return self.set({'arrowStart': v})
    arrowStart = property(get_arrowStart, set_arrowStart)
    def get_arrowEnd(self): return self.get('arrowEnd')
    def set_arrowEnd(self, v): return self.set({'arrowEnd': v})
    arrowEnd = property(get_arrowEnd, set_arrowEnd)
    def get_lineWidth(self):
        pts = self.pointList
        return utils.distance(pts[0][0], pts[0][1], pts[3][0], pts[3][1])
    def set_lineWidth(self, v):
        self.pointList = utils.getLinePoints(self.x1, self.y1, self.x2, self.y2, v)
        return self.set({'lineWidth': v})
    lineWidth = property(get_lineWidth, set_lineWidth)
    def get_borderWidth(self): return 0
    def set_borderWidth(self, v): pyThrow("Cannot set Line's borderWidth")
    borderWidth = property(get_borderWidth, set_borderWidth)
    def get_border(self): return None
    def set_border(self, v): pyThrow("Cannot set Line's border")
    border = property(get_border, set_border)

    def get_area(self): return self.lineWidth * utils.distance(self.x1, self.y1, self.x2, self.y2)
    area = property(get_area)

    def get(self, attr):
        if (attr == 'x1'): return self.x1
        elif (attr == 'y1'): return self.y1
        elif (attr == 'x2'): return self.x2
        elif (attr == 'y2'): return self.y2
        else: return super().get(attr)

    def drawArrows(self, ctx):
        if (not self.arrowEnd and not self.arrowStart): return

        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        dist = math.sqrt(dy * dy + dx * dx)
        if dist < 0.01: return
        dx /= dist
        dy /= dist

        normalDx = -dy
        normalDy = dx

        arrowLength = min(50, 10*math.sqrt(self.lineWidth))
        arrowWidth = arrowLength / 3

        def drawArrow(x, y, dir):
            ctx.new_path()
            self.setFillOrStrokeStyle(ctx, self.fill)
            ctx.set_dash([])
            ctx.move_to(x, y)
            ctx.line_to(x + dir * arrowLength * dx - arrowWidth * normalDx,
                y + dir * arrowLength * dy - arrowWidth * normalDy)
            ctx.line_to(x + dir * arrowLength * dx + arrowWidth * normalDx,
                y + dir * arrowLength * dy + arrowWidth * normalDy)
            ctx.close_path()
            ctx.fill_preserve()
            ctx.stroke()

        if self.arrowEnd:
            drawArrow(self.x2, self.y2, -1)
        if self.arrowStart:
            drawArrow(self.x1, self.y1, 1)

    def toString():
        args = [self.x1, self.y1, self.x2, self.y2]
        return 'Line{args}'.format(args=utils.roundedTupleString(args, 2))

class PolygonInCircle(Polygon):
    def get_radius(self): return self.get('radius')
    def set_radius(self, v):
        self.set({'radius': v})
        self.updatePointList()
        return v
    radius = property(get_radius, set_radius)

    def get_points(self): return self.get('points')
    def set_points(self, v):
        self.set({'points': v})
        self.updatePointList()
        return v
    points = property(get_points, set_points)

    def get_centerX(self): return utils.round2(self.centroid[0])
    def set_centerX(self, v): self.addx(v - self.centerX)
    centerX = property(get_centerX, set_centerX)
    def get_centerY(self): return utils.round2(self.centroid[1])
    def set_centerY(self, v): self.addy(v - self.centerY)
    centerY = property(get_centerY, set_centerY)

class RegularPolygon(PolygonInCircle):
    def __init__(self, attrs):
        attrs['initialPoints'] = utils.flatten(utils.getRegularPolygonPoints(attrs['centerX'], attrs['centerY'], attrs['radius'], attrs['points'], 0))
        super().__init__(attrs)

    def updatePointList(self):
        self.pointList = utils.getRegularPolygonPoints(self.centerX, self.centerY, self.radius, self.points, self.rotateAngle)

    def toString(self):
        args = [self.centerX, self.centerY, self.radius, self.points]
        return 'RegularPolygon{args}'.format(args=utils.roundedTupleString(args, 2))

class Star(PolygonInCircle):
    def __init__(self, attrs):
        attrs['initialPoints'] = utils.flatten(utils.getStarPoints(attrs['centerX'], attrs['centerY'], attrs['radius'], attrs['points'], None, 0))
        super().__init__(attrs)

    def get_roundness(self):
        result = self.get('roundness')
        if result == 'default':
            return utils.getDefaultRoundness(self.points)
        return result
    def set_roundness(self, v):
        self.set({'roundness': v})
        self.updatePointList()
        return v
    roundness = property(get_roundness, set_roundness)

    def updatePointList(self):
        self.pointList = utils.getStarPoints(self.centerX, self.centerY, self.radius, self.points, self.roundness, self.rotateAngle)

    def toString(self):
        args = [self.centerX, self.centerY, self.radius, self.points]
        return 'Star{args}'.format(args=utils.roundedTupleString(args, 2))

class PolygonWithTransform(Polygon):
    def get_transformMatrix(self): return self.get('transformMatrix')
    def set_transformMatrix(self, v): return self.set({'transformMatrix': v})
    transformMatrix = property(get_transformMatrix, set_transformMatrix)

    def multMat(self, trans):
        newTrans = [[0,0], [0,0]]
        for i in range(len(newTrans)):
            for j in range(len(newTrans)):
                for k in range(len(newTrans)):
                    newTrans[i][j] += self.transformMatrix[k][j] * trans[i][k]
        self.transformMatrix = newTrans

    def doRotate(self, degrees, cx, cy):
        super().doRotate(degrees, cx, cy)
        radians = -utils.toRadians(degrees)
        rotateTrans = [
            [math.cos(radians), math.sin(radians)],
            [-math.sin(radians), math.cos(radians)]
        ]
        self.multMat(rotateTrans)

    def scalexy(self, varName, k, scaleAnchor = None):
        super().scalexy(varName, k, scaleAnchor)
        if k == 1: return
        i = 0 if (varName == 'x') else 1

        trans = [[1, 0], [0, 1]]
        trans[i][i] = k
        self.multMat(trans)

class CMUSound(object):
    processes = []
    def __init__(self, url):
        current_directory = os.path.dirname(__file__)
        sound_path = os.path.join(current_directory, 'sound.py')
        self.soundProcess = subprocess.Popen(
            [sys.executable, sound_path], stdout=subprocess.PIPE,
            stdin=subprocess.PIPE, stderr=subprocess.PIPE,
            cwd=current_directory)
        CMUSound.processes.append(self.soundProcess)
        self.sendProcessMessage({'url': url})

    def sendProcessMessage(self, message):
        packet = bytes(json.dumps(message) + '\n', encoding='utf-8')
        self.soundProcess.stdin.write(packet)
        self.soundProcess.stdin.flush()
        self.soundProcess.stdout.readline()
        self.soundProcess.poll()
        if self.soundProcess.returncode is not None and self.soundProcess.returncode != 0:
            print(self.soundProcess.stderr.read().decode('utf-8'))
            raise Exception('Exception in Sound.')

    def play(self, doLoop, doRestart):
        self.sendProcessMessage({
            'command': 'play',
            'kwargs': {
                'doLoop': doLoop,
                'doRestart': doRestart
            }
        })

    def pause(self):
        self.sendProcessMessage({
            'command': 'pause',
            'kwargs': {}
        })

def cleanSoundProcesses():
    for p in CMUSound.processes: p.kill()

# clean up processes when the interpreter closes
atexit.register(cleanSoundProcesses)

class CMUImage(PolygonWithTransform):
    def __init__(self, attrs):
        if attrs is not None:
            imageData = loadImage(attrs['url'])

            height, width = imageData['height'], imageData['width']
            right = attrs['left'] + width
            bottom = attrs['top'] + height
            attrs['defaultAlign'] = 'left-top'
            attrs['initialPoints'] = [
                attrs['left'], attrs['top'],
                right, attrs['top'],
                right, bottom,
                attrs['left'], bottom
            ]
            attrs['transformMatrix'] = [
                [1, 0],
                [0, 1],
            ]
            super().__init__(attrs)
            self.attrDefaults = copy.deepcopy(self.attrDefaults)
            self.attrDefaults.update({'fill': None})

    def get_url(self): return self.get('url')
    def set_url(self, v): return self.set({'url': v})
    url = property(get_url, set_url)

    def getScaleAnchor(self): return [self.left, self.top]

    def drawImage(self, ctx):
        mat = self.transformMatrix
        ctx.translate(self.pointList[0][0], self.pointList[0][1])
        ctx.transform(cairo.Matrix(mat[0][0], mat[1][0], mat[0][1], mat[1][1], 0, 0))
        ctx.set_source_surface(activeDrawing.images[self.url], 0, 0)
        ctx.paint_with_alpha(self.opacity / 100)

    def toString(self):
        args = [self.left, self.top, self.width, self.height]
        return 'Image{args}'.format(args=utils.roundedTupleString(args, 2))

class Oval(PolygonWithTransform):
    def __init__(self, attrs):
        attrs['initialPoints'] = utils.flatten(utils.getArcPoints(
            attrs['centerX'], attrs['centerY'], attrs['width'], attrs['height'],
            attrs.get('startAngle', None), attrs.get('sweepAngle', None)))
        attrs['transformMatrix'] = [
            [attrs['width'] / 2, 0],
            [0, attrs['height'] / 2],
        ]
        attrs['translation'] = [attrs['centerX'], attrs['centerY']]
        if ('startAngle' not in attrs):
            attrs['startAngle'] = 0
        if ('sweepAngle' not in attrs):
            attrs['sweepAngle'] = 360
        attrs['bezierPoints'] = Oval.getBezierPoints(attrs['startAngle'], attrs['sweepAngle'])
        super().__init__(attrs)

    @staticmethod
    def getBezierPoints(startAngle, sweepAngle):
        offset = utils.toRadians(startAngle)
        remaining = sweepAngle
        bp = []
        while (remaining > 0):
            bp.extend(Oval.getBezierFragment(utils.toRadians(min(90, remaining)), offset))
            offset += math.pi / 2
            remaining -= 90
        return bp

    @staticmethod
    def getBezierFragment(sweepAngle, offsetAngle):
        # Return a cubic Bezier curve that approximates up to 90 degrees of a circle.
        # https://www.tinaja.com/glib/bezcirc2.pdf
        result = [[0, 0], [0, 0], [0, 0], [0, 0]]
        result[3][0] = math.cos(sweepAngle / 2)
        result[3][1] = math.sin(sweepAngle / 2)
        result[0][0] = result[3][0]
        result[0][1] = -result[3][1]

        result[2][0] = (4 - result[3][0]) / 3
        result[2][1] = ((1 - result[3][0]) * (3 - result[3][0])) / (3 * result[3][1])
        result[1][0] = result[2][0]
        result[1][1] = -result[2][1]

        result = utils.rotatePoints(result, (sweepAngle / 2) + offsetAngle - (math.pi / 2), 0, 0)
        return result

    def get_bezierPoints(self): return self.get('bezierPoints')
    def set_bezierPoints(self, v): return self.set({'bezierPoints': v})
    bezierPoints = property(get_bezierPoints, set_bezierPoints)

    def get_translation(self): return self.get('translation')
    def set_translation(self, v): return self.set({'translation': v})
    translation = property(get_translation, set_translation)

    def makePath(self, ctx):
        ctx.save()
        ctx.new_path()
        ctx.translate(self.translation[0], self.translation[1])
        bp = list(map((lambda p:
            [self.transformMatrix[0][0] * p[0] + self.transformMatrix[0][1] * p[1],
             self.transformMatrix[1][0] * p[0] + self.transformMatrix[1][1] * p[1]]
            ), self.bezierPoints))
        if isinstance(self, Arc):
            ctx.move_to(0, 0)
            ctx.line_to(bp[0][0], bp[0][1])
        else:
            ctx.move_to(bp[0][0], bp[0][1])

        for i in range(0, len(bp) // 4):
            i2 = i * 4
            ctx.curve_to(bp[i2+1][0], bp[i2+1][1], bp[i2+2][0], bp[i2+2][1], bp[i2+3][0], bp[i2+3][1])

        ctx.close_path()
        ctx.restore()

    def addxy(self, varName, d):
        super().addxy(varName, d)
        if d == 0: return
        varIndex = 0 if varName == 'x' else 1
        self.translation[varIndex] += d
        self.translation = self.translation

    def scalexy(self, varName, k, scaleAnchor = None):
        super().scalexy(varName, k, scaleAnchor)
        if k == 1: return
        i = 0 if varName == 'x' else 1

        cxy = (scaleAnchor or self.getScaleAnchor())[i]
        self.translation[i] = cxy + (self.translation[i] - cxy) * k
        self.translation = self.translation

    def doRotate(self, degrees, cx, cy):
        super().doRotate(degrees, cx, cy)
        radians = -utils.toRadians(degrees)
        self.translation = utils.rotatePoint(self.translation, -radians, cx, cy)

    def toString(self):
        args = [self.centerX, self.centerY, self.width, self.height]
        return 'Oval{args}'.format(args=utils.roundedTupleString(args, 2))

class Arc(Oval):
    def __init__(self, attrs):
        super().__init__(attrs)
        self.ovalWidth = attrs['width']
        self.ovalHeight = attrs['height']

    def get_ovalWidth(self): return self.get('ovalWidth')
    def set_ovalWidth(self, v): return self.set({'ovalWidth': v})
    ovalWidth = property(get_ovalWidth, set_ovalWidth)

    def get_ovalHeight(self): return self.get('ovalHeight')
    def set_ovalHeight(self, v): return self.set({'ovalHeight': v})
    ovalHeight = property(get_ovalHeight, set_ovalHeight)

    def doRotate(self, degrees, cx, cy):
        super().doRotate(degrees, cx, cy)

    def scalexy(self, varName, k, scaleAnchor = None):
        super().scalexy(varName, k, scaleAnchor)
        if (k == 1 or self.ovalWidth is None or self.ovalHeight is None):
            return

        if (self.rotateAngle != 0):
            self.ovalWidth = None
            self.ovalHeight = None
            return

        if (varName == 'x'):
            self.ovalWidth *= k
        elif (varName == 'y'):
            self.ovalHeight *= k

    def get_startAngle(self): return self.get('startAngle')
    def set_startAngle(self, v):
        self.set({'startAngle': v})
        self.regeneratePoints()
        return v
    startAngle = property(get_startAngle, set_startAngle)

    def get_sweepAngle(self): return self.get('sweepAngle')
    def set_sweepAngle(self, v):
        self.set({'sweepAngle': v})
        self.regeneratePoints()
        return v
    sweepAngle = property(get_sweepAngle, set_sweepAngle)

    def regeneratePoints(self):
        self.pointList = utils.getArcPoints(
            0, 0, 2, 2, self.startAngle, self.sweepAngle,
            (self.width + self.height) / 2
        )
        for pt in self.pointList:
            newPt = [
                self.transformMatrix[0][0] * pt[0] + self.transformMatrix[0][1] * pt[1],
                self.transformMatrix[1][0] * pt[0] + self.transformMatrix[1][1] * pt[1]
            ]
            pt[0] = newPt[0] + self.translation[0]
            pt[1] = newPt[1] + self.translation[1]
        self.pointList = self.pointList
        self.bezierPoints = Oval.getBezierPoints(self.startAngle, self.sweepAngle)

    def getRotateAnchor(self):
        return [self.pointList[0][0], self.pointList[0][1]]

    def get_centerX(self): return utils.round2(self.pointList[0][0])
    def set_centerX(self, v): self.addx(v - self.centerX)
    centerX = property(get_centerX, set_centerX)

    def get_centerY(self): return utils.round2(self.pointList[0][1])
    def set_centerY(self, v): self.addy(v - self.centerY)
    centerY = property(get_centerY, set_centerY)

class Circle(Oval):
    def __init__(self, attrs):
        attrs['width'] = attrs['height'] = 2 * attrs['radius']
        super().__init__(attrs)
        self._exactRadius = attrs['radius']

    def get_radius(self):
        if self._exactRadius != None:
            return self._exactRadius
        return (self.get('width') + self.get('height')) / 4
    def set_radius(self, v):
        super().set_width(2 * v)
        super().set_height(2 * v)
        self._exactRadius = v
        return v
    radius = property(get_radius, set_radius)

    def get__exactRadius(self): return self.get('_exactRadius')
    def set__exactRadius(self, v): return self.set({'_exactRadius': v})
    _exactRadius = property(get__exactRadius, set__exactRadius)

    def get_width(self): return super().get_width()
    def set_width(self, v): self._exactRadius = None; super().set_width(v); return v
    width = property(get_width, set_width)

    def get_height(self): return super().get_height()
    def set_height(self, v): self._exactRadius = None; super().set_height(v); return v
    height = property(get_height, set_height)

    def toString(self):
        args = [self.centerX, self.centerY, self.radius]
        return 'Circle{args}'.format(args=utils.roundedTupleString(args, 2))

objConstructors = {
  'Arc': Arc,
  'Circle': Circle,
  'Gradient': Gradient,
  'Group': Group,
  'CMUImage': CMUImage,
  'Label': Label,
  'Line': Line,
  'Oval': Oval,
  'Polygon': Polygon,
  'Rect': Rect,
  'RegularPolygon': RegularPolygon,
  'RGB': RGB,
  'Star': Star,
}

BACKGROUND_POINTS = [
  [0, 0],
  [400, 0],
  [0, 400],
  [400, 400],
];
BACKGROUND_DUMMY = object()

class Inspector(object):
    def __init__(self, app):
        self.app = app
        self.keyPoints = None
        self.keyPointsToShapes = None
        self.bestX = self.bestY = self.mouseX = self.mouseY = None

    def getKeyPoints(self, shape):
        x0 = shape.left
        y0 = shape.top
        x1 = shape.right
        y1 = shape.bottom

        points = [
            [x0, y0],
            [x0, y1],
            [x1, y0],
            [x1, y1],
        ]

        if isinstance(shape, Arc):
            points = []
            points.append([shape.pointList[0][0], shape.pointList[0][1]])
            points.append([shape.pointList[1][0], shape.pointList[1][1]])
            numPoints = len(shape.pointList)
            points.append([
                shape.pointList[numPoints-1][0],
                shape.pointList[numPoints-1][1],
            ])
        elif (
            (shape.rotateAngle % 360 != 0 and
                (isinstance(shape, Oval) or isinstance(shape, Rect))) or
            isinstance(shape, Circle) or
            isinstance(shape, Oval) or
            isinstance(shape, Star) or
            isinstance(shape, RegularPolygon) or
            isinstance(shape, Label)
        ):
            points = [[shape.centerX, shape.centerY]]
        elif isinstance(shape, Line):
            points = [
                [shape.x1, shape.y1],
                [shape.x2, shape.y2],
            ]
        elif isinstance(shape, Polygon):
            points = []
            for i in range(len(shape.pointList)):
                points.append([shape.pointList[i][0], shape.pointList[i][1]])

        return list(map(lambda pt: [round(pt[0]), round(pt[1])], points))

    def getKeyPointKey(self, point):
        return '%d-%d' % (point[0], point[1])

    def ensureKeyPointToShapesMap(self):
        if (self.keyPointsToShapes != None):
            return
        self.keyPointsToShapes = dict()
        self.keyPoints = list()

        def addKeyPointTo(shape):
            def addKeyPoint(keyPoint):
                key = self.getKeyPointKey(keyPoint)
                if self.keyPointsToShapes.get(key, None) is None:
                    self.keyPointsToShapes[key] = []
                    self.keyPoints.append(keyPoint)
                self.keyPointsToShapes[key].append(shape)
            return addKeyPoint

        def processShape(shape):
            if shape.isGroup:
                list(map(processShape, shape._shapes))
                return
            if shape.doNotInspect:
                return

            list(map(addKeyPointTo(shape), self.getKeyPoints(shape)))

        processShape(self.app._tlg)
        if self.app.background is not None:
            list(map(addKeyPointTo(BACKGROUND_DUMMY), BACKGROUND_POINTS))


    def getKeyPointExtraShapeInfo(self, kx, ky):
        key = self.getKeyPointKey([kx, ky])
        attrVals = dict()
        def msgsAdd(attr, value):
            if attrVals.get(attr, None) is None:
                attrVals[attr] = set()
            if utils.isNumber(value):
                value = utils.round2(value)
            elif value == True:
                value = 'True'
            elif value == False:
                value = 'False'
            attrVals[attr].add(value)

        if self.keyPointsToShapes.get(key, None) is None:
            return ''

        def gradientToString(color):
            result = ''
            for value in color.colors:
                if isinstance(value, str):
                    result += value
                    result += ', '
                else:
                    result += value.attrs['strVal']
                    result += ', '
            return result[:-2]

        for shape in self.keyPointsToShapes[key]:
            if (shape is BACKGROUND_DUMMY):
                if isinstance(self.app.background, Gradient):
                    msgsAdd('background', gradientToString(self.app.background))
                else:
                    msgsAdd('background', self.app.background)
                continue

            for attr in ['fill', 'border']:
                color = getattr(shape, attr)
                if color is not None:
                    if isinstance(color, Gradient):
                        msgsAdd('gradient', gradientToString(color))
                    else:
                        msgsAdd('color', color)
                elif attr == 'fill' and not isinstance(shape, CMUImage):
                    msgsAdd('color', 'None')

            def checkAttrDefaults(attrDefaults):
                for attr, defaultVal in attrDefaults:
                    try:
                        val = getattr(shape, attr)
                        if val != None and val != defaultVal:
                            msgsAdd(attr, val)
                    except:
                        pass
            checkAttrDefaults([
                ['opacity', 100],
                ['lineWidth', 2],
                ['radius', None],
                ['dashes', False]
            ])
            if isinstance(shape, Label):
                checkAttrDefaults([
                    ['font', 'Arial'],
                    ['size', 12],
                    ['style', 'normal'],
                    ['bold', False],
                    ['italic', False],
                ])
            if isinstance(shape, Line):
                checkAttrDefaults([
                    ['arrowStart', False],
                    ['arrowEnd', False]
                ])
            if (not isinstance(shape, Label) and not isinstance(shape, Line)):
                checkAttrDefaults([['borderWidth', 2]])
            if isinstance(shape, Star):
                checkAttrDefaults([
                    ['roundness', utils.getDefaultRoundness(shape.points)],
                ])
            if isinstance(shape, Star) or isinstance(shape, RegularPolygon):
                checkAttrDefaults([['points', None]])
            if shape.rotateAngle % 360 != 0:
                msgsAdd('rotateAngle', shape.rotateAngle)
            if isinstance(shape, Arc):
                checkAttrDefaults([
                    ['sweepAngle', None],
                    ['startAngle', None],
                ])
                if (shape.ovalWidth != None and shape.ovalHeight != None):
                    msgsAdd(
                        'oval size',
                        '(%d, %d)' % (
                            utils.round2(shape.ovalWidth),
                            utils.round2(shape.ovalHeight)
                        )
                    )
            if (
                (isinstance(shape, Oval) and
                    not isinstance(shape, Circle) and
                    not isinstance(shape, Arc)) or
                (shape.rotateAngle % 360 != 0 and isinstance(shape, Rect))
            ):
                pts = shape.getApproxPoints()
                unrotatedPoints = utils.rotatePoints(
                    pts,
                    -shape.rotateAngle,
                    shape.centerX,
                    shape.centerY
                )
                bounds = utils.getBoxDims(unrotatedPoints)
                msgsAdd(
                    'size',
                    '(%d, %d)' % (
                        utils.round2(bounds['width']),
                        utils.round2(bounds['height'])
                    )
                )
        msgs = [self.getPointStr(kx, ky)];
        for attr in attrVals:
            for val in attrVals[attr]:
                msgs.append('%s: %s' % (attr, str(val)))
        return '\n'.join(msgs)

    def getPointStr(self, x, y):
        return '(%d, %d)' % (x, y)

    def nearestKeyPoint(self, x, y):
        bestD = 100000000
        bestX = None
        bestY = None
        for pt in self.keyPoints:
            d = (pt[0] - x) ** 2 + (pt[1] - y) ** 2
            if d < bestD:
                bestD = d
                [bestX, bestY] = pt
        return [bestX, bestY]

    def reset(self):
        self.mouseX = self.mouseY = None
        self.clearCache()

    def clearCache(self):
        self.keyPoints = self.keyPointsToShapes = None
        self.bestX = self.bestY = None

    def setMousePosition(self, x, y):
        self.mouseX = x
        self.mouseY = y
        self.bestX = self.bestY = None

    def computeBestPoint(self):
        if self.mouseX is None or self.mouseX is None:
            return
        self.ensureKeyPointToShapesMap()
        bestX, bestY = self.nearestKeyPoint(self.mouseX, self.mouseY)

        if (
            bestX is None or
            utils.distance(self.mouseX, self.mouseY, bestX, bestY) > 300
        ):
            self.bestX = self.bestY = None
        else:
            self.bestX = bestX
            self.bestY = bestY

    def draw(self, ctx):
        self.computeBestPoint()
        if self.bestX is None or self.bestY is None:
            return

        black = (0, 0, 0)
        red = (0, 0, 255)
        gold = (0, 215, 255)
        white = (255, 255, 255)

        for pt in self.keyPoints:
            ctx.new_path()
            ctx.arc(pt[0], pt[1], 2, 0, 2 * math.pi)
            ctx.close_path()
            ctx.set_source_rgba(*black)
            ctx.set_line_width(2)
            ctx.stroke_preserve()
            ctx.set_source_rgba(*gold)
            ctx.fill()

        ctx.set_source_rgba(*red)
        for r in [5, 4, 3, 2, 1]:
            ctx.set_source_rgb(*(red if r % 2 == 1 else black))
            ctx.new_path()
            ctx.arc(self.bestX, self.bestY, r, 0, 2 * math.pi)
            ctx.close_path()
            ctx.fill()

        def textWidth(text):
            return ctx.text_extents(text)[2]

        def drawCenteredText(text, x, y):
            x, y = int(x), int(y)
            _, _, width, _, _, _ = ctx.text_extents(text)
            ctx.move_to(x - width / 2, y)
            ctx.show_text(text)

        ctx.select_font_face(*getFont('arial'))
        ctx.set_font_size(12)
        pointLabelText = self.getPointStr(self.bestX, self.bestY)
        w = textWidth(pointLabelText)
        h = 12
        margin = 10
        pointLabelCenterX = min(
            400 - margin - w / 2,
            max(margin + w / 2, self.bestX - 10)
        )
        pointLabelCenterY = min(
            400 - margin - h / 2,
            max(margin + h / 2, self.bestY - 10)
        )

        ctx.set_source_rgba(*white, 0.5)
        ctx.rectangle(
            pointLabelCenterX - w / 2 - 2,
            pointLabelCenterY - h / 2 - 2,
            w + 4,
            h + 4
        )
        ctx.fill()

        ctx.set_source_rgba(*black)
        drawCenteredText(
            pointLabelText,
            pointLabelCenterX,
            pointLabelCenterY + h / 2 - 2,
        )

        minTop = 10
        if pointLabelCenterX > 300 and pointLabelCenterY < 50:
            minTop = pointLabelCenterY + margin
        info = self.getKeyPointExtraShapeInfo(self.bestX, self.bestY)
        infoLines = info.split('\n')
        ctx.set_source_rgba(*white, 0.5)
        infoWidth = 0
        newLines = []
        maxWidth = 300

        def shortenLine(line):
            splitLine = line.split(',')
            return [splitLine.pop(), ''.join(splitLine)]

        for line in infoLines:
            if textWidth(line) < maxWidth:
                newLines.append(line)
            else:
                leftover = ''
                while textWidth(line) > maxWidth:
                    lastWord, line = shortenLine(line)
                    if len(leftover) > 0:
                        leftover = ',' + leftover
                    leftover = lastWord + leftover
                if len(leftover) > 0:
                    line = line + ','
                newLines.append(line, leftover)

        for line in newLines:
            infoWidth = max(infoWidth, textWidth(line))

        lineHeight = 12
        infoHeight = lineHeight * len(newLines)
        ctx.rectangle(
            400 - 2 * margin - infoWidth,
            minTop,
            infoWidth + 2 * margin,
            infoHeight + margin
        )
        ctx.fill()
        ctx.set_source_rgba(*black)
        verticalOffset = 0
        for line in newLines:
            firstword = line[0:line.find(':')+1]
            newline = line[line.find(':')+1:]
            ctx.select_font_face(*getFont('arial', isBold=True))
            firstwordWidth = textWidth(firstword)
            ctx.select_font_face(*getFont('arial'))
            newlineWidth = textWidth(newline)
            ctx.select_font_face(*getFont('arial', isBold=True))

            drawCenteredText(
                firstword,
                400 -
                    margin -
                    infoWidth / 2 -
                    (newlineWidth + firstwordWidth) / 2 +
                    firstwordWidth / 2,
                minTop + lineHeight + verticalOffset
            )

            ctx.select_font_face(*getFont('arial'))
            drawCenteredText(
                newline,
                400 -
                    margin -
                    infoWidth / 2 +
                    (newlineWidth + firstwordWidth) / 2 -
                    newlineWidth / 2,
                minTop + lineHeight + verticalOffset
            )
            verticalOffset += lineHeight

class ShapeLogicInterface(object):
    def rgb(self, r, g, b):
        return RGB(r, g, b)

    def gradient(self, *colors, start='center'):
        checkArgCount(None, 'gradient', ['colors', 'start'], (colors, start))
        return Gradient(list(colors), start)

    def newSound(self, url):
        checkArgCount(None, 'Sound', ['url'], (url,))
        checkString('Sound', 'url', url)
        return CMUSound(url)

    def slNew(self, className, args):
        return (objConstructors[className])(args)

    def slApply(self, slObj, method, args, kwargs):
        args = list(args)
        # 1. replace student shapes with sl shapes
        for i in range(len(args)):
            if hasattr(args[i], '_shape'):
                args[i] = args[i]._shape
        # 2. make the call
        result = (getattr(slObj, method))(*args, **kwargs)
        # 3. replace sl shapes with student shapes and return
        if isinstance(result, Shape):
            if hasattr(result, 'studentShape'):
                utils.internalError('Need to wrap new sl shape in student shape')
            result = result.studentShape
        return result

    def slGet(self, slObj, attr):
        if not hasattr(slObj, attr):
            pyThrow('No such attribute: {attr}'.format(attr=attr))
        result = getattr(slObj, attr)
        if callable(result):
            result = lambda *args, **kwargs: self.slApply(slObj, attr, args, kwargs)
        return result

    def slSet(self, obj, attr, val):
        if shapeAttrs.get(attr, None) is not None:
            shapeAttrs[attr].typeCheckFn(obj, attr, val)
        try:
            setattr(obj, attr, val)
        except:
            # TODO: print console.error(e)
            raise
        return val

    def slSetAppProperty(app, propName, value):
        if propName == 'maxShapeCount':
            checkNumber('app.setMaxShapeCount(n)', 'n', value)
        activeDrawing.appProperties[propName] = value

    def slGetAppProperty(app, propName):
        return activeDrawing.appProperties[propName]

    def slInitShape(self, clsName, argNames, args, kwargs):
        if clsName == 'Image':
            clsName = 'CMUImage'
        checkArgCount(clsName, None, argNames, args)
        for attr in kwargs:
            if shapeAttrs.get(attr, None) is None:
                pyThrow('"{attr}" is not a valid shape constructor argument'.format(attr=attr))
        if kwargs.get('align', None) is not None and clsName == 'Polygon':
            pyThrow('"align" is not a valid Polygon constructor argument')
        constructorArgs = dict()
        for i in range(0, len(argNames)):
            constructorArgs[argNames[i]] = args[i]
        shape = self.slNew(clsName, constructorArgs)
        try:
            align = None
            if 'align' in kwargs:
                align = kwargs['align']
                del kwargs['align']
            for attr in kwargs:
                self.slSet(shape, attr, kwargs[attr])
            if align is not None:
                checkString(shape, 'align', align)
                xPoint = constructorArgs.get('left', None) if constructorArgs.get('centerX', None) is None else constructorArgs['centerX']
                yPoint = constructorArgs.get('top', None) if constructorArgs.get('centerY', None) is None else constructorArgs['centerY']
                shape.doAlign(xPoint, yPoint, align)
        except:
            activeDrawing.tlg.remove(shape)
            raise
        return shape

    def setTopLevelGroup(self, tlg):
        activeDrawing.tlg = tlg
