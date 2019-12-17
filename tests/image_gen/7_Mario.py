app.background = 'royalBlue'

# world
coin = Oval(375, 120, 15, 25, fill=gradient('gold', 'yellow'), border='khaki')
Rect(0, 205, 700, 195, fill=gradient('mediumSeaGreen', 'darkGreen', start='top'))

# body
mario = Oval(205, 175, 25, 40, fill='deepSkyBlue')

# face/hair
Circle(200, 145, 15, fill='wheat')
Oval(185, 140, 10, 20, fill='sienna')
Oval(200, 130, 30, 20, fill='sienna', rotateAngle=-10)
Oval(195, 138, 15, 15, fill='sienna')
Circle(190, 145, 5, fill='wheat')

# nose/eyes/mustache
Circle(215, 145, 5, fill='wheat')
Oval(210, 140, 5, 10, fill='white')
Oval(213, 140, 3, 5, fill='blue')
Line(215, 150, 210, 148)

# feet
leftFoot = Oval(200, 200, 30, 15, fill='sienna')
rightFoot = Oval(200, 200, 30, 15, fill='sienna')

# arms
Circle(195, 170, 10, fill='fireBrick')
Oval(193, 175, 15, 30, fill='red')
Circle(193, 190, 7, fill='white')
Circle(215, 170, 4, fill='yellow')

# hat
hat = Polygon(180, 145, 200, 135, 220, 130, 225, 125, 215, 125, 205, 115,
              185, 115, 180, 125, 180, 140,
              fill=gradient('crimson', 'red', start='left'))
hat.centerX = 200

def walking():
    leftFoot.rotateAngle = 30
    leftFoot.centerX = 185
    rightFoot.rotateAngle = -30
    rightFoot.centerX = 215

def standing():
    leftFoot.rotateAngle = 0
    leftFoot.centerX = 200
    rightFoot.rotateAngle = 0
    rightFoot.centerX = 200

def checkWin():
    if (hat.centerX > coin.centerX):
        Label('You got the coin!', 200, 300, size=20)
        app.stop()

def checkLose():
    if (coin.centerX < mario.centerX):
        Label('You missed the coin!', 200, 300, size=20)
        app.stop()

def onKeyPress(key):
    # If the left or right arrow key is pressed, move the feet and coin.
    # If enter is pressed, throw the hat and check if it got the coin.
    if (key == 'left'):
        walking()
        coin.centerX += 10
    elif (key == 'right'):
        walking()
        coin.centerX -= 10
    elif (key == 'enter'):
        hat.centerX += 100
        checkWin()

    # Then, check if you lose.
    checkLose()

def onKeyRelease(key):
    # If the left or right arrow key is released, move the feet back.
    # If enter is released, bring the hat back to its original location.
    if (key == 'left'):
        standing()
    elif (key == 'right'):
        standing()
    elif (key == 'enter'):
        hat.centerX -= 100

onKeyPresses('right', 10)
onKeyRelease('right')
onKeyPress('enter')


# -
app.background = 'royalBlue'

# world
coin = Oval(375, 120, 15, 25, fill=gradient('gold', 'yellow'), border='khaki')
Rect(0, 205, 700, 195, fill=gradient('mediumSeaGreen', 'darkGreen', start='top'))

# body
mario = Oval(205, 175, 25, 40, fill='deepSkyBlue')

# face/hair
Circle(200, 145, 15, fill='wheat')
Oval(185, 140, 10, 20, fill='sienna')
Oval(200, 130, 30, 20, fill='sienna', rotateAngle=-10)
Oval(195, 138, 15, 15, fill='sienna')
Circle(190, 145, 5, fill='wheat')

# nose/eyes/mustache
Circle(215, 145, 5, fill='wheat')
Oval(210, 140, 5, 10, fill='white')
Oval(213, 140, 3, 5, fill='blue')
Line(215, 150, 210, 148)

# feet
leftFoot = Oval(200, 200, 30, 15, fill='sienna')
rightFoot = Oval(200, 200, 30, 15, fill='sienna')

# arms
Circle(195, 170, 10, fill='fireBrick')
Oval(193, 175, 15, 30, fill='red')
Circle(193, 190, 7, fill='white')
Circle(215, 170, 4, fill='yellow')

# hat
hat = Polygon(180, 145, 200, 135, 220, 130, 225, 125, 215, 125, 205, 115,
              185, 115, 180, 125, 180, 140,
              fill=gradient('crimson', 'red', start='left'))
