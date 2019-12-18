app.background = 'saddleBrown'

Polygon(0, 400, 0, 230, 15, 165, 385, 165, 400, 230, 400, 400, fill='sienna')
Line(15, 80, 15, 165, fill='sienna')
Line(385, 80, 385, 165, fill='sienna')

Polygon(0, 0, 0, 145, 15, 80, 385, 80, 400, 145, 400, 0, fill='lavender')
Polygon(0, 145, 15, 80, 385, 80, 400, 145, 400, 70, 10, 70, 0, 110,
        fill='saddleBrown', border='sienna')

# typewriter
Circle(315, 210, 25, fill='darkGray')
Polygon(50, 225, 350, 225, 360, 325, 40, 325, fill=rgb(100, 160, 210))
Polygon(50, 225, 350, 225, 300, 175, 100, 175, fill='steelBlue')
Polygon(105, 190, 295, 190, 275, 80, 125, 80, fill='white', border='darkGray')
Rect(100, 185, 200, 10, fill='darkGray')

# message
app.messageText = 'ilovetocode'
app.index = 0

letters = Group()
message = Label('', 200, 150, size=18, font='monospace')

def drawKeyboard():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    x = 80
    y = 250

    # For each letter in the alphabet, draws the key.
    for letter in alphabet:
        # Moves to the next line when the key would be drawn past x=340.
        if (x > 340):
            x = 80
            y += 25

        # Draws the key.
        letterKey = Oval(x, y, 30, 20, fill='dimGray')
        Label(letter, x, y, fill='white', size=14, font='monospace')

        # Keeps track of the letters drawn.
        letterKey.letter = letter
        letters.add(letterKey)

        # Moves to the next location to draw the letter.
        x += 30

def highlightNextLetter():
    # If app.index goes beyond the length of the message, reset it.
    # Then, use the index to get the selected letter from app.messageText.
    if (app.index == len(app.messageText)):
        app.index = 0
    app.selectedLetter = app.messageText[app.index]
    # Change the border of the key that matches app.selectedLetter.
    for letterKey in letters.children:
        if (letterKey.letter == app.selectedLetter):
            letterKey.fill = 'darkGreen'
        else:
            letterKey.fill = 'dimGray'
drawKeyboard()
highlightNextLetter()

def onKeyPress(key):
    # When the selected letter is pressed, increase the index, highlight
    # the next letter, and add the key to the message.
    if (key == app.selectedLetter):
        app.index += 1
        highlightNextLetter()
        message.value += key

onKeyPress('j')


# -
app.background = 'saddleBrown'

Polygon(0, 400, 0, 230, 15, 165, 385, 165, 400, 230, 400, 400, fill='sienna')
Line(15, 80, 15, 165, fill='sienna')
Line(385, 80, 385, 165, fill='sienna')

Polygon(0, 0, 0, 145, 15, 80, 385, 80, 400, 145, 400, 0, fill='lavender')
Polygon(0, 145, 15, 80, 385, 80, 400, 145, 400, 70, 10, 70, 0, 110,
        fill='saddleBrown', border='sienna')

# typewriter
Circle(315, 210, 25, fill='darkGray')
Polygon(50, 225, 350, 225, 360, 325, 40, 325, fill=rgb(100, 160, 210))
Polygon(50, 225, 350, 225, 300, 175, 100, 175, fill='steelBlue')
Polygon(105, 190, 295, 190, 275, 80, 125, 80, fill='white', border='darkGray')
Rect(100, 185, 200, 10, fill='darkGray')

# message
app.messageText = 'ilovetocode'
app.index = 0

letters = Group()
message = Label('', 200, 150, size=18, font='monospace')

