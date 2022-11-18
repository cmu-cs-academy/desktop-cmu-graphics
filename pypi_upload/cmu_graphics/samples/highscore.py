from cmu_graphics import *
import os

# Set up or reset the game
# Here we clear labels from the screen, create our game objects,
# set their properties, and set our mode to playing
# (rather than start screen or game over)
def startGame():
    app.group.clear()
    app.mode = 'playing'
    app.scoreLabel = Label('Score: 0', 200, 30, size=30)
    app.ball = Circle(-30, 200, 30, fill='purple')
    app.ballSpeed = 3
    app.score = 0

def onMouseMove(mouseX, mouseY):
    # If we're in the start or game over screens, there's no need to
    # handle mouse presses
    if app.mode != 'playing':
        return

    # If we touch the ball, increase our score, move the ball to the left,
    # give it a random Y position, and make it move faster
    if app.ball.hits(mouseX, mouseY):
        app.score += 1
        app.ball.centerY = randrange(60, 350)
        app.ball.right = 0
        app.ballSpeed += 1
        app.scoreLabel.value = 'Score: ' + str(app.score)

# A helper function for drawing text centered on the screen
def drawText(linesList):
    lineHeight = 35
    # lineY starts out at the center (200) minus half the height of our
    # whole block of text
    lineY = 200 - ((len(linesList) * lineHeight) // 2)
    for line in linesList:
        # Create a label for each line, and move lineY down so the next
        # line is drawn lower
        Label(line, 200, lineY, align='center', size=25)
        lineY += lineHeight

# Handle a player loss
def gameOver():
    # Clear game objects from the screen and set our mode
    # so we stop listening to mouse events and can handle key presses
    # correctly later
    app.mode = 'gameOver'
    app.group.clear()

    # We don't know the high score or the user with the highest score yet,
    # so set them to placeholders
    highscore = 0
    highscoreUser = ''

    # If the high score file already exists, open it and read it
    if os.path.exists('highscore.txt'):
        with open('highscore.txt', 'r') as f:
            # split by commas because we store data in the file like:
            # "highscore,highscoreUser"
            highscore, highscoreUser = f.read().split(',')

            # We read strings from the file, so we have to convert highscore
            # to a string
            highscore = int(highscore)

    # If our score is better than the saved highscore
    if app.score > highscore:
        # Set the new highscore to the current score, get the user's initials
        # and save them to the file in the format that we will read later:
        # "highscore,highscoreUser"
        highscore = app.score
        highscoreUser = app.getTextInput("New high score! Enter your initials.")
        with open('highscore.txt', 'w+') as f:
            f.write(str(app.score) + ',' + highscoreUser)

    drawText([
        'You Lost',
        '',
        'High Score: ' + str(highscore) + ' by ' + highscoreUser,
        '',
        "Press 'r' to restart"
    ])

def onKeyPress(key):
    # Restart or start the game from the game over or start screens
    if ((key == 'r' and app.mode == 'gameOver') or
        (key == 's' and app.mode == 'startScreen')):
        startGame()

def onStep():
    # Only move the ball if we're playing the game
    if app.mode == 'playing':
        app.ball.centerX += app.ballSpeed

        # If the ball exits the screen, the player loses
        if app.ball.left > 400:
            gameOver()

def initStartScreen():
    # Set the mode to startScreen so we know to handle the s key correctly
    app.mode = 'startScreen'
    drawText([
        'A Simple Game With High Scores',
        '',
        'To play:',
        'Hover over the purple ball before',
        'it reaches the edge of the screen',
        '',
        "Press 's' to start",
        'Good Luck!'
    ])

initStartScreen()

cmu_graphics.run()