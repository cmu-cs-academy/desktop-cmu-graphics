# In this exercise, you will draw the flowers in the sky and then add a spiral
# to Gary's shell in order to complete the scene.

app.background = gradient('turquoise', 'blue', start='top')

def createSkyFlower(x, y, color, startAngle):
    ### Shapes can be drawn around a circle by placing their centers at the
    ### endpoint of a line which rotates after placing each shape.

    # This line's x1, y1 can be used to place the petals.
    petalPosition = Line(x, y - 35, x, y + 35)
    petalPosition.rotateAngle = startAngle

    # Create 5 petals placed at 72 degree intervals around a central point.
    for i in range(5):
        ovalAngle = petalPosition.rotateAngle
        Oval(petalPosition.x1, petalPosition.y1, 30, 50, fill=None, border=color,
             rotateAngle=ovalAngle, opacity=40)
        petalPosition.rotateAngle += 72
    # Removes the line.
    petalPosition.visible = False

createSkyFlower(350, 50, 'paleGreen', 5)
createSkyFlower(210, 115, 'mediumAquamarine', 15)
createSkyFlower(100, 200, 'mediumSeaGreen', -10)
createSkyFlower(50, 50, 'paleGreen', -10)

# Spongebob's house
Star(330, 170, 40, 9, fill=gradient(rgb(188, 226, 66), rgb(23, 133, 23)),
     border='seaGreen', roundness=50)
Oval(370, 280, 80, 120, fill=gradient('orange', 'orangeRed', start='left'),
     border='brown', align='right-bottom')
Line(360, 180, 290, 220, fill='brown')
Line(370, 220, 300, 260, fill='brown')
Line(300, 180, 370, 220, fill='brown')
Line(290, 220, 360, 260, fill='brown')

# Spongebob's door
Oval(345, 270, 30, 50, fill=gradient('lightSkyBlue', 'skyBlue', start='left'),
     border='steelBlue', align='right-bottom')
Oval(343, 266, 25, 45, fill=gradient('lightSkyBlue', 'skyBlue', start='left'),
     border='steelBlue', align='right-bottom')

# Spongebob's windows and chimney
Circle(310, 210, 8, fill=gradient('lightSkyBlue', 'skyBlue', start='left'),
       border='steelBlue')
Circle(310, 210, 6, fill=gradient('lightSkyBlue', 'skyBlue', start='left'),
       border='steelBlue')
Circle(358, 235, 6, fill=gradient('lightSkyBlue', 'skyBlue', start='left'),
       border='steelBlue')
Polygon(360, 200, 370, 195, 370, 180, 380, 180, 375, 200, fill='deepSkyBlue',
        border='steelBlue')

# sand
Rect(0, 250, 400, 150, fill=gradient(rgb(200, 251, 220), 'cornSilk', start='top'))

