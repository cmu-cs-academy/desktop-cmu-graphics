app.background = 'black'

# maze
Rect(5, 20, 390, 6, fill=None, border='royalBlue')
Rect(5, 380, 390, 6, fill=None, border='royalBlue')
Rect(5, 100, 155, 6, fill=None, border='royalBlue')
Rect(240, 100, 155, 6, fill=None, border='royalBlue')
Rect(154, 108, 6, 50, fill=None, border='royalBlue')
Rect(240, 108, 6, 50, fill=None, border='royalBlue')
Rect(5, 160, 155, 6, fill=None, border='royalBlue')
Rect(240, 160, 155, 6, fill=None, border='royalBlue')
Rect(5, 240, 35, 6, fill=None, border='royalBlue')
Rect(120, 240, 275, 6, fill=None, border='royalBlue')
Rect(34, 248, 6, 50, fill=None, border='royalBlue')
Rect(120, 248, 6, 50, fill=None, border='royalBlue')
Rect(5, 300, 35, 6, fill=None, border='royalBlue')
Rect(120, 300, 275, 6, fill=None, border='royalBlue')
Rect(240, 308, 6, 70, fill=None, border='royalBlue')

path = Group(
    Line(-30, 63, 430, 63, fill='royalBlue', opacity=70),
    Line(200, 63, 200, 200, fill='royalBlue', opacity=70),
    Line(-30, 200, 430, 200, fill='royalBlue', opacity=70),
    Line(80, 200, 80, 343, fill='royalBlue', opacity=70),
    Line(-30, 343, 215, 343, fill='royalBlue', opacity=70),
    Line(270, 343, 430, 343, fill='royalBlue', opacity=70),
    )

def drawDots(y):
    for x in range(20, 400, 60):
        # If the dot is placed on a path, draws it.
        line = path.hitTest(x, y)
        if (line != None):
            dots.add(
                Circle(x, y, 5, fill='lightSalmon')
                )

# small dots
dots = Group()
drawDots(63)
drawDots(134)
drawDots(200)
drawDots(273)
drawDots(343)
powerDot = Circle(270, 343, 10, fill='lightSalmon')

# ghost
pinky = Group(
    Circle(350, 200, 25, fill='magenta'),
    Rect(325, 200, 50, 25, fill='magenta'),
    Circle(331, 225, 6, fill='magenta'),
    Circle(344, 225, 6, fill='magenta'),
    Circle(356, 225, 6, fill='magenta'),
    Circle(369, 225, 6, fill='magenta'),
    Circle(335, 190, 6, fill='white'),
    Circle(355, 190, 6, fill='white'),
    Circle(333, 190, 3, fill='royalBlue'),
    Circle(353, 190, 3, fill='royalBlue')
    )
pinky.dx = 2
pinky.color = 'magenta'

pacman = Arc(100, 200, 50, 50, 120, 300, fill='yellow')
pacman.dx = 2
pacman.dy = 0
pacman.dS = 10

def movePacman():
    # Changes pacman's start and sweep angles to open and close its mouth.
    pacman.startAngle -= pacman.dS // 2
    pacman.sweepAngle += pacman.dS
    if (pacman.sweepAngle <= 300):
        pacman.dS *= -1
    elif (pacman.sweepAngle >= 360):
        pacman.dS *= -1

    # Check to see if the next location pacman will move to is on the path.
    # If it is, move pacman to that spot.
    newX = pacman.centerX + pacman.dx
    newY = pacman.centerY + pacman.dy
    if (path.hitTest(newX, newY) != None):
        pacman.centerX = newX
        pacman.centerY = newY
    # Wraparound.
    if (pacman.left > 400):
        pacman.right = 0
    elif (pacman.right < 0):
        pacman.left = 400

def onKeyHold(keys):
    # Checks whether moving two pixels in each direction will be on the path.
    lineLeft = path.hitTest(pacman.centerX - 2, pacman.centerY)
    lineRight = path.hitTest(pacman.centerX + 2, pacman.centerY)
    lineUp = path.hitTest(pacman.centerX, pacman.centerY - 2)
    lineDown = path.hitTest(pacman.centerX, pacman.centerY + 2)

    # Changes direction with the arrow keys.
    if (('left' in keys) and (lineLeft != None)):
        pacman.dx = -2
        pacman.dy = 0
        pacman.rotateAngle = 180
    elif (('right' in keys) and (lineRight != None)):
        pacman.dx = 2
        pacman.dy = 0
        pacman.rotateAngle = 0
    elif (('up' in keys) and (lineUp != None)):
        pacman.dx = 0
        pacman.dy = -2
        pacman.rotateAngle = 270
    elif (('down' in keys) and (lineDown != None)):
        pacman.dx = 0
        pacman.dy = 2
        pacman.rotateAngle = 90

