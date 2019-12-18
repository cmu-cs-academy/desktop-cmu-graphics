app.background = rgb(0, 0, 80)

# screen
Rect(0, 25, 400, 350)

# curtains
Oval(0, 0, 100, 600, fill=rgb(50, 10, 0), rotateAngle=5)
Oval(400, 0, 100, 600, fill=rgb(50, 10, 0), rotateAngle=-5)

# chairs
Oval(200, 500, 350, 350, fill=rgb(130, 20, 10))
Oval(-100, 500, 350, 350, fill=rgb(130, 20, 10))
Oval(500, 500, 350, 350, fill=rgb(130, 20, 10))

popcorn = Group()

def drawCup():
    # Draws the cup in front of everything else.
    Polygon(100, 400, 70, 250, 330, 250, 300, 400, fill='red')
    for centerX in range(110, 261, 50):
        Rect(centerX, 250, 30, 150, fill='white')

def drawPopcorn(centerX, centerY):
    color1 = gradient('gold', 'khaki')
    color2 = 'paleGoldenrod'
    popcornPiece = Group(
        Circle(centerX, centerY, 25, fill=color1, border=color2),
        Circle(centerX + 15, centerY - 25, 15, fill=color1, border=color2),
        Circle(centerX + 20, centerY - 10, 15, fill=color1, border=color2),
        Circle(centerX - 15, centerY - 25, 15, fill=color1, border=color2),
        Circle(centerX - 20, centerY - 10, 15, fill=color1, border=color2),
        Circle(centerX, centerY-5, 15, fill=color1),
        )
    popcorn.add(popcornPiece)

    # Create a custom property isMovingUp for each piece.
    popcornPiece.isMovingUp = True
def makePopcorn():
    # Creates the lists we need.
    xList = [ 100, 140, 170, 200, 240, 280, 300 ]
    yList = [ 170, 200, 240 ]

    # Loop through each list and draw a piece of popcorn using that
    # centerX and centerY.
    for centerX in xList:
        for centerY in yList:
            drawPopcorn(centerX, centerY)
makePopcorn()
drawCup()

def onStep():
    # As long as we have some popcorn, gets a random piece of popcorn.
    if (len(popcorn.children) > 0):
        popcornPiece = popcorn.children[randrange(0, len(popcorn.children))]

        # Moves the popcorn either up or down and change direction for next step.
        if (popcornPiece.isMovingUp == True):
            popcornPiece.centerY -= 10
            popcornPiece.isMovingUp = False
        else:
            popcornPiece.centerY += 10
            popcornPiece.isMovingUp = True

onStep()
app.paused = True


# -
app.background = rgb(0, 0, 80)

# screen
Rect(0, 25, 400, 350)

# curtains
Oval(0, 0, 100, 600, fill=rgb(50, 10, 0), rotateAngle=5)
Oval(400, 0, 100, 600, fill=rgb(50, 10, 0), rotateAngle=-5)

# chairs
Oval(200, 500, 350, 350, fill=rgb(130, 20, 10))
Oval(-100, 500, 350, 350, fill=rgb(130, 20, 10))
Oval(500, 500, 350, 350, fill=rgb(130, 20, 10))

popcorn = Group()

def drawCup():
    # Draws the cup in front of everything else.
    Polygon(100, 400, 70, 250, 330, 250, 300, 400, fill='red')
    for centerX in range(110, 261, 50):
        Rect(centerX, 250, 30, 150, fill='white')

def drawPopcorn(centerX, centerY):
    color1 = gradient('gold', 'khaki')
    color2 = 'paleGoldenrod'
    popcornPiece = Group(
        Circle(centerX, centerY, 25, fill=color1, border=color2),
        Circle(centerX + 15, centerY - 25, 15, fill=color1, border=color2),
        Circle(centerX + 20, centerY - 10, 15, fill=color1, border=color2),
        Circle(centerX - 15, centerY - 25, 15, fill=color1, border=color2),
        Circle(centerX - 20, centerY - 10, 15, fill=color1, border=color2),
        Circle(centerX, centerY-5, 15, fill=color1),
        )
    popcorn.add(popcornPiece)

    # Create a custom property isMovingUp for each piece.
    popcornPiece.isMovingUp = True
def makePopcorn():
    # Creates the lists we need.
    xList = [ 100, 140, 170, 200, 240, 280, 300 ]
    yList = [ 170, 200, 240 ]

    # Loop through each list and draw a piece of popcorn using that
    # centerX and centerY.
    for centerX in xList:
        for centerY in yList:
            drawPopcorn(centerX, centerY)
makePopcorn()
drawCup()

def onStep():
    # As long as we have some popcorn, gets a random piece of popcorn.
    if (len(popcorn.children) > 0):
        popcornPiece = popcorn.children[randrange(0, len(popcorn.children))]

        # Moves the popcorn either up or down and change direction for next step.
        if (popcornPiece.isMovingUp == True):
            popcornPiece.centerY -= 10
            popcornPiece.isMovingUp = False
        else:
            popcornPiece.centerY += 10
            popcornPiece.isMovingUp = True

onSteps(50)
app.paused = True


# -
app.background = rgb(0, 0, 80)

# screen
Rect(0, 25, 400, 350)

# curtains
Oval(0, 0, 100, 600, fill=rgb(50, 10, 0), rotateAngle=5)
Oval(400, 0, 100, 600, fill=rgb(50, 10, 0), rotateAngle=-5)

# chairs
Oval(200, 500, 350, 350, fill=rgb(130, 20, 10))
Oval(-100, 500, 350, 350, fill=rgb(130, 20, 10))
Oval(500, 500, 350, 350, fill=rgb(130, 20, 10))

popcorn = Group()

def drawCup():
    # Draws the cup in front of everything else.
    Polygon(100, 400, 70, 250, 330, 250, 300, 400, fill='red')
    for centerX in range(110, 261, 50):
        Rect(centerX, 250, 30, 150, fill='white')

def drawPopcorn(centerX, centerY):
    color1 = gradient('gold', 'khaki')
    color2 = 'paleGoldenrod'
    popcornPiece = Group(
        Circle(centerX, centerY, 25, fill=color1, border=color2),
        Circle(centerX + 15, centerY - 25, 15, fill=color1, border=color2),
        Circle(centerX + 20, centerY - 10, 15, fill=color1, border=color2),
        Circle(centerX - 15, centerY - 25, 15, fill=color1, border=color2),
        Circle(centerX - 20, centerY - 10, 15, fill=color1, border=color2),
        Circle(centerX, centerY-5, 15, fill=color1),
        )
    popcorn.add(popcornPiece)

    # Create a custom property isMovingUp for each piece.
    popcornPiece.isMovingUp = True
def makePopcorn():
    # Creates the lists we need.
    xList = [ 100, 140, 170, 200, 240, 280, 300 ]
    yList = [ 170, 200, 240 ]

    # Loop through each list and draw a piece of popcorn using that
    # centerX and centerY.
    for centerX in xList:
        for centerY in yList:
            drawPopcorn(centerX, centerY)
makePopcorn()
drawCup()

def onStep():
    # As long as we have some popcorn, gets a random piece of popcorn.
    if (len(popcorn.children) > 0):
        popcornPiece = popcorn.children[randrange(0, len(popcorn.children))]

        # Moves the popcorn either up or down and change direction for next step.
        if (popcornPiece.isMovingUp == True):
            popcornPiece.centerY -= 10
            popcornPiece.isMovingUp = False
        else:
            popcornPiece.centerY += 10
            popcornPiece.isMovingUp = True

onSteps(10)
app.paused = True