# Gary (the snail)
Oval(60, 295, 100, 20, fill='paleTurquoise', opacity=60, align='top')
slime = Rect(60, 295, 5, 20, fill='paleTurquoise', opacity=60, align='top')
shellSpiral = Polygon(45, 290, 45, 285, fill=None, border='red')
gary = Group(
    Oval(60, 295, 100, 20, fill='skyBlue', align='top'),

    # eye stalks and eyes
    Line(95, 305, 95, 265, fill='skyBlue', lineWidth=5),
    Circle(95, 265, 7, fill=rgb(200, 255, 170), border='black', borderWidth=1),
    Circle(97, 265, 3, border='coral'),
    Line(90, 305, 85, 265, fill='skyBlue', lineWidth=5),
    Circle(85, 265, 7, fill=rgb(200, 255, 170), border='black', borderWidth=1),
    Circle(87, 265, 3, border='coral'),

    # shell
    Oval(78, 312, 55, 65, fill=gradient(rgb(225, 170, 160), 'pink', start='left'),
         border='darkRed', borderWidth=1, rotateAngle=-10, align='right-bottom'),
    Oval(82, 305, 60, 10, border='darkRed', borderWidth=1, align='right-bottom',
         fill=gradient(rgb(255, 170, 160), 'pink', start='left-top')),
    Line(25, 296, 75, 295, fill=gradient(rgb(225, 170, 160), 'pink', start='left'),
         lineWidth=3),
    shellSpiral,
    Line(45, 305, 45, 290, fill=rgb(240, 185, 170), lineWidth=4),

    # spots
    Oval(50, 260, 8, 5, fill='steelBlue'),
    Oval(38, 265, 6, 4, fill='steelBlue', rotateAngle=-30),
    Oval(30, 275, 4, 3, fill='steelBlue', rotateAngle=-60),
    Oval(62, 265, 6, 4, fill='steelBlue', rotateAngle=30),
    Oval(70, 275, 4, 3, fill='steelBlue', rotateAngle=60),

    Polygon(18, 303, 25, 310, 40, 315, 65, 315, 90, 303, fill='skyBlue'),
    Polygon(35, 315, 65, 315, 50, 320, fill='honeydew'),
    Line(27, 303, 73, 303, fill='lightSlateGrey', lineWidth=1),
    Polygon(10, 305, 40, 310, 80, 310, 110, 305, 110, 310, 80, 315, 40, 315,
            10, 310, fill='lightGreen')
    )

def drawSpiral():
    ### A spiral can be created by using a similar trick to what we did for the
    ### sky flowers, just increasing the length of the rotated line every time
    ### we increase its angle. Do that here to create a spiral on the shell!

    # Use this line to create the spiral on the shell.
    spiralLine = Line(45, 285, 45, 295)

    # The spiral will be a polygon of 12 points created in the manner
    # described above.
    for i in range(12):
        # There is no length property for lines but if a line is vertical
        # we can make it longer by simply moving both of the endpoints!
        # First, get the next angle that the line should rotate to.
        nextAngle = spiralLine.rotateAngle + 30
        # For the first 6 points of the spiral, increase the length of
        # the line by 8.
        if (i < 6):
            spiralLine.rotateAngle = 0
            spiralLine.y1 += 4
            spiralLine.y2 -= 4
        # Set the new angle and add the new point to the spiral.
        spiralLine.rotateAngle = nextAngle
        shellSpiral.addPoint(spiralLine.x1, spiralLine.y1)
    # Removes the line.
    spiralLine.visible = False

drawSpiral()

def onStep():
    gary.centerX += 1
    slime.width += 1
    if (gary.left >= 400):
        gary.right = 0

onSteps(30)
app.paused = True


# -
# In this exercise, you will draw the flowers in the sky and then add a spiral
# to Gary's shell in order to complete the scene.

app.background = gradient('turquoise', 'blue', start='top')

def createSkyFlower(x, y, color, startAngle):
    ### Shapes can be drawn around a circle by placing their centers at the
    ### endpoint of a line which rotates after placing each shape.

    # This line's x1, y1 can be used to place the petals.
    petalPosition = Line(x, y - 35, x, y + 35)
    petalPosition.rotateAngle = startAngle

    # Create 5 petals placed at 72 degree intervals around a central point.
    for i in range(5):
        ovalAngle = petalPosition.rotateAngle
        Oval(petalPosition.x1, petalPosition.y1, 30, 50, fill=None, border=color,
             rotateAngle=ovalAngle, opacity=40)
        petalPosition.rotateAngle += 72
    # Removes the line.
    petalPosition.visible = False

createSkyFlower(350, 50, 'paleGreen', 5)
createSkyFlower(210, 115, 'mediumAquamarine', 15)
createSkyFlower(100, 200, 'mediumSeaGreen', -10)
createSkyFlower(50, 50, 'paleGreen', -10)

