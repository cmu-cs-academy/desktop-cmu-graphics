def testShape(s, delta):
    assert s.centerX == 200, s.centerX
    assert s.centerY == 200, s.centerY
    assert s.left < s.centerX, s.left
    assert s.centerX < s.right, s.right

    original_left = s.left
    s.right += delta
    assert rounded(s.left - original_left) == delta, s.left - original_left
    assert s.centerX == 200 + delta, s.centerX

    s.points += 4
    assert s.centerX == 200 + delta, s.centerX


regPoly = RegularPolygon(200, 200, 50, 3, opacity=50)
testShape(regPoly, 10)

star = Star(200, 200, 50, 10, opacity=50)
testShape(star, -10)


def drawStarBounds(s):
    Rect(s.centerX - 50, s.top, 100, 1, fill='red')
    Rect(s.centerX - 50, s.bottom, 100, 1, fill='blue')
    Rect(s.left, s.centerY - 50, 1, 100, fill='green')
    Rect(s.right, s.centerY - 50, 1, 100, fill='yellow')

s = Star(100, 100, 50, 3, rotateAngle=10)
drawStarBounds(s)

s = Star(100, 300, 50, 3)
drawStarBounds(s)
