app.background = gradient('sienna', 'saddleBrown', start='left-top')

app.alphabet = 'CSAcademyRocks'

# Keeps track of how many labels have been drawn.
app.successes = 0

# bowl of letter-less soup
Circle(200, 200, 125, fill='lightBlue')
soup = Star(200, 200, 100, 15, fill='tomato', roundness=97)
Arc(240, 160, 40, 40, 300, 180, fill='silver')
Rect(268, 53, 10, 100, fill='silver', rotateAngle=30)
Circle(297, 60, 5, fill='silver')
Label('Press space to pour a bowl of alphabet soup!', 200, 360, size=16,
      bold=True)

labels = Group()

def drawLabel():
    # Gets a random position and opacity.
    centerX = randrange(60, 340)
    centerY = randrange(60, 340)
    randOpacity = randrange(20, 80)

    # Get a random letter from the alphabet.
    index = randrange(0, len(app.alphabet))
    letter = app.alphabet[index]
    # If the new position is in the soup and not already in
    # the labels group, draw the label and add to app.successes.
    if ((soup.contains(centerX, centerY) == True) and
        (labels.contains(centerX, centerY) == False)):
        labels.add(
            Label(letter, centerX, centerY, fill='lemonChiffon', size=16,
                  opacity=randOpacity, bold=True)
            )
        app.successes += 1
def drawLettersInSoup():
    # While fewer than 100 letters have been drawn, draw another label.
    while (app.successes < 100):
        drawLabel()
def onKeyPress(key):
    # When space is pressed, draws a new bowl of soup.
    if (key == 'space'):
        app.successes = 0
        labels.clear()
        drawLettersInSoup()

onKeyPress('space')


# -
app.background = gradient('sienna', 'saddleBrown', start='left-top')

app.alphabet = 'CSAcademyRocks'

# Keeps track of how many labels have been drawn.
app.successes = 0

# bowl of letter-less soup
Circle(200, 200, 125, fill='lightBlue')
soup = Star(200, 200, 100, 15, fill='tomato', roundness=97)
Arc(240, 160, 40, 40, 300, 180, fill='silver')
Rect(268, 53, 10, 100, fill='silver', rotateAngle=30)
Circle(297, 60, 5, fill='silver')
Label('Press space to pour a bowl of alphabet soup!', 200, 360, size=16,
      bold=True)

labels = Group()

def drawLabel():
    # Gets a random position and opacity.
    centerX = randrange(60, 340)
    centerY = randrange(60, 340)
    randOpacity = randrange(20, 80)

    # Get a random letter from the alphabet.
    index = randrange(0, len(app.alphabet))
    letter = app.alphabet[index]
    # If the new position is in the soup and not already in
    # the labels group, draw the label and add to app.successes.
    if ((soup.contains(centerX, centerY) == True) and
        (labels.contains(centerX, centerY) == False)):
        labels.add(
            Label(letter, centerX, centerY, fill='lemonChiffon', size=16,
                  opacity=randOpacity, bold=True)
            )
        app.successes += 1
def drawLettersInSoup():
    # While fewer than 100 letters have been drawn, draw another label.
    while (app.successes < 100):
        drawLabel()
def onKeyPress(key):
    # When space is pressed, draws a new bowl of soup.
    if (key == 'space'):
        app.successes = 0
        labels.clear()
        drawLettersInSoup()

onKeyPress('space')


# -
app.background = gradient('sienna', 'saddleBrown', start='left-top')

app.alphabet = 'CSAcademyRocks'

# Keeps track of how many labels have been drawn.
app.successes = 0

# bowl of letter-less soup
Circle(200, 200, 125, fill='lightBlue')
soup = Star(200, 200, 100, 15, fill='tomato', roundness=97)
Arc(240, 160, 40, 40, 300, 180, fill='silver')
Rect(268, 53, 10, 100, fill='silver', rotateAngle=30)
Circle(297, 60, 5, fill='silver')
Label('Press space to pour a bowl of alphabet soup!', 200, 360, size=16,
      bold=True)

labels = Group()

def drawLabel():
    # Gets a random position and opacity.
    centerX = randrange(60, 340)
    centerY = randrange(60, 340)
    randOpacity = randrange(20, 80)

    # Get a random letter from the alphabet.
    index = randrange(0, len(app.alphabet))
    letter = app.alphabet[index]
    # If the new position is in the soup and not already in
    # the labels group, draw the label and add to app.successes.
    if ((soup.contains(centerX, centerY) == True) and
        (labels.contains(centerX, centerY) == False)):
        labels.add(
            Label(letter, centerX, centerY, fill='lemonChiffon', size=16,
                  opacity=randOpacity, bold=True)
            )
        app.successes += 1
def drawLettersInSoup():
    # While fewer than 100 letters have been drawn, draw another label.
    while (app.successes < 100):
        drawLabel()
def onKeyPress(key):
    # When space is pressed, draws a new bowl of soup.
    if (key == 'space'):
        app.successes = 0
        labels.clear()
        drawLettersInSoup()


