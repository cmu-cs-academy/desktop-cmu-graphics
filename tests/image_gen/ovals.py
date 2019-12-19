CENTER_X = 200
CENTER_Y = 200

o = Oval(CENTER_X, CENTER_Y, 200, 300, rotateAngle=10, fill='pink', db='bbox')

def resize(w, h):
    o.width = w
    assert o.width == w, o.width
    assert o.centerX == CENTER_X, o.centerX
    o.height = h
    assert o.height == h, o.height
    assert o.centerY == CENTER_Y, o.centerY

# -
CENTER_X = 200
CENTER_Y = 200

o = Oval(CENTER_X, CENTER_Y, 200, 300, rotateAngle=10, fill='pink', db='bbox')

def resize(w, h):
    o.width = w
    assert o.width == w, o.width
    assert o.centerX == CENTER_X, o.centerX
    o.height = h
    assert o.height == h, o.height
    assert o.centerY == CENTER_Y, o.centerY
resize(100, 100)
# -
CENTER_X = 200
CENTER_Y = 200

o = Oval(CENTER_X, CENTER_Y, 200, 300, rotateAngle=10, fill='pink', db='bbox')

def resize(w, h):
    o.width = w
    assert o.width == w, o.width
    assert o.centerX == CENTER_X, o.centerX
    o.height = h
    assert o.height == h, o.height
    assert o.centerY == CENTER_Y, o.centerY
resize(50, 200)
# -
CENTER_X = 200
CENTER_Y = 200

o = Oval(CENTER_X, CENTER_Y, 200, 300, rotateAngle=10, fill='pink', db='bbox')

def resize(w, h):
    o.width = w
    assert o.width == w, o.width
    assert o.centerX == CENTER_X, o.centerX
    o.height = h
    assert o.height == h, o.height
    assert o.centerY == CENTER_Y, o.centerY
resize(200, 50)


# -
o = Oval(300, 300, 200, 100, db='bbox')

while o.width > 10e-12:
    o.width /= 2
    assert o.height == 100
    assert o.width > 0
    assert o.rotateAngle == 0 or o.rotateAngle == 90, o.rotateAngle

o = Oval(300, 300, 200, 100, db='bbox')

while o.height > 10e-12:
    o.height /= 2
    assert o.width == 200
    assert o.height > 0
    assert o.rotateAngle == 0 or o.rotateAngle == 90, o.rotateAngle



#-
c2 = Oval(200, 200, 100, 20, fill=None, border='black')

def jiggle(width, height):
    c2.width = width
    assert c2.width == width, c2.width
    c2.height = height
    assert c2.height == height, c2.height
    c2.rotateAngle += 1
    c2.centerX = 200
    c2.centerY = 200
    assert c2.centerX == 200, c2.centerX
    assert c2.centerY == 200, c2.centerY

for _ in range(400):
    jiggle(200, 100)

Circle(100, 100, 30, fill='red', border='blue')
Oval(200, 100, 30, 60, fill='red', border='blue')

Oval(50, 350, 100, 150, fill=gradient('red', 'white', 'white', 'red'))
Circle(150, 350, 45, fill=gradient('red', 'white', 'white', 'red'))
