app.background = gradient(rgb(150, 225, 175), rgb(95, 180, 155), start='top')

leftArm = Line(200, 190, 140, 100, fill=rgb(70, 75, 75), lineWidth=5)
rightArm = Line(200, 190, 260, 100, fill=rgb(70, 75, 75), lineWidth=5)
stickPerson = Group(
    Circle(200, 140, 30, fill=rgb(70, 75, 75)),
    Line(200, 170, 200, 275, fill=rgb(70, 75, 75), lineWidth=6),
    Line(200, 275, 150, 325, fill=rgb(70, 75, 75), lineWidth=5),
    Line(200, 275, 250, 325, fill=rgb(70, 75, 75), lineWidth=5),
    leftArm,
    rightArm
    )
stickPerson.bottom = 325

# pull up bar
Line(50, 100, 350, 100,
     fill=gradient('gainsboro', 'silver', 'gainsboro', start='top'), lineWidth=6)
Line(50, 100, 50, 400,
     fill=gradient('gainsboro', 'silver', 'gainsboro', start='top'), lineWidth=6)
Line(350, 100, 350, 400,
     fill=gradient('gainsboro', 'silver', 'gainsboro', start='top'), lineWidth=6)

pullUpCounter = Label(0, 100, 60, fill=rgb(70, 75, 75), size=25)

def onKeyPress(key):
    # Increase the number of pull-ups done.
    pullUpCounter.value += 1
    # Move the stickPerson group up.
    # Then change the left and right arm, so they are gripping the bar.
    stickPerson.bottom = 250
    leftArm.y2 = 100
    rightArm.y2 = 100
def onKeyRelease(key):
    # Move the stickPerson group down.
    # Then change the left and right arm, so they are gripping the bar.
    stickPerson.bottom = 325
    leftArm.y2 = 100
    rightArm.y2 = 100

onKeyPresses('a', 101)


# -
app.background = gradient(rgb(150, 225, 175), rgb(95, 180, 155), start='top')

leftArm = Line(200, 190, 140, 100, fill=rgb(70, 75, 75), lineWidth=5)
rightArm = Line(200, 190, 260, 100, fill=rgb(70, 75, 75), lineWidth=5)
stickPerson = Group(
    Circle(200, 140, 30, fill=rgb(70, 75, 75)),
    Line(200, 170, 200, 275, fill=rgb(70, 75, 75), lineWidth=6),
    Line(200, 275, 150, 325, fill=rgb(70, 75, 75), lineWidth=5),
    Line(200, 275, 250, 325, fill=rgb(70, 75, 75), lineWidth=5),
    leftArm,
    rightArm
    )
stickPerson.bottom = 325

# pull up bar
Line(50, 100, 350, 100,
     fill=gradient('gainsboro', 'silver', 'gainsboro', start='top'), lineWidth=6)
Line(50, 100, 50, 400,
     fill=gradient('gainsboro', 'silver', 'gainsboro', start='top'), lineWidth=6)
Line(350, 100, 350, 400,
     fill=gradient('gainsboro', 'silver', 'gainsboro', start='top'), lineWidth=6)

pullUpCounter = Label(0, 100, 60, fill=rgb(70, 75, 75), size=25)

def onKeyPress(key):
    # Increase the number of pull-ups done.
    pullUpCounter.value += 1
    # Move the stickPerson group up.
    # Then change the left and right arm, so they are gripping the bar.
    stickPerson.bottom = 250
    leftArm.y2 = 100
    rightArm.y2 = 100
def onKeyRelease(key):
    # Move the stickPerson group down.
    # Then change the left and right arm, so they are gripping the bar.
    stickPerson.bottom = 325
    leftArm.y2 = 100
    rightArm.y2 = 100

onKeyPress('a')
onKeyPress('s')
onKeyPress('d')


# -
app.background = gradient(rgb(150, 225, 175), rgb(95, 180, 155), start='top')

leftArm = Line(200, 190, 140, 100, fill=rgb(70, 75, 75), lineWidth=5)
rightArm = Line(200, 190, 260, 100, fill=rgb(70, 75, 75), lineWidth=5)
stickPerson = Group(
    Circle(200, 140, 30, fill=rgb(70, 75, 75)),
    Line(200, 170, 200, 275, fill=rgb(70, 75, 75), lineWidth=6),
    Line(200, 275, 150, 325, fill=rgb(70, 75, 75), lineWidth=5),
    Line(200, 275, 250, 325, fill=rgb(70, 75, 75), lineWidth=5),
    leftArm,
    rightArm
    )
stickPerson.bottom = 325

# pull up bar
Line(50, 100, 350, 100,
     fill=gradient('gainsboro', 'silver', 'gainsboro', start='top'), lineWidth=6)
Line(50, 100, 50, 400,
     fill=gradient('gainsboro', 'silver', 'gainsboro', start='top'), lineWidth=6)
Line(350, 100, 350, 400,
     fill=gradient('gainsboro', 'silver', 'gainsboro', start='top'), lineWidth=6)

pullUpCounter = Label(0, 100, 60, fill=rgb(70, 75, 75), size=25)

def onKeyPress(key):
    # Increase the number of pull-ups done.
    pullUpCounter.value += 1
    # Move the stickPerson group up.
    # Then change the left and right arm, so they are gripping the bar.
    stickPerson.bottom = 250
    leftArm.y2 = 100
    rightArm.y2 = 100
def onKeyRelease(key):
    # Move the stickPerson group down.
    # Then change the left and right arm, so they are gripping the bar.
    stickPerson.bottom = 325
    leftArm.y2 = 100
    rightArm.y2 = 100

onKeyPress('s')
onKeyRelease('s')
onKeyPress('w')
onKeyRelease('w')

