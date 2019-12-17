app.background = gradient('cornSilk', 'wheat', start='top')

# Letters used to populate the keyboard.
app.letters = 'qwertyuiopasdfghjklzxcvbnm'

# screen borders
Rect(200, 200, 200, 340, align='center')
Rect(200, 200, 180, 360, align='center')
Circle(110, 30, 10)
Circle(110, 370, 10)
Circle(290, 30, 10)
Circle(290, 370, 10)
Rect(110, 60, 180, 265, fill='white')
Rect(200, 45, 50, 5, fill='dimGrey', align='center')
Rect(110, 60, 180, 50, fill='ghostWhite')
Line(110, 110, 290, 110, fill='gainsboro', lineWidth=1)
Circle(150, 45, 5, fill='dimGrey')
Circle(200, 30, 3, fill='dimGrey')
Circle(200, 350, 13, fill='dimGrey')

# status bar
Rect(113, 70, 2, 2, align='left-bottom')
Rect(116, 70, 2, 3, align='left-bottom')
Rect(119, 70, 2, 5, align='left-bottom')
Rect(122, 70, 2, 7, fill='lightGrey', align='left-bottom')
Label('8:00', 200, 65, size=6)
Rect(275, 63, 10, 5, fill='ghostWhite', border='grey', borderWidth=1)
Rect(276, 64, 2, 3, fill='red')

# CS Academy icon
Circle(200, 83, 11, fill='lightGray')
Label('CS', 200, 83, fill='white', size=10)
Label('CS Academy', 200, 100, size=8)

# text bubbles
Rect(120, 120, 100, 20, fill='lightGrey')
Polygon(120, 140, 130, 140, 120, 150, fill='lightGrey')
Rect(280, 150, 100, 20, fill='dodgerBlue', align='right-top')
Polygon(280, 170, 270, 170, 280, 180, fill='dodgerBlue')
Rect(120, 180, 100, 20, fill='lightGrey')
Polygon(120, 200, 130, 200, 120, 210, fill='lightGrey')

def drawKeyboard():
    # outline and buttons
    Rect(110, 235, 180, 90, fill='lightGrey')
    Rect(116, 218, 155, 15, fill='white', border='lightGrey', borderWidth=1)
    Label('Text Message', 120, 222, fill='darkGrey', size=10, align='left-top')
    Rect(275, 218, 12, 15, fill='dodgerBlue')
    Rect(281, 224, 4, 5, fill='white', align='center-top')
    Polygon(281, 220, 285, 224, 277, 224, fill='white')
    Rect(200, 308, 70, 12, fill='white', align='center-top')
    Rect(262, 285, 21, 20, fill='darkGray')
    Label('del', 272, 295, size=10)
    Rect(116, 285, 19, 20, fill='darkGray')

    # Draws all of the keys using the letters string.
    for index in range(len(app.letters)):
        letter = app.letters[index]

        # If we are in the first row.
        if (index < 10):
            x = 123 + index * 17
            y = 248
        # The second row.
        elif (index < 19):
            x = 130 + (index - 10) * 17
            y = 271
        # The third row.
        else:
            x = 147 + (index - 19) * 17
            y = 295
        Rect(x, y, 14, 20, fill='white', align='center')
        Label(letter, x, y, size=12)

capsLockArrow = Group(
    Polygon(125, 288, 131, 295, 119, 295, fill='white'),
    Rect(125, 295, 5, 7, fill='white', align='center-top')
    )

def capsLock(isCapsLockOn, text1, text2, text3):
    # If caps lock is on, all the texts should be uppercase. Otherwise they
    # should be lowercase.
    if (isCapsLockOn == True):
        app.letters = app.letters.upper()
        Label(text1.upper(), 125, 125, size=10, align='left-top')
        Label(text2.upper(), 185, 155, fill='white', size=10, align='left-top')
        Label(text3.upper(), 125, 185, size=10, align='left-top')
        # Changes the color of the capsLockArrow.
        capsLockArrow.fill = 'black'
    else:
        Label(text1.lower(), 125, 125, size=10, align='left-top')
        Label(text2.lower(), 185, 155, fill='white', size=10, align='left-top')
        Label(text3.lower(), 125, 185, size=10, align='left-top')
    # Draws the keyboard, and brings the capsLockArrow to front.
    drawKeyboard()
    capsLockArrow.toFront()

capsLock(True, 'sup ma dude', 'y u yelling?', 'sorry caps lock')


