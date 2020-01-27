r = Rect(100, 100, 50, 50)
assert r.width == 50 and r.height == 50
assert r.fill == 'black' and r.border == None and r.borderWidth == 2
assert r.rotateAngle == 0 and r.opacity == 100 and r.dashes == False
errorMsg = ''
try:
    assert r.align == 'left-top'
except Exception as e:
    errorMsg = str(e)
if (errorMsg != "You can't get or set the align property"):
    assert False

s = Star(200, 200, 25, 5)
assert s.points == 5 and rounded(s.roundness) == 38
s.points = 7
assert rounded(s.roundness) != 38

p = Polygon()
assert p.fill == 'black' and p.pointList == []
assert p.width == 0 and p.height == 0 and p.centerX == 0 and p.centerY == 0

line = Line(250, 250, 300, 350)
assert rounded(line.lineWidth) == 2
assert line.dashes == False and line.arrowStart == False and line.arrowEnd == False
assert line.border == None and line.borderWidth == 0

label = Label('', 200, 200)
assert label.value == '' and label.size == 12 and label.font == 'arial'
assert label.bold == False and label.italic == False

g = Group()
assert g.width == 0 and g.height == 0
g.add(r)
assert g.width == r.width and g.height == r.height
assert g.fill == 'black' and g.opacity == 100
g.add(s)
s.fill = 'red'

errorMsg = ''
try:
    assert g.fill == 'black'
except Exception as e:
    errorMsg = str(e)
if (errorMsg != "Group.fill has no value because its children don't all have the same value for fill"):
    assert False
