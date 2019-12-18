app.background = 'lightCyan'
app.stepsPerSecond = 20
app.steps = 0

ripples = Group()

def onStep():
    # Create a ripple with random x and y center, and add it to ripples group.
    randX = randrange(0, 400)
    randY = randrange(0, 400)
    ripples.add(
        Circle(randX, randY, 5, fill=None, border='lightBlue', borderWidth=20)
        )
    # Goes through each ripple and makes the border decrease and the ripple expand.
    for ripple in ripples.children:
        ripple.borderWidth -= 2
        ripple.radius += 5

        # If the ripple fades out, remove it.
        if (ripple.borderWidth <= 0):
            ripples.remove(ripple)

onSteps(10)
app.paused = True


# -
app.background = 'lightCyan'
app.stepsPerSecond = 20
app.steps = 0

ripples = Group()

def onStep():
    # Create a ripple with random x and y center, and add it to ripples group.
    randX = randrange(0, 400)
    randY = randrange(0, 400)
    ripples.add(
        Circle(randX, randY, 5, fill=None, border='lightBlue', borderWidth=20)
        )
    # Goes through each ripple and makes the border decrease and the ripple expand.
    for ripple in ripples.children:
        ripple.borderWidth -= 2
        ripple.radius += 5

        # If the ripple fades out, remove it.
        if (ripple.borderWidth <= 0):
            ripples.remove(ripple)

onSteps(50)
app.paused = True


# -
app.background = 'lightCyan'
app.stepsPerSecond = 20
app.steps = 0

ripples = Group()

def onStep():
    # Create a ripple with random x and y center, and add it to ripples group.
    randX = randrange(0, 400)
    randY = randrange(0, 400)
    ripples.add(
        Circle(randX, randY, 5, fill=None, border='lightBlue', borderWidth=20)
        )
    # Goes through each ripple and makes the border decrease and the ripple expand.
    for ripple in ripples.children:
        ripple.borderWidth -= 2
        ripple.radius += 5

        # If the ripple fades out, remove it.
        if (ripple.borderWidth <= 0):
            ripples.remove(ripple)

onSteps(50)
app.paused = True

