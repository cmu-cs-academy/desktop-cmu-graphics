app.background = 'black'
app.stepsPerSecond = 20

Label('Click on the canvas to add stars.', 200, 15, fill='white', size=18)
Label('Press left arrow key to undo.', 200, 35, fill='white', size=18)
Label('Press right arrow key to redo.', 200, 55, fill='white', size=18)

app.stars = [ ]
app.removedStars = [ ]

def undo():
    # Pop the last star from app.stars and add it to app.removedStars.
    # Also make it invisible.
    if (len(app.stars) > 0):
        lastStar = app.stars.pop()
        lastStar.visible = False
        app.removedStars.append(lastStar)
def redo():
    # Pop the last star from app.removedStars and add it to app.stars.
    if (len(app.removedStars) > 0):
        lastStar = app.removedStars.pop()
        lastStar.visible = True
        app.stars.append(lastStar)
def onMousePress(mouseX, mouseY):
    # Adds a star with a random color and radius at the mouse press location.
    radius = randrange(25, 45)
    colors = [ 'fuchsia', 'yellow', 'aqua', 'lawnGreen', 'ghostWhite' ]
    color = choice(colors)
    app.stars.append(
        Star(mouseX, mouseY, radius, 5, fill=None, border=color, borderWidth=4,
             roundness=60)
        )

def onKeyPress(key):
    # Undo when left key is pressed. Redo when right key is pressed.
    if (key == 'left'):
        undo()
    elif (key == 'right'):
        redo()

def onStep():
    for star in app.stars:
        star.rotateAngle += 5

onMousePress(100, 100)
onMousePress(200, 200)
onSteps(20)
app.paused = True


# -
app.background = 'black'
app.stepsPerSecond = 20

Label('Click on the canvas to add stars.', 200, 15, fill='white', size=18)
Label('Press left arrow key to undo.', 200, 35, fill='white', size=18)
Label('Press right arrow key to redo.', 200, 55, fill='white', size=18)

app.stars = [ ]
app.removedStars = [ ]

def undo():
    # Pop the last star from app.stars and add it to app.removedStars.
    # Also make it invisible.
    if (len(app.stars) > 0):
        lastStar = app.stars.pop()
        lastStar.visible = False
        app.removedStars.append(lastStar)
def redo():
    # Pop the last star from app.removedStars and add it to app.stars.
    if (len(app.removedStars) > 0):
        lastStar = app.removedStars.pop()
        lastStar.visible = True
        app.stars.append(lastStar)
def onMousePress(mouseX, mouseY):
    # Adds a star with a random color and radius at the mouse press location.
    radius = randrange(25, 45)
    colors = [ 'fuchsia', 'yellow', 'aqua', 'lawnGreen', 'ghostWhite' ]
    color = choice(colors)
    app.stars.append(
        Star(mouseX, mouseY, radius, 5, fill=None, border=color, borderWidth=4,
             roundness=60)
        )

def onKeyPress(key):
    # Undo when left key is pressed. Redo when right key is pressed.
    if (key == 'left'):
        undo()
    elif (key == 'right'):
        redo()

def onStep():
    for star in app.stars:
        star.rotateAngle += 5

onMousePress(100, 100)
onSteps(10)
onMousePress(200, 200)
onSteps(20)
app.paused = True


# -
app.background = 'black'
app.stepsPerSecond = 20

Label('Click on the canvas to add stars.', 200, 15, fill='white', size=18)
Label('Press left arrow key to undo.', 200, 35, fill='white', size=18)
Label('Press right arrow key to redo.', 200, 55, fill='white', size=18)

app.stars = [ ]
app.removedStars = [ ]

def undo():
    # Pop the last star from app.stars and add it to app.removedStars.
    # Also make it invisible.
    if (len(app.stars) > 0):
        lastStar = app.stars.pop()
        lastStar.visible = False
        app.removedStars.append(lastStar)
def redo():
    # Pop the last star from app.removedStars and add it to app.stars.
    if (len(app.removedStars) > 0):
        lastStar = app.removedStars.pop()
        lastStar.visible = True
        app.stars.append(lastStar)
def onMousePress(mouseX, mouseY):
    # Adds a star with a random color and radius at the mouse press location.
    radius = randrange(25, 45)
    colors = [ 'fuchsia', 'yellow', 'aqua', 'lawnGreen', 'ghostWhite' ]
    color = choice(colors)
    app.stars.append(
        Star(mouseX, mouseY, radius, 5, fill=None, border=color, borderWidth=4,
             roundness=60)
        )

def onKeyPress(key):
    # Undo when left key is pressed. Redo when right key is pressed.
    if (key == 'left'):
        undo()
    elif (key == 'right'):
        redo()

def onStep():
    for star in app.stars:
        star.rotateAngle += 5

onMousePress(100, 100)
onMousePress(300, 300)
onKeyPress('left')
onSteps(10)
onKeyPress('left')
onKeyPress('right')
app.paused = True

