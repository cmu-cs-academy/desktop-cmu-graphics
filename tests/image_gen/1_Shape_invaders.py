app.background = 'black'
app.index = 0

# Earth
Oval(200, 400, 600, 100, fill='lightSkyBlue', border='mediumSeaGreen',
     borderWidth=8)
Polygon(-50, 375, 40, 390, 140, 365, 205, 380, 290, 365, 355, 360,
        400, 365, 245, 355, 145, 355, fill='mediumSeaGreen')

# Draws stars in the background.
for i in range(100):
    Circle(randrange(0, 400), randrange(0, 350), 1, fill='white')

# Shapes along the bottom.
app.shapes = [ Circle(70, 310, 30, fill='tomato', border='lime'),
               RegularPolygon(200, 310, 35, 3, fill='darkGray', border='gray'),
               RegularPolygon(330, 310, 35, 4, fill='orange', border='gray') ]

# Shapes that fall from the top.
app.fallingShapes = [ RegularPolygon(70, 0, 35, 3, fill='darkGray', border='gray'),
                      RegularPolygon(200, 0, 35, 4, fill='orange', border='gray'),
                      Circle(330, 0, 30, fill='tomato', border='gray') ]

def checkShapes():
    # Loops through each of the shapes.
    for i in range(len(app.shapes)):
        # If the fills don't match, return False.
        if (app.fallingShapes[i].fill != app.shapes[i].fill):
            return False
    # If all the fills match, return True.
    return True
def setBorders():
    # Highlights the selected shape.
    for i in range(len(app.shapes)):
        if (i == app.index):
            app.shapes[i].border = 'lime'
        else:
            app.shapes[i].border = 'gray'

def onKeyPress(key):
    x = app.index * 130 + 70

    # Changes the selected shape on space.
    if (key == 'space'):
        app.index += 1
        if (app.index == 3):
            app.index = 0
        setBorders()

    # If the key is c, change the shape at app.index to a circle.
    if (key == 'c'):
        app.shapes[app.index].visible = False
        app.shapes[app.index] = Circle(x, 310, 30, fill='tomato',
                                       border='lime')
    # If the key is t, change the shape at app.index to a triangle.
    if (key == 't'):
        app.shapes[app.index].visible = False
        app.shapes[app.index] = RegularPolygon(x, 310, 35, 3, fill='darkGray',
                                               border='lime')
    # If the key is d, change the shape at app.index to a diamond.
    if (key == 'd'):
        app.shapes[app.index].visible = False
        app.shapes[app.index] = RegularPolygon(x, 310, 35, 4, fill='orange',
                                               border='lime')
def onStep():
    # Moves all the shapes and check for a win or loss.
    for shape in app.fallingShapes:
        shape.centerY += 3
        if (shape.centerY >= 310):
            if (checkShapes() == False):
                Label('YOU LOSE', 200, 200, fill='gold', size=40)
            else:
                Label('YOU WIN', 200, 200, fill='gold', size=40)

            app.stop()

onKeyPress('d')
onKeyPress('space')
onKeyPress('c')
app.paused = True


# -
app.background = 'black'
app.index = 0

# Earth
Oval(200, 400, 600, 100, fill='lightSkyBlue', border='mediumSeaGreen',
     borderWidth=8)
Polygon(-50, 375, 40, 390, 140, 365, 205, 380, 290, 365, 355, 360,
        400, 365, 245, 355, 145, 355, fill='mediumSeaGreen')

# Draws stars in the background.
for i in range(100):
    Circle(randrange(0, 400), randrange(0, 350), 1, fill='white')

# Shapes along the bottom.
app.shapes = [ Circle(70, 310, 30, fill='tomato', border='lime'),
               RegularPolygon(200, 310, 35, 3, fill='darkGray', border='gray'),
               RegularPolygon(330, 310, 35, 4, fill='orange', border='gray') ]

# Shapes that fall from the top.
app.fallingShapes = [ RegularPolygon(70, 0, 35, 3, fill='darkGray', border='gray'),
                      RegularPolygon(200, 0, 35, 4, fill='orange', border='gray'),
                      Circle(330, 0, 30, fill='tomato', border='gray') ]

def checkShapes():
    # Loops through each of the shapes.
    for i in range(len(app.shapes)):
        # If the fills don't match, return False.
        if (app.fallingShapes[i].fill != app.shapes[i].fill):
            return False
    # If all the fills match, return True.
    return True
