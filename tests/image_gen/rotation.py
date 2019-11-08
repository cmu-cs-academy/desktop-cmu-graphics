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







Rect(390, 390, 10, 10, fill='green')
