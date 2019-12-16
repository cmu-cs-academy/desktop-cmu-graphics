app.background = gradient('indigo', 'royalBlue', start='top')

# hillside
Oval(200, 270, 400, 50, fill='teal')
Rect(0, 270, 400, 150, fill='teal')

def drawStars():
    starX = [ 30, 60, 70, 180, 230, 360, 380, 130, 25, 145, 380, 275 ]
    starY = [ 40, 35, 70, 50, 60, 70, 90, 100, 185, 145, 210, 225 ]

    # Loop over the star coordinates and draw random stars.
    for i in range(len(starX)):
        x = starX[i]
        y = starY[i]
        starRadius = randrange(3, 7)
        starPoint = randrange(4, 8)
        starColor = choice([ 'cornSilk', 'aliceBlue', 'lavenderBlush' ])
        starRound = randrange(10, 30)
        Star(x, y, starRadius, starPoint, fill=starColor, roundness=starRound)
def drawCows():
    cowX = [ 80, 280, 325 ]
    cowY = [ 335, 355, 275 ]

    # Loops over the cow positions and draw the cows.
    for i in range(len(cowX)):
        color = gradient('whiteSmoke', 'lightGrey', start='left')
        cow = Group(
            # legs
            Line(205, 240, 215, 240, fill=color, lineWidth=15, dashes=(3, 2)),
            Line(240, 240, 250, 240, fill=color, lineWidth=15, dashes=(3, 2)),

            # tail
            Star(257, 235, 4, 7, roundness=20),
            Line(253, 215, 257, 235, fill='white', lineWidth=1),

            # body
            Oval(200, 200, 55, 45, fill=color, align='left-top'),
            Oval(195, 205, 8, 4, rotateAngle=-20),
            Oval(215, 205, 8, 3, rotateAngle=20),

            # head
            Oval(220, 230, 25, 20, rotateAngle=-30),
            Arc(245, 205, 20, 25, 130, 160),
            Oval(205, 215, 25, 30, fill=color),
            Circle(200, 210, 3, border='white'),
            Circle(210, 210, 3, border='white'),
            Arc(205, 220, 22, 20, 90, 180, fill='lightCoral')
            )
        cow.centerX = cowX[i]
        cow.centerY = cowY[i]
        cows.add(cow)

drawStars()

cows = Group()
drawCows()

# UFO and light
light = Group(
    Polygon(160, 150, 240, 150, 280, 300, 120, 300, fill='yellow', opacity=50),
    Arc(200, 300, 160, 40, 90, 180, fill='yellow', opacity=50),
    Arc(200, 150, 80, 7, 270, 180, fill='yellow', opacity=50)
    )
UFO = Group(
    Oval(200, 120, 100, 60, opacity=50),
    Polygon(150, 120, 250, 120, 290, 150, 110, 150),
    Oval(200, 150, 180, 20, border='royalBlue'),
    light
    )

def onMouseMove(mouseX, mouseY):
    # Moves the UFO.
    UFO.centerX = mouseX
    UFO.centerY = mouseY

def onStep():
    # If any of the cows are hit by the beam from the UFO, move the cow into
    # the light beam. Also increase the rotate angle of that cow by 5.
    for cow in cows.children:
        if (light.hitsShape(cow) == True):
            cow.centerX = light.centerX
            cow.centerY = light.centerY
            cow.rotateAngle += 5

onMouseMove(275, 225)
onSteps(30)
app.paused = True


# -
app.background = gradient('indigo', 'royalBlue', start='top')

# hillside
Oval(200, 270, 400, 50, fill='teal')
Rect(0, 270, 400, 150, fill='teal')

def drawStars():
    starX = [ 30, 60, 70, 180, 230, 360, 380, 130, 25, 145, 380, 275 ]
    starY = [ 40, 35, 70, 50, 60, 70, 90, 100, 185, 145, 210, 225 ]

    # Loop over the star coordinates and draw random stars.
    for i in range(len(starX)):
        x = starX[i]
        y = starY[i]
        starRadius = randrange(3, 7)
        starPoint = randrange(4, 8)
        starColor = choice([ 'cornSilk', 'aliceBlue', 'lavenderBlush' ])
        starRound = randrange(10, 30)
        Star(x, y, starRadius, starPoint, fill=starColor, roundness=starRound)
def drawCows():
    cowX = [ 80, 280, 325 ]
    cowY = [ 335, 355, 275 ]

    # Loops over the cow positions and draw the cows.
    for i in range(len(cowX)):
        color = gradient('whiteSmoke', 'lightGrey', start='left')
        cow = Group(
            # legs
            Line(205, 240, 215, 240, fill=color, lineWidth=15, dashes=(3, 2)),
            Line(240, 240, 250, 240, fill=color, lineWidth=15, dashes=(3, 2)),

            # tail
            Star(257, 235, 4, 7, roundness=20),
            Line(253, 215, 257, 235, fill='white', lineWidth=1),

            # body
            Oval(200, 200, 55, 45, fill=color, align='left-top'),
            Oval(195, 205, 8, 4, rotateAngle=-20),
            Oval(215, 205, 8, 3, rotateAngle=20),

            # head
            Oval(220, 230, 25, 20, rotateAngle=-30),
            Arc(245, 205, 20, 25, 130, 160),
            Oval(205, 215, 25, 30, fill=color),
            Circle(200, 210, 3, border='white'),
            Circle(210, 210, 3, border='white'),
            Arc(205, 220, 22, 20, 90, 180, fill='lightCoral')
            )
        cow.centerX = cowX[i]
        cow.centerY = cowY[i]
        cows.add(cow)

