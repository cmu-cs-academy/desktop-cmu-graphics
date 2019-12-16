app.background = gradient('wheat', 'wheat', 'tan')

app.steps = 0
app.isFaceUp = False

# lake
Circle(200, 200, 200, fill=gradient('blue', 'blue', rgb(30, 145, 255)), opacity=50)
fishes = Group()
Circle(200, 200, 190, fill=gradient('blue', 'blue', rgb(30, 145, 255)), opacity=50)

# island
Circle(200, 200, 80, fill=gradient('brown', 'wheat'))
Star(200, 200, 100, 10, fill=gradient('yellowGreen', 'green'), roundness=25)

catFaceDown = Group()
catBodies = Group()
catFaceUp = Group()

def drawFish(centerX, centerY, color):
    finColor = gradient(color, color, 'silver', 'silver', start='left-top')
    fish = Group(
        Star(centerX - 12, centerY, 10, 3, fill=finColor, roundness=35,
             rotateAngle=-30),
        RegularPolygon(centerX - 1, centerY - 6, 6, 3, fill=finColor,
                       rotateAngle=10),
        Oval(centerX, centerY, 22, 12,
             fill=gradient('silver', 'white', start='top')),
        Circle(centerX + 6, centerY - 2, 1),
        Line(centerX + 3, centerY - 5, centerX + 1, centerY, lineWidth=0.5),
        Line(centerX, centerY, centerX + 2, centerY + 5, lineWidth=0.5),
        Arc(centerX, centerY + 1, 7, 3, 135, 270, fill=finColor)
        )

    # Gets a random direction to move and rotate the fish to swim in that direction.
    fish.dx = randrange(-4, 5)
    fish.dy = randrange(-4, 5)
    fish.rotateAngle = angleTo(fish.centerX, fish.centerY, fish.centerX + fish.dx,
                               fish.centerY + fish.dy) - 90
    fishes.add(fish)

def drawTwoCats(centerY):
    # Draws a cat on the left at the centerY.
    leftFaceDown = Group(
        Circle(66, centerY, 28, fill='grey'),
        Arc(84, centerY + 15, 25, 15, 180, 180,
            fill=gradient('darkGrey', 'grey'), rotateAngle=-135),
        Arc(84, centerY - 15, 25, 15, 180, 180,
            fill=gradient('darkGrey', 'grey'), rotateAngle=135)
        )
    leftCatBody = Oval(10, centerY, 100, 70, fill=gradient('darkGrey', 'grey'))
    leftFaceUp = Group(
        Circle(66, centerY, 28, fill=gradient('dimGrey', 'grey', start='right')),
        Arc(50, centerY + 15, 25, 15, 0, 180,
            fill=gradient('darkGrey', 'darkGrey'), rotateAngle=135),
        Arc(50, centerY - 15, 25, 15, 0, 180,
            fill=gradient('darkGrey', 'darkGrey'), rotateAngle=-135),
        Circle(60, centerY - 10, 3),
        Circle(60, centerY + 10, 3),
        Arc(75, centerY, 15, 12, 45, 90)
        )
    leftFaceUp.visible = False

    # Draws a cat on the right at the centerY.
    rightFaceDown = Group(
        Circle(344, centerY, 28, fill='grey'),
        Arc(328, centerY + 15, 25, 15, 180, 180,
            fill=gradient('darkGrey', 'grey'), rotateAngle=-45),
        Arc(328, centerY - 15, 25, 15, 180, 180,
            fill=gradient('darkGrey', 'grey'), rotateAngle=45),
        )
    rightCatBody = Oval(390, centerY, 100, 70, fill=gradient('darkGrey', 'grey'))
    rightFaceUp = Group(
        Circle(334, centerY, 28, fill=gradient('dimGrey', 'grey', start='left')),
        Arc(350, centerY + 15, 25, 15, 0, 180,
            fill=gradient('darkGrey', 'darkGrey'), rotateAngle=45),
        Arc(350, centerY - 15, 25, 15, 0, 180,
            fill=gradient('darkGrey', 'darkGrey'), rotateAngle=-45),
        Circle(340, centerY - 10, 3),
        Circle(340, centerY + 10, 3),
        Arc(325, centerY, 15, 12, 225, 90)
        )
    rightFaceUp.visible = False

    catFaceDown.add(rightFaceDown)
    catFaceDown.add(leftFaceDown)
    catBodies.add(rightCatBody)
    catBodies.add(leftCatBody)
    catFaceUp.add(rightFaceUp)
    catFaceUp.add(leftFaceUp)

def createCats():
    # Draws 4 rows of two cats.
    for centerY in range(80, 380, 80):
        drawTwoCats(centerY)

def createFish():
    # Creates a grid of fish.
    for i in range(110, 300, 60):
        for j in range(105, 300, 25):
            chance = randrange(0, 3)
            if (chance == 0):
                color = 'red'
            elif (chance == 1):
                color = 'green'
            else:
                color = 'blue'

            drawFish(i, j, color)

def moveFishes():
    # Moves the fish around the lake.
    for fish in fishes:
        fish.centerX += fish.dx
        fish.centerY += fish.dy
        # When the fish are near the edge of the lake, places them at a new
        # random point around the edge of the lake.
        if (distance(200, 200, fish.centerX, fish.centerY) > 175):
            x, y = getPointInDir(200, 200, randrange(0, 360), 165)
            fish.centerX = x
            fish.centerY = y
            fish.opacity = 100

        # If the fish is close to the edge of the lake, halve its opacity.
        elif (distance(200, 200, fish.centerX, fish.centerY) > 165):
            fish.opacity //= 2

def moveCatHeads():
    # Shows the correct-facing head.
    if (app.isFaceUp == True):
        catFaceUp.visible = True
        catFaceDown.visible = False
    else:
        catFaceUp.visible = False
        catFaceDown.visible = True

def onStep():
    moveFishes()
    moveCatHeads()

    # Keeps track of when the head should be up or down.
    if (app.steps == 55):
        app.isFaceUp = True
    elif (app.steps >= 80):
        app.isFaceUp = False
        app.steps = 0

    app.steps += 1

createFish()
createCats()


