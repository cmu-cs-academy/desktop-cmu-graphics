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

def check(r):
    assert c.radius == r
    assert c.width == 2*r
    assert c.height == 2*r
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
