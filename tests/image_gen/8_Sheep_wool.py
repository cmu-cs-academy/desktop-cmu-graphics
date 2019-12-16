app.background = gradient('lightSkyBlue', 'lightCyan', start='top')
Rect(0, 300, 400, 100, fill=gradient('seaGreen', 'mediumSeaGreen', start='top'))

app.stepsPerSecond = 20
app.nextAngle = 0
app.radius = 145

# sheep body
Rect(120, 315, 40, 50, fill='dimGray')
Rect(240, 315, 40, 50, fill='dimGray')
Star(200, 200, 155, 20, fill='white', roundness=95)

# This stores all of the labels making up the wool texture.
woolTexture = Group()

# sheep head
Circle(200, 200, 60, fill='dimGray')
Oval(140, 175, 70, 25, fill='dimGray', rotateAngle=320)
Oval(260, 175, 70, 25, fill='dimGray', rotateAngle=40)
Circle(170, 195, 4)
Circle(230, 195, 4)
Polygon(195, 200, 205, 200, 200, 205)

def writeLetter(letter):
    app.nextAngle += 5

    # Use the getPointInDir function with app radius and nextAngle to get
    # the nextX and nextY for the label.
    nextX, nextY = getPointInDir(200, 200, app.nextAngle, app.radius)
    # Get the angle between the center of the canvas and nextX, nextY.
    newAngle = angleTo(200, 200, nextX, nextY)
    # Gets a random color and borderWidth.
    randomGray = randrange(200, 256)
    color = rgb(randomGray, randomGray, randomGray)
    newBorderWidth = randrange(0, 50)

    # Draw the label in the correct position and add it to the woolTexture group.
    woolTexture.add(
        Label(letter, nextX, nextY, fill=color, size=20, bold=True,
              rotateAngle=newAngle)
        )
    # Gets the next ring of words.
    if (app.nextAngle == 360):
        app.nextAngle = 0
        app.radius -= 15

    # Stops when we reach the head.
    if (app.radius == 55):
        app.paused = True

def onStep():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Get a random letter to call writeLetter with.
    letter = alphabet[randrange(0, len(alphabet))]
    writeLetter(letter)

onStep()
app.paused = True


# -
app.background = gradient('lightSkyBlue', 'lightCyan', start='top')
Rect(0, 300, 400, 100, fill=gradient('seaGreen', 'mediumSeaGreen', start='top'))

app.stepsPerSecond = 20
app.nextAngle = 0
app.radius = 145

# sheep body
Rect(120, 315, 40, 50, fill='dimGray')
Rect(240, 315, 40, 50, fill='dimGray')
Star(200, 200, 155, 20, fill='white', roundness=95)

# This stores all of the labels making up the wool texture.
woolTexture = Group()

# sheep head
Circle(200, 200, 60, fill='dimGray')
Oval(140, 175, 70, 25, fill='dimGray', rotateAngle=320)
Oval(260, 175, 70, 25, fill='dimGray', rotateAngle=40)
Circle(170, 195, 4)
Circle(230, 195, 4)
Polygon(195, 200, 205, 200, 200, 205)

def writeLetter(letter):
    app.nextAngle += 5

    # Use the getPointInDir function with app radius and nextAngle to get
    # the nextX and nextY for the label.
    nextX, nextY = getPointInDir(200, 200, app.nextAngle, app.radius)
    # Get the angle between the center of the canvas and nextX, nextY.
    newAngle = angleTo(200, 200, nextX, nextY)
    # Gets a random color and borderWidth.
    randomGray = randrange(200, 256)
    color = rgb(randomGray, randomGray, randomGray)
    newBorderWidth = randrange(0, 50)

    # Draw the label in the correct position and add it to the woolTexture group.
    woolTexture.add(
        Label(letter, nextX, nextY, fill=color, size=20, bold=True,
              rotateAngle=newAngle)
        )
    # Gets the next ring of words.
    if (app.nextAngle == 360):
        app.nextAngle = 0
        app.radius -= 15

    # Stops when we reach the head.
    if (app.radius == 55):
        app.paused = True

def onStep():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Get a random letter to call writeLetter with.
    letter = alphabet[randrange(0, len(alphabet))]
    writeLetter(letter)

onSteps(5)
app.paused = True


# -
app.background = gradient('lightSkyBlue', 'lightCyan', start='top')
Rect(0, 300, 400, 100, fill=gradient('seaGreen', 'mediumSeaGreen', start='top'))

app.stepsPerSecond = 20
app.nextAngle = 0
app.radius = 145

# sheep body
Rect(120, 315, 40, 50, fill='dimGray')
Rect(240, 315, 40, 50, fill='dimGray')
Star(200, 200, 155, 20, fill='white', roundness=95)

# This stores all of the labels making up the wool texture.
woolTexture = Group()

# sheep head
Circle(200, 200, 60, fill='dimGray')
Oval(140, 175, 70, 25, fill='dimGray', rotateAngle=320)
Oval(260, 175, 70, 25, fill='dimGray', rotateAngle=40)
Circle(170, 195, 4)
Circle(230, 195, 4)
Polygon(195, 200, 205, 200, 200, 205)

def writeLetter(letter):
    app.nextAngle += 5

    # Use the getPointInDir function with app radius and nextAngle to get
    # the nextX and nextY for the label.
    nextX, nextY = getPointInDir(200, 200, app.nextAngle, app.radius)
    # Get the angle between the center of the canvas and nextX, nextY.
    newAngle = angleTo(200, 200, nextX, nextY)
    # Gets a random color and borderWidth.
    randomGray = randrange(200, 256)
    color = rgb(randomGray, randomGray, randomGray)
    newBorderWidth = randrange(0, 50)

    # Draw the label in the correct position and add it to the woolTexture group.
    woolTexture.add(
        Label(letter, nextX, nextY, fill=color, size=20, bold=True,
              rotateAngle=newAngle)
        )
    # Gets the next ring of words.
    if (app.nextAngle == 360):
        app.nextAngle = 0
        app.radius -= 15

    # Stops when we reach the head.
    if (app.radius == 55):
        app.paused = True

def onStep():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Get a random letter to call writeLetter with.
    letter = alphabet[randrange(0, len(alphabet))]
    writeLetter(letter)


