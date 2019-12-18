app.background = 'black'
app.stepsPerSecond = 30

stars = Group(align='center')
stars.count = 0

# starship frame
Line(100, 70, 40, -5,
     fill=gradient(rgb(0, 25, 40), rgb(0, 30, 50), start='top'), lineWidth=20)
Line(300, 70, 360, -5,
     fill=gradient(rgb(0, 25, 40), rgb(0, 30, 50), start='top'), lineWidth=20)
Line(0, 180, 100, 70,
     fill=gradient(rgb(0, 50, 80), rgb(0, 30, 50), start='left'), lineWidth=20)
Line(400, 180, 300, 70,
     fill=gradient(rgb(0, 50, 80), rgb(0, 30, 50), start='right'), lineWidth=20)
Line(100, 70, 300, 70, fill=rgb(0, 30, 50), lineWidth=20)

# starship dashboard
Polygon(75, 360, 325, 360, 400, 380, 400, 400, 0, 400, 0, 380,
        fill=rgb(0, 40, 60), border='cadetBlue', borderWidth=1)
Rect(75, 360, 250, 40, fill=rgb(0, 50, 80), border='cadetBlue', borderWidth=1)
Line(100, 400, 300, 400, fill='paleGreen', lineWidth=60, opacity=60, dashes=True)
Line(200, 365, 200, 400, fill=rgb(0, 50, 80), lineWidth=200, dashes=True)

# starship steering wheel
Star(200, 395, 50, 4, fill=rgb(0, 30, 50), roundness=20, rotateAngle=25)
Circle(200, 395, 50, fill=None, border=rgb(0, 30, 50), borderWidth=10)

def onStep():
    if (stars.count >= 250):
        stars.clear()
        stars.count = 0
        stars.width = 1
        stars.height = 1

    # Add a new randomly placed star with radius 1 to the stars.
    newX = randrange(0, 400)
    newY = randrange(0, 400)
    stars.add(
        Circle(newX, newY, 1, fill='white')
        )
    # Change the width and height of the stars group by multiplying by 1.01.
    stars.width = stars.width * 1.01
    stars.height = stars.height * 1.01
    stars.count += 1

onSteps(50)
app.paused = True


# -
app.background = 'black'
app.stepsPerSecond = 30

stars = Group(align='center')
stars.count = 0

# starship frame
Line(100, 70, 40, -5,
     fill=gradient(rgb(0, 25, 40), rgb(0, 30, 50), start='top'), lineWidth=20)
Line(300, 70, 360, -5,
     fill=gradient(rgb(0, 25, 40), rgb(0, 30, 50), start='top'), lineWidth=20)
Line(0, 180, 100, 70,
     fill=gradient(rgb(0, 50, 80), rgb(0, 30, 50), start='left'), lineWidth=20)
Line(400, 180, 300, 70,
     fill=gradient(rgb(0, 50, 80), rgb(0, 30, 50), start='right'), lineWidth=20)
Line(100, 70, 300, 70, fill=rgb(0, 30, 50), lineWidth=20)

# starship dashboard
Polygon(75, 360, 325, 360, 400, 380, 400, 400, 0, 400, 0, 380,
        fill=rgb(0, 40, 60), border='cadetBlue', borderWidth=1)
Rect(75, 360, 250, 40, fill=rgb(0, 50, 80), border='cadetBlue', borderWidth=1)
Line(100, 400, 300, 400, fill='paleGreen', lineWidth=60, opacity=60, dashes=True)
Line(200, 365, 200, 400, fill=rgb(0, 50, 80), lineWidth=200, dashes=True)

# starship steering wheel
Star(200, 395, 50, 4, fill=rgb(0, 30, 50), roundness=20, rotateAngle=25)
Circle(200, 395, 50, fill=None, border=rgb(0, 30, 50), borderWidth=10)

def onStep():
    if (stars.count >= 250):
        stars.clear()
        stars.count = 0
        stars.width = 1
        stars.height = 1

    # Add a new randomly placed star with radius 1 to the stars.
    newX = randrange(0, 400)
    newY = randrange(0, 400)
    stars.add(
        Circle(newX, newY, 1, fill='white')
        )
    # Change the width and height of the stars group by multiplying by 1.01.
    stars.width = stars.width * 1.01
    stars.height = stars.height * 1.01
    stars.count += 1

onStep()
app.paused = True


# -
app.background = 'black'
app.stepsPerSecond = 30

stars = Group(align='center')
stars.count = 0

# starship frame
Line(100, 70, 40, -5,
     fill=gradient(rgb(0, 25, 40), rgb(0, 30, 50), start='top'), lineWidth=20)
Line(300, 70, 360, -5,
     fill=gradient(rgb(0, 25, 40), rgb(0, 30, 50), start='top'), lineWidth=20)
Line(0, 180, 100, 70,
     fill=gradient(rgb(0, 50, 80), rgb(0, 30, 50), start='left'), lineWidth=20)
Line(400, 180, 300, 70,
     fill=gradient(rgb(0, 50, 80), rgb(0, 30, 50), start='right'), lineWidth=20)
Line(100, 70, 300, 70, fill=rgb(0, 30, 50), lineWidth=20)

# starship dashboard
Polygon(75, 360, 325, 360, 400, 380, 400, 400, 0, 400, 0, 380,
        fill=rgb(0, 40, 60), border='cadetBlue', borderWidth=1)
Rect(75, 360, 250, 40, fill=rgb(0, 50, 80), border='cadetBlue', borderWidth=1)
Line(100, 400, 300, 400, fill='paleGreen', lineWidth=60, opacity=60, dashes=True)
Line(200, 365, 200, 400, fill=rgb(0, 50, 80), lineWidth=200, dashes=True)

# starship steering wheel
Star(200, 395, 50, 4, fill=rgb(0, 30, 50), roundness=20, rotateAngle=25)
Circle(200, 395, 50, fill=None, border=rgb(0, 30, 50), borderWidth=10)

def onStep():
    if (stars.count >= 250):
        stars.clear()
        stars.count = 0
        stars.width = 1
        stars.height = 1

    # Add a new randomly placed star with radius 1 to the stars.
    newX = randrange(0, 400)
    newY = randrange(0, 400)
    stars.add(
        Circle(newX, newY, 1, fill='white')
        )
    # Change the width and height of the stars group by multiplying by 1.01.
    stars.width = stars.width * 1.01
    stars.height = stars.height * 1.01
    stars.count += 1

onSteps(125)
app.paused = True

