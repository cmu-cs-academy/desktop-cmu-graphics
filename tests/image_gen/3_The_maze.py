app.background = 'mediumSeaGreen'
app.stepsPerSecond = 50

maze = Group(
    Line(45, 105, 45, 365, fill='sienna', lineWidth=10),
    Line(45, 365, 365, 365, fill='sienna', lineWidth=10),
    Line(365, 305, 365, 45, fill='sienna', lineWidth=10),
    Line(45, 45, 365, 45, fill='sienna', lineWidth=10),
    Line(115, 45, 115, 305, fill='sienna', lineWidth=10),
    Line(115, 245, 235, 245, fill='sienna', lineWidth=10),
    Line(175, 365, 175, 305, fill='sienna', lineWidth=10),
    Line(295, 365, 295, 105, fill='sienna', lineWidth=10),
    Line(235, 305, 235, 175, fill='sienna', lineWidth=10),
    Line(175, 105, 295, 105, fill='sienna', lineWidth=10),
    Line(175, 105, 175, 185, fill='sienna', lineWidth=10),
    Line(40, 100, 40, 360, fill='white', lineWidth=10),
    Line(40, 360, 360, 360, fill='white', lineWidth=10),
    Line(360, 300, 360, 40, fill='white', lineWidth=10),
    Line(40, 40, 360, 40, fill='white', lineWidth=10),
    Line(110, 40, 110, 300, fill='white', lineWidth=10),
    Line(110, 240, 230, 240, fill='white', lineWidth=10),
    Line(170, 360, 170, 300, fill='white', lineWidth=10),
    Line(290, 360, 290, 100, fill='white', lineWidth=10),
    Line(230, 300, 230, 170, fill='white', lineWidth=10),
    Line(170, 100, 290, 100, fill='white', lineWidth=10),
    Line(170, 100, 170, 180, fill='white', lineWidth=10),
    )

Label('Use arrow keys to move  /  Press r to restart', 200, 385, fill='white',
      size=15)

player = Circle(40, 72, 18, fill='orange', border='darkOrange')
player.score = Label(0, 40, 72, fill='white', bold=True)
player.gameOver = False

endOfGameMessage = Label('', 200, 200, fill='indigo', size=50, bold=True)
endOfGame = Group(
    Rect(200, 200, 300, 70, fill='lavender', align='center'),
    endOfGameMessage
    )
endOfGame.visible = False

def restartGame():
    player.centerX = 40
    player.centerY = 70
    player.score.centerX = player.centerX
    player.score.centerY = player.centerY
    player.score.value = 0
    player.gameOver = False
    endOfGame.visible = False

def finishGame(message):
    endOfGame.visible = True
    endOfGameMessage.value = message

def checkWin():
    # You should win the game when the player is at the end of the maze.
    if ((player.centerX > 360) and (300 < player.centerY) and
        (player.centerY < 360)):
        player.gameOver = True
        finishGame('YOU WIN!')
def checkLose():
    # You should lose the game when the player intersects the maze.
    if (maze.hitsShape(player) == True):
        player.gameOver = True
        finishGame('YOU LOSE!')
def onKeyPress(key):
    if (key == 'r'):
        restartGame()

def onKeyHold(keys):
    if (player.gameOver == False):
        if ('up' in keys):
            player.centerY -= 2
        if ('down' in keys):
            player.centerY += 2
        if ('left' in  keys):
            player.centerX -= 2
        if ('right' in keys):
            player.centerX += 2

        player.score.centerX = player.centerX
        player.score.centerY = player.centerY
        player.score.value += 1
        checkLose()
        checkWin()

player.centerX = 340
player.centerY = 330
onKeyHolds(['left'], 10)
onKeyHolds(['up'], 40)


# -
app.background = 'mediumSeaGreen'
app.stepsPerSecond = 50

maze = Group(
    Line(45, 105, 45, 365, fill='sienna', lineWidth=10),
    Line(45, 365, 365, 365, fill='sienna', lineWidth=10),
    Line(365, 305, 365, 45, fill='sienna', lineWidth=10),
    Line(45, 45, 365, 45, fill='sienna', lineWidth=10),
    Line(115, 45, 115, 305, fill='sienna', lineWidth=10),
    Line(115, 245, 235, 245, fill='sienna', lineWidth=10),
    Line(175, 365, 175, 305, fill='sienna', lineWidth=10),
    Line(295, 365, 295, 105, fill='sienna', lineWidth=10),
    Line(235, 305, 235, 175, fill='sienna', lineWidth=10),
    Line(175, 105, 295, 105, fill='sienna', lineWidth=10),
    Line(175, 105, 175, 185, fill='sienna', lineWidth=10),
    Line(40, 100, 40, 360, fill='white', lineWidth=10),
    Line(40, 360, 360, 360, fill='white', lineWidth=10),
    Line(360, 300, 360, 40, fill='white', lineWidth=10),
    Line(40, 40, 360, 40, fill='white', lineWidth=10),
    Line(110, 40, 110, 300, fill='white', lineWidth=10),
    Line(110, 240, 230, 240, fill='white', lineWidth=10),
    Line(170, 360, 170, 300, fill='white', lineWidth=10),
    Line(290, 360, 290, 100, fill='white', lineWidth=10),
    Line(230, 300, 230, 170, fill='white', lineWidth=10),
    Line(170, 100, 290, 100, fill='white', lineWidth=10),
    Line(170, 100, 170, 180, fill='white', lineWidth=10),
    )

