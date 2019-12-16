# Most of the code for Concentration has been given to you.
# You will only write the code for onStep.
# A detailed explanation of how to write this code is provided in the notes!
# (1) Write the code to check if two cards match.
# (2) Write the code to check if the game is over.
# That's it, let's code!

app.rows = 3
app.cols = 4
app.cards = makeList(app.rows, app.cols)
app.firstCard = None
app.secondCard = None
app.stepsPerSecond = 1

Label('Concentration', 200, 20, size=30, bold=True)
Label('Time Remaining: ', 180, 50, size=20)
timer = Label(30, 270, 50, size=20)
Label('Try to match all of the cards before time runs out', 200, 80, size=16)

def setColor(color):
    row = randrange(0, app.rows)
    col = randrange(0, app.cols)
    while (app.cards[row][col] != None):
        row = randrange(0, app.rows)
        col = randrange(0, app.cols)
    x = 20 + col * 100
    y = 100 + row * 100
    r = Rect(x, y, 60, 80, fill='darkGray', border='black', borderWidth=4)
    r.color = color
    app.cards[row][col] = r

def initializeCards():
    colors = [ 'red', 'lightBlue', 'blue', 'orange', 'pink', 'purple' ]
    for color in colors:
        setColor(color)
        setColor(color)

initializeCards()

def findCard(x, y):
    for row in range(app.rows):
        for col in range(app.cols):
            card = app.cards[row][col]
            if (card.hits(x, y) == True):
                return card
    return None

def onMousePress(mouseX, mouseY):
    card = findCard(mouseX, mouseY)
    if ((card != None) and (card.fill == 'darkGray')):
        if (app.firstCard == None):
            app.firstCard = card
            card.fill = card.color
        elif (app.secondCard == None):
            app.secondCard = card
            card.fill = card.color

def checkWin():
    for row in range(app.rows):
        for col in range(app.cols):
            if (app.cards[row][col].fill == 'darkGray'):
                return False
    return True

def onStep():
    timer.value -= 1
    # Check if we've clicked on two cards.
    if (app.secondCard != None):
        # Compare the fills of the cards.
        # If they don't match, set the fills to darkGray.
        # If they do match, set the borders to lime.
        # Either way, reset both card variables to None.
        if (app.firstCard.fill != app.secondCard.fill):
            app.firstCard.fill = 'darkGray'
            app.secondCard.fill = 'darkGray'
        else:
            app.firstCard.border = 'lime'
            app.secondCard.border = 'lime'
        app.firstCard = None
        app.secondCard = None
    # Check if the game has been won by calling the checkWin function and
    # draw the game win screen.
    if (checkWin() == True):
        Rect(0, 100, 400, 200, opacity=50)
        Label('YOU WIN', 200, 200, fill='white', size=40)
        app.stop()

    # Check if the game has been lost by checking timer.value and
    # draw the game lose screen.
    if (timer.value == 0):
        Rect(0, 100, 400, 200, opacity=50)
        Label('GAME OVER', 200, 200, fill='white', size=40)
        app.stop()

onMousePress(50, 150)
onMousePress(150, 150)
onStep()
app.paused = True


# -
# Most of the code for Concentration has been given to you.
# You will only write the code for onStep.
# A detailed explanation of how to write this code is provided in the notes!
# (1) Write the code to check if two cards match.
# (2) Write the code to check if the game is over.
# That's it, let's code!

app.rows = 3
app.cols = 4
app.cards = makeList(app.rows, app.cols)
app.firstCard = None
app.secondCard = None
app.stepsPerSecond = 1

Label('Concentration', 200, 20, size=30, bold=True)
Label('Time Remaining: ', 180, 50, size=20)
timer = Label(30, 270, 50, size=20)
Label('Try to match all of the cards before time runs out', 200, 80, size=16)

def setColor(color):
    row = randrange(0, app.rows)
    col = randrange(0, app.cols)
    while (app.cards[row][col] != None):
        row = randrange(0, app.rows)
        col = randrange(0, app.cols)
    x = 20 + col * 100
    y = 100 + row * 100
    r = Rect(x, y, 60, 80, fill='darkGray', border='black', borderWidth=4)
    r.color = color
    app.cards[row][col] = r

def initializeCards():
    colors = [ 'red', 'lightBlue', 'blue', 'orange', 'pink', 'purple' ]
    for color in colors:
        setColor(color)
        setColor(color)

initializeCards()

def findCard(x, y):
    for row in range(app.rows):
        for col in range(app.cols):
            card = app.cards[row][col]
            if (card.hits(x, y) == True):
                return card
    return None

