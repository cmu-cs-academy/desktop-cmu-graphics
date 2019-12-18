app.background = 'black'
app.steps = 0
app.word = 'meteor'

# background
for i in range (30):
    Star(randrange(0, 400), randrange(0, 400), 5, 4, fill='white', opacity=80)

meteors = Group()
spaceships = Group()

Label('Score: ', 325, 25, fill='white', size=20, bold=True)
score = Label(0, 375, 25, fill='white', size=20, bold=True)

def drawMeteor(meteorSize):
    # Draws a new meteor.
    meteor = Group(
        Polygon(0, 340, 0, 365, 20, 400, 40, 365, 40, 340,
                fill=gradient('orange', 'orangeRed', 'black', start='top')),
        Circle(20, 340, 20,
              fill=gradient('white', 'gray', 'dimGray', start='top')),
        Oval(30, 345, 5, 8, fill='dimGray', rotateAngle=20),
        Oval(30, 345, 7, 8,
             fill=gradient('silver', 'gray', start='top'), rotateAngle=20),
        Oval(12, 330, 3, 5,
             fill=gradient('silver', 'gray', start='top'), rotateAngle=20)
        )

    # Sets properties to position, angle, and size the meteor properly.
    meteor.rotateAngle = 180
    meteor.centerX = randrange(0, 400)
    meteor.bottom = 0
    meteor.width = meteorSize
    meteor.height = 2 * meteorSize

    # Randomly decides if the meteor has uppercase or lowercase letters.
    isCaps = randrange(0, 2)

    # Set the new meteor's word depending on if the word should be capital or not.
    if (isCaps == 0):
        meteor.word = app.word.upper()
    else:
        meteor.word = app.word.lower()
    # Adds the letter to the meteor.
    meteor.add(
        Label(meteor.word, meteor.centerX, -15, size=meteorSize/5, bold=True)
        )
    meteors.add(meteor)

def onMousePress(mouseX, mouseY):
    # Draws a new spaceship.
    spaceship = Group(
        Polygon(15, 400, 4, 370, 26, 370,
                fill=gradient('orange', 'darkOrange', 'red', start='right-top')),
        Oval(15, 337, 32, 65, fill='white'),
        RegularPolygon(15, 307, 14, 3, fill='crimson'),
        Circle(15, 332, 10, fill='lightSkyBlue', border='dimGray', borderWidth=3),
        Rect(2, 358, 28, 12, fill='crimson')
        )

    # Sets the target for the spaceship and rotates it to be angled towards that
    # target.
    spaceship.targetX = mouseX
    spaceship.targetY = mouseY
    spaceship.rotateAngle = angleTo(spaceship.centerX, spaceship.centerY,
                                    mouseX, mouseY)
    spaceships.add(spaceship)

