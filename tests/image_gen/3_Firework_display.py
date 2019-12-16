app.background = gradient('midnightBlue', 'steelBlue', start='top')
app.stepsPerSecond = 60
app.randomColor = 'red'

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

def createFerrisWheel():
    # Adds inner loops for ferris wheel.
    for ringNumber in range(5):
        # Gets the ring's color.
        if (ringNumber == 0):
            borderColor = 'mediumBlue'
        elif (ringNumber == 1):
            borderColor = 'yellow'
        elif (ringNumber == 2):
            borderColor = 'green'
        elif (ringNumber == 3):
            borderColor = 'blue'
        elif (ringNumber == 4):
            borderColor = 'red'
        else:
            borderColor = 'purple'

        newRadius = ferrisWheel.radius / (ringNumber + 1)
        Circle(100, 300, newRadius, fill=None, border=borderColor, borderWidth=8,
               opacity=70)

    # Adds highlights and legs for ferris wheel.
    Circle(100, 300, 71, fill=None, border='white')
    Circle(100, 300, 79, fill=None, border='white')
    Line(75, 400, 100, 300, fill='white', lineWidth=4)
    Line(125, 400, 100, 300, fill='white', lineWidth=4)

createFerrisWheel()

def setFireworkColor(randomNumber):
    # Picks the color given by the randomNumber.
    if (randomNumber == 0):
        app.randomColor = 'lime'
    elif (randomNumber == 1):
        app.randomColor = 'red'
    elif (randomNumber == 2):
        app.randomColor = 'orangeRed'
    elif (randomNumber == 3):
        app.randomColor = 'yellow'
    else:
        app.randomColor = 'magenta'

# Called when a firework explodes at its max height.
def makeNewExplosion(cx, cy, color):
    firework = Circle(cx, cy, randrange(10, 30), fill=color)
    fireworks.add(firework)

def animateLaunches():
    # Moves the firework trails up.
    streams.toFront()
    for stream in streams.children:
        stream.top -= 5
        stream.opacity -= 1

        # If the firework has reached the max height, it should explode.
        if (stream.top <= stream.fireworkHeight):
            makeNewExplosion(stream.x1, stream.y1, stream.fill)
            streams.remove(stream)

def animateExplosions():
    # Expands and fades out all of the explosions.
    fireworks.toFront()
    for firework in fireworks.children:
        firework.radius += 1
        firework.opacity -= 2

        # Once the firework has faded enough, removes it completely.
        if (firework.opacity <= 3):
            fireworks.remove(firework)

def onMousePress(mouseX, mouseY):
    # Creates a new stream with a random color and a max height of mouseY.
    setFireworkColor(randrange(0, 5))
    newStream = Line(mouseX, 400, mouseX, 460, fill=app.randomColor)
    newStream.fireworkHeight = mouseY
    streams.add(newStream)

def onStep():
    animateExplosions()
    animateLaunches()

    # Rotates the ferris wheel and move the clouds.
    ferrisWheel.rotateAngle += 0.1
    clouds.centerX += 1
    if (clouds.left >= 400):
        clouds.right = 0


