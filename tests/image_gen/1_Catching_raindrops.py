app.background = 'midnightBlue'
app.step = 0

umbrella = Group(
    Label('J', 195, 210, fill='sienna', size=50),
    Arc(200, 200, 120, 110, -90, 180,
        fill=gradient('gold', 'yellow', 'gold', start='left')),
    Line(200, 145, 200, 140, fill='sienna', lineWidth=3)
    )
glow = Circle(200, 180, 80, fill=gradient('white', 'midnightBlue'), opacity=30)

raindrops = Group()
dropletsCaught = Label(0, 200, 30, fill='white', size=40)

def onMouseMove(mouseX, mouseY):
    # If the umbrella doesn't contain mouseX, mouseY, we want to move
    # the umbrella 5 pixels in the direction of the mouse.
    if (umbrella.contains(mouseX, mouseY) == False):
        angle = angleTo(umbrella.centerX, umbrella.centerY, mouseX, mouseY)
        newX, newY = getPointInDir(umbrella.centerX, umbrella.centerY, angle, 5)
        umbrella.centerX = newX
        umbrella.centerY = newY
        glow.centerX = umbrella.centerX
        glow.centerY = umbrella.centerY
def onStep():
    app.step += 1
    # Every 10 steps, creates a new drop.
    if (app.step % 10 == 0):
        x = randrange(0, 400)
        drop = Circle(x, 0, 5, fill=gradient('white', 'steelBlue'), opacity=50)
        drop.fallSpeed = randrange(1, 10)
        raindrops.add(drop)

    # Move each raindrop down, based on its fallSpeed value.
    for drop in raindrops.children:
        drop.centerY += drop.fallSpeed
        # Then check if the raindrop hit the umbrella, or the bottom of
        # the canvas, and update the dropletsCaught value as needed.
        if (umbrella.hitsShape(drop) == True):
            dropletsCaught.value += 1
            raindrops.remove(drop)
        elif (drop.centerY >= 400):
            raindrops.remove(drop)
    # The game ends once 10 raindrops are caught.
    if (dropletsCaught.value >= 10):
        Rect(50, 150, 300, 100, fill='white', border='steelBlue', opacity=50)
        Label('You finished in ' + str(app.step) + ' steps', 200, 200, size=25)
        app.stop()

onSteps(200)
onMouseMove(0, 0)
onMouseMove(400, 200)
onMouseMove(200, 400)
onSteps(100)
app.paused = True


# -
app.background = 'midnightBlue'
app.step = 0

umbrella = Group(
    Label('J', 195, 210, fill='sienna', size=50),
    Arc(200, 200, 120, 110, -90, 180,
        fill=gradient('gold', 'yellow', 'gold', start='left')),
    Line(200, 145, 200, 140, fill='sienna', lineWidth=3)
    )
glow = Circle(200, 180, 80, fill=gradient('white', 'midnightBlue'), opacity=30)

raindrops = Group()
dropletsCaught = Label(0, 200, 30, fill='white', size=40)

def onMouseMove(mouseX, mouseY):
    # If the umbrella doesn't contain mouseX, mouseY, we want to move
    # the umbrella 5 pixels in the direction of the mouse.
    if (umbrella.contains(mouseX, mouseY) == False):
        angle = angleTo(umbrella.centerX, umbrella.centerY, mouseX, mouseY)
        newX, newY = getPointInDir(umbrella.centerX, umbrella.centerY, angle, 5)
        umbrella.centerX = newX
        umbrella.centerY = newY
        glow.centerX = umbrella.centerX
        glow.centerY = umbrella.centerY
def onStep():
    app.step += 1
    # Every 10 steps, creates a new drop.
    if (app.step % 10 == 0):
        x = randrange(0, 400)
        drop = Circle(x, 0, 5, fill=gradient('white', 'steelBlue'), opacity=50)
        drop.fallSpeed = randrange(1, 10)
        raindrops.add(drop)

    # Move each raindrop down, based on its fallSpeed value.
    for drop in raindrops.children:
        drop.centerY += drop.fallSpeed
        # Then check if the raindrop hit the umbrella, or the bottom of
        # the canvas, and update the dropletsCaught value as needed.
        if (umbrella.hitsShape(drop) == True):
            dropletsCaught.value += 1
            raindrops.remove(drop)
        elif (drop.centerY >= 400):
            raindrops.remove(drop)
    # The game ends once 10 raindrops are caught.
    if (dropletsCaught.value >= 10):
        Rect(50, 150, 300, 100, fill='white', border='steelBlue', opacity=50)
        Label('You finished in ' + str(app.step) + ' steps', 200, 200, size=25)
        app.stop()

onSteps(10)
app.paused = True


# -
app.background = 'midnightBlue'
app.step = 0

umbrella = Group(
    Label('J', 195, 210, fill='sienna', size=50),
    Arc(200, 200, 120, 110, -90, 180,
        fill=gradient('gold', 'yellow', 'gold', start='left')),
    Line(200, 145, 200, 140, fill='sienna', lineWidth=3)
    )
glow = Circle(200, 180, 80, fill=gradient('white', 'midnightBlue'), opacity=30)

raindrops = Group()
dropletsCaught = Label(0, 200, 30, fill='white', size=40)

def onMouseMove(mouseX, mouseY):
    # If the umbrella doesn't contain mouseX, mouseY, we want to move
    # the umbrella 5 pixels in the direction of the mouse.
    if (umbrella.contains(mouseX, mouseY) == False):
        angle = angleTo(umbrella.centerX, umbrella.centerY, mouseX, mouseY)
        newX, newY = getPointInDir(umbrella.centerX, umbrella.centerY, angle, 5)
        umbrella.centerX = newX
        umbrella.centerY = newY
        glow.centerX = umbrella.centerX
        glow.centerY = umbrella.centerY
def onStep():
    app.step += 1
    # Every 10 steps, creates a new drop.
    if (app.step % 10 == 0):
        x = randrange(0, 400)
        drop = Circle(x, 0, 5, fill=gradient('white', 'steelBlue'), opacity=50)
        drop.fallSpeed = randrange(1, 10)
        raindrops.add(drop)

    # Move each raindrop down, based on its fallSpeed value.
    for drop in raindrops.children:
        drop.centerY += drop.fallSpeed
        # Then check if the raindrop hit the umbrella, or the bottom of
        # the canvas, and update the dropletsCaught value as needed.
        if (umbrella.hitsShape(drop) == True):
            dropletsCaught.value += 1
            raindrops.remove(drop)
        elif (drop.centerY >= 400):
            raindrops.remove(drop)
    # The game ends once 10 raindrops are caught.
    if (dropletsCaught.value >= 10):
        Rect(50, 150, 300, 100, fill='white', border='steelBlue', opacity=50)
        Label('You finished in ' + str(app.step) + ' steps', 200, 200, size=25)
        app.stop()

onMouseMove(200, 50)
onMouseMove(200, 50)
app.paused = True

