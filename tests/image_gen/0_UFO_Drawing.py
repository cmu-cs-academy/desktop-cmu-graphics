app.background = 'black'
app.stepsPerSecond = 20

# background stars
Star(320, 50, 2, 5, fill='white')
Star(230, 115, 3, 5, fill='white')
Star(380, 315, 2, 5, fill='white')
Star(150, 190, 2, 5, fill='white')
Star(285, 290, 3, 5, fill='white')
Star(50, 325, 2, 5, fill='white')
Star(210, 375, 2, 5, fill='white')
Star(10, 25, 2, 5, fill='white')

# moon
Circle(50, 100, 30, fill=gradient('black', 'grey', start='left'))
Circle(40, 80, 3, fill=rgb(50, 50, 50))
Circle(65, 85, 4, fill=rgb(85, 85, 85))
Circle(70, 110, 3, fill=rgb(85, 85, 85))
Circle(40, 115, 4, fill=rgb(45, 45, 45))
Circle(45, 95, 4, fill=rgb(55, 55, 55))
Circle(60, 100, 4, fill=rgb(75, 75, 75))
Circle(30, 95, 3, fill=rgb(15, 15, 15))

app.UFOs = [ ]
app.points = [ ]

def createUFOs(n):
    # trails
    for i in range(n):
        color = rgb(randrange(0, 256), randrange(0, 256), randrange(0, 256))
        trail = Line(8, 10, 10, 10, fill=gradient(color, 'black'), lineWidth=5)
        ufo = Circle(10, 10, 5, fill=gradient('lightGrey', 'grey'))
        ufo.targetX = 0
        ufo.targetY = 0
        app.UFOs.append(ufo)
        app.UFOs.append(trail)

def moveFighter(fighter):
    fighter.centerX = fighter.targetX
    fighter.centerY = fighter.targetY

def moveTrail(fighter, trail):
    trail.x1 = trail.x2
    trail.y1 = trail.y2

    trail.x2 = fighter.centerX
    trail.y2 = fighter.centerY


def onMousePress(mouseX, mouseY):
    app.points.append(mouseX)
    app.points.append(mouseY)
    app.paused = True

def onKeyPress(key):
    if (key == 'space'):
        app.paused = False

def onStep():
    firstUFO = app.UFOs[0]
    firstTrail = app.UFOs[1]
    distToTarget = distance(firstUFO.centerX, firstUFO.centerY,
                            firstUFO.targetX, firstUFO.targetY)
    if (distToTarget < 15):
        nextPointX = app.points.pop(0)
        nextPointY = app.points.pop(0)
        firstUFO.targetX = nextPointX
        firstUFO.targetY = nextPointY
        app.points.append(nextPointX)
        app.points.append(nextPointY)

    angle = angleTo(firstUFO.centerX, firstUFO.centerY,
                    firstUFO.targetX, firstUFO.targetY)
    newX, newY = getPointInDir(firstUFO.centerX, firstUFO.centerY, angle,
                               randrange(10, 30))
    firstUFO.centerX = newX
    firstUFO.centerY = newY
    moveTrail(firstUFO, firstTrail)

    oldX = firstTrail.x1
    oldY = firstTrail.y1
    i = 0
    for index in range(2, len(app.UFOs), 2):
        fighter = app.UFOs[index]
        trail = app.UFOs[index + 1]
        moveFighter(fighter)
        moveTrail(fighter, trail)
        fighter.targetX = oldX
        fighter.targetY = oldY
        oldX = trail.x1
        oldY = trail.y1

app.points = [ 40, 120, 125, 150, 160, 200, 190, 230, 175, 320, 300, 370,
               350, 315, 190, 230, 160, 200, 125, 150, 40, 120 ]
createUFOs(25)


# -
app.background = 'black'
app.stepsPerSecond = 20

