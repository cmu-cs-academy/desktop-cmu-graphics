app.background = gradient('orange', 'red', 'orange')

steps = Group(
    Polygon(10, 345, 70, 320, 95, 375, 15, 390, fill='white'),
    Polygon(160, 360, 195, 330, 165, 320, fill='white'),
    Polygon(25, 240, 70, 260, 55, 220, fill='white'),
    Polygon(135, 155, 170, 130, 200, 175, fill='white'),
    Polygon(75, 60, 40, 75, 75, 100, fill='white'),
    Polygon(280, 125, 230, 90, 290, 95, fill='white'),
    Polygon(270, 280, 295, 310, 350, 270, fill='white'),
    Polygon(320, 165, 345, 200, 370, 155, fill='white')
    )

goal = Polygon(320, 15, 390, 5, 395, 50, 340, 70, fill='limeGreen')

Label('# of Steps', 250, 350, size=15)
numSteps = Label(0, 250, 370, size=25)

Label('Next foot:', 350, 350, size=15)
nextFootLabel = Label('R', 350, 370, size=25)

leftFoot = Group(
    Circle(30, 350, 8),
    Rect(30, 360, 16, 20, align='center'),
    Circle(30, 375, 8),
    Rect(30, 370, 16, 5, fill='white', align='top'),
    Label('L', 30, 355, fill='white')
    )

rightFoot = Group(
    Circle(60, 350, 8),
    Rect(60, 360, 16, 20, align='center'),
    Circle(60, 375, 8),
    Rect(60, 370, 16, 5, fill='white', align='top'),
    Label('R', 60, 355, fill='white')
    )

def winGame():
    Rect(200, 225, 200, 100, fill='lightGreen', align='center')
    Label('You win!', 200, 225, size=50)
    app.stop()

def loseGame(reason):
    Rect(200, 225, 200, 100, fill='pink', align='center')
    Label(reason, 200, 200, size=30)
    Label('You lose!', 200, 250, size=30)
    app.stop()

def onMousePress(mouseX, mouseY):
    # Then take the step.
    if (nextFootLabel.value == 'L'):
        leftFoot.centerX = mouseX
        leftFoot.centerY = mouseY
        nextFootLabel.value = 'R'
    else:
        rightFoot.centerX = mouseX
        rightFoot.centerY = mouseY
        nextFootLabel.value = 'L'

    # After a step, increment the number of steps taken so far.
    numSteps.value += 1

    # Finally, check for win or lose. A step loses if any of the following occur:
    # 1 - The left foot centerX is bigger than the right foot centerX.
    # 2 - The distance between the feet's centerX or centerY is bigger than 175.
    # 3 - If the place clicked is not in the steps group or the goal.
    footDistanceX = rightFoot.centerX - leftFoot.centerX
    footDistanceY = rightFoot.centerY - leftFoot.centerY
    if (footDistanceX < 0):
        loseGame('Crossed feet!')
    elif ((footDistanceX > 175) or (footDistanceY > 175)):
        loseGame('Too far!')
    elif (goal.hits(mouseX, mouseY) == True):
        winGame()
    elif (steps.hits(mouseX, mouseY) == False):
        loseGame('Not a step!')

onMousePress(50, 350)
onMousePress(300, 290)


# -
app.background = gradient('orange', 'red', 'orange')

steps = Group(
    Polygon(10, 345, 70, 320, 95, 375, 15, 390, fill='white'),
    Polygon(160, 360, 195, 330, 165, 320, fill='white'),
    Polygon(25, 240, 70, 260, 55, 220, fill='white'),
    Polygon(135, 155, 170, 130, 200, 175, fill='white'),
    Polygon(75, 60, 40, 75, 75, 100, fill='white'),
    Polygon(280, 125, 230, 90, 290, 95, fill='white'),
    Polygon(270, 280, 295, 310, 350, 270, fill='white'),
    Polygon(320, 165, 345, 200, 370, 155, fill='white')
    )

goal = Polygon(320, 15, 390, 5, 395, 50, 340, 70, fill='limeGreen')

Label('# of Steps', 250, 350, size=15)
numSteps = Label(0, 250, 370, size=25)

Label('Next foot:', 350, 350, size=15)
nextFootLabel = Label('R', 350, 370, size=25)

leftFoot = Group(
    Circle(30, 350, 8),
    Rect(30, 360, 16, 20, align='center'),
    Circle(30, 375, 8),
    Rect(30, 370, 16, 5, fill='white', align='top'),
    Label('L', 30, 355, fill='white')
    )

rightFoot = Group(
    Circle(60, 350, 8),
    Rect(60, 360, 16, 20, align='center'),
    Circle(60, 375, 8),
    Rect(60, 370, 16, 5, fill='white', align='top'),
    Label('R', 60, 355, fill='white')
    )

