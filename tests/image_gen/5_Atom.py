app.background = gradient('violet', 'navy', start='top')

allRings = Group()


def makeNRings(n):
    # Creates n rings of circles with the first ring's properties defined here.
    ringRadius = 15
    numCircles = 4
    circleRadius = 20
    clockwise = False

    # Creates each of the rings.
    for ring in range(n):
        angleBetweenCircles = 360 / numCircles
        newRing = Group()
        newRing.clockwise = clockwise

        # Draw the circles in the new ring, and add them to the newRing group.
        for c in range(numCircles):
            if ((ring == 0) and (c % 2 == 0)):
                color = 'crimson'
            elif (ring == 0):
                color = 'dodgerblue'
            else:
                color = rgb(255, 220, ring * 60)
            x, y = getPointInDir(200, 200, angleBetweenCircles * c, ringRadius)
            newRing.add(
                Circle(x, y, circleRadius, fill=color)
                )
        allRings.add(newRing)
        # Update the ring radius, number of circles, circle radius, and
        # clockwise bool.
        ringRadius += 50
        numCircles *= 2
        circleRadius /= 2
        clockwise = not clockwise
def onStep():
    # Rotates each ring its correct direction.
    for ring in allRings:
        if (ring.clockwise == True):
            ring.rotateAngle += 1
        else:
            ring.rotateAngle -= 1

makeNRings(3)
onStep()
app.paused = True


# -
app.background = gradient('violet', 'navy', start='top')

allRings = Group()


def makeNRings(n):
    # Creates n rings of circles with the first ring's properties defined here.
    ringRadius = 15
    numCircles = 4
    circleRadius = 20
    clockwise = False

    # Creates each of the rings.
    for ring in range(n):
        angleBetweenCircles = 360 / numCircles
        newRing = Group()
        newRing.clockwise = clockwise

        # Draw the circles in the new ring, and add them to the newRing group.
        for c in range(numCircles):
            if ((ring == 0) and (c % 2 == 0)):
                color = 'crimson'
            elif (ring == 0):
                color = 'dodgerblue'
            else:
                color = rgb(255, 220, ring * 60)
            x, y = getPointInDir(200, 200, angleBetweenCircles * c, ringRadius)
            newRing.add(
                Circle(x, y, circleRadius, fill=color)
                )
        allRings.add(newRing)
        # Update the ring radius, number of circles, circle radius, and
        # clockwise bool.
        ringRadius += 50
        numCircles *= 2
        circleRadius /= 2
        clockwise = not clockwise
def onStep():
    # Rotates each ring its correct direction.
    for ring in allRings:
        if (ring.clockwise == True):
            ring.rotateAngle += 1
        else:
            ring.rotateAngle -= 1

makeNRings(4)
onSteps(15)
app.paused = True


# -
app.background = gradient('violet', 'navy', start='top')

allRings = Group()


def makeNRings(n):
    # Creates n rings of circles with the first ring's properties defined here.
    ringRadius = 15
    numCircles = 4
    circleRadius = 20
    clockwise = False

    # Creates each of the rings.
    for ring in range(n):
        angleBetweenCircles = 360 / numCircles
        newRing = Group()
        newRing.clockwise = clockwise

        # Draw the circles in the new ring, and add them to the newRing group.
        for c in range(numCircles):
            if ((ring == 0) and (c % 2 == 0)):
                color = 'crimson'
            elif (ring == 0):
                color = 'dodgerblue'
            else:
                color = rgb(255, 220, ring * 60)
            x, y = getPointInDir(200, 200, angleBetweenCircles * c, ringRadius)
            newRing.add(
                Circle(x, y, circleRadius, fill=color)
                )
        allRings.add(newRing)
        # Update the ring radius, number of circles, circle radius, and
        # clockwise bool.
        ringRadius += 50
        numCircles *= 2
        circleRadius /= 2
        clockwise = not clockwise
def onStep():
    # Rotates each ring its correct direction.
    for ring in allRings:
        if (ring.clockwise == True):
            ring.rotateAngle += 1
        else:
            ring.rotateAngle -= 1

makeNRings(3)
app.paused = True

