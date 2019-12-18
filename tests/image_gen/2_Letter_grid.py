app.background = 'black'

app.alphabet = 'abcdefghijklmnopqrstuvwxyz'
app.gridSize = 10

letters = Group()

def drawLetters(gridSize, letter):
    letters.clear()

    # Finds the amount of space between each letter and the starting
    # coordinate of the letters.
    spacing = 400 // (gridSize + 1)
    start = spacing // gridSize

    # Loops over each position in the grid.
    for x in range(start, 400, spacing):
        for y in range(start, 400, spacing):
            letterSize = randrange(20, 50)
            letterColor = rgb(randrange(150, 240), randrange(150, 240),
                              randrange(150, 240))

            # Add each letter to the letters group.
            letters.add(
                Label(letter, x, y, fill=letterColor, size=letterSize)
                )
drawLetters(app.gridSize, 'i')

def onMousePress(mouseX, mouseY):
    # Update the letter by getting a random index between 0 and the length
    # of the alphabet. Then use that index to get the corresponding letter
    # of the alphabet and call drawLetters with the new letter and a
    # gridSize of index + 1.
    index = randrange(0, len(app.alphabet))
    newLetter = app.alphabet[index]
    drawLetters(index + 1, newLetter)
def onStep():
    # Rotates each letter.
    for letter in letters:
        letter.rotateAngle += 5

onSteps(20)
app.paused = True


# -
app.background = 'black'

app.alphabet = 'abcdefghijklmnopqrstuvwxyz'
app.gridSize = 10

letters = Group()

def drawLetters(gridSize, letter):
    letters.clear()

    # Finds the amount of space between each letter and the starting
    # coordinate of the letters.
    spacing = 400 // (gridSize + 1)
    start = spacing // gridSize

    # Loops over each position in the grid.
    for x in range(start, 400, spacing):
        for y in range(start, 400, spacing):
            letterSize = randrange(20, 50)
            letterColor = rgb(randrange(150, 240), randrange(150, 240),
                              randrange(150, 240))

            # Add each letter to the letters group.
            letters.add(
                Label(letter, x, y, fill=letterColor, size=letterSize)
                )
drawLetters(app.gridSize, 'i')

def onMousePress(mouseX, mouseY):
    # Update the letter by getting a random index between 0 and the length
    # of the alphabet. Then use that index to get the corresponding letter
    # of the alphabet and call drawLetters with the new letter and a
    # gridSize of index + 1.
    index = randrange(0, len(app.alphabet))
    newLetter = app.alphabet[index]
    drawLetters(index + 1, newLetter)
def onStep():
    # Rotates each letter.
    for letter in letters:
        letter.rotateAngle += 5



# -
app.background = 'black'

app.alphabet = 'abcdefghijklmnopqrstuvwxyz'
app.gridSize = 10

letters = Group()

def drawLetters(gridSize, letter):
    letters.clear()

    # Finds the amount of space between each letter and the starting
    # coordinate of the letters.
    spacing = 400 // (gridSize + 1)
    start = spacing // gridSize

    # Loops over each position in the grid.
    for x in range(start, 400, spacing):
        for y in range(start, 400, spacing):
            letterSize = randrange(20, 50)
            letterColor = rgb(randrange(150, 240), randrange(150, 240),
                              randrange(150, 240))

            # Add each letter to the letters group.
            letters.add(
                Label(letter, x, y, fill=letterColor, size=letterSize)
                )
drawLetters(app.gridSize, 'i')

def onMousePress(mouseX, mouseY):
    # Update the letter by getting a random index between 0 and the length
    # of the alphabet. Then use that index to get the corresponding letter
    # of the alphabet and call drawLetters with the new letter and a
    # gridSize of index + 1.
    index = randrange(0, len(app.alphabet))
    newLetter = app.alphabet[index]
    drawLetters(index + 1, newLetter)
def onStep():
    # Rotates each letter.
    for letter in letters:
        letter.rotateAngle += 5