def onMousePress(mouseX, mouseY):
    card = findCard(mouseX, mouseY)
    if ((card != None) and (card.fill == 'darkGray')):
        if (app.firstCard == None):
            app.firstCard = card
            card.fill = card.color
        elif (app.secondCard == None):
            app.secondCard = card
            card.fill = card.color

def checkWin():
    for row in range(app.rows):
        for col in range(app.cols):
            if (app.cards[row][col].fill == 'darkGray'):
                return False
    return True

def onStep():
    timer.value -= 1
    # Check if we've clicked on two cards.
    if (app.secondCard != None):
        # Compare the fills of the cards.
        # If they don't match, set the fills to darkGray.
        # If they do match, set the borders to lime.
        # Either way, reset both card variables to None.
        if (app.firstCard.fill != app.secondCard.fill):
            app.firstCard.fill = 'darkGray'
            app.secondCard.fill = 'darkGray'
        else:
            app.firstCard.border = 'lime'
            app.secondCard.border = 'lime'
        app.firstCard = None
        app.secondCard = None
    # Check if the game has been won by calling the checkWin function and
    # draw the game win screen.
    if (checkWin() == True):
        Rect(0, 100, 400, 200, opacity=50)
        Label('YOU WIN', 200, 200, fill='white', size=40)
        app.stop()

    # Check if the game has been lost by checking timer.value and
    # draw the game lose screen.
    if (timer.value == 0):
        Rect(0, 100, 400, 200, opacity=50)
        Label('GAME OVER', 200, 200, fill='white', size=40)
        app.stop()



# -
# Most of the code for Concentration has been given to you.
# You will only write the code for onStep.
# A detailed explanation of how to write this code is provided in the notes!
# (1) Write the code to check if two cards match.
# (2) Write the code to check if the game is over.
# That's it, let's code!

app.rows = 3
app.cols = 4
app.cards = makeList(app.rows, app.cols)
app.firstCard = None
app.secondCard = None
app.stepsPerSecond = 1

Label('Concentration', 200, 20, size=30, bold=True)
Label('Time Remaining: ', 180, 50, size=20)
timer = Label(30, 270, 50, size=20)
Label('Try to match all of the cards before time runs out', 200, 80, size=16)

def setColor(color):
    row = randrange(0, app.rows)
    col = randrange(0, app.cols)
    while (app.cards[row][col] != None):
        row = randrange(0, app.rows)
        col = randrange(0, app.cols)
    x = 20 + col * 100
    y = 100 + row * 100
    r = Rect(x, y, 60, 80, fill='darkGray', border='black', borderWidth=4)
    r.color = color
    app.cards[row][col] = r

def initializeCards():
    colors = [ 'red', 'lightBlue', 'blue', 'orange', 'pink', 'purple' ]
    for color in colors:
        setColor(color)
        setColor(color)

initializeCards()

def findCard(x, y):
    for row in range(app.rows):
        for col in range(app.cols):
            card = app.cards[row][col]
            if (card.hits(x, y) == True):
                return card
    return None

def onMousePress(mouseX, mouseY):
    card = findCard(mouseX, mouseY)
    if ((card != None) and (card.fill == 'darkGray')):
        if (app.firstCard == None):
            app.firstCard = card
            card.fill = card.color
        elif (app.secondCard == None):
            app.secondCard = card
            card.fill = card.color

def checkWin():
    for row in range(app.rows):
        for col in range(app.cols):
            if (app.cards[row][col].fill == 'darkGray'):
                return False
    return True

def onStep():
    timer.value -= 1
    # Check if we've clicked on two cards.
    if (app.secondCard != None):
        # Compare the fills of the cards.
        # If they don't match, set the fills to darkGray.
        # If they do match, set the borders to lime.
        # Either way, reset both card variables to None.
        if (app.firstCard.fill != app.secondCard.fill):
            app.firstCard.fill = 'darkGray'
            app.secondCard.fill = 'darkGray'
        else:
            app.firstCard.border = 'lime'
            app.secondCard.border = 'lime'
        app.firstCard = None
        app.secondCard = None
    # Check if the game has been won by calling the checkWin function and
    # draw the game win screen.
    if (checkWin() == True):
        Rect(0, 100, 400, 200, opacity=50)
        Label('YOU WIN', 200, 200, fill='white', size=40)
        app.stop()

    # Check if the game has been lost by checking timer.value and
    # draw the game lose screen.
    if (timer.value == 0):
        Rect(0, 100, 400, 200, opacity=50)
        Label('GAME OVER', 200, 200, fill='white', size=40)
        app.stop()

onSteps(30)
app.paused = True

