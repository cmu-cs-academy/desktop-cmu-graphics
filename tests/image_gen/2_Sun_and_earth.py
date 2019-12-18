app.background = 'black'

Label('*Not to scale', 340, 370, fill='white', size=16)

sun = Star(200, 200, 35, 400, fill=gradient('orange', 'yellow', 'orangeRed'))

earth = Group(
    Circle(200, 200, 150, fill=None, border='darkGrey'),
    Circle(200, 50, 10, fill=gradient('green', 'royalBlue', start='left-top'))
    )
earth.direction = 'clockwise'

def onKeyPress(key):
    # Change the direction based on key.
    if (key == 'right'):
        earth.direction = 'clockwise'
    elif (key == 'left'):
        earth.direction = 'counterclockwise'

def onStep():
    # If the direction of the Earth is clockwise, add 3 to the rotateAngle.
    # Otherwise subtract 3.
    if (earth.direction == 'clockwise'):
        earth.rotateAngle += 3
    else:
        earth.rotateAngle -= 3
    # Increase the number of points of the sun by 1.
    sun.points += 1

onSteps(200)
app.paused = True


# -
app.background = 'black'

Label('*Not to scale', 340, 370, fill='white', size=16)

sun = Star(200, 200, 35, 400, fill=gradient('orange', 'yellow', 'orangeRed'))

earth = Group(
    Circle(200, 200, 150, fill=None, border='darkGrey'),
    Circle(200, 50, 10, fill=gradient('green', 'royalBlue', start='left-top'))
    )
earth.direction = 'clockwise'

def onKeyPress(key):
    # Change the direction based on key.
    if (key == 'right'):
        earth.direction = 'clockwise'
    elif (key == 'left'):
        earth.direction = 'counterclockwise'

def onStep():
    # If the direction of the Earth is clockwise, add 3 to the rotateAngle.
    # Otherwise subtract 3.
    if (earth.direction == 'clockwise'):
        earth.rotateAngle += 3
    else:
        earth.rotateAngle -= 3
    # Increase the number of points of the sun by 1.
    sun.points += 1

onSteps(20)
onKeyPress('left')
onSteps(20)
onKeyPress('right')
onSteps(20)
app.paused = True


# -
app.background = 'black'

Label('*Not to scale', 340, 370, fill='white', size=16)

sun = Star(200, 200, 35, 400, fill=gradient('orange', 'yellow', 'orangeRed'))

earth = Group(
    Circle(200, 200, 150, fill=None, border='darkGrey'),
    Circle(200, 50, 10, fill=gradient('green', 'royalBlue', start='left-top'))
    )
earth.direction = 'clockwise'

def onKeyPress(key):
    # Change the direction based on key.
    if (key == 'right'):
        earth.direction = 'clockwise'
    elif (key == 'left'):
        earth.direction = 'counterclockwise'

def onStep():
    # If the direction of the Earth is clockwise, add 3 to the rotateAngle.
    # Otherwise subtract 3.
    if (earth.direction == 'clockwise'):
        earth.rotateAngle += 3
    else:
        earth.rotateAngle -= 3
    # Increase the number of points of the sun by 1.
    sun.points += 1