hat.centerX = 200

def walking():
    leftFoot.rotateAngle = 30
    leftFoot.centerX = 185
    rightFoot.rotateAngle = -30
    rightFoot.centerX = 215

def standing():
    leftFoot.rotateAngle = 0
    leftFoot.centerX = 200
    rightFoot.rotateAngle = 0
    rightFoot.centerX = 200

def checkWin():
    if (hat.centerX > coin.centerX):
        Label('You got the coin!', 200, 300, size=20)
        app.stop()

def checkLose():
    if (coin.centerX < mario.centerX):
        Label('You missed the coin!', 200, 300, size=20)
        app.stop()

def onKeyPress(key):
    # If the left or right arrow key is pressed, move the feet and coin.
    # If enter is pressed, throw the hat and check if it got the coin.
    if (key == 'left'):
        walking()
        coin.centerX += 10
    elif (key == 'right'):
        walking()
        coin.centerX -= 10
    elif (key == 'enter'):
        hat.centerX += 100
        checkWin()

    # Then, check if you lose.
    checkLose()

def onKeyRelease(key):
    # If the left or right arrow key is released, move the feet back.
    # If enter is released, bring the hat back to its original location.
    if (key == 'left'):
        standing()
    elif (key == 'right'):
        standing()
    elif (key == 'enter'):
        hat.centerX -= 100

onKeyPresses('right', 10)
onKeyRelease('right')
onKeyPress('enter')


# -
app.background = 'royalBlue'

# world
coin = Oval(375, 120, 15, 25, fill=gradient('gold', 'yellow'), border='khaki')
Rect(0, 205, 700, 195, fill=gradient('mediumSeaGreen', 'darkGreen', start='top'))

# body
mario = Oval(205, 175, 25, 40, fill='deepSkyBlue')

# face/hair
Circle(200, 145, 15, fill='wheat')
Oval(185, 140, 10, 20, fill='sienna')
Oval(200, 130, 30, 20, fill='sienna', rotateAngle=-10)
Oval(195, 138, 15, 15, fill='sienna')
Circle(190, 145, 5, fill='wheat')

# nose/eyes/mustache
Circle(215, 145, 5, fill='wheat')
Oval(210, 140, 5, 10, fill='white')
Oval(213, 140, 3, 5, fill='blue')
Line(215, 150, 210, 148)

# feet
leftFoot = Oval(200, 200, 30, 15, fill='sienna')
rightFoot = Oval(200, 200, 30, 15, fill='sienna')

# arms
Circle(195, 170, 10, fill='fireBrick')
Oval(193, 175, 15, 30, fill='red')
Circle(193, 190, 7, fill='white')
Circle(215, 170, 4, fill='yellow')

# hat
hat = Polygon(180, 145, 200, 135, 220, 130, 225, 125, 215, 125, 205, 115,
              185, 115, 180, 125, 180, 140,
              fill=gradient('crimson', 'red', start='left'))
hat.centerX = 200

def walking():
    leftFoot.rotateAngle = 30
    leftFoot.centerX = 185
    rightFoot.rotateAngle = -30
    rightFoot.centerX = 215

def standing():
    leftFoot.rotateAngle = 0
    leftFoot.centerX = 200
    rightFoot.rotateAngle = 0
    rightFoot.centerX = 200

def checkWin():
    if (hat.centerX > coin.centerX):
        Label('You got the coin!', 200, 300, size=20)
        app.stop()

def checkLose():
    if (coin.centerX < mario.centerX):
        Label('You missed the coin!', 200, 300, size=20)
        app.stop()

def onKeyPress(key):
    # If the left or right arrow key is pressed, move the feet and coin.
    # If enter is pressed, throw the hat and check if it got the coin.
    if (key == 'left'):
        walking()
        coin.centerX += 10
    elif (key == 'right'):
        walking()
        coin.centerX -= 10
    elif (key == 'enter'):
        hat.centerX += 100
        checkWin()

    # Then, check if you lose.
    checkLose()

def onKeyRelease(key):
    # If the left or right arrow key is released, move the feet back.
    # If enter is released, bring the hat back to its original location.
    if (key == 'left'):
        standing()
    elif (key == 'right'):
        standing()
    elif (key == 'enter'):
        hat.centerX -= 100


