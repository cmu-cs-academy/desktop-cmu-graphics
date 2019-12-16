app.background = 'black'
app.stepsPerSecond = 20

app.ghost = None
app.ghostName = None

Label("Type the ghost's name to fend it off!", 200, 25, fill='white', size=15)

def drawName():
    # Positions the name around the center of the canvas.
    x = randrange(50, 351)
    if ((x >= 100) and (x <= 300)):
        y = 300 * randrange(0, 2) + randrange(25, 101)
    else:
        y = randrange(50, 351)

    # Draws the name.
    app.ghostName = Group(
        Rect(x, y, 8 * len(app.ghost.forbiddenName), 20, fill='aliceBlue',
             border='lightBlue', align='center'),
        Label(app.ghost.forbiddenName, x, y)
        )
    app.ghostName.opacity = 0
    app.ghostName.dO = 4
    app.ghostName.toFront()

def createGhost():
    app.ghost = Group(
        Arc(200, 175, 60, 60, 270, 180, fill='ghostWhite'),
        Rect(170, 174, 60, 65, fill='ghostWhite'),
        Oval(190, 170, 10, 20, rotateAngle=10),
        Oval(210, 170, 10, 20, rotateAngle=-10),
        Oval(200, 190, 10, 20),
        Arc(165, 200, 35, 30, 265, 90, fill='ghostWhite', rotateAngle=30),
        Arc(235, 200, 35, 30, 5, 90, fill='ghostWhite', rotateAngle=-30),
        Polygon(165, 200, 171, 180, 171, 210, fill='ghostWhite'),
        Polygon(235, 200, 229, 180, 229, 210, fill='ghostWhite'),
        Arc(190, 238, 40, 45, 90, 180, fill='ghostWhite'),
        Arc(210, 238, 40, 30, 90, 110, fill='ghostWhite')
        )

    # Creates the ghost's name. It either has 4 vowels or 20 characters.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    app.ghost.forbiddenName = ''
    numVowels = 0
    while ((numVowels <= 3) and (len(app.ghost.forbiddenName) < 20)):
        randIndex = randrange(0, 26)
        newCharacter = alphabet[randIndex]
        app.ghost.forbiddenName += newCharacter
        if (newCharacter in 'aeiou'):
            numVowels += 1

    # Sets the amount that the ghost's opacity decreases each time a letter
    # is pressed that is in they name.
    app.ghost.dO = -50 / len(app.ghost.forbiddenName)

    # Draws the box which contains the ghost's name.
    drawName()

createGhost()

def endGame():
    Label('Oh no, the ghost got you!', 200, 225, size=15)
    Label("The rest of the ghost's name was:", 200, 250, size=15)
    Label(app.ghost.forbiddenName, 200, 275, size=15)
    app.stop()

def onKeyPress(key):
    # Checks each letter in the name to see if the key matches.
    newName = ''
    for i in range(len(app.ghost.forbiddenName)):
        character = app.ghost.forbiddenName[i]
        if (key != character):
            newName += character
        else:
            app.ghost.opacity += app.ghost.dO

    app.ghost.forbiddenName = newName

def onStep():
    # When the ghost's entire name has been said, creates a new ghost.
    if (app.ghost.forbiddenName == ''):
        app.group.clear()
        createGhost()

    # Increases the size of the ghost and end the game if it gets too big.
    app.ghost.width += 2
    app.ghost.height += 2
    if (app.ghost.width >= 500):
        endGame()

    # Makes the ghost's name appear and disappear.
    app.ghostName.opacity += app.ghostName.dO
    if ((app.ghostName.opacity >= 80) or (app.ghostName.opacity <= 0)):
        app.ghostName.dO *= -1


