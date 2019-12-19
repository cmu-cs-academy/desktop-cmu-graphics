app.background = gradient('black', 'midnightBlue', start='left-top')
app.diagonalStarSize = 12
app.paused = True

# shooting star tail
Polygon (0, 0, 350, 400, 380, 400, fill='paleGreen', opacity=70)
Polygon (0, 0, 380, 400, 400, 400, 400, 380, fill='pink', opacity=70)
Polygon (0, 0, 400, 380, 400, 350, fill='paleTurquoise', opacity=70)

diagonalStars = Group()
# Create an 8x8 grid of stars, equally spaced throughout the screen.
# The stars along the diagonal should be gold and increase in size by 3
# each time you move right and down along the canvas.
for row in range(8):
    for col in range(8):
        x = 50 * col + 20
        y = 50 * row + 20
        if (x == y):
            diagonalStars.add(
                Star(x, y, app.diagonalStarSize, 5,
                     fill=gradient('yellow', 'goldenrod'))
                )
            app.diagonalStarSize += 3
        else:
            Star(x, y, 5, 5, fill='white', roundness=20)
def onKeyPress(key):
    # When any key is pressed, unpause the app.
    app.paused = False

def onStep():
    # Move the diagonal stars 10 pixels towards the right-bottom of the canvas.
    newX, newY = getPointInDir(diagonalStars.centerX, diagonalStars.centerY,
                               135, 10)
    diagonalStars.centerX = newX
    diagonalStars.centerY = newY

onKeyPress('space')


# -
app.background = gradient('black', 'midnightBlue', start='left-top')
app.diagonalStarSize = 12
app.paused = True

# shooting star tail
Polygon (0, 0, 350, 400, 380, 400, fill='paleGreen', opacity=70)
Polygon (0, 0, 380, 400, 400, 400, 400, 380, fill='pink', opacity=70)
Polygon (0, 0, 400, 380, 400, 350, fill='paleTurquoise', opacity=70)

diagonalStars = Group()
# Create an 8x8 grid of stars, equally spaced throughout the screen.
# The stars along the diagonal should be gold and increase in size by 3
# each time you move right and down along the canvas.
for row in range(8):
    for col in range(8):
        x = 50 * col + 20
        y = 50 * row + 20
        if (x == y):
            diagonalStars.add(
                Star(x, y, app.diagonalStarSize, 5,
                     fill=gradient('yellow', 'goldenrod'))
                )
            app.diagonalStarSize += 3
        else:
            Star(x, y, 5, 5, fill='white', roundness=20)
def onKeyPress(key):
    # When any key is pressed, unpause the app.
    app.paused = False

def onStep():
    # Move the diagonal stars 10 pixels towards the right-bottom of the canvas.
    newX, newY = getPointInDir(diagonalStars.centerX, diagonalStars.centerY,
                               135, 10)
    diagonalStars.centerX = newX
    diagonalStars.centerY = newY



# -
app.background = gradient('black', 'midnightBlue', start='left-top')
app.diagonalStarSize = 12
app.paused = True

# shooting star tail
Polygon (0, 0, 350, 400, 380, 400, fill='paleGreen', opacity=70)
Polygon (0, 0, 380, 400, 400, 400, 400, 380, fill='pink', opacity=70)
Polygon (0, 0, 400, 380, 400, 350, fill='paleTurquoise', opacity=70)

diagonalStars = Group()
# Create an 8x8 grid of stars, equally spaced throughout the screen.
# The stars along the diagonal should be gold and increase in size by 3
# each time you move right and down along the canvas.
for row in range(8):
    for col in range(8):
        x = 50 * col + 20
        y = 50 * row + 20
        if (x == y):
            diagonalStars.add(
                Star(x, y, app.diagonalStarSize, 5,
                     fill=gradient('yellow', 'goldenrod'))
                )
            app.diagonalStarSize += 3
        else:
            Star(x, y, 5, 5, fill='white', roundness=20)
def onKeyPress(key):
    # When any key is pressed, unpause the app.
    app.paused = False

def onStep():
    # Move the diagonal stars 10 pixels towards the right-bottom of the canvas.
    newX, newY = getPointInDir(diagonalStars.centerX, diagonalStars.centerY,
                               135, 10)
    diagonalStars.centerX = newX
    diagonalStars.centerY = newY

onKeyPress('space')
onSteps(30)
app.paused = True

