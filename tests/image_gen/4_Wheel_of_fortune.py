app.background = 'blanchedAlmond'
app.spinning = True

# wheel stand and base
Polygon(175, 20, 225, 20, 250, 375, 150, 375, fill='peru')
Polygon(125, 375, 275, 375, 290, 400, 110, 400, fill='peru')
Circle(200, 200, 150, fill='sandyBrown')

wheel = Group()

def drawArc(num):
    # Draws one arc of the wheel.
    colorList = [ 'lightCoral', 'mediumAquamarine', 'lightBlue', 'plum',
                  'royalBlue' ]
    color = colorList[num % 5]
    startAngle = 36 * num
    sweepAngle = 36
    wheel.add(
        Arc(200, 200, 260, 260, startAngle, sweepAngle, fill=color, border='white')
        )

def drawLabel(num):
    prizes = [ '$0', '$100', '$200', '$300', '$400', '$500', '$1000', '$5000' ]

    # Get a random prize amount.
    text = choice(prizes)
    # Adds the prize to the wheel.
    angle = 36 * num + 18
    centerX, centerY = getPointInDir(200, 200, angle, 90)
    rotate = 300 + 36 * num
    wheel.add(
        Label(text, centerX, centerY, fill='white', size=18, bold=True,
              rotateAngle=rotate)
        )

    # Adds the dots to the outside of the wheel.
    dotX, dotY = getPointInDir(200, 200, angle, 140)
    wheel.add(
        Circle(dotX, dotY, 4, fill='beige')
        )

def drawWheel():
    # Draws the wheel pointer and center circle.
    Polygon(185, 30, 215, 30, 200, 70, fill='tomato', border='white',
            borderWidth=3)
    Circle(200, 200, 20, fill=gradient('silver', 'white', start='left'),
           border='sandyBrown', borderWidth=10)

    for num in range(10):
        drawArc(num)
        drawLabel(num)

drawWheel()

def onKeyPress(key):
    # Begins slowing the wheel.
    if (key == 'space'):
        app.spinning = False

def onStep():
    # Gradually slows the wheel.
    if (app.spinning == False):
        app.stepsPerSecond -= 1

    # When the wheel has stopped, check which part of the wheel is touching the
    # triangle and set its fill. Also draw the winner label.
    if (app.stepsPerSecond == 0):
        winningArc = wheel.hitTest(200, 80)
        winningArc.fill = 'lime'
        Label('WINNER!', 200, 300, fill='gold', border='black', size=50, bold=True)
    wheel.rotateAngle += 3

onSteps(10)
app.paused = True


# -
app.background = 'blanchedAlmond'
app.spinning = True

# wheel stand and base
Polygon(175, 20, 225, 20, 250, 375, 150, 375, fill='peru')
Polygon(125, 375, 275, 375, 290, 400, 110, 400, fill='peru')
Circle(200, 200, 150, fill='sandyBrown')

wheel = Group()

def drawArc(num):
    # Draws one arc of the wheel.
    colorList = [ 'lightCoral', 'mediumAquamarine', 'lightBlue', 'plum',
                  'royalBlue' ]
    color = colorList[num % 5]
    startAngle = 36 * num
    sweepAngle = 36
    wheel.add(
        Arc(200, 200, 260, 260, startAngle, sweepAngle, fill=color, border='white')
        )

def drawLabel(num):
    prizes = [ '$0', '$100', '$200', '$300', '$400', '$500', '$1000', '$5000' ]

    # Get a random prize amount.
    text = choice(prizes)
    # Adds the prize to the wheel.
    angle = 36 * num + 18
    centerX, centerY = getPointInDir(200, 200, angle, 90)
    rotate = 300 + 36 * num
    wheel.add(
        Label(text, centerX, centerY, fill='white', size=18, bold=True,
              rotateAngle=rotate)
        )

    # Adds the dots to the outside of the wheel.
    dotX, dotY = getPointInDir(200, 200, angle, 140)
    wheel.add(
        Circle(dotX, dotY, 4, fill='beige')
        )

def drawWheel():
    # Draws the wheel pointer and center circle.
    Polygon(185, 30, 215, 30, 200, 70, fill='tomato', border='white',
            borderWidth=3)
    Circle(200, 200, 20, fill=gradient('silver', 'white', start='left'),
           border='sandyBrown', borderWidth=10)

    for num in range(10):
        drawArc(num)
        drawLabel(num)

drawWheel()

def onKeyPress(key):
    # Begins slowing the wheel.
    if (key == 'space'):
        app.spinning = False

def onStep():
    # Gradually slows the wheel.
    if (app.spinning == False):
        app.stepsPerSecond -= 1

    # When the wheel has stopped, check which part of the wheel is touching the
    # triangle and set its fill. Also draw the winner label.
    if (app.stepsPerSecond == 0):
        winningArc = wheel.hitTest(200, 80)
        winningArc.fill = 'lime'
        Label('WINNER!', 200, 300, fill='gold', border='black', size=50, bold=True)
    wheel.rotateAngle += 3

onSteps(10)
onKeyPress('space')
onSteps(30)
app.paused = True


# -
app.background = 'blanchedAlmond'
app.spinning = True

# wheel stand and base
Polygon(175, 20, 225, 20, 250, 375, 150, 375, fill='peru')
Polygon(125, 375, 275, 375, 290, 400, 110, 400, fill='peru')
Circle(200, 200, 150, fill='sandyBrown')

wheel = Group()

def drawArc(num):
    # Draws one arc of the wheel.
    colorList = [ 'lightCoral', 'mediumAquamarine', 'lightBlue', 'plum',
                  'royalBlue' ]
    color = colorList[num % 5]
    startAngle = 36 * num
    sweepAngle = 36
    wheel.add(
        Arc(200, 200, 260, 260, startAngle, sweepAngle, fill=color, border='white')
        )

def drawLabel(num):
    prizes = [ '$0', '$100', '$200', '$300', '$400', '$500', '$1000', '$5000' ]

    # Get a random prize amount.
    text = choice(prizes)
    # Adds the prize to the wheel.
    angle = 36 * num + 18
    centerX, centerY = getPointInDir(200, 200, angle, 90)
    rotate = 300 + 36 * num
    wheel.add(
        Label(text, centerX, centerY, fill='white', size=18, bold=True,
              rotateAngle=rotate)
        )

    # Adds the dots to the outside of the wheel.
    dotX, dotY = getPointInDir(200, 200, angle, 140)
    wheel.add(
        Circle(dotX, dotY, 4, fill='beige')
        )

def drawWheel():
    # Draws the wheel pointer and center circle.
    Polygon(185, 30, 215, 30, 200, 70, fill='tomato', border='white',
            borderWidth=3)
    Circle(200, 200, 20, fill=gradient('silver', 'white', start='left'),
           border='sandyBrown', borderWidth=10)

    for num in range(10):
        drawArc(num)
        drawLabel(num)

drawWheel()

def onKeyPress(key):
    # Begins slowing the wheel.
    if (key == 'space'):
        app.spinning = False

def onStep():
    # Gradually slows the wheel.
    if (app.spinning == False):
        app.stepsPerSecond -= 1

    # When the wheel has stopped, check which part of the wheel is touching the
    # triangle and set its fill. Also draw the winner label.
    if (app.stepsPerSecond == 0):
        winningArc = wheel.hitTest(200, 80)
        winningArc.fill = 'lime'
        Label('WINNER!', 200, 300, fill='gold', border='black', size=50, bold=True)
    wheel.rotateAngle += 3


