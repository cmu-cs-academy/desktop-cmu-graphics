app.background = 'black'

# Define the rows and cols properties to properly define the 2D lightbulb
# list so it can hold the proper number of lightbulbs.
app.rows = 3
app.cols = 3
app.lights = makeList(app.rows, app.cols)
app.lightsOut = False

Label('Moves:', 190, 40, fill='white', size=20)
moves = Label(0, 240, 40, fill='white', size=20)

def createLightBulb(x, y):
    lightBulb = Group(
        Circle(x, y, 29, fill='gainsboro'),
        Oval(x + 15, y - 15, 8, 20, fill='white', rotateAngle=-50, opacity=70),
        Polygon(x - 27, y + 10, x + 27, y + 10, x + 12, y + 50, x - 12, y + 50,
                fill='gainsboro'),
        Polygon(x - 7, y + 52, x - 12, y + 5, x - 6, y + 10, x, y + 5,
                x + 6, y + 10, x + 12, y + 5, x + 7, y + 52, fill=None,
                border='dimGray'),
        Oval(x, y + 65, 10, 5, fill='gray'),
        Polygon(x - 10, y + 50, x + 10, y + 50, x + 6, y + 65, x - 6, y + 65,
                fill='goldenrod'),
        Line(x, y + 55, x, y + 65, fill='white', lineWidth=15, dashes=(1, 2))
        )

    # Adds a custom property that references a circle and return the lightBulb.
    lightBulb.light = Circle(x, y, 45, fill=gradient('yellow', 'cornSilk'),
                             opacity=75)
    return lightBulb

def drawLights():
    startX = 100
    startY = 120
    lightSize = 100

    # Loop over rows and cols and calculate the x and y values. For each
    # position, create a lightbulb and store its return value in app.lights.
    for row in range(app.rows):
        for col in range(app.cols):
            x = startX + col * lightSize
            y = startY + row * lightSize
            app.lights[row][col] = createLightBulb(x, y)
drawLights()

def turnLight(row, col):
    # This allows us to access the lightbulbs above, below, to the left, and to
    # the right of the lightbulb we clicked on.
    rowChange = [ 0, -1, 1, 0, 0 ]
    colChange = [ 0, 0, 0, -1, 1 ]

    # Changes lights near the row, col from on to off or off to on.
    for i in range(len(rowChange)):
        # These are either +1, 0, or -1.
        dRow, dCol = rowChange[i], colChange[i]

        # As long as row + dRow and col + dCol are valid indices for app.lights,
        # switches the visibility of the light at those indices.
        if ((row + dRow >= 0) and (row + dRow <= 2) and
            (col + dCol >= 0) and (col + dCol <= 2)):
            lightBulb = app.lights[row + dRow][col + dCol]
            lightBulb.light.visible = not lightBulb.light.visible

def checkWin():
    # Check if all the lights are off.
    for row in range(app.rows):
        for col in range(app.cols):
            lightbulb = app.lights[row][col]
            light = lightbulb.light

            # If the light is visible return False.
            if (light.visible == True):
                return False
    return True

def findLight(mouseX, mouseY):
    # Check each light to see if it was clicked. If it was, call turnLight
    # and return the light.
    for row in range(app.rows):
        for col in range(app.cols):
            light = app.lights[row][col]
            if (light.hits(mouseX, mouseY) == True):
                turnLight(row, col)
                return light
    return None
def onMousePress(mouseX, mouseY):
    # Only changes the state of the lights when the player hasn't won.
    if (app.lightsOut == False):
       light = findLight(mouseX, mouseY)
       if (light != None):
            moves.value += 1

    # Draws the winning screen when the player wins.
    if (checkWin() == True):
        app.lightsOut = True
        Rect(0, 0, 400, 400, opacity=70)
        Label('Lights Out!', 200, 200, fill='gold', size=40, font='monospace',
              bold=True)

onMousePress(200, 230)
onMousePress(300, 230)


