app.background = 'black'

arcs = Group()

def onMouseMove(mouseX, mouseY):
    randomSweepAngle = randrange(1, 360)
    color = rgb(randrange(100, 256), 0, randrange(100, 256))

    # Create an arc centered at the mouse position using the variables above,
    # and a width of 10, a height of 20, and a startAngle of 0.
    arc = Arc(mouseX, mouseY, 10, 20, 0, randomSweepAngle, fill=color)
    arc.dx = randrange(-5, 5)
    arc.dy = randrange(2, 15)
    arcs.add(arc)

def onStep():
    for arc in arcs.children:
        # Update the centerX, centerY, by using the custom properties defined
        # in onMouseMove for each arc. Then rotate the arc by 5 degrees.
        arc.centerX += arc.dx
        arc.centerY += arc.dy
        arc.rotateAngle += 5
        # Remove any arcs that leave the canvas.
        if ((arc.right < 0) or (arc.top > 400) or (arc.left > 400)):
            arcs.remove(arc)

onMouseMove(100, 100)
onMouseMove(300, 150)
onSteps(20)
app.paused = True


# -
app.background = 'black'

arcs = Group()

def onMouseMove(mouseX, mouseY):
    randomSweepAngle = randrange(1, 360)
    color = rgb(randrange(100, 256), 0, randrange(100, 256))

    # Create an arc centered at the mouse position using the variables above,
    # and a width of 10, a height of 20, and a startAngle of 0.
    arc = Arc(mouseX, mouseY, 10, 20, 0, randomSweepAngle, fill=color)
    arc.dx = randrange(-5, 5)
    arc.dy = randrange(2, 15)
    arcs.add(arc)

def onStep():
    for arc in arcs.children:
        # Update the centerX, centerY, by using the custom properties defined
        # in onMouseMove for each arc. Then rotate the arc by 5 degrees.
        arc.centerX += arc.dx
        arc.centerY += arc.dy
        arc.rotateAngle += 5
        # Remove any arcs that leave the canvas.
        if ((arc.right < 0) or (arc.top > 400) or (arc.left > 400)):
            arcs.remove(arc)

onMouseMove(200, 100)
app.paused = True


# -
app.background = 'black'

arcs = Group()

def onMouseMove(mouseX, mouseY):
    randomSweepAngle = randrange(1, 360)
    color = rgb(randrange(100, 256), 0, randrange(100, 256))

    # Create an arc centered at the mouse position using the variables above,
    # and a width of 10, a height of 20, and a startAngle of 0.
    arc = Arc(mouseX, mouseY, 10, 20, 0, randomSweepAngle, fill=color)
    arc.dx = randrange(-5, 5)
    arc.dy = randrange(2, 15)
    arcs.add(arc)

def onStep():
    for arc in arcs.children:
        # Update the centerX, centerY, by using the custom properties defined
        # in onMouseMove for each arc. Then rotate the arc by 5 degrees.
        arc.centerX += arc.dx
        arc.centerY += arc.dy
        arc.rotateAngle += 5
        # Remove any arcs that leave the canvas.
        if ((arc.right < 0) or (arc.top > 400) or (arc.left > 400)):
            arcs.remove(arc)

onMouseMove(200, 100)
onSteps(20)
app.paused = True

