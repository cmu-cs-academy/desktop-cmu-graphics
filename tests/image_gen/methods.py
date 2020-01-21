# general shape methods
r1 = Rect(110, 110, 50, 50)
assert r1.contains(110, 110)
assert r1.hits(110, 110)
r1.visible = False
assert r1.contains(110, 110)
assert r1.hits(110, 110)
r1.visible = True
r1.opacity = 0
assert r1.contains(110, 110)
assert r1.hits(110, 110)
r1.opacity = 100

r2 = Rect(150, 150, 50, 50, fill=None, border='black', borderWidth=15)
assert r2.contains(152, 152)
assert r2.hits(152, 152)
assert r2.contains(175, 175)
assert not r2.hits(175, 175)
assert not r2.containsShape(r1)
assert r2.hitsShape(r1)

r3 = Rect(150, 150, 5, 5)
assert r2.containsShape(r3)
assert r2.hitsShape(r3)
assert not r3.containsShape(r2)
assert r3.hitsShape(r2)
r3.centerX = 175
r3.centerY = 175
assert r2.containsShape(r3)
assert not r2.hitsShape(r3)
assert not r3.containsShape(r2)
assert not r3.hitsShape(r2)

p = Polygon(200, 200, 300, 200, 200, 300)
p.addPoint(300, 300)
assert p.pointList == [[200, 200], [300, 200], [200, 300], [300, 300]]

# group methods
g = Group()
g.add(p)
assert g.children == [p]
g.remove(p)
assert g.children == []
assert p.visible == False
p.visible = True
assert g.children == [p]
g.clear()
assert g.children == []
assert p.visible == False
p.visible = True
assert g.children == [p]
g.remove(p)
g.add(p)
assert p.visible == True
assert g.children == [p]
assert g.hitTest(100, 100) == None
assert g.hitTest(250, 215) == p
g.centerX -= 10
g.centerY -= 10
assert g.hitsShape(r2)
assert not g.containsShape(r2)

# groups containing other groups
h = Group(r1, g)
assert h.children == [r1, g]
assert h.children != [r1, p]
h.remove(g)
assert g.visible == False
assert p.visible == False
p.visible = True
assert g.children == []
g.visible = True
assert g.children == []
