app.background = gradient('azure', 'lightBlue', 'blue')

# face and body
Circle(200, 135, 25)
Line(200, 160, 200, 240)
Label(')', 203, 145, fill='white', size=20, rotateAngle=90, bold=True)
Circle(190, 130, 3, fill='white')
Circle(210, 130, 3, fill='white')

# upper arms
leftArm = Line(200, 185, 150, 175)
rightArm = Line(200, 185, 250, 175)

# legs
Line(200, 240, 230, 300)
Line(200, 240, 170, 300)

def toggleLeftArm():
    # Move the left arm down if currently up, up if down.
    if (leftArm.y2 == 125):
        leftArm.y2 = 175
    else:
        leftArm.y2 = 125

def toggleRightArm():
    # Move the right arm down if currently up, up if down.
    if (rightArm.y2 == 125):
        rightArm.y2 = 175
    else:
        rightArm.y2 = 125

def onKeyPress(key):
    # On left and right key press, call the corresponding helper function.
    if (key == 'left'):
        toggleLeftArm()
    elif (key == 'right'):
        toggleRightArm()

onKeyPress('left')
onKeyPress('left')
onKeyPress('left')
onKeyPress('left')
onKeyPress('left')


# -
app.background = gradient('azure', 'lightBlue', 'blue')

# face and body
Circle(200, 135, 25)
Line(200, 160, 200, 240)
Label(')', 203, 145, fill='white', size=20, rotateAngle=90, bold=True)
Circle(190, 130, 3, fill='white')
Circle(210, 130, 3, fill='white')

# upper arms
leftArm = Line(200, 185, 150, 175)
rightArm = Line(200, 185, 250, 175)

# legs
Line(200, 240, 230, 300)
Line(200, 240, 170, 300)

def toggleLeftArm():
    # Move the left arm down if currently up, up if down.
    if (leftArm.y2 == 125):
        leftArm.y2 = 175
    else:
        leftArm.y2 = 125

def toggleRightArm():
    # Move the right arm down if currently up, up if down.
    if (rightArm.y2 == 125):
        rightArm.y2 = 175
    else:
        rightArm.y2 = 125

def onKeyPress(key):
    # On left and right key press, call the corresponding helper function.
    if (key == 'left'):
        toggleLeftArm()
    elif (key == 'right'):
        toggleRightArm()

onKeyPress('right')


# -
app.background = gradient('azure', 'lightBlue', 'blue')

# face and body
Circle(200, 135, 25)
Line(200, 160, 200, 240)
Label(')', 203, 145, fill='white', size=20, rotateAngle=90, bold=True)
Circle(190, 130, 3, fill='white')
Circle(210, 130, 3, fill='white')

# upper arms
leftArm = Line(200, 185, 150, 175)
rightArm = Line(200, 185, 250, 175)

# legs
Line(200, 240, 230, 300)
Line(200, 240, 170, 300)

def toggleLeftArm():
    # Move the left arm down if currently up, up if down.
    if (leftArm.y2 == 125):
        leftArm.y2 = 175
    else:
        leftArm.y2 = 125

def toggleRightArm():
    # Move the right arm down if currently up, up if down.
    if (rightArm.y2 == 125):
        rightArm.y2 = 175
    else:
        rightArm.y2 = 125

def onKeyPress(key):
    # On left and right key press, call the corresponding helper function.
    if (key == 'left'):
        toggleLeftArm()
    elif (key == 'right'):
        toggleRightArm()

onKeyPress('left')
onKeyPress('left')
onKeyPress('right')
onKeyPress('right')
onKeyPress('right')
onKeyPress('left')
onKeyPress('right')

