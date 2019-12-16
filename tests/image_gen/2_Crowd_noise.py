app.background = 'deepSkyBlue'
app.stepsPerSecond = 4

# This is used to store the input sentence.
app.sentence = ''
app.colors = [ 'crimson', 'gold', 'cornflowerBlue', 'seaGreen' ]

# speech bubble
Polygon(0, 0, 400, 0, 400, 175, 300, 175, 315, 195, 270, 175, 130, 175, 85, 195,
        100, 175, 0, 175, fill='aliceBlue', border='black')

app.words = [ ]

def createPeople():
    headColors = [ 'saddleBrown', 'peachPuff', 'burlywood', 'tan' ]

    # Draws a crowd of people of random colors.
    for row in range(6):
        for col in range(9):
            color = choice(app.colors)
            headColor = choice(headColors)

            if (row % 2 == 0):
                x = 50 * col + 25
            else:
                x = 50 * col
            y = 30 * row + 280

            Circle(x, y - 65, 15, fill=headColor, border='black')
            Arc(x, y, 50, 100, 270, 180, fill=color, border='black')

createPeople()

# speech bubble
Line(0, 175, 100, 175)
Line(100, 175, 85, 195)
Line(85, 195, 130, 175)
Line(130, 175, 270, 175)
Line(300, 175, 315, 195)
Line(315, 195, 270, 175)
Line(300, 175, 400, 175)

def onKeyPress(key):
    # Gets a new sentence.
    if (key == 'space'):
        app.sentence = app.getTextInput('Enter a sentence')

def getJumbledLetters(sentence):
    # Gets a random step between 1 and half the length of the text.
    letters = ''
    halfLength = (len(sentence) // 2) + 1
    step = randrange(1, halfLength)

    # Create a jumbled version of the input sentece by looping over the sentence
    # using step to pick the letters. Then return the letters variable.
    for i in range(0, len(sentence), step):
        letters += sentence[i]
    return letters
def onStep():
    # Removes a word if there are too many.
    if (len(app.words) >= 10):
        word = app.words.pop(0)
        word.visible = False


    # Create a list of jumbled letters and set it to the letters variable.
    letters = getJumbledLetters(app.sentence)
    # Draws a new random label with the letters and add it to the words group.
    app.words.append(
        Label(letters.upper(), randrange(50, 351), randrange(50, 151),
              fill=choice(app.colors), size=randrange(14, 40),
              rotateAngle=randrange(0, 360), bold=True)
        )

app.setTextInputs('laugh out loud')
onKeyPress('space')
onSteps(20)
app.paused = True


# -
app.background = 'deepSkyBlue'
app.stepsPerSecond = 4

# This is used to store the input sentence.
app.sentence = ''
app.colors = [ 'crimson', 'gold', 'cornflowerBlue', 'seaGreen' ]

# speech bubble
Polygon(0, 0, 400, 0, 400, 175, 300, 175, 315, 195, 270, 175, 130, 175, 85, 195,
        100, 175, 0, 175, fill='aliceBlue', border='black')

app.words = [ ]

def createPeople():
    headColors = [ 'saddleBrown', 'peachPuff', 'burlywood', 'tan' ]

    # Draws a crowd of people of random colors.
    for row in range(6):
        for col in range(9):
            color = choice(app.colors)
            headColor = choice(headColors)

            if (row % 2 == 0):
                x = 50 * col + 25
            else:
                x = 50 * col
            y = 30 * row + 280

            Circle(x, y - 65, 15, fill=headColor, border='black')
            Arc(x, y, 50, 100, 270, 180, fill=color, border='black')

createPeople()

# speech bubble
Line(0, 175, 100, 175)
Line(100, 175, 85, 195)
Line(85, 195, 130, 175)
Line(130, 175, 270, 175)
Line(300, 175, 315, 195)
Line(315, 195, 270, 175)
Line(300, 175, 400, 175)

def onKeyPress(key):
    # Gets a new sentence.
    if (key == 'space'):
        app.sentence = app.getTextInput('Enter a sentence')

def getJumbledLetters(sentence):
    # Gets a random step between 1 and half the length of the text.
    letters = ''
    halfLength = (len(sentence) // 2) + 1
    step = randrange(1, halfLength)

    # Create a jumbled version of the input sentece by looping over the sentence
    # using step to pick the letters. Then return the letters variable.
    for i in range(0, len(sentence), step):
        letters += sentence[i]
    return letters
def onStep():
    # Removes a word if there are too many.
    if (len(app.words) >= 10):
        word = app.words.pop(0)
        word.visible = False


    # Create a list of jumbled letters and set it to the letters variable.
    letters = getJumbledLetters(app.sentence)
    # Draws a new random label with the letters and add it to the words group.
    app.words.append(
        Label(letters.upper(), randrange(50, 351), randrange(50, 151),
              fill=choice(app.colors), size=randrange(14, 40),
              rotateAngle=randrange(0, 360), bold=True)
        )

app.setTextInputs('CS Academy is cool')
onKeyPress('space')
onSteps(5)
app.paused = True


# -
app.background = 'deepSkyBlue'
app.stepsPerSecond = 4

# This is used to store the input sentence.
app.sentence = ''
app.colors = [ 'crimson', 'gold', 'cornflowerBlue', 'seaGreen' ]

# speech bubble
Polygon(0, 0, 400, 0, 400, 175, 300, 175, 315, 195, 270, 175, 130, 175, 85, 195,
        100, 175, 0, 175, fill='aliceBlue', border='black')

app.words = [ ]

def createPeople():
    headColors = [ 'saddleBrown', 'peachPuff', 'burlywood', 'tan' ]

    # Draws a crowd of people of random colors.
    for row in range(6):
        for col in range(9):
            color = choice(app.colors)
            headColor = choice(headColors)

            if (row % 2 == 0):
                x = 50 * col + 25
            else:
                x = 50 * col
            y = 30 * row + 280

            Circle(x, y - 65, 15, fill=headColor, border='black')
            Arc(x, y, 50, 100, 270, 180, fill=color, border='black')

createPeople()

# speech bubble
Line(0, 175, 100, 175)
Line(100, 175, 85, 195)
Line(85, 195, 130, 175)
Line(130, 175, 270, 175)
Line(300, 175, 315, 195)
Line(315, 195, 270, 175)
Line(300, 175, 400, 175)

def onKeyPress(key):
    # Gets a new sentence.
    if (key == 'space'):
        app.sentence = app.getTextInput('Enter a sentence')

def getJumbledLetters(sentence):
    # Gets a random step between 1 and half the length of the text.
    letters = ''
    halfLength = (len(sentence) // 2) + 1
    step = randrange(1, halfLength)

    # Create a jumbled version of the input sentece by looping over the sentence
    # using step to pick the letters. Then return the letters variable.
    for i in range(0, len(sentence), step):
        letters += sentence[i]
    return letters
def onStep():
    # Removes a word if there are too many.
    if (len(app.words) >= 10):
        word = app.words.pop(0)
        word.visible = False


    # Create a list of jumbled letters and set it to the letters variable.
    letters = getJumbledLetters(app.sentence)
    # Draws a new random label with the letters and add it to the words group.
    app.words.append(
        Label(letters.upper(), randrange(50, 351), randrange(50, 151),
              fill=choice(app.colors), size=randrange(14, 40),
              rotateAngle=randrange(0, 360), bold=True)
        )