# background stars
Star(320, 50, 2, 5, fill='white')
Star(230, 115, 3, 5, fill='white')
Star(380, 315, 2, 5, fill='white')
Star(150, 190, 2, 5, fill='white')
Star(285, 290, 3, 5, fill='white')
Star(50, 325, 2, 5, fill='white')
Star(210, 375, 2, 5, fill='white')
Star(10, 25, 2, 5, fill='white')

# moon
Circle(50, 100, 30, fill=gradient('black', 'grey', start='left'))
Circle(40, 80, 3, fill=rgb(50, 50, 50))
Circle(65, 85, 4, fill=rgb(85, 85, 85))
Circle(70, 110, 3, fill=rgb(85, 85, 85))
Circle(40, 115, 4, fill=rgb(45, 45, 45))
Circle(45, 95, 4, fill=rgb(55, 55, 55))
Circle(60, 100, 4, fill=rgb(75, 75, 75))
Circle(30, 95, 3, fill=rgb(15, 15, 15))

app.UFOs = [ ]
app.points = [ ]

def createUFOs(n):
    # trails
    for i in range(n):
        color = rgb(randrange(0, 256), randrange(0, 256), randrange(0, 256))
        trail = Line(8, 10, 10, 10, fill=gradient(color, 'black'), lineWidth=5)
        ufo = Circle(10, 10, 5, fill=gradient('lightGrey', 'grey'))
        ufo.targetX = 0
        ufo.targetY = 0
        app.UFOs.append(ufo)
        app.UFOs.append(trail)

def moveFighter(fighter):
    fighter.centerX = fighter.targetX
    fighter.centerY = fighter.targetY

def moveTrail(fighter, trail):
    trail.x1 = trail.x2
    trail.y1 = trail.y2

    trail.x2 = fighter.centerX
    trail.y2 = fighter.centerY


def onMousePress(mouseX, mouseY):
    app.points.append(mouseX)
    app.points.append(mouseY)
    app.paused = True

def onKeyPress(key):
    if (key == 'space'):
        app.paused = False

def onStep():
    firstUFO = app.UFOs[0]
    firstTrail = app.UFOs[1]
    distToTarget = distance(firstUFO.centerX, firstUFO.centerY,
                            firstUFO.targetX, firstUFO.targetY)
    if (distToTarget < 15):
        nextPointX = app.points.pop(0)
        nextPointY = app.points.pop(0)
        firstUFO.targetX = nextPointX
        firstUFO.targetY = nextPointY
        app.points.append(nextPointX)
        app.points.append(nextPointY)

    angle = angleTo(firstUFO.centerX, firstUFO.centerY,
                    firstUFO.targetX, firstUFO.targetY)
    newX, newY = getPointInDir(firstUFO.centerX, firstUFO.centerY, angle,
                               randrange(10, 30))
    firstUFO.centerX = newX
    firstUFO.centerY = newY
    moveTrail(firstUFO, firstTrail)

    oldX = firstTrail.x1
    oldY = firstTrail.y1
    i = 0
    for index in range(2, len(app.UFOs), 2):
        fighter = app.UFOs[index]
        trail = app.UFOs[index + 1]
        moveFighter(fighter)
        moveTrail(fighter, trail)
        fighter.targetX = oldX
        fighter.targetY = oldY
        oldX = trail.x1
        oldY = trail.y1

app.points = [
    190, 175, 120, 160, 85, 170, 85, 110, 70, 40, 120, 75, 140, 80, 195, 50,
    175, 105, 190, 175, 135, 260, 85, 170, 120, 160, 190, 175, 135, 260, 170,
    340, 190, 260, 220, 270, 250, 261, 280, 340, 300, 260, 320, 225, 300, 180,
    325, 95, 390, 65, 370, 130, 300, 180, 325, 95, 340, 110, 360, 105,
    355, 125, 370, 130, 300, 180, 190, 175
    ]
createUFOs(55)


# -
app.background = 'black'
app.stepsPerSecond = 20

