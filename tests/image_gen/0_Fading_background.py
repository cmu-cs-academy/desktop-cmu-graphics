app.stepsPerSecond = 50
app.steps = 0
app.innerBlueIncreasing = True

background = Rect(0, 0, 400, 400)

def onStep():
    # Increases steps up to 250.
    if ((app.steps <= 250) and (app.innerBlueIncreasing == True)):
        app.steps += 1

    # Then decreases steps to 0. Then increases again, and repeats.
    elif (app.steps >= 0):
        app.steps -= 1

        # Keeps track of if we are increasing or decreasing steps.
        app.innerBlueIncreasing = False
        if (app.steps == 0):
            app.innerBlueIncreasing = True

    # Set the following variables using app.steps to indicate the amount of blue
    # and green in the background.
    innerBlue = app.steps
    outerGreen = 255 - app.steps
    # Use the local variables to define the proper colors below.
    innerColor = rgb(255, 0, innerBlue)
    outerColor = rgb(0, outerGreen, 255)
    # Finally, set the background to a gradient using the inner and outer color
    # local variables.
    background.fill = gradient(innerColor, outerColor)

onSteps(30)
app.paused = True


# -
app.stepsPerSecond = 50
app.steps = 0
app.innerBlueIncreasing = True

background = Rect(0, 0, 400, 400)

def onStep():
    # Increases steps up to 250.
    if ((app.steps <= 250) and (app.innerBlueIncreasing == True)):
        app.steps += 1

    # Then decreases steps to 0. Then increases again, and repeats.
    elif (app.steps >= 0):
        app.steps -= 1

        # Keeps track of if we are increasing or decreasing steps.
        app.innerBlueIncreasing = False
        if (app.steps == 0):
            app.innerBlueIncreasing = True

    # Set the following variables using app.steps to indicate the amount of blue
    # and green in the background.
    innerBlue = app.steps
    outerGreen = 255 - app.steps
    # Use the local variables to define the proper colors below.
    innerColor = rgb(255, 0, innerBlue)
    outerColor = rgb(0, outerGreen, 255)
    # Finally, set the background to a gradient using the inner and outer color
    # local variables.
    background.fill = gradient(innerColor, outerColor)

onSteps(150)
app.paused = True


# -
app.stepsPerSecond = 50
app.steps = 0
app.innerBlueIncreasing = True

background = Rect(0, 0, 400, 400)

def onStep():
    # Increases steps up to 250.
    if ((app.steps <= 250) and (app.innerBlueIncreasing == True)):
        app.steps += 1

    # Then decreases steps to 0. Then increases again, and repeats.
    elif (app.steps >= 0):
        app.steps -= 1

        # Keeps track of if we are increasing or decreasing steps.
        app.innerBlueIncreasing = False
        if (app.steps == 0):
            app.innerBlueIncreasing = True

    # Set the following variables using app.steps to indicate the amount of blue
    # and green in the background.
    innerBlue = app.steps
    outerGreen = 255 - app.steps
    # Use the local variables to define the proper colors below.
    innerColor = rgb(255, 0, innerBlue)
    outerColor = rgb(0, outerGreen, 255)
    # Finally, set the background to a gradient using the inner and outer color
    # local variables.
    background.fill = gradient(innerColor, outerColor)

onSteps(150)
app.paused = True

