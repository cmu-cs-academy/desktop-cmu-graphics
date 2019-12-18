app.stepsPerSecond = 1

# background
Rect(0, 0, 400, 400)

def drawLetter(key, x, y, index, size, angle, red, green, blue):
    # Draws one rotated letter.
    green -= 25 * index
    blue -= 10 * index
    angle = angle + 10 * index
    Label(key, x, y, fill=rgb(red, green, blue), size=size, rotateAngle=angle)

def onStep():
    # Clears the canvas.
    app.group.clear()
    Rect(0, 0, 400, 400)

    # Sets variables.
    letterSize = 400
    index = 0

    letter = choice('abcdefghijklmnopqrstuvwxyz')
    rotateAngle = randrange(0, 360)
    r = randrange(0, 256)
    g = randrange(200, 256)
    b = randrange(200, 256)
    x = randrange(100, 300)
    y = randrange(100, 300)

    # Draw a letter until the letterSize reaches 0. After each letter is
    # drawn, randomly decrease the next letter size and add 1 to the index.
    while (letterSize > 0):
        drawLetter(letter, x, y, index, letterSize, rotateAngle, r, g, b)
        sizeChange = randrange(40, 100)
        letterSize -= sizeChange
        index += 1



# -
app.stepsPerSecond = 1

# background
Rect(0, 0, 400, 400)

def drawLetter(key, x, y, index, size, angle, red, green, blue):
    # Draws one rotated letter.
    green -= 25 * index
    blue -= 10 * index
    angle = angle + 10 * index
    Label(key, x, y, fill=rgb(red, green, blue), size=size, rotateAngle=angle)

def onStep():
    # Clears the canvas.
    app.group.clear()
    Rect(0, 0, 400, 400)

    # Sets variables.
    letterSize = 400
    index = 0

    letter = choice('abcdefghijklmnopqrstuvwxyz')
    rotateAngle = randrange(0, 360)
    r = randrange(0, 256)
    g = randrange(200, 256)
    b = randrange(200, 256)
    x = randrange(100, 300)
    y = randrange(100, 300)

    # Draw a letter until the letterSize reaches 0. After each letter is
    # drawn, randomly decrease the next letter size and add 1 to the index.
    while (letterSize > 0):
        drawLetter(letter, x, y, index, letterSize, rotateAngle, r, g, b)
        sizeChange = randrange(40, 100)
        letterSize -= sizeChange
        index += 1

onSteps(15)
app.paused = True


# -
app.stepsPerSecond = 1

# background
Rect(0, 0, 400, 400)

def drawLetter(key, x, y, index, size, angle, red, green, blue):
    # Draws one rotated letter.
    green -= 25 * index
    blue -= 10 * index
    angle = angle + 10 * index
    Label(key, x, y, fill=rgb(red, green, blue), size=size, rotateAngle=angle)

def onStep():
    # Clears the canvas.
    app.group.clear()
    Rect(0, 0, 400, 400)

    # Sets variables.
    letterSize = 400
    index = 0

    letter = choice('abcdefghijklmnopqrstuvwxyz')
    rotateAngle = randrange(0, 360)
    r = randrange(0, 256)
    g = randrange(200, 256)
    b = randrange(200, 256)
    x = randrange(100, 300)
    y = randrange(100, 300)

    # Draw a letter until the letterSize reaches 0. After each letter is
    # drawn, randomly decrease the next letter size and add 1 to the index.
    while (letterSize > 0):
        drawLetter(letter, x, y, index, letterSize, rotateAngle, r, g, b)
        sizeChange = randrange(40, 100)
        letterSize -= sizeChange
        index += 1

onSteps(15)
app.paused = True