# -
app.background = 'black'

# Define the rows and cols properties to properly define the 2D lightbulb
# list so it can hold the proper number of lightbulbs.
app.rows = 3
app.cols = 3
app.lights = makeList(app.rows, app.cols)
app.lightsOut = False

Label('Moves:', 190, 40, fill='white', size=20)
moves = Label(0, 240, 40, fill='white', size=20)

def createLightBulb(x, y):
    lightBulb = Group(
        Circle(x, y, 29, fill='gainsboro'),
        Oval(x + 15, y - 15, 8, 20, fill='white', rotateAngle=-50, opacity=70),
        Polygon(x - 27, y + 10, x + 27, y + 10, x + 12, y + 50, x - 12, y + 50,
                fill='gainsboro'),
        Polygon(x - 7, y + 52, x - 12, y + 5, x - 6, y + 10, x, y + 5,
                x + 6, y + 10, x + 12, y + 5, x + 7, y + 52, fill=None,
                border='dimGray'),
        Oval(x, y + 65, 10, 5, fill='gray'),
        Polygon(x - 10, y + 50, x + 10, y + 50, x + 6, y + 65, x - 6, y + 65,
                fill='goldenrod'),
        Line(x, y + 55, x, y + 65, fill='white', lineWidth=15, dashes=(1, 2))
        )

    # Adds a custom property that references a circle and return the lightBulb.
    lightBulb.light = Circle(x, y, 45, fill=gradient('yellow', 'cornSilk'),
                             opacity=75)
    return lightBulb

def drawLights():
    startX = 100
    startY = 120
    lightSize = 100

    # Loop over rows and cols and calculate the x and y values. For each
    # position, create a lightbulb and store its return value in app.lights.
    for row in range(app.rows):
        for col in range(app.cols):
            x = startX + col * lightSize
            y = startY + row * lightSize
            app.lights[row][col] = createLightBulb(x, y)
drawLights()

def turnLight(row, col):
    # This allows us to access the lightbulbs above, below, to the left, and to
    # the right of the lightbulb we clicked on.
    rowChange = [ 0, -1, 1, 0, 0 ]
    colChange = [ 0, 0, 0, -1, 1 ]

    # Changes lights near the row, col from on to off or off to on.
    for i in range(len(rowChange)):
        # These are either +1, 0, or -1.
        dRow, dCol = rowChange[i], colChange[i]

        # As long as row + dRow and col + dCol are valid indices for app.lights,
        # switches the visibility of the light at those indices.
        if ((row + dRow >= 0) and (row + dRow <= 2) and
            (col + dCol >= 0) and (col + dCol <= 2)):
            lightBulb = app.lights[row + dRow][col + dCol]
            lightBulb.light.visible = not lightBulb.light.visible

def checkWin():
    # Check if all the lights are off.
    for row in range(app.rows):
        for col in range(app.cols):
            lightbulb = app.lights[row][col]
            light = lightbulb.light

            # If the light is visible return False.
            if (light.visible == True):
                return False
    return True

def findLight(mouseX, mouseY):
    # Check each light to see if it was clicked. If it was, call turnLight
    # and return the light.
    for row in range(app.rows):
        for col in range(app.cols):
            light = app.lights[row][col]
            if (light.hits(mouseX, mouseY) == True):
                turnLight(row, col)
                return light
    return None
def onMousePress(mouseX, mouseY):
    # Only changes the state of the lights when the player hasn't won.
    if (app.lightsOut == False):
       light = findLight(mouseX, mouseY)
       if (light != None):
            moves.value += 1

    # Draws the winning screen when the player wins.
    if (checkWin() == True):
        app.lightsOut = True
        Rect(0, 0, 400, 400, opacity=70)
        Label('Lights Out!', 200, 200, fill='gold', size=40, font='monospace',
              bold=True)

