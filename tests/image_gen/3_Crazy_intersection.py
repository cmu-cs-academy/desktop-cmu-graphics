app.background = 'mediumSeaGreen'
app.stepsTillNextCar = 0

# roads
Rect(150, 0, 100, 400, fill='dimGray')
Rect(0, 150, 400, 100, fill='dimGray')
Rect(-100, 150, 600, 100, fill='dimGray', rotateAngle=45)
Rect(-100, 150, 600, 100, fill='dimGray', rotateAngle=315)

lines = Group()
cars = Group()

def makeLines():
    # Adds four dashed lines.
    lines.add(
        Line(200, 0, 200, 400, fill='fireBrick', lineWidth=8, dashes=True),
        Line(0, 200, 400, 200, fill='gold', lineWidth=8, dashes=True),
        Line(0, 0, 400, 400, fill='mediumSeaGreen', lineWidth=8, dashes=True),
        Line(400, 0, 0, 400, fill='dodgerBlue', lineWidth=8, dashes=True)
        )

    # Sets the originalFill of each line so we can reset it later.
    originalFills = [ 'fireBrick', 'gold', 'mediumSeaGreen', 'dodgerBlue' ]
    for i in range(len(lines.children)):
        lines.children[i].originalFill = originalFills[i]

makeLines()

def drawCar(x, y, angle, color):
    car = Group(
        Rect(200, 200, 30, 60, fill=color, align='center'),
        Rect(200, 185, 34, 3, fill=color, align='center'),
        Rect(188, 172, 5, 4, fill='yellow', align='center'),
        Rect(213, 172, 5, 4, fill='yellow', align='center'),
        Rect(200, 220, 20, 8, fill='gray', align='center'),
        Rect(200, 190, 20, 12, fill='gray', align='center')
        )
    car.rotateAngle = angle
    car.centerX = x
    car.centerY = y
    cars.add(car)

def onMouseMove(mouseX, mouseY):
    # Resets each line back to its original color.
    for line in lines.children:
        line.fill = line.originalFill

    # If the mouse is on a line, set its fill to white.
    line = lines.hitTest(mouseX, mouseY)
    if (line != None):
        line.fill = 'white'
def onStep():
    app.stepsTillNextCar += 1

    # Every 30 steps, tries to create a new car in the correct road.
    if (app.stepsTillNextCar >= 30):
        app.stepsTillNextCar = 0
        for line in lines:
            # If any of the lines are being hovered over, draw a new car.
            if (line.fill == 'white'):
                if (line.originalFill == 'fireBrick'):
                    drawCar(175, -30, 180, 'fireBrick')
                elif (line.originalFill == 'gold'):
                    drawCar(-30, 225, 90, 'gold')
                elif (line.originalFill == 'mediumSeaGreen'):
                    drawCar(-20, 15, 135, 'mediumSeaGreen')
                else:
                    drawCar(15, 420, 45, 'dodgerBlue')

    for car in cars:
        # Move each car 5 pixels in the direction that it is facing.
        newX, newY = getPointInDir(car.centerX, car.centerY, car.rotateAngle, 5)
        car.centerX = newX
        car.centerY = newY
        # Removes any cars that leave the canvas.
        if ((car.left >= 400) or (car.top >= 400)):
            cars.remove(car)

onMouseMove(100, 200)
app.paused = True


# -
app.background = 'mediumSeaGreen'
app.stepsTillNextCar = 0

# roads
Rect(150, 0, 100, 400, fill='dimGray')
Rect(0, 150, 400, 100, fill='dimGray')
Rect(-100, 150, 600, 100, fill='dimGray', rotateAngle=45)
Rect(-100, 150, 600, 100, fill='dimGray', rotateAngle=315)

lines = Group()
cars = Group()

def makeLines():
    # Adds four dashed lines.
    lines.add(
        Line(200, 0, 200, 400, fill='fireBrick', lineWidth=8, dashes=True),
        Line(0, 200, 400, 200, fill='gold', lineWidth=8, dashes=True),
        Line(0, 0, 400, 400, fill='mediumSeaGreen', lineWidth=8, dashes=True),
        Line(400, 0, 0, 400, fill='dodgerBlue', lineWidth=8, dashes=True)
        )

    # Sets the originalFill of each line so we can reset it later.
    originalFills = [ 'fireBrick', 'gold', 'mediumSeaGreen', 'dodgerBlue' ]
    for i in range(len(lines.children)):
        lines.children[i].originalFill = originalFills[i]

makeLines()

def drawCar(x, y, angle, color):
    car = Group(
        Rect(200, 200, 30, 60, fill=color, align='center'),
        Rect(200, 185, 34, 3, fill=color, align='center'),
        Rect(188, 172, 5, 4, fill='yellow', align='center'),
        Rect(213, 172, 5, 4, fill='yellow', align='center'),
        Rect(200, 220, 20, 8, fill='gray', align='center'),
        Rect(200, 190, 20, 12, fill='gray', align='center')
        )
    car.rotateAngle = angle
    car.centerX = x
    car.centerY = y
    cars.add(car)

