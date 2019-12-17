# background
Rect(0, 0, 400, 350, fill=gradient('dodgerBlue', 'lightCyan', start='top'))
Rect(0, 350, 400, 110, fill=gradient('mediumSeaGreen', 'green', start='top'))

app.solution = ''
app.guesses = ''
app.numRight = 0
app.numWrong = 0
app.win = False
app.paused = True

instructions = Label('Press space to set the word', 200, 325, size=18,
                     bold=True)

upHouse = Group()

def makeBalloon(centerX, centerY, radius, color1, color2):
    # Draws a balloon and adds it to the upHouse group.
    balloon = Group(
        Line(200, 175, centerX, centerY, fill='white', lineWidth=1),
        Circle(centerX, centerY, radius,
               fill=gradient(color1, color2, start='right-top'))
        )
    balloon.type = 'balloon'
    upHouse.add(balloon)

makeBalloon(175, 2, 50, 'lightCoral', 'red')
makeBalloon(200, 50, 35, 'orange', 'orangeRed')
makeBalloon(260, 30, 45, 'plum', 'mediumVioletRed')
makeBalloon(150, 70, 30, 'lavenderBlush', 'pink')
makeBalloon(150, 15, 37, 'mediumPurple', 'darkOrchid')
makeBalloon(240, 1, 40, 'cornSilk', 'yellow')

# Draws the house and adds it to group upHouse.
house = Group(
    Rect(155, 260, 90, 10, fill='maroon'),
    Rect(160, 220, 40, 40, fill='pink'),
    Rect(200, 220, 40, 40, fill='lightGreen'),
    Polygon(150, 220, 250, 220, 240, 175, 160, 175, fill='darkSlateBlue'),
    Polygon(200, 220, 220, 190, 240, 220, fill='lemonChiffon'),
    Polygon(170, 208, 170, 195, 180, 185, 190, 195, 190, 208,
            fill='lemonChiffon'),
    Rect(180, 242, 12, 18, fill='maroon'),
    Rect(160, 220, 40, 15, fill='lightSkyBlue'),
    Rect(215, 232, 10, 18, fill='plum'),
    Rect(205, 232, 5, 18, fill='plum'),
    Rect(230, 232, 5, 18, fill='plum'),
    Rect(215, 205, 10, 12, fill='plum'),
    Rect(176, 193, 8, 10, fill='plum'),
    Rect(195, 165, 10, 18, fill='maroon'),
    Line(220, 190, 200, 220, fill='lightSkyBlue', lineWidth=5),
    Line(220, 190, 240, 220, fill='lightSkyBlue', lineWidth=5),
    Line(180, 185, 170, 195, fill='lightSkyBlue', lineWidth=5),
    Line(180, 185, 190, 195, fill='lightSkyBlue', lineWidth=5),
    Line(160, 220, 160, 260, fill='white', lineWidth=3),
    Line(160, 235, 200, 235, fill='white', lineWidth=3)
    )
house.type = 'house'
upHouse.add(house)

def drawInputLines():
    # Draws the lines that shows where the correct letters will be drawn.
    for index in range(len(app.solution)):
        lineCx = app.spacing * (index + 1 / 2)
        lineCy = 390
        Line(lineCx - 10, lineCy, lineCx + 10, lineCy, fill='white')

def drawLetter(index):
    # Draws a letter on the correct input line.
    letter = app.solution[index]
    letterX = app.spacing * (index + 1 / 2)
    letterY = 390
    Label(letter, letterX, letterY, fill='white', size=35, align='bottom')

def popBalloon():
    # Removes a balloon by setting its visibility to false.
    notChanged = False
    for housePart in upHouse:
        if (housePart.type == 'balloon'):
            if ((housePart.visible == True) and (notChanged == False)):
                housePart.visible = False
                notChanged = True

    # Drops the house a little.
    upHouse.centerY += 15
    if (upHouse.bottom >= 350):
        upHouse.bottom = 350

def checkWin():
    # When all of the letters have been correctly guessed, ends the game.
    if ((app.numRight == len(app.solution)) and (app.numRight != 0)):
        app.win = True
    elif (app.numWrong >= 6):
        Rect(0, 50, 400, 50, fill='lightCoral')
        Label(app.solution, 200, 75, fill='white', size=35, bold=True)
        app.stop()