onMousePress(100, 130)
onMousePress(300, 130)
onMousePress(200, 230)
onMousePress(100, 330)
onMousePress(300, 330)


# -
app.background = 'black'

# Define the rows and cols properties to properly define the 2D lightbulb
# list so it can hold the proper number of lightbulbs.
app.rows = 3
app.cols = 3
app.lights = makeList(app.rows, app.cols)
app.lightsOut = False

Label('Moves:', 190, 40, fill='white', size=20)
moves = Label(0, 240, 40, fill='white', size=20)

def createLightBulb(x, y):
    lightBulb = Group(
        Circle(x, y, 29, fill='gainsboro'),
        Oval(x + 15, y - 15, 8, 20, fill='white', rotateAngle=-50, opacity=70),
        Polygon(x - 27, y + 10, x + 27, y + 10, x + 12, y + 50, x - 12, y + 50,
                fill='gainsboro'),
        Polygon(x - 7, y + 52, x - 12, y + 5, x - 6, y + 10, x, y + 5,
                x + 6, y + 10, x + 12, y + 5, x + 7, y + 52, fill=None,
                border='dimGray'),
        Oval(x, y + 65, 10, 5, fill='gray'),
        Polygon(x - 10, y + 50, x + 10, y + 50, x + 6, y + 65, x - 6, y + 65,
                fill='goldenrod'),
        Line(x, y + 55, x, y + 65, fill='white', lineWidth=15, dashes=(1, 2))
        )

    # Adds a custom property that references a circle and return the lightBulb.
    lightBulb.light = Circle(x, y, 45, fill=gradient('yellow', 'cornSilk'),
                             opacity=75)
    return lightBulb

def drawLights():
    startX = 100
    startY = 120
    lightSize = 100

    # Loop over rows and cols and calculate the x and y values. For each
    # position, create a lightbulb and store its return value in app.lights.
    for row in range(app.rows):
        for col in range(app.cols):
            x = startX + col * lightSize
            y = startY + row * lightSize
            app.lights[row][col] = createLightBulb(x, y)
drawLights()

def turnLight(row, col):
    # This allows us to access the lightbulbs above, below, to the left, and to
    # the right of the lightbulb we clicked on.
    rowChange = [ 0, -1, 1, 0, 0 ]
    colChange = [ 0, 0, 0, -1, 1 ]

    # Changes lights near the row, col from on to off or off to on.
    for i in range(len(rowChange)):
        # These are either +1, 0, or -1.
        dRow, dCol = rowChange[i], colChange[i]

        # As long as row + dRow and col + dCol are valid indices for app.lights,
        # switches the visibility of the light at those indices.
        if ((row + dRow >= 0) and (row + dRow <= 2) and
            (col + dCol >= 0) and (col + dCol <= 2)):
            lightBulb = app.lights[row + dRow][col + dCol]
            lightBulb.light.visible = not lightBulb.light.visible

def checkWin():
    # Check if all the lights are off.
    for row in range(app.rows):
        for col in range(app.cols):
            lightbulb = app.lights[row][col]
            light = lightbulb.light

            # If the light is visible return False.
            if (light.visible == True):
                return False
    return True

def findLight(mouseX, mouseY):
    # Check each light to see if it was clicked. If it was, call turnLight
    # and return the light.
    for row in range(app.rows):
        for col in range(app.cols):
            light = app.lights[row][col]
            if (light.hits(mouseX, mouseY) == True):
                turnLight(row, col)
                return light
    return None
def onMousePress(mouseX, mouseY):
    # Only changes the state of the lights when the player hasn't won.
    if (app.lightsOut == False):
       light = findLight(mouseX, mouseY)
       if (light != None):
            moves.value += 1

    # Draws the winning screen when the player wins.
    if (checkWin() == True):
        app.lightsOut = True
        Rect(0, 0, 400, 400, opacity=70)
        Label('Lights Out!', 200, 200, fill='gold', size=40, font='monospace',
              bold=True)