def setBorders():
    # Highlights the selected shape.
    for i in range(len(app.shapes)):
        if (i == app.index):
            app.shapes[i].border = 'lime'
        else:
            app.shapes[i].border = 'gray'

def onKeyPress(key):
    x = app.index * 130 + 70

    # Changes the selected shape on space.
    if (key == 'space'):
        app.index += 1
        if (app.index == 3):
            app.index = 0
        setBorders()

    # If the key is c, change the shape at app.index to a circle.
    if (key == 'c'):
        app.shapes[app.index].visible = False
        app.shapes[app.index] = Circle(x, 310, 30, fill='tomato',
                                       border='lime')
    # If the key is t, change the shape at app.index to a triangle.
    if (key == 't'):
        app.shapes[app.index].visible = False
        app.shapes[app.index] = RegularPolygon(x, 310, 35, 3, fill='darkGray',
                                               border='lime')
    # If the key is d, change the shape at app.index to a diamond.
    if (key == 'd'):
        app.shapes[app.index].visible = False
        app.shapes[app.index] = RegularPolygon(x, 310, 35, 4, fill='orange',
                                               border='lime')
def onStep():
    # Moves all the shapes and check for a win or loss.
    for shape in app.fallingShapes:
        shape.centerY += 3
        if (shape.centerY >= 310):
            if (checkShapes() == False):
                Label('YOU LOSE', 200, 200, fill='gold', size=40)
            else:
                Label('YOU WIN', 200, 200, fill='gold', size=40)

            app.stop()

onKeyPress('t')
onSteps(105)
app.paused = True


# -
app.background = 'black'
app.index = 0

# Earth
Oval(200, 400, 600, 100, fill='lightSkyBlue', border='mediumSeaGreen',
     borderWidth=8)
Polygon(-50, 375, 40, 390, 140, 365, 205, 380, 290, 365, 355, 360,
        400, 365, 245, 355, 145, 355, fill='mediumSeaGreen')

# Draws stars in the background.
for i in range(100):
    Circle(randrange(0, 400), randrange(0, 350), 1, fill='white')

# Shapes along the bottom.
app.shapes = [ Circle(70, 310, 30, fill='tomato', border='lime'),
               RegularPolygon(200, 310, 35, 3, fill='darkGray', border='gray'),
               RegularPolygon(330, 310, 35, 4, fill='orange', border='gray') ]

# Shapes that fall from the top.
app.fallingShapes = [ RegularPolygon(70, 0, 35, 3, fill='darkGray', border='gray'),
                      RegularPolygon(200, 0, 35, 4, fill='orange', border='gray'),
                      Circle(330, 0, 30, fill='tomato', border='gray') ]

def checkShapes():
    # Loops through each of the shapes.
    for i in range(len(app.shapes)):
        # If the fills don't match, return False.
        if (app.fallingShapes[i].fill != app.shapes[i].fill):
            return False
    # If all the fills match, return True.
    return True
def setBorders():
    # Highlights the selected shape.
    for i in range(len(app.shapes)):
        if (i == app.index):
            app.shapes[i].border = 'lime'
        else:
            app.shapes[i].border = 'gray'

def onKeyPress(key):
    x = app.index * 130 + 70

    # Changes the selected shape on space.
    if (key == 'space'):
        app.index += 1
        if (app.index == 3):
            app.index = 0
        setBorders()

    # If the key is c, change the shape at app.index to a circle.
    if (key == 'c'):
        app.shapes[app.index].visible = False
        app.shapes[app.index] = Circle(x, 310, 30, fill='tomato',
                                       border='lime')
    # If the key is t, change the shape at app.index to a triangle.
    if (key == 't'):
        app.shapes[app.index].visible = False
        app.shapes[app.index] = RegularPolygon(x, 310, 35, 3, fill='darkGray',
                                               border='lime')
    # If the key is d, change the shape at app.index to a diamond.
    if (key == 'd'):
        app.shapes[app.index].visible = False
        app.shapes[app.index] = RegularPolygon(x, 310, 35, 4, fill='orange',
                                               border='lime')
def onStep():
    # Moves all the shapes and check for a win or loss.
    for shape in app.fallingShapes:
        shape.centerY += 3
        if (shape.centerY >= 310):
            if (checkShapes() == False):
                Label('YOU LOSE', 200, 200, fill='gold', size=40)
            else:
                Label('YOU WIN', 200, 200, fill='gold', size=40)

            app.stop()

onKeyPress('space')
onKeyPress('space')
onKeyPress('c')
app.paused = True

