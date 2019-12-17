# background
Rect(0, 0, 400, 400, fill=gradient('indigo', 'black', start='top'))
app.logoSize = 2

def drawLogo(x, y, size):
    # Draws a single Green Lantern logo.
    logo = Group(
        Circle(x, y, 7, fill=gradient('lime', 'mediumSeaGreen'),
               border='green', borderWidth=size),
        Circle(x, y, 3, fill=None, border='green', borderWidth=size),
        Line(x - 3, y - 3, x + 3, y - 3, fill='green', lineWidth=1),
        Line(x - 3, y + 3, x + 3, y + 3, fill='green', lineWidth=1)
        )
    logo.width *= size
    logo.height *= size

def drawLogos():
    # While the logoSize is less than 12, draw a logo at a random location.
    # Then, randomly add 1 or 2 to the logoSize.
    while (app.logoSize < 12):
        randomX = randrange(0, 400)
        randomY = randrange(0, 400)
        drawLogo(randomX, randomY, app.logoSize)
        app.logoSize += randrange(1, 3)
def onKeyPress(key):
    # Draws a new set of logos.
    app.group.clear()
    Rect(0, 0, 400, 400, fill=gradient('indigo', 'black', start='top'))
    app.logoSize = 2
    drawLogos()

onKeyPress('a')


# -
# background
Rect(0, 0, 400, 400, fill=gradient('indigo', 'black', start='top'))
app.logoSize = 2

def drawLogo(x, y, size):
    # Draws a single Green Lantern logo.
    logo = Group(
        Circle(x, y, 7, fill=gradient('lime', 'mediumSeaGreen'),
               border='green', borderWidth=size),
        Circle(x, y, 3, fill=None, border='green', borderWidth=size),
        Line(x - 3, y - 3, x + 3, y - 3, fill='green', lineWidth=1),
        Line(x - 3, y + 3, x + 3, y + 3, fill='green', lineWidth=1)
        )
    logo.width *= size
    logo.height *= size

def drawLogos():
    # While the logoSize is less than 12, draw a logo at a random location.
    # Then, randomly add 1 or 2 to the logoSize.
    while (app.logoSize < 12):
        randomX = randrange(0, 400)
        randomY = randrange(0, 400)
        drawLogo(randomX, randomY, app.logoSize)
        app.logoSize += randrange(1, 3)
def onKeyPress(key):
    # Draws a new set of logos.
    app.group.clear()
    Rect(0, 0, 400, 400, fill=gradient('indigo', 'black', start='top'))
    app.logoSize = 2
    drawLogos()

onKeyPress('space')
onKeyPress('a')
onKeyPress('d')


# -
# background
Rect(0, 0, 400, 400, fill=gradient('indigo', 'black', start='top'))
app.logoSize = 2

def drawLogo(x, y, size):
    # Draws a single Green Lantern logo.
    logo = Group(
        Circle(x, y, 7, fill=gradient('lime', 'mediumSeaGreen'),
               border='green', borderWidth=size),
        Circle(x, y, 3, fill=None, border='green', borderWidth=size),
        Line(x - 3, y - 3, x + 3, y - 3, fill='green', lineWidth=1),
        Line(x - 3, y + 3, x + 3, y + 3, fill='green', lineWidth=1)
        )
    logo.width *= size
    logo.height *= size

def drawLogos():
    # While the logoSize is less than 12, draw a logo at a random location.
    # Then, randomly add 1 or 2 to the logoSize.
    while (app.logoSize < 12):
        randomX = randrange(0, 400)
        randomY = randrange(0, 400)
        drawLogo(randomX, randomY, app.logoSize)
        app.logoSize += randrange(1, 3)
def onKeyPress(key):
    # Draws a new set of logos.
    app.group.clear()
    Rect(0, 0, 400, 400, fill=gradient('indigo', 'black', start='top'))
    app.logoSize = 2
    drawLogos()

onKeyPress('space')

