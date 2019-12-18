# background
Rect(0, 0, 400, 275, fill='lightSkyBlue')
Rect(0, 275, 400, 125, fill='lightGreen')

# mountains
mountain1 = Polygon(140, 275, 240, 155, 290, 175, 330, 120, 465, 275,
                    fill=rgb(95, 155, 200))
mountain2 = Polygon(0, 275, 60, 185, 100, 240, 135, 220, 190, 275,
                    fill=rgb(95, 110, 175))

# left wheel of the bike
leftWheel = Star(100, 250, 55, 17, fill=None, border='black', roundness=0)
Circle(100, 250, 60, fill=None, border='black', borderWidth=5)
Circle(100, 250, 55, fill=None, border='grey', borderWidth=5)

# right wheel of the bike
rightWheel = Star(300, 250, 55, 17, fill=None, border='black', roundness=0)
Circle(300, 250, 60, fill=None, border='black', borderWidth=5)
Circle(300, 250, 55, fill=None, border='grey', borderWidth=5)

# bike frame
Polygon(100, 250, 180, 250, 275, 155, 150, 175, fill=None, border='red',
        borderWidth=5)
Line(300, 250, 265, 115, fill='red', lineWidth=5)
Line(180, 250, 140, 150, fill='red', lineWidth=5)
Oval(145, 155, 50, 10, rotateAngle=5, align='bottom')
Line(270, 115, 235, 110, lineWidth=5)

def moveMountainsLeft():
    # Moves the moustains left in relation to the bike.
    mountain1.centerX -= 10
    mountain2.centerX -= 15

    if (mountain1.right < 0):
        mountain1.left = 400
    if (mountain2.right < 0):
        mountain2.left = 400

def moveMountainsRight():
    # Move the moustains right in relation to the bike.
    mountain1.centerX += 10
    mountain2.centerX += 15

    if (mountain1.left > 400):
        mountain1.right = 0
    if (mountain2.left > 400):
        mountain2.right = 0

def onKeyHold(keys):
    # Rotate the wheels of the bike and move the mountains appropriately.
    if ('right' in keys):
        leftWheel.rotateAngle += 5
        rightWheel.rotateAngle += 5
        moveMountainsLeft()
    elif ('left' in keys):
        leftWheel.rotateAngle -= 5
        rightWheel.rotateAngle -= 5
        moveMountainsRight()

onKeyHolds(['right'], 20)


# -
# background
Rect(0, 0, 400, 275, fill='lightSkyBlue')
Rect(0, 275, 400, 125, fill='lightGreen')

# mountains
mountain1 = Polygon(140, 275, 240, 155, 290, 175, 330, 120, 465, 275,
                    fill=rgb(95, 155, 200))
mountain2 = Polygon(0, 275, 60, 185, 100, 240, 135, 220, 190, 275,
                    fill=rgb(95, 110, 175))

# left wheel of the bike
leftWheel = Star(100, 250, 55, 17, fill=None, border='black', roundness=0)
Circle(100, 250, 60, fill=None, border='black', borderWidth=5)
Circle(100, 250, 55, fill=None, border='grey', borderWidth=5)

# right wheel of the bike
rightWheel = Star(300, 250, 55, 17, fill=None, border='black', roundness=0)
Circle(300, 250, 60, fill=None, border='black', borderWidth=5)
Circle(300, 250, 55, fill=None, border='grey', borderWidth=5)

# bike frame
Polygon(100, 250, 180, 250, 275, 155, 150, 175, fill=None, border='red',
        borderWidth=5)
Line(300, 250, 265, 115, fill='red', lineWidth=5)
Line(180, 250, 140, 150, fill='red', lineWidth=5)
Oval(145, 155, 50, 10, rotateAngle=5, align='bottom')
Line(270, 115, 235, 110, lineWidth=5)

def moveMountainsLeft():
    # Moves the moustains left in relation to the bike.
    mountain1.centerX -= 10
    mountain2.centerX -= 15

    if (mountain1.right < 0):
        mountain1.left = 400
    if (mountain2.right < 0):
        mountain2.left = 400

def moveMountainsRight():
    # Move the moustains right in relation to the bike.
    mountain1.centerX += 10
    mountain2.centerX += 15

    if (mountain1.left > 400):
        mountain1.right = 0
    if (mountain2.left > 400):
        mountain2.right = 0

def onKeyHold(keys):
    # Rotate the wheels of the bike and move the mountains appropriately.
    if ('right' in keys):
        leftWheel.rotateAngle += 5
        rightWheel.rotateAngle += 5
        moveMountainsLeft()
    elif ('left' in keys):
        leftWheel.rotateAngle -= 5
        rightWheel.rotateAngle -= 5
        moveMountainsRight()

onKeyHolds(['right'], 10)


# -
# background
Rect(0, 0, 400, 275, fill='lightSkyBlue')
Rect(0, 275, 400, 125, fill='lightGreen')

# mountains
mountain1 = Polygon(140, 275, 240, 155, 290, 175, 330, 120, 465, 275,
                    fill=rgb(95, 155, 200))
mountain2 = Polygon(0, 275, 60, 185, 100, 240, 135, 220, 190, 275,
                    fill=rgb(95, 110, 175))

# left wheel of the bike
leftWheel = Star(100, 250, 55, 17, fill=None, border='black', roundness=0)
Circle(100, 250, 60, fill=None, border='black', borderWidth=5)
Circle(100, 250, 55, fill=None, border='grey', borderWidth=5)

# right wheel of the bike
rightWheel = Star(300, 250, 55, 17, fill=None, border='black', roundness=0)
Circle(300, 250, 60, fill=None, border='black', borderWidth=5)
Circle(300, 250, 55, fill=None, border='grey', borderWidth=5)

# bike frame
Polygon(100, 250, 180, 250, 275, 155, 150, 175, fill=None, border='red',
        borderWidth=5)
Line(300, 250, 265, 115, fill='red', lineWidth=5)
Line(180, 250, 140, 150, fill='red', lineWidth=5)
Oval(145, 155, 50, 10, rotateAngle=5, align='bottom')
Line(270, 115, 235, 110, lineWidth=5)

def moveMountainsLeft():
    # Moves the moustains left in relation to the bike.
    mountain1.centerX -= 10
    mountain2.centerX -= 15

    if (mountain1.right < 0):
        mountain1.left = 400
    if (mountain2.right < 0):
        mountain2.left = 400

def moveMountainsRight():
    # Move the moustains right in relation to the bike.
    mountain1.centerX += 10
    mountain2.centerX += 15

    if (mountain1.left > 400):
        mountain1.right = 0
    if (mountain2.left > 400):
        mountain2.right = 0

def onKeyHold(keys):
    # Rotate the wheels of the bike and move the mountains appropriately.
    if ('right' in keys):
        leftWheel.rotateAngle += 5
        rightWheel.rotateAngle += 5
        moveMountainsLeft()
    elif ('left' in keys):
        leftWheel.rotateAngle -= 5
        rightWheel.rotateAngle -= 5
        moveMountainsRight()


