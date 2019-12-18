app.background = gradient('lightBlue', 'aliceBlue', start='top')
app.stepsPerSecond = 20
app.stepsSinceNewBubble = 0
app.gameOver = False

Label('Score:', 50, 370, size=20, bold=True)
score = Label(0, 100, 370, size=20, bold=True)

# bubbles
bubbles = Group()
bubbles.bubbleColor = gradient(rgb(255, 215, 230), rgb(255, 0, 100),
                               start='right-top')
bubbles.speed = 8

# player
player = Group(
    Polygon(200, 330, 180, 380, 195, 370, 205, 370, 220, 380,
            fill='white', border='lightSteelBlue'),
    Polygon(200, 330, 195, 370, 200, 380, 205, 370, fill='whiteSmoke',
            border='lightSteelBlue'),
    Line(200, 330, 200, 380, fill='lightSteelBlue')
    )

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

def drawBubble():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    letterIndex = randrange(0, 52)
    letter = alphabet[letterIndex]

    # Change the color of the letter based on if it's uppercase or lowercase.
    if (letter.isupper() == True):
        letterColor = 'dodgerBlue'
    else:
        letterColor = 'crimson'
    # Gets the position, radius, and color, then draws the bubble.
    bubbleX = randrange(0, 400)
    bubbleRadius = randrange(15, 66)
    changeBubbleColor()
    bubble = Group(
        Circle(bubbleX, 0, bubbleRadius, fill=bubbles.bubbleColor,
               opacity=40),
        Label(letter, bubbleX, 0, fill=letterColor, size=20, bold=True)
        )
    bubble.letter = letter

    bubbles.add(bubble)

def onMouseMove(mouseX, mouseY):
    player.centerX = mouseX
    player.centerY = mouseY

def onStep():
    if (app.gameOver == False):
        app.stepsSinceNewBubble += 1

        # Creates a new bubble every 8 steps.
        if (app.stepsSinceNewBubble % 8 == 0):
            drawBubble()

        # Moves the bubbles down.
        bubbles.centerY += bubbles.speed
        for bubble in bubbles.children:
            # Check if the player is hitting the bubble.
            # Depending on if the letter is lowercase or uppercase, either
            # add or subtract from the player width, height, and score.
            if (player.hitsShape(bubble) == True):
                if (bubble.letter.islower() == True):
                    player.width += 10
                    player.height += 10
                    score.value += 1
                else:
                    if (player.width >= 30):
                        player.width -= 10
                        player.height -= 10
                    score.value -= 1
                # Remove any bubble that was hit.
                bubbles.remove(bubble)
            # Removes a bubble if it is below the canvas.
            if (bubble.top >= 400):
                bubbles.remove(bubble)

onSteps(10)
app.paused = True


# -
app.background = gradient('lightBlue', 'aliceBlue', start='top')
app.stepsPerSecond = 20
app.stepsSinceNewBubble = 0
app.gameOver = False

Label('Score:', 50, 370, size=20, bold=True)
score = Label(0, 100, 370, size=20, bold=True)

# bubbles
bubbles = Group()
bubbles.bubbleColor = gradient(rgb(255, 215, 230), rgb(255, 0, 100),
                               start='right-top')
bubbles.speed = 8

# player
player = Group(
    Polygon(200, 330, 180, 380, 195, 370, 205, 370, 220, 380,
            fill='white', border='lightSteelBlue'),
    Polygon(200, 330, 195, 370, 200, 380, 205, 370, fill='whiteSmoke',
            border='lightSteelBlue'),
    Line(200, 330, 200, 380, fill='lightSteelBlue')
    )

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

def drawBubble():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    letterIndex = randrange(0, 52)
    letter = alphabet[letterIndex]

    # Change the color of the letter based on if it's uppercase or lowercase.
    if (letter.isupper() == True):
        letterColor = 'dodgerBlue'
    else:
        letterColor = 'crimson'
    # Gets the position, radius, and color, then draws the bubble.
    bubbleX = randrange(0, 400)
    bubbleRadius = randrange(15, 66)
    changeBubbleColor()
    bubble = Group(
        Circle(bubbleX, 0, bubbleRadius, fill=bubbles.bubbleColor,
               opacity=40),
        Label(letter, bubbleX, 0, fill=letterColor, size=20, bold=True)
        )
    bubble.letter = letter

    bubbles.add(bubble)

