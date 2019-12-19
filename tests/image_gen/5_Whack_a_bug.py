app.stepsPerSecond = 2
app.bugs = [ ]

# background
Rect(0, 0, 400, 150, fill=gradient('cornSilk', 'ghostWhite', start='top'))
Rect(0, 150, 400, 250, fill=gradient('peru', 'saddleBrown', start='top'))

Label('You have whacked', 150, 60, fill='saddleBrown', size=20, bold=True)
score = Label(0, 255, 60, fill='saddleBrown', size=20, bold=True)
Label('bugs!', 300, 60, fill='saddleBrown', size=20, bold=True)

def drawBug(x, y):
    Oval(x, y, 100, 40,
         fill=gradient('saddleBrown', rgb(120, 15, 10), start='top'))

    bugColor = gradient('greenYellow', rgb(135, 170, 65), start='right')
    bug = Group(
        Rect(x, y, 30, 60, fill=bugColor, align='bottom'),
        Circle(x, y - 60, 15, fill=bugColor),
        Label('O o', x, y - 70, bold=True),
        Label('_', x, y - 65, bold=True),
        Line(x, y, x, y - 60, fill='oliveDrab', lineWidth=30, dashes=(2, 12))
        )

    # Hide the bug and add it to our list of bugs.
    bug.visible = False
    app.bugs.append(bug)
def drawBugs():
    # Creates all of the bugs at once.
    bugXCoords = [ 75, 200, 325, 135, 260, 200 ]
    bugYCoords = [ 220, 220, 220, 300, 300, 380 ]
    for index in range(len(bugXCoords)):
        x = bugXCoords[index]
        y = bugYCoords[index]
        drawBug(x, y)

drawBugs()

# hammer
hammer = Group(
    Rect(185, 100, 50, 40, fill='indianRed'),
    Oval(185, 120, 20, 40, fill='indianRed'),
    Oval(235, 120, 20, 40, fill=rgb(195, 80, 80)),
    Rect(204, 140, 12, 50, fill=gradient('peru', 'burlyWood', start='left'))
    )
hammer.rotateAngle = 35

def checkGameOver():
    # Checks the number of bugs that are up.
    upCount = 0
    for bug in app.bugs:
        if (bug.visible == True):
            upCount += 1

    # If all the bugs are up, the game is over.
    if (upCount == len(app.bugs)):
        Rect(50, 185, 300, 100, fill=gradient('maroon', 'crimson'),
             border='white')
        Label('Game Over', 200, 235, fill='white', size=50, font='monospace',
              bold=True)
        app.stop()

def onMousePress(mouseX, mouseY):
    # Rotates the hammer.
    hammer.rotateAngle = 90

    # Checks if any bug is hit by the hammer.
    for bug in app.bugs:
        if ((bug.visible == True) and (bug.hitsShape(hammer) == True)):
            bug.visible = False
            score.value += 1

def onMouseRelease(mouseX, mouseY):
    # Returns the hammer to the original rotateAngle.
    hammer.rotateAngle = 35

def onMouseMove(mouseX, mouseY):
    hammer.centerX = mouseX
    hammer.centerY = mouseY

def onStep():
    # Choose a random bug from the list to turn visible.
    bug = choice(app.bugs)
    bug.visible = True
    checkGameOver()

onMousePress(200, 200)
onMouseRelease(200, 200)
app.paused = True


# -
app.stepsPerSecond = 2
app.bugs = [ ]

# background
Rect(0, 0, 400, 150, fill=gradient('cornSilk', 'ghostWhite', start='top'))
Rect(0, 150, 400, 250, fill=gradient('peru', 'saddleBrown', start='top'))

Label('You have whacked', 150, 60, fill='saddleBrown', size=20, bold=True)
score = Label(0, 255, 60, fill='saddleBrown', size=20, bold=True)
Label('bugs!', 300, 60, fill='saddleBrown', size=20, bold=True)

def drawBug(x, y):
    Oval(x, y, 100, 40,
         fill=gradient('saddleBrown', rgb(120, 15, 10), start='top'))

    bugColor = gradient('greenYellow', rgb(135, 170, 65), start='right')
    bug = Group(
        Rect(x, y, 30, 60, fill=bugColor, align='bottom'),
        Circle(x, y - 60, 15, fill=bugColor),
        Label('O o', x, y - 70, bold=True),
        Label('_', x, y - 65, bold=True),
        Line(x, y, x, y - 60, fill='oliveDrab', lineWidth=30, dashes=(2, 12))
        )

    # Hide the bug and add it to our list of bugs.
    bug.visible = False
    app.bugs.append(bug)
def drawBugs():
    # Creates all of the bugs at once.
    bugXCoords = [ 75, 200, 325, 135, 260, 200 ]
    bugYCoords = [ 220, 220, 220, 300, 300, 380 ]
    for index in range(len(bugXCoords)):
        x = bugXCoords[index]
        y = bugYCoords[index]
        drawBug(x, y)

