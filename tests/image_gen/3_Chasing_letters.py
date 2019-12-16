app.background = 'black'
app.stepsPerSecond = 12

app.alphabet = 'abcdefghijklmnopqrstuvwxyz'
app.currentIndex = 0

letters = Group()

def drawLetters():
    # Draws the letters evenly spaced and add them to the letters group.
    spacing = 395 / len(app.alphabet)
    for i in range(len(app.alphabet)):
        x = 10 + i * spacing
        letters.add(
            Label(app.alphabet[i], x, 200, fill='white', size=15, bold=True)
            )

drawLetters()

def onStep():
    # Get the current letter by using the alphabet and app.currentIndex.
    currentLetter = app.alphabet[app.currentIndex]
    # Loops over the letters Group.
    for letter in letters:
        # Set the currentLetter's fill to red and increase its size.
        if (letter.value == currentLetter):
            letter.fill = 'red'
            letter.size = 36
        # Set all other letters' fills to white and decrease their size.
        else:
            letter.fill = 'white'
            if (letter.size > 15):
                letter.size -= 3
    # Increases the currentIndex by 1 and reset to 0 if the end of the
    # alphabet is reached.
    app.currentIndex += 1
    if (app.currentIndex == len(app.alphabet)):
        app.currentIndex = 0

onSteps(10)
app.paused = True


# -
app.background = 'black'
app.stepsPerSecond = 12

app.alphabet = 'abcdefghijklmnopqrstuvwxyz'
app.currentIndex = 0

letters = Group()

def drawLetters():
    # Draws the letters evenly spaced and add them to the letters group.
    spacing = 395 / len(app.alphabet)
    for i in range(len(app.alphabet)):
        x = 10 + i * spacing
        letters.add(
            Label(app.alphabet[i], x, 200, fill='white', size=15, bold=True)
            )

drawLetters()

def onStep():
    # Get the current letter by using the alphabet and app.currentIndex.
    currentLetter = app.alphabet[app.currentIndex]
    # Loops over the letters Group.
    for letter in letters:
        # Set the currentLetter's fill to red and increase its size.
        if (letter.value == currentLetter):
            letter.fill = 'red'
            letter.size = 36
        # Set all other letters' fills to white and decrease their size.
        else:
            letter.fill = 'white'
            if (letter.size > 15):
                letter.size -= 3
    # Increases the currentIndex by 1 and reset to 0 if the end of the
    # alphabet is reached.
    app.currentIndex += 1
    if (app.currentIndex == len(app.alphabet)):
        app.currentIndex = 0

onSteps(25)
app.paused = True


# -
app.background = 'black'
app.stepsPerSecond = 12

app.alphabet = 'abcdefghijklmnopqrstuvwxyz'
app.currentIndex = 0

letters = Group()

def drawLetters():
    # Draws the letters evenly spaced and add them to the letters group.
    spacing = 395 / len(app.alphabet)
    for i in range(len(app.alphabet)):
        x = 10 + i * spacing
        letters.add(
            Label(app.alphabet[i], x, 200, fill='white', size=15, bold=True)
            )

drawLetters()

def onStep():
    # Get the current letter by using the alphabet and app.currentIndex.
    currentLetter = app.alphabet[app.currentIndex]
    # Loops over the letters Group.
    for letter in letters:
        # Set the currentLetter's fill to red and increase its size.
        if (letter.value == currentLetter):
            letter.fill = 'red'
            letter.size = 36
        # Set all other letters' fills to white and decrease their size.
        else:
            letter.fill = 'white'
            if (letter.size > 15):
                letter.size -= 3
    # Increases the currentIndex by 1 and reset to 0 if the end of the
    # alphabet is reached.
    app.currentIndex += 1
    if (app.currentIndex == len(app.alphabet)):
        app.currentIndex = 0

onSteps(25)
app.paused = True

