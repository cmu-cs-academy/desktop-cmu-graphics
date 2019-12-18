app.background = gradient(rgb(245, 240, 130), rgb(210, 200, 135), start='top')

app.stepsPerSecond = 20
app.degreesSinceLastCartwheel = 0

# floor
Line(0, 300, 400, 300, lineWidth=6,
     fill=gradient('gainsboro', rgb(197, 195, 198), 'gainsboro', start='bottom'))

stickPerson = Group(
    Circle(200, 125, 30, fill=rgb(70, 75, 75)),
    Line(200, 125, 200, 225, fill=rgb(70, 75, 75), lineWidth=6),
    Line(200, 225, 140, 275, fill=rgb(70, 75, 75), lineWidth=5),
    Line(200, 225, 260, 275, fill=rgb(70, 75, 75), lineWidth=5),
    Line(200, 175, 135, 100, fill=rgb(70, 75, 75), lineWidth=5),
    Line(200, 175, 265, 100, fill=rgb(70, 75, 75), lineWidth=5),

    # These circles make the transition from legs to hands look more natural.
    Circle(150, 200, 30, opacity=0),
    Circle(250, 200, 30, opacity=0)
    )

cartwheelCounter = Label(0, 200, 330, fill=rgb(70, 75, 75), size=25)

def onStep():
    # Rotate and move the stick person by the same amount. And set the
    # bottom of the person onto the floor.
    stickPerson.rotateAngle += 8
    stickPerson.centerX += 8
    stickPerson.bottom = 300
    # Implement wrap-around on the stick person.
    if (stickPerson.left >= 400):
        stickPerson.right = 0
    # Increase cartwheel count, each cartwheel is 360 degrees
    app.degreesSinceLastCartwheel += 8
    if (app.degreesSinceLastCartwheel >= 360):
        cartwheelCounter.value += 1
        app.degreesSinceLastCartwheel = 0

onStep()
app.paused = True


# -
app.background = gradient(rgb(245, 240, 130), rgb(210, 200, 135), start='top')

app.stepsPerSecond = 20
app.degreesSinceLastCartwheel = 0

# floor
Line(0, 300, 400, 300, lineWidth=6,
     fill=gradient('gainsboro', rgb(197, 195, 198), 'gainsboro', start='bottom'))

stickPerson = Group(
    Circle(200, 125, 30, fill=rgb(70, 75, 75)),
    Line(200, 125, 200, 225, fill=rgb(70, 75, 75), lineWidth=6),
    Line(200, 225, 140, 275, fill=rgb(70, 75, 75), lineWidth=5),
    Line(200, 225, 260, 275, fill=rgb(70, 75, 75), lineWidth=5),
    Line(200, 175, 135, 100, fill=rgb(70, 75, 75), lineWidth=5),
    Line(200, 175, 265, 100, fill=rgb(70, 75, 75), lineWidth=5),

    # These circles make the transition from legs to hands look more natural.
    Circle(150, 200, 30, opacity=0),
    Circle(250, 200, 30, opacity=0)
    )

cartwheelCounter = Label(0, 200, 330, fill=rgb(70, 75, 75), size=25)

def onStep():
    # Rotate and move the stick person by the same amount. And set the
    # bottom of the person onto the floor.
    stickPerson.rotateAngle += 8
    stickPerson.centerX += 8
    stickPerson.bottom = 300
    # Implement wrap-around on the stick person.
    if (stickPerson.left >= 400):
        stickPerson.right = 0
    # Increase cartwheel count, each cartwheel is 360 degrees
    app.degreesSinceLastCartwheel += 8
    if (app.degreesSinceLastCartwheel >= 360):
        cartwheelCounter.value += 1
        app.degreesSinceLastCartwheel = 0

onStep()
app.paused = True


# -
app.background = gradient(rgb(245, 240, 130), rgb(210, 200, 135), start='top')

app.stepsPerSecond = 20
app.degreesSinceLastCartwheel = 0

# floor
Line(0, 300, 400, 300, lineWidth=6,
     fill=gradient('gainsboro', rgb(197, 195, 198), 'gainsboro', start='bottom'))

stickPerson = Group(
    Circle(200, 125, 30, fill=rgb(70, 75, 75)),
    Line(200, 125, 200, 225, fill=rgb(70, 75, 75), lineWidth=6),
    Line(200, 225, 140, 275, fill=rgb(70, 75, 75), lineWidth=5),
    Line(200, 225, 260, 275, fill=rgb(70, 75, 75), lineWidth=5),
    Line(200, 175, 135, 100, fill=rgb(70, 75, 75), lineWidth=5),
    Line(200, 175, 265, 100, fill=rgb(70, 75, 75), lineWidth=5),

    # These circles make the transition from legs to hands look more natural.
    Circle(150, 200, 30, opacity=0),
    Circle(250, 200, 30, opacity=0)
    )

cartwheelCounter = Label(0, 200, 330, fill=rgb(70, 75, 75), size=25)

def onStep():
    # Rotate and move the stick person by the same amount. And set the
    # bottom of the person onto the floor.
    stickPerson.rotateAngle += 8
    stickPerson.centerX += 8
    stickPerson.bottom = 300
    # Implement wrap-around on the stick person.
    if (stickPerson.left >= 400):
        stickPerson.right = 0
    # Increase cartwheel count, each cartwheel is 360 degrees
    app.degreesSinceLastCartwheel += 8
    if (app.degreesSinceLastCartwheel >= 360):
        cartwheelCounter.value += 1
        app.degreesSinceLastCartwheel = 0

onSteps(40)
app.paused = True

