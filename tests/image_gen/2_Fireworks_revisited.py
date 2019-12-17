app.background = gradient('midnightBlue', 'steelBlue', start='top')
app.stepsPerSecond = 60

Polygon(150, 400, 300, 200, 450, 400,
        fill=gradient('darkSlateBlue', 'darkBlue', start='top'))
Polygon(-100, 400, 100, 100, 300, 400,
        fill=gradient('darkSlateBlue', 'midnightBlue', start='top'))

fireworks = Group()
streams = Group()

clouds = Group(
    Circle(90, 50, 20, fill=rgb(80, 80, 150)),
    Circle(110, 50, 20, fill=rgb(80, 80, 150)),
    Circle(100, 60, 20, fill=rgb(80, 80, 150)),
    Circle(120, 60, 20, fill=rgb(80, 80, 150)),
    Circle(80, 60, 20, fill=rgb(80, 80, 150))
    )

ferrisWheel = Star(100, 300, 75, 20, fill='white', roundness=15)

def drawRings():
    # Adds inner loops for ferris wheel.
    ringBorderColors = [ 'lightBlue', 'red', 'yellow', 'green', 'purple', 'blue' ]
    ringNumber = 1

    # Make a ring for each of the colors in the ringBorderColors list.
    for borderColor in ringBorderColors:
        newRadius = ferrisWheel.radius / (ringNumber)
        Circle(100, 300, newRadius, fill=None, border=borderColor, borderWidth=8,
               opacity=70)
        ringNumber += 1
drawRings()

# Adds highlights and legs for ferris wheel.
Circle(100, 300, 71, fill=None, border='white')
Circle(100, 300, 79, fill=None, border='white')
Line(75, 400, 100, 300, fill='white', lineWidth=4)
Line(125, 400, 100, 300, fill='white', lineWidth=4)

def onMousePress(mouseX, mouseY):
    fireWorkColors = [ 'red', 'lime', 'magenta', 'yellow', 'orangeRed',
                       'powderBlue' ]

    # Get a random color for the firework from fireWorkColors.
    randomColor = fireWorkColors[randrange(0, len(fireWorkColors))]
    # Makes the firework.
    newStream = Line(mouseX, 400, mouseX, 460, fill=randomColor)
    newStream.fireworkHeight = mouseY
    newStream.color = randomColor
    streams.add(newStream)

def makeNewExplosion(cx, cy, color):
    # Firework goes off.
    firework = Group(
        Star(cx, cy, randrange(5, 20), 1500, fill=color),
        Star(cx, cy, 1, 30, fill=color, roundness=10)
        )
    fireworks.add(firework)

def animateLaunches():
    # Moves the firework trails up.
    streams.toFront()
    for stream in streams.children:
        stream.top -= 5
        stream.opacity -= 1

        # If the firework has reached the height, it should explode.
        if (stream.top <= stream.fireworkHeight):
            streams.remove(stream)
            makeNewExplosion(stream.x1, stream.y1, stream.color)

def animateExplosions():
    # Expands and fades out all of the explosions.
    fireworks.toFront()
    for firework in fireworks.children:
        firework.width += 1
        firework.height += 1
        firework.opacity -= 2
        firework.rotateAngle += 5

        # Once the firework has faded enough, removes it completely.
        if (firework.opacity <= 3):
            fireworks.remove(firework)

def rotateFerrisWheel():
    ferrisWheel.rotateAngle += 0.1

def moveCloud():
    clouds.centerX += 1
    if (clouds.left >= 400):
        clouds.right = 0

def onStep():
    animateExplosions()
    animateLaunches()
    rotateFerrisWheel()
    moveCloud()

onMousePress(200, 50)
onStep()
app.paused = True


# -
app.background = gradient('midnightBlue', 'steelBlue', start='top')
app.stepsPerSecond = 60

Polygon(150, 400, 300, 200, 450, 400,
        fill=gradient('darkSlateBlue', 'darkBlue', start='top'))
Polygon(-100, 400, 100, 100, 300, 400,
        fill=gradient('darkSlateBlue', 'midnightBlue', start='top'))

fireworks = Group()
streams = Group()

clouds = Group(
    Circle(90, 50, 20, fill=rgb(80, 80, 150)),
    Circle(110, 50, 20, fill=rgb(80, 80, 150)),
    Circle(100, 60, 20, fill=rgb(80, 80, 150)),
    Circle(120, 60, 20, fill=rgb(80, 80, 150)),
    Circle(80, 60, 20, fill=rgb(80, 80, 150))
    )

ferrisWheel = Star(100, 300, 75, 20, fill='white', roundness=15)

def drawRings():
    # Adds inner loops for ferris wheel.
    ringBorderColors = [ 'lightBlue', 'red', 'yellow', 'green', 'purple', 'blue' ]
    ringNumber = 1

    # Make a ring for each of the colors in the ringBorderColors list.
    for borderColor in ringBorderColors:
        newRadius = ferrisWheel.radius / (ringNumber)
        Circle(100, 300, newRadius, fill=None, border=borderColor, borderWidth=8,
               opacity=70)
        ringNumber += 1
drawRings()

# Adds highlights and legs for ferris wheel.
Circle(100, 300, 71, fill=None, border='white')
Circle(100, 300, 79, fill=None, border='white')
Line(75, 400, 100, 300, fill='white', lineWidth=4)
Line(125, 400, 100, 300, fill='white', lineWidth=4)

