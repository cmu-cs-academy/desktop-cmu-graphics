app.background = 'black'

app.numRings = 0
app.ringList = [ ]

def drawCircles(n):
    app.numRings = n

    # Creates n rings.
    for index in range(n):
        # Every second ring should be thin.
        if (index % 2 == 1):
            width = 3
        else:
            width = 5
        angle = 18 * index

        # Gets the center coordinate of the ring by using the angle
        # and the center of the canvas.
        centerX, centerY = getPointInDir(200, 200, angle, 60)

        # Adds the ring to the rings group.
        rings.add(
            Circle(centerX, centerY, 60, fill=None, border='mediumAquamarine',
                   borderWidth=width)
            )

rings = Group()
drawCircles(20)
app.ringList = rings.children

def onKeyHold(keys):
    borderColor = gradient('pink', 'hotPink', start='top')

    # For every other ring, set the border fill to borderColor and increase
    # or decrease the radius depending on if 'up' or 'down' is held.
    for index in range(0, app.numRings, 2):
        ring = app.ringList[index]
        ring.border = borderColor
        if ('up' in keys):
            ring.radius += 5
        elif (('down' in keys) and (ring.radius >= 10)):
            ring.radius -= 5
def onKeyRelease(key):
    # Resets all the ring borders to white.
    for ring in app.ringList:
        ring.border = 'mediumAquamarine'



# -
app.background = 'black'

app.numRings = 0
app.ringList = [ ]

def drawCircles(n):
    app.numRings = n

    # Creates n rings.
    for index in range(n):
        # Every second ring should be thin.
        if (index % 2 == 1):
            width = 3
        else:
            width = 5
        angle = 18 * index

        # Gets the center coordinate of the ring by using the angle
        # and the center of the canvas.
        centerX, centerY = getPointInDir(200, 200, angle, 60)

        # Adds the ring to the rings group.
        rings.add(
            Circle(centerX, centerY, 60, fill=None, border='mediumAquamarine',
                   borderWidth=width)
            )

rings = Group()
drawCircles(20)
app.ringList = rings.children

def onKeyHold(keys):
    borderColor = gradient('pink', 'hotPink', start='top')

    # For every other ring, set the border fill to borderColor and increase
    # or decrease the radius depending on if 'up' or 'down' is held.
    for index in range(0, app.numRings, 2):
        ring = app.ringList[index]
        ring.border = borderColor
        if ('up' in keys):
            ring.radius += 5
        elif (('down' in keys) and (ring.radius >= 10)):
            ring.radius -= 5
def onKeyRelease(key):
    # Resets all the ring borders to white.
    for ring in app.ringList:
        ring.border = 'mediumAquamarine'



# -
app.background = 'black'

app.numRings = 0
app.ringList = [ ]

def drawCircles(n):
    app.numRings = n

    # Creates n rings.
    for index in range(n):
        # Every second ring should be thin.
        if (index % 2 == 1):
            width = 3
        else:
            width = 5
        angle = 18 * index

        # Gets the center coordinate of the ring by using the angle
        # and the center of the canvas.
        centerX, centerY = getPointInDir(200, 200, angle, 60)

        # Adds the ring to the rings group.
        rings.add(
            Circle(centerX, centerY, 60, fill=None, border='mediumAquamarine',
                   borderWidth=width)
            )

rings = Group()
drawCircles(20)
app.ringList = rings.children

def onKeyHold(keys):
    borderColor = gradient('pink', 'hotPink', start='top')

    # For every other ring, set the border fill to borderColor and increase
    # or decrease the radius depending on if 'up' or 'down' is held.
    for index in range(0, app.numRings, 2):
        ring = app.ringList[index]
        ring.border = borderColor
        if ('up' in keys):
            ring.radius += 5
        elif (('down' in keys) and (ring.radius >= 10)):
            ring.radius -= 5
def onKeyRelease(key):
    # Resets all the ring borders to white.
    for ring in app.ringList:
        ring.border = 'mediumAquamarine'


