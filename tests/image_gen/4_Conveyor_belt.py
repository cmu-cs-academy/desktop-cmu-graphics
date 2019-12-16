app.background = gradient('steelBlue', 'lightSlateGray', start='top')
app.stepsPerSecond = 15

def createWheels(sideWheels, start):
    for i in range(6):
        sideWheels.add(
            Star(start + i * 20, 265, 10, 7, roundness=20),
            Circle(start + i * 20, 265, 6, fill='grey', border='black')
            )

# conveyor belts
Line(10, 290, 390, 290, lineWidth=30, dashes=(2, 40))
Rect(-10, 255, 420, 20, fill='grey', border='black')
rightWheels = Group()
leftWheels = Group()
createWheels(rightWheels, 292)
createWheels(leftWheels, 8)

leftDots = Group()
rightDots = Group()

# machine
Polygon(150, 135, 250, 135, 235, 100, 235, 0, 165, 0, 165, 100,
        fill=gradient('lightGrey', 'grey', start='left-top'))
Line(165, 100, 235, 100, fill='grey')
Rect(116, 135, 168, 200, fill=gradient('lightGrey', 'grey', start='left-top'))
Rect(135, 265, 65, 60, fill=gradient('lightGrey', 'dimGrey', start='left-top'))
Oval(240, 260, 60, 30, fill=gradient('lightGrey', 'dimGrey', start='left-top'))
Line(220, 300, 260, 300, fill=gradient('silver', 'dimGrey', start='left-top'),
     lineWidth=70, dashes=(10, 5))
Line(114, 200, 114, 280, fill='dimGrey', lineWidth=4)
Line(286, 200, 286, 280, fill='dimGrey', lineWidth=4)
Line(115, 330, 285, 330, fill='dimGrey', lineWidth=10)
Rect(135, 150, 130, 60, border='dimGrey')

arrow = Line(160, 190, 240, 190, fill='crimson')
direction = Label('Random', 200, 165, fill='crimson', size=20)

def onKeyPress(key):
    if (key == 'left'):
        arrow.arrowStart = True
    if (key == 'right'):
        arrow.arrowEnd = True

def onKeyRelease(key):
    if (key == 'left'):
        arrow.arrowStart = False
    if (key == 'right'):
        arrow.arrowEnd = False

def onStep():
    # Rotates the wheels of the belts.
    for wheel in leftWheels:
        wheel.rotateAngle -= 5
    for wheel in rightWheels:
        wheel.rotateAngle += 5

    # Add dots based on which direction the arrow points. Also change
    # the direction label!
    if (arrow.arrowStart == True):
        leftDots.add(
            Circle(120, 250, 5, fill='springGreen')
            )
        direction.value = 'Left'
    elif (arrow.arrowEnd == True):
        rightDots.add(
            Circle(280, 250, 5, fill='deepSkyBlue')
            )
        direction.value = 'Right'
    # If the arrow is not pointing in any direction, then randomly choose
    # left or right.
    else:
        chance = randrange(0, 2)
        if (chance == 0):
            leftDots.add(
                Circle(120, 250, 5, fill='springGreen')
                )
        else:
            rightDots.add(
                Circle(280, 250, 5, fill='deepSkyBlue')
                )
        direction.value = 'Random'
    # Move the dots in their respective directions and remove them
    # once they are off-screen.
    for dot in rightDots:
        dot.centerX += 10
        if (dot.left > 400):
            rightDots.remove(dot)
    for dot in leftDots:
        dot.centerX -= 10
        if (dot.left < 0):
            leftDots.remove(dot)

onKeyPress('left')
onStep()
app.paused = True


# -
app.background = gradient('steelBlue', 'lightSlateGray', start='top')
app.stepsPerSecond = 15

def createWheels(sideWheels, start):
    for i in range(6):
        sideWheels.add(
            Star(start + i * 20, 265, 10, 7, roundness=20),
            Circle(start + i * 20, 265, 6, fill='grey', border='black')
            )

# conveyor belts
Line(10, 290, 390, 290, lineWidth=30, dashes=(2, 40))
Rect(-10, 255, 420, 20, fill='grey', border='black')
rightWheels = Group()
leftWheels = Group()
createWheels(rightWheels, 292)
createWheels(leftWheels, 8)

leftDots = Group()
rightDots = Group()

# machine
Polygon(150, 135, 250, 135, 235, 100, 235, 0, 165, 0, 165, 100,
        fill=gradient('lightGrey', 'grey', start='left-top'))
Line(165, 100, 235, 100, fill='grey')
Rect(116, 135, 168, 200, fill=gradient('lightGrey', 'grey', start='left-top'))
Rect(135, 265, 65, 60, fill=gradient('lightGrey', 'dimGrey', start='left-top'))
Oval(240, 260, 60, 30, fill=gradient('lightGrey', 'dimGrey', start='left-top'))
Line(220, 300, 260, 300, fill=gradient('silver', 'dimGrey', start='left-top'),
     lineWidth=70, dashes=(10, 5))
Line(114, 200, 114, 280, fill='dimGrey', lineWidth=4)
Line(286, 200, 286, 280, fill='dimGrey', lineWidth=4)
Line(115, 330, 285, 330, fill='dimGrey', lineWidth=10)
Rect(135, 150, 130, 60, border='dimGrey')

