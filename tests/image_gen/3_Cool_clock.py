app.background = 'whiteSmoke'

app.expectedTime = 5
app.actualTime = 0

# clock background
Label('How good are you at guessing time?', 200, 35, size=20, bold=True)
bottomText = Label('Press space after ' + str(app.expectedTime) + ' s',
                   200, 370, size=18)
Star(200, 200, 140, 4, fill='maroon')
Star(200, 200, 130, 8, fill='goldenrod', roundness=30, rotateAngle=23)

# clock body
clock = Group(
    Circle(200, 200, 100, fill=gradient('peru', 'saddleBrown'),
           border='saddleBrown'),
    Circle(200, 200, 90, fill='white', border='black', borderWidth=5),
    Circle(200, 200, 70, fill='cornSilk'),
    Circle(200, 200, 3),
    Line(200, 200, 200, 150, arrowEnd=True)
    )

def drawTickMarks():
    # Draws the tick marks around the clock.
    for index in range(12):
        angle = 30 * (index + 1)
        x1, y1 = getPointInDir(200, 200, angle, 75)
        x2, y2 = getPointInDir(200, 200, angle, 85)
        Line(x1, y1, x2, y2)

drawTickMarks()

def calculateDifference():
    # Divide app.actualTime by the stepsPerSecond to get the time in seconds.
    # Subtract the actual time from the expected time to get the difference.
    app.actualTime = app.actualTime // app.stepsPerSecond
    return abs(app.expectedTime - app.actualTime)
def onKeyPress(key):
    if (key == 'space'):
        # Get the difference between the actual and expected times.
        difference = calculateDifference()
        if (difference == 0):
            bottomText.value = 'WOW! Right on'
        else:
            bottomText.value = 'You were off by ' + str(difference) + ' s'

        app.stop()

def onStep():
    # Moves the hand of the clock and adds to the time.
    clock.rotateAngle += 2
    app.actualTime += 1

onSteps(250)
onKeyPress('space')


# -
app.background = 'whiteSmoke'

app.expectedTime = 5
app.actualTime = 0

# clock background
Label('How good are you at guessing time?', 200, 35, size=20, bold=True)
bottomText = Label('Press space after ' + str(app.expectedTime) + ' s',
                   200, 370, size=18)
Star(200, 200, 140, 4, fill='maroon')
Star(200, 200, 130, 8, fill='goldenrod', roundness=30, rotateAngle=23)

# clock body
clock = Group(
    Circle(200, 200, 100, fill=gradient('peru', 'saddleBrown'),
           border='saddleBrown'),
    Circle(200, 200, 90, fill='white', border='black', borderWidth=5),
    Circle(200, 200, 70, fill='cornSilk'),
    Circle(200, 200, 3),
    Line(200, 200, 200, 150, arrowEnd=True)
    )

def drawTickMarks():
    # Draws the tick marks around the clock.
    for index in range(12):
        angle = 30 * (index + 1)
        x1, y1 = getPointInDir(200, 200, angle, 75)
        x2, y2 = getPointInDir(200, 200, angle, 85)
        Line(x1, y1, x2, y2)

drawTickMarks()

def calculateDifference():
    # Divide app.actualTime by the stepsPerSecond to get the time in seconds.
    # Subtract the actual time from the expected time to get the difference.
    app.actualTime = app.actualTime // app.stepsPerSecond
    return abs(app.expectedTime - app.actualTime)
def onKeyPress(key):
    if (key == 'space'):
        # Get the difference between the actual and expected times.
        difference = calculateDifference()
        if (difference == 0):
            bottomText.value = 'WOW! Right on'
        else:
            bottomText.value = 'You were off by ' + str(difference) + ' s'

        app.stop()

def onStep():
    # Moves the hand of the clock and adds to the time.
    clock.rotateAngle += 2
    app.actualTime += 1

onSteps(30)
onKeyPress('space')


# -
app.background = 'whiteSmoke'

app.expectedTime = 5
app.actualTime = 0

# clock background
Label('How good are you at guessing time?', 200, 35, size=20, bold=True)
bottomText = Label('Press space after ' + str(app.expectedTime) + ' s',
                   200, 370, size=18)
Star(200, 200, 140, 4, fill='maroon')
Star(200, 200, 130, 8, fill='goldenrod', roundness=30, rotateAngle=23)

# clock body
clock = Group(
    Circle(200, 200, 100, fill=gradient('peru', 'saddleBrown'),
           border='saddleBrown'),
    Circle(200, 200, 90, fill='white', border='black', borderWidth=5),
    Circle(200, 200, 70, fill='cornSilk'),
    Circle(200, 200, 3),
    Line(200, 200, 200, 150, arrowEnd=True)
    )

def drawTickMarks():
    # Draws the tick marks around the clock.
    for index in range(12):
        angle = 30 * (index + 1)
        x1, y1 = getPointInDir(200, 200, angle, 75)
        x2, y2 = getPointInDir(200, 200, angle, 85)
        Line(x1, y1, x2, y2)

drawTickMarks()

def calculateDifference():
    # Divide app.actualTime by the stepsPerSecond to get the time in seconds.
    # Subtract the actual time from the expected time to get the difference.
    app.actualTime = app.actualTime // app.stepsPerSecond
    return abs(app.expectedTime - app.actualTime)
def onKeyPress(key):
    if (key == 'space'):
        # Get the difference between the actual and expected times.
        difference = calculateDifference()
        if (difference == 0):
            bottomText.value = 'WOW! Right on'
        else:
            bottomText.value = 'You were off by ' + str(difference) + ' s'

        app.stop()

def onStep():
    # Moves the hand of the clock and adds to the time.
    clock.rotateAngle += 2
    app.actualTime += 1

onSteps(150)
onKeyPress('space')

