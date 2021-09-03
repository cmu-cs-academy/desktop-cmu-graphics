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
# Group length
g2 = Group()
assert len(g2) == 0
g2.add(Rect(50, 50, 50, 50))
assert len(g2) == 1
g2.add(Rect(100, 100, 50, 50))
assert len(g2) == 2

r2 = Rect(200, 200, 50, 50)
g2.add(r2)
assert len(g2) == 3
g2.remove(r2)
assert len(g2) == 2
g2.visible = False

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

r142 = Rect(50, 50, 200, 200)
g = Group(r142)

# Make sure that r142.group evaluates properly
count = 0
for shape in r142.group:
    count += 1
assert count == 1

g.clear()
assert r142.visible == False
r142.visible = False
r142.visible = True
r142.visible = False

g3 = Group()
g3.add(Group())
g3.add(Circle(1, 1, 1))
# Make sure that resizing a group that contains an empty group doesn't crash
g3.width += 1

###
# Zero height/width lines
l = Line(50, 200, 50, 300, fill=gradient('black', 'red'))
l.y1 = l.y2 = 200
l.height = 100

l2 = Line(350, 200, 350, 400, fill=gradient('black', 'red'))
g = Group(l2)

l2.y1 = l2.y2 = 200
g.height = 100

l3 = Line(50, 200, 100, 200, fill=gradient('black', 'red'))
l3.x1 = l3.x2 = 50
l3.width = 100

l4 = Line(350, 200, 350, 200, fill=gradient('black', 'red'))
g2 = Group(l4)
g2.width = 100

x = Group()
y = Group(x)
z = Group(y)
add_successful = False
try:
    x.add(z)
    add_successful = True
except Exception:
    pass
assert not add_successful, "Recursive groups should not be allowed"


# Make sure that containsShape works for concave shapes
concave = Polygon(0, 0, 300, 0, 300, 300, 200, 300, 200, 150, 100, 150, 100, 300, 0, 300)
not_inside = Rect(50, 50, 200, 200, fill='yellow', opacity=50, align='left-top')
assert not concave.containsShape(not_inside)
not_inside.height = 50
not_inside.width = 50
assert concave.containsShape(not_inside)

concave.visible = False
not_inside.visible = False

# Check that hitsShape works correctly for images without fill
url = 'https://s3.amazonaws.com/cmu-cs-academy.lib.prod/default_avatar.png'
img = Image(url, 100, 100)
img.width = 200
img.height = 200
c1 = Circle(150, 200, 50)
c2 = Circle(200, 200, 50)
assert img.hitsShape(c1)
assert img.hitsShape(c2)
assert c1.hitsShape(img)
assert c2.hitsShape(img)

Group(img, c1, c2, visible=False)

# Ensure can have attributes that translate to the same word
custom = Rect(200, 200, 200, 200, visible=False)
custom.reiniciar = 'a'
custom.restart = 'b'
assert custom.reiniciar == 'a'
assert custom.restart == 'b'

# Ensures that pointList isn't available for other shapes
assertRaises(lambda: r1.pointList)
assertRaises(lambda: c1.pointList)

# Zero-point polygon should not cause hitsShape to crash
p = Polygon()
assert not c1.hitsShape(p)
assert not p.hitsShape(c1)

# Ensure that star borders are closed
Star(200, 200, 150, 5, fill=None, border='black', borderWidth=20)

# Ensure group attribute works correctly
c = Circle(200, 20, 5)
g = Group(c)

def setGroup(shape, val):
  shape.group = val

# should not be possible to set group
assertRaises(lambda: setGroup(c, g))

assert app.group.group == None

c.visible = False
assert c.group == None

g2 = Group(c)
g2.remove(c)

assert c.group == None

c.visible = True
assert c.group == g2
assert len(g2.children) == 1

g.visible = False
g2.visible = False

# Ensure .toFront() doesn't crash when group is null
removedRect = Rect(200, 200, 100, 100)
app.group.remove(removedRect)
removedRect.toFront()