# -
app.background = gradient('cornSilk', 'wheat', start='top')

# Letters used to populate the keyboard.
app.letters = 'qwertyuiopasdfghjklzxcvbnm'

# screen borders
Rect(200, 200, 200, 340, align='center')
Rect(200, 200, 180, 360, align='center')
Circle(110, 30, 10)
Circle(110, 370, 10)
Circle(290, 30, 10)
Circle(290, 370, 10)
Rect(110, 60, 180, 265, fill='white')
Rect(200, 45, 50, 5, fill='dimGrey', align='center')
Rect(110, 60, 180, 50, fill='ghostWhite')
Line(110, 110, 290, 110, fill='gainsboro', lineWidth=1)
Circle(150, 45, 5, fill='dimGrey')
Circle(200, 30, 3, fill='dimGrey')
Circle(200, 350, 13, fill='dimGrey')

# status bar
Rect(113, 70, 2, 2, align='left-bottom')
Rect(116, 70, 2, 3, align='left-bottom')
Rect(119, 70, 2, 5, align='left-bottom')
Rect(122, 70, 2, 7, fill='lightGrey', align='left-bottom')
Label('8:00', 200, 65, size=6)
Rect(275, 63, 10, 5, fill='ghostWhite', border='grey', borderWidth=1)
Rect(276, 64, 2, 3, fill='red')

# CS Academy icon
Circle(200, 83, 11, fill='lightGray')
Label('CS', 200, 83, fill='white', size=10)
Label('CS Academy', 200, 100, size=8)

# text bubbles
Rect(120, 120, 100, 20, fill='lightGrey')
Polygon(120, 140, 130, 140, 120, 150, fill='lightGrey')
Rect(280, 150, 100, 20, fill='dodgerBlue', align='right-top')
Polygon(280, 170, 270, 170, 280, 180, fill='dodgerBlue')
Rect(120, 180, 100, 20, fill='lightGrey')
Polygon(120, 200, 130, 200, 120, 210, fill='lightGrey')

def drawKeyboard():
    # outline and buttons
    Rect(110, 235, 180, 90, fill='lightGrey')
    Rect(116, 218, 155, 15, fill='white', border='lightGrey', borderWidth=1)
    Label('Text Message', 120, 222, fill='darkGrey', size=10, align='left-top')
    Rect(275, 218, 12, 15, fill='dodgerBlue')
    Rect(281, 224, 4, 5, fill='white', align='center-top')
    Polygon(281, 220, 285, 224, 277, 224, fill='white')
    Rect(200, 308, 70, 12, fill='white', align='center-top')
    Rect(262, 285, 21, 20, fill='darkGray')
    Label('del', 272, 295, size=10)
    Rect(116, 285, 19, 20, fill='darkGray')

    # Draws all of the keys using the letters string.
    for index in range(len(app.letters)):
        letter = app.letters[index]

        # If we are in the first row.
        if (index < 10):
            x = 123 + index * 17
            y = 248
        # The second row.
        elif (index < 19):
            x = 130 + (index - 10) * 17
            y = 271
        # The third row.
        else:
            x = 147 + (index - 19) * 17
            y = 295
        Rect(x, y, 14, 20, fill='white', align='center')
        Label(letter, x, y, size=12)

capsLockArrow = Group(
    Polygon(125, 288, 131, 295, 119, 295, fill='white'),
    Rect(125, 295, 5, 7, fill='white', align='center-top')
    )

def capsLock(isCapsLockOn, text1, text2, text3):
    # If caps lock is on, all the texts should be uppercase. Otherwise they
    # should be lowercase.
    if (isCapsLockOn == True):
        app.letters = app.letters.upper()
        Label(text1.upper(), 125, 125, size=10, align='left-top')
        Label(text2.upper(), 185, 155, fill='white', size=10, align='left-top')
        Label(text3.upper(), 125, 185, size=10, align='left-top')
        # Changes the color of the capsLockArrow.
        capsLockArrow.fill = 'black'
    else:
        Label(text1.lower(), 125, 125, size=10, align='left-top')
        Label(text2.lower(), 185, 155, fill='white', size=10, align='left-top')
        Label(text3.lower(), 125, 185, size=10, align='left-top')
    # Draws the keyboard, and brings the capsLockArrow to front.
    drawKeyboard()
    capsLockArrow.toFront()

