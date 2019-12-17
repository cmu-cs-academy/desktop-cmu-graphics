app.background = gradient('paleTurquoise', 'lightCyan', 'aliceBlue', start='top')
app.flowerCount = 0

earth = Circle(200, 200, 70, fill=gradient('mediumAquamarine', 'mediumSeaGreen'))

text = Label('Plant some flowers!', 200, 360, fill='seaGreen', size=18, bold=True)

def drawFlower(flowerX, flowerY):
    text.value = 'Flower Planted!'
    Line(200, 200, flowerX, flowerY, fill='seaGreen', lineWidth=5)
    app.flowerCount += 1

    # If app.flowerCount is even, draw a orange star.
    # Otherwise draw a lightPink one.
    if (app.flowerCount % 2 == 0):
        Star(flowerX, flowerY, 20, 7, fill='orange', roundness=75)
    else:
        Star(flowerX, flowerY, 20, 7, fill='lightPink', roundness=75)
    Circle(flowerX, flowerY, 8, fill='gold')

def onMousePress(mouseX, mouseY):
    # If the distance between the mouse position and the center of the canvas
    # is less than 120 but larger than 70, draw the flower! Otherwise, change
    # the text value.
    dist = distance(mouseX, mouseY, 200, 200)
    if ((dist < 120) and (dist > 70)):
        drawFlower(mouseX, mouseY)
    elif (dist >= 120):
        text.value = 'Flowers cannot grow that tall!'
    else:
        text.value = 'Flowers cannot be planted inside the earth!'
    earth.toFront()

onMousePress(271, 200)
onMousePress(270, 200)


# -
app.background = gradient('paleTurquoise', 'lightCyan', 'aliceBlue', start='top')
app.flowerCount = 0

earth = Circle(200, 200, 70, fill=gradient('mediumAquamarine', 'mediumSeaGreen'))

text = Label('Plant some flowers!', 200, 360, fill='seaGreen', size=18, bold=True)

def drawFlower(flowerX, flowerY):
    text.value = 'Flower Planted!'
    Line(200, 200, flowerX, flowerY, fill='seaGreen', lineWidth=5)
    app.flowerCount += 1

    # If app.flowerCount is even, draw a orange star.
    # Otherwise draw a lightPink one.
    if (app.flowerCount % 2 == 0):
        Star(flowerX, flowerY, 20, 7, fill='orange', roundness=75)
    else:
        Star(flowerX, flowerY, 20, 7, fill='lightPink', roundness=75)
    Circle(flowerX, flowerY, 8, fill='gold')

def onMousePress(mouseX, mouseY):
    # If the distance between the mouse position and the center of the canvas
    # is less than 120 but larger than 70, draw the flower! Otherwise, change
    # the text value.
    dist = distance(mouseX, mouseY, 200, 200)
    if ((dist < 120) and (dist > 70)):
        drawFlower(mouseX, mouseY)
    elif (dist >= 120):
        text.value = 'Flowers cannot grow that tall!'
    else:
        text.value = 'Flowers cannot be planted inside the earth!'
    earth.toFront()

onMousePress(200, 200)


# -
app.background = gradient('paleTurquoise', 'lightCyan', 'aliceBlue', start='top')
app.flowerCount = 0

earth = Circle(200, 200, 70, fill=gradient('mediumAquamarine', 'mediumSeaGreen'))

text = Label('Plant some flowers!', 200, 360, fill='seaGreen', size=18, bold=True)

def drawFlower(flowerX, flowerY):
    text.value = 'Flower Planted!'
    Line(200, 200, flowerX, flowerY, fill='seaGreen', lineWidth=5)
    app.flowerCount += 1

    # If app.flowerCount is even, draw a orange star.
    # Otherwise draw a lightPink one.
    if (app.flowerCount % 2 == 0):
        Star(flowerX, flowerY, 20, 7, fill='orange', roundness=75)
    else:
        Star(flowerX, flowerY, 20, 7, fill='lightPink', roundness=75)
    Circle(flowerX, flowerY, 8, fill='gold')

def onMousePress(mouseX, mouseY):
    # If the distance between the mouse position and the center of the canvas
    # is less than 120 but larger than 70, draw the flower! Otherwise, change
    # the text value.
    dist = distance(mouseX, mouseY, 200, 200)
    if ((dist < 120) and (dist > 70)):
        drawFlower(mouseX, mouseY)
    elif (dist >= 120):
        text.value = 'Flowers cannot grow that tall!'
    else:
        text.value = 'Flowers cannot be planted inside the earth!'
    earth.toFront()

onMousePress(120, 270)

