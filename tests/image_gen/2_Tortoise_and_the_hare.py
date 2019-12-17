app.stepsPerSecond = 10

def makeBackground():
    Rect(0, 0, 400, 200, fill=gradient('lemonChiffon', 'lightSkyBlue'))
    Arc(200, 105, 117, 125, 270, 180, fill=None, border='gold', borderWidth=8,
        opacity=40)
    Arc(200, 100, 90, 90, 270, 180, fill='gold')
    Rect(0, 100, 400, 300,
         fill=gradient('seaGreen', 'mediumSeaGreen', start='bottom'))

    # finish line
    for i in range (3):
        for j in range(20):
            if ((i + j) % 2 == 0):
                color = 'black'
            else:
                color = 'white'
            Rect(340 + i * 15, 100 + j * 15, 15, 15, fill=color)

makeBackground()

# timer label
Label('Time ', 45, 355, fill='white', size=16)
timer = Label(0, 43, 375, fill='white', size=16)

# Draws the tortoise.
tortoise = Group(
    Polygon(220, 200, 230, 180, 250, 180, 255, 200, fill='darkSeaGreen'),
    Circle(243, 190, 3),
    Rect(175, 210, 15, 8, fill='darkSeaGreen'),
    Rect(210, 210, 15, 8, fill='darkSeaGreen'),
    Polygon(160, 195, 175, 190, 175, 200, fill='darkSeaGreen'),
    Arc(200, 200, 60, 65, 270, 180, fill='saddleBrown'),
    Rect(170, 200, 60, 10, fill='saddleBrown'),
    Circle(170, 205, 5, fill='saddleBrown'),
    Circle(230, 205, 5, fill='saddleBrown')
    )
tortoise.centerX = 50
tortoise.centerY = 150

# Draws the hare.
hare = Group(
    Oval(335, 200, 20, 10, fill='navajoWhite', rotateAngle=70),
    Oval(335, 150, 10, 30, fill='antiqueWhite', rotateAngle=10),
    Oval(325, 150, 10, 30, fill='antiqueWhite', rotateAngle=350),
    Arc(300, 200, 65, 80, 270, 180, fill='antiqueWhite'),
    Circle(330, 170, 15, fill='navajoWhite'),
    Circle (335, 166, 2),
    Circle(345, 166, 1),
    RegularPolygon(342, 172, 2, 3, rotateAngle=60),
    Circle(270, 190, 8, fill='antiqueWhite'),
    Circle(285, 190, 15, fill='navajoWhite'),
    Oval(295, 205, 22, 12, fill='navajoWhite'),
    Oval(320, 200, 20, 10, fill='navajoWhite', rotateAngle=70)
    )
hare.centerX = 50
hare.centerY = 250

def endRace(text):
    Rect(0, 285, 400, 50, fill='indianRed')
    Label(text, 200, 310, fill='white', size=30, bold=True)
    app.stop()

def onStep():
    # Increase the timer's value.
    timer.value += 1
    # Move the hare by 50 pixels, every 10 steps.
    if (timer.value % 10 == 0):
        hare.centerX += 50
    # Move the tortoise by 10 pixels, every 2 steps.
    if (timer.value % 2 == 0):
        tortoise.centerX += 10
    # When the tortoise wins, end the program and display the winner.
    if (tortoise.right >= 380):
        endRace('Tortoise wins!')

onStep()
app.paused = True


# -
app.stepsPerSecond = 10

def makeBackground():
    Rect(0, 0, 400, 200, fill=gradient('lemonChiffon', 'lightSkyBlue'))
    Arc(200, 105, 117, 125, 270, 180, fill=None, border='gold', borderWidth=8,
        opacity=40)
    Arc(200, 100, 90, 90, 270, 180, fill='gold')
    Rect(0, 100, 400, 300,
         fill=gradient('seaGreen', 'mediumSeaGreen', start='bottom'))

    # finish line
    for i in range (3):
        for j in range(20):
            if ((i + j) % 2 == 0):
                color = 'black'
            else:
                color = 'white'
            Rect(340 + i * 15, 100 + j * 15, 15, 15, fill=color)

makeBackground()

# timer label
Label('Time ', 45, 355, fill='white', size=16)
timer = Label(0, 43, 375, fill='white', size=16)

# Draws the tortoise.
tortoise = Group(
    Polygon(220, 200, 230, 180, 250, 180, 255, 200, fill='darkSeaGreen'),
    Circle(243, 190, 3),
    Rect(175, 210, 15, 8, fill='darkSeaGreen'),
    Rect(210, 210, 15, 8, fill='darkSeaGreen'),
    Polygon(160, 195, 175, 190, 175, 200, fill='darkSeaGreen'),
    Arc(200, 200, 60, 65, 270, 180, fill='saddleBrown'),
    Rect(170, 200, 60, 10, fill='saddleBrown'),
    Circle(170, 205, 5, fill='saddleBrown'),
    Circle(230, 205, 5, fill='saddleBrown')
    )
