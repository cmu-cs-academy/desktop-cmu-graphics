app.background = gradient('lightSkyBlue', 'skyBlue')

# sun and grass
Star(0, 0, 70, 60, fill='yellow', roundness=40)
Circle(0, 0, 55, fill=gradient('yellow', 'khaki'))
Rect(0, 150, 400, 250, fill=gradient('yellowGreen', 'forestGreen', start='top'))

Label('Flower count:', 340, 20, align='right')
flowerCount = Label(0, 350, 20, align='left')

def drawFlower(x, y, size, color):
    # stem and petals
    Line(x, y, x, y + 2 * size, fill='mediumSeaGreen')
    Star(x, y, size, 12, fill=color)

    # Changes the fill of the center part of the flower depending on the petals.
    if (color == 'yellow'):
        innerFill = 'peru'
    elif (color == 'lightCyan'):
        innerFill = 'skyBlue'
    elif (color == 'white'):
        innerFill = 'pink'
    Circle(x, y, size // 2, fill=innerFill)

def onStep():
    # As long as there aren't too many flowers, make another.
    if (flowerCount.value < 175):
        # Get the random position of the flower. It can't be higher than the
        # grass and the lowest point it can be is a y value of 390.
        flowerX = randrange(0, 400)
        flowerY = randrange(150, 391)
        # Makes the flower size bigger the lower it is on the canvas.
        size = 2 * flowerY // 100
        # Randomly define pickColor to a value between 0 and 100 (excluding
        # 100). If it is less than 60, set the color to yellow, if it is
        # between 60 and 80 set it to lightCyan, and white otherwise.
        pickColor = randrange(0, 100)
        if (pickColor < 60):
            color = 'yellow'
        elif (pickColor < 80):
            color = 'lightCyan'
        else:
            color = 'white'
        drawFlower(flowerX, flowerY, size, color)
        flowerCount.value += 1

onSteps(50)
app.paused = True


# -
app.background = gradient('lightSkyBlue', 'skyBlue')

# sun and grass
Star(0, 0, 70, 60, fill='yellow', roundness=40)
Circle(0, 0, 55, fill=gradient('yellow', 'khaki'))
Rect(0, 150, 400, 250, fill=gradient('yellowGreen', 'forestGreen', start='top'))

Label('Flower count:', 340, 20, align='right')
flowerCount = Label(0, 350, 20, align='left')

def drawFlower(x, y, size, color):
    # stem and petals
    Line(x, y, x, y + 2 * size, fill='mediumSeaGreen')
    Star(x, y, size, 12, fill=color)

    # Changes the fill of the center part of the flower depending on the petals.
    if (color == 'yellow'):
        innerFill = 'peru'
    elif (color == 'lightCyan'):
        innerFill = 'skyBlue'
    elif (color == 'white'):
        innerFill = 'pink'
    Circle(x, y, size // 2, fill=innerFill)

def onStep():
    # As long as there aren't too many flowers, make another.
    if (flowerCount.value < 175):
        # Get the random position of the flower. It can't be higher than the
        # grass and the lowest point it can be is a y value of 390.
        flowerX = randrange(0, 400)
        flowerY = randrange(150, 391)
        # Makes the flower size bigger the lower it is on the canvas.
        size = 2 * flowerY // 100
        # Randomly define pickColor to a value between 0 and 100 (excluding
        # 100). If it is less than 60, set the color to yellow, if it is
        # between 60 and 80 set it to lightCyan, and white otherwise.
        pickColor = randrange(0, 100)
        if (pickColor < 60):
            color = 'yellow'
        elif (pickColor < 80):
            color = 'lightCyan'
        else:
            color = 'white'
        drawFlower(flowerX, flowerY, size, color)
        flowerCount.value += 1

onSteps(50)
app.paused = True


# -
app.background = gradient('lightSkyBlue', 'skyBlue')

# sun and grass
Star(0, 0, 70, 60, fill='yellow', roundness=40)
Circle(0, 0, 55, fill=gradient('yellow', 'khaki'))
Rect(0, 150, 400, 250, fill=gradient('yellowGreen', 'forestGreen', start='top'))

Label('Flower count:', 340, 20, align='right')
flowerCount = Label(0, 350, 20, align='left')

def drawFlower(x, y, size, color):
    # stem and petals
    Line(x, y, x, y + 2 * size, fill='mediumSeaGreen')
    Star(x, y, size, 12, fill=color)

    # Changes the fill of the center part of the flower depending on the petals.
    if (color == 'yellow'):
        innerFill = 'peru'
    elif (color == 'lightCyan'):
        innerFill = 'skyBlue'
    elif (color == 'white'):
        innerFill = 'pink'
    Circle(x, y, size // 2, fill=innerFill)

def onStep():
    # As long as there aren't too many flowers, make another.
    if (flowerCount.value < 175):
        # Get the random position of the flower. It can't be higher than the
        # grass and the lowest point it can be is a y value of 390.
        flowerX = randrange(0, 400)
        flowerY = randrange(150, 391)
        # Makes the flower size bigger the lower it is on the canvas.
        size = 2 * flowerY // 100
        # Randomly define pickColor to a value between 0 and 100 (excluding
        # 100). If it is less than 60, set the color to yellow, if it is
        # between 60 and 80 set it to lightCyan, and white otherwise.
        pickColor = randrange(0, 100)
        if (pickColor < 60):
            color = 'yellow'
        elif (pickColor < 80):
            color = 'lightCyan'
        else:
            color = 'white'
        drawFlower(flowerX, flowerY, size, color)
        flowerCount.value += 1

onStep()
app.paused = True

