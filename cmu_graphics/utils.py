import decimal
import math
from . import shape_logic
from collections import defaultdict

def toDegrees(radians): return radians * 180 / math.pi
def toRadians(degrees): return degrees * math.pi / 180

def fromPythonAngle(radians): return (90 - toDegrees(radians)) % 360
def toPythonAngle(degrees): return (toRadians(90 - degrees)) % (2 * math.pi)

def intSin(degrees):
    if isinstance(degrees, float) and degrees.is_integer():
        degrees = int(degrees)
    if isinstance(degrees, int):
        degrees = degrees % 360
        if (degrees == 0 or degrees == 180):
            return 0
        elif degrees == 90:
            return 1
        elif degrees == 270:
            return -1
    return math.sin(toRadians(degrees))

def intCos(degrees):
    if isinstance(degrees, float) and degrees.is_integer():
        degrees = int(degrees)
    if isinstance(degrees, int):
        degrees = degrees % 360
        if (degrees == 90 or degrees == 270):
            return 0
        elif degrees == 0:
            return 1
        elif degrees == 180:
            return -1
    return math.cos(toRadians(degrees))

pythonRound = round

def round(*args):
    raise Exception("Use our rounded(n) instead of Python 3's round(n)\n"
                    "  Python 3's round(n) does not work as one might expect!\n"
                    "  If you still want Python 3's round, use pythonRound")

def rounded(d):
    sign = 1 if (d >= 0) else -1
    d = abs(d)
    n = int(d)
    if (d - n >= 0.5): n += 1
    return sign * n

EPSILON = 10e-7
def almostEqual(x, y, epsilon=EPSILON):
    return abs(x - y) <= epsilon

def makeList(rows, cols, value=None):
    if rows < 0 or cols < 0:
        raise Exception('Both rows and cols must be >= 0')
    return [[value for _ in range(cols)] for _ in range(rows)]

def getPointInDir(x1, y1, degrees, d):
    A = toPythonAngle(degrees)
    return [x1 + d * math.cos(A), y1 - d * math.sin(A)]