tortoise.centerX = 50
tortoise.centerY = 150

# Draws the hare.
hare = Group(
    Oval(335, 200, 20, 10, fill='navajoWhite', rotateAngle=70),
    Oval(335, 150, 10, 30, fill='antiqueWhite', rotateAngle=10),
    Oval(325, 150, 10, 30, fill='antiqueWhite', rotateAngle=350),
    Arc(300, 200, 65, 80, 270, 180, fill='antiqueWhite'),
    Circle(330, 170, 15, fill='navajoWhite'),
    Circle (335, 166, 2),
    Circle(345, 166, 1),
    RegularPolygon(342, 172, 2, 3, rotateAngle=60),
    Circle(270, 190, 8, fill='antiqueWhite'),
    Circle(285, 190, 15, fill='navajoWhite'),
    Oval(295, 205, 22, 12, fill='navajoWhite'),
    Oval(320, 200, 20, 10, fill='navajoWhite', rotateAngle=70)
    )
hare.centerX = 50
hare.centerY = 250

def endRace(text):
    Rect(0, 285, 400, 50, fill='indianRed')
    Label(text, 200, 310, fill='white', size=30, bold=True)
    app.stop()

def onStep():
    # Increase the timer's value.
    timer.value += 1
    # Move the hare by 50 pixels, every 10 steps.
    if (timer.value % 10 == 0):
        hare.centerX += 50
    # Move the tortoise by 10 pixels, every 2 steps.
    if (timer.value % 2 == 0):
        tortoise.centerX += 10
    # When the tortoise wins, end the program and display the winner.
    if (tortoise.right >= 380):
        endRace('Tortoise wins!')

onSteps(10)
app.paused = True


# -
app.stepsPerSecond = 10

def makeBackground():
    Rect(0, 0, 400, 200, fill=gradient('lemonChiffon', 'lightSkyBlue'))
    Arc(200, 105, 117, 125, 270, 180, fill=None, border='gold', borderWidth=8,
        opacity=40)
    Arc(200, 100, 90, 90, 270, 180, fill='gold')
    Rect(0, 100, 400, 300,
         fill=gradient('seaGreen', 'mediumSeaGreen', start='bottom'))

    # finish line
    for i in range (3):
        for j in range(20):
            if ((i + j) % 2 == 0):
                color = 'black'
            else:
                color = 'white'
            Rect(340 + i * 15, 100 + j * 15, 15, 15, fill=color)

makeBackground()

# timer label
Label('Time ', 45, 355, fill='white', size=16)
timer = Label(0, 43, 375, fill='white', size=16)

# Draws the tortoise.
tortoise = Group(
    Polygon(220, 200, 230, 180, 250, 180, 255, 200, fill='darkSeaGreen'),
    Circle(243, 190, 3),
    Rect(175, 210, 15, 8, fill='darkSeaGreen'),
    Rect(210, 210, 15, 8, fill='darkSeaGreen'),
    Polygon(160, 195, 175, 190, 175, 200, fill='darkSeaGreen'),
    Arc(200, 200, 60, 65, 270, 180, fill='saddleBrown'),
    Rect(170, 200, 60, 10, fill='saddleBrown'),
    Circle(170, 205, 5, fill='saddleBrown'),
    Circle(230, 205, 5, fill='saddleBrown')
    )
tortoise.centerX = 50
tortoise.centerY = 150

# Draws the hare.
hare = Group(
    Oval(335, 200, 20, 10, fill='navajoWhite', rotateAngle=70),
    Oval(335, 150, 10, 30, fill='antiqueWhite', rotateAngle=10),
    Oval(325, 150, 10, 30, fill='antiqueWhite', rotateAngle=350),
    Arc(300, 200, 65, 80, 270, 180, fill='antiqueWhite'),
    Circle(330, 170, 15, fill='navajoWhite'),
    Circle (335, 166, 2),
    Circle(345, 166, 1),
    RegularPolygon(342, 172, 2, 3, rotateAngle=60),
    Circle(270, 190, 8, fill='antiqueWhite'),
    Circle(285, 190, 15, fill='navajoWhite'),
    Oval(295, 205, 22, 12, fill='navajoWhite'),
    Oval(320, 200, 20, 10, fill='navajoWhite', rotateAngle=70)
    )
hare.centerX = 50
hare.centerY = 250

def endRace(text):
    Rect(0, 285, 400, 50, fill='indianRed')
    Label(text, 200, 310, fill='white', size=30, bold=True)
    app.stop()

def onStep():
    # Increase the timer's value.
    timer.value += 1
    # Move the hare by 50 pixels, every 10 steps.
    if (timer.value % 10 == 0):
        hare.centerX += 50
    # Move the tortoise by 10 pixels, every 2 steps.
    if (timer.value % 2 == 0):
        tortoise.centerX += 10
    # When the tortoise wins, end the program and display the winner.
    if (tortoise.right >= 380):
        endRace('Tortoise wins!')

onSteps(8)
app.paused = True

