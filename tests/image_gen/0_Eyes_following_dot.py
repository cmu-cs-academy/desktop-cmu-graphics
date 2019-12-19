app.background = 'salmon'

dot = Circle(200, 200, 5, fill=None, border='white')
eyes = Group()

def makeEyes():
    # Fix these nested for loops so that they draw another row and column of
    # eyes in the bottom right corner.
    for centerX in range(0, 401, 100):
        for centerY in range(0, 401, 100):
            Oval(centerX, centerY, 70, 65, fill='white')
            newEye = Group(
                Oval(centerX, centerY, 30, 28, fill='cyan', border='black'),
                Oval(centerX, centerY, 15, 15)
                )
            # Saves centerX, and centerY value so you can use it for resetting
            # the eye in onMouseMove.
            newEye.resetX = centerX
            newEye.resetY = centerY
            eyes.add(newEye)
    eyes.toFront()
    dot.toFront()

makeEyes()

def onMouseMove(mouseX, mouseY):
    # Moves the dot to the mouse location.
    dot.centerX = mouseX
    dot.centerY = mouseY

    # Loops over each eye in the group eyes.
    for eye in eyes.children:
        # Change this code so that the angle it is creating is the angle between
        # the eye's reset custom properties and the current mouse location.
        angle = angleTo(eye.resetX, eye.resetY, mouseX, mouseY)
        # Increase the amount the eyes move based on how far from the mouse
        # they are.
        distanceMoved = 20 - (distance(mouseX, mouseY, eye.resetX, eye.resetY) / 20)

        # Change this code so that the getPointInDir function uses the eye's
        # reset custom properties as its x1 and y1, and uses the calculated
        # angle above.
        newCenterX, newCenterY = getPointInDir(eye.resetX, eye.resetY,
                                               angle, distanceMoved)
        eye.centerX = newCenterX
        eye.centerY = newCenterY

onMouseMove(250, 200)


# -
app.background = 'salmon'

dot = Circle(200, 200, 5, fill=None, border='white')
eyes = Group()

def makeEyes():
    # Fix these nested for loops so that they draw another row and column of
    # eyes in the bottom right corner.
    for centerX in range(0, 401, 100):
        for centerY in range(0, 401, 100):
            Oval(centerX, centerY, 70, 65, fill='white')
            newEye = Group(
                Oval(centerX, centerY, 30, 28, fill='cyan', border='black'),
                Oval(centerX, centerY, 15, 15)
                )
            # Saves centerX, and centerY value so you can use it for resetting
            # the eye in onMouseMove.
            newEye.resetX = centerX
            newEye.resetY = centerY
            eyes.add(newEye)
    eyes.toFront()
    dot.toFront()

makeEyes()

def onMouseMove(mouseX, mouseY):
    # Moves the dot to the mouse location.
    dot.centerX = mouseX
    dot.centerY = mouseY

    # Loops over each eye in the group eyes.
    for eye in eyes.children:
        # Change this code so that the angle it is creating is the angle between
        # the eye's reset custom properties and the current mouse location.
        angle = angleTo(eye.resetX, eye.resetY, mouseX, mouseY)
        # Increase the amount the eyes move based on how far from the mouse
        # they are.
        distanceMoved = 20 - (distance(mouseX, mouseY, eye.resetX, eye.resetY) / 20)

        # Change this code so that the getPointInDir function uses the eye's
        # reset custom properties as its x1 and y1, and uses the calculated
        # angle above.
        newCenterX, newCenterY = getPointInDir(eye.resetX, eye.resetY,
                                               angle, distanceMoved)
        eye.centerX = newCenterX
        eye.centerY = newCenterY

onMouseMove(270, 220)
onMouseMove(230, 60)


# -
app.background = 'salmon'

dot = Circle(200, 200, 5, fill=None, border='white')
eyes = Group()

def makeEyes():
    # Fix these nested for loops so that they draw another row and column of
    # eyes in the bottom right corner.
    for centerX in range(0, 401, 100):
        for centerY in range(0, 401, 100):
            Oval(centerX, centerY, 70, 65, fill='white')
            newEye = Group(
                Oval(centerX, centerY, 30, 28, fill='cyan', border='black'),
                Oval(centerX, centerY, 15, 15)
                )
            # Saves centerX, and centerY value so you can use it for resetting
            # the eye in onMouseMove.
            newEye.resetX = centerX
            newEye.resetY = centerY
            eyes.add(newEye)
    eyes.toFront()
    dot.toFront()

makeEyes()

def onMouseMove(mouseX, mouseY):
    # Moves the dot to the mouse location.
    dot.centerX = mouseX
    dot.centerY = mouseY

    # Loops over each eye in the group eyes.
    for eye in eyes.children:
        # Change this code so that the angle it is creating is the angle between
        # the eye's reset custom properties and the current mouse location.
        angle = angleTo(eye.resetX, eye.resetY, mouseX, mouseY)
        # Increase the amount the eyes move based on how far from the mouse
        # they are.
        distanceMoved = 20 - (distance(mouseX, mouseY, eye.resetX, eye.resetY) / 20)

        # Change this code so that the getPointInDir function uses the eye's
        # reset custom properties as its x1 and y1, and uses the calculated
        # angle above.
        newCenterX, newCenterY = getPointInDir(eye.resetX, eye.resetY,
                                               angle, distanceMoved)
        eye.centerX = newCenterX
        eye.centerY = newCenterY


