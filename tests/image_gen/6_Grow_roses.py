app.background='skyBlue'

app.lightColor = 'lightCoral'
app.darkColor = 'indianRed'

roseBush = Group(
    Oval(220, 130, 150, 120, fill='seaGreen'),
    Oval(130, 180, 210, 150, fill='seaGreen'),
    Oval(20, 240, 180, 150, fill='seaGreen'),
    Oval(320, 180, 210, 170, fill='seaGreen'),
    Rect(0, 200, 400, 200, fill='seaGreen')
    )

def getRoseColors():
    # Picks a random color for the rose to be.
    randNum = randrange(0, 3)
    if (randNum == 0):
        app.lightColor = 'lightCoral'
        app.darkColor = 'indianRed'
    elif (randNum == 1):
        app.lightColor = 'mistyRose'
        app.darkColor = 'pink'
    else:
        app.lightColor = 'gold'
        app.darkColor = 'orange'

def drawPetalRing(numberOfPetals, x, y):
    width = 1.5 * numberOfPetals
    height = 3 * numberOfPetals

    # Create a ring of petals.
    for i in range(numberOfPetals):
        angle = 30 * i

        # Alternate whether the color of the petal is light or dark.
        if (i % 2 == 0):
            color = app.lightColor
        else:
            color = app.darkColor
        # Draw a petal.
        Rect(x, y, width, height, fill=color, rotateAngle=angle,
             align='center')
def onMousePress(mouseX, mouseY):
    numberOfPetalsInRing = [ 19, 17, 13, 11, 7, 5, 1 ]

    # If you click on the roseBush, draw a rose.
    if (roseBush.hits(mouseX, mouseY) == True):
        randNum = randrange(0, 3)
        getRoseColors()

        # To draw a rose, draw one petal ring for each number in the
        # numberOfPetalsInRing list.
        for num in numberOfPetalsInRing:
            drawPetalRing(num, mouseX, mouseY)

onMousePress(150, 100)
onMousePress(200, 200)


# -
app.background='skyBlue'

app.lightColor = 'lightCoral'
app.darkColor = 'indianRed'

roseBush = Group(
    Oval(220, 130, 150, 120, fill='seaGreen'),
    Oval(130, 180, 210, 150, fill='seaGreen'),
    Oval(20, 240, 180, 150, fill='seaGreen'),
    Oval(320, 180, 210, 170, fill='seaGreen'),
    Rect(0, 200, 400, 200, fill='seaGreen')
    )

def getRoseColors():
    # Picks a random color for the rose to be.
    randNum = randrange(0, 3)
    if (randNum == 0):
        app.lightColor = 'lightCoral'
        app.darkColor = 'indianRed'
    elif (randNum == 1):
        app.lightColor = 'mistyRose'
        app.darkColor = 'pink'
    else:
        app.lightColor = 'gold'
        app.darkColor = 'orange'

def drawPetalRing(numberOfPetals, x, y):
    width = 1.5 * numberOfPetals
    height = 3 * numberOfPetals

    # Create a ring of petals.
    for i in range(numberOfPetals):
        angle = 30 * i

        # Alternate whether the color of the petal is light or dark.
        if (i % 2 == 0):
            color = app.lightColor
        else:
            color = app.darkColor
        # Draw a petal.
        Rect(x, y, width, height, fill=color, rotateAngle=angle,
             align='center')
def onMousePress(mouseX, mouseY):
    numberOfPetalsInRing = [ 19, 17, 13, 11, 7, 5, 1 ]

    # If you click on the roseBush, draw a rose.
    if (roseBush.hits(mouseX, mouseY) == True):
        randNum = randrange(0, 3)
        getRoseColors()

        # To draw a rose, draw one petal ring for each number in the
        # numberOfPetalsInRing list.
        for num in numberOfPetalsInRing:
            drawPetalRing(num, mouseX, mouseY)

onMousePress(60, 230)
onMousePress(320, 130)


# -
app.background='skyBlue'

app.lightColor = 'lightCoral'
app.darkColor = 'indianRed'

roseBush = Group(
    Oval(220, 130, 150, 120, fill='seaGreen'),
    Oval(130, 180, 210, 150, fill='seaGreen'),
    Oval(20, 240, 180, 150, fill='seaGreen'),
    Oval(320, 180, 210, 170, fill='seaGreen'),
    Rect(0, 200, 400, 200, fill='seaGreen')
    )

def getRoseColors():
    # Picks a random color for the rose to be.
    randNum = randrange(0, 3)
    if (randNum == 0):
        app.lightColor = 'lightCoral'
        app.darkColor = 'indianRed'
    elif (randNum == 1):
        app.lightColor = 'mistyRose'
        app.darkColor = 'pink'
    else:
        app.lightColor = 'gold'
        app.darkColor = 'orange'

def drawPetalRing(numberOfPetals, x, y):
    width = 1.5 * numberOfPetals
    height = 3 * numberOfPetals

    # Create a ring of petals.
    for i in range(numberOfPetals):
        angle = 30 * i

        # Alternate whether the color of the petal is light or dark.
        if (i % 2 == 0):
            color = app.lightColor
        else:
            color = app.darkColor
        # Draw a petal.
        Rect(x, y, width, height, fill=color, rotateAngle=angle,
             align='center')
def onMousePress(mouseX, mouseY):
    numberOfPetalsInRing = [ 19, 17, 13, 11, 7, 5, 1 ]

    # If you click on the roseBush, draw a rose.
    if (roseBush.hits(mouseX, mouseY) == True):
        randNum = randrange(0, 3)
        getRoseColors()

        # To draw a rose, draw one petal ring for each number in the
        # numberOfPetalsInRing list.
        for num in numberOfPetalsInRing:
            drawPetalRing(num, mouseX, mouseY)

onMousePress(200, 200)

