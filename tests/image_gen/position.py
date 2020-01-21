r1 = Rect(100, 100, 50, 50)
assert r1.centerX == 125
assert r1.centerY == 125
r1.centerX += 75
r1.centerY += 25
assert r1.centerX == 200 and r1.left == 175 and r1.right == 225
assert r1.centerY == 150 and r1.top == 125 and r1.bottom == 175
r1.rotateAngle = 30
assert r1.centerX == 200 and r1.left != 175 and r1.right != 225

r2 = Rect(100, 250, 50, 50, align='center')
assert r2.centerX == 100
assert r2.centerY == 250

s = Star(300, 100, 50, 4)
assert s.left == 250
assert s.centerX == 300
s.rotateAngle = 72
assert s.centerX == 300
assert s.centerY == 100

p = Polygon(100, 150, 200, 250, 100, 350, 0, 250, fill='red')
assert p.centerX == 100
assert p.centerY == 250
p.centerX += 50
assert p.centerX == 150
p.pointList = [[100, 150], [200, 250], [250, 225], [0, 250]]
assert p.centerX != 100 and p.left == 00 and p.right == 250
assert p.centerY != 250 and p.top == 150 and p.bottom == 250

l = Label('test label 0', 200, 40, size=18)
assert l.centerX == 200
assert l.centerY == 40
l.value = 'changing test label'
assert l.centerX == 200
assert l.centerY == 40

line = Line(150, 250, 300, 400, arrowEnd=True)
assert line.centerX == 225
assert line.centerY == 325
l.arrowEnd = False
assert line.centerX == 225
assert line.centerY == 325

a = Arc(350, 350, 50, 100, 45, 90)
assert a.centerX == 350
assert a.centerY == 350
a.rotateAngle = 45
assert a.centerX == 350
assert a.centerY == 350

g = Group()
assert g.centerX == 0
r1.rotateAngle = 0
g.add(r1)
assert g.centerX == r1.centerX
g.add(r2)
assert g.centerX == 150
g.centerX += 100
assert g.centerX == 250
assert r1.centerX == 300
assert r2.centerX == 200

g.remove(r1)
assert r1.centerX == 300 and r1.visible == False
assert g.centerX == r2.centerX
