app.background = rgb(35, 30, 30)

app.stepsPerSecond = 8
app.paused = True

# player
player = Rect(200, 200, 20, 20, fill=rgb(70, 75, 220), align='center')
player.speed = 21
player.dx = 0
player.dy = player.speed
player.offScreen = False

# The past locations of the player.
trail = Group()

# instructions
instructions = Group(
    Label('TRON', 200, 50, size=20),
    Label('Move with w,a,s,d', 200, 70),
    Label('The path starts moving down', 200, 85),
    Label('Press r to start or restart', 200, 100)
    )
instructions.fill = rgb(250, 245, 255)

# end game labels
endGameInfo = Group(
    Rect(200, 200, 250, 150, fill=rgb(185, 70, 50), align='center'),
    Label('GAME OVER', 200, 150, fill='white', size=30),
    Label('Score: ', 150, 185, fill='white', size=24, align='left'),
    Label('Restart with r', 200, 225, fill='white', size=18)
    )

endScore = Label(0, 240, 185, fill='white', size=24)
endGameInfo.add(endScore)
endGameInfo.visible = False

score = Label(0, 35, 30, fill='white', size=40)
score.visible = False

def restartGame():
    # Reset the player.
    player.centerX = 200
    player.centerY = 200
    player.dx = 0
    player.dy = player.speed
    player.offScreen = False

    # Reset the scores and info screens.
    score.value = 0
    score.visible = True
    endGameInfo.visible = False
    trail.clear()
    instructions.visible = False

    app.paused = False

def gameOver():
    # Hide the score, show the end game screen, and pause the app.
    score.visible = False

    endGameInfo.visible = True
    endScore.value = score.value
    endGameInfo.toFront()
    app.paused = True
    instructions.visible = True

def playerOffScreenTest():
    # Check if the player's centerX or centerY are off the screen and set
    # the custom property appropriately.
    if ((player.centerX < 0) or (player.centerX > 400) or
        (player.centerY < 0) or (player.centerY > 400)):
        player.offScreen = True
def setPlayerSpeed(newDx, newDy):
    player.dx = newDx
    player.dy = newDy

def onKeyPress(key):
    # Restart the game if 'r' is pressed.
    if (key == 'r'):
        restartGame()

    # Change the player's dx and dy.
    if (key == 'w'):
        setPlayerSpeed(0, -player.speed)
    elif (key == 'a'):
        setPlayerSpeed(-player.speed, 0)
    elif (key == 's'):
        setPlayerSpeed(0, player.speed)
    elif (key == 'd'):
        setPlayerSpeed(player.speed, 0)

def onStep():
    # Move the player and make sure they are on the screen.
    player.centerX += player.dx
    player.centerY += player.dy
    playerOffScreenTest()

    # If the player is offscreen or intersecting itself, then end the game.
    if ((player.offScreen == True) or (player.hitsShape(trail) == True)):
        gameOver()
    # Otherwise, add a copy of the current player to the group trail,
    # and increase the score by 1.
    else:
        trail.add(
            Rect(player.left, player.top, player.width, player.height,
                 fill=player.fill)
            )
        score.value += 1

onKeyPress('r')
onSteps(9)
app.paused = True


# -
app.background = rgb(35, 30, 30)

app.stepsPerSecond = 8
app.paused = True

# player
player = Rect(200, 200, 20, 20, fill=rgb(70, 75, 220), align='center')
player.speed = 21
player.dx = 0
player.dy = player.speed
player.offScreen = False

# The past locations of the player.
trail = Group()

# instructions
instructions = Group(
    Label('TRON', 200, 50, size=20),
    Label('Move with w,a,s,d', 200, 70),
    Label('The path starts moving down', 200, 85),
    Label('Press r to start or restart', 200, 100)
    )
instructions.fill = rgb(250, 245, 255)

# end game labels
endGameInfo = Group(
    Rect(200, 200, 250, 150, fill=rgb(185, 70, 50), align='center'),
    Label('GAME OVER', 200, 150, fill='white', size=30),
    Label('Score: ', 150, 185, fill='white', size=24, align='left'),
    Label('Restart with r', 200, 225, fill='white', size=18)
    )

endScore = Label(0, 240, 185, fill='white', size=24)
endGameInfo.add(endScore)
endGameInfo.visible = False

score = Label(0, 35, 30, fill='white', size=40)
score.visible = False

def restartGame():
    # Reset the player.
    player.centerX = 200
    player.centerY = 200
    player.dx = 0
    player.dy = player.speed
    player.offScreen = False

    # Reset the scores and info screens.
    score.value = 0
    score.visible = True
    endGameInfo.visible = False
    trail.clear()
    instructions.visible = False

    app.paused = False