def onMousePress(mouseX, mouseY):
    fireWorkColors = [ 'red', 'lime', 'magenta', 'yellow', 'orangeRed',
                       'powderBlue' ]

    # Get a random color for the firework from fireWorkColors.
    randomColor = fireWorkColors[randrange(0, len(fireWorkColors))]
    # Makes the firework.
    newStream = Line(mouseX, 400, mouseX, 460, fill=randomColor)
    newStream.fireworkHeight = mouseY
    newStream.color = randomColor
    streams.add(newStream)

def makeNewExplosion(cx, cy, color):
    # Firework goes off.
    firework = Group(
        Star(cx, cy, randrange(5, 20), 1500, fill=color),
        Star(cx, cy, 1, 30, fill=color, roundness=10)
        )
    fireworks.add(firework)

def animateLaunches():
    # Moves the firework trails up.
    streams.toFront()
    for stream in streams.children:
        stream.top -= 5
        stream.opacity -= 1

        # If the firework has reached the height, it should explode.
        if (stream.top <= stream.fireworkHeight):
            streams.remove(stream)
            makeNewExplosion(stream.x1, stream.y1, stream.color)

def animateExplosions():
    # Expands and fades out all of the explosions.
    fireworks.toFront()
    for firework in fireworks.children:
        firework.width += 1
        firework.height += 1
        firework.opacity -= 2
        firework.rotateAngle += 5

        # Once the firework has faded enough, removes it completely.
        if (firework.opacity <= 3):
            fireworks.remove(firework)

def rotateFerrisWheel():
    ferrisWheel.rotateAngle += 0.1

def moveCloud():
    clouds.centerX += 1
    if (clouds.left >= 400):
        clouds.right = 0

def onStep():
    animateExplosions()
    animateLaunches()
    rotateFerrisWheel()
    moveCloud()

onMousePress(200, 50)
onStep()
app.paused = True


# -
app.background = gradient('midnightBlue', 'steelBlue', start='top')
app.stepsPerSecond = 60

Polygon(150, 400, 300, 200, 450, 400,
        fill=gradient('darkSlateBlue', 'darkBlue', start='top'))
Polygon(-100, 400, 100, 100, 300, 400,
        fill=gradient('darkSlateBlue', 'midnightBlue', start='top'))

fireworks = Group()
streams = Group()

clouds = Group(
    Circle(90, 50, 20, fill=rgb(80, 80, 150)),
    Circle(110, 50, 20, fill=rgb(80, 80, 150)),
    Circle(100, 60, 20, fill=rgb(80, 80, 150)),
    Circle(120, 60, 20, fill=rgb(80, 80, 150)),
    Circle(80, 60, 20, fill=rgb(80, 80, 150))
    )

ferrisWheel = Star(100, 300, 75, 20, fill='white', roundness=15)

def drawRings():
    # Adds inner loops for ferris wheel.
    ringBorderColors = [ 'lightBlue', 'red', 'yellow', 'green', 'purple', 'blue' ]
    ringNumber = 1

    # Make a ring for each of the colors in the ringBorderColors list.
    for borderColor in ringBorderColors:
        newRadius = ferrisWheel.radius / (ringNumber)
        Circle(100, 300, newRadius, fill=None, border=borderColor, borderWidth=8,
               opacity=70)
        ringNumber += 1
drawRings()

# Adds highlights and legs for ferris wheel.
Circle(100, 300, 71, fill=None, border='white')
Circle(100, 300, 79, fill=None, border='white')
Line(75, 400, 100, 300, fill='white', lineWidth=4)
Line(125, 400, 100, 300, fill='white', lineWidth=4)

def onMousePress(mouseX, mouseY):
    fireWorkColors = [ 'red', 'lime', 'magenta', 'yellow', 'orangeRed',
                       'powderBlue' ]

    # Get a random color for the firework from fireWorkColors.
    randomColor = fireWorkColors[randrange(0, len(fireWorkColors))]
    # Makes the firework.
    newStream = Line(mouseX, 400, mouseX, 460, fill=randomColor)
    newStream.fireworkHeight = mouseY
    newStream.color = randomColor
    streams.add(newStream)

def makeNewExplosion(cx, cy, color):
    # Firework goes off.
    firework = Group(
        Star(cx, cy, randrange(5, 20), 1500, fill=color),
        Star(cx, cy, 1, 30, fill=color, roundness=10)
        )
    fireworks.add(firework)

def animateLaunches():
    # Moves the firework trails up.
    streams.toFront()
    for stream in streams.children:
        stream.top -= 5
        stream.opacity -= 1

        # If the firework has reached the height, it should explode.
        if (stream.top <= stream.fireworkHeight):
            streams.remove(stream)
            makeNewExplosion(stream.x1, stream.y1, stream.color)

def animateExplosions():
    # Expands and fades out all of the explosions.
    fireworks.toFront()
    for firework in fireworks.children:
        firework.width += 1
        firework.height += 1
        firework.opacity -= 2
        firework.rotateAngle += 5

        # Once the firework has faded enough, removes it completely.
        if (firework.opacity <= 3):
            fireworks.remove(firework)

def rotateFerrisWheel():
    ferrisWheel.rotateAngle += 0.1

def moveCloud():
    clouds.centerX += 1
    if (clouds.left >= 400):
        clouds.right = 0

def onStep():
    animateExplosions()
    animateLaunches()
    rotateFerrisWheel()
    moveCloud()

onSteps(30)
app.paused = True