capsLock(False, 'NEW PHONE WHO DIS', 'pls stop w that lol', 'sorry sorry')


# -
app.background = gradient('cornSilk', 'wheat', start='top')

# Letters used to populate the keyboard.
app.letters = 'qwertyuiopasdfghjklzxcvbnm'

# screen borders
Rect(200, 200, 200, 340, align='center')
Rect(200, 200, 180, 360, align='center')
Circle(110, 30, 10)
Circle(110, 370, 10)
Circle(290, 30, 10)
Circle(290, 370, 10)
Rect(110, 60, 180, 265, fill='white')
Rect(200, 45, 50, 5, fill='dimGrey', align='center')
Rect(110, 60, 180, 50, fill='ghostWhite')
Line(110, 110, 290, 110, fill='gainsboro', lineWidth=1)
Circle(150, 45, 5, fill='dimGrey')
Circle(200, 30, 3, fill='dimGrey')
Circle(200, 350, 13, fill='dimGrey')

# status bar
Rect(113, 70, 2, 2, align='left-bottom')
Rect(116, 70, 2, 3, align='left-bottom')
Rect(119, 70, 2, 5, align='left-bottom')
Rect(122, 70, 2, 7, fill='lightGrey', align='left-bottom')
Label('8:00', 200, 65, size=6)
Rect(275, 63, 10, 5, fill='ghostWhite', border='grey', borderWidth=1)
Rect(276, 64, 2, 3, fill='red')

# CS Academy icon
Circle(200, 83, 11, fill='lightGray')
Label('CS', 200, 83, fill='white', size=10)
Label('CS Academy', 200, 100, size=8)

# text bubbles
Rect(120, 120, 100, 20, fill='lightGrey')
Polygon(120, 140, 130, 140, 120, 150, fill='lightGrey')
Rect(280, 150, 100, 20, fill='dodgerBlue', align='right-top')
Polygon(280, 170, 270, 170, 280, 180, fill='dodgerBlue')
Rect(120, 180, 100, 20, fill='lightGrey')
Polygon(120, 200, 130, 200, 120, 210, fill='lightGrey')

def drawKeyboard():
    # outline and buttons
    Rect(110, 235, 180, 90, fill='lightGrey')
    Rect(116, 218, 155, 15, fill='white', border='lightGrey', borderWidth=1)
    Label('Text Message', 120, 222, fill='darkGrey', size=10, align='left-top')
    Rect(275, 218, 12, 15, fill='dodgerBlue')
    Rect(281, 224, 4, 5, fill='white', align='center-top')
    Polygon(281, 220, 285, 224, 277, 224, fill='white')
    Rect(200, 308, 70, 12, fill='white', align='center-top')
    Rect(262, 285, 21, 20, fill='darkGray')
    Label('del', 272, 295, size=10)
    Rect(116, 285, 19, 20, fill='darkGray')

    # Draws all of the keys using the letters string.
    for index in range(len(app.letters)):
        letter = app.letters[index]

        # If we are in the first row.
        if (index < 10):
            x = 123 + index * 17
            y = 248
        # The second row.
        elif (index < 19):
            x = 130 + (index - 10) * 17
            y = 271
        # The third row.
        else:
            x = 147 + (index - 19) * 17
            y = 295
        Rect(x, y, 14, 20, fill='white', align='center')
        Label(letter, x, y, size=12)

capsLockArrow = Group(
    Polygon(125, 288, 131, 295, 119, 295, fill='white'),
    Rect(125, 295, 5, 7, fill='white', align='center-top')
    )

def capsLock(isCapsLockOn, text1, text2, text3):
    # If caps lock is on, all the texts should be uppercase. Otherwise they
    # should be lowercase.
    if (isCapsLockOn == True):
        app.letters = app.letters.upper()
        Label(text1.upper(), 125, 125, size=10, align='left-top')
        Label(text2.upper(), 185, 155, fill='white', size=10, align='left-top')
        Label(text3.upper(), 125, 185, size=10, align='left-top')
        # Changes the color of the capsLockArrow.
        capsLockArrow.fill = 'black'
    else:
        Label(text1.lower(), 125, 125, size=10, align='left-top')
        Label(text2.lower(), 185, 155, fill='white', size=10, align='left-top')
        Label(text3.lower(), 125, 185, size=10, align='left-top')
    # Draws the keyboard, and brings the capsLockArrow to front.
    drawKeyboard()
    capsLockArrow.toFront()


