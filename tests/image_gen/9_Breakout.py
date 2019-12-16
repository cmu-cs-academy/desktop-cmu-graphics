app.stepsPerSecond = 50
app.background = 'black'

blocks = Group()
blocks.blockCount = 0
blocks.rowColor = 'red'

paddle = Rect(160, 380, 80, 20, fill='lemonChiffon', border='black')
paddle.prevX = 160

ball = Circle(200, 370, 10, fill='lemonChiffon')
ball.dx = 3
ball.dy = -6

def setRowColor(row):
    if (row == 0):
        blocks.rowColor = 'steelBlue'
    elif (row == 1):
        blocks.rowColor = 'cornflowerBlue'
    elif (row == 2):
        blocks.rowColor = 'skyBlue'
    elif (row == 3):
        blocks.rowColor = 'lightBlue'
    else:
        blocks.rowColor = 'lightCyan'

def makeRow(row):
    # For the given row, add 5 blocks and increase the blockCount.
    for col in range(5):
        blocks.add(
            Rect(col * 80, row * 30, 80, 30, fill=blocks.rowColor,
                 border='black', borderWidth=3)
            )
        blocks.blockCount += 1
def makeBlocks():
    # For each row, set the row color and make the row.
    for row in range(5):
        setRowColor(row)
        makeRow(row)
makeBlocks()

def onMouseMove(mouseX, mouseY):
    # Moves the paddle.
    paddle.prevX = paddle.centerX
    paddle.centerX = mouseX

def onStep():
    ball.centerX += ball.dx
    ball.centerY += ball.dy

    # Checks if the ball has gone out of range and bounce it if it hits a wall.
    if ((ball.left <= 0) or (ball.right >= 400)):
        ball.dx = -ball.dx
    if (ball.top <= 0):
        ball.dy = 6
    elif (ball.bottom >= 400):
        Label('You Lose!', 200, 200, fill='white', size=50)
        app.paused = True

    # Checks if the paddle intersected the ball.
    if (paddle.hitsShape(ball) == True):
        ball.dy = -6

        # If player moved the paddle left to right, moves the ball right.
        if (paddle.centerX - paddle.prevX > 0):
            ball.dx = 6

        # If player moved the paddle right to left, moves the ball left.
        elif (paddle.centerX - paddle.prevX < 0):
            ball.dx = -6
        else:
            ball.dx = 0

    # Check if the ball has hit any blocks in the group blocks.
    # If it has, remove that block, reverse the direction of the ball,
    # and decrease the ball count.
    for block in blocks.children:
        if (block.hitsShape(ball) == True):
            blocks.remove(block)
            ball.dy *= -1
            blocks.blockCount -= 1
    # Checks if all of the blocks have been removed.
    if (blocks.blockCount == 0):
        Label('You Win!', 200, 200, fill='white', size=50)
        app.paused = True

onSteps(80)
app.paused = True


# -
app.stepsPerSecond = 50
app.background = 'black'

blocks = Group()
blocks.blockCount = 0
blocks.rowColor = 'red'

paddle = Rect(160, 380, 80, 20, fill='lemonChiffon', border='black')
paddle.prevX = 160

ball = Circle(200, 370, 10, fill='lemonChiffon')
ball.dx = 3
ball.dy = -6

def setRowColor(row):
    if (row == 0):
        blocks.rowColor = 'steelBlue'
    elif (row == 1):
        blocks.rowColor = 'cornflowerBlue'
    elif (row == 2):
        blocks.rowColor = 'skyBlue'
    elif (row == 3):
        blocks.rowColor = 'lightBlue'
    else:
        blocks.rowColor = 'lightCyan'

def makeRow(row):
    # For the given row, add 5 blocks and increase the blockCount.
    for col in range(5):
        blocks.add(
            Rect(col * 80, row * 30, 80, 30, fill=blocks.rowColor,
                 border='black', borderWidth=3)
            )
        blocks.blockCount += 1
def makeBlocks():
    # For each row, set the row color and make the row.
    for row in range(5):
        setRowColor(row)
        makeRow(row)
makeBlocks()

def onMouseMove(mouseX, mouseY):
    # Moves the paddle.
    paddle.prevX = paddle.centerX
    paddle.centerX = mouseX

