app.background = gradient('azure', 'lightBlue', 'blue')
app.stepsPerSecond = 5
app.counter = 0

# head and body
Circle(200, 110, 25)
Line(200, 135, 200, 225)

# upper arms
leftArm = Line(200, 150, 150, 175)
rightArm = Line(200, 150, 250, 125)

# legs
Line(200, 225, 250, 300)
Line(200, 225, 150, 300)

def toggleLeftArm():
    # Move the left arm down if currently up, up if currently down.
    if (leftArm.y2 == 125):
        leftArm.y2 = 175
    else:
        leftArm.y2 = 125

def toggleRightArm():
    # Move the right arm down if currently up, up if currently down.
    if (rightArm.y2 == 125):
        rightArm.y2 = 175
    else:
        rightArm.y2 = 125

def onStep():
    app.counter += 1

    # When app.counter is 1, call the left arm helper function.
    # When app.counter is 2, call the right arm helper function. Also, set
    # app.counter to be 0.
    if (app.counter == 1):
        toggleLeftArm()
    if (app.counter == 2):
        toggleRightArm()
        app.counter = 0

onSteps(4)
app.paused = True


# -
app.background = gradient('azure', 'lightBlue', 'blue')
app.stepsPerSecond = 5
app.counter = 0

# head and body
Circle(200, 110, 25)
Line(200, 135, 200, 225)

# upper arms
leftArm = Line(200, 150, 150, 175)
rightArm = Line(200, 150, 250, 125)

# legs
Line(200, 225, 250, 300)
Line(200, 225, 150, 300)

def toggleLeftArm():
    # Move the left arm down if currently up, up if currently down.
    if (leftArm.y2 == 125):
        leftArm.y2 = 175
    else:
        leftArm.y2 = 125

def toggleRightArm():
    # Move the right arm down if currently up, up if currently down.
    if (rightArm.y2 == 125):
        rightArm.y2 = 175
    else:
        rightArm.y2 = 125

def onStep():
    app.counter += 1

    # When app.counter is 1, call the left arm helper function.
    # When app.counter is 2, call the right arm helper function. Also, set
    # app.counter to be 0.
    if (app.counter == 1):
        toggleLeftArm()
    if (app.counter == 2):
        toggleRightArm()
        app.counter = 0

onSteps(3)
app.paused = True


# -
app.background = gradient('azure', 'lightBlue', 'blue')
app.stepsPerSecond = 5
app.counter = 0

# head and body
Circle(200, 110, 25)
Line(200, 135, 200, 225)

# upper arms
leftArm = Line(200, 150, 150, 175)
rightArm = Line(200, 150, 250, 125)

# legs
Line(200, 225, 250, 300)
Line(200, 225, 150, 300)

def toggleLeftArm():
    # Move the left arm down if currently up, up if currently down.
    if (leftArm.y2 == 125):
        leftArm.y2 = 175
    else:
        leftArm.y2 = 125

def toggleRightArm():
    # Move the right arm down if currently up, up if currently down.
    if (rightArm.y2 == 125):
        rightArm.y2 = 175
    else:
        rightArm.y2 = 125

def onStep():
    app.counter += 1

    # When app.counter is 1, call the left arm helper function.
    # When app.counter is 2, call the right arm helper function. Also, set
    # app.counter to be 0.
    if (app.counter == 1):
        toggleLeftArm()
    if (app.counter == 2):
        toggleRightArm()
        app.counter = 0

onStep()
app.paused = True

