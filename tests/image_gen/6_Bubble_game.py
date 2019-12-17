app.background = gradient('lightBlue', 'aliceBlue', start='top')
app.stepsPerSecond = 20
app.stepsSinceNewBubble = 0
app.gameOver = False

# bubbles
bubbles = Group()
bubbles.bubbleColor = gradient(rgb(255, 215, 230), rgb(255, 0, 100),
                               start='right-top')
bubbles.speed = 8

# scores
Label('High score: ', 10, 20, fill=rgb(40, 45, 55), size=20, align='left')
highscore = Label(0, 140, 21, fill=rgb(40, 45, 55), size=20, align='right')
Label('Your score: ', 10, 45, fill=rgb(40, 45, 55), size=20, align='left')
score = Label(0, 140, 46, fill=rgb(40, 45, 55), size=20, align='right')

# game over
endGameScore = Label(0, 290, 151, fill=rgb(40, 45, 55), size=28, align='right')
endGameHighscore = Label(0, 290, 201, fill=rgb(40, 45, 55), size=28,
                         align='right')
endScreen = Group(
    Rect(0, 0, 400, 400, fill=app.background),
    Label('GAME OVER', 200, 100, fill=rgb(40, 45, 55), size=20),
    Label('Your Score: ', 250, 150, fill=rgb(40, 45, 55), size=28, align='right'),
    Label('High Score: ', 250, 200, fill=rgb(40, 45, 55), size=28, align='right'),
    endGameScore,
    endGameHighscore,
    Label('Press r to restart', 200, 275, fill=rgb(40, 45, 55))
    )
endScreen.visible = False

# player
player = Group(
    Polygon(200, 330, 180, 380, 195, 370, 205, 370, 220, 380,
            fill='white', border='lightSteelBlue'),
    Polygon(200, 330, 195, 370, 200, 380, 205, 370, fill='whiteSmoke',
            border='lightSteelBlue'),
    Line(200, 330, 200, 380, fill='lightSteelBlue')
    )

def restart():
    # Resets the properties to start a new game.
    player.centerX = 200
    player.centerY = 300
    bubbles.clear()
    score.value = 0

    endScreen.visible = False
    endGameScore.value = 0

    app.steps = 0
    app.gameOver = False

def gameOver():
    # Ends the game and display the score.
    app.gameOver = True
    endScreen.visible = True
    if (score.value > highscore.value):
        highscore.value = score.value

    endGameScore.value = score.value
    endGameHighscore.value = highscore.value

def changeBubbleColor():
    # Cycles through four different bubble colors.
    redColor = gradient(rgb(255, 215, 230), rgb(255, 0, 100), start='right-top')
    greenColor = gradient(rgb(230, 250, 210), rgb(110, 215, 30), start='right-top')
    blueColor = gradient(rgb(230, 235, 255), rgb(15, 80, 255), start='right-top')
    yellowColor = gradient(rgb(255, 245, 205), rgb(255, 205, 10), start='right-top')

    if (bubbles.bubbleColor == redColor):
        bubbles.bubbleColor = yellowColor
    elif (bubbles.bubbleColor == yellowColor):
        bubbles.bubbleColor = greenColor
    elif (bubbles.bubbleColor == greenColor):
        bubbles.bubbleColor = blueColor
    else:
        bubbles.bubbleColor = redColor

def onMouseMove(mouseX, mouseY):
    if (app.gameOver == False):
        player.centerX = mouseX
        if (mouseY >= 175):
            player.centerY = mouseY
        else:
            player.centerY = 175

def onKeyPress(key):
    if (app.gameOver == True):
        if (key == 'r'):
            restart()

def onStep():
    if (app.gameOver == False):
        app.stepsSinceNewBubble += 1

        # Create a new bubble every 8 steps.
        if (app.stepsSinceNewBubble == 8):
            bubbleX = randrange(0, 400)
            bubbleRadius = randrange(15, 66)
            changeBubbleColor()
            bubbles.add(
                Circle(bubbleX, 50, bubbleRadius, fill=bubbles.bubbleColor,
                       opacity=40)
                )
            app.stepsSinceNewBubble = 0
        # Move the bubbles down.
        # For each bubble in bubbles.children, if it is below the screen, add the
        # bubble's radius to the score and remove it from the bubbles group.
        bubbles.centerY += bubbles.speed
        for bubble in bubbles.children:
            if (bubble.top >= 400):
                score.value += bubble.radius
                bubbles.remove(bubble)
        # End the game if the player hits a bubble.
        if (bubbles.hitsShape(player) == True):
            gameOver()

