app.stepsPerSecond = 10

# Creates the lists of x and y coordinates for the circles.
app.listX = [ ]
app.listY = [ ]
app.listColors = [ 'lightCoral', 'paleGreen', 'lavender' ]

Rect(0, 0, 400, 400)

def addCircle():
    centerX = randrange(0, 400)
    centerY = randrange(0, 400)

    # Add the x coordinate and y coordinate to the appropriate list.
    app.listX.append(centerX)
    app.listY.append(centerY)
def removeCircle():
    if (len(app.listX) > 10):
        removeIndex = randrange(0, len(app.listX))

        # Use removeIndex to get rid of the element at that index in
        # both listX and listY.
        app.listX.pop(removeIndex)
        app.listY.pop(removeIndex)
def drawCircles():
    # Clears the canvas and redraws the background.
    app.group.clear()
    Rect(0, 0, 400, 400)

    # Loops over all the coordinates and draws 2 circles with random
    # radius and color.
    for index in range(len(app.listX)):
        centerX = app.listX[index]
        centerY = app.listY[index]
        radius = randrange(5, 25)

        color = choice(app.listColors)

        Circle(centerX, centerY, radius, fill=None, border=color)
        Circle(centerX, centerY, radius + 5, fill=None, border=color,
               borderWidth=3)

def onStep():
    addCircle()
    removeCircle()
    drawCircles()

onSteps(5)
app.paused = True


# -
app.stepsPerSecond = 10

# Creates the lists of x and y coordinates for the circles.
app.listX = [ ]
app.listY = [ ]
app.listColors = [ 'lightCoral', 'paleGreen', 'lavender' ]

Rect(0, 0, 400, 400)

def addCircle():
    centerX = randrange(0, 400)
    centerY = randrange(0, 400)

    # Add the x coordinate and y coordinate to the appropriate list.
    app.listX.append(centerX)
    app.listY.append(centerY)
def removeCircle():
    if (len(app.listX) > 10):
        removeIndex = randrange(0, len(app.listX))

        # Use removeIndex to get rid of the element at that index in
        # both listX and listY.
        app.listX.pop(removeIndex)
        app.listY.pop(removeIndex)
def drawCircles():
    # Clears the canvas and redraws the background.
    app.group.clear()
    Rect(0, 0, 400, 400)

    # Loops over all the coordinates and draws 2 circles with random
    # radius and color.
    for index in range(len(app.listX)):
        centerX = app.listX[index]
        centerY = app.listY[index]
        radius = randrange(5, 25)

        color = choice(app.listColors)

        Circle(centerX, centerY, radius, fill=None, border=color)
        Circle(centerX, centerY, radius + 5, fill=None, border=color,
               borderWidth=3)

def onStep():
    addCircle()
    removeCircle()
    drawCircles()

onSteps(20)
app.paused = True


# -
app.stepsPerSecond = 10

# Creates the lists of x and y coordinates for the circles.
app.listX = [ ]
app.listY = [ ]
app.listColors = [ 'lightCoral', 'paleGreen', 'lavender' ]

Rect(0, 0, 400, 400)

def addCircle():
    centerX = randrange(0, 400)
    centerY = randrange(0, 400)

    # Add the x coordinate and y coordinate to the appropriate list.
    app.listX.append(centerX)
    app.listY.append(centerY)
def removeCircle():
    if (len(app.listX) > 10):
        removeIndex = randrange(0, len(app.listX))

        # Use removeIndex to get rid of the element at that index in
        # both listX and listY.
        app.listX.pop(removeIndex)
        app.listY.pop(removeIndex)
def drawCircles():
    # Clears the canvas and redraws the background.
    app.group.clear()
    Rect(0, 0, 400, 400)

    # Loops over all the coordinates and draws 2 circles with random
    # radius and color.
    for index in range(len(app.listX)):
        centerX = app.listX[index]
        centerY = app.listY[index]
        radius = randrange(5, 25)

        color = choice(app.listColors)

        Circle(centerX, centerY, radius, fill=None, border=color)
        Circle(centerX, centerY, radius + 5, fill=None, border=color,
               borderWidth=3)

def onStep():
    addCircle()
    removeCircle()
    drawCircles()


