app.size = 40
app.rows = 10
app.cols = 10
app.land = makeList(app.rows, app.cols)
app.count = 0

def makeLand():
    # Loop over the rows and cols and create rectangles for each value in
    # app.land to draw the initial desert.
    for row in range(app.rows):
        for col in range(app.cols):
            x = col * app.size
            y = row * app.size
            landRect = Rect(x, y, app.size, app.size, fill='khaki', opacity=90)
            app.land[row][col] = landRect
makeLand()

gameOverMessage = Label('You have turned a desert into a forest!', 200, 180,
                        fill='honeydew', size=20, bold=True, visible=False)

def plantATree(x, y):
    # Draws a tree centered at (x, y).
    Rect(x, y + 15, 10, 15,
         fill=gradient('sienna', rgb(120, 50, 30), start='top'), align='center')
    RegularPolygon(x, y, 20, 3,
                   fill=gradient('green', rgb(0, 80, 0), start='top'))
    RegularPolygon(x, y - 15, 15, 3,
                   fill=gradient('lightGreen', 'darkGreen', start='top'))

def getForestColor(distance):
    # The closer the distance to the tree, the greener the color.
    if (distance <= 100):
        color = 'green'
    elif (distance <= 150):
        color = 'limeGreen'
    elif (distance <= 250):
        color = 'yellowGreen'
    else:
        color = 'khaki'
    return color

def isGameOver():
    # Check if the land is all covered with forest.
    for row in range(app.rows):
        for col in range(app.cols):
            if (app.land[row][col].fill != 'green'):
                return False
    return True

def onMousePress(mouseX, mouseY):
    # Plants a tree where you pressed and increments the count.
    plantATree(mouseX, mouseY)
    app.count += 1

    # Updates the ground type to account for the new tree.
    for row in range(app.rows):
        for col in range(app.cols):
            x = col * app.size
            y = row * app.size

            # Gets the distance between the click and every cell in the grid.
            d = distance(mouseX, mouseY, x, y)

            # Uses the distance to get the new color for the cell.
            color = getForestColor(d)

            # If the land isn't already green, change its color.
            if (app.land[row][col].fill != 'green'):
                app.land[row][col].fill = color
    # When the game is over, displays the message and pauses the app.
    if (isGameOver() == True):
        gameOverMessage.visible = True
        gameOverMessage.toFront()
        Label('Trees planted: ' + str(app.count), 200, 220, fill='white',
              size=20, bold=True)
        app.paused = True

onMousePress(70, 55)
onMousePress(330, 60)
onMousePress(200, 80)
onMousePress(85, 325)
onMousePress(290, 320)
onMousePress(80, 210)
onMousePress(295, 220)


# -
app.size = 40
app.rows = 10
app.cols = 10
app.land = makeList(app.rows, app.cols)
app.count = 0

def makeLand():
    # Loop over the rows and cols and create rectangles for each value in
    # app.land to draw the initial desert.
    for row in range(app.rows):
        for col in range(app.cols):
            x = col * app.size
            y = row * app.size
            landRect = Rect(x, y, app.size, app.size, fill='khaki', opacity=90)
            app.land[row][col] = landRect
makeLand()

gameOverMessage = Label('You have turned a desert into a forest!', 200, 180,
                        fill='honeydew', size=20, bold=True, visible=False)

def plantATree(x, y):
    # Draws a tree centered at (x, y).
    Rect(x, y + 15, 10, 15,
         fill=gradient('sienna', rgb(120, 50, 30), start='top'), align='center')
    RegularPolygon(x, y, 20, 3,
                   fill=gradient('green', rgb(0, 80, 0), start='top'))
    RegularPolygon(x, y - 15, 15, 3,
                   fill=gradient('lightGreen', 'darkGreen', start='top'))