def onStep():
    # Moves pacman.
    movePacman()

    # Check to see if pacman is hitting a dot and if so, remove it.
    dot = dots.hitTest(pacman.centerX, pacman.centerY)
    if (dot != None):
        dots.remove(dot)
    # Otherwise, check if pacman is hitting the powerDot and set it to invisible.
    # Then, change the ghost color.
    if (pacman.hitsShape(powerDot) == True):
        powerDot.visible = False
        pinky.fill = 'royalBlue'
        pinky.color = 'royalBlue'
    # Moves the ghost with bouncing.
    pinky.centerX += pinky.dx
    if ((pinky.centerX <= 25) or (pinky.centerX >= 375)):
        pinky.dx *= -1

    # If pacman hits the ghost when it is pink, the player loses.
    # Otherwise, the ghost's body disappears.
    if (pacman.hitsShape(pinky) == True):
        if (pinky.color == 'royalBlue'):
            pinky.visible = False
        else:
            Label('Ooops!', 265, 273, fill='white', size=24)
            app.stop()

    # Checks if the player won.
    if ((len(dots.children) == 0) and (pinky.visible == False)):
        Label('You Won!', 265, 273, fill='white', size=24)
        app.stop()

pacman.centerX = 300
pacman.centerY = 343
onKeyHold(['left'])
onSteps(20)
app.paused = True


# -
app.background = 'black'

# maze
Rect(5, 20, 390, 6, fill=None, border='royalBlue')
Rect(5, 380, 390, 6, fill=None, border='royalBlue')
Rect(5, 100, 155, 6, fill=None, border='royalBlue')
Rect(240, 100, 155, 6, fill=None, border='royalBlue')
Rect(154, 108, 6, 50, fill=None, border='royalBlue')
Rect(240, 108, 6, 50, fill=None, border='royalBlue')
Rect(5, 160, 155, 6, fill=None, border='royalBlue')
Rect(240, 160, 155, 6, fill=None, border='royalBlue')
Rect(5, 240, 35, 6, fill=None, border='royalBlue')
Rect(120, 240, 275, 6, fill=None, border='royalBlue')
Rect(34, 248, 6, 50, fill=None, border='royalBlue')
Rect(120, 248, 6, 50, fill=None, border='royalBlue')
Rect(5, 300, 35, 6, fill=None, border='royalBlue')
Rect(120, 300, 275, 6, fill=None, border='royalBlue')
Rect(240, 308, 6, 70, fill=None, border='royalBlue')

path = Group(
    Line(-30, 63, 430, 63, fill='royalBlue', opacity=70),
    Line(200, 63, 200, 200, fill='royalBlue', opacity=70),
    Line(-30, 200, 430, 200, fill='royalBlue', opacity=70),
    Line(80, 200, 80, 343, fill='royalBlue', opacity=70),
    Line(-30, 343, 215, 343, fill='royalBlue', opacity=70),
    Line(270, 343, 430, 343, fill='royalBlue', opacity=70),
    )

def drawDots(y):
    for x in range(20, 400, 60):
        # If the dot is placed on a path, draws it.
        line = path.hitTest(x, y)
        if (line != None):
            dots.add(
                Circle(x, y, 5, fill='lightSalmon')
                )

# small dots
dots = Group()
drawDots(63)
drawDots(134)
drawDots(200)
drawDots(273)
drawDots(343)
powerDot = Circle(270, 343, 10, fill='lightSalmon')

# ghost
pinky = Group(
    Circle(350, 200, 25, fill='magenta'),
    Rect(325, 200, 50, 25, fill='magenta'),
    Circle(331, 225, 6, fill='magenta'),
    Circle(344, 225, 6, fill='magenta'),
    Circle(356, 225, 6, fill='magenta'),
    Circle(369, 225, 6, fill='magenta'),
    Circle(335, 190, 6, fill='white'),
    Circle(355, 190, 6, fill='white'),
    Circle(333, 190, 3, fill='royalBlue'),
    Circle(353, 190, 3, fill='royalBlue')
    )
pinky.dx = 2
pinky.color = 'magenta'

pacman = Arc(100, 200, 50, 50, 120, 300, fill='yellow')
pacman.dx = 2
pacman.dy = 0
pacman.dS = 10

