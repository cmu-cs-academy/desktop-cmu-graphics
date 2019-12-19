app.background = gradient('midnightBlue', 'navy', 'black', start='bottom')

# background stars
Star(20, 50, 5, 8, fill='gold', roundness=40)
Star(280, 30, 5, 5, fill='gold')
Star(170, 300, 5, 8, fill='white', roundness=40)
Star(340, 150, 5, 5, fill='gold')
Star(50, 350, 5, 8, fill='white', roundness=40)
Star(250, 220, 5, 5, fill='white')
Star(380, 380, 5, 5, fill='white')
Star(75, 100, 5, 8, fill='gold', roundness=40)
Star(80, 210, 5, 8, fill='white', roundness=40)
Star(175, 80, 5, 8, fill='gold', roundness=40)

star = Star(20, 20, 10, 8, fill=gradient('gold', 'navy'), roundness=40, opacity=70)

def onMousePress(mouseX, mouseY):
    # Draws a copy of the star at the mouse position.
    Star(mouseX, mouseY, 10, star.points, fill=star.fill, roundness=40)

def onMouseMove(mouseX, mouseY):
    # Moves the star according to the mouse position.
    star.centerX = mouseX
    star.centerY = mouseY

    # If the mouse is in the top half of the canvas, the fill should be a
    # gradient starting at gold. Otherwise the gradient should start at white.
    if (mouseY < 200):
        star.fill = gradient('gold', 'navy')
    else:
        star.fill = gradient('white', 'navy')
    # If the mouse is on the left half of the canvas, the star should have
    # 8 points. Otherwise there should be 5 points.
    if (mouseX < 200):
        star.points = 8
    else:
        star.points = 5

onMouseMove(230, 160)
onMouseMove(50, 330)
onMouseMove(155, 380)
onMouseMove(320, 250)


# -
app.background = gradient('midnightBlue', 'navy', 'black', start='bottom')

# background stars
Star(20, 50, 5, 8, fill='gold', roundness=40)
Star(280, 30, 5, 5, fill='gold')
Star(170, 300, 5, 8, fill='white', roundness=40)
Star(340, 150, 5, 5, fill='gold')
Star(50, 350, 5, 8, fill='white', roundness=40)
Star(250, 220, 5, 5, fill='white')
Star(380, 380, 5, 5, fill='white')
Star(75, 100, 5, 8, fill='gold', roundness=40)
Star(80, 210, 5, 8, fill='white', roundness=40)
Star(175, 80, 5, 8, fill='gold', roundness=40)

star = Star(20, 20, 10, 8, fill=gradient('gold', 'navy'), roundness=40, opacity=70)

def onMousePress(mouseX, mouseY):
    # Draws a copy of the star at the mouse position.
    Star(mouseX, mouseY, 10, star.points, fill=star.fill, roundness=40)

def onMouseMove(mouseX, mouseY):
    # Moves the star according to the mouse position.
    star.centerX = mouseX
    star.centerY = mouseY

    # If the mouse is in the top half of the canvas, the fill should be a
    # gradient starting at gold. Otherwise the gradient should start at white.
    if (mouseY < 200):
        star.fill = gradient('gold', 'navy')
    else:
        star.fill = gradient('white', 'navy')
    # If the mouse is on the left half of the canvas, the star should have
    # 8 points. Otherwise there should be 5 points.
    if (mouseX < 200):
        star.points = 8
    else:
        star.points = 5

onMousePress(50, 50)
onMousePress(300, 300)
onMousePress(250, 150)
onMousePress(150, 250)


# -
app.background = gradient('midnightBlue', 'navy', 'black', start='bottom')

# background stars
Star(20, 50, 5, 8, fill='gold', roundness=40)
Star(280, 30, 5, 5, fill='gold')
Star(170, 300, 5, 8, fill='white', roundness=40)
Star(340, 150, 5, 5, fill='gold')
Star(50, 350, 5, 8, fill='white', roundness=40)
Star(250, 220, 5, 5, fill='white')
Star(380, 380, 5, 5, fill='white')
Star(75, 100, 5, 8, fill='gold', roundness=40)
Star(80, 210, 5, 8, fill='white', roundness=40)
Star(175, 80, 5, 8, fill='gold', roundness=40)

star = Star(20, 20, 10, 8, fill=gradient('gold', 'navy'), roundness=40, opacity=70)

def onMousePress(mouseX, mouseY):
    # Draws a copy of the star at the mouse position.
    Star(mouseX, mouseY, 10, star.points, fill=star.fill, roundness=40)

def onMouseMove(mouseX, mouseY):
    # Moves the star according to the mouse position.
    star.centerX = mouseX
    star.centerY = mouseY

    # If the mouse is in the top half of the canvas, the fill should be a
    # gradient starting at gold. Otherwise the gradient should start at white.
    if (mouseY < 200):
        star.fill = gradient('gold', 'navy')
    else:
        star.fill = gradient('white', 'navy')
    # If the mouse is on the left half of the canvas, the star should have
    # 8 points. Otherwise there should be 5 points.
    if (mouseX < 200):
        star.points = 8
    else:
        star.points = 5

onMouseMove(50, 300)

