app.background = 'black'
Circle(200, 800, 800, fill=gradient('lightSkyBlue', 'deepSkyBlue', 'black'),
       opacity=75)

Label('Press space to safely teleport!', 200, 30, fill='white', size=18,
      bold=True)
speech = Label('AHHHHH!', 50, 75, fill='white', size=14, bold=True,
               align='left')

planet = Group(
    Circle(200, 800, 500, fill='dodgerBlue'),
    Polygon(155, 305, 50, 330, 120, 355, 185, 335, 230, 355, 260, 330,
            330, 350, 365, 335, 255, 305, fill='darkGreen'),
    Circle(200, 800, 500, fill=None, border='darkGreen', borderWidth=10)
    )

# astronaut
astronaut = Group(
    Rect(15, 100, 40, 40, fill='darkGray'),
    Circle(35, 95, 15, fill='white'),
    Rect(20, 110, 30, 40, fill='white'),
    Rect(10, 110, 50, 12, fill='white'),
    Rect(25, 88, 20, 14, fill='steelBlue'),
    Line(35, 135, 35, 150),
    Rect(30, 117, 10, 10, fill='gray'),
    Rect(15, 110, 3, 12, fill='fireBrick'),
    Rect(52, 110, 3, 12, fill='fireBrick')
    )
astronaut.rescue = False

def onKeyPress(key):
    # Press 'space' to teleport the astronaut to ground level.
    if ((astronaut.rescue == False) and (key == 'space')):
        astronaut.rotateAngle = 0

        # Get the angle from the astronaut to the planet.
        angle = angleTo(astronaut.centerX, astronaut.centerY,
                        planet.centerX, planet.centerY)
        # Move the astronaut by 1 pixel to the planet until the astronaut's
        # bottom is contained in the planet.
        while (planet.contains(astronaut.centerX, astronaut.bottom) == False):
            newX, newY = getPointInDir(astronaut.centerX, astronaut.centerY,
                                       angle, 1)
            astronaut.centerX = newX
            astronaut.centerY = newY
        # Sets the astronaut as rescued and rotate.
        astronaut.rescue = True
        astronaut.rotateAngle = angle - 180

        # Changes and moves the text next to the astronaut.
        speech.value = 'Phew!'
        speech.centerX = astronaut.centerX
        speech.centerY = astronaut.centerY - 50

def onStep():
    # Moves the astronaut towards the right edge of the screen.
    if ((astronaut.left < 400) and (astronaut.rescue == False)):
        astronaut.centerX += 2
        astronaut.rotateAngle += 5
        speech.centerX += 2

    # If the astronaut flies off the screen, adds a label and pause the app.
    elif (astronaut.left >= 400):
        Label('NOOOOOO! Lost in space!', 200, 60, fill='white', size=14,
              bold=True)
        app.paused = True

onSteps(20)
app.paused = True


# -
app.background = 'black'
Circle(200, 800, 800, fill=gradient('lightSkyBlue', 'deepSkyBlue', 'black'),
       opacity=75)

Label('Press space to safely teleport!', 200, 30, fill='white', size=18,
      bold=True)
speech = Label('AHHHHH!', 50, 75, fill='white', size=14, bold=True,
               align='left')

planet = Group(
    Circle(200, 800, 500, fill='dodgerBlue'),
    Polygon(155, 305, 50, 330, 120, 355, 185, 335, 230, 355, 260, 330,
            330, 350, 365, 335, 255, 305, fill='darkGreen'),
    Circle(200, 800, 500, fill=None, border='darkGreen', borderWidth=10)
    )

# astronaut
astronaut = Group(
    Rect(15, 100, 40, 40, fill='darkGray'),
    Circle(35, 95, 15, fill='white'),
    Rect(20, 110, 30, 40, fill='white'),
    Rect(10, 110, 50, 12, fill='white'),
    Rect(25, 88, 20, 14, fill='steelBlue'),
    Line(35, 135, 35, 150),
    Rect(30, 117, 10, 10, fill='gray'),
    Rect(15, 110, 3, 12, fill='fireBrick'),
    Rect(52, 110, 3, 12, fill='fireBrick')
    )
astronaut.rescue = False