def drawKeyboard():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    x = 80
    y = 250

    # For each letter in the alphabet, draws the key.
    for letter in alphabet:
        # Moves to the next line when the key would be drawn past x=340.
        if (x > 340):
            x = 80
            y += 25

        # Draws the key.
        letterKey = Oval(x, y, 30, 20, fill='dimGray')
        Label(letter, x, y, fill='white', size=14, font='monospace')

        # Keeps track of the letters drawn.
        letterKey.letter = letter
        letters.add(letterKey)

        # Moves to the next location to draw the letter.
        x += 30

def highlightNextLetter():
    # If app.index goes beyond the length of the message, reset it.
    # Then, use the index to get the selected letter from app.messageText.
    if (app.index == len(app.messageText)):
        app.index = 0
    app.selectedLetter = app.messageText[app.index]
    # Change the border of the key that matches app.selectedLetter.
    for letterKey in letters.children:
        if (letterKey.letter == app.selectedLetter):
            letterKey.fill = 'darkGreen'
        else:
            letterKey.fill = 'dimGray'
drawKeyboard()
highlightNextLetter()

def onKeyPress(key):
    # When the selected letter is pressed, increase the index, highlight
    # the next letter, and add the key to the message.
    if (key == app.selectedLetter):
        app.index += 1
        highlightNextLetter()
        message.value += key

onKeyPress('i')


# -
app.background = 'saddleBrown'

Polygon(0, 400, 0, 230, 15, 165, 385, 165, 400, 230, 400, 400, fill='sienna')
Line(15, 80, 15, 165, fill='sienna')
Line(385, 80, 385, 165, fill='sienna')

Polygon(0, 0, 0, 145, 15, 80, 385, 80, 400, 145, 400, 0, fill='lavender')
Polygon(0, 145, 15, 80, 385, 80, 400, 145, 400, 70, 10, 70, 0, 110,
        fill='saddleBrown', border='sienna')

# typewriter
Circle(315, 210, 25, fill='darkGray')
Polygon(50, 225, 350, 225, 360, 325, 40, 325, fill=rgb(100, 160, 210))
Polygon(50, 225, 350, 225, 300, 175, 100, 175, fill='steelBlue')
Polygon(105, 190, 295, 190, 275, 80, 125, 80, fill='white', border='darkGray')
Rect(100, 185, 200, 10, fill='darkGray')

# message
app.messageText = 'ilovetocode'
app.index = 0

letters = Group()
message = Label('', 200, 150, size=18, font='monospace')

def drawKeyboard():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    x = 80
    y = 250

    # For each letter in the alphabet, draws the key.
    for letter in alphabet:
        # Moves to the next line when the key would be drawn past x=340.
        if (x > 340):
            x = 80
            y += 25

        # Draws the key.
        letterKey = Oval(x, y, 30, 20, fill='dimGray')
        Label(letter, x, y, fill='white', size=14, font='monospace')

        # Keeps track of the letters drawn.
        letterKey.letter = letter
        letters.add(letterKey)

        # Moves to the next location to draw the letter.
        x += 30

def highlightNextLetter():
    # If app.index goes beyond the length of the message, reset it.
    # Then, use the index to get the selected letter from app.messageText.
    if (app.index == len(app.messageText)):
        app.index = 0
    app.selectedLetter = app.messageText[app.index]
    # Change the border of the key that matches app.selectedLetter.
    for letterKey in letters.children:
        if (letterKey.letter == app.selectedLetter):
            letterKey.fill = 'darkGreen'
        else:
            letterKey.fill = 'dimGray'
drawKeyboard()
highlightNextLetter()

def onKeyPress(key):
    # When the selected letter is pressed, increase the index, highlight
    # the next letter, and add the key to the message.
    if (key == app.selectedLetter):
        app.index += 1
        highlightNextLetter()
        message.value += key

onKeyPress('i')
onKeyPress('l')
onKeyPress('o')
onKeyPress('v')
onKeyPress('e')
onKeyPress('t')
onKeyPress('o')
onKeyPress('c')
onKeyPress('o')
onKeyPress('d')
onKeyPress('e')