def winGame():
    Rect(200, 225, 200, 100, fill='lightGreen', align='center')
    Label('You win!', 200, 225, size=50)
    app.stop()

def loseGame(reason):
    Rect(200, 225, 200, 100, fill='pink', align='center')
    Label(reason, 200, 200, size=30)
    Label('You lose!', 200, 250, size=30)
    app.stop()

def onMousePress(mouseX, mouseY):
    # Then take the step.
    if (nextFootLabel.value == 'L'):
        leftFoot.centerX = mouseX
        leftFoot.centerY = mouseY
        nextFootLabel.value = 'R'
    else:
        rightFoot.centerX = mouseX
        rightFoot.centerY = mouseY
        nextFootLabel.value = 'L'

    # After a step, increment the number of steps taken so far.
    numSteps.value += 1

    # Finally, check for win or lose. A step loses if any of the following occur:
    # 1 - The left foot centerX is bigger than the right foot centerX.
    # 2 - The distance between the feet's centerX or centerY is bigger than 175.
    # 3 - If the place clicked is not in the steps group or the goal.
    footDistanceX = rightFoot.centerX - leftFoot.centerX
    footDistanceY = rightFoot.centerY - leftFoot.centerY
    if (footDistanceX < 0):
        loseGame('Crossed feet!')
    elif ((footDistanceX > 175) or (footDistanceY > 175)):
        loseGame('Too far!')
    elif (goal.hits(mouseX, mouseY) == True):
        winGame()
    elif (steps.hits(mouseX, mouseY) == False):
        loseGame('Not a step!')

onMousePress(55, 240)
onMousePress(135, 170)


# -
app.background = gradient('orange', 'red', 'orange')

steps = Group(
    Polygon(10, 345, 70, 320, 95, 375, 15, 390, fill='white'),
    Polygon(160, 360, 195, 330, 165, 320, fill='white'),
    Polygon(25, 240, 70, 260, 55, 220, fill='white'),
    Polygon(135, 155, 170, 130, 200, 175, fill='white'),
    Polygon(75, 60, 40, 75, 75, 100, fill='white'),
    Polygon(280, 125, 230, 90, 290, 95, fill='white'),
    Polygon(270, 280, 295, 310, 350, 270, fill='white'),
    Polygon(320, 165, 345, 200, 370, 155, fill='white')
    )

goal = Polygon(320, 15, 390, 5, 395, 50, 340, 70, fill='limeGreen')

Label('# of Steps', 250, 350, size=15)
numSteps = Label(0, 250, 370, size=25)

Label('Next foot:', 350, 350, size=15)
nextFootLabel = Label('R', 350, 370, size=25)

leftFoot = Group(
    Circle(30, 350, 8),
    Rect(30, 360, 16, 20, align='center'),
    Circle(30, 375, 8),
    Rect(30, 370, 16, 5, fill='white', align='top'),
    Label('L', 30, 355, fill='white')
    )

rightFoot = Group(
    Circle(60, 350, 8),
    Rect(60, 360, 16, 20, align='center'),
    Circle(60, 375, 8),
    Rect(60, 370, 16, 5, fill='white', align='top'),
    Label('R', 60, 355, fill='white')
    )

def winGame():
    Rect(200, 225, 200, 100, fill='lightGreen', align='center')
    Label('You win!', 200, 225, size=50)
    app.stop()

def loseGame(reason):
    Rect(200, 225, 200, 100, fill='pink', align='center')
    Label(reason, 200, 200, size=30)
    Label('You lose!', 200, 250, size=30)
    app.stop()

def onMousePress(mouseX, mouseY):
    # Then take the step.
    if (nextFootLabel.value == 'L'):
        leftFoot.centerX = mouseX
        leftFoot.centerY = mouseY
        nextFootLabel.value = 'R'
    else:
        rightFoot.centerX = mouseX
        rightFoot.centerY = mouseY
        nextFootLabel.value = 'L'

    # After a step, increment the number of steps taken so far.
    numSteps.value += 1

    # Finally, check for win or lose. A step loses if any of the following occur:
    # 1 - The left foot centerX is bigger than the right foot centerX.
    # 2 - The distance between the feet's centerX or centerY is bigger than 175.
    # 3 - If the place clicked is not in the steps group or the goal.
    footDistanceX = rightFoot.centerX - leftFoot.centerX
    footDistanceY = rightFoot.centerY - leftFoot.centerY
    if (footDistanceX < 0):
        loseGame('Crossed feet!')
    elif ((footDistanceX > 175) or (footDistanceY > 175)):
        loseGame('Too far!')
    elif (goal.hits(mouseX, mouseY) == True):
        winGame()
    elif (steps.hits(mouseX, mouseY) == False):
        loseGame('Not a step!')

onMousePress(55, 240)
onMousePress(35, 240)
onMousePress(150, 150)

