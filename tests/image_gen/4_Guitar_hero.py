app.background = gradient('saddleBrown', 'sienna', 'saddleBrown', start='left')
app.stepsPerSecond = 50

# scoreboard
score = Label(0, 200, 25, size=32)

# guitar strings
Line(50, 0, 50, 400, lineWidth=5, opacity=75)
Line(150, 0, 150, 400, lineWidth=5, opacity=75)
Line(250, 0, 250, 400, lineWidth=5, opacity=75)
Line(350, 0, 350, 400, lineWidth=5, opacity=75)

# buttons
buttons = Group()
aButton = Circle(50, 325, 30, fill='saddleBrown', border='lime', borderWidth=5)
aButton.name = 'a'
sButton = Circle(150, 325, 30, fill='saddleBrown', border='red', borderWidth=5)
sButton.name = 's'
dButton = Circle(250, 325, 30, fill='saddleBrown', border='yellow', borderWidth=5)
dButton.name = 'd'
fButton = Circle(350, 325, 30,  fill='saddleBrown', border='cyan', borderWidth=5)
fButton.name = 'f'
buttons.add(aButton, sButton, dButton, fButton)

Label('a', 50, 325, size=25)
Label('s', 150, 325, size=25)
Label('d', 250, 325, size=25)
Label('f', 350, 325, size=25)

Label('Guitar Hero', 200, 375, fill='white', size=32)

notes = Group()

def moveNotes():
    # First, move all the notes down by 5 at once.
    notes.top += 5
    # Any note that is offscreen should be removed, and the score should
    # be decreased by 5 and made red.
    for note in notes.children:
        if (note.top > 400):
            if (score.value >= 5):
                score.value -= 5
            score.fill = 'red'
            notes.remove(note)
def addNote(string, centerY):
    # String is one of 0, 1, 2, or 3. Add a circle (a 'note') so that it is
    # on the given string.
    if (string == 0):
        color = 'lime'
    elif (string == 1):
        color = 'red'
    elif (string == 2):
        color = 'yellow'
    else:
        color = 'cyan'

    notes.add(
        Circle(50 + (string * 100), centerY, 25, fill=color)
        )

def checkNote(note):
    # Any note which is over a button that is being pressed should be
    # removed, and the score should increase by 5 and be turned green.
    for button in buttons.children:
        if ((note.hitsShape(button) == True) and
            (button.fill != 'saddleBrown')):
            score.value += 5
            score.fill = 'green'
            notes.remove(note)
def onKeyPress(key):
    # If a button's key is pressed, sets the fill to be the border color.
    for button in buttons.children:
        if (button.name == key):
            button.fill = button.border
        else:
            button.fill = 'saddleBrown'

    for note in notes.children:
        checkNote(note)

def onKeyRelease(key):
    # Resets all of the buttons to have a fill of saddleBrown.
    for button in buttons.children:
        if (button.name == key):
            button.fill = 'saddleBrown'

def onStep():
    # Makes a new note on a random string with 5% chance.
    if (randrange(0, 40) == 20):
        addNote(randrange(0, 4), -25)

    moveNotes()

addNote(1, 275)
onKeyPress('a')
app.paused = True


# -
app.background = gradient('saddleBrown', 'sienna', 'saddleBrown', start='left')
app.stepsPerSecond = 50

# scoreboard
score = Label(0, 200, 25, size=32)

# guitar strings
Line(50, 0, 50, 400, lineWidth=5, opacity=75)
Line(150, 0, 150, 400, lineWidth=5, opacity=75)
Line(250, 0, 250, 400, lineWidth=5, opacity=75)
Line(350, 0, 350, 400, lineWidth=5, opacity=75)

# buttons
buttons = Group()
aButton = Circle(50, 325, 30, fill='saddleBrown', border='lime', borderWidth=5)
aButton.name = 'a'
sButton = Circle(150, 325, 30, fill='saddleBrown', border='red', borderWidth=5)
sButton.name = 's'
dButton = Circle(250, 325, 30, fill='saddleBrown', border='yellow', borderWidth=5)
dButton.name = 'd'
fButton = Circle(350, 325, 30,  fill='saddleBrown', border='cyan', borderWidth=5)
fButton.name = 'f'
buttons.add(aButton, sButton, dButton, fButton)

Label('a', 50, 325, size=25)
Label('s', 150, 325, size=25)
Label('d', 250, 325, size=25)
Label('f', 350, 325, size=25)

Label('Guitar Hero', 200, 375, fill='white', size=32)

notes = Group()

