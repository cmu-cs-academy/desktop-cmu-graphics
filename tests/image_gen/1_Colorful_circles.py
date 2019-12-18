app.background = 'darkBlue'
app.stepsPerSecond = 3

circles = Group()

def onStep():
    colors = [ 'lightCoral', 'deepSkyBlue', 'mediumPurple',
               'lavender', 'crimson' ]

    # Loop through the colors and add a circle for each color.
    for color in colors:
        # Each circle should have a random x and y coordinate between 0 and
        # 400 and a random radius between 5 and 20. (not including 400 and 20.)
        centerX = randrange(0, 400)
        centerY = randrange(0, 400)
        radius = randrange(5, 20)
        circles.add(
            Circle(centerX, centerY, radius, fill=color, border='black',
                   borderWidth=3)
            )
    # Increases the size of all the circles until they get to 50, then
    # removes them.
    for circle in circles.children:
        circle.radius += 5
        if (circle.radius > 50):
            circles.remove(circle)



# -
app.background = 'darkBlue'
app.stepsPerSecond = 3

circles = Group()

def onStep():
    colors = [ 'lightCoral', 'deepSkyBlue', 'mediumPurple',
               'lavender', 'crimson' ]

    # Loop through the colors and add a circle for each color.
    for color in colors:
        # Each circle should have a random x and y coordinate between 0 and
        # 400 and a random radius between 5 and 20. (not including 400 and 20.)
        centerX = randrange(0, 400)
        centerY = randrange(0, 400)
        radius = randrange(5, 20)
        circles.add(
            Circle(centerX, centerY, radius, fill=color, border='black',
                   borderWidth=3)
            )
    # Increases the size of all the circles until they get to 50, then
    # removes them.
    for circle in circles.children:
        circle.radius += 5
        if (circle.radius > 50):
            circles.remove(circle)

onStep()
app.paused = True


# -
app.background = 'darkBlue'
app.stepsPerSecond = 3

circles = Group()

def onStep():
    colors = [ 'lightCoral', 'deepSkyBlue', 'mediumPurple',
               'lavender', 'crimson' ]

    # Loop through the colors and add a circle for each color.
    for color in colors:
        # Each circle should have a random x and y coordinate between 0 and
        # 400 and a random radius between 5 and 20. (not including 400 and 20.)
        centerX = randrange(0, 400)
        centerY = randrange(0, 400)
        radius = randrange(5, 20)
        circles.add(
            Circle(centerX, centerY, radius, fill=color, border='black',
                   borderWidth=3)
            )
    # Increases the size of all the circles until they get to 50, then
    # removes them.
    for circle in circles.children:
        circle.radius += 5
        if (circle.radius > 50):
            circles.remove(circle)


