from cmu_graphics import *

r = Circle(200, 100, 50)
o = Oval(200, 100, 100, 30, fill='red')
rp = RegularPolygon(200, 100, 50, 3, fill='green')

def rotateTest(cx, cy, d):
    for s in [r, o, rp]:
        s.rotate(d, cx, cy)


# test rotating around the center
# -
rotateTest(200, 200, 15)

# -
rotateTest(200, 200, 30)

# -
rotateTest(200, 200, 72)

# test rotating around an arbitrary point inside the canvas
# -
rotateTest(378, 194, 30)

# -
rotateTest(378, 194, 90)

# -
rotateTest(378, 194, -57)

# test rotating around an arbitrary point outside the canvas
# -
rotateTest(431, -18, 30)

# -
rotateTest(431, -18, -45)

# -
rotateTest(431, -18, 24)

# -
# Test rotating an arc around a center that is not the circle center
a = Arc(200, 200, 150, 150, 90, 180, db='all')
r = Rect(0, 0, 10, 10)
g = Group(a, r)
g.rotate(45, 100, 100)

cmu_graphics.run()
