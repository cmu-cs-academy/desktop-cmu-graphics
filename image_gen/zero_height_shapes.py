o = Oval(100, 200, 100, 0.0000000001, rotateAngle=45, db='all')
assert o.centerX == 100, o.centerX
assert o.centerY == 200, o.centerY

l = Line(0, 200, 400, 200, lineWidth=0.000000001)
# -
l.rotateAngle += 30
# -
l.rotateAngle += 30
# -
l.rotateAngle += 30

p = Polygon(10, 10, 10, 200, db='all')
assert p.centerX == 10
assert p.centerY == 105