def onKeyPress(key):
    if ((key == 'space') and (app.paused == True)):
        app.paused = False

        # Sets the instructions label to be invisible.
        instructions.visible = False

        # Gets a solution and if it is valid start the game.
        app.solution = app.getTextInput('Give me a word!')
        if (app.solution == ''):
            app.win = True
        else:
            app.spacing = 400 / len(app.solution)
            drawInputLines()
    else:
        # When a wrong letter is guessed, pops a balloon.
        if (key not in app.solution):
            popBalloon()
            app.numWrong += 1
        elif ((key in app.solution) and (key not in app.guesses)):
            # Loop through each letter in the solution. If the letter is
            # the same as the key, draw the letter and add 1 to numRight.
            for index in range(len(app.solution)):
                letter = app.solution[index]
                if (letter == key):
                    drawLetter(index)
                    app.numRight += 1
            # Keeps track of the letters that were guessed.
            app.guesses = app.guesses + key
        checkWin()

def onStep():
    # Makes the house float away if the player wins.
    if (app.win == True):
        upHouse.centerY -= 5
        if (upHouse.bottom < 0):
            app.stop()

app.setTextInputs('python')
onKeyPress('space')
onKeyPress('a')
onKeyPress('s')


# -
# background
Rect(0, 0, 400, 350, fill=gradient('dodgerBlue', 'lightCyan', start='top'))
Rect(0, 350, 400, 110, fill=gradient('mediumSeaGreen', 'green', start='top'))

app.solution = ''
app.guesses = ''
app.numRight = 0
app.numWrong = 0
app.win = False
app.paused = True

instructions = Label('Press space to set the word', 200, 325, size=18,
                     bold=True)

upHouse = Group()

def makeBalloon(centerX, centerY, radius, color1, color2):
    # Draws a balloon and adds it to the upHouse group.
    balloon = Group(
        Line(200, 175, centerX, centerY, fill='white', lineWidth=1),
        Circle(centerX, centerY, radius,
               fill=gradient(color1, color2, start='right-top'))
        )
    balloon.type = 'balloon'
    upHouse.add(balloon)

makeBalloon(175, 2, 50, 'lightCoral', 'red')
makeBalloon(200, 50, 35, 'orange', 'orangeRed')
makeBalloon(260, 30, 45, 'plum', 'mediumVioletRed')
makeBalloon(150, 70, 30, 'lavenderBlush', 'pink')
makeBalloon(150, 15, 37, 'mediumPurple', 'darkOrchid')
makeBalloon(240, 1, 40, 'cornSilk', 'yellow')

# Draws the house and adds it to group upHouse.
house = Group(
    Rect(155, 260, 90, 10, fill='maroon'),
    Rect(160, 220, 40, 40, fill='pink'),
    Rect(200, 220, 40, 40, fill='lightGreen'),
    Polygon(150, 220, 250, 220, 240, 175, 160, 175, fill='darkSlateBlue'),
    Polygon(200, 220, 220, 190, 240, 220, fill='lemonChiffon'),
    Polygon(170, 208, 170, 195, 180, 185, 190, 195, 190, 208,
            fill='lemonChiffon'),
    Rect(180, 242, 12, 18, fill='maroon'),
    Rect(160, 220, 40, 15, fill='lightSkyBlue'),
    Rect(215, 232, 10, 18, fill='plum'),
    Rect(205, 232, 5, 18, fill='plum'),
    Rect(230, 232, 5, 18, fill='plum'),
    Rect(215, 205, 10, 12, fill='plum'),
    Rect(176, 193, 8, 10, fill='plum'),
    Rect(195, 165, 10, 18, fill='maroon'),
    Line(220, 190, 200, 220, fill='lightSkyBlue', lineWidth=5),
    Line(220, 190, 240, 220, fill='lightSkyBlue', lineWidth=5),
    Line(180, 185, 170, 195, fill='lightSkyBlue', lineWidth=5),
    Line(180, 185, 190, 195, fill='lightSkyBlue', lineWidth=5),
    Line(160, 220, 160, 260, fill='white', lineWidth=3),
    Line(160, 235, 200, 235, fill='white', lineWidth=3)
    )
