app.background = gradient('black', 'slateGrey', start='top')

# Sets a number of steps for how long a flash lasts.
app.stepsOfFlash = 6

# Sets how many steps until you see another set of lighning bolts.
app.stepsBetweenFlash = 15

lightning = Group()

clouds = Group(
    Circle(42, 50, 70, fill='grey', border='dimGrey'),
    Circle(162, 50, 120, fill='grey', border='dimGrey'),
    Circle(342, 50, 90, fill='grey', border='dimGrey'),
    Rect(0, 0, 400, 85, fill='grey')
    )

def makeLightningBolt(startX, startY):
    x1 = startX
    y1 = startY

    # Each lightning bolt is formed by 25 pieces: 25 lines that create a random
    # downward zigzag effect.
    for boltPiece in range(25):
        # Define a variable to give each bolt piece a random lineWidth between
        # 1 and 2 (inclusive).
        randomWidth = randrange(1, 3)
        # Define a variable x2 that is within 15 pixels of the x1.
        x2 = x1 + randrange(-15, 16)
        # Draw the lightning bolt segment to go down by a random distance
        # between 5 and 20 (inclusive).
        if (boltPiece == 24):
            y2 = 400
        else:
            y2 = y1 + randrange(5, 21)
        # Add a new line to the lightning Group.
        lightning.add(
            Line(x1, y1, x2, y2, fill='aliceBlue', lineWidth=randomWidth)
            )
        # The next bolt piece should start where this one ends.
        x1 = x2
        y1 = y2
def onStep():
    app.stepsBetweenFlash -= 1

    if (app.stepsBetweenFlash == 0):
        # Each lightning strike is made up of 4 individual lightning bolts.
        # Initializes where the bolts start here so each bolt has the same
        # starting position and stays close to the other bolts.
        startX = randrange(50, 350)
        startY = 100
        for bolt in range(4):
            makeLightningBolt(startX, startY)

        # Changes the clouds fill, and the background.
        clouds.fill = 'gainsboro'
        app.background = gradient('dimGrey', rgb(170, 180, 200), start='top')

        # Resets flash steps to 15, and steps of the flash to 6.
        app.stepsBetweenFlash = 15
        app.stepsOfFlash = 6

    # Decreases the number of steps the flash has been on for until it gets to 0.
    if (app.stepsOfFlash > 0):
        app.stepsOfFlash -= 1

    # When the strike has been on the canvas long enough, removes the lightning,
    # and changes the fills back to their original values.
    if (app.stepsOfFlash == 0):
        lightning.clear()
        clouds.fill = 'grey'
        app.background = gradient('black', 'slateGrey', start='top')



# -
app.background = gradient('black', 'slateGrey', start='top')

# Sets a number of steps for how long a flash lasts.
app.stepsOfFlash = 6

# Sets how many steps until you see another set of lighning bolts.
app.stepsBetweenFlash = 15

lightning = Group()

clouds = Group(
    Circle(42, 50, 70, fill='grey', border='dimGrey'),
    Circle(162, 50, 120, fill='grey', border='dimGrey'),
    Circle(342, 50, 90, fill='grey', border='dimGrey'),
    Rect(0, 0, 400, 85, fill='grey')
    )

def makeLightningBolt(startX, startY):
    x1 = startX
    y1 = startY

    # Each lightning bolt is formed by 25 pieces: 25 lines that create a random
    # downward zigzag effect.
    for boltPiece in range(25):
        # Define a variable to give each bolt piece a random lineWidth between
        # 1 and 2 (inclusive).
        randomWidth = randrange(1, 3)
        # Define a variable x2 that is within 15 pixels of the x1.
        x2 = x1 + randrange(-15, 16)
        # Draw the lightning bolt segment to go down by a random distance
        # between 5 and 20 (inclusive).
        if (boltPiece == 24):
            y2 = 400
        else:
            y2 = y1 + randrange(5, 21)
        # Add a new line to the lightning Group.
        lightning.add(
            Line(x1, y1, x2, y2, fill='aliceBlue', lineWidth=randomWidth)
            )
        # The next bolt piece should start where this one ends.
        x1 = x2
        y1 = y2
