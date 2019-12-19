app.background = gradient('lightSkyBlue', 'deepSkyBlue', start='top')

# clouds
Circle(33, 60, 20, fill='white', border='gainsboro')
Circle(50, 40, 20, fill='white', border='gainsboro')
Circle(67, 60, 30, fill='white', border='gainsboro')
Rect(30, 45, 50, 30, fill='white')
Circle(183, 100, 30, fill='white', border='gainsboro')
Circle(200, 80, 20, fill='white', border='gainsboro')
Circle(217, 100, 30, fill='white', border='gainsboro')
Rect(180, 75, 40, 40, fill='white')
Circle(333, 300, 20, fill='white', border='gainsboro')
Circle(350, 280, 30, fill='white', border='gainsboro')
Circle(367, 300, 30, fill='white', border='gainsboro')
Rect(325, 270, 50, 40, fill='white')

# bird body
Polygon(145, 215, 110, 210, 145, 225, fill='salmon')
Polygon(145, 220, 110, 215, 145, 230, fill='salmon')
Line(170, 245, 160, 255, fill='gold', lineWidth=3)
Line(170, 245, 165, 260, fill='gold', lineWidth=3)
Oval(190, 250, 100, 65, fill='crimson', align='bottom')
Oval(190, 250, 80, 40, fill='salmon', align='bottom')
Circle(220, 200, 12, border='white', borderWidth=7)
Polygon(235, 210, 235, 215, 270, 210, fill='gold')
Polygon(235, 215, 270, 210, 235, 220, fill='goldenrod')

# bird wings
upWing = Polygon(170, 220, 185, 210, 130, 170, fill='lightSalmon')
downWing = Polygon(160, 220, 185, 210, 150, 255, fill='lightSalmon')
downWing.visible = False

def onKeyPress(key):
    # If spacebar is pressed, hide the upwards wing and show the downwards one.
    if (key == 'space'):
        upWing.visible = False
        downWing.visible = True
def onKeyRelease(key):
    # If spacebar is released, do the opposite of when it is pressed.
    if (key == 'space'):
        downWing.visible = False
        upWing.visible = True

onKeyPress('space')
onKeyPress('space')
onKeyPress('space')
onKeyPress('space')


# -
app.background = gradient('lightSkyBlue', 'deepSkyBlue', start='top')

# clouds
Circle(33, 60, 20, fill='white', border='gainsboro')
Circle(50, 40, 20, fill='white', border='gainsboro')
Circle(67, 60, 30, fill='white', border='gainsboro')
Rect(30, 45, 50, 30, fill='white')
Circle(183, 100, 30, fill='white', border='gainsboro')
Circle(200, 80, 20, fill='white', border='gainsboro')
Circle(217, 100, 30, fill='white', border='gainsboro')
Rect(180, 75, 40, 40, fill='white')
Circle(333, 300, 20, fill='white', border='gainsboro')
Circle(350, 280, 30, fill='white', border='gainsboro')
Circle(367, 300, 30, fill='white', border='gainsboro')
Rect(325, 270, 50, 40, fill='white')

# bird body
Polygon(145, 215, 110, 210, 145, 225, fill='salmon')
Polygon(145, 220, 110, 215, 145, 230, fill='salmon')
Line(170, 245, 160, 255, fill='gold', lineWidth=3)
Line(170, 245, 165, 260, fill='gold', lineWidth=3)
Oval(190, 250, 100, 65, fill='crimson', align='bottom')
Oval(190, 250, 80, 40, fill='salmon', align='bottom')
Circle(220, 200, 12, border='white', borderWidth=7)
Polygon(235, 210, 235, 215, 270, 210, fill='gold')
Polygon(235, 215, 270, 210, 235, 220, fill='goldenrod')

# bird wings
upWing = Polygon(170, 220, 185, 210, 130, 170, fill='lightSalmon')
downWing = Polygon(160, 220, 185, 210, 150, 255, fill='lightSalmon')
downWing.visible = False

def onKeyPress(key):
    # If spacebar is pressed, hide the upwards wing and show the downwards one.
    if (key == 'space'):
        upWing.visible = False
        downWing.visible = True
def onKeyRelease(key):
    # If spacebar is released, do the opposite of when it is pressed.
    if (key == 'space'):
        downWing.visible = False
        upWing.visible = True

onKeyPress('space')
onKeyRelease('space')


# -
app.background = gradient('lightSkyBlue', 'deepSkyBlue', start='top')

# clouds
Circle(33, 60, 20, fill='white', border='gainsboro')
Circle(50, 40, 20, fill='white', border='gainsboro')
Circle(67, 60, 30, fill='white', border='gainsboro')
Rect(30, 45, 50, 30, fill='white')
Circle(183, 100, 30, fill='white', border='gainsboro')
Circle(200, 80, 20, fill='white', border='gainsboro')
Circle(217, 100, 30, fill='white', border='gainsboro')
Rect(180, 75, 40, 40, fill='white')
Circle(333, 300, 20, fill='white', border='gainsboro')
Circle(350, 280, 30, fill='white', border='gainsboro')
Circle(367, 300, 30, fill='white', border='gainsboro')
Rect(325, 270, 50, 40, fill='white')

# bird body
Polygon(145, 215, 110, 210, 145, 225, fill='salmon')
Polygon(145, 220, 110, 215, 145, 230, fill='salmon')
Line(170, 245, 160, 255, fill='gold', lineWidth=3)
Line(170, 245, 165, 260, fill='gold', lineWidth=3)
Oval(190, 250, 100, 65, fill='crimson', align='bottom')
Oval(190, 250, 80, 40, fill='salmon', align='bottom')
Circle(220, 200, 12, border='white', borderWidth=7)
Polygon(235, 210, 235, 215, 270, 210, fill='gold')
Polygon(235, 215, 270, 210, 235, 220, fill='goldenrod')

# bird wings
upWing = Polygon(170, 220, 185, 210, 130, 170, fill='lightSalmon')
downWing = Polygon(160, 220, 185, 210, 150, 255, fill='lightSalmon')
downWing.visible = False

def onKeyPress(key):
    # If spacebar is pressed, hide the upwards wing and show the downwards one.
    if (key == 'space'):
        upWing.visible = False
        downWing.visible = True
def onKeyRelease(key):
    # If spacebar is released, do the opposite of when it is pressed.
    if (key == 'space'):
        downWing.visible = False
        upWing.visible = True

onKeyPress('space')
onKeyRelease('space')
onKeyPress('space')

