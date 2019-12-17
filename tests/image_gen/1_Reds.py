app.stepsPerSecond = 5

app.reds = [ 255, 220, 200, 150, 125, 100, 90, 75, 50, 10 ]
app.y = 0

Rect(0, 0, 400, 400)

def drawRowOfRectangles():
    x = 0
    # Draws a rectangle for each red value.
    for red in app.reds:
        Rect(x, app.y, 40, 25, fill=rgb(red, 0, 0))
        x += 40

def onStep():
    drawRowOfRectangles()

    # Remove the last value from the app.reds list and store it in newVal.
    newVal = app.reds.pop()
    # Creates a new list with the last value.
    newList = [ newVal ]

    # Add back all of the other values.
    for r in app.reds:
        newList.append(r)
    # Sets app.reds equal to the new list.
    app.reds = newList

    # Shifts where the next rectangle will be drawn.
    app.y += 25
    if (app.y >= 400):
        app.paused = True



# -
app.stepsPerSecond = 5

app.reds = [ 255, 220, 200, 150, 125, 100, 90, 75, 50, 10 ]
app.y = 0

Rect(0, 0, 400, 400)

def drawRowOfRectangles():
    x = 0
    # Draws a rectangle for each red value.
    for red in app.reds:
        Rect(x, app.y, 40, 25, fill=rgb(red, 0, 0))
        x += 40

def onStep():
    drawRowOfRectangles()

    # Remove the last value from the app.reds list and store it in newVal.
    newVal = app.reds.pop()
    # Creates a new list with the last value.
    newList = [ newVal ]

    # Add back all of the other values.
    for r in app.reds:
        newList.append(r)
    # Sets app.reds equal to the new list.
    app.reds = newList

    # Shifts where the next rectangle will be drawn.
    app.y += 25
    if (app.y >= 400):
        app.paused = True

onSteps(16)
app.paused = True


# -
app.stepsPerSecond = 5

app.reds = [ 255, 220, 200, 150, 125, 100, 90, 75, 50, 10 ]
app.y = 0

Rect(0, 0, 400, 400)

def drawRowOfRectangles():
    x = 0
    # Draws a rectangle for each red value.
    for red in app.reds:
        Rect(x, app.y, 40, 25, fill=rgb(red, 0, 0))
        x += 40

def onStep():
    drawRowOfRectangles()

    # Remove the last value from the app.reds list and store it in newVal.
    newVal = app.reds.pop()
    # Creates a new list with the last value.
    newList = [ newVal ]

    # Add back all of the other values.
    for r in app.reds:
        newList.append(r)
    # Sets app.reds equal to the new list.
    app.reds = newList

    # Shifts where the next rectangle will be drawn.
    app.y += 25
    if (app.y >= 400):
        app.paused = True

onSteps(16)
app.paused = True