def onStep():
    ball.centerX += ball.dx
    ball.centerY += ball.dy

    # Checks if the ball has gone out of range and bounce it if it hits a wall.
    if ((ball.left <= 0) or (ball.right >= 400)):
        ball.dx = -ball.dx
    if (ball.top <= 0):
        ball.dy = 6
    elif (ball.bottom >= 400):
        Label('You Lose!', 200, 200, fill='white', size=50)
        app.paused = True

    # Checks if the paddle intersected the ball.
    if (paddle.hitsShape(ball) == True):
        ball.dy = -6

        # If player moved the paddle left to right, moves the ball right.
        if (paddle.centerX - paddle.prevX > 0):
            ball.dx = 6

        # If player moved the paddle right to left, moves the ball left.
        elif (paddle.centerX - paddle.prevX < 0):
            ball.dx = -6
        else:
            ball.dx = 0

    # Check if the ball has hit any blocks in the group blocks.
    # If it has, remove that block, reverse the direction of the ball,
    # and decrease the ball count.
    for block in blocks.children:
        if (block.hitsShape(ball) == True):
            blocks.remove(block)
            ball.dy *= -1
            blocks.blockCount -= 1
    # Checks if all of the blocks have been removed.
    if (blocks.blockCount == 0):
        Label('You Win!', 200, 200, fill='white', size=50)
        app.paused = True

onSteps(50)
app.paused = True


# -
app.stepsPerSecond = 50
app.background = 'black'

blocks = Group()
blocks.blockCount = 0
blocks.rowColor = 'red'

paddle = Rect(160, 380, 80, 20, fill='lemonChiffon', border='black')
paddle.prevX = 160

ball = Circle(200, 370, 10, fill='lemonChiffon')
ball.dx = 3
ball.dy = -6

def setRowColor(row):
    if (row == 0):
        blocks.rowColor = 'steelBlue'
    elif (row == 1):
        blocks.rowColor = 'cornflowerBlue'
    elif (row == 2):
        blocks.rowColor = 'skyBlue'
    elif (row == 3):
        blocks.rowColor = 'lightBlue'
    else:
        blocks.rowColor = 'lightCyan'

def makeRow(row):
    # For the given row, add 5 blocks and increase the blockCount.
    for col in range(5):
        blocks.add(
            Rect(col * 80, row * 30, 80, 30, fill=blocks.rowColor,
                 border='black', borderWidth=3)
            )
        blocks.blockCount += 1
def makeBlocks():
    # For each row, set the row color and make the row.
    for row in range(5):
        setRowColor(row)
        makeRow(row)
makeBlocks()

def onMouseMove(mouseX, mouseY):
    # Moves the paddle.
    paddle.prevX = paddle.centerX
    paddle.centerX = mouseX

def onStep():
    ball.centerX += ball.dx
    ball.centerY += ball.dy

    # Checks if the ball has gone out of range and bounce it if it hits a wall.
    if ((ball.left <= 0) or (ball.right >= 400)):
        ball.dx = -ball.dx
    if (ball.top <= 0):
        ball.dy = 6
    elif (ball.bottom >= 400):
        Label('You Lose!', 200, 200, fill='white', size=50)
        app.paused = True

    # Checks if the paddle intersected the ball.
    if (paddle.hitsShape(ball) == True):
        ball.dy = -6

        # If player moved the paddle left to right, moves the ball right.
        if (paddle.centerX - paddle.prevX > 0):
            ball.dx = 6

        # If player moved the paddle right to left, moves the ball left.
        elif (paddle.centerX - paddle.prevX < 0):
            ball.dx = -6
        else:
            ball.dx = 0

    # Check if the ball has hit any blocks in the group blocks.
    # If it has, remove that block, reverse the direction of the ball,
    # and decrease the ball count.
    for block in blocks.children:
        if (block.hitsShape(ball) == True):
            blocks.remove(block)
            ball.dy *= -1
            blocks.blockCount -= 1
    # Checks if all of the blocks have been removed.
    if (blocks.blockCount == 0):
        Label('You Win!', 200, 200, fill='white', size=50)
        app.paused = True

onSteps(50)
app.paused = True