def getForestColor(distance):
    # The closer the distance to the tree, the greener the color.
    if (distance <= 100):
        color = 'green'
    elif (distance <= 150):
        color = 'limeGreen'
    elif (distance <= 250):
        color = 'yellowGreen'
    else:
        color = 'khaki'
    return color

def isGameOver():
    # Check if the land is all covered with forest.
    for row in range(app.rows):
        for col in range(app.cols):
            if (app.land[row][col].fill != 'green'):
                return False
    return True

def onMousePress(mouseX, mouseY):
    # Plants a tree where you pressed and increments the count.
    plantATree(mouseX, mouseY)
    app.count += 1

    # Updates the ground type to account for the new tree.
    for row in range(app.rows):
        for col in range(app.cols):
            x = col * app.size
            y = row * app.size

            # Gets the distance between the click and every cell in the grid.
            d = distance(mouseX, mouseY, x, y)

            # Uses the distance to get the new color for the cell.
            color = getForestColor(d)

            # If the land isn't already green, change its color.
            if (app.land[row][col].fill != 'green'):
                app.land[row][col].fill = color
    # When the game is over, displays the message and pauses the app.
    if (isGameOver() == True):
        gameOverMessage.visible = True
        gameOverMessage.toFront()
        Label('Trees planted: ' + str(app.count), 200, 220, fill='white',
              size=20, bold=True)
        app.paused = True

onMousePress(200, 120)
onMousePress(90, 230)
onMousePress(300, 280)


# -
app.size = 40
app.rows = 10
app.cols = 10
app.land = makeList(app.rows, app.cols)
app.count = 0

def makeLand():
    # Loop over the rows and cols and create rectangles for each value in
    # app.land to draw the initial desert.
    for row in range(app.rows):
        for col in range(app.cols):
            x = col * app.size
            y = row * app.size
            landRect = Rect(x, y, app.size, app.size, fill='khaki', opacity=90)
            app.land[row][col] = landRect
makeLand()

gameOverMessage = Label('You have turned a desert into a forest!', 200, 180,
                        fill='honeydew', size=20, bold=True, visible=False)

def plantATree(x, y):
    # Draws a tree centered at (x, y).
    Rect(x, y + 15, 10, 15,
         fill=gradient('sienna', rgb(120, 50, 30), start='top'), align='center')
    RegularPolygon(x, y, 20, 3,
                   fill=gradient('green', rgb(0, 80, 0), start='top'))
    RegularPolygon(x, y - 15, 15, 3,
                   fill=gradient('lightGreen', 'darkGreen', start='top'))

def getForestColor(distance):
    # The closer the distance to the tree, the greener the color.
    if (distance <= 100):
        color = 'green'
    elif (distance <= 150):
        color = 'limeGreen'
    elif (distance <= 250):
        color = 'yellowGreen'
    else:
        color = 'khaki'
    return color

def isGameOver():
    # Check if the land is all covered with forest.
    for row in range(app.rows):
        for col in range(app.cols):
            if (app.land[row][col].fill != 'green'):
                return False
    return True

def onMousePress(mouseX, mouseY):
    # Plants a tree where you pressed and increments the count.
    plantATree(mouseX, mouseY)
    app.count += 1

    # Updates the ground type to account for the new tree.
    for row in range(app.rows):
        for col in range(app.cols):
            x = col * app.size
            y = row * app.size

            # Gets the distance between the click and every cell in the grid.
            d = distance(mouseX, mouseY, x, y)

            # Uses the distance to get the new color for the cell.
            color = getForestColor(d)

            # If the land isn't already green, change its color.
            if (app.land[row][col].fill != 'green'):
                app.land[row][col].fill = color
    # When the game is over, displays the message and pauses the app.
    if (isGameOver() == True):
        gameOverMessage.visible = True
        gameOverMessage.toFront()
        Label('Trees planted: ' + str(app.count), 200, 220, fill='white',
              size=20, bold=True)
        app.paused = True

onMousePress(200, 120)
onMousePress(90, 230)
onMousePress(300, 280)