def movePacman():
    # Changes pacman's start and sweep angles to open and close its mouth.
    pacman.startAngle -= pacman.dS // 2
    pacman.sweepAngle += pacman.dS
    if (pacman.sweepAngle <= 300):
        pacman.dS *= -1
    elif (pacman.sweepAngle >= 360):
        pacman.dS *= -1

    # Check to see if the next location pacman will move to is on the path.
    # If it is, move pacman to that spot.
    newX = pacman.centerX + pacman.dx
    newY = pacman.centerY + pacman.dy
    if (path.hitTest(newX, newY) != None):
        pacman.centerX = newX
        pacman.centerY = newY
    # Wraparound.
    if (pacman.left > 400):
        pacman.right = 0
    elif (pacman.right < 0):
        pacman.left = 400

def onKeyHold(keys):
    # Checks whether moving two pixels in each direction will be on the path.
    lineLeft = path.hitTest(pacman.centerX - 2, pacman.centerY)
    lineRight = path.hitTest(pacman.centerX + 2, pacman.centerY)
    lineUp = path.hitTest(pacman.centerX, pacman.centerY - 2)
    lineDown = path.hitTest(pacman.centerX, pacman.centerY + 2)

    # Changes direction with the arrow keys.
    if (('left' in keys) and (lineLeft != None)):
        pacman.dx = -2
        pacman.dy = 0
        pacman.rotateAngle = 180
    elif (('right' in keys) and (lineRight != None)):
        pacman.dx = 2
        pacman.dy = 0
        pacman.rotateAngle = 0
    elif (('up' in keys) and (lineUp != None)):
        pacman.dx = 0
        pacman.dy = -2
        pacman.rotateAngle = 270
    elif (('down' in keys) and (lineDown != None)):
        pacman.dx = 0
        pacman.dy = 2
        pacman.rotateAngle = 90

def onStep():
    # Moves pacman.
    movePacman()

    # Check to see if pacman is hitting a dot and if so, remove it.
    dot = dots.hitTest(pacman.centerX, pacman.centerY)
    if (dot != None):
        dots.remove(dot)
    # Otherwise, check if pacman is hitting the powerDot and set it to invisible.
    # Then, change the ghost color.
    if (pacman.hitsShape(powerDot) == True):
        powerDot.visible = False
        pinky.fill = 'royalBlue'
        pinky.color = 'royalBlue'
    # Moves the ghost with bouncing.
    pinky.centerX += pinky.dx
    if ((pinky.centerX <= 25) or (pinky.centerX >= 375)):
        pinky.dx *= -1

    # If pacman hits the ghost when it is pink, the player loses.
    # Otherwise, the ghost's body disappears.
    if (pacman.hitsShape(pinky) == True):
        if (pinky.color == 'royalBlue'):
            pinky.visible = False
        else:
            Label('Ooops!', 265, 273, fill='white', size=24)
            app.stop()

    # Checks if the player won.
    if ((len(dots.children) == 0) and (pinky.visible == False)):
        Label('You Won!', 265, 273, fill='white', size=24)
        app.stop()

onSteps(40)
app.paused = True


# -
app.background = 'black'

# maze
Rect(5, 20, 390, 6, fill=None, border='royalBlue')
Rect(5, 380, 390, 6, fill=None, border='royalBlue')
Rect(5, 100, 155, 6, fill=None, border='royalBlue')
Rect(240, 100, 155, 6, fill=None, border='royalBlue')
Rect(154, 108, 6, 50, fill=None, border='royalBlue')
Rect(240, 108, 6, 50, fill=None, border='royalBlue')
Rect(5, 160, 155, 6, fill=None, border='royalBlue')
Rect(240, 160, 155, 6, fill=None, border='royalBlue')
Rect(5, 240, 35, 6, fill=None, border='royalBlue')
Rect(120, 240, 275, 6, fill=None, border='royalBlue')
Rect(34, 248, 6, 50, fill=None, border='royalBlue')
Rect(120, 248, 6, 50, fill=None, border='royalBlue')
Rect(5, 300, 35, 6, fill=None, border='royalBlue')
Rect(120, 300, 275, 6, fill=None, border='royalBlue')
Rect(240, 308, 6, 70, fill=None, border='royalBlue')

path = Group(
    Line(-30, 63, 430, 63, fill='royalBlue', opacity=70),
    Line(200, 63, 200, 200, fill='royalBlue', opacity=70),
    Line(-30, 200, 430, 200, fill='royalBlue', opacity=70),
    Line(80, 200, 80, 343, fill='royalBlue', opacity=70),
    Line(-30, 343, 215, 343, fill='royalBlue', opacity=70),
    Line(270, 343, 430, 343, fill='royalBlue', opacity=70),
    )