def gameOver():
    # Hide the score, show the end game screen, and pause the app.
    score.visible = False

    endGameInfo.visible = True
    endScore.value = score.value
    endGameInfo.toFront()
    app.paused = True
    instructions.visible = True

def playerOffScreenTest():
    # Check if the player's centerX or centerY are off the screen and set
    # the custom property appropriately.
    if ((player.centerX < 0) or (player.centerX > 400) or
        (player.centerY < 0) or (player.centerY > 400)):
        player.offScreen = True
def setPlayerSpeed(newDx, newDy):
    player.dx = newDx
    player.dy = newDy

def onKeyPress(key):
    # Restart the game if 'r' is pressed.
    if (key == 'r'):
        restartGame()

    # Change the player's dx and dy.
    if (key == 'w'):
        setPlayerSpeed(0, -player.speed)
    elif (key == 'a'):
        setPlayerSpeed(-player.speed, 0)
    elif (key == 's'):
        setPlayerSpeed(0, player.speed)
    elif (key == 'd'):
        setPlayerSpeed(player.speed, 0)

def onStep():
    # Move the player and make sure they are on the screen.
    player.centerX += player.dx
    player.centerY += player.dy
    playerOffScreenTest()

    # If the player is offscreen or intersecting itself, then end the game.
    if ((player.offScreen == True) or (player.hitsShape(trail) == True)):
        gameOver()
    # Otherwise, add a copy of the current player to the group trail,
    # and increase the score by 1.
    else:
        trail.add(
            Rect(player.left, player.top, player.width, player.height,
                 fill=player.fill)
            )
        score.value += 1

onKeyPress('r')
onSteps(5)
app.paused = True


# -
app.background = rgb(35, 30, 30)

app.stepsPerSecond = 8
app.paused = True

# player
player = Rect(200, 200, 20, 20, fill=rgb(70, 75, 220), align='center')
player.speed = 21
player.dx = 0
player.dy = player.speed
player.offScreen = False

# The past locations of the player.
trail = Group()

# instructions
instructions = Group(
    Label('TRON', 200, 50, size=20),
    Label('Move with w,a,s,d', 200, 70),
    Label('The path starts moving down', 200, 85),
    Label('Press r to start or restart', 200, 100)
    )
instructions.fill = rgb(250, 245, 255)

# end game labels
endGameInfo = Group(
    Rect(200, 200, 250, 150, fill=rgb(185, 70, 50), align='center'),
    Label('GAME OVER', 200, 150, fill='white', size=30),
    Label('Score: ', 150, 185, fill='white', size=24, align='left'),
    Label('Restart with r', 200, 225, fill='white', size=18)
    )

endScore = Label(0, 240, 185, fill='white', size=24)
endGameInfo.add(endScore)
endGameInfo.visible = False

score = Label(0, 35, 30, fill='white', size=40)
score.visible = False

def restartGame():
    # Reset the player.
    player.centerX = 200
    player.centerY = 200
    player.dx = 0
    player.dy = player.speed
    player.offScreen = False

    # Reset the scores and info screens.
    score.value = 0
    score.visible = True
    endGameInfo.visible = False
    trail.clear()
    instructions.visible = False

    app.paused = False

def gameOver():
    # Hide the score, show the end game screen, and pause the app.
    score.visible = False

    endGameInfo.visible = True
    endScore.value = score.value
    endGameInfo.toFront()
    app.paused = True
    instructions.visible = True

def playerOffScreenTest():
    # Check if the player's centerX or centerY are off the screen and set
    # the custom property appropriately.
    if ((player.centerX < 0) or (player.centerX > 400) or
        (player.centerY < 0) or (player.centerY > 400)):
        player.offScreen = True
def setPlayerSpeed(newDx, newDy):
    player.dx = newDx
    player.dy = newDy

def onKeyPress(key):
    # Restart the game if 'r' is pressed.
    if (key == 'r'):
        restartGame()

    # Change the player's dx and dy.
    if (key == 'w'):
        setPlayerSpeed(0, -player.speed)
    elif (key == 'a'):
        setPlayerSpeed(-player.speed, 0)
    elif (key == 's'):
        setPlayerSpeed(0, player.speed)
    elif (key == 'd'):
        setPlayerSpeed(player.speed, 0)

def onStep():
    # Move the player and make sure they are on the screen.
    player.centerX += player.dx
    player.centerY += player.dy
    playerOffScreenTest()

    # If the player is offscreen or intersecting itself, then end the game.
    if ((player.offScreen == True) or (player.hitsShape(trail) == True)):
        gameOver()
    # Otherwise, add a copy of the current player to the group trail,
    # and increase the score by 1.
    else:
        trail.add(
            Rect(player.left, player.top, player.width, player.height,
                 fill=player.fill)
            )
        score.value += 1

onKeyPress('r')
onSteps(9)
app.paused = True

