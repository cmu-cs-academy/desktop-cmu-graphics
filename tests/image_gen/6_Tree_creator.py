app.background = 'skyBlue'

# tree
Polygon(175, 400, 225, 400, 205, 120, 195, 120,
        fill=gradient('saddleBrown', 'burlyWood', start='left'))
Rect(0, 370, 400, 30, fill='forestGreen')

app.lastX = 200
app.lastY = 120
app.oldXVals = [ ]
app.oldYVals = [ ]
app.leafColors = [ 'darkGreen', 'forestGreen', 'oliveDrab', 'mediumSeaGreen' ]

def onKeyPress(key):
    if (len(app.oldXVals) > 1):
        # Set app.lastX and app.lastY to a random element from the
        # oldVals lists.
        app.lastX = choice(app.oldXVals)
        app.lastY = choice(app.oldYVals)
def onStep():
    # Gets a new (x,y) position.
    newX = app.lastX + randrange(-20, 21)
    newY = app.lastY + randrange(-20, 21)

    # Get a new color for the leaf and then draw a line using the app properties.
    color = choice(app.leafColors)
    Line(app.lastX, app.lastY, newX, newY, fill=color, lineWidth=20)
    # Add the lastX and lastX to the oldVals lists.
    app.oldXVals.append(app.lastX)
    app.oldYVals.append(app.lastY)
    # Update lastX and lastY to the new positions.
    app.lastX = newX
    app.lastY = newY

onSteps(100)
app.paused = True


# -
app.background = 'skyBlue'

# tree
Polygon(175, 400, 225, 400, 205, 120, 195, 120,
        fill=gradient('saddleBrown', 'burlyWood', start='left'))
Rect(0, 370, 400, 30, fill='forestGreen')

app.lastX = 200
app.lastY = 120
app.oldXVals = [ ]
app.oldYVals = [ ]
app.leafColors = [ 'darkGreen', 'forestGreen', 'oliveDrab', 'mediumSeaGreen' ]

def onKeyPress(key):
    if (len(app.oldXVals) > 1):
        # Set app.lastX and app.lastY to a random element from the
        # oldVals lists.
        app.lastX = choice(app.oldXVals)
        app.lastY = choice(app.oldYVals)
def onStep():
    # Gets a new (x,y) position.
    newX = app.lastX + randrange(-20, 21)
    newY = app.lastY + randrange(-20, 21)

    # Get a new color for the leaf and then draw a line using the app properties.
    color = choice(app.leafColors)
    Line(app.lastX, app.lastY, newX, newY, fill=color, lineWidth=20)
    # Add the lastX and lastX to the oldVals lists.
    app.oldXVals.append(app.lastX)
    app.oldYVals.append(app.lastY)
    # Update lastX and lastY to the new positions.
    app.lastX = newX
    app.lastY = newY



# -
app.background = 'skyBlue'

# tree
Polygon(175, 400, 225, 400, 205, 120, 195, 120,
        fill=gradient('saddleBrown', 'burlyWood', start='left'))
Rect(0, 370, 400, 30, fill='forestGreen')

app.lastX = 200
app.lastY = 120
app.oldXVals = [ ]
app.oldYVals = [ ]
app.leafColors = [ 'darkGreen', 'forestGreen', 'oliveDrab', 'mediumSeaGreen' ]

def onKeyPress(key):
    if (len(app.oldXVals) > 1):
        # Set app.lastX and app.lastY to a random element from the
        # oldVals lists.
        app.lastX = choice(app.oldXVals)
        app.lastY = choice(app.oldYVals)
def onStep():
    # Gets a new (x,y) position.
    newX = app.lastX + randrange(-20, 21)
    newY = app.lastY + randrange(-20, 21)

    # Get a new color for the leaf and then draw a line using the app properties.
    color = choice(app.leafColors)
    Line(app.lastX, app.lastY, newX, newY, fill=color, lineWidth=20)
    # Add the lastX and lastX to the oldVals lists.
    app.oldXVals.append(app.lastX)
    app.oldYVals.append(app.lastY)
    # Update lastX and lastY to the new positions.
    app.lastX = newX
    app.lastY = newY

onSteps(100)
app.paused = True