# Spongebob's house
Star(330, 170, 40, 9, fill=gradient(rgb(188, 226, 66), rgb(23, 133, 23)),
     border='seaGreen', roundness=50)
Oval(370, 280, 80, 120, fill=gradient('orange', 'orangeRed', start='left'),
     border='brown', align='right-bottom')
Line(360, 180, 290, 220, fill='brown')
Line(370, 220, 300, 260, fill='brown')
Line(300, 180, 370, 220, fill='brown')
Line(290, 220, 360, 260, fill='brown')

# Spongebob's door
Oval(345, 270, 30, 50, fill=gradient('lightSkyBlue', 'skyBlue', start='left'),
     border='steelBlue', align='right-bottom')
Oval(343, 266, 25, 45, fill=gradient('lightSkyBlue', 'skyBlue', start='left'),
     border='steelBlue', align='right-bottom')

# Spongebob's windows and chimney
Circle(310, 210, 8, fill=gradient('lightSkyBlue', 'skyBlue', start='left'),
       border='steelBlue')
Circle(310, 210, 6, fill=gradient('lightSkyBlue', 'skyBlue', start='left'),
       border='steelBlue')
Circle(358, 235, 6, fill=gradient('lightSkyBlue', 'skyBlue', start='left'),
       border='steelBlue')
Polygon(360, 200, 370, 195, 370, 180, 380, 180, 375, 200, fill='deepSkyBlue',
        border='steelBlue')

# sand
Rect(0, 250, 400, 150, fill=gradient(rgb(200, 251, 220), 'cornSilk', start='top'))

# Gary (the snail)
Oval(60, 295, 100, 20, fill='paleTurquoise', opacity=60, align='top')
slime = Rect(60, 295, 5, 20, fill='paleTurquoise', opacity=60, align='top')
shellSpiral = Polygon(45, 290, 45, 285, fill=None, border='red')
gary = Group(
    Oval(60, 295, 100, 20, fill='skyBlue', align='top'),

    # eye stalks and eyes
    Line(95, 305, 95, 265, fill='skyBlue', lineWidth=5),
    Circle(95, 265, 7, fill=rgb(200, 255, 170), border='black', borderWidth=1),
    Circle(97, 265, 3, border='coral'),
    Line(90, 305, 85, 265, fill='skyBlue', lineWidth=5),
    Circle(85, 265, 7, fill=rgb(200, 255, 170), border='black', borderWidth=1),
    Circle(87, 265, 3, border='coral'),

    # shell
    Oval(78, 312, 55, 65, fill=gradient(rgb(225, 170, 160), 'pink', start='left'),
         border='darkRed', borderWidth=1, rotateAngle=-10, align='right-bottom'),
    Oval(82, 305, 60, 10, border='darkRed', borderWidth=1, align='right-bottom',
         fill=gradient(rgb(255, 170, 160), 'pink', start='left-top')),
    Line(25, 296, 75, 295, fill=gradient(rgb(225, 170, 160), 'pink', start='left'),
         lineWidth=3),
    shellSpiral,
    Line(45, 305, 45, 290, fill=rgb(240, 185, 170), lineWidth=4),

    # spots
    Oval(50, 260, 8, 5, fill='steelBlue'),
    Oval(38, 265, 6, 4, fill='steelBlue', rotateAngle=-30),
    Oval(30, 275, 4, 3, fill='steelBlue', rotateAngle=-60),
    Oval(62, 265, 6, 4, fill='steelBlue', rotateAngle=30),
    Oval(70, 275, 4, 3, fill='steelBlue', rotateAngle=60),

    Polygon(18, 303, 25, 310, 40, 315, 65, 315, 90, 303, fill='skyBlue'),
    Polygon(35, 315, 65, 315, 50, 320, fill='honeydew'),
    Line(27, 303, 73, 303, fill='lightSlateGrey', lineWidth=1),
    Polygon(10, 305, 40, 310, 80, 310, 110, 305, 110, 310, 80, 315, 40, 315,
            10, 310, fill='lightGreen')
    )