def angleTo(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return fromPythonAngle(math.atan2(-dy, dx)) # use -dy since up is down

def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def internalError(err):
    raise Exception('Internal Error: {err}'.format(err=err))

def polygonContainsPoint(pts, px, py):
    # based on: https://github.com/mathigon/fermat.js/blob/master/src/geometry.js
    n = len(pts)
    inside = False
    for i in range(n):
        q1 = pts[i]
        q2 = pts[(i + 1) % n]
        q1x = q1[0]
        q1y = q1[1]
        q2x = q2[0]
        q2y = q2[1]
        if distanceToLineSegment2(px, py, q1x, q1y, q2x, q2y) < 0.0002:
            return True
        x = (q1y > py) != (q2y > py)
        if (q2y - q1y == 0):
            y = True
        else:
            y = px < (q2x - q1x) * (py - q1y) / (q2y - q1y) + q1x
        if (x and y): inside = not inside
    return inside

def pointNearPolygonBorder(pts, x, y, d):
    # does not check if the polygon contains the point!
    d2 = d ** 2
    n = len(pts)
    for i in range(n):
        p1 = pts[i]
        p2 = pts[(i + 1) % n]
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        if (distanceToLineSegment2(x, y, x1, y1, x2, y2) <= d2):
            return True
    return False

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def distance2(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

def distanceToLineSegment2(x, y, x1, y1, x2, y2):
    # return square of distance from (x,y) to ((x1,y1),(x2,y2))
    # inspired by https://stackoverflow.com/questions/849211/shortest-distance-between-a-point-and-a-line-segment/24913403
    l2 = distance2(x1, y1, x2, y2)
    if (l2 == 0): return distance(x, y, x1, y1)
    t = ((x - x1) * (x2 - x1) + (y - y1) * (y2 - y1)) / l2
    t = max(0, min(1, t))
    return distance2(x, y, x1 + t * (x2 - x1), y1 + t * (y2 - y1))

def edgesIntersect(edges1, edges2):
    ADD = True
    REMOVE = False

    x_to_events = defaultdict(list)
    for (shape, edges) in ((1, edges1), (2, edges2)):
        for edge in edges:
            # Assumes that x1 <= x2 for all edges
            (x1, _, x2, _) = edge
            x_to_events[x1].append((shape, ADD, edge))
            x_to_events[x2].append((shape, REMOVE, edge))

    active_edges1 = set()
    active_edges2 = set()

    # Here we're looping over a list of all line segments' start and ends points,
    # which is sorted by the points' x values. 
    # 
    # We're keeping track of which line segments are "active" as we go
    # (which line segments intersect with the line x=x for the current x value).
    # 
    # When we encounter a new line segment, we see if it intersects with any
    # active line segments in the other shape. 
    for (_, events) in sorted(x_to_events.items(), key=lambda item: item[0]):
        for shape, event_type, edge1 in events:
            my_active_edges, other_active_edges = (active_edges1, active_edges2) if shape == 1 else (active_edges2, active_edges1)
            if event_type == ADD:
                for edge2 in other_active_edges:
                    if segmentsIntersect(*edge1, *edge2):
                        return True
                my_active_edges.add(edge1)
            else:
                my_active_edges.remove(edge1)

    return False

def segmentsIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
    dxa = x2 - x1
    dya = y2 - y1
    dxb = x4 - x3
    dyb = y4 - y3
    s = math.inf if (-dxb * dya + dxa * dyb) == 0 else (-dya * (x1 - x3) + dxa * (y1 - y3)) / (-dxb * dya + dxa * dyb)
    t = math.inf if (-dxb * dya + dxa * dyb) == 0 else (+dxb * (y1 - y3) - dyb * (x1 - x3)) / (-dxb * dya + dxa * dyb)
    return (s >= 0 and s <= 1 and t >= 0 and t <= 1)

def isGroup(shape):
    if hasattr(shape, '_shape'):
        shape = shape._shape
    return isinstance(shape, shape_logic.Group)

def getChildShapes(shape):
    result = []
    if hasattr(shape, '_shape'):
        shape = shape._shape
    if isGroup(shape):
        for s in shape.children:
            result += getChildShapes(s)
    else:
        result = [shape]
    return result

def getPolygonArea(pts):
    A = 0
    for i in range (0, len(pts)):
        j = (i + 1) % len(pts)
        A += (pts[i][0] * pts[j][1] - pts[j][0] * pts[i][1])
    return A / 2

def getPolygonCentroid(pts):
    A = getPolygonArea(pts)
    if (A < 0.00001):
        # If the area of the polygon is small enough, average the points instead
        # of returning a value that is heavily influenced by floating point error
        sumX = 0
        sumY = 0
        for i in range(0, len(pts)):
            sumX += pts[i][0]
            sumY += pts[i][1]
        return [sumX / len(pts), sumY / len(pts)]
    cx, cy = 0, 0
    for i in range(0, len(pts)):
        j = (i + 1) % len(pts)
        term = (pts[i][0] * pts[j][1] - pts[j][0] * pts[i][1])
        cx += (pts[i][0] + pts[j][0]) * term
        cy += (pts[i][1] + pts[j][1]) * term
    return [cx / (6 * A), cy / (6 * A)]

def rotatePoint(pt, degrees, cx, cy):
    [x, y] = pt
    cos = intCos(degrees)
    sin = intSin(degrees)
    return [cx + ((x - cx) * cos - (y - cy) * sin),
            cy + ((x - cx) * sin + (y - cy) * cos)]

def rotatePoints(pts, degrees, cx, cy):
    return list(map(lambda pt: rotatePoint(pt, degrees, cx, cy), pts))


def getBoxDims(pts):
    if len(pts) == 0:
        internalError('getBoxDims: empty points list')

    xlo = xhi = pts[0][0]
    ylo = yhi = pts[0][1]
    for pt in pts:
        [x, y] = pt
        if (x < xlo): xlo = x
        elif (x > xhi): xhi = x
        if (y < ylo): ylo = y
        elif (y > yhi): yhi = y
    return {'left': xlo, 'top': ylo, 'width': xhi - xlo, 'height': yhi - ylo}

def flatten(a):
    out = []
    for elem in a:
        if isinstance(elem, list):
            out.extend(flatten(elem))
        else:
            out.append(elem)
    return out

def truncateIntegerFloats(n):
    if isinstance(n, float) and n.is_integer():
        return int(n)
    return n

def utilsRounded(n, precision = 0):
    if isinstance(n, list) or isinstance(n, tuple): return list(map(lambda v: utilsRounded(v, precision), n))
    elif not (isinstance(n, int) or isinstance(n, float)): return n
    elif n < 0: return -utilsRounded(-n, precision)
    return truncateIntegerFloats(roundHalfUp(n * 10 ** precision) / 10 ** precision)

def tupleString(a):
    return "({s})".format(s=', '.join(map(str, a)))

def roundedTupleString(a, precision = 0):
    return tupleString(utilsRounded(a, precision))

def getArcPoints(cx, cy, width, height, startAngle = None, sweepAngle = None, sizeForN = None, isMvc = False):
    # get points that approximate an oval
    a, b = width / 2, height / 2
    pts = []
    if sizeForN is None:
        sizeForN = (a + b) / 2
    if startAngle is None:
        startAngle = 0
    if sweepAngle is None:
        sweepAngle = 360
    else:
        pts.append([cx, cy])
    n = rounded(6 + 18 * sizeForN / 50)
    n = math.ceil(n / 4) * 4
    denominator = n if sweepAngle == 360 else n - 1
    startAngle = toRadians(startAngle) if isMvc else toRadians(90 - startAngle) 
    sweepAngle = toRadians(sweepAngle)
    multiplyFactor = 1 if isMvc else -1;
    for i in range(n):
        theta = startAngle + (multiplyFactor * (sweepAngle * i / denominator))
        x = cx + a * math.cos(theta)
        y = cy - b * math.sin(theta)
        pts.append([x, y])
    return pts

def isNumber(value):
    return isinstance(value, int) or isinstance(value, float)

def round6(value):
    return pythonRound((value + 0.00000001) * 1000000) / 1000000

def round2(value):
    return pythonRound((value + 0.001) * 100) / 100

def makePolygonPath(pts, ctx):
    ctx.new_path()
    if pts is None or len(pts) == 0:
        return
    lastPt = pts[-1]
    ctx.move_to(lastPt[0], lastPt[1])
    for pt in pts: ctx.line_to(pt[0], pt[1])

def getLinePoints(x1, y1, x2, y2, lineWidth):
    # 0. get angle of rotation clockwise past horizontal
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    a = angleTo(x1, y1, x2, y2) - 90 # -90 so we're off the horizontal

    # 1. unrotate to horizontal, with p3 n the left, p4 on the right
    pts = [[x1, y1], [x2, y2]]
    pts = rotatePoints(pts, -a, cx, cy)
    x3 = pts[0][0]
    y3 = pts[0][1]
    x4 = pts[1][0]
    y4 = pts[1][1] # y3 should be isClose to y4

    # 2. define bounding box around the unrotated-to-horizontal line
    s = lineWidth / 2
    pts = [[x3, y3 - s], [x4, y3 - s], [x4, y4 + s], [x3, y4 + s]]
    return rotatePoints(pts, a, cx, cy)


def getRegularPolygonPoints(cx, cy, r, points, rotateAngle):
    pts = [[cx, cy - r]]
    dtheta = 360 / points
    for i in range(1, points):
        [x, y] = getPointInDir(cx, cy, i * dtheta, r)
        pts.append([x, y])
    if rotateAngle: pts = rotatePoints(pts, rotateAngle, cx, cy)
    return pts

def getDefaultRoundness(points):
    return 38.196601125 if points < 6 else 57.735026919

def getStarPoints(cx, cy, r, points, roundness, rotateAngle):
    if roundness is None: roundness = getDefaultRoundness(points)
    if roundness < 5: roundness = 5
    innerR = r * roundness / 100
    pts = [[cx, cy - r]]
    dtheta = 360 / points
    for i in range(points):
        if i > 0:
            [x, y] = getPointInDir(cx, cy, i * dtheta, r)
            pts.append([x, y])
        [x, y] = getPointInDir(cx, cy, i * dtheta + dtheta / 2, innerR)
        pts.append([x, y])
    if rotateAngle: pts = rotatePoints(pts, rotateAngle, cx, cy)
    return pts

def convertLabelValue(value):
    if callable(value): return '<function>'
    return str(value)

def min_or_inf(L):
    if len(L) == 0:
        return math.inf
    return min(L)