# background stars
Star(320, 50, 2, 5, fill='white')
Star(230, 115, 3, 5, fill='white')
Star(380, 315, 2, 5, fill='white')
Star(150, 190, 2, 5, fill='white')
Star(285, 290, 3, 5, fill='white')
Star(50, 325, 2, 5, fill='white')
Star(210, 375, 2, 5, fill='white')
Star(10, 25, 2, 5, fill='white')

# moon
Circle(50, 100, 30, fill=gradient('black', 'grey', start='left'))
Circle(40, 80, 3, fill=rgb(50, 50, 50))
Circle(65, 85, 4, fill=rgb(85, 85, 85))
Circle(70, 110, 3, fill=rgb(85, 85, 85))
Circle(40, 115, 4, fill=rgb(45, 45, 45))
Circle(45, 95, 4, fill=rgb(55, 55, 55))
Circle(60, 100, 4, fill=rgb(75, 75, 75))
Circle(30, 95, 3, fill=rgb(15, 15, 15))

app.UFOs = [ ]
app.points = [ ]

def createUFOs(n):
    # trails
    for i in range(n):
        color = rgb(randrange(0, 256), randrange(0, 256), randrange(0, 256))
        trail = Line(8, 10, 10, 10, fill=gradient(color, 'black'), lineWidth=5)
        ufo = Circle(10, 10, 5, fill=gradient('lightGrey', 'grey'))
        ufo.targetX = 0
        ufo.targetY = 0
        app.UFOs.append(ufo)
        app.UFOs.append(trail)

def moveFighter(fighter):
    fighter.centerX = fighter.targetX
    fighter.centerY = fighter.targetY

def moveTrail(fighter, trail):
    trail.x1 = trail.x2
    trail.y1 = trail.y2

    trail.x2 = fighter.centerX
    trail.y2 = fighter.centerY


def onMousePress(mouseX, mouseY):
    app.points.append(mouseX)
    app.points.append(mouseY)
    app.paused = True

def onKeyPress(key):
    if (key == 'space'):
        app.paused = False

def onStep():
    firstUFO = app.UFOs[0]
    firstTrail = app.UFOs[1]
    distToTarget = distance(firstUFO.centerX, firstUFO.centerY,
                            firstUFO.targetX, firstUFO.targetY)
    if (distToTarget < 15):
        nextPointX = app.points.pop(0)
        nextPointY = app.points.pop(0)
        firstUFO.targetX = nextPointX
        firstUFO.targetY = nextPointY
        app.points.append(nextPointX)
        app.points.append(nextPointY)

    angle = angleTo(firstUFO.centerX, firstUFO.centerY,
                    firstUFO.targetX, firstUFO.targetY)
    newX, newY = getPointInDir(firstUFO.centerX, firstUFO.centerY, angle,
                               randrange(10, 30))
    firstUFO.centerX = newX
    firstUFO.centerY = newY
    moveTrail(firstUFO, firstTrail)

    oldX = firstTrail.x1
    oldY = firstTrail.y1
    i = 0
    for index in range(2, len(app.UFOs), 2):
        fighter = app.UFOs[index]
        trail = app.UFOs[index + 1]
        moveFighter(fighter)
        moveTrail(fighter, trail)
        fighter.targetX = oldX
        fighter.targetY = oldY
        oldX = trail.x1
        oldY = trail.y1

app.points = [
    190, 175, 120, 160, 85, 170, 85, 110, 70, 40, 120, 75, 140, 80, 195, 50,
    175, 105, 190, 175, 135, 260, 85, 170, 120, 160, 190, 175, 135, 260, 170,
    340, 190, 260, 220, 270, 250, 261, 280, 340, 300, 260, 320, 225, 300, 180,
    325, 95, 390, 65, 370, 130, 300, 180, 325, 95, 340, 110, 360, 105,
    355, 125, 370, 130, 300, 180, 190, 175
    ]
createUFOs(55)