drawBugs()

# hammer
hammer = Group(
    Rect(185, 100, 50, 40, fill='indianRed'),
    Oval(185, 120, 20, 40, fill='indianRed'),
    Oval(235, 120, 20, 40, fill=rgb(195, 80, 80)),
    Rect(204, 140, 12, 50, fill=gradient('peru', 'burlyWood', start='left'))
    )
hammer.rotateAngle = 35

def checkGameOver():
    # Checks the number of bugs that are up.
    upCount = 0
    for bug in app.bugs:
        if (bug.visible == True):
            upCount += 1

    # If all the bugs are up, the game is over.
    if (upCount == len(app.bugs)):
        Rect(50, 185, 300, 100, fill=gradient('maroon', 'crimson'),
             border='white')
        Label('Game Over', 200, 235, fill='white', size=50, font='monospace',
              bold=True)
        app.stop()

def onMousePress(mouseX, mouseY):
    # Rotates the hammer.
    hammer.rotateAngle = 90

    # Checks if any bug is hit by the hammer.
    for bug in app.bugs:
        if ((bug.visible == True) and (bug.hitsShape(hammer) == True)):
            bug.visible = False
            score.value += 1

def onMouseRelease(mouseX, mouseY):
    # Returns the hammer to the original rotateAngle.
    hammer.rotateAngle = 35

def onMouseMove(mouseX, mouseY):
    hammer.centerX = mouseX
    hammer.centerY = mouseY

def onStep():
    # Choose a random bug from the list to turn visible.
    bug = choice(app.bugs)
    bug.visible = True
    checkGameOver()

onSteps(10)
app.paused = True


# -
app.stepsPerSecond = 2
app.bugs = [ ]

# background
Rect(0, 0, 400, 150, fill=gradient('cornSilk', 'ghostWhite', start='top'))
Rect(0, 150, 400, 250, fill=gradient('peru', 'saddleBrown', start='top'))

Label('You have whacked', 150, 60, fill='saddleBrown', size=20, bold=True)
score = Label(0, 255, 60, fill='saddleBrown', size=20, bold=True)
Label('bugs!', 300, 60, fill='saddleBrown', size=20, bold=True)

def drawBug(x, y):
    Oval(x, y, 100, 40,
         fill=gradient('saddleBrown', rgb(120, 15, 10), start='top'))

    bugColor = gradient('greenYellow', rgb(135, 170, 65), start='right')
    bug = Group(
        Rect(x, y, 30, 60, fill=bugColor, align='bottom'),
        Circle(x, y - 60, 15, fill=bugColor),
        Label('O o', x, y - 70, bold=True),
        Label('_', x, y - 65, bold=True),
        Line(x, y, x, y - 60, fill='oliveDrab', lineWidth=30, dashes=(2, 12))
        )

    # Hide the bug and add it to our list of bugs.
    bug.visible = False
    app.bugs.append(bug)
def drawBugs():
    # Creates all of the bugs at once.
    bugXCoords = [ 75, 200, 325, 135, 260, 200 ]
    bugYCoords = [ 220, 220, 220, 300, 300, 380 ]
    for index in range(len(bugXCoords)):
        x = bugXCoords[index]
        y = bugYCoords[index]
        drawBug(x, y)

drawBugs()

# hammer
hammer = Group(
    Rect(185, 100, 50, 40, fill='indianRed'),
    Oval(185, 120, 20, 40, fill='indianRed'),
    Oval(235, 120, 20, 40, fill=rgb(195, 80, 80)),
    Rect(204, 140, 12, 50, fill=gradient('peru', 'burlyWood', start='left'))
    )
hammer.rotateAngle = 35

def checkGameOver():
    # Checks the number of bugs that are up.
    upCount = 0
    for bug in app.bugs:
        if (bug.visible == True):
            upCount += 1

    # If all the bugs are up, the game is over.
    if (upCount == len(app.bugs)):
        Rect(50, 185, 300, 100, fill=gradient('maroon', 'crimson'),
             border='white')
        Label('Game Over', 200, 235, fill='white', size=50, font='monospace',
              bold=True)
        app.stop()

def onMousePress(mouseX, mouseY):
    # Rotates the hammer.
    hammer.rotateAngle = 90

    # Checks if any bug is hit by the hammer.
    for bug in app.bugs:
        if ((bug.visible == True) and (bug.hitsShape(hammer) == True)):
            bug.visible = False
            score.value += 1

def onMouseRelease(mouseX, mouseY):
    # Returns the hammer to the original rotateAngle.
    hammer.rotateAngle = 35

def onMouseMove(mouseX, mouseY):
    hammer.centerX = mouseX
    hammer.centerY = mouseY

def onStep():
    # Choose a random bug from the list to turn visible.
    bug = choice(app.bugs)
    bug.visible = True
    checkGameOver()

bug4 = app.bugs[4]
bug4.visible = True
onMouseMove(255, 280)
onMousePress(255, 280)
app.paused = True