def onStep():
    app.stepsBetweenFlash -= 1

    if (app.stepsBetweenFlash == 0):
        # Each lightning strike is made up of 4 individual lightning bolts.
        # Initializes where the bolts start here so each bolt has the same
        # starting position and stays close to the other bolts.
        startX = randrange(50, 350)
        startY = 100
        for bolt in range(4):
            makeLightningBolt(startX, startY)

        # Changes the clouds fill, and the background.
        clouds.fill = 'gainsboro'
        app.background = gradient('dimGrey', rgb(170, 180, 200), start='top')

        # Resets flash steps to 15, and steps of the flash to 6.
        app.stepsBetweenFlash = 15
        app.stepsOfFlash = 6

    # Decreases the number of steps the flash has been on for until it gets to 0.
    if (app.stepsOfFlash > 0):
        app.stepsOfFlash -= 1

    # When the strike has been on the canvas long enough, removes the lightning,
    # and changes the fills back to their original values.
    if (app.stepsOfFlash == 0):
        lightning.clear()
        clouds.fill = 'grey'
        app.background = gradient('black', 'slateGrey', start='top')

onSteps(15)
app.paused = True


# -
app.background = gradient('black', 'slateGrey', start='top')

# Sets a number of steps for how long a flash lasts.
app.stepsOfFlash = 6

# Sets how many steps until you see another set of lighning bolts.
app.stepsBetweenFlash = 15

lightning = Group()

clouds = Group(
    Circle(42, 50, 70, fill='grey', border='dimGrey'),
    Circle(162, 50, 120, fill='grey', border='dimGrey'),
    Circle(342, 50, 90, fill='grey', border='dimGrey'),
    Rect(0, 0, 400, 85, fill='grey')
    )

def makeLightningBolt(startX, startY):
    x1 = startX
    y1 = startY

    # Each lightning bolt is formed by 25 pieces: 25 lines that create a random
    # downward zigzag effect.
    for boltPiece in range(25):
        # Define a variable to give each bolt piece a random lineWidth between
        # 1 and 2 (inclusive).
        randomWidth = randrange(1, 3)
        # Define a variable x2 that is within 15 pixels of the x1.
        x2 = x1 + randrange(-15, 16)
        # Draw the lightning bolt segment to go down by a random distance
        # between 5 and 20 (inclusive).
        if (boltPiece == 24):
            y2 = 400
        else:
            y2 = y1 + randrange(5, 21)
        # Add a new line to the lightning Group.
        lightning.add(
            Line(x1, y1, x2, y2, fill='aliceBlue', lineWidth=randomWidth)
            )
        # The next bolt piece should start where this one ends.
        x1 = x2
        y1 = y2
def onStep():
    app.stepsBetweenFlash -= 1

    if (app.stepsBetweenFlash == 0):
        # Each lightning strike is made up of 4 individual lightning bolts.
        # Initializes where the bolts start here so each bolt has the same
        # starting position and stays close to the other bolts.
        startX = randrange(50, 350)
        startY = 100
        for bolt in range(4):
            makeLightningBolt(startX, startY)

        # Changes the clouds fill, and the background.
        clouds.fill = 'gainsboro'
        app.background = gradient('dimGrey', rgb(170, 180, 200), start='top')

        # Resets flash steps to 15, and steps of the flash to 6.
        app.stepsBetweenFlash = 15
        app.stepsOfFlash = 6

    # Decreases the number of steps the flash has been on for until it gets to 0.
    if (app.stepsOfFlash > 0):
        app.stepsOfFlash -= 1

    # When the strike has been on the canvas long enough, removes the lightning,
    # and changes the fills back to their original values.
    if (app.stepsOfFlash == 0):
        lightning.clear()
        clouds.fill = 'grey'
        app.background = gradient('black', 'slateGrey', start='top')

onSteps(30)
app.paused = True

