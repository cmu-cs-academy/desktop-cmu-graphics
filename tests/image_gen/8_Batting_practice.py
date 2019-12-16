app.background = 'green'
app.stepsPerSecond = 40

Label('Batting Practice', 15, 20, fill='white', size=20,
      bold=True, align='left')
Label('Press any key to pitch!', 15, 40, fill='white', align='left')
Label('Press any key to hit!', 15, 55, fill='white', align='left')

Label('Strikes:', 300, 20, fill='white', size=16, bold=True)
strikeCount = Label(0, 350, 20, fill='white', size=16, bold=True)
Label('Hits:', 300, 40, fill='white', size=16, bold=True)
hitCount = Label(0, 350, 40, fill='white', size=16, bold=True)

# infield, plate, and ball
Circle(300, 300, 250, fill='brown')
plate = Polygon(270, 330, 325, 275, 360, 315, 355, 355, 305, 360, fill='white')
ball = Group(
    Circle(200, 200, 20, fill='white'),
    Line(180, 195, 200, 220, fill='red', dashes=True),
    Line(205, 180, 220, 205, fill='red', dashes=True),
    Circle(200, 200, 20, fill=None, border='black')
    )
ball.visible = False

def throwBall():
    # Put the ball on the mound and set its dx, dy to move it towards the plate.
    ball.centerX = 200
    ball.centerY = 200
    ball.dx = 6
    ball.dy = 6
    ball.visible = True

def strike():
    ball.visible = False
    strikeCount.value += 1

def swing():
    # If the ball is over the plate when the swing happens, move the ball at a
    # random rate by changing the dx and dy to be a random number between -25
    # and -10 (inclusive). Otherwise it was a strike.
    if (ball.hitsShape(plate) == True):
        ball.dx = randrange(-25, -9)
        ball.dy = randrange(-25, -9)
    else:
        strike()

def onKeyPress(key):
    if (ball.visible == False):
        throwBall()
    else:
        swing()

def onStep():
    if (ball.visible == True):
        # If the ball is visible, then move it by dx and dy.
        ball.centerX += ball.dx
        ball.centerY += ball.dy

        # When the ball goes past the plate, call the strike() function.
        if (ball.centerX > 400):
            strike()

        # If the ball goes offscreen to the left or to the top, increase
        # the hit count and hide the ball.
        if ((ball.centerX < 0) or (ball.centerY < 0)):
            hitCount.value += 1
            ball.visible = False

onKeyPress('space')
onSteps(30)
app.paused = True


# -
app.background = 'green'
app.stepsPerSecond = 40

Label('Batting Practice', 15, 20, fill='white', size=20,
      bold=True, align='left')
Label('Press any key to pitch!', 15, 40, fill='white', align='left')
Label('Press any key to hit!', 15, 55, fill='white', align='left')

Label('Strikes:', 300, 20, fill='white', size=16, bold=True)
strikeCount = Label(0, 350, 20, fill='white', size=16, bold=True)
Label('Hits:', 300, 40, fill='white', size=16, bold=True)
hitCount = Label(0, 350, 40, fill='white', size=16, bold=True)

# infield, plate, and ball
Circle(300, 300, 250, fill='brown')
plate = Polygon(270, 330, 325, 275, 360, 315, 355, 355, 305, 360, fill='white')
ball = Group(
    Circle(200, 200, 20, fill='white'),
    Line(180, 195, 200, 220, fill='red', dashes=True),
    Line(205, 180, 220, 205, fill='red', dashes=True),
    Circle(200, 200, 20, fill=None, border='black')
    )
ball.visible = False

def throwBall():
    # Put the ball on the mound and set its dx, dy to move it towards the plate.
    ball.centerX = 200
    ball.centerY = 200
    ball.dx = 6
    ball.dy = 6
    ball.visible = True

def strike():
    ball.visible = False
    strikeCount.value += 1

def swing():
    # If the ball is over the plate when the swing happens, move the ball at a
    # random rate by changing the dx and dy to be a random number between -25
    # and -10 (inclusive). Otherwise it was a strike.
    if (ball.hitsShape(plate) == True):
        ball.dx = randrange(-25, -9)
        ball.dy = randrange(-25, -9)
    else:
        strike()

def onKeyPress(key):
    if (ball.visible == False):
        throwBall()
    else:
        swing()

def onStep():
    if (ball.visible == True):
        # If the ball is visible, then move it by dx and dy.
        ball.centerX += ball.dx
        ball.centerY += ball.dy

        # When the ball goes past the plate, call the strike() function.
        if (ball.centerX > 400):
            strike()

        # If the ball goes offscreen to the left or to the top, increase
        # the hit count and hide the ball.
        if ((ball.centerX < 0) or (ball.centerY < 0)):
            hitCount.value += 1
            ball.visible = False

onKeyPress('space')
onSteps(20)
onKeyPress('space')
onSteps(5)
app.paused = True


# -
app.background = 'green'
app.stepsPerSecond = 40

Label('Batting Practice', 15, 20, fill='white', size=20,
      bold=True, align='left')
Label('Press any key to pitch!', 15, 40, fill='white', align='left')
Label('Press any key to hit!', 15, 55, fill='white', align='left')

Label('Strikes:', 300, 20, fill='white', size=16, bold=True)
strikeCount = Label(0, 350, 20, fill='white', size=16, bold=True)
Label('Hits:', 300, 40, fill='white', size=16, bold=True)
hitCount = Label(0, 350, 40, fill='white', size=16, bold=True)

# infield, plate, and ball
Circle(300, 300, 250, fill='brown')
plate = Polygon(270, 330, 325, 275, 360, 315, 355, 355, 305, 360, fill='white')
ball = Group(
    Circle(200, 200, 20, fill='white'),
    Line(180, 195, 200, 220, fill='red', dashes=True),
    Line(205, 180, 220, 205, fill='red', dashes=True),
    Circle(200, 200, 20, fill=None, border='black')
    )
ball.visible = False

def throwBall():
    # Put the ball on the mound and set its dx, dy to move it towards the plate.
    ball.centerX = 200
    ball.centerY = 200
    ball.dx = 6
    ball.dy = 6
    ball.visible = True

def strike():
    ball.visible = False
    strikeCount.value += 1

def swing():
    # If the ball is over the plate when the swing happens, move the ball at a
    # random rate by changing the dx and dy to be a random number between -25
    # and -10 (inclusive). Otherwise it was a strike.
    if (ball.hitsShape(plate) == True):
        ball.dx = randrange(-25, -9)
        ball.dy = randrange(-25, -9)
    else:
        strike()

def onKeyPress(key):
    if (ball.visible == False):
        throwBall()
    else:
        swing()

def onStep():
    if (ball.visible == True):
        # If the ball is visible, then move it by dx and dy.
        ball.centerX += ball.dx
        ball.centerY += ball.dy

        # When the ball goes past the plate, call the strike() function.
        if (ball.centerX > 400):
            strike()

        # If the ball goes offscreen to the left or to the top, increase
        # the hit count and hide the ball.
        if ((ball.centerX < 0) or (ball.centerY < 0)):
            hitCount.value += 1
            ball.visible = False

onKeyPress('space')
onSteps(10)
app.paused = True

