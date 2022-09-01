r = Circle(100, 100, 50)
o = Oval(100, 100, 100, 30, fill='red')
rp =  RegularPolygon(100, 100, 50, 3, fill='green')

center = Circle(0, 0, 2, fill='blue')

def move():
    for s in [r, rp, o]:
        s.left += 10
        s.top += 10
        s.rotateAngle += 15
    for s in [r, rp, o]:
        assert rounded(s.centerX) == rounded(r.centerX)
        assert rounded(s.centerY) == rounded(r.centerY)
    center.centerX = s.centerX
    center.centerY = s.centerY

# -
move()

# -
move()

# -
move()

# -
for _ in range(15): move()




# -
def testRotate(angles):
    moon = Circle(0, 200, 50, fill=gradient('grey', 'powderBlue', start='left'))

    baseX = moon.centerX
    baseY = moon.centerY
    assert (baseX, baseY) == (0, 200)

    angles = list(angles)
    for angle in angles:
        baseX += 27
        moon.centerX += 27
        baseY += 13
        moon.centerY += 13
        moon.rotateAngle = angle

        assert (moon.left, moon.centerX, moon.right) == (baseX-50, baseX, baseX+50), (
            angle, baseX, (moon.left, moon.centerX, moon.right))
        assert (moon.top, moon.centerY, moon.bottom) == (baseY-50, baseY, baseY+50), (
            angle, baseY, (moon.top, moon.centerY, moon.bottom))
    moon.visible = False
    print(angles, 'passed')


testRotate([0] * 10)
testRotate([90] * 10)
testRotate([180] * 10)
testRotate(x * 90 for x in range(10))
testRotate(x * 450 for x in range(10))
testRotate(x * 360 for x in range(10))


# -
# Test rotating an arc around a center that is not the circle center
a = Arc(200, 200, 150, 150, 90, 180, db='all')
r = Rect(0, 0, 10, 10)
g = Group(a, r)
g.rotateAngle += 45

Rect(390, 390, 10, 10, fill='green')