def drawSpiral():
    ### A spiral can be created by using a similar trick to what we did for the
    ### sky flowers, just increasing the length of the rotated line every time
    ### we increase its angle. Do that here to create a spiral on the shell!

    # Use this line to create the spiral on the shell.
    spiralLine = Line(45, 285, 45, 295)

    # The spiral will be a polygon of 12 points created in the manner
    # described above.
    for i in range(12):
        # There is no length property for lines but if a line is vertical
        # we can make it longer by simply moving both of the endpoints!
        # First, get the next angle that the line should rotate to.
        nextAngle = spiralLine.rotateAngle + 30
        # For the first 6 points of the spiral, increase the length of
        # the line by 8.
        if (i < 6):
            spiralLine.rotateAngle = 0
            spiralLine.y1 += 4
            spiralLine.y2 -= 4
        # Set the new angle and add the new point to the spiral.
        spiralLine.rotateAngle = nextAngle
        shellSpiral.addPoint(spiralLine.x1, spiralLine.y1)
    # Removes the line.
    spiralLine.visible = False

drawSpiral()

def onStep():
    gary.centerX += 1
    slime.width += 1
    if (gary.left >= 400):
        gary.right = 0

onSteps(100)
app.paused = True


# -
# In this exercise, you will draw the flowers in the sky and then add a spiral
# to Gary's shell in order to complete the scene.

app.background = gradient('turquoise', 'blue', start='top')

def createSkyFlower(x, y, color, startAngle):
    ### Shapes can be drawn around a circle by placing their centers at the
    ### endpoint of a line which rotates after placing each shape.

    # This line's x1, y1 can be used to place the petals.
    petalPosition = Line(x, y - 35, x, y + 35)
    petalPosition.rotateAngle = startAngle

    # Create 5 petals placed at 72 degree intervals around a central point.
    for i in range(5):
        ovalAngle = petalPosition.rotateAngle
        Oval(petalPosition.x1, petalPosition.y1, 30, 50, fill=None, border=color,
             rotateAngle=ovalAngle, opacity=40)
        petalPosition.rotateAngle += 72
    # Removes the line.
    petalPosition.visible = False

createSkyFlower(350, 50, 'paleGreen', 5)
createSkyFlower(210, 115, 'mediumAquamarine', 15)
createSkyFlower(100, 200, 'mediumSeaGreen', -10)
createSkyFlower(50, 50, 'paleGreen', -10)

# Spongebob's house
Star(330, 170, 40, 9, fill=gradient(rgb(188, 226, 66), rgb(23, 133, 23)),
     border='seaGreen', roundness=50)
Oval(370, 280, 80, 120, fill=gradient('orange', 'orangeRed', start='left'),
     border='brown', align='right-bottom')
Line(360, 180, 290, 220, fill='brown')
Line(370, 220, 300, 260, fill='brown')
Line(300, 180, 370, 220, fill='brown')
Line(290, 220, 360, 260, fill='brown')

# Spongebob's door
Oval(345, 270, 30, 50, fill=gradient('lightSkyBlue', 'skyBlue', start='left'),
     border='steelBlue', align='right-bottom')
Oval(343, 266, 25, 45, fill=gradient('lightSkyBlue', 'skyBlue', start='left'),
     border='steelBlue', align='right-bottom')

# Spongebob's windows and chimney
Circle(310, 210, 8, fill=gradient('lightSkyBlue', 'skyBlue', start='left'),
       border='steelBlue')
Circle(310, 210, 6, fill=gradient('lightSkyBlue', 'skyBlue', start='left'),
       border='steelBlue')
Circle(358, 235, 6, fill=gradient('lightSkyBlue', 'skyBlue', start='left'),
       border='steelBlue')
