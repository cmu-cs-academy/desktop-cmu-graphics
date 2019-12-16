app.background = gradient('aliceBlue', 'lightBlue')

app.direction = None

boat = Group(
    Label('()', 200, 200, fill='red', size=150),
    Line(200, 160, 200, 280, fill='saddleBrown', lineWidth=30, dashes=(6, 20))
    )

paddle = Group(
    Line(100, 200, 300, 200, fill='gray', lineWidth=6),
    Rect(80, 190, 40, 20, fill='red'),
    Rect(280, 190, 40, 20, fill='red')
    )
boat.add(paddle)

ball = Circle(100, 100, 30, fill='coral')
ball.dx = 0
ball.dy = 10


def onKeyHold(keys):
    # Depending on what arrow key is held, moves the boat appropriately and
    # sets app.direction.
    if ('up' in keys):
        boat.rotateAngle = 0
        boat.centerY -= 5
        app.direction = 'up'
    elif ('down' in keys):
        boat.rotateAngle = 180
        boat.centerY += 5
        app.direction = 'down'
    elif ('left' in keys):
        boat.rotateAngle = -90
        boat.centerX -= 5
        app.direction = 'left'
    elif ('right' in keys):
        boat.rotateAngle = 90
        boat.centerX += 5
        app.direction = 'right'

    # Wrap the boat around in each direction if it goes off the canvas so that
    # it appears on the other side of the canvas.
    if (boat.bottom < 0):
        boat.top = 400
    elif (boat.top > 400):
        boat.bottom = 0
    elif (boat.left > 400):
        boat.right = 0
    elif (boat.right < 0):
        boat.left = 400
def onStep():
    # The ball bounces if it hits the boat.
    if (boat.hitsShape(ball) == True):
        if (app.direction == 'up'):
            ball.dy = -10
        elif (app.direction == 'down'):
            ball.dy = 10
        elif (app.direction == 'left'):
            ball.dx = -10
        elif (app.direction == 'right'):
            ball.dx = 10

    # The ball should bounce when it hits a wall.
    if ((ball.left < 0) or (ball.right > 400)):
        ball.dx *= -1

    # Also bounce the ball in the y direction if it goes out of bounds.
    if ((ball.top < 0) or (ball.bottom > 400)):
        ball.dy *= -1
    # Move the ball using ball.dx and dy.
    ball.centerX += ball.dx
    ball.centerY += ball.dy

onKeyHolds(['left'], 10)
onSteps(20)
app.paused = True


# -
app.background = gradient('aliceBlue', 'lightBlue')

app.direction = None

boat = Group(
    Label('()', 200, 200, fill='red', size=150),
    Line(200, 160, 200, 280, fill='saddleBrown', lineWidth=30, dashes=(6, 20))
    )

paddle = Group(
    Line(100, 200, 300, 200, fill='gray', lineWidth=6),
    Rect(80, 190, 40, 20, fill='red'),
    Rect(280, 190, 40, 20, fill='red')
    )
boat.add(paddle)

ball = Circle(100, 100, 30, fill='coral')
ball.dx = 0
ball.dy = 10


def onKeyHold(keys):
    # Depending on what arrow key is held, moves the boat appropriately and
    # sets app.direction.
    if ('up' in keys):
        boat.rotateAngle = 0
        boat.centerY -= 5
        app.direction = 'up'
    elif ('down' in keys):
        boat.rotateAngle = 180
        boat.centerY += 5
        app.direction = 'down'
    elif ('left' in keys):
        boat.rotateAngle = -90
        boat.centerX -= 5
        app.direction = 'left'
    elif ('right' in keys):
        boat.rotateAngle = 90
        boat.centerX += 5
        app.direction = 'right'

    # Wrap the boat around in each direction if it goes off the canvas so that
    # it appears on the other side of the canvas.
    if (boat.bottom < 0):
        boat.top = 400
    elif (boat.top > 400):
        boat.bottom = 0
    elif (boat.left > 400):
        boat.right = 0
    elif (boat.right < 0):
        boat.left = 400
def onStep():
    # The ball bounces if it hits the boat.
    if (boat.hitsShape(ball) == True):
        if (app.direction == 'up'):
            ball.dy = -10
        elif (app.direction == 'down'):
            ball.dy = 10
        elif (app.direction == 'left'):
            ball.dx = -10
        elif (app.direction == 'right'):
            ball.dx = 10

    # The ball should bounce when it hits a wall.
    if ((ball.left < 0) or (ball.right > 400)):
        ball.dx *= -1

    # Also bounce the ball in the y direction if it goes out of bounds.
    if ((ball.top < 0) or (ball.bottom > 400)):
        ball.dy *= -1
    # Move the ball using ball.dx and dy.
    ball.centerX += ball.dx
    ball.centerY += ball.dy



# -
app.background = gradient('aliceBlue', 'lightBlue')

app.direction = None

boat = Group(
    Label('()', 200, 200, fill='red', size=150),
    Line(200, 160, 200, 280, fill='saddleBrown', lineWidth=30, dashes=(6, 20))
    )

paddle = Group(
    Line(100, 200, 300, 200, fill='gray', lineWidth=6),
    Rect(80, 190, 40, 20, fill='red'),
    Rect(280, 190, 40, 20, fill='red')
    )
boat.add(paddle)

ball = Circle(100, 100, 30, fill='coral')
ball.dx = 0
ball.dy = 10


def onKeyHold(keys):
    # Depending on what arrow key is held, moves the boat appropriately and
    # sets app.direction.
    if ('up' in keys):
        boat.rotateAngle = 0
        boat.centerY -= 5
        app.direction = 'up'
    elif ('down' in keys):
        boat.rotateAngle = 180
        boat.centerY += 5
        app.direction = 'down'
    elif ('left' in keys):
        boat.rotateAngle = -90
        boat.centerX -= 5
        app.direction = 'left'
    elif ('right' in keys):
        boat.rotateAngle = 90
        boat.centerX += 5
        app.direction = 'right'

    # Wrap the boat around in each direction if it goes off the canvas so that
    # it appears on the other side of the canvas.
    if (boat.bottom < 0):
        boat.top = 400
    elif (boat.top > 400):
        boat.bottom = 0
    elif (boat.left > 400):
        boat.right = 0
    elif (boat.right < 0):
        boat.left = 400
def onStep():
    # The ball bounces if it hits the boat.
    if (boat.hitsShape(ball) == True):
        if (app.direction == 'up'):
            ball.dy = -10
        elif (app.direction == 'down'):
            ball.dy = 10
        elif (app.direction == 'left'):
            ball.dx = -10
        elif (app.direction == 'right'):
            ball.dx = 10

    # The ball should bounce when it hits a wall.
    if ((ball.left < 0) or (ball.right > 400)):
        ball.dx *= -1

    # Also bounce the ball in the y direction if it goes out of bounds.
    if ((ball.top < 0) or (ball.bottom > 400)):
        ball.dy *= -1
    # Move the ball using ball.dx and dy.
    ball.centerX += ball.dx
    ball.centerY += ball.dy