def moveNotes():
    # First, move all the notes down by 5 at once.
    notes.top += 5
    # Any note that is offscreen should be removed, and the score should
    # be decreased by 5 and made red.
    for note in notes.children:
        if (note.top > 400):
            if (score.value >= 5):
                score.value -= 5
            score.fill = 'red'
            notes.remove(note)
def addNote(string, centerY):
    # String is one of 0, 1, 2, or 3. Add a circle (a 'note') so that it is
    # on the given string.
    if (string == 0):
        color = 'lime'
    elif (string == 1):
        color = 'red'
    elif (string == 2):
        color = 'yellow'
    else:
        color = 'cyan'

    notes.add(
        Circle(50 + (string * 100), centerY, 25, fill=color)
        )

def checkNote(note):
    # Any note which is over a button that is being pressed should be
    # removed, and the score should increase by 5 and be turned green.
    for button in buttons.children:
        if ((note.hitsShape(button) == True) and
            (button.fill != 'saddleBrown')):
            score.value += 5
            score.fill = 'green'
            notes.remove(note)
def onKeyPress(key):
    # If a button's key is pressed, sets the fill to be the border color.
    for button in buttons.children:
        if (button.name == key):
            button.fill = button.border
        else:
            button.fill = 'saddleBrown'

    for note in notes.children:
        checkNote(note)

def onKeyRelease(key):
    # Resets all of the buttons to have a fill of saddleBrown.
    for button in buttons.children:
        if (button.name == key):
            button.fill = 'saddleBrown'

def onStep():
    # Makes a new note on a random string with 5% chance.
    if (randrange(0, 40) == 20):
        addNote(randrange(0, 4), -25)

    moveNotes()

addNote(1, 100)
app.paused = True


# -
app.background = gradient('saddleBrown', 'sienna', 'saddleBrown', start='left')
app.stepsPerSecond = 50

# scoreboard
score = Label(0, 200, 25, size=32)

# guitar strings
Line(50, 0, 50, 400, lineWidth=5, opacity=75)
Line(150, 0, 150, 400, lineWidth=5, opacity=75)
Line(250, 0, 250, 400, lineWidth=5, opacity=75)
Line(350, 0, 350, 400, lineWidth=5, opacity=75)

# buttons
buttons = Group()
aButton = Circle(50, 325, 30, fill='saddleBrown', border='lime', borderWidth=5)
aButton.name = 'a'
sButton = Circle(150, 325, 30, fill='saddleBrown', border='red', borderWidth=5)
sButton.name = 's'
dButton = Circle(250, 325, 30, fill='saddleBrown', border='yellow', borderWidth=5)
dButton.name = 'd'
fButton = Circle(350, 325, 30,  fill='saddleBrown', border='cyan', borderWidth=5)
fButton.name = 'f'
buttons.add(aButton, sButton, dButton, fButton)

Label('a', 50, 325, size=25)
Label('s', 150, 325, size=25)
Label('d', 250, 325, size=25)
Label('f', 350, 325, size=25)

Label('Guitar Hero', 200, 375, fill='white', size=32)

notes = Group()

def moveNotes():
    # First, move all the notes down by 5 at once.
    notes.top += 5
    # Any note that is offscreen should be removed, and the score should
    # be decreased by 5 and made red.
    for note in notes.children:
        if (note.top > 400):
            if (score.value >= 5):
                score.value -= 5
            score.fill = 'red'
            notes.remove(note)
def addNote(string, centerY):
    # String is one of 0, 1, 2, or 3. Add a circle (a 'note') so that it is
    # on the given string.
    if (string == 0):
        color = 'lime'
    elif (string == 1):
        color = 'red'
    elif (string == 2):
        color = 'yellow'
    else:
        color = 'cyan'

    notes.add(
        Circle(50 + (string * 100), centerY, 25, fill=color)
        )

def checkNote(note):
    # Any note which is over a button that is being pressed should be
    # removed, and the score should increase by 5 and be turned green.
    for button in buttons.children:
        if ((note.hitsShape(button) == True) and
            (button.fill != 'saddleBrown')):
            score.value += 5
            score.fill = 'green'
            notes.remove(note)
def onKeyPress(key):
    # If a button's key is pressed, sets the fill to be the border color.
    for button in buttons.children:
        if (button.name == key):
            button.fill = button.border
        else:
            button.fill = 'saddleBrown'

    for note in notes.children:
        checkNote(note)

def onKeyRelease(key):
    # Resets all of the buttons to have a fill of saddleBrown.
    for button in buttons.children:
        if (button.name == key):
            button.fill = 'saddleBrown'

def onStep():
    # Makes a new note on a random string with 5% chance.
    if (randrange(0, 40) == 20):
        addNote(randrange(0, 4), -25)

    moveNotes()

addNote(1, 100)
app.paused = True

