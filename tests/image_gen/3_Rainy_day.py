app.background = 'darkGrey'
app.stepsPerSecond = 10

# cloud
Circle(210, 20, 50, fill='white', border='gainsboro', borderWidth=3)
Circle(130, 65, 70, fill='white', border='gainsboro', borderWidth=3)
Circle(280, 65, 60, fill='white', border='gainsboro', borderWidth=3)
Circle(200, 95, 80, fill='white', border='gainsboro')
Rect(165, 5, 20, 11, fill='white')
Rect(235, 10, 20, 13, fill='white')
Rect(115, 35, 155, 95, fill='white')

rain = Group()

def onStep():
    # Adds new raindrops.
    rain.add(
        Circle(200, 200, 7, fill=gradient('white', 'lightBlue')),
        Circle(115, 140, 7, fill=gradient('white', 'lightBlue')),
        Circle(280, 140, 7, fill=gradient('white', 'lightBlue'))
        )

    # Move the rain group down by 40. If the centerY of the rain gets
    # below 400, clear the group.
    rain.centerY += 40
    if (rain.centerY > 400):
        rain.clear()



# -
app.background = 'darkGrey'
app.stepsPerSecond = 10

# cloud
Circle(210, 20, 50, fill='white', border='gainsboro', borderWidth=3)
Circle(130, 65, 70, fill='white', border='gainsboro', borderWidth=3)
Circle(280, 65, 60, fill='white', border='gainsboro', borderWidth=3)
Circle(200, 95, 80, fill='white', border='gainsboro')
Rect(165, 5, 20, 11, fill='white')
Rect(235, 10, 20, 13, fill='white')
Rect(115, 35, 155, 95, fill='white')

rain = Group()

def onStep():
    # Adds new raindrops.
    rain.add(
        Circle(200, 200, 7, fill=gradient('white', 'lightBlue')),
        Circle(115, 140, 7, fill=gradient('white', 'lightBlue')),
        Circle(280, 140, 7, fill=gradient('white', 'lightBlue'))
        )

    # Move the rain group down by 40. If the centerY of the rain gets
    # below 400, clear the group.
    rain.centerY += 40
    if (rain.centerY > 400):
        rain.clear()

onSteps(140)
app.paused = True


# -
app.background = 'darkGrey'
app.stepsPerSecond = 10

# cloud
Circle(210, 20, 50, fill='white', border='gainsboro', borderWidth=3)
Circle(130, 65, 70, fill='white', border='gainsboro', borderWidth=3)
Circle(280, 65, 60, fill='white', border='gainsboro', borderWidth=3)
Circle(200, 95, 80, fill='white', border='gainsboro')
Rect(165, 5, 20, 11, fill='white')
Rect(235, 10, 20, 13, fill='white')
Rect(115, 35, 155, 95, fill='white')

rain = Group()

def onStep():
    # Adds new raindrops.
    rain.add(
        Circle(200, 200, 7, fill=gradient('white', 'lightBlue')),
        Circle(115, 140, 7, fill=gradient('white', 'lightBlue')),
        Circle(280, 140, 7, fill=gradient('white', 'lightBlue'))
        )

    # Move the rain group down by 40. If the centerY of the rain gets
    # below 400, clear the group.
    rain.centerY += 40
    if (rain.centerY > 400):
        rain.clear()


