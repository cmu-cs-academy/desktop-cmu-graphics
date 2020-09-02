import os
from cmu_graphics import *

def initData():
    app.scoreLabel = Label('Score: 0', 200, 30, size=30)
    app.ball = Circle(-30, 200, 30, fill='purple')
    app.ballSpeed = 3
    app.mode = 'playing'
    app.score = 0

def onMouseMove(mouseX, mouseY):
    if app.ball.hits(mouseX, mouseY):
        app.score += 1
        app.ball.centerY = randrange(60, 350)
        app.ball.right = 0
        app.ballSpeed += 1
        app.scoreLabel.value = 'Score: ' + str(app.score)

def playerLost():
    app.mode = 'lost'
    app.group.clear()

    highscore = 0
    user = ''

    if os.path.exists('highscore.txt'):
        with open('highscore.txt', 'r') as f:
            highscore, user = f.read().split(',')
            highscore = int(highscore)

    if app.score > highscore:
        highscore = app.score
        user = app.getTextInput("New high score! Enter your initials.")
        with open('highscore.txt', 'w+') as f:
            f.write(str(app.score) + ',' + user)

    Label('You Lost', 200, 150, size=30)
    if highscore > 0:
        Label('High Score: ' + str(highscore) + ' by ' + user, 200, 200, size=30)
    Label('Press r to restart', 200, 250, size=30)

def onKeyPress(key):
    if key == 'r':
        app.group.clear()
        initData()

def onStep():
    if app.mode == 'playing':
        app.ball.centerX += app.ballSpeed
        if app.ball.left > 400:
            playerLost()

initData()

cmu_graphics.loop()