def onMouseMove(mouseX, mouseY):
    player.centerX = mouseX
    player.centerY = mouseY

def onStep():
    if (app.gameOver == False):
        app.stepsSinceNewBubble += 1

        # Creates a new bubble every 8 steps.
        if (app.stepsSinceNewBubble % 8 == 0):
            drawBubble()

        # Moves the bubbles down.
        bubbles.centerY += bubbles.speed
        for bubble in bubbles.children:
            # Check if the player is hitting the bubble.
            # Depending on if the letter is lowercase or uppercase, either
            # add or subtract from the player width, height, and score.
            if (player.hitsShape(bubble) == True):
                if (bubble.letter.islower() == True):
                    player.width += 10
                    player.height += 10
                    score.value += 1
                else:
                    if (player.width >= 30):
                        player.width -= 10
                        player.height -= 10
                    score.value -= 1
                # Remove any bubble that was hit.
                bubbles.remove(bubble)
            # Removes a bubble if it is below the canvas.
            if (bubble.top >= 400):
                bubbles.remove(bubble)

onSteps(10)
onMouseMove(100, 300)
app.paused = True


# -
app.background = gradient('lightBlue', 'aliceBlue', start='top')
app.stepsPerSecond = 20
app.stepsSinceNewBubble = 0
app.gameOver = False

Label('Score:', 50, 370, size=20, bold=True)
score = Label(0, 100, 370, size=20, bold=True)

# bubbles
bubbles = Group()
bubbles.bubbleColor = gradient(rgb(255, 215, 230), rgb(255, 0, 100),
                               start='right-top')
bubbles.speed = 8

# player
player = Group(
    Polygon(200, 330, 180, 380, 195, 370, 205, 370, 220, 380,
            fill='white', border='lightSteelBlue'),
    Polygon(200, 330, 195, 370, 200, 380, 205, 370, fill='whiteSmoke',
            border='lightSteelBlue'),
    Line(200, 330, 200, 380, fill='lightSteelBlue')
    )

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

def drawBubble():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    letterIndex = randrange(0, 52)
    letter = alphabet[letterIndex]

    # Change the color of the letter based on if it's uppercase or lowercase.
    if (letter.isupper() == True):
        letterColor = 'dodgerBlue'
    else:
        letterColor = 'crimson'
    # Gets the position, radius, and color, then draws the bubble.
    bubbleX = randrange(0, 400)
    bubbleRadius = randrange(15, 66)
    changeBubbleColor()
    bubble = Group(
        Circle(bubbleX, 0, bubbleRadius, fill=bubbles.bubbleColor,
               opacity=40),
        Label(letter, bubbleX, 0, fill=letterColor, size=20, bold=True)
        )
    bubble.letter = letter

    bubbles.add(bubble)

def onMouseMove(mouseX, mouseY):
    player.centerX = mouseX
    player.centerY = mouseY

def onStep():
    if (app.gameOver == False):
        app.stepsSinceNewBubble += 1

        # Creates a new bubble every 8 steps.
        if (app.stepsSinceNewBubble % 8 == 0):
            drawBubble()

        # Moves the bubbles down.
        bubbles.centerY += bubbles.speed
        for bubble in bubbles.children:
            # Check if the player is hitting the bubble.
            # Depending on if the letter is lowercase or uppercase, either
            # add or subtract from the player width, height, and score.
            if (player.hitsShape(bubble) == True):
                if (bubble.letter.islower() == True):
                    player.width += 10
                    player.height += 10
                    score.value += 1
                else:
                    if (player.width >= 30):
                        player.width -= 10
                        player.height -= 10
                    score.value -= 1
                # Remove any bubble that was hit.
                bubbles.remove(bubble)
            # Removes a bubble if it is below the canvas.
            if (bubble.top >= 400):
                bubbles.remove(bubble)

player.width = 400
player.height = 100
onSteps(50)
onMouseMove(200, 200)
onStep()
app.paused = True

