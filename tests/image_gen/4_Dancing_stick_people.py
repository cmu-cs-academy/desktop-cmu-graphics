app.background = gradient('lightBlue', 'royalBlue')

sticks = Group()
sticks.toBack()

sticks.rightArmsUp = False
sticks.leftArmsUp = False

def drawStick(headX, headY):
    stick = Group()
    stick.leftArm = Line(headX, headY + 25, headX - 15, headY + 35)
    stick.rightArm = Line(headX, headY + 25, headX + 15, headY + 35)
    stick.add(
        # head
        Circle(headX, headY, 15),

        stick.leftArm,
        stick.rightArm,

        # body
        Line(headX, headY, headX, headY + 50),

        # legs
        Line(headX, headY + 50, headX - 10, headY + 75),
        Line(headX, headY + 50, headX + 10, headY + 75)
        )

    # The stick was created with its arms down, so we have to raise
    # them now if needed.
    if (sticks.rightArmsUp == True):
        stick.rightArm.y2 -= 20
    if (sticks.leftArmsUp == True):
        stick.leftArm.y2 -= 20
    sticks.add(stick)

def onMousePress(mouseX, mouseY):
    drawStick(mouseX, mouseY)

def toggleLeftArms():
    # Depending on if the left arm is up or down, changes the dy value.
    if (sticks.leftArmsUp == True):
        dy = 20
        sticks.leftArmsUp = False
    else:
        dy = -20
        sticks.leftArmsUp = True

    # For each stickman, moves the left arm by dy.
    for stick in sticks.children:
        stick.leftArm.y2 += dy

def toggleRightArms():
    # If the right arm is up, set dy to 20 and rightArmsUp to False.
    # Otherwise, set dy to -20 and rightArmsUp to True.
    if (sticks.rightArmsUp == True):
        dy = 20
        sticks.rightArmsUp = False
    else:
        dy = -20
        sticks.rightArmsUp = True

    # For each stickman, move the right arm by dy.
    for stick in sticks.children:
        stick.rightArm.y2 += dy

def onKeyPress(key):
    if (key == 'left'):
        toggleLeftArms()
    elif (key == 'right'):
        toggleRightArms()

onMousePress(200, 200)
onKeyPress('left')


# -
app.background = gradient('lightBlue', 'royalBlue')

sticks = Group()
sticks.toBack()

sticks.rightArmsUp = False
sticks.leftArmsUp = False

def drawStick(headX, headY):
    stick = Group()
    stick.leftArm = Line(headX, headY + 25, headX - 15, headY + 35)
    stick.rightArm = Line(headX, headY + 25, headX + 15, headY + 35)
    stick.add(
        # head
        Circle(headX, headY, 15),

        stick.leftArm,
        stick.rightArm,

        # body
        Line(headX, headY, headX, headY + 50),

        # legs
        Line(headX, headY + 50, headX - 10, headY + 75),
        Line(headX, headY + 50, headX + 10, headY + 75)
        )

    # The stick was created with its arms down, so we have to raise
    # them now if needed.
    if (sticks.rightArmsUp == True):
        stick.rightArm.y2 -= 20
    if (sticks.leftArmsUp == True):
        stick.leftArm.y2 -= 20
    sticks.add(stick)

def onMousePress(mouseX, mouseY):
    drawStick(mouseX, mouseY)

def toggleLeftArms():
    # Depending on if the left arm is up or down, changes the dy value.
    if (sticks.leftArmsUp == True):
        dy = 20
        sticks.leftArmsUp = False
    else:
        dy = -20
        sticks.leftArmsUp = True

    # For each stickman, moves the left arm by dy.
    for stick in sticks.children:
        stick.leftArm.y2 += dy

def toggleRightArms():
    # If the right arm is up, set dy to 20 and rightArmsUp to False.
    # Otherwise, set dy to -20 and rightArmsUp to True.
    if (sticks.rightArmsUp == True):
        dy = 20
        sticks.rightArmsUp = False
    else:
        dy = -20
        sticks.rightArmsUp = True

    # For each stickman, move the right arm by dy.
    for stick in sticks.children:
        stick.rightArm.y2 += dy

def onKeyPress(key):
    if (key == 'left'):
        toggleLeftArms()
    elif (key == 'right'):
        toggleRightArms()

onMousePress(100, 100)
onMousePress(300, 300)


# -
app.background = gradient('lightBlue', 'royalBlue')

sticks = Group()
sticks.toBack()

sticks.rightArmsUp = False
sticks.leftArmsUp = False

def drawStick(headX, headY):
    stick = Group()
    stick.leftArm = Line(headX, headY + 25, headX - 15, headY + 35)
    stick.rightArm = Line(headX, headY + 25, headX + 15, headY + 35)
    stick.add(
        # head
        Circle(headX, headY, 15),

        stick.leftArm,
        stick.rightArm,

        # body
        Line(headX, headY, headX, headY + 50),

        # legs
        Line(headX, headY + 50, headX - 10, headY + 75),
        Line(headX, headY + 50, headX + 10, headY + 75)
        )

    # The stick was created with its arms down, so we have to raise
    # them now if needed.
    if (sticks.rightArmsUp == True):
        stick.rightArm.y2 -= 20
    if (sticks.leftArmsUp == True):
        stick.leftArm.y2 -= 20
    sticks.add(stick)

def onMousePress(mouseX, mouseY):
    drawStick(mouseX, mouseY)

def toggleLeftArms():
    # Depending on if the left arm is up or down, changes the dy value.
    if (sticks.leftArmsUp == True):
        dy = 20
        sticks.leftArmsUp = False
    else:
        dy = -20
        sticks.leftArmsUp = True

    # For each stickman, moves the left arm by dy.
    for stick in sticks.children:
        stick.leftArm.y2 += dy

def toggleRightArms():
    # If the right arm is up, set dy to 20 and rightArmsUp to False.
    # Otherwise, set dy to -20 and rightArmsUp to True.
    if (sticks.rightArmsUp == True):
        dy = 20
        sticks.rightArmsUp = False
    else:
        dy = -20
        sticks.rightArmsUp = True

    # For each stickman, move the right arm by dy.
    for stick in sticks.children:
        stick.rightArm.y2 += dy

def onKeyPress(key):
    if (key == 'left'):
        toggleLeftArms()
    elif (key == 'right'):
        toggleRightArms()

onMousePress(100, 100)
onKeyPress('left')
onMousePress(200, 200)
onKeyPress('right')
onMousePress(300, 300)
onKeyPress('left')

