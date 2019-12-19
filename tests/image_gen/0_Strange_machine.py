app.stepsPerSecond = 5
app.nextRadius = 0

Rect(0, 0, 400, 400)

def onStep():
    if (app.nextRadius < 200):
        # Increases the radius by 5.
        app.nextRadius += 5

        # Define these variables to generate new random values for the next
        # circle. Borders are less than 50 and dash values are less than 100.
        redGreen = randrange(0, 256)
        newBorderWidth = randrange(0, 50)
        dashWidth = randrange(0, 100)
        dashSpace = randrange(0, 100)
        # Draws the next circle with the values generated above.
        Circle(200, 200, app.nextRadius, fill=None,
               border=rgb(redGreen, 255 - redGreen, 255),
               borderWidth=newBorderWidth, dashes=(dashWidth, dashSpace))

onSteps(20)
app.paused = True


# -
app.stepsPerSecond = 5
app.nextRadius = 0

Rect(0, 0, 400, 400)

def onStep():
    if (app.nextRadius < 200):
        # Increases the radius by 5.
        app.nextRadius += 5

        # Define these variables to generate new random values for the next
        # circle. Borders are less than 50 and dash values are less than 100.
        redGreen = randrange(0, 256)
        newBorderWidth = randrange(0, 50)
        dashWidth = randrange(0, 100)
        dashSpace = randrange(0, 100)
        # Draws the next circle with the values generated above.
        Circle(200, 200, app.nextRadius, fill=None,
               border=rgb(redGreen, 255 - redGreen, 255),
               borderWidth=newBorderWidth, dashes=(dashWidth, dashSpace))

onSteps(50)
app.paused = True


# -
app.stepsPerSecond = 5
app.nextRadius = 0

Rect(0, 0, 400, 400)

def onStep():
    if (app.nextRadius < 200):
        # Increases the radius by 5.
        app.nextRadius += 5

        # Define these variables to generate new random values for the next
        # circle. Borders are less than 50 and dash values are less than 100.
        redGreen = randrange(0, 256)
        newBorderWidth = randrange(0, 50)
        dashWidth = randrange(0, 100)
        dashSpace = randrange(0, 100)
        # Draws the next circle with the values generated above.
        Circle(200, 200, app.nextRadius, fill=None,
               border=rgb(redGreen, 255 - redGreen, 255),
               borderWidth=newBorderWidth, dashes=(dashWidth, dashSpace))


