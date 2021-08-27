CENTER_X = 200
CENTER_Y = 250

Rect(CENTER_X, CENTER_Y, 200, 200, align='center', fill='green')
Rect(CENTER_X, CENTER_Y, 100, 100, align='center', fill='red')

c = Circle(CENTER_X, CENTER_Y, 50)

###
# Interactive test that can be used to ensure that the
# inspector is also working properly:
# def onMousePress(x, y):
#     c.radius = 50
#     check(50)
# def onMouseRelease(x, y):
#     c.radius = 100
#     check(100)

def round_eq(a, b):
    return rounded(a) == rounded(b)

def check(r):
    assert round_eq(c.radius, r)
    assert round_eq(c.width, 2 * r)
    assert round_eq(c.height, 2 * r)
    assert c.rotateAngle == 0

check(50)

# -
c.radius = 100
check(100)

# -
c.radius = 50
check(50)

# -
c.radius = 100
check(100)

# Check radius for circle with different height and width
# Radius should be half of the average of height and width
# -
c.radius = 50
c.width = 200
assert c.width == 200
assert c.height == 100
assert rounded(c.radius) == 75
assert c.rotateAngle == 0

# Check if circle is resized by group
# -
c.radius = 50
g = Group(c)
g.width += 100
g.height += 100
check(100)