house.type = 'house'
upHouse.add(house)

def drawInputLines():
    # Draws the lines that shows where the correct letters will be drawn.
    for index in range(len(app.solution)):
        lineCx = app.spacing * (index + 1 / 2)
        lineCy = 390
        Line(lineCx - 10, lineCy, lineCx + 10, lineCy, fill='white')

def drawLetter(index):
    # Draws a letter on the correct input line.
    letter = app.solution[index]
    letterX = app.spacing * (index + 1 / 2)
    letterY = 390
    Label(letter, letterX, letterY, fill='white', size=35, align='bottom')

def popBalloon():
    # Removes a balloon by setting its visibility to false.
    notChanged = False
    for housePart in upHouse:
        if (housePart.type == 'balloon'):
            if ((housePart.visible == True) and (notChanged == False)):
                housePart.visible = False
                notChanged = True

    # Drops the house a little.
    upHouse.centerY += 15
    if (upHouse.bottom >= 350):
        upHouse.bottom = 350

def checkWin():
    # When all of the letters have been correctly guessed, ends the game.
    if ((app.numRight == len(app.solution)) and (app.numRight != 0)):
        app.win = True
    elif (app.numWrong >= 6):
        Rect(0, 50, 400, 50, fill='lightCoral')
        Label(app.solution, 200, 75, fill='white', size=35, bold=True)
        app.stop()

def onKeyPress(key):
    if ((key == 'space') and (app.paused == True)):
        app.paused = False

        # Sets the instructions label to be invisible.
        instructions.visible = False

        # Gets a solution and if it is valid start the game.
        app.solution = app.getTextInput('Give me a word!')
        if (app.solution == ''):
            app.win = True
        else:
            app.spacing = 400 / len(app.solution)
            drawInputLines()
    else:
        # When a wrong letter is guessed, pops a balloon.
        if (key not in app.solution):
            popBalloon()
            app.numWrong += 1
        elif ((key in app.solution) and (key not in app.guesses)):
            # Loop through each letter in the solution. If the letter is
            # the same as the key, draw the letter and add 1 to numRight.
            for index in range(len(app.solution)):
                letter = app.solution[index]
                if (letter == key):
                    drawLetter(index)
                    app.numRight += 1
            # Keeps track of the letters that were guessed.
            app.guesses = app.guesses + key
        checkWin()

def onStep():
    # Makes the house float away if the player wins.
    if (app.win == True):
        upHouse.centerY -= 5
        if (upHouse.bottom < 0):
            app.stop()

app.setTextInputs('python')
onKeyPress('space')
onKeyPress('t')


# -
# background
Rect(0, 0, 400, 350, fill=gradient('dodgerBlue', 'lightCyan', start='top'))
Rect(0, 350, 400, 110, fill=gradient('mediumSeaGreen', 'green', start='top'))

app.solution = ''
app.guesses = ''
app.numRight = 0
app.numWrong = 0
app.win = False
app.paused = True

instructions = Label('Press space to set the word', 200, 325, size=18,
                     bold=True)

upHouse = Group()

def makeBalloon(centerX, centerY, radius, color1, color2):
    # Draws a balloon and adds it to the upHouse group.
    balloon = Group(
        Line(200, 175, centerX, centerY, fill='white', lineWidth=1),
        Circle(centerX, centerY, radius,
               fill=gradient(color1, color2, start='right-top'))
        )
    balloon.type = 'balloon'
    upHouse.add(balloon)

makeBalloon(175, 2, 50, 'lightCoral', 'red')
makeBalloon(200, 50, 35, 'orange', 'orangeRed')
makeBalloon(260, 30, 45, 'plum', 'mediumVioletRed')
makeBalloon(150, 70, 30, 'lavenderBlush', 'pink')
makeBalloon(150, 15, 37, 'mediumPurple', 'darkOrchid')
makeBalloon(240, 1, 40, 'cornSilk', 'yellow')

