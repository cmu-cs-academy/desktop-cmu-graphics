# background
app.background = gradient('moccasin', 'papayaWhip', start='top')
Polygon(200, 400, 360, 340, 450, 400,
        fill=gradient('gold', 'goldenrod', start='top'))
Polygon(-100, 400, 40, 300, 300, 400,
        fill=gradient('orange', 'tomato', start='top'))

# rotating piece
rotatingSpikes = Star(200, 200, 150, 20, fill=gradient('red', 'blue'),
                      roundness=15)

# back leg
Line(175, 400, 200, 200, fill='white', lineWidth=8)

# inner rings
Circle(200, 200, 100, fill=None, border='yellow', borderWidth=10, opacity=70)
Circle(200, 200, 75, fill=None, border='blue', borderWidth=10, opacity=70)
Circle(200, 200, 50, fill=None, border='red', borderWidth=10, opacity=70)
Circle(200, 200, 25, fill=None, border='purple', borderWidth=10, opacity=70)

# outer ring
Circle(200, 200, 150, fill=None, borderWidth=10, opacity=70,
       border=gradient('blue', 'red', 'green', 'yellow', start='top'))
Circle(200, 200, 146, fill=None, border='white')
Circle(200, 200, 154, fill=None, border='white')

# front leg
Line(225, 400, 200, 200, fill='white', lineWidth=8)

def onMouseMove(mouseX, mouseY):
    rotatingSpikes.rotateAngle += 1

# This test case is intentionally left blank.