Label('Use arrow keys to move  /  Press r to restart', 200, 385, fill='white',
      size=15)

player = Circle(40, 72, 18, fill='orange', border='darkOrange')
player.score = Label(0, 40, 72, fill='white', bold=True)
player.gameOver = False

endOfGameMessage = Label('', 200, 200, fill='indigo', size=50, bold=True)
endOfGame = Group(
    Rect(200, 200, 300, 70, fill='lavender', align='center'),
    endOfGameMessage
    )
endOfGame.visible = False

def restartGame():
    player.centerX = 40
    player.centerY = 70
    player.score.centerX = player.centerX
    player.score.centerY = player.centerY
    player.score.value = 0
    player.gameOver = False
    endOfGame.visible = False

def finishGame(message):
    endOfGame.visible = True
    endOfGameMessage.value = message

def checkWin():
    # You should win the game when the player is at the end of the maze.
    if ((player.centerX > 360) and (300 < player.centerY) and
        (player.centerY < 360)):
        player.gameOver = True
        finishGame('YOU WIN!')
def checkLose():
    # You should lose the game when the player intersects the maze.
    if (maze.hitsShape(player) == True):
        player.gameOver = True
        finishGame('YOU LOSE!')
def onKeyPress(key):
    if (key == 'r'):
        restartGame()

def onKeyHold(keys):
    if (player.gameOver == False):
        if ('up' in keys):
            player.centerY -= 2
        if ('down' in keys):
            player.centerY += 2
        if ('left' in  keys):
            player.centerX -= 2
        if ('right' in keys):
            player.centerX += 2

        player.score.centerX = player.centerX
        player.score.centerY = player.centerY
        player.score.value += 1
        checkLose()
        checkWin()

player.centerX = 340
player.centerY = 330
onKeyHolds(['right'], 20)


# -
app.background = 'mediumSeaGreen'
app.stepsPerSecond = 50

maze = Group(
    Line(45, 105, 45, 365, fill='sienna', lineWidth=10),
    Line(45, 365, 365, 365, fill='sienna', lineWidth=10),
    Line(365, 305, 365, 45, fill='sienna', lineWidth=10),
    Line(45, 45, 365, 45, fill='sienna', lineWidth=10),
    Line(115, 45, 115, 305, fill='sienna', lineWidth=10),
    Line(115, 245, 235, 245, fill='sienna', lineWidth=10),
    Line(175, 365, 175, 305, fill='sienna', lineWidth=10),
    Line(295, 365, 295, 105, fill='sienna', lineWidth=10),
    Line(235, 305, 235, 175, fill='sienna', lineWidth=10),
    Line(175, 105, 295, 105, fill='sienna', lineWidth=10),
    Line(175, 105, 175, 185, fill='sienna', lineWidth=10),
    Line(40, 100, 40, 360, fill='white', lineWidth=10),
    Line(40, 360, 360, 360, fill='white', lineWidth=10),
    Line(360, 300, 360, 40, fill='white', lineWidth=10),
    Line(40, 40, 360, 40, fill='white', lineWidth=10),
    Line(110, 40, 110, 300, fill='white', lineWidth=10),
    Line(110, 240, 230, 240, fill='white', lineWidth=10),
    Line(170, 360, 170, 300, fill='white', lineWidth=10),
    Line(290, 360, 290, 100, fill='white', lineWidth=10),
    Line(230, 300, 230, 170, fill='white', lineWidth=10),
    Line(170, 100, 290, 100, fill='white', lineWidth=10),
    Line(170, 100, 170, 180, fill='white', lineWidth=10),
    )

Label('Use arrow keys to move  /  Press r to restart', 200, 385, fill='white',
      size=15)

player = Circle(40, 72, 18, fill='orange', border='darkOrange')
player.score = Label(0, 40, 72, fill='white', bold=True)
player.gameOver = False

endOfGameMessage = Label('', 200, 200, fill='indigo', size=50, bold=True)
endOfGame = Group(
    Rect(200, 200, 300, 70, fill='lavender', align='center'),
    endOfGameMessage
    )
endOfGame.visible = False

def restartGame():
    player.centerX = 40
    player.centerY = 70
    player.score.centerX = player.centerX
    player.score.centerY = player.centerY
    player.score.value = 0
    player.gameOver = False
    endOfGame.visible = False

def finishGame(message):
    endOfGame.visible = True
    endOfGameMessage.value = message

def checkWin():
    # You should win the game when the player is at the end of the maze.
    if ((player.centerX > 360) and (300 < player.centerY) and
        (player.centerY < 360)):
        player.gameOver = True
        finishGame('YOU WIN!')
def checkLose():
    # You should lose the game when the player intersects the maze.
    if (maze.hitsShape(player) == True):
        player.gameOver = True
        finishGame('YOU LOSE!')
def onKeyPress(key):
    if (key == 'r'):
        restartGame()

def onKeyHold(keys):
    if (player.gameOver == False):
        if ('up' in keys):
            player.centerY -= 2
        if ('down' in keys):
            player.centerY += 2
        if ('left' in  keys):
            player.centerX -= 2
        if ('right' in keys):
            player.centerX += 2

        player.score.centerX = player.centerX
        player.score.centerY = player.centerY
        player.score.value += 1
        checkLose()
        checkWin()

onKeyHolds(['right'], 10)

