app.background = gradient('mediumPurple', 'black')
app.stepsPerSecond = 3
app.index = 0

# crystal ball
glass = Circle(200, 175, 125, fill='lightBlue')
crystalBall = Group(
    Polygon(120 ,315, 280, 315, 300, 350, 100, 350, fill='darkGoldenrod'),
    Oval(200, 350, 200, 50, fill='darkGoldenrod'),
    Oval(200, 315, 160, 40, fill='goldenrod'),
    glass,
    Polygon(100, 250, 200, 295, 300, 250, 310, 270, 200, 315, 90, 270,
            fill='darkGoldenrod'),
    Oval(200, 312, 70, 18, fill='darkGoldenrod'),
    glass,
    Oval(255, 100, 30, 95, fill='white', rotateAngle=-50, opacity=50)
    )

def getFortune(index):
    fortunes = [ 'A good suprise is in your future :)',
                 'You will stain your shirt :(',
                 'Your next dream will come true :)',
                 'You will drop your phone :(' ]

    # Return the fortune at the index.
    return fortunes[index]
def onMousePress(mouseX, mouseY):
    # If the ball is clicked on, display the appropriate fortune.
    if ((crystalBall.contains(mouseX, mouseY) == True) and (app.paused == False)):
        fortune = getFortune(app.index)
        Label(fortune, 200, 180, fill='darkSlateBlue', size=14, bold=True)
        app.paused = True

def onStep():
    colors = [ 'lightBlue', rgb(235, 225, 180), 'thistle', rgb(180, 225, 180) ]

    # Cycles through the colors with wraparound.
    app.index += 1
    if (app.index == len(colors)):
        app.index = 0

    glass.fill = colors[app.index]

onMousePress(200, 200)


# -
app.background = gradient('mediumPurple', 'black')
app.stepsPerSecond = 3
app.index = 0

# crystal ball
glass = Circle(200, 175, 125, fill='lightBlue')
crystalBall = Group(
    Polygon(120 ,315, 280, 315, 300, 350, 100, 350, fill='darkGoldenrod'),
    Oval(200, 350, 200, 50, fill='darkGoldenrod'),
    Oval(200, 315, 160, 40, fill='goldenrod'),
    glass,
    Polygon(100, 250, 200, 295, 300, 250, 310, 270, 200, 315, 90, 270,
            fill='darkGoldenrod'),
    Oval(200, 312, 70, 18, fill='darkGoldenrod'),
    glass,
    Oval(255, 100, 30, 95, fill='white', rotateAngle=-50, opacity=50)
    )

def getFortune(index):
    fortunes = [ 'A good suprise is in your future :)',
                 'You will stain your shirt :(',
                 'Your next dream will come true :)',
                 'You will drop your phone :(' ]

    # Return the fortune at the index.
    return fortunes[index]
def onMousePress(mouseX, mouseY):
    # If the ball is clicked on, display the appropriate fortune.
    if ((crystalBall.contains(mouseX, mouseY) == True) and (app.paused == False)):
        fortune = getFortune(app.index)
        Label(fortune, 200, 180, fill='darkSlateBlue', size=14, bold=True)
        app.paused = True

def onStep():
    colors = [ 'lightBlue', rgb(235, 225, 180), 'thistle', rgb(180, 225, 180) ]

    # Cycles through the colors with wraparound.
    app.index += 1
    if (app.index == len(colors)):
        app.index = 0

    glass.fill = colors[app.index]

onStep()
onMousePress(200, 200)


# -
app.background = gradient('mediumPurple', 'black')
app.stepsPerSecond = 3
app.index = 0

# crystal ball
glass = Circle(200, 175, 125, fill='lightBlue')
crystalBall = Group(
    Polygon(120 ,315, 280, 315, 300, 350, 100, 350, fill='darkGoldenrod'),
    Oval(200, 350, 200, 50, fill='darkGoldenrod'),
    Oval(200, 315, 160, 40, fill='goldenrod'),
    glass,
    Polygon(100, 250, 200, 295, 300, 250, 310, 270, 200, 315, 90, 270,
            fill='darkGoldenrod'),
    Oval(200, 312, 70, 18, fill='darkGoldenrod'),
    glass,
    Oval(255, 100, 30, 95, fill='white', rotateAngle=-50, opacity=50)
    )

def getFortune(index):
    fortunes = [ 'A good suprise is in your future :)',
                 'You will stain your shirt :(',
                 'Your next dream will come true :)',
                 'You will drop your phone :(' ]

    # Return the fortune at the index.
    return fortunes[index]
def onMousePress(mouseX, mouseY):
    # If the ball is clicked on, display the appropriate fortune.
    if ((crystalBall.contains(mouseX, mouseY) == True) and (app.paused == False)):
        fortune = getFortune(app.index)
        Label(fortune, 200, 180, fill='darkSlateBlue', size=14, bold=True)
        app.paused = True

def onStep():
    colors = [ 'lightBlue', rgb(235, 225, 180), 'thistle', rgb(180, 225, 180) ]

    # Cycles through the colors with wraparound.
    app.index += 1
    if (app.index == len(colors)):
        app.index = 0

    glass.fill = colors[app.index]

onStep()
onMousePress(200, 200)

