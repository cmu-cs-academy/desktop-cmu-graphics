app.background = 'black'
app.stepsPerSecond = 2
app.points = makeList(5, 2)

Label('Add 5 points to animate the polygon', 200, 15, fill='white', size=18,
      bold=True)
Label('Points Added: ', 190, 40, fill='white', size=18, bold=True)
pointsAdded = Label(0, 255, 40, fill='white', size=18, bold=True)
p = Polygon(fill=gradient('salmon', 'cornflowerBlue', start='bottom'))


def onMousePress(mouseX, mouseY):
    # Only adds up to 5 points.
    if (pointsAdded.value < 5):
        # Gets the index for the next point.
        index = pointsAdded.value

        # Use the index to get an inner list from app.points. Set the 0th
        # value of that inner list to mouseX and set the 1st value of the
        # inner list to mouseY. Also draw a dot and update the value of
        # pointsAdded.
        app.points[index][0] = mouseX
        app.points[index][1] = mouseY
        Circle(mouseX, mouseY, 4, fill='white')
        pointsAdded.value += 1
def onStep():
    # Animates if all 5 points are added and the polygon is not yet complete.
    if ((pointsAdded.value == 5) and (len(app.points) > 0)):
        coords = app.points.pop()
        x = coords[0]
        y = coords[1]
        Circle(x, y, 5, fill='royalBlue')
        p.addPoint(x, y)

onMousePress(100, 100)
onMousePress(300, 200)
onMousePress(200, 300)
onMousePress(100, 200)
onMousePress(300, 100)
onSteps(5)
app.paused = True


# -
app.background = 'black'
app.stepsPerSecond = 2
app.points = makeList(5, 2)

Label('Add 5 points to animate the polygon', 200, 15, fill='white', size=18,
      bold=True)
Label('Points Added: ', 190, 40, fill='white', size=18, bold=True)
pointsAdded = Label(0, 255, 40, fill='white', size=18, bold=True)
p = Polygon(fill=gradient('salmon', 'cornflowerBlue', start='bottom'))


def onMousePress(mouseX, mouseY):
    # Only adds up to 5 points.
    if (pointsAdded.value < 5):
        # Gets the index for the next point.
        index = pointsAdded.value

        # Use the index to get an inner list from app.points. Set the 0th
        # value of that inner list to mouseX and set the 1st value of the
        # inner list to mouseY. Also draw a dot and update the value of
        # pointsAdded.
        app.points[index][0] = mouseX
        app.points[index][1] = mouseY
        Circle(mouseX, mouseY, 4, fill='white')
        pointsAdded.value += 1
def onStep():
    # Animates if all 5 points are added and the polygon is not yet complete.
    if ((pointsAdded.value == 5) and (len(app.points) > 0)):
        coords = app.points.pop()
        x = coords[0]
        y = coords[1]
        Circle(x, y, 5, fill='royalBlue')
        p.addPoint(x, y)

onMousePress(100, 100)
onMousePress(100, 200)
onMousePress(200, 300)
onMousePress(300, 200)
onMousePress(300, 100)
onSteps(3)
app.paused = True


# -
app.background = 'black'
app.stepsPerSecond = 2
app.points = makeList(5, 2)

Label('Add 5 points to animate the polygon', 200, 15, fill='white', size=18,
      bold=True)
Label('Points Added: ', 190, 40, fill='white', size=18, bold=True)
pointsAdded = Label(0, 255, 40, fill='white', size=18, bold=True)
p = Polygon(fill=gradient('salmon', 'cornflowerBlue', start='bottom'))


def onMousePress(mouseX, mouseY):
    # Only adds up to 5 points.
    if (pointsAdded.value < 5):
        # Gets the index for the next point.
        index = pointsAdded.value

        # Use the index to get an inner list from app.points. Set the 0th
        # value of that inner list to mouseX and set the 1st value of the
        # inner list to mouseY. Also draw a dot and update the value of
        # pointsAdded.
        app.points[index][0] = mouseX
        app.points[index][1] = mouseY
        Circle(mouseX, mouseY, 4, fill='white')
        pointsAdded.value += 1
def onStep():
    # Animates if all 5 points are added and the polygon is not yet complete.
    if ((pointsAdded.value == 5) and (len(app.points) > 0)):
        coords = app.points.pop()
        x = coords[0]
        y = coords[1]
        Circle(x, y, 5, fill='royalBlue')
        p.addPoint(x, y)

onMousePress(100, 100)
onMousePress(100, 200)
onMousePress(200, 300)
onMousePress(300, 200)
onMousePress(300, 100)
onSteps(3)
app.paused = True

