# background
Rect(0, 0, 400, 400, fill=gradient('white', 'navy'))

# Draw the perspective lines next.
Line(100, 0, 100, 250)
Line(300, 0, 300, 250)
Line(100, 250, 0, 400)
Line(300, 250, 400, 400)
Line(100, 250, 300, 250)

# Draw the ninja here.
# face and mask
Circle(200, 200, 70, fill=gradient('lightBlue', 'royalBlue'))
Oval(200, 195, 140, 50)
Polygon(270, 195, 280, 180, 290, 190)

# ninja eyebrows
Line(190, 170, 160, 165, lineWidth=3)
Line(210, 170, 240, 165, lineWidth=3)

# ninja eyes and pupils
Oval(175, 195, 30, 40, fill='white')
Oval(225, 195, 30, 40, fill='white')
Circle(178, 195, 10)
Circle(222, 195, 10)

# shadow
Oval(200, 315, 100, 30)

# This test case is intentionally left blank.

