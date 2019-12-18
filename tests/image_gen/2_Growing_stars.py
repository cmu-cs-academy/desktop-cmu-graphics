app.background = 'black'
app.stepsPerSecond = 30

app.counter = 0

stars = Group()
stars.nextFill = 'orange'

def onStep():
    app.counter += 1

    # Adds a star every 10 steps.
    if (app.counter == 10):
        # Resets the counter and change the fill color.
        app.counter = 0
        if (stars.nextFill == 'orange'):
            stars.nextFill = 'yellow'
        else:
            stars.nextFill = 'orange'

        # Adds a new star to the stars group.
        stars.add(
            Star(200, 200, 10, 5, fill=stars.nextFill)
            )

    # Increase each star's radius by 5 until it is larger than 700, at which
    # point remove the star from the group.
    for eachStar in stars.children:
        eachStar.radius += 5
        if (eachStar.radius > 700):
            stars.remove(eachStar)



# -
app.background = 'black'
app.stepsPerSecond = 30

app.counter = 0

stars = Group()
stars.nextFill = 'orange'

def onStep():
    app.counter += 1

    # Adds a star every 10 steps.
    if (app.counter == 10):
        # Resets the counter and change the fill color.
        app.counter = 0
        if (stars.nextFill == 'orange'):
            stars.nextFill = 'yellow'
        else:
            stars.nextFill = 'orange'

        # Adds a new star to the stars group.
        stars.add(
            Star(200, 200, 10, 5, fill=stars.nextFill)
            )

    # Increase each star's radius by 5 until it is larger than 700, at which
    # point remove the star from the group.
    for eachStar in stars.children:
        eachStar.radius += 5
        if (eachStar.radius > 700):
            stars.remove(eachStar)

onSteps(5)
app.paused = True


# -
app.background = 'black'
app.stepsPerSecond = 30

app.counter = 0

stars = Group()
stars.nextFill = 'orange'

def onStep():
    app.counter += 1

    # Adds a star every 10 steps.
    if (app.counter == 10):
        # Resets the counter and change the fill color.
        app.counter = 0
        if (stars.nextFill == 'orange'):
            stars.nextFill = 'yellow'
        else:
            stars.nextFill = 'orange'

        # Adds a new star to the stars group.
        stars.add(
            Star(200, 200, 10, 5, fill=stars.nextFill)
            )

    # Increase each star's radius by 5 until it is larger than 700, at which
    # point remove the star from the group.
    for eachStar in stars.children:
        eachStar.radius += 5
        if (eachStar.radius > 700):
            stars.remove(eachStar)

onSteps(100)
app.paused = True

