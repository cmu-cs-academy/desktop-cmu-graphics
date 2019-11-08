def assertRaises(fn):
    raised = True
    try:
        fn()
        raised = False
    except:
        pass
    if not raised:
        raise Exception('fn failed to raise an exception')

###
# Basic group children behavior
r1 = Rect(10, 20, 30, 40)
r2 = Rect(40, 50, 60, 70)
g = Group(r1, r2)

assert len(g.children) == 2, g.children
g.shapes = 4
g._shapes = 1233

assert len(g.children) == 2, g.children
assert g.shapes == 4
assert g._shapes == 1233

g.foo = r2
assert g.foo == r2

###
# Returning Gradients or RGBs as properties
r = Rect(100, 100, 200, 200, fill=rgb(100, 200, 212))
assert r.fill.red == 100
assert r.fill.green == 200
assert r.fill.blue == 212

r = Rect(100, 100, 200, 200, fill=gradient('red', 'blue'))
assert r.fill.start == 'center'
assert r.fill.colors == ['red', 'blue']

###
# Star default roundness
s = Star(355, 355, 45, 5)
assert rounded(s.roundness) == 38, s.roundness
s.points = 6
assert rounded(s.roundness) == 58, s.roundness
s.points = 16
assert rounded(s.roundness) == 58, s.roundness
s.roundness=12
assert s.roundness == 12, s.roundness

###
# Gradient type checking
assertRaises(lambda: Rect(0, 0, 50, 50, fill=gradient('red', gradient('red', 'blue'))))
assertRaises(lambda: Rect(0, 0, 50, 50, fill=gradient('red', None)))


###
# Custom properties can't be used in a shape constructor
assertRaises(lambda: Circle(40, 40, 40, foo='bar'))


###
# Can't set width or height of shape to 0
assertRaises(lambda: Rect(200, 200, 100, 0))
assertRaises(lambda: Rect(200, 200, 0, 100))
s = Rect(200, 200, 100, 100)
def f():
    s.width = 0
assertRaises(f)
s.visible = False

assertRaises(lambda: Oval(200, 200, 100, 0))
assertRaises(lambda: Oval(200, 200, 0, 100))
s = Oval(200, 200, 100, 100)
def f():
    s.width = 0
assertRaises(f)
s.visible = False

assertRaises(lambda: Circle(200, 200, 0))
s = Circle(200, 200, 100)
def f():
    s.radius = 0
assertRaises(f)
s.visible = False

assertRaises(lambda: Line(200, 200, 0, 0, lineWidth=0))


###
# Can't use "align" with Polygons
assertRaises(lambda: Polygon(10, 10, 50, 50, align='left'))

###
# Can't get or set "align" property
r = Rect(0, 0, 100, 100)
def f():
    r.align = 'center'
assertRaises(f)
assertRaises(lambda: print(r.align))
r.visible = False

###
# Radial gradients should move with their object
r = Rect(0, 380, 20, 20, fill=gradient('black', 'white'))
# -
r.left += 10

assert isinstance(app.group, Group)

Line(320, 20, 370, 70, fill=None)

# Align should work even if centerX === 0
Oval(0, 0, 50, 50, align='left')

# Raise error if sweep angle is not in [0, 360]
assertRaises(lambda: Arc(200, 200, 200, 200, 90, -45))
assertRaises(lambda: Arc(200, 200, 200, 200, 90, -1))
assertRaises(lambda: Arc(200, 200, 200, 200, 90, 361))

# Raise error if roundness is not in [0, 100]
assertRaises(lambda: Star(355, 355, 45, 5, roundness=-1))
assertRaises(lambda: Star(355, 355, 45, 5, roundness=101))

# This should not throw an error
Polygon(fill=gradient('red', 'orange'))

# Test that rotating an empty group is OK
g = Group()
assert g.rotateAngle == 0
g.rotateAngle += 20
g.rotateAngle += 20
assert g.rotateAngle == 40

import time
from collections import defaultdict

grad = gradient('red', 'black', start='left-top')
assert grad.start == 'left-top'
grad2 = gradient('red', 'black', start='top-left')
assert grad2.start == 'top-left'