def onMouseMove(mouseX, mouseY):
    # Resets each line back to its original color.
    for line in lines.children:
        line.fill = line.originalFill

    # If the mouse is on a line, set its fill to white.
    line = lines.hitTest(mouseX, mouseY)
    if (line != None):
        line.fill = 'white'
def onStep():
    app.stepsTillNextCar += 1

    # Every 30 steps, tries to create a new car in the correct road.
    if (app.stepsTillNextCar >= 30):
        app.stepsTillNextCar = 0
        for line in lines:
            # If any of the lines are being hovered over, draw a new car.
            if (line.fill == 'white'):
                if (line.originalFill == 'fireBrick'):
                    drawCar(175, -30, 180, 'fireBrick')
                elif (line.originalFill == 'gold'):
                    drawCar(-30, 225, 90, 'gold')
                elif (line.originalFill == 'mediumSeaGreen'):
                    drawCar(-20, 15, 135, 'mediumSeaGreen')
                else:
                    drawCar(15, 420, 45, 'dodgerBlue')

    for car in cars:
        # Move each car 5 pixels in the direction that it is facing.
        newX, newY = getPointInDir(car.centerX, car.centerY, car.rotateAngle, 5)
        car.centerX = newX
        car.centerY = newY
        # Removes any cars that leave the canvas.
        if ((car.left >= 400) or (car.top >= 400)):
            cars.remove(car)

onMouseMove(100, 200)
onSteps(30)
onMouseMove(100, 100)
onSteps(30)
onMouseMove(200, 100)
onSteps(30)
onMouseMove(100, 300)
onSteps(30)
app.paused = True


# -
app.background = 'mediumSeaGreen'
app.stepsTillNextCar = 0

# roads
Rect(150, 0, 100, 400, fill='dimGray')
Rect(0, 150, 400, 100, fill='dimGray')
Rect(-100, 150, 600, 100, fill='dimGray', rotateAngle=45)
Rect(-100, 150, 600, 100, fill='dimGray', rotateAngle=315)

lines = Group()
cars = Group()

def makeLines():
    # Adds four dashed lines.
    lines.add(
        Line(200, 0, 200, 400, fill='fireBrick', lineWidth=8, dashes=True),
        Line(0, 200, 400, 200, fill='gold', lineWidth=8, dashes=True),
        Line(0, 0, 400, 400, fill='mediumSeaGreen', lineWidth=8, dashes=True),
        Line(400, 0, 0, 400, fill='dodgerBlue', lineWidth=8, dashes=True)
        )

    # Sets the originalFill of each line so we can reset it later.
    originalFills = [ 'fireBrick', 'gold', 'mediumSeaGreen', 'dodgerBlue' ]
    for i in range(len(lines.children)):
        lines.children[i].originalFill = originalFills[i]

makeLines()

def drawCar(x, y, angle, color):
    car = Group(
        Rect(200, 200, 30, 60, fill=color, align='center'),
        Rect(200, 185, 34, 3, fill=color, align='center'),
        Rect(188, 172, 5, 4, fill='yellow', align='center'),
        Rect(213, 172, 5, 4, fill='yellow', align='center'),
        Rect(200, 220, 20, 8, fill='gray', align='center'),
        Rect(200, 190, 20, 12, fill='gray', align='center')
        )
    car.rotateAngle = angle
    car.centerX = x
    car.centerY = y
    cars.add(car)

def onMouseMove(mouseX, mouseY):
    # Resets each line back to its original color.
    for line in lines.children:
        line.fill = line.originalFill

    # If the mouse is on a line, set its fill to white.
    line = lines.hitTest(mouseX, mouseY)
    if (line != None):
        line.fill = 'white'
def onStep():
    app.stepsTillNextCar += 1

    # Every 30 steps, tries to create a new car in the correct road.
    if (app.stepsTillNextCar >= 30):
        app.stepsTillNextCar = 0
        for line in lines:
            # If any of the lines are being hovered over, draw a new car.
            if (line.fill == 'white'):
                if (line.originalFill == 'fireBrick'):
                    drawCar(175, -30, 180, 'fireBrick')
                elif (line.originalFill == 'gold'):
                    drawCar(-30, 225, 90, 'gold')
                elif (line.originalFill == 'mediumSeaGreen'):
                    drawCar(-20, 15, 135, 'mediumSeaGreen')
                else:
                    drawCar(15, 420, 45, 'dodgerBlue')

    for car in cars:
        # Move each car 5 pixels in the direction that it is facing.
        newX, newY = getPointInDir(car.centerX, car.centerY, car.rotateAngle, 5)
        car.centerX = newX
        car.centerY = newY
        # Removes any cars that leave the canvas.
        if ((car.left >= 400) or (car.top >= 400)):
            cars.remove(car)

onMouseMove(275, 125)
app.paused = True

