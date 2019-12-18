app.background = gradient('lightCyan', 'skyBlue', start='bottom')
snowflakes = Group()

def onMouseMove(mouseX, mouseY):
    # Check if the mouse is on a snowflake.
    snowflake = snowflakes.hitTest(mouseX, mouseY)
    if (snowflake != None):
        # If the mouse is on a snowflake, rotate the flake and increase
        # its opacity.
        snowflake.rotateAngle += 10
        if (snowflake.opacity <= 90):
            snowflake.opacity += 10
def onStep():
    # Makes at most 70 snowflakes.
    if (len(snowflakes.children) < 70):
        # Creates a new flake with a random position, dx, and dy.
        snowflake = Label('*', randrange(0, 400), 0, fill='white', size=70,
                          opacity=30, bold=True)
        snowflake.dx = randrange(-1, 2)
        snowflake.dy = randrange(5, 8)
        snowflakes.add(snowflake)

    # Moves all the snowflakes and removes the ones that are off the canvas.
    for snowflake in snowflakes.children:
        snowflake.centerX += snowflake.dx
        snowflake.centerY += snowflake.dy
        if ((snowflake.right < 0) or (snowflake.top > 400) or
            (snowflake.left > 400)):
            snowflakes.remove(snowflake)

onSteps(10)
flake = snowflakes.children[0]
onMouseMove(flake.centerX, flake.centerY)
onMouseMove(flake.centerX, flake.centerY)
onMouseMove(flake.centerX, flake.centerY)
onMouseMove(flake.centerX, flake.centerY)
onMouseMove(flake.centerX, flake.centerY)
onMouseMove(flake.centerX, flake.centerY)
onMouseMove(flake.centerX, flake.centerY)
onMouseMove(flake.centerX, flake.centerY)
onMouseMove(flake.centerX, flake.centerY)
onSteps(5)
app.paused = True


# -
app.background = gradient('lightCyan', 'skyBlue', start='bottom')
snowflakes = Group()

def onMouseMove(mouseX, mouseY):
    # Check if the mouse is on a snowflake.
    snowflake = snowflakes.hitTest(mouseX, mouseY)
    if (snowflake != None):
        # If the mouse is on a snowflake, rotate the flake and increase
        # its opacity.
        snowflake.rotateAngle += 10
        if (snowflake.opacity <= 90):
            snowflake.opacity += 10
def onStep():
    # Makes at most 70 snowflakes.
    if (len(snowflakes.children) < 70):
        # Creates a new flake with a random position, dx, and dy.
        snowflake = Label('*', randrange(0, 400), 0, fill='white', size=70,
                          opacity=30, bold=True)
        snowflake.dx = randrange(-1, 2)
        snowflake.dy = randrange(5, 8)
        snowflakes.add(snowflake)

    # Moves all the snowflakes and removes the ones that are off the canvas.
    for snowflake in snowflakes.children:
        snowflake.centerX += snowflake.dx
        snowflake.centerY += snowflake.dy
        if ((snowflake.right < 0) or (snowflake.top > 400) or
            (snowflake.left > 400)):
            snowflakes.remove(snowflake)



# -
app.background = gradient('lightCyan', 'skyBlue', start='bottom')
snowflakes = Group()

def onMouseMove(mouseX, mouseY):
    # Check if the mouse is on a snowflake.
    snowflake = snowflakes.hitTest(mouseX, mouseY)
    if (snowflake != None):
        # If the mouse is on a snowflake, rotate the flake and increase
        # its opacity.
        snowflake.rotateAngle += 10
        if (snowflake.opacity <= 90):
            snowflake.opacity += 10
def onStep():
    # Makes at most 70 snowflakes.
    if (len(snowflakes.children) < 70):
        # Creates a new flake with a random position, dx, and dy.
        snowflake = Label('*', randrange(0, 400), 0, fill='white', size=70,
                          opacity=30, bold=True)
        snowflake.dx = randrange(-1, 2)
        snowflake.dy = randrange(5, 8)
        snowflakes.add(snowflake)

    # Moves all the snowflakes and removes the ones that are off the canvas.
    for snowflake in snowflakes.children:
        snowflake.centerX += snowflake.dx
        snowflake.centerY += snowflake.dy
        if ((snowflake.right < 0) or (snowflake.top > 400) or
            (snowflake.left > 400)):
            snowflakes.remove(snowflake)

onSteps(10)
flake = snowflakes.children[0]
onMouseMove(flake.centerX, flake.centerY)
onMouseMove(flake.centerX, flake.centerY)
onMouseMove(flake.centerX, flake.centerY)
onMouseMove(flake.centerX, flake.centerY)
onMouseMove(flake.centerX, flake.centerY)
onMouseMove(flake.centerX, flake.centerY)
onMouseMove(flake.centerX, flake.centerY)
onMouseMove(flake.centerX, flake.centerY)
onMouseMove(flake.centerX, flake.centerY)
onSteps(5)
app.paused = True

