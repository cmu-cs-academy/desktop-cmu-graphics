app.background = gradient('tan', 'sienna', start='left-top')
app.stepsPerSecond = 20

app.x = 40
app.y = 90
app.words = [ 'the', 'dog', 'cat', 'was', 'blue', 'nice', 'and' ]

# book
Rect(25, 75, 350, 250, fill='fireBrick')
Oval(200, 325, 60, 10, fill='fireBrick')
Rect(225, 25, 20, 55, fill='red')
Polygon(225, 25, 225, 15, 235, 20, 245, 15, 245, 25, fill='red')
Rect(30, 80, 340, 240, fill='white')
Line(200, 80, 200, 320, lineWidth=5, opacity=10)

def drawWord(word):
    # Draws a word at the current app location.
    x = app.x + 2 * len(word)
    Label(word, x, app.y, size=9)

def onKeyPress(key):
    # If 'space' is pressed, ask the user to 'Type a word' and add
    # it to app.words.
    if (key == 'space'):
        newWord = app.getTextInput('Type a word')
        app.words.append(newWord)
    # If r is pressed, get rid of the last word in app.words.
    elif ((key == 'r') and (len(app.words) > 0)):
        app.words.pop()
def onStep():
    # Gets a new random word from app.words and draws it.
    if (len(app.words) > 0):
        newWord = choice(app.words)
        drawWord(newWord)

    # Moves where we will draw the next word.
    app.x += 20
    if ((app.x < 215) and (app.x > 180)):
        app.y += 10
        app.x = 40
    elif (app.x > 350):
        app.y += 10
        app.x = 215
    if ((app.y > 310) and (app.x < 200)):
        app.x = 215
        app.y = 90
    elif ((app.y > 310) and (app.x > 200)):
        app.paused = True

onKeyPress('r')
app.setTextInputs('or')
onKeyPress('space')
onSteps(50)
app.paused = True


# -
app.background = gradient('tan', 'sienna', start='left-top')
app.stepsPerSecond = 20

app.x = 40
app.y = 90
app.words = [ 'the', 'dog', 'cat', 'was', 'blue', 'nice', 'and' ]

# book
Rect(25, 75, 350, 250, fill='fireBrick')
Oval(200, 325, 60, 10, fill='fireBrick')
Rect(225, 25, 20, 55, fill='red')
Polygon(225, 25, 225, 15, 235, 20, 245, 15, 245, 25, fill='red')
Rect(30, 80, 340, 240, fill='white')
Line(200, 80, 200, 320, lineWidth=5, opacity=10)

def drawWord(word):
    # Draws a word at the current app location.
    x = app.x + 2 * len(word)
    Label(word, x, app.y, size=9)

def onKeyPress(key):
    # If 'space' is pressed, ask the user to 'Type a word' and add
    # it to app.words.
    if (key == 'space'):
        newWord = app.getTextInput('Type a word')
        app.words.append(newWord)
    # If r is pressed, get rid of the last word in app.words.
    elif ((key == 'r') and (len(app.words) > 0)):
        app.words.pop()
def onStep():
    # Gets a new random word from app.words and draws it.
    if (len(app.words) > 0):
        newWord = choice(app.words)
        drawWord(newWord)

    # Moves where we will draw the next word.
    app.x += 20
    if ((app.x < 215) and (app.x > 180)):
        app.y += 10
        app.x = 40
    elif (app.x > 350):
        app.y += 10
        app.x = 215
    if ((app.y > 310) and (app.x < 200)):
        app.x = 215
        app.y = 90
    elif ((app.y > 310) and (app.x > 200)):
        app.paused = True

onStep()
app.paused = True


# -
app.background = gradient('tan', 'sienna', start='left-top')
app.stepsPerSecond = 20

app.x = 40
app.y = 90
app.words = [ 'the', 'dog', 'cat', 'was', 'blue', 'nice', 'and' ]

# book
Rect(25, 75, 350, 250, fill='fireBrick')
Oval(200, 325, 60, 10, fill='fireBrick')
Rect(225, 25, 20, 55, fill='red')
Polygon(225, 25, 225, 15, 235, 20, 245, 15, 245, 25, fill='red')
Rect(30, 80, 340, 240, fill='white')
Line(200, 80, 200, 320, lineWidth=5, opacity=10)

def drawWord(word):
    # Draws a word at the current app location.
    x = app.x + 2 * len(word)
    Label(word, x, app.y, size=9)

def onKeyPress(key):
    # If 'space' is pressed, ask the user to 'Type a word' and add
    # it to app.words.
    if (key == 'space'):
        newWord = app.getTextInput('Type a word')
        app.words.append(newWord)
    # If r is pressed, get rid of the last word in app.words.
    elif ((key == 'r') and (len(app.words) > 0)):
        app.words.pop()
def onStep():
    # Gets a new random word from app.words and draws it.
    if (len(app.words) > 0):
        newWord = choice(app.words)
        drawWord(newWord)

    # Moves where we will draw the next word.
    app.x += 20
    if ((app.x < 215) and (app.x > 180)):
        app.y += 10
        app.x = 40
    elif (app.x > 350):
        app.y += 10
        app.x = 215
    if ((app.y > 310) and (app.x < 200)):
        app.x = 215
        app.y = 90
    elif ((app.y > 310) and (app.x > 200)):
        app.paused = True

onKeyPress('r')
onKeyPress('r')
onSteps(50)
app.paused = True

