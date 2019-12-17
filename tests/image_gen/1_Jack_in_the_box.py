app.background = gradient('darkSlateBlue', 'fuchsia')

crank = Line(85, 270, 85, 225, fill='grey', lineWidth=6)
Circle(85, 270, 5, fill='grey')
handle = Rect(85, 225, 50, 20, fill='red', align='right')

# box
Polygon(155, 230, 105, 180, 235, 180, 285, 230, fill='mediumSpringGreen',
        border='black')
Line(235, 180, 235, 230)
Polygon(155, 230, 155, 360, 105, 310, 105, 180, fill='mediumSpringGreen',
        border='black')
Rect(155, 230, 130, 130, fill='lightGreen', border='black')
Star(220, 300, 50, 5, fill='red')
Line(125, 260, 125, 280, fill='tan', lineWidth=5)
Line(125, 270, 85, 270, fill='grey', lineWidth=10)

lid = Polygon(155, 230, 105, 180, 235, 180, 285, 230, fill='springGreen',
              border='black')

jack = Group(
    # body
    Oval(185, 175, 50, 140, fill='dodgerBlue', rotateAngle=-20),
    Rect(160, 233, 120, 15, fill='lightGreen'),

    # head and hat
    Circle(160, 95, 50, fill='navajoWhite'),
    Polygon(105, 90, 200, 60, 205, 65, 105, 95, fill='gold'),
    Polygon(105, 90, 130, 15, 200, 60, fill='red'),
    Circle(130, 15, 10, fill='gold'),

    # mouth
    Oval(165, 118, 60, 40, rotateAngle=-10),
    Oval(160, 112, 60, 30, fill='navajoWhite', rotateAngle=-15),
    Oval(180, 130, 25, 15, fill='crimson', rotateAngle=-10),

    # eyes
    Circle(140, 95, 8, fill='white'),
    Circle(140, 95, 4),
    Circle(175, 85, 10, fill='white'),
    Circle(175, 85, 5),

    # nose
    Circle(160, 105, 10, fill='red'),
    )
jack.visible = False

# Cover the bottom of Jack so it looks like he's inside the box.
Line(155, 230, 285, 230, lineWidth=5)

def onMousePress(mouseX, mouseY):
    # If the mouse presses the handle, pull the handle down, open the box,
    # and show Jack.
    if (handle.contains(mouseX, mouseY) == True):
        jack.visible = True
        lid.centerX += 130
        crank.centerY += 45
        handle.centerY += 90

def onMouseRelease(mouseX, mouseY):
    # If Jack is visible, push the handle up, close the box, and hide Jack.
    if (jack.visible == True):
        jack.visible = False
        lid.centerX -= 130
        crank.centerY -= 45
        handle.centerY -= 90

onMousePress(70, 230)


# -
app.background = gradient('darkSlateBlue', 'fuchsia')

crank = Line(85, 270, 85, 225, fill='grey', lineWidth=6)
Circle(85, 270, 5, fill='grey')
handle = Rect(85, 225, 50, 20, fill='red', align='right')

# box
Polygon(155, 230, 105, 180, 235, 180, 285, 230, fill='mediumSpringGreen',
        border='black')
Line(235, 180, 235, 230)
Polygon(155, 230, 155, 360, 105, 310, 105, 180, fill='mediumSpringGreen',
        border='black')
Rect(155, 230, 130, 130, fill='lightGreen', border='black')
Star(220, 300, 50, 5, fill='red')
Line(125, 260, 125, 280, fill='tan', lineWidth=5)
Line(125, 270, 85, 270, fill='grey', lineWidth=10)

lid = Polygon(155, 230, 105, 180, 235, 180, 285, 230, fill='springGreen',
              border='black')

