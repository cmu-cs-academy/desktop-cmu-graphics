app.background = 'midnightBlue'

Label('Ball wrap around', 200, 20, fill='white', size=20, bold=True)
Label('Move the mouse to move the ball right by 10', 200, 45, fill='white')
Label('When the ball gets to the edge, it wraps around!', 200, 65, fill='white')

ball = Circle(20, 200, 20, fill='yellow')

def onMouseMove(mouseX, mouseY):
    # As long as the ball's center is left of the right edge of the canvas,
    # keep moving right by 10. Otherwise restart at the left edge.
    if (ball.centerX < 400):
        ball.centerX += 10
    else:
        ball.centerX = 0

onMouseMove(100, 100)
onMouseMove(100, 200)
onMouseMove(100, 300)
onMouseMove(100, 100)


# -
app.background = 'midnightBlue'

Label('Ball wrap around', 200, 20, fill='white', size=20, bold=True)
Label('Move the mouse to move the ball right by 10', 200, 45, fill='white')
Label('When the ball gets to the edge, it wraps around!', 200, 65, fill='white')

ball = Circle(20, 200, 20, fill='yellow')

def onMouseMove(mouseX, mouseY):
    # As long as the ball's center is left of the right edge of the canvas,
    # keep moving right by 10. Otherwise restart at the left edge.
    if (ball.centerX < 400):
        ball.centerX += 10
    else:
        ball.centerX = 0

ball.centerX = 380
onMouseMove(100, 100)
onMouseMove(100, 100)
onMouseMove(100, 100)
onMouseMove(100, 100)


# -
app.background = 'midnightBlue'

Label('Ball wrap around', 200, 20, fill='white', size=20, bold=True)
Label('Move the mouse to move the ball right by 10', 200, 45, fill='white')
Label('When the ball gets to the edge, it wraps around!', 200, 65, fill='white')

ball = Circle(20, 200, 20, fill='yellow')

def onMouseMove(mouseX, mouseY):
    # As long as the ball's center is left of the right edge of the canvas,
    # keep moving right by 10. Otherwise restart at the left edge.
    if (ball.centerX < 400):
        ball.centerX += 10
    else:
        ball.centerX = 0

onMouseMove(100, 100)

