app.background = 'midnightBlue'

Line(0, 200, 400, 200, fill='lightCyan', lineWidth=400, dashes=(2, 38))
Line(200, 0, 200, 400, fill='lightCyan', lineWidth=400, dashes=(2, 38))

labels = Group()

def drawLabels(letter, number):
    # Pick a random index for the letter.
    letterXIndex = randrange(0, 10)
    letterYIndex = randrange(0, 10)

    # Draws and adds the labels for each grid position to the labels group.
    for xIndex in range(0, 10):
        for yIndex in range(0, 10):
            centerX = 40 * (xIndex + 1 / 2)
            centerY = 40 * (yIndex + 1 / 2)
            # At the position where the letter should be, draws a letter.
            # Otherwise draws a number.
            if ((xIndex == letterXIndex) and (yIndex == letterYIndex)):
                labels.add(
                    Label(letter, centerX, centerY, fill='white', size=24,
                          bold=True)
                    )
            else:
                labels.add(
                    Label(number, centerX, centerY, fill='white', size=25,
                          bold=True)
                    )

def onKeyPress(key):
    if (key == 'space'):
        # Loop over each label and check if it is a letter.
        # If it is, change its fill and size.
        for label in labels.children:
            if (label.value.isalpha() == True):
                label.fill = 'red'
                label.size = 26

drawLabels('O', '0')
onKeyPress('space')


# -
app.background = 'midnightBlue'

Line(0, 200, 400, 200, fill='lightCyan', lineWidth=400, dashes=(2, 38))
Line(200, 0, 200, 400, fill='lightCyan', lineWidth=400, dashes=(2, 38))

labels = Group()

def drawLabels(letter, number):
    # Pick a random index for the letter.
    letterXIndex = randrange(0, 10)
    letterYIndex = randrange(0, 10)

    # Draws and adds the labels for each grid position to the labels group.
    for xIndex in range(0, 10):
        for yIndex in range(0, 10):
            centerX = 40 * (xIndex + 1 / 2)
            centerY = 40 * (yIndex + 1 / 2)
            # At the position where the letter should be, draws a letter.
            # Otherwise draws a number.
            if ((xIndex == letterXIndex) and (yIndex == letterYIndex)):
                labels.add(
                    Label(letter, centerX, centerY, fill='white', size=24,
                          bold=True)
                    )
            else:
                labels.add(
                    Label(number, centerX, centerY, fill='white', size=25,
                          bold=True)
                    )

def onKeyPress(key):
    if (key == 'space'):
        # Loop over each label and check if it is a letter.
        # If it is, change its fill and size.
        for label in labels.children:
            if (label.value.isalpha() == True):
                label.fill = 'red'
                label.size = 26

drawLabels('O', '0')
onKeyPress('space')


# -
app.background = 'midnightBlue'

Line(0, 200, 400, 200, fill='lightCyan', lineWidth=400, dashes=(2, 38))
Line(200, 0, 200, 400, fill='lightCyan', lineWidth=400, dashes=(2, 38))

labels = Group()

def drawLabels(letter, number):
    # Pick a random index for the letter.
    letterXIndex = randrange(0, 10)
    letterYIndex = randrange(0, 10)

    # Draws and adds the labels for each grid position to the labels group.
    for xIndex in range(0, 10):
        for yIndex in range(0, 10):
            centerX = 40 * (xIndex + 1 / 2)
            centerY = 40 * (yIndex + 1 / 2)
            # At the position where the letter should be, draws a letter.
            # Otherwise draws a number.
            if ((xIndex == letterXIndex) and (yIndex == letterYIndex)):
                labels.add(
                    Label(letter, centerX, centerY, fill='white', size=24,
                          bold=True)
                    )
            else:
                labels.add(
                    Label(number, centerX, centerY, fill='white', size=25,
                          bold=True)
                    )

def onKeyPress(key):
    if (key == 'space'):
        # Loop over each label and check if it is a letter.
        # If it is, change its fill and size.
        for label in labels.children:
            if (label.value.isalpha() == True):
                label.fill = 'red'
                label.size = 26

drawLabels('T', '7')