onMouseMove(-400, 0)
onSteps(100)
app.paused = True


# -
app.background = gradient('lightBlue', 'aliceBlue', start='top')
app.stepsPerSecond = 20
app.stepsSinceNewBubble = 0
app.gameOver = False

# bubbles
bubbles = Group()
bubbles.bubbleColor = gradient(rgb(255, 215, 230), rgb(255, 0, 100),
                               start='right-top')
bubbles.speed = 8

# scores
Label('High score: ', 10, 20, fill=rgb(40, 45, 55), size=20, align='left')
highscore = Label(0, 140, 21, fill=rgb(40, 45, 55), size=20, align='right')
Label('Your score: ', 10, 45, fill=rgb(40, 45, 55), size=20, align='left')
score = Label(0, 140, 46, fill=rgb(40, 45, 55), size=20, align='right')

# game over
endGameScore = Label(0, 290, 151, fill=rgb(40, 45, 55), size=28, align='right')
endGameHighscore = Label(0, 290, 201, fill=rgb(40, 45, 55), size=28,
                         align='right')
endScreen = Group(
    Rect(0, 0, 400, 400, fill=app.background),
    Label('GAME OVER', 200, 100, fill=rgb(40, 45, 55), size=20),
    Label('Your Score: ', 250, 150, fill=rgb(40, 45, 55), size=28, align='right'),
    Label('High Score: ', 250, 200, fill=rgb(40, 45, 55), size=28, align='right'),
    endGameScore,
    endGameHighscore,
    Label('Press r to restart', 200, 275, fill=rgb(40, 45, 55))
    )
endScreen.visible = False

# player
player = Group(
    Polygon(200, 330, 180, 380, 195, 370, 205, 370, 220, 380,
            fill='white', border='lightSteelBlue'),
    Polygon(200, 330, 195, 370, 200, 380, 205, 370, fill='whiteSmoke',
            border='lightSteelBlue'),
    Line(200, 330, 200, 380, fill='lightSteelBlue')
    )

def restart():
    # Resets the properties to start a new game.
    player.centerX = 200
    player.centerY = 300
    bubbles.clear()
    score.value = 0

    endScreen.visible = False
    endGameScore.value = 0

    app.steps = 0
    app.gameOver = False

def gameOver():
    # Ends the game and display the score.
    app.gameOver = True
    endScreen.visible = True
    if (score.value > highscore.value):
        highscore.value = score.value

    endGameScore.value = score.value
    endGameHighscore.value = highscore.value

def changeBubbleColor():
    # Cycles through four different bubble colors.
    redColor = gradient(rgb(255, 215, 230), rgb(255, 0, 100), start='right-top')
    greenColor = gradient(rgb(230, 250, 210), rgb(110, 215, 30), start='right-top')
    blueColor = gradient(rgb(230, 235, 255), rgb(15, 80, 255), start='right-top')
    yellowColor = gradient(rgb(255, 245, 205), rgb(255, 205, 10), start='right-top')

    if (bubbles.bubbleColor == redColor):
        bubbles.bubbleColor = yellowColor
    elif (bubbles.bubbleColor == yellowColor):
        bubbles.bubbleColor = greenColor
    elif (bubbles.bubbleColor == greenColor):
        bubbles.bubbleColor = blueColor
    else:
        bubbles.bubbleColor = redColor

def onMouseMove(mouseX, mouseY):
    if (app.gameOver == False):
        player.centerX = mouseX
        if (mouseY >= 175):
            player.centerY = mouseY
        else:
            player.centerY = 175

def onKeyPress(key):
    if (app.gameOver == True):
        if (key == 'r'):
            restart()

def onStep():
    if (app.gameOver == False):
        app.stepsSinceNewBubble += 1

        # Create a new bubble every 8 steps.
        if (app.stepsSinceNewBubble == 8):
            bubbleX = randrange(0, 400)
            bubbleRadius = randrange(15, 66)
            changeBubbleColor()
            bubbles.add(
                Circle(bubbleX, 50, bubbleRadius, fill=bubbles.bubbleColor,
                       opacity=40)
                )
            app.stepsSinceNewBubble = 0
        # Move the bubbles down.
        # For each bubble in bubbles.children, if it is below the screen, add the
        # bubble's radius to the score and remove it from the bubbles group.
        bubbles.centerY += bubbles.speed
        for bubble in bubbles.children:
            if (bubble.top >= 400):
                score.value += bubble.radius
                bubbles.remove(bubble)
        # End the game if the player hits a bubble.
        if (bubbles.hitsShape(player) == True):
            gameOver()

onSteps(30)
app.paused = True


