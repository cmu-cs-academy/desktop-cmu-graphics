app.background = 'paleTurquoise'

# title and instructions
Label('The Green Duck', 10, 10, size=30, align='left-top')
Label('Up and down change duck count', 20, 45, align='left-top')
Label('Left and right move green duck', 20, 65, align='left-top')

# water and sun
Rect(0, 200, 400, 200, fill='dodgerBlue')
Circle(350, 50, 50, fill='gold')

ducks = Group()
ducks.greenDuckPosition = 0
ducks.count = 5
ducks.maxCount = 20

def drawDuck(position, color):
    # First draws full-size duck near (0,0).
    duck = Group(
        Oval(10, 8, 20, 8, fill='orange'),
        Circle(30, 8, 20, fill=color),
        Oval(50, 33, 60, 50, fill=color),
        Circle(25, 3, 2)
        )

    # Now moves and resizes the duck as needed.
    scale = (400 / ducks.count) / duck.width
    duck.width *= scale
    duck.height *= scale
    duck.centerX = (position + 0.5) * duck.width
    duck.bottom = 210
    ducks.add(duck)

def drawDucks():
    # Call drawDuck to draw the appropriate number of ducks.
    # All of the ducks are yellow except the one at green duck position.
    for i in range(ducks.count):
        if (i == ducks.greenDuckPosition):
            drawDuck(i, 'lime')
        else:
            drawDuck(i, 'yellow')

def onKeyPress(key):
    # Add or remove ducks whe key pressed.
    if ((key == 'up') and (ducks.count < ducks.maxCount)):
        ducks.count += 1
    elif (key == 'down'):
        if (ducks.count > 3):
            ducks.count -= 1

    # Move the green duck when key pressed.
    elif (key == 'right'):
        ducks.greenDuckPosition += 1
    elif (key == 'left'):
        ducks.greenDuckPosition -= 1

    # Adjust green duck position if needed.
    if (ducks.greenDuckPosition < 0):
        ducks.greenDuckPosition = ducks.count - 1
    elif (ducks.greenDuckPosition >= ducks.count):
        ducks.greenDuckPosition = 0

    # Remove old ducks and draw new ones.
    ducks.clear()
    drawDucks()

drawDucks()

onKeyPress('right')
onKeyPress('up')
onKeyPress('right')
onKeyPress('up')
onKeyPress('left')
onKeyPress('up')


# -
app.background = 'paleTurquoise'

# title and instructions
Label('The Green Duck', 10, 10, size=30, align='left-top')
Label('Up and down change duck count', 20, 45, align='left-top')
Label('Left and right move green duck', 20, 65, align='left-top')

# water and sun
Rect(0, 200, 400, 200, fill='dodgerBlue')
Circle(350, 50, 50, fill='gold')

ducks = Group()
ducks.greenDuckPosition = 0
ducks.count = 5
ducks.maxCount = 20

def drawDuck(position, color):
    # First draws full-size duck near (0,0).
    duck = Group(
        Oval(10, 8, 20, 8, fill='orange'),
        Circle(30, 8, 20, fill=color),
        Oval(50, 33, 60, 50, fill=color),
        Circle(25, 3, 2)
        )

    # Now moves and resizes the duck as needed.
    scale = (400 / ducks.count) / duck.width
    duck.width *= scale
    duck.height *= scale
    duck.centerX = (position + 0.5) * duck.width
    duck.bottom = 210
    ducks.add(duck)

def drawDucks():
    # Call drawDuck to draw the appropriate number of ducks.
    # All of the ducks are yellow except the one at green duck position.
    for i in range(ducks.count):
        if (i == ducks.greenDuckPosition):
            drawDuck(i, 'lime')
        else:
            drawDuck(i, 'yellow')

def onKeyPress(key):
    # Add or remove ducks whe key pressed.
    if ((key == 'up') and (ducks.count < ducks.maxCount)):
        ducks.count += 1
    elif (key == 'down'):
        if (ducks.count > 3):
            ducks.count -= 1

    # Move the green duck when key pressed.
    elif (key == 'right'):
        ducks.greenDuckPosition += 1
    elif (key == 'left'):
        ducks.greenDuckPosition -= 1

    # Adjust green duck position if needed.
    if (ducks.greenDuckPosition < 0):
        ducks.greenDuckPosition = ducks.count - 1
    elif (ducks.greenDuckPosition >= ducks.count):
        ducks.greenDuckPosition = 0

    # Remove old ducks and draw new ones.
    ducks.clear()
    drawDucks()

drawDucks()

onKeyPresses('down', 5)


# -
app.background = 'paleTurquoise'

# title and instructions
Label('The Green Duck', 10, 10, size=30, align='left-top')
Label('Up and down change duck count', 20, 45, align='left-top')
Label('Left and right move green duck', 20, 65, align='left-top')

# water and sun
Rect(0, 200, 400, 200, fill='dodgerBlue')
Circle(350, 50, 50, fill='gold')

ducks = Group()
ducks.greenDuckPosition = 0
ducks.count = 5
ducks.maxCount = 20

def drawDuck(position, color):
    # First draws full-size duck near (0,0).
    duck = Group(
        Oval(10, 8, 20, 8, fill='orange'),
        Circle(30, 8, 20, fill=color),
        Oval(50, 33, 60, 50, fill=color),
        Circle(25, 3, 2)
        )

    # Now moves and resizes the duck as needed.
    scale = (400 / ducks.count) / duck.width
    duck.width *= scale
    duck.height *= scale
    duck.centerX = (position + 0.5) * duck.width
    duck.bottom = 210
    ducks.add(duck)

def drawDucks():
    # Call drawDuck to draw the appropriate number of ducks.
    # All of the ducks are yellow except the one at green duck position.
    for i in range(ducks.count):
        if (i == ducks.greenDuckPosition):
            drawDuck(i, 'lime')
        else:
            drawDuck(i, 'yellow')

def onKeyPress(key):
    # Add or remove ducks whe key pressed.
    if ((key == 'up') and (ducks.count < ducks.maxCount)):
        ducks.count += 1
    elif (key == 'down'):
        if (ducks.count > 3):
            ducks.count -= 1

    # Move the green duck when key pressed.
    elif (key == 'right'):
        ducks.greenDuckPosition += 1
    elif (key == 'left'):
        ducks.greenDuckPosition -= 1

    # Adjust green duck position if needed.
    if (ducks.greenDuckPosition < 0):
        ducks.greenDuckPosition = ducks.count - 1
    elif (ducks.greenDuckPosition >= ducks.count):
        ducks.greenDuckPosition = 0

    # Remove old ducks and draw new ones.
    ducks.clear()
    drawDucks()

drawDucks()

onKeyPress('right')

