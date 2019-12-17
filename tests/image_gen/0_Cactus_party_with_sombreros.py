app.background = gradient('dodgerBlue', 'deepSkyBlue', 'lightCyan', start='top')

cactus = Rect(160, 50, 80, 350,
              fill=gradient('forestGreen', 'green', 'forestGreen', start='left'))
cactusTop = Circle(200, 50, 40, fill=gradient('forestGreen', 'green',
                                              'forestGreen', start='left'))
sand = Oval(200, 440, 500, 160, fill='darkKhaki')

def drawCactusArm(x, y):
    # An arm is two rounded lines connecting at (x, y). The arm connects to
    # the body of the cactus at the point (200, y).
    Line(200, y, x, y, fill='forestGreen', lineWidth=30)
    Circle(x, y, 15, fill='forestGreen')
    Line(x, y, x, y - 40, fill='forestGreen', lineWidth=30)
    Circle(x, y - 40, 15, fill='forestGreen')

def drawCactusHat(x, y):
    # Here (x, y) is the center of the bill of the sombrero, 50 pixels above
    # the elbow of the arm.
    Oval(x, y - 10, 25, 35, fill=gradient('yellow', 'darkOrange', start='left'))
    Oval(x, y, 60, 15,
         fill=gradient('lime', 'red', 'orange', 'orange', start='top'))

def onMousePress(mouseX, mouseY):
    # Add a cactus arm and hat.
    # Make sure the cactus and sand is in front of the added arms.
    drawCactusArm(mouseX, mouseY)
    drawCactusHat(mouseX, mouseY - 50)
    cactus.toFront()
    cactusTop.toFront()
    sand.toFront()

onMousePress(70, 150)
onMousePress(330, 180)


# -
app.background = gradient('dodgerBlue', 'deepSkyBlue', 'lightCyan', start='top')

cactus = Rect(160, 50, 80, 350,
              fill=gradient('forestGreen', 'green', 'forestGreen', start='left'))
cactusTop = Circle(200, 50, 40, fill=gradient('forestGreen', 'green',
                                              'forestGreen', start='left'))
sand = Oval(200, 440, 500, 160, fill='darkKhaki')

def drawCactusArm(x, y):
    # An arm is two rounded lines connecting at (x, y). The arm connects to
    # the body of the cactus at the point (200, y).
    Line(200, y, x, y, fill='forestGreen', lineWidth=30)
    Circle(x, y, 15, fill='forestGreen')
    Line(x, y, x, y - 40, fill='forestGreen', lineWidth=30)
    Circle(x, y - 40, 15, fill='forestGreen')

def drawCactusHat(x, y):
    # Here (x, y) is the center of the bill of the sombrero, 50 pixels above
    # the elbow of the arm.
    Oval(x, y - 10, 25, 35, fill=gradient('yellow', 'darkOrange', start='left'))
    Oval(x, y, 60, 15,
         fill=gradient('lime', 'red', 'orange', 'orange', start='top'))

def onMousePress(mouseX, mouseY):
    # Add a cactus arm and hat.
    # Make sure the cactus and sand is in front of the added arms.
    drawCactusArm(mouseX, mouseY)
    drawCactusHat(mouseX, mouseY - 50)
    cactus.toFront()
    cactusTop.toFront()
    sand.toFront()



# -
app.background = gradient('dodgerBlue', 'deepSkyBlue', 'lightCyan', start='top')

cactus = Rect(160, 50, 80, 350,
              fill=gradient('forestGreen', 'green', 'forestGreen', start='left'))
cactusTop = Circle(200, 50, 40, fill=gradient('forestGreen', 'green',
                                              'forestGreen', start='left'))
sand = Oval(200, 440, 500, 160, fill='darkKhaki')

def drawCactusArm(x, y):
    # An arm is two rounded lines connecting at (x, y). The arm connects to
    # the body of the cactus at the point (200, y).
    Line(200, y, x, y, fill='forestGreen', lineWidth=30)
    Circle(x, y, 15, fill='forestGreen')
    Line(x, y, x, y - 40, fill='forestGreen', lineWidth=30)
    Circle(x, y - 40, 15, fill='forestGreen')

def drawCactusHat(x, y):
    # Here (x, y) is the center of the bill of the sombrero, 50 pixels above
    # the elbow of the arm.
    Oval(x, y - 10, 25, 35, fill=gradient('yellow', 'darkOrange', start='left'))
    Oval(x, y, 60, 15,
         fill=gradient('lime', 'red', 'orange', 'orange', start='top'))

def onMousePress(mouseX, mouseY):
    # Add a cactus arm and hat.
    # Make sure the cactus and sand is in front of the added arms.
    drawCactusArm(mouseX, mouseY)
    drawCactusHat(mouseX, mouseY - 50)
    cactus.toFront()
    cactusTop.toFront()
    sand.toFront()

onMousePress(200, 200)
onMousePress(50, 300)
onMousePress(140, 50)
onMousePress(310, 170)
onMousePress(250, 350)