# -
app.background = gradient('lightBlue', 'aliceBlue', start='top')
app.stepsPerSecond = 20
app.stepsSinceNewBubble = 0
app.gameOver = False

# bubbles
bubbles = Group()
bubbles.bubbleColor = gradient(rgb(255, 215, 230), rgb(255, 0, 100),
                               start='right-top')
bubbles.speed = 8

# scores
Label('High score: ', 10, 20, fill=rgb(40, 45, 55), size=20, align='left')
highscore = Label(0, 140, 21, fill=rgb(40, 45, 55), size=20, align='right')
Label('Your score: ', 10, 45, fill=rgb(40, 45, 55), size=20, align='left')
score = Label(0, 140, 46, fill=rgb(40, 45, 55), size=20, align='right')

# game over
endGameScore = Label(0, 290, 151, fill=rgb(40, 45, 55), size=28, align='right')
endGameHighscore = Label(0, 290, 201, fill=rgb(40, 45, 55), size=28,
                         align='right')
endScreen = Group(
    Rect(0, 0, 400, 400, fill=app.background),
    Label('GAME OVER', 200, 100, fill=rgb(40, 45, 55), size=20),
    Label('Your Score: ', 250, 150, fill=rgb(40, 45, 55), size=28, align='right'),
    Label('High Score: ', 250, 200, fill=rgb(40, 45, 55), size=28, align='right'),
    endGameScore,
    endGameHighscore,
    Label('Press r to restart', 200, 275, fill=rgb(40, 45, 55))
    )
endScreen.visible = False

# player
player = Group(
    Polygon(200, 330, 180, 380, 195, 370, 205, 370, 220, 380,
            fill='white', border='lightSteelBlue'),
    Polygon(200, 330, 195, 370, 200, 380, 205, 370, fill='whiteSmoke',
            border='lightSteelBlue'),
    Line(200, 330, 200, 380, fill='lightSteelBlue')
    )

def restart():
    # Resets the properties to start a new game.
    player.centerX = 200
    player.centerY = 300
    bubbles.clear()
    score.value = 0

    endScreen.visible = False
    endGameScore.value = 0

    app.steps = 0
    app.gameOver = False

def gameOver():
    # Ends the game and display the score.
    app.gameOver = True
    endScreen.visible = True
    if (score.value > highscore.value):
        highscore.value = score.value

    endGameScore.value = score.value
    endGameHighscore.value = highscore.value

def changeBubbleColor():
    # Cycles through four different bubble colors.
    redColor = gradient(rgb(255, 215, 230), rgb(255, 0, 100), start='right-top')
    greenColor = gradient(rgb(230, 250, 210), rgb(110, 215, 30), start='right-top')
    blueColor = gradient(rgb(230, 235, 255), rgb(15, 80, 255), start='right-top')
    yellowColor = gradient(rgb(255, 245, 205), rgb(255, 205, 10), start='right-top')

    if (bubbles.bubbleColor == redColor):
        bubbles.bubbleColor = yellowColor
    elif (bubbles.bubbleColor == yellowColor):
        bubbles.bubbleColor = greenColor
    elif (bubbles.bubbleColor == greenColor):
        bubbles.bubbleColor = blueColor
    else:
        bubbles.bubbleColor = redColor

def onMouseMove(mouseX, mouseY):
    if (app.gameOver == False):
        player.centerX = mouseX
        if (mouseY >= 175):
            player.centerY = mouseY
        else:
            player.centerY = 175

def onKeyPress(key):
    if (app.gameOver == True):
        if (key == 'r'):
            restart()

def onStep():
    if (app.gameOver == False):
        app.stepsSinceNewBubble += 1

        # Create a new bubble every 8 steps.
        if (app.stepsSinceNewBubble == 8):
            bubbleX = randrange(0, 400)
            bubbleRadius = randrange(15, 66)
            changeBubbleColor()
            bubbles.add(
                Circle(bubbleX, 50, bubbleRadius, fill=bubbles.bubbleColor,
                       opacity=40)
                )
            app.stepsSinceNewBubble = 0
        # Move the bubbles down.
        # For each bubble in bubbles.children, if it is below the screen, add the
        # bubble's radius to the score and remove it from the bubbles group.
        bubbles.centerY += bubbles.speed
        for bubble in bubbles.children:
            if (bubble.top >= 400):
                score.value += bubble.radius
                bubbles.remove(bubble)
        # End the game if the player hits a bubble.
        if (bubbles.hitsShape(player) == True):
            gameOver()

onMouseMove(-400, 0)
onSteps(100)
app.paused = True