jack = Group(
    # body
    Oval(185, 175, 50, 140, fill='dodgerBlue', rotateAngle=-20),
    Rect(160, 233, 120, 15, fill='lightGreen'),

    # head and hat
    Circle(160, 95, 50, fill='navajoWhite'),
    Polygon(105, 90, 200, 60, 205, 65, 105, 95, fill='gold'),
    Polygon(105, 90, 130, 15, 200, 60, fill='red'),
    Circle(130, 15, 10, fill='gold'),

    # mouth
    Oval(165, 118, 60, 40, rotateAngle=-10),
    Oval(160, 112, 60, 30, fill='navajoWhite', rotateAngle=-15),
    Oval(180, 130, 25, 15, fill='crimson', rotateAngle=-10),

    # eyes
    Circle(140, 95, 8, fill='white'),
    Circle(140, 95, 4),
    Circle(175, 85, 10, fill='white'),
    Circle(175, 85, 5),

    # nose
    Circle(160, 105, 10, fill='red'),
    )
jack.visible = False

# Cover the bottom of Jack so it looks like he's inside the box.
Line(155, 230, 285, 230, lineWidth=5)

def onMousePress(mouseX, mouseY):
    # If the mouse presses the handle, pull the handle down, open the box,
    # and show Jack.
    if (handle.contains(mouseX, mouseY) == True):
        jack.visible = True
        lid.centerX += 130
        crank.centerY += 45
        handle.centerY += 90

def onMouseRelease(mouseX, mouseY):
    # If Jack is visible, push the handle up, close the box, and hide Jack.
    if (jack.visible == True):
        jack.visible = False
        lid.centerX -= 130
        crank.centerY -= 45
        handle.centerY -= 90



# -
app.background = gradient('darkSlateBlue', 'fuchsia')

crank = Line(85, 270, 85, 225, fill='grey', lineWidth=6)
Circle(85, 270, 5, fill='grey')
handle = Rect(85, 225, 50, 20, fill='red', align='right')

# box
Polygon(155, 230, 105, 180, 235, 180, 285, 230, fill='mediumSpringGreen',
        border='black')
Line(235, 180, 235, 230)
Polygon(155, 230, 155, 360, 105, 310, 105, 180, fill='mediumSpringGreen',
        border='black')
Rect(155, 230, 130, 130, fill='lightGreen', border='black')
Star(220, 300, 50, 5, fill='red')
Line(125, 260, 125, 280, fill='tan', lineWidth=5)
Line(125, 270, 85, 270, fill='grey', lineWidth=10)

lid = Polygon(155, 230, 105, 180, 235, 180, 285, 230, fill='springGreen',
              border='black')

jack = Group(
    # body
    Oval(185, 175, 50, 140, fill='dodgerBlue', rotateAngle=-20),
    Rect(160, 233, 120, 15, fill='lightGreen'),

    # head and hat
    Circle(160, 95, 50, fill='navajoWhite'),
    Polygon(105, 90, 200, 60, 205, 65, 105, 95, fill='gold'),
    Polygon(105, 90, 130, 15, 200, 60, fill='red'),
    Circle(130, 15, 10, fill='gold'),

    # mouth
    Oval(165, 118, 60, 40, rotateAngle=-10),
    Oval(160, 112, 60, 30, fill='navajoWhite', rotateAngle=-15),
    Oval(180, 130, 25, 15, fill='crimson', rotateAngle=-10),

    # eyes
    Circle(140, 95, 8, fill='white'),
    Circle(140, 95, 4),
    Circle(175, 85, 10, fill='white'),
    Circle(175, 85, 5),

    # nose
    Circle(160, 105, 10, fill='red'),
    )
jack.visible = False

# Cover the bottom of Jack so it looks like he's inside the box.
Line(155, 230, 285, 230, lineWidth=5)

def onMousePress(mouseX, mouseY):
    # If the mouse presses the handle, pull the handle down, open the box,
    # and show Jack.
    if (handle.contains(mouseX, mouseY) == True):
        jack.visible = True
        lid.centerX += 130
        crank.centerY += 45
        handle.centerY += 90

def onMouseRelease(mouseX, mouseY):
    # If Jack is visible, push the handle up, close the box, and hide Jack.
    if (jack.visible == True):
        jack.visible = False
        lid.centerX -= 130
        crank.centerY -= 45
        handle.centerY -= 90

onMousePress(70, 230)
onMouseRelease(70, 230)

