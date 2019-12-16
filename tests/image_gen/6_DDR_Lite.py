app.background = 'black'
app.stepsPerSecond = 40

Label('Dance Dance Revolution Lite', 200, 70,
      fill='white', size=22, font='monospace', bold=True)
Line(0, 150, 400, 150, fill='white', dashes=True)
Line(0, 250, 400, 250, fill='white', dashes=True)

score = Label(0, 200, 100, fill='white', size=20, font='monospace')
bottomText = Label('How close can you get?', 200, 330, fill='white', size=20,
                   font='monospace', bold=True)
circle = Circle(340, 200, 35, fill=None, border='white', borderWidth=3)
arrow = Group(
    Line(20, 177, 20, 222, fill='red', lineWidth=10),
    Line(0, 200, 20, 177, fill='red', lineWidth=9),
    Line(40, 200, 20, 177, fill='red', lineWidth=9)
    )
arrow.dx = 3

def resetArrow():
    # Rotate the arrow so that it appears randomized.
    x = arrow.centerX // 4
    arrow.rotateAngle = 90 * x - 360 * (x // 4)
    arrow.left = 0
    arrow.centerY = 200

def checkHit():
    # Check if the circle contains the arrow and update the text, score, and
    # speed. Then check if the circle hits the arrow and update the text.
    # Otherwise update the text to 'Missed' and decrease the score and speed.
    if (circle.containsShape(arrow) == True):
        bottomText.value = 'Right on!'
        score.value += 20
        arrow.dx += 1
    elif (circle.hitsShape(arrow) == True):
        bottomText.value = 'Close!'
    else:
        bottomText.value = 'Missed'
        score.value -= 20
        arrow.dx -= 1
    if (arrow.dx <= 0):
        arrow.dx = 1

def onKeyPress(key):
    # If the correct arrow key is pressed, check to see if the arrow is
    # in the circle. Otherwise, change the value of bottomText.
    if (((key == 'up') and (arrow.rotateAngle == 0)) or
        ((key == 'right') and (arrow.rotateAngle == 90)) or
        ((key == 'down') and (arrow.rotateAngle == 180)) or
        ((key == 'left') and (arrow.rotateAngle == 270))):
        checkHit()
    else:
        bottomText.value = 'Wrong key!'
        score.value -= 50
        arrow.dx -= 1
        if (arrow.dx <= 0):
            arrow.dx = 1

    resetArrow()

def onStep():
    # Move arrow.centerX to the right using its custom property.
    # If the arrow moves off screen, change the value of bottomText and
    # score and reset the arrow.
    arrow.centerX += arrow.dx
    if (arrow.left > 400):
        bottomText.value = 'Missed'
        score.value -= 20
        resetArrow()

onSteps(20)
onKeyPress('up')
app.paused = True


# -
app.background = 'black'
app.stepsPerSecond = 40

Label('Dance Dance Revolution Lite', 200, 70,
      fill='white', size=22, font='monospace', bold=True)
Line(0, 150, 400, 150, fill='white', dashes=True)
Line(0, 250, 400, 250, fill='white', dashes=True)

score = Label(0, 200, 100, fill='white', size=20, font='monospace')
bottomText = Label('How close can you get?', 200, 330, fill='white', size=20,
                   font='monospace', bold=True)
circle = Circle(340, 200, 35, fill=None, border='white', borderWidth=3)
arrow = Group(
    Line(20, 177, 20, 222, fill='red', lineWidth=10),
    Line(0, 200, 20, 177, fill='red', lineWidth=9),
    Line(40, 200, 20, 177, fill='red', lineWidth=9)
    )
arrow.dx = 3

def resetArrow():
    # Rotate the arrow so that it appears randomized.
    x = arrow.centerX // 4
    arrow.rotateAngle = 90 * x - 360 * (x // 4)
    arrow.left = 0
    arrow.centerY = 200

def checkHit():
    # Check if the circle contains the arrow and update the text, score, and
    # speed. Then check if the circle hits the arrow and update the text.
    # Otherwise update the text to 'Missed' and decrease the score and speed.
    if (circle.containsShape(arrow) == True):
        bottomText.value = 'Right on!'
        score.value += 20
        arrow.dx += 1
    elif (circle.hitsShape(arrow) == True):
        bottomText.value = 'Close!'
    else:
        bottomText.value = 'Missed'
        score.value -= 20
        arrow.dx -= 1
    if (arrow.dx <= 0):
        arrow.dx = 1

def onKeyPress(key):
    # If the correct arrow key is pressed, check to see if the arrow is
    # in the circle. Otherwise, change the value of bottomText.
    if (((key == 'up') and (arrow.rotateAngle == 0)) or
        ((key == 'right') and (arrow.rotateAngle == 90)) or
        ((key == 'down') and (arrow.rotateAngle == 180)) or
        ((key == 'left') and (arrow.rotateAngle == 270))):
        checkHit()
    else:
        bottomText.value = 'Wrong key!'
        score.value -= 50
        arrow.dx -= 1
        if (arrow.dx <= 0):
            arrow.dx = 1

    resetArrow()

def onStep():
    # Move arrow.centerX to the right using its custom property.
    # If the arrow moves off screen, change the value of bottomText and
    # score and reset the arrow.
    arrow.centerX += arrow.dx
    if (arrow.left > 400):
        bottomText.value = 'Missed'
        score.value -= 20
        resetArrow()

onSteps(107)
onKeyPress('up')
onSteps(20)
app.paused = True


# -
app.background = 'black'
app.stepsPerSecond = 40

Label('Dance Dance Revolution Lite', 200, 70,
      fill='white', size=22, font='monospace', bold=True)
Line(0, 150, 400, 150, fill='white', dashes=True)
Line(0, 250, 400, 250, fill='white', dashes=True)

score = Label(0, 200, 100, fill='white', size=20, font='monospace')
bottomText = Label('How close can you get?', 200, 330, fill='white', size=20,
                   font='monospace', bold=True)
circle = Circle(340, 200, 35, fill=None, border='white', borderWidth=3)
arrow = Group(
    Line(20, 177, 20, 222, fill='red', lineWidth=10),
    Line(0, 200, 20, 177, fill='red', lineWidth=9),
    Line(40, 200, 20, 177, fill='red', lineWidth=9)
    )
arrow.dx = 3

def resetArrow():
    # Rotate the arrow so that it appears randomized.
    x = arrow.centerX // 4
    arrow.rotateAngle = 90 * x - 360 * (x // 4)
    arrow.left = 0
    arrow.centerY = 200

def checkHit():
    # Check if the circle contains the arrow and update the text, score, and
    # speed. Then check if the circle hits the arrow and update the text.
    # Otherwise update the text to 'Missed' and decrease the score and speed.
    if (circle.containsShape(arrow) == True):
        bottomText.value = 'Right on!'
        score.value += 20
        arrow.dx += 1
    elif (circle.hitsShape(arrow) == True):
        bottomText.value = 'Close!'
    else:
        bottomText.value = 'Missed'
        score.value -= 20
        arrow.dx -= 1
    if (arrow.dx <= 0):
        arrow.dx = 1

def onKeyPress(key):
    # If the correct arrow key is pressed, check to see if the arrow is
    # in the circle. Otherwise, change the value of bottomText.
    if (((key == 'up') and (arrow.rotateAngle == 0)) or
        ((key == 'right') and (arrow.rotateAngle == 90)) or
        ((key == 'down') and (arrow.rotateAngle == 180)) or
        ((key == 'left') and (arrow.rotateAngle == 270))):
        checkHit()
    else:
        bottomText.value = 'Wrong key!'
        score.value -= 50
        arrow.dx -= 1
        if (arrow.dx <= 0):
            arrow.dx = 1

    resetArrow()

def onStep():
    # Move arrow.centerX to the right using its custom property.
    # If the arrow moves off screen, change the value of bottomText and
    # score and reset the arrow.
    arrow.centerX += arrow.dx
    if (arrow.left > 400):
        bottomText.value = 'Missed'
        score.value -= 20
        resetArrow()

onSteps(107)
onKeyPress('up')
onSteps(80)
onKeyPress('right')
app.paused = True