def onKeyPress(key):
    # Press 'space' to teleport the astronaut to ground level.
    if ((astronaut.rescue == False) and (key == 'space')):
        astronaut.rotateAngle = 0

        # Get the angle from the astronaut to the planet.
        angle = angleTo(astronaut.centerX, astronaut.centerY,
                        planet.centerX, planet.centerY)
        # Move the astronaut by 1 pixel to the planet until the astronaut's
        # bottom is contained in the planet.
        while (planet.contains(astronaut.centerX, astronaut.bottom) == False):
            newX, newY = getPointInDir(astronaut.centerX, astronaut.centerY,
                                       angle, 1)
            astronaut.centerX = newX
            astronaut.centerY = newY
        # Sets the astronaut as rescued and rotate.
        astronaut.rescue = True
        astronaut.rotateAngle = angle - 180

        # Changes and moves the text next to the astronaut.
        speech.value = 'Phew!'
        speech.centerX = astronaut.centerX
        speech.centerY = astronaut.centerY - 50

def onStep():
    # Moves the astronaut towards the right edge of the screen.
    if ((astronaut.left < 400) and (astronaut.rescue == False)):
        astronaut.centerX += 2
        astronaut.rotateAngle += 5
        speech.centerX += 2

    # If the astronaut flies off the screen, adds a label and pause the app.
    elif (astronaut.left >= 400):
        Label('NOOOOOO! Lost in space!', 200, 60, fill='white', size=14,
              bold=True)
        app.paused = True

onSteps(100)
onKeyPress('space')


# -
app.background = 'black'
Circle(200, 800, 800, fill=gradient('lightSkyBlue', 'deepSkyBlue', 'black'),
       opacity=75)

Label('Press space to safely teleport!', 200, 30, fill='white', size=18,
      bold=True)
speech = Label('AHHHHH!', 50, 75, fill='white', size=14, bold=True,
               align='left')

planet = Group(
    Circle(200, 800, 500, fill='dodgerBlue'),
    Polygon(155, 305, 50, 330, 120, 355, 185, 335, 230, 355, 260, 330,
            330, 350, 365, 335, 255, 305, fill='darkGreen'),
    Circle(200, 800, 500, fill=None, border='darkGreen', borderWidth=10)
    )

# astronaut
astronaut = Group(
    Rect(15, 100, 40, 40, fill='darkGray'),
    Circle(35, 95, 15, fill='white'),
    Rect(20, 110, 30, 40, fill='white'),
    Rect(10, 110, 50, 12, fill='white'),
    Rect(25, 88, 20, 14, fill='steelBlue'),
    Line(35, 135, 35, 150),
    Rect(30, 117, 10, 10, fill='gray'),
    Rect(15, 110, 3, 12, fill='fireBrick'),
    Rect(52, 110, 3, 12, fill='fireBrick')
    )
astronaut.rescue = False

def onKeyPress(key):
    # Press 'space' to teleport the astronaut to ground level.
    if ((astronaut.rescue == False) and (key == 'space')):
        astronaut.rotateAngle = 0

        # Get the angle from the astronaut to the planet.
        angle = angleTo(astronaut.centerX, astronaut.centerY,
                        planet.centerX, planet.centerY)
        # Move the astronaut by 1 pixel to the planet until the astronaut's
        # bottom is contained in the planet.
        while (planet.contains(astronaut.centerX, astronaut.bottom) == False):
            newX, newY = getPointInDir(astronaut.centerX, astronaut.centerY,
                                       angle, 1)
            astronaut.centerX = newX
            astronaut.centerY = newY
        # Sets the astronaut as rescued and rotate.
        astronaut.rescue = True
        astronaut.rotateAngle = angle - 180

        # Changes and moves the text next to the astronaut.
        speech.value = 'Phew!'
        speech.centerX = astronaut.centerX
        speech.centerY = astronaut.centerY - 50

def onStep():
    # Moves the astronaut towards the right edge of the screen.
    if ((astronaut.left < 400) and (astronaut.rescue == False)):
        astronaut.centerX += 2
        astronaut.rotateAngle += 5
        speech.centerX += 2

    # If the astronaut flies off the screen, adds a label and pause the app.
    elif (astronaut.left >= 400):
        Label('NOOOOOO! Lost in space!', 200, 60, fill='white', size=14,
              bold=True)
        app.paused = True

onSteps(205)
app.paused = True