Polygon(360, 200, 370, 195, 370, 180, 380, 180, 375, 200, fill='deepSkyBlue',
        border='steelBlue')

# sand
Rect(0, 250, 400, 150, fill=gradient(rgb(200, 251, 220), 'cornSilk', start='top'))

# Gary (the snail)
Oval(60, 295, 100, 20, fill='paleTurquoise', opacity=60, align='top')
slime = Rect(60, 295, 5, 20, fill='paleTurquoise', opacity=60, align='top')
shellSpiral = Polygon(45, 290, 45, 285, fill=None, border='red')
gary = Group(
    Oval(60, 295, 100, 20, fill='skyBlue', align='top'),

    # eye stalks and eyes
    Line(95, 305, 95, 265, fill='skyBlue', lineWidth=5),
    Circle(95, 265, 7, fill=rgb(200, 255, 170), border='black', borderWidth=1),
    Circle(97, 265, 3, border='coral'),
    Line(90, 305, 85, 265, fill='skyBlue', lineWidth=5),
    Circle(85, 265, 7, fill=rgb(200, 255, 170), border='black', borderWidth=1),
    Circle(87, 265, 3, border='coral'),

    # shell
    Oval(78, 312, 55, 65, fill=gradient(rgb(225, 170, 160), 'pink', start='left'),
         border='darkRed', borderWidth=1, rotateAngle=-10, align='right-bottom'),
    Oval(82, 305, 60, 10, border='darkRed', borderWidth=1, align='right-bottom',
         fill=gradient(rgb(255, 170, 160), 'pink', start='left-top')),
    Line(25, 296, 75, 295, fill=gradient(rgb(225, 170, 160), 'pink', start='left'),
         lineWidth=3),
    shellSpiral,
    Line(45, 305, 45, 290, fill=rgb(240, 185, 170), lineWidth=4),

    # spots
    Oval(50, 260, 8, 5, fill='steelBlue'),
    Oval(38, 265, 6, 4, fill='steelBlue', rotateAngle=-30),
    Oval(30, 275, 4, 3, fill='steelBlue', rotateAngle=-60),
    Oval(62, 265, 6, 4, fill='steelBlue', rotateAngle=30),
    Oval(70, 275, 4, 3, fill='steelBlue', rotateAngle=60),

    Polygon(18, 303, 25, 310, 40, 315, 65, 315, 90, 303, fill='skyBlue'),
    Polygon(35, 315, 65, 315, 50, 320, fill='honeydew'),
    Line(27, 303, 73, 303, fill='lightSlateGrey', lineWidth=1),
    Polygon(10, 305, 40, 310, 80, 310, 110, 305, 110, 310, 80, 315, 40, 315,
            10, 310, fill='lightGreen')
    )

def drawSpiral():
    ### A spiral can be created by using a similar trick to what we did for the
    ### sky flowers, just increasing the length of the rotated line every time
    ### we increase its angle. Do that here to create a spiral on the shell!

    # Use this line to create the spiral on the shell.
    spiralLine = Line(45, 285, 45, 295)

    # The spiral will be a polygon of 12 points created in the manner
    # described above.
    for i in range(12):
        # There is no length property for lines but if a line is vertical
        # we can make it longer by simply moving both of the endpoints!
        # First, get the next angle that the line should rotate to.
        nextAngle = spiralLine.rotateAngle + 30
        # For the first 6 points of the spiral, increase the length of
        # the line by 8.
        if (i < 6):
            spiralLine.rotateAngle = 0
            spiralLine.y1 += 4
            spiralLine.y2 -= 4
        # Set the new angle and add the new point to the spiral.
        spiralLine.rotateAngle = nextAngle
        shellSpiral.addPoint(spiralLine.x1, spiralLine.y1)
    # Removes the line.
    spiralLine.visible = False

drawSpiral()

def onStep():
    gary.centerX += 1
    slime.width += 1
    if (gary.left >= 400):
        gary.right = 0


