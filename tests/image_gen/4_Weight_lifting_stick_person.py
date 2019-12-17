app.background = gradient(rgb(230, 120, 70), rgb(225, 215, 135), start='top')

# stick figure
Circle(200, 200, 30, fill=rgb(70, 75, 75))
Line(200, 200, 200, 300, fill=rgb(70, 75, 75), lineWidth=6)
Line(200, 300, 150, 350, fill=rgb(70, 75, 75), lineWidth=5)
Line(200, 300, 250, 350, fill=rgb(70, 75, 75), lineWidth=5)
leftArm = Line(200, 250, 150, 300, fill=rgb(70, 75, 75), lineWidth=5)
rightArm = Line(200, 250, 250, 300, fill=rgb(70, 75, 75), lineWidth=5)

# Define the weight (with a line and 4 rectangles).
weight = Group(
    Line(100, 300, 300, 300, lineWidth=6,
         fill=gradient('gainsboro', rgb(195, 195, 200), start='bottom')),
    Rect(85, 300, 15, 60, fill=rgb(70, 75, 75), border=rgb(195, 195, 200),
         align='center'),
    Rect(100, 300, 15, 80, fill=rgb(70, 75, 75), border=rgb(195, 195, 200),
         align='center'),
    Rect(315, 300, 15, 60, fill=rgb(70, 75, 75), border=rgb(195, 195, 200),
         align='center'),
    Rect(300, 300, 15, 80, fill=rgb(70, 75, 75), border=rgb(195, 195, 200),
         align='center')
    )
liftedCounter = Label(0, 200, 100, fill=rgb(70, 75, 75), size=25)

def onKeyPress(key):
    # Move the weight up.
    weight.centerY = 140
    # Move the left and right arms to lift the weight.
    leftArm.y2 = 140
    rightArm.y2 = 140
    liftedCounter.value += 1

def onKeyRelease(key):
    # Move the arms and weight back to their original positions.
    leftArm.y2 = 300
    rightArm.y2 = 300
    weight.centerY = 300

onKeyPress('space')
onKeyRelease('space')
onKeyPress('space')


# -
app.background = gradient(rgb(230, 120, 70), rgb(225, 215, 135), start='top')

# stick figure
Circle(200, 200, 30, fill=rgb(70, 75, 75))
Line(200, 200, 200, 300, fill=rgb(70, 75, 75), lineWidth=6)
Line(200, 300, 150, 350, fill=rgb(70, 75, 75), lineWidth=5)
Line(200, 300, 250, 350, fill=rgb(70, 75, 75), lineWidth=5)
leftArm = Line(200, 250, 150, 300, fill=rgb(70, 75, 75), lineWidth=5)
rightArm = Line(200, 250, 250, 300, fill=rgb(70, 75, 75), lineWidth=5)

# Define the weight (with a line and 4 rectangles).
weight = Group(
    Line(100, 300, 300, 300, lineWidth=6,
         fill=gradient('gainsboro', rgb(195, 195, 200), start='bottom')),
    Rect(85, 300, 15, 60, fill=rgb(70, 75, 75), border=rgb(195, 195, 200),
         align='center'),
    Rect(100, 300, 15, 80, fill=rgb(70, 75, 75), border=rgb(195, 195, 200),
         align='center'),
    Rect(315, 300, 15, 60, fill=rgb(70, 75, 75), border=rgb(195, 195, 200),
         align='center'),
    Rect(300, 300, 15, 80, fill=rgb(70, 75, 75), border=rgb(195, 195, 200),
         align='center')
    )
liftedCounter = Label(0, 200, 100, fill=rgb(70, 75, 75), size=25)

def onKeyPress(key):
    # Move the weight up.
    weight.centerY = 140
    # Move the left and right arms to lift the weight.
    leftArm.y2 = 140
    rightArm.y2 = 140
    liftedCounter.value += 1

def onKeyRelease(key):
    # Move the arms and weight back to their original positions.
    leftArm.y2 = 300
    rightArm.y2 = 300
    weight.centerY = 300

onKeyPress('space')
onKeyPress('space')
onKeyRelease('space')


# -
app.background = gradient(rgb(230, 120, 70), rgb(225, 215, 135), start='top')

# stick figure
Circle(200, 200, 30, fill=rgb(70, 75, 75))
Line(200, 200, 200, 300, fill=rgb(70, 75, 75), lineWidth=6)
Line(200, 300, 150, 350, fill=rgb(70, 75, 75), lineWidth=5)
Line(200, 300, 250, 350, fill=rgb(70, 75, 75), lineWidth=5)
leftArm = Line(200, 250, 150, 300, fill=rgb(70, 75, 75), lineWidth=5)
rightArm = Line(200, 250, 250, 300, fill=rgb(70, 75, 75), lineWidth=5)

# Define the weight (with a line and 4 rectangles).
weight = Group(
    Line(100, 300, 300, 300, lineWidth=6,
         fill=gradient('gainsboro', rgb(195, 195, 200), start='bottom')),
    Rect(85, 300, 15, 60, fill=rgb(70, 75, 75), border=rgb(195, 195, 200),
         align='center'),
    Rect(100, 300, 15, 80, fill=rgb(70, 75, 75), border=rgb(195, 195, 200),
         align='center'),
    Rect(315, 300, 15, 60, fill=rgb(70, 75, 75), border=rgb(195, 195, 200),
         align='center'),
    Rect(300, 300, 15, 80, fill=rgb(70, 75, 75), border=rgb(195, 195, 200),
         align='center')
    )
liftedCounter = Label(0, 200, 100, fill=rgb(70, 75, 75), size=25)

def onKeyPress(key):
    # Move the weight up.
    weight.centerY = 140
    # Move the left and right arms to lift the weight.
    leftArm.y2 = 140
    rightArm.y2 = 140
    liftedCounter.value += 1

def onKeyRelease(key):
    # Move the arms and weight back to their original positions.
    leftArm.y2 = 300
    rightArm.y2 = 300
    weight.centerY = 300

onKeyPress('space')
onKeyPress('space')
onKeyRelease('space')