def drawDots(y):
    for x in range(20, 400, 60):
        # If the dot is placed on a path, draws it.
        line = path.hitTest(x, y)
        if (line != None):
            dots.add(
                Circle(x, y, 5, fill='lightSalmon')
                )

# small dots
dots = Group()
drawDots(63)
drawDots(134)
drawDots(200)
drawDots(273)
drawDots(343)
powerDot = Circle(270, 343, 10, fill='lightSalmon')

# ghost
pinky = Group(
    Circle(350, 200, 25, fill='magenta'),
    Rect(325, 200, 50, 25, fill='magenta'),
    Circle(331, 225, 6, fill='magenta'),
    Circle(344, 225, 6, fill='magenta'),
    Circle(356, 225, 6, fill='magenta'),
    Circle(369, 225, 6, fill='magenta'),
    Circle(335, 190, 6, fill='white'),
    Circle(355, 190, 6, fill='white'),
    Circle(333, 190, 3, fill='royalBlue'),
    Circle(353, 190, 3, fill='royalBlue')
    )
pinky.dx = 2
pinky.color = 'magenta'

pacman = Arc(100, 200, 50, 50, 120, 300, fill='yellow')
pacman.dx = 2
pacman.dy = 0
pacman.dS = 10

def movePacman():
    # Changes pacman's start and sweep angles to open and close its mouth.
    pacman.startAngle -= pacman.dS // 2
    pacman.sweepAngle += pacman.dS
    if (pacman.sweepAngle <= 300):
        pacman.dS *= -1
    elif (pacman.sweepAngle >= 360):
        pacman.dS *= -1

    # Check to see if the next location pacman will move to is on the path.
    # If it is, move pacman to that spot.
    newX = pacman.centerX + pacman.dx
    newY = pacman.centerY + pacman.dy
    if (path.hitTest(newX, newY) != None):
        pacman.centerX = newX
        pacman.centerY = newY
    # Wraparound.
    if (pacman.left > 400):
        pacman.right = 0
    elif (pacman.right < 0):
        pacman.left = 400

def onKeyHold(keys):
    # Checks whether moving two pixels in each direction will be on the path.
    lineLeft = path.hitTest(pacman.centerX - 2, pacman.centerY)
    lineRight = path.hitTest(pacman.centerX + 2, pacman.centerY)
    lineUp = path.hitTest(pacman.centerX, pacman.centerY - 2)
    lineDown = path.hitTest(pacman.centerX, pacman.centerY + 2)

    # Changes direction with the arrow keys.
    if (('left' in keys) and (lineLeft != None)):
        pacman.dx = -2
        pacman.dy = 0
        pacman.rotateAngle = 180
    elif (('right' in keys) and (lineRight != None)):
        pacman.dx = 2
        pacman.dy = 0
        pacman.rotateAngle = 0
    elif (('up' in keys) and (lineUp != None)):
        pacman.dx = 0
        pacman.dy = -2
        pacman.rotateAngle = 270
    elif (('down' in keys) and (lineDown != None)):
        pacman.dx = 0
        pacman.dy = 2
        pacman.rotateAngle = 90

def onStep():
    # Moves pacman.
    movePacman()

    # Check to see if pacman is hitting a dot and if so, remove it.
    dot = dots.hitTest(pacman.centerX, pacman.centerY)
    if (dot != None):
        dots.remove(dot)
    # Otherwise, check if pacman is hitting the powerDot and set it to invisible.
    # Then, change the ghost color.
    if (pacman.hitsShape(powerDot) == True):
        powerDot.visible = False
        pinky.fill = 'royalBlue'
        pinky.color = 'royalBlue'
    # Moves the ghost with bouncing.
    pinky.centerX += pinky.dx
    if ((pinky.centerX <= 25) or (pinky.centerX >= 375)):
        pinky.dx *= -1

    # If pacman hits the ghost when it is pink, the player loses.
    # Otherwise, the ghost's body disappears.
    if (pacman.hitsShape(pinky) == True):
        if (pinky.color == 'royalBlue'):
            pinky.visible = False
        else:
            Label('Ooops!', 265, 273, fill='white', size=24)
            app.stop()

    # Checks if the player won.
    if ((len(dots.children) == 0) and (pinky.visible == False)):
        Label('You Won!', 265, 273, fill='white', size=24)
        app.stop()

onSteps(64)
app.paused = True