# Draws the house and adds it to group upHouse.
house = Group(
    Rect(155, 260, 90, 10, fill='maroon'),
    Rect(160, 220, 40, 40, fill='pink'),
    Rect(200, 220, 40, 40, fill='lightGreen'),
    Polygon(150, 220, 250, 220, 240, 175, 160, 175, fill='darkSlateBlue'),
    Polygon(200, 220, 220, 190, 240, 220, fill='lemonChiffon'),
    Polygon(170, 208, 170, 195, 180, 185, 190, 195, 190, 208,
            fill='lemonChiffon'),
    Rect(180, 242, 12, 18, fill='maroon'),
    Rect(160, 220, 40, 15, fill='lightSkyBlue'),
    Rect(215, 232, 10, 18, fill='plum'),
    Rect(205, 232, 5, 18, fill='plum'),
    Rect(230, 232, 5, 18, fill='plum'),
    Rect(215, 205, 10, 12, fill='plum'),
    Rect(176, 193, 8, 10, fill='plum'),
    Rect(195, 165, 10, 18, fill='maroon'),
    Line(220, 190, 200, 220, fill='lightSkyBlue', lineWidth=5),
    Line(220, 190, 240, 220, fill='lightSkyBlue', lineWidth=5),
    Line(180, 185, 170, 195, fill='lightSkyBlue', lineWidth=5),
    Line(180, 185, 190, 195, fill='lightSkyBlue', lineWidth=5),
    Line(160, 220, 160, 260, fill='white', lineWidth=3),
    Line(160, 235, 200, 235, fill='white', lineWidth=3)
    )
house.type = 'house'
upHouse.add(house)

def drawInputLines():
    # Draws the lines that shows where the correct letters will be drawn.
    for index in range(len(app.solution)):
        lineCx = app.spacing * (index + 1 / 2)
        lineCy = 390
        Line(lineCx - 10, lineCy, lineCx + 10, lineCy, fill='white')

def drawLetter(index):
    # Draws a letter on the correct input line.
    letter = app.solution[index]
    letterX = app.spacing * (index + 1 / 2)
    letterY = 390
    Label(letter, letterX, letterY, fill='white', size=35, align='bottom')

def popBalloon():
    # Removes a balloon by setting its visibility to false.
    notChanged = False
    for housePart in upHouse:
        if (housePart.type == 'balloon'):
            if ((housePart.visible == True) and (notChanged == False)):
                housePart.visible = False
                notChanged = True

    # Drops the house a little.
    upHouse.centerY += 15
    if (upHouse.bottom >= 350):
        upHouse.bottom = 350

def checkWin():
    # When all of the letters have been correctly guessed, ends the game.
    if ((app.numRight == len(app.solution)) and (app.numRight != 0)):
        app.win = True
    elif (app.numWrong >= 6):
        Rect(0, 50, 400, 50, fill='lightCoral')
        Label(app.solution, 200, 75, fill='white', size=35, bold=True)
        app.stop()

def onKeyPress(key):
    if ((key == 'space') and (app.paused == True)):
        app.paused = False

        # Sets the instructions label to be invisible.
        instructions.visible = False

        # Gets a solution and if it is valid start the game.
        app.solution = app.getTextInput('Give me a word!')
        if (app.solution == ''):
            app.win = True
        else:
            app.spacing = 400 / len(app.solution)
            drawInputLines()
    else:
        # When a wrong letter is guessed, pops a balloon.
        if (key not in app.solution):
            popBalloon()
            app.numWrong += 1
        elif ((key in app.solution) and (key not in app.guesses)):
            # Loop through each letter in the solution. If the letter is
            # the same as the key, draw the letter and add 1 to numRight.
            for index in range(len(app.solution)):
                letter = app.solution[index]
                if (letter == key):
                    drawLetter(index)
                    app.numRight += 1
            # Keeps track of the letters that were guessed.
            app.guesses = app.guesses + key
        checkWin()

def onStep():
    # Makes the house float away if the player wins.
    if (app.win == True):
        upHouse.centerY -= 5
        if (upHouse.bottom < 0):
            app.stop()