def onStep():
    app.steps += 1

    # When the player has 300 points, they win.
    if (score.value >= 300):
        Rect(0, 150, 400, 100, fill='white', opacity=60)
        Label('YOU WIN', 200, 200, size=42, bold=True)
        app.stop()

    # Makes a new star every 20 steps.
    if (app.steps >= 20):
        drawMeteor(randrange(40, 80))
        app.steps = 0

    # Moves each spaceship towards its target position.
    for spaceship in spaceships.children:
        newAngle = angleTo(spaceship.centerX, spaceship.centerY,
                           spaceship.targetX, spaceship.targetY)
        newX, newY = getPointInDir(spaceship.centerX, spaceship.centerY,
                                   newAngle, 5)
        spaceship.centerX = newX
        spaceship.centerY = newY

        # Checks if the spaceship reaches its target and remove it if it has.
        if ((abs(spaceship.centerX - spaceship.targetX) < 5) and
            (abs(spaceship.centerY - spaceship.targetY) < 5)):
            spaceships.remove(spaceship)

    # Moves each of the meteors.
    for meteor in meteors.children:
        meteor.centerY += 4

        # If a spaceship hits the meteor, increment or decrement the score
        # depending on if the meteor's letter is lower or upper case.
        if (spaceships.hitsShape(meteor) == True):
            meteors.remove(meteor)
            if (meteor.word.isupper() == True):
                score.value += meteor.width // 2
            elif (score.value >= meteor.width // 2):
                score.value -= meteor.width // 2
        # Remove any meteor that are off the screen.
        if (meteor.top > 400):
            meteors.remove(meteor)

onSteps(25)
app.paused = True


# -
app.background = 'black'
app.steps = 0
app.word = 'meteor'

# background
for i in range (30):
    Star(randrange(0, 400), randrange(0, 400), 5, 4, fill='white', opacity=80)

meteors = Group()
spaceships = Group()

Label('Score: ', 325, 25, fill='white', size=20, bold=True)
score = Label(0, 375, 25, fill='white', size=20, bold=True)

def drawMeteor(meteorSize):
    # Draws a new meteor.
    meteor = Group(
        Polygon(0, 340, 0, 365, 20, 400, 40, 365, 40, 340,
                fill=gradient('orange', 'orangeRed', 'black', start='top')),
        Circle(20, 340, 20,
              fill=gradient('white', 'gray', 'dimGray', start='top')),
        Oval(30, 345, 5, 8, fill='dimGray', rotateAngle=20),
        Oval(30, 345, 7, 8,
             fill=gradient('silver', 'gray', start='top'), rotateAngle=20),
        Oval(12, 330, 3, 5,
             fill=gradient('silver', 'gray', start='top'), rotateAngle=20)
        )

    # Sets properties to position, angle, and size the meteor properly.
    meteor.rotateAngle = 180
    meteor.centerX = randrange(0, 400)
    meteor.bottom = 0
    meteor.width = meteorSize
    meteor.height = 2 * meteorSize

    # Randomly decides if the meteor has uppercase or lowercase letters.
    isCaps = randrange(0, 2)

    # Set the new meteor's word depending on if the word should be capital or not.
    if (isCaps == 0):
        meteor.word = app.word.upper()
    else:
        meteor.word = app.word.lower()
    # Adds the letter to the meteor.
    meteor.add(
        Label(meteor.word, meteor.centerX, -15, size=meteorSize/5, bold=True)
        )
    meteors.add(meteor)

def onMousePress(mouseX, mouseY):
    # Draws a new spaceship.
    spaceship = Group(
        Polygon(15, 400, 4, 370, 26, 370,
                fill=gradient('orange', 'darkOrange', 'red', start='right-top')),
        Oval(15, 337, 32, 65, fill='white'),
        RegularPolygon(15, 307, 14, 3, fill='crimson'),
        Circle(15, 332, 10, fill='lightSkyBlue', border='dimGray', borderWidth=3),
        Rect(2, 358, 28, 12, fill='crimson')
        )

    # Sets the target for the spaceship and rotates it to be angled towards that
    # target.
    spaceship.targetX = mouseX
    spaceship.targetY = mouseY
    spaceship.rotateAngle = angleTo(spaceship.centerX, spaceship.centerY,
                                    mouseX, mouseY)
    spaceships.add(spaceship)

def onStep():
    app.steps += 1

    # When the player has 300 points, they win.
    if (score.value >= 300):
        Rect(0, 150, 400, 100, fill='white', opacity=60)
        Label('YOU WIN', 200, 200, size=42, bold=True)
        app.stop()

    # Makes a new star every 20 steps.
    if (app.steps >= 20):
        drawMeteor(randrange(40, 80))
        app.steps = 0

    # Moves each spaceship towards its target position.
    for spaceship in spaceships.children:
        newAngle = angleTo(spaceship.centerX, spaceship.centerY,
                           spaceship.targetX, spaceship.targetY)
        newX, newY = getPointInDir(spaceship.centerX, spaceship.centerY,
                                   newAngle, 5)
        spaceship.centerX = newX
        spaceship.centerY = newY

        # Checks if the spaceship reaches its target and remove it if it has.
        if ((abs(spaceship.centerX - spaceship.targetX) < 5) and
            (abs(spaceship.centerY - spaceship.targetY) < 5)):
            spaceships.remove(spaceship)

    # Moves each of the meteors.
    for meteor in meteors.children:
        meteor.centerY += 4

        # If a spaceship hits the meteor, increment or decrement the score
        # depending on if the meteor's letter is lower or upper case.
        if (spaceships.hitsShape(meteor) == True):
            meteors.remove(meteor)
            if (meteor.word.isupper() == True):
                score.value += meteor.width // 2
            elif (score.value >= meteor.width // 2):
                score.value -= meteor.width // 2
        # Remove any meteor that are off the screen.
        if (meteor.top > 400):
            meteors.remove(meteor)

onSteps(30)
onMousePress(200, 200)
for meteor in meteors:
    meteor.word = meteor.word.lower()
    spaceships.centerX = meteor.centerX
    spaceships.centerY = meteor.centerY
onStep()
app.paused = True


# -
app.background = 'black'
app.steps = 0
app.word = 'meteor'

# background
for i in range (30):
    Star(randrange(0, 400), randrange(0, 400), 5, 4, fill='white', opacity=80)

meteors = Group()
spaceships = Group()

Label('Score: ', 325, 25, fill='white', size=20, bold=True)
score = Label(0, 375, 25, fill='white', size=20, bold=True)

def drawMeteor(meteorSize):
    # Draws a new meteor.
    meteor = Group(
        Polygon(0, 340, 0, 365, 20, 400, 40, 365, 40, 340,
                fill=gradient('orange', 'orangeRed', 'black', start='top')),
        Circle(20, 340, 20,
              fill=gradient('white', 'gray', 'dimGray', start='top')),
        Oval(30, 345, 5, 8, fill='dimGray', rotateAngle=20),
        Oval(30, 345, 7, 8,
             fill=gradient('silver', 'gray', start='top'), rotateAngle=20),
        Oval(12, 330, 3, 5,
             fill=gradient('silver', 'gray', start='top'), rotateAngle=20)
        )

    # Sets properties to position, angle, and size the meteor properly.
    meteor.rotateAngle = 180
    meteor.centerX = randrange(0, 400)
    meteor.bottom = 0
    meteor.width = meteorSize
    meteor.height = 2 * meteorSize

    # Randomly decides if the meteor has uppercase or lowercase letters.
    isCaps = randrange(0, 2)

    # Set the new meteor's word depending on if the word should be capital or not.
    if (isCaps == 0):
        meteor.word = app.word.upper()
    else:
        meteor.word = app.word.lower()
    # Adds the letter to the meteor.
    meteor.add(
        Label(meteor.word, meteor.centerX, -15, size=meteorSize/5, bold=True)
        )
    meteors.add(meteor)

def onMousePress(mouseX, mouseY):
    # Draws a new spaceship.
    spaceship = Group(
        Polygon(15, 400, 4, 370, 26, 370,
                fill=gradient('orange', 'darkOrange', 'red', start='right-top')),
        Oval(15, 337, 32, 65, fill='white'),
        RegularPolygon(15, 307, 14, 3, fill='crimson'),
        Circle(15, 332, 10, fill='lightSkyBlue', border='dimGray', borderWidth=3),
        Rect(2, 358, 28, 12, fill='crimson')
        )

    # Sets the target for the spaceship and rotates it to be angled towards that
    # target.
    spaceship.targetX = mouseX
    spaceship.targetY = mouseY
    spaceship.rotateAngle = angleTo(spaceship.centerX, spaceship.centerY,
                                    mouseX, mouseY)
    spaceships.add(spaceship)

def onStep():
    app.steps += 1

    # When the player has 300 points, they win.
    if (score.value >= 300):
        Rect(0, 150, 400, 100, fill='white', opacity=60)
        Label('YOU WIN', 200, 200, size=42, bold=True)
        app.stop()

    # Makes a new star every 20 steps.
    if (app.steps >= 20):
        drawMeteor(randrange(40, 80))
        app.steps = 0

    # Moves each spaceship towards its target position.
    for spaceship in spaceships.children:
        newAngle = angleTo(spaceship.centerX, spaceship.centerY,
                           spaceship.targetX, spaceship.targetY)
        newX, newY = getPointInDir(spaceship.centerX, spaceship.centerY,
                                   newAngle, 5)
        spaceship.centerX = newX
        spaceship.centerY = newY

        # Checks if the spaceship reaches its target and remove it if it has.
        if ((abs(spaceship.centerX - spaceship.targetX) < 5) and
            (abs(spaceship.centerY - spaceship.targetY) < 5)):
            spaceships.remove(spaceship)

    # Moves each of the meteors.
    for meteor in meteors.children:
        meteor.centerY += 4

        # If a spaceship hits the meteor, increment or decrement the score
        # depending on if the meteor's letter is lower or upper case.
        if (spaceships.hitsShape(meteor) == True):
            meteors.remove(meteor)
            if (meteor.word.isupper() == True):
                score.value += meteor.width // 2
            elif (score.value >= meteor.width // 2):
                score.value -= meteor.width // 2
        # Remove any meteor that are off the screen.
        if (meteor.top > 400):
            meteors.remove(meteor)

onSteps(30)
onMousePress(200, 200)
for meteor in meteors:
    meteor.word = meteor.word.lower()
    spaceships.centerX = meteor.centerX
    spaceships.centerY = meteor.centerY
onStep()
app.paused = True