arrow = Line(160, 190, 240, 190, fill='crimson')
direction = Label('Random', 200, 165, fill='crimson', size=20)

def onKeyPress(key):
    if (key == 'left'):
        arrow.arrowStart = True
    if (key == 'right'):
        arrow.arrowEnd = True

def onKeyRelease(key):
    if (key == 'left'):
        arrow.arrowStart = False
    if (key == 'right'):
        arrow.arrowEnd = False

def onStep():
    # Rotates the wheels of the belts.
    for wheel in leftWheels:
        wheel.rotateAngle -= 5
    for wheel in rightWheels:
        wheel.rotateAngle += 5

    # Add dots based on which direction the arrow points. Also change
    # the direction label!
    if (arrow.arrowStart == True):
        leftDots.add(
            Circle(120, 250, 5, fill='springGreen')
            )
        direction.value = 'Left'
    elif (arrow.arrowEnd == True):
        rightDots.add(
            Circle(280, 250, 5, fill='deepSkyBlue')
            )
        direction.value = 'Right'
    # If the arrow is not pointing in any direction, then randomly choose
    # left or right.
    else:
        chance = randrange(0, 2)
        if (chance == 0):
            leftDots.add(
                Circle(120, 250, 5, fill='springGreen')
                )
        else:
            rightDots.add(
                Circle(280, 250, 5, fill='deepSkyBlue')
                )
        direction.value = 'Random'
    # Move the dots in their respective directions and remove them
    # once they are off-screen.
    for dot in rightDots:
        dot.centerX += 10
        if (dot.left > 400):
            rightDots.remove(dot)
    for dot in leftDots:
        dot.centerX -= 10
        if (dot.left < 0):
            leftDots.remove(dot)

onSteps(10)
app.paused = True


# -
app.background = gradient('steelBlue', 'lightSlateGray', start='top')
app.stepsPerSecond = 15

def createWheels(sideWheels, start):
    for i in range(6):
        sideWheels.add(
            Star(start + i * 20, 265, 10, 7, roundness=20),
            Circle(start + i * 20, 265, 6, fill='grey', border='black')
            )

# conveyor belts
Line(10, 290, 390, 290, lineWidth=30, dashes=(2, 40))
Rect(-10, 255, 420, 20, fill='grey', border='black')
rightWheels = Group()
leftWheels = Group()
createWheels(rightWheels, 292)
createWheels(leftWheels, 8)

leftDots = Group()
rightDots = Group()

# machine
Polygon(150, 135, 250, 135, 235, 100, 235, 0, 165, 0, 165, 100,
        fill=gradient('lightGrey', 'grey', start='left-top'))
Line(165, 100, 235, 100, fill='grey')
Rect(116, 135, 168, 200, fill=gradient('lightGrey', 'grey', start='left-top'))
Rect(135, 265, 65, 60, fill=gradient('lightGrey', 'dimGrey', start='left-top'))
Oval(240, 260, 60, 30, fill=gradient('lightGrey', 'dimGrey', start='left-top'))
Line(220, 300, 260, 300, fill=gradient('silver', 'dimGrey', start='left-top'),
     lineWidth=70, dashes=(10, 5))
Line(114, 200, 114, 280, fill='dimGrey', lineWidth=4)
Line(286, 200, 286, 280, fill='dimGrey', lineWidth=4)
Line(115, 330, 285, 330, fill='dimGrey', lineWidth=10)
Rect(135, 150, 130, 60, border='dimGrey')

arrow = Line(160, 190, 240, 190, fill='crimson')
direction = Label('Random', 200, 165, fill='crimson', size=20)

def onKeyPress(key):
    if (key == 'left'):
        arrow.arrowStart = True
    if (key == 'right'):
        arrow.arrowEnd = True

def onKeyRelease(key):
    if (key == 'left'):
        arrow.arrowStart = False
    if (key == 'right'):
        arrow.arrowEnd = False

def onStep():
    # Rotates the wheels of the belts.
    for wheel in leftWheels:
        wheel.rotateAngle -= 5
    for wheel in rightWheels:
        wheel.rotateAngle += 5

    # Add dots based on which direction the arrow points. Also change
    # the direction label!
    if (arrow.arrowStart == True):
        leftDots.add(
            Circle(120, 250, 5, fill='springGreen')
            )
        direction.value = 'Left'
    elif (arrow.arrowEnd == True):
        rightDots.add(
            Circle(280, 250, 5, fill='deepSkyBlue')
            )
        direction.value = 'Right'
    # If the arrow is not pointing in any direction, then randomly choose
    # left or right.
    else:
        chance = randrange(0, 2)
        if (chance == 0):
            leftDots.add(
                Circle(120, 250, 5, fill='springGreen')
                )
        else:
            rightDots.add(
                Circle(280, 250, 5, fill='deepSkyBlue')
                )
        direction.value = 'Random'
    # Move the dots in their respective directions and remove them
    # once they are off-screen.
    for dot in rightDots:
        dot.centerX += 10
        if (dot.left > 400):
            rightDots.remove(dot)
    for dot in leftDots:
        dot.centerX -= 10
        if (dot.left < 0):
            leftDots.remove(dot)

onKeyPress('right')
onSteps(5)
app.paused = True

