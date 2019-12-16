app.background = gradient('sienna', 'peru', start='top')
Line(0, 200, 400, 200, fill='saddleBrown', lineWidth=400, dashes=(3, 35))

# scoreboard
Rect(0, 365, 400, 35, fill='lightGrey', border='black')
Label('Your Score:', 220, 380, size=15, align='right')
score = Label(0, 230, 380, size=15, align='left')

# target
Line(155, 120, 200, 50, fill='white', lineWidth=5)
Line(245, 120, 200, 50, fill='white', lineWidth=5)
Circle(200, 54, 5, fill='darkSlateGray')
Circle(200, 180, 90, fill='white', border='black')
blueBoard = Circle(200, 180, 90, fill='dodgerBlue', border='black')
redBoard = Circle(200, 180, 60, fill='red', border='black')
yellowBoard = Circle(200, 180, 35, fill='yellow', border='black')
Label(30, 200, 195)
Label(20, 200, 225)
Label(10, 200, 255)

# additional targets on the side
Circle(50, 180, 90, fill='white', border='black', align='right')
Circle(45, 180, 90, fill='dodgerBlue', border='black', align='right')
Circle(350, 180, 90, fill='white', border='black', align='left')
Circle(355, 180, 85, fill='dodgerBlue', border='black', align='left')

def drawDart(x, y):
    # Here (x, y) is the center of the body of the dart. The point is 35 pixels
    # to the left of x.
    Polygon(x - 20, y - 2, x - 35, y, x - 20, y + 2)
    Oval(x, y, 50, 15, fill='mediumBlue')
    Polygon(x, y - 7, x + 5, y - 15, x + 25, y - 10, x + 24, y - 2, fill='white')
    Polygon(x, y + 7, x + 5, y + 15, x + 25, y + 10, x + 24, y + 2, fill='white')

def onMousePress(mouseX, mouseY):
    # Draw the dart so that its tip is where you clicked.
    drawDart(mouseX + 35, mouseY)

    # Depending on the dart location add different values to the score.
    # When the dart is thrown outside the board, subtract from the score.
    if (yellowBoard.contains(mouseX, mouseY) == True):
        score.value += 30
    elif (redBoard.contains(mouseX, mouseY) == True):
        score.value += 20
    elif (blueBoard.contains(mouseX, mouseY) == True):
        score.value += 10
    elif (score.value >= 5):
        score.value -= 5

onMousePress(120, 175)


# -
app.background = gradient('sienna', 'peru', start='top')
Line(0, 200, 400, 200, fill='saddleBrown', lineWidth=400, dashes=(3, 35))

# scoreboard
Rect(0, 365, 400, 35, fill='lightGrey', border='black')
Label('Your Score:', 220, 380, size=15, align='right')
score = Label(0, 230, 380, size=15, align='left')

# target
Line(155, 120, 200, 50, fill='white', lineWidth=5)
Line(245, 120, 200, 50, fill='white', lineWidth=5)
Circle(200, 54, 5, fill='darkSlateGray')
Circle(200, 180, 90, fill='white', border='black')
blueBoard = Circle(200, 180, 90, fill='dodgerBlue', border='black')
redBoard = Circle(200, 180, 60, fill='red', border='black')
yellowBoard = Circle(200, 180, 35, fill='yellow', border='black')
Label(30, 200, 195)
Label(20, 200, 225)
Label(10, 200, 255)

# additional targets on the side
Circle(50, 180, 90, fill='white', border='black', align='right')
Circle(45, 180, 90, fill='dodgerBlue', border='black', align='right')
Circle(350, 180, 90, fill='white', border='black', align='left')
Circle(355, 180, 85, fill='dodgerBlue', border='black', align='left')

def drawDart(x, y):
    # Here (x, y) is the center of the body of the dart. The point is 35 pixels
    # to the left of x.
    Polygon(x - 20, y - 2, x - 35, y, x - 20, y + 2)
    Oval(x, y, 50, 15, fill='mediumBlue')
    Polygon(x, y - 7, x + 5, y - 15, x + 25, y - 10, x + 24, y - 2, fill='white')
    Polygon(x, y + 7, x + 5, y + 15, x + 25, y + 10, x + 24, y + 2, fill='white')

def onMousePress(mouseX, mouseY):
    # Draw the dart so that its tip is where you clicked.
    drawDart(mouseX + 35, mouseY)

    # Depending on the dart location add different values to the score.
    # When the dart is thrown outside the board, subtract from the score.
    if (yellowBoard.contains(mouseX, mouseY) == True):
        score.value += 30
    elif (redBoard.contains(mouseX, mouseY) == True):
        score.value += 20
    elif (blueBoard.contains(mouseX, mouseY) == True):
        score.value += 10
    elif (score.value >= 5):
        score.value -= 5

onMousePress(200, 150)
onMousePress(180, 170)
onMousePress(220, 190)
onMousePress(200, 175)
onMousePress(180, 200)


# -
app.background = gradient('sienna', 'peru', start='top')
Line(0, 200, 400, 200, fill='saddleBrown', lineWidth=400, dashes=(3, 35))

# scoreboard
Rect(0, 365, 400, 35, fill='lightGrey', border='black')
Label('Your Score:', 220, 380, size=15, align='right')
score = Label(0, 230, 380, size=15, align='left')

# target
Line(155, 120, 200, 50, fill='white', lineWidth=5)
Line(245, 120, 200, 50, fill='white', lineWidth=5)
Circle(200, 54, 5, fill='darkSlateGray')
Circle(200, 180, 90, fill='white', border='black')
blueBoard = Circle(200, 180, 90, fill='dodgerBlue', border='black')
redBoard = Circle(200, 180, 60, fill='red', border='black')
yellowBoard = Circle(200, 180, 35, fill='yellow', border='black')
Label(30, 200, 195)
Label(20, 200, 225)
Label(10, 200, 255)

# additional targets on the side
Circle(50, 180, 90, fill='white', border='black', align='right')
Circle(45, 180, 90, fill='dodgerBlue', border='black', align='right')
Circle(350, 180, 90, fill='white', border='black', align='left')
Circle(355, 180, 85, fill='dodgerBlue', border='black', align='left')

def drawDart(x, y):
    # Here (x, y) is the center of the body of the dart. The point is 35 pixels
    # to the left of x.
    Polygon(x - 20, y - 2, x - 35, y, x - 20, y + 2)
    Oval(x, y, 50, 15, fill='mediumBlue')
    Polygon(x, y - 7, x + 5, y - 15, x + 25, y - 10, x + 24, y - 2, fill='white')
    Polygon(x, y + 7, x + 5, y + 15, x + 25, y + 10, x + 24, y + 2, fill='white')

def onMousePress(mouseX, mouseY):
    # Draw the dart so that its tip is where you clicked.
    drawDart(mouseX + 35, mouseY)

    # Depending on the dart location add different values to the score.
    # When the dart is thrown outside the board, subtract from the score.
    if (yellowBoard.contains(mouseX, mouseY) == True):
        score.value += 30
    elif (redBoard.contains(mouseX, mouseY) == True):
        score.value += 20
    elif (blueBoard.contains(mouseX, mouseY) == True):
        score.value += 10
    elif (score.value >= 5):
        score.value -= 5

onMousePress(120, 175)

