app.stepsPerSecond = 60

newLineHolder = Line(200, 200, 200, 200)
newLineHolder.dx = -5
newLineHolder.dy = 0
cursor = Circle(200, 200, 3, fill='red')

allLines = Group()

def setDxAndDy(newDx, newDy):
    newLineHolder.dx = newDx
    newLineHolder.dy = newDy

def stayOnScreen():
    # Check to make sure the lines aren't going off the screen, and change its
    # direction if it is.
    if (newLineHolder.y2 <= 0):
        setDxAndDy(0, 5)
    elif (newLineHolder.y2 >= 400):
        setDxAndDy(0, -5)
    elif (newLineHolder.x2 >= 400):
        setDxAndDy(-5, 0)
    elif (newLineHolder.x2 <= 0):
        setDxAndDy(5, 0)

def onStep():
    # There is a 1/2 chance we draw a new line.
    newLineChance = randrange(0, 2)

    if (newLineChance == 0):
        allLines.add(
            Line(newLineHolder.x1, newLineHolder.y1,
                 newLineHolder.x2, newLineHolder.y2)
            )

        # Set the new position for newLineHolder.
        newLineHolder.x1 = newLineHolder.x2
        newLineHolder.y1 = newLineHolder.y2

        # There is a 1/2 chance we change the direction the next line heads in.
        newDirectionChance = randrange(0, 2)

        if (newLineHolder.dy != 0):
            if (newDirectionChance == 0):
                setDxAndDy(-5, 0)
            else:
                setDxAndDy(5, 0)
        else:
            if (newDirectionChance == 0):
                setDxAndDy(0, -5)
            else:
                setDxAndDy(0, 5)

    # If the line goes off the screen, move back on screen.
    stayOnScreen()

    # Adjust the x2 and y2 values depending on its dx and dy.
    newLineHolder.x2 += newLineHolder.dx
    newLineHolder.y2 += newLineHolder.dy

    # Move the cursor.
    cursor.centerX = newLineHolder.x2
    cursor.centerY = newLineHolder.y2
    cursor.toFront()

def onKeyPress(key):
    allLines.clear()