drawStars()

cows = Group()
drawCows()

# UFO and light
light = Group(
    Polygon(160, 150, 240, 150, 280, 300, 120, 300, fill='yellow', opacity=50),
    Arc(200, 300, 160, 40, 90, 180, fill='yellow', opacity=50),
    Arc(200, 150, 80, 7, 270, 180, fill='yellow', opacity=50)
    )
UFO = Group(
    Oval(200, 120, 100, 60, opacity=50),
    Polygon(150, 120, 250, 120, 290, 150, 110, 150),
    Oval(200, 150, 180, 20, border='royalBlue'),
    light
    )

def onMouseMove(mouseX, mouseY):
    # Moves the UFO.
    UFO.centerX = mouseX
    UFO.centerY = mouseY

def onStep():
    # If any of the cows are hit by the beam from the UFO, move the cow into
    # the light beam. Also increase the rotate angle of that cow by 5.
    for cow in cows.children:
        if (light.hitsShape(cow) == True):
            cow.centerX = light.centerX
            cow.centerY = light.centerY
            cow.rotateAngle += 5

onMouseMove(100, 150)
app.paused = True


# -
app.background = gradient('indigo', 'royalBlue', start='top')

# hillside
Oval(200, 270, 400, 50, fill='teal')
Rect(0, 270, 400, 150, fill='teal')

def drawStars():
    starX = [ 30, 60, 70, 180, 230, 360, 380, 130, 25, 145, 380, 275 ]
    starY = [ 40, 35, 70, 50, 60, 70, 90, 100, 185, 145, 210, 225 ]

    # Loop over the star coordinates and draw random stars.
    for i in range(len(starX)):
        x = starX[i]
        y = starY[i]
        starRadius = randrange(3, 7)
        starPoint = randrange(4, 8)
        starColor = choice([ 'cornSilk', 'aliceBlue', 'lavenderBlush' ])
        starRound = randrange(10, 30)
        Star(x, y, starRadius, starPoint, fill=starColor, roundness=starRound)
def drawCows():
    cowX = [ 80, 280, 325 ]
    cowY = [ 335, 355, 275 ]

    # Loops over the cow positions and draw the cows.
    for i in range(len(cowX)):
        color = gradient('whiteSmoke', 'lightGrey', start='left')
        cow = Group(
            # legs
            Line(205, 240, 215, 240, fill=color, lineWidth=15, dashes=(3, 2)),
            Line(240, 240, 250, 240, fill=color, lineWidth=15, dashes=(3, 2)),

            # tail
            Star(257, 235, 4, 7, roundness=20),
            Line(253, 215, 257, 235, fill='white', lineWidth=1),

            # body
            Oval(200, 200, 55, 45, fill=color, align='left-top'),
            Oval(195, 205, 8, 4, rotateAngle=-20),
            Oval(215, 205, 8, 3, rotateAngle=20),

            # head
            Oval(220, 230, 25, 20, rotateAngle=-30),
            Arc(245, 205, 20, 25, 130, 160),
            Oval(205, 215, 25, 30, fill=color),
            Circle(200, 210, 3, border='white'),
            Circle(210, 210, 3, border='white'),
            Arc(205, 220, 22, 20, 90, 180, fill='lightCoral')
            )
        cow.centerX = cowX[i]
        cow.centerY = cowY[i]
        cows.add(cow)

drawStars()

cows = Group()
drawCows()

# UFO and light
light = Group(
    Polygon(160, 150, 240, 150, 280, 300, 120, 300, fill='yellow', opacity=50),
    Arc(200, 300, 160, 40, 90, 180, fill='yellow', opacity=50),
    Arc(200, 150, 80, 7, 270, 180, fill='yellow', opacity=50)
    )
UFO = Group(
    Oval(200, 120, 100, 60, opacity=50),
    Polygon(150, 120, 250, 120, 290, 150, 110, 150),
    Oval(200, 150, 180, 20, border='royalBlue'),
    light
    )

def onMouseMove(mouseX, mouseY):
    # Moves the UFO.
    UFO.centerX = mouseX
    UFO.centerY = mouseY

def onStep():
    # If any of the cows are hit by the beam from the UFO, move the cow into
    # the light beam. Also increase the rotate angle of that cow by 5.
    for cow in cows.children:
        if (light.hitsShape(cow) == True):
            cow.centerX = light.centerX
            cow.centerY = light.centerY
            cow.rotateAngle += 5

onMouseMove(100, 150)
app.paused = True

