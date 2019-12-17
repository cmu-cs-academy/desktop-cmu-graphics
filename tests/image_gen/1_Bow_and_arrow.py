# background
Rect(0, 0, 400, 300, fill=gradient('lightSkyBlue', 'lightCyan', start='top'))
Rect(0, 300, 400, 100, fill=gradient('seaGreen', 'darkOliveGreen', start='top'))

# stick person
Circle(80, 140, 20)
Line(80, 140, 80, 250, lineWidth=3)
Line(80, 250, 100, 300, lineWidth=3)
Line(80, 250, 60, 300, lineWidth=3)
leftArm = Line(80, 175, 50, 200, lineWidth=3)
rightArm = Line(80, 175, 115, 200, lineWidth=3)

# points
Label('Score:', 10, 25, size=24, align='left')
score = Label(0, 110, 26, size=28)

# target
Line(325, 200, 365, 300, fill='burlyWood', lineWidth=8)
Line(325, 200, 285, 300, fill='burlyWood', lineWidth=8)
Circle(325, 200, 68, fill='burlyWood')
Circle(325, 200, 60, border='ghostWhite', borderWidth=10)
Circle(325, 200, 40, fill='crimson', border='deepSkyBlue', borderWidth=10)
Circle(325, 200, 10, fill='yellow')

# bow and arrow
### (HINT: The bow is defined as an arc!)
bow = Arc(100, 200, 50, 80, 0, 180, fill=None,
          border=gradient('saddleBrown', 'burlyWood', start='left'), borderWidth=5)

arrow = Line(50, 200, 150, 200, lineWidth=3, arrowEnd=True,
             fill=gradient('lightGrey', 'saddleBrown', start='right'))

def resetBowAndArrow():
    arrow.centerX = 100
    bow.width = 25
    leftArm.x2 = arrow.left
    rightArm.x2 = bow.right

def arrowToTarget():
    arrow.right = 325
    bow.startAngle = 0
    bow.sweepAngle = 180
    bow.width = 25
    rightArm.x2 = bow.right
    score.value += 10

def onMousePress(mouseX, mouseY):
    resetBowAndArrow()

def onMouseRelease(mouseX, mouseY):
    if (arrow.centerX < 150):
        arrowToTarget()

def onMouseDrag(mouseX, mouseY):
    if (bow.sweepAngle >= 125):
        # Pull back the arrow.
        # Move the arrow back and increase the startAngle of the bow by 1 pixel
        # each. Then decrease the sweepAngle of the bow and increase the width
        # of the bow.
        arrow.left -= 1
        bow.startAngle += 1
        bow.sweepAngle -= 2
        bow.width += 1
        # Moves the arms.
        leftArm.x2 = arrow.left
        rightArm.x2 = bow.right


onMouseDrag(200, 200)


# -
# background
Rect(0, 0, 400, 300, fill=gradient('lightSkyBlue', 'lightCyan', start='top'))
Rect(0, 300, 400, 100, fill=gradient('seaGreen', 'darkOliveGreen', start='top'))

# stick person
Circle(80, 140, 20)
Line(80, 140, 80, 250, lineWidth=3)
Line(80, 250, 100, 300, lineWidth=3)
Line(80, 250, 60, 300, lineWidth=3)
leftArm = Line(80, 175, 50, 200, lineWidth=3)
rightArm = Line(80, 175, 115, 200, lineWidth=3)

# points
Label('Score:', 10, 25, size=24, align='left')
score = Label(0, 110, 26, size=28)

# target
Line(325, 200, 365, 300, fill='burlyWood', lineWidth=8)
Line(325, 200, 285, 300, fill='burlyWood', lineWidth=8)
Circle(325, 200, 68, fill='burlyWood')
Circle(325, 200, 60, border='ghostWhite', borderWidth=10)
Circle(325, 200, 40, fill='crimson', border='deepSkyBlue', borderWidth=10)
Circle(325, 200, 10, fill='yellow')

# bow and arrow
### (HINT: The bow is defined as an arc!)
bow = Arc(100, 200, 50, 80, 0, 180, fill=None,
          border=gradient('saddleBrown', 'burlyWood', start='left'), borderWidth=5)

arrow = Line(50, 200, 150, 200, lineWidth=3, arrowEnd=True,
             fill=gradient('lightGrey', 'saddleBrown', start='right'))

def resetBowAndArrow():
    arrow.centerX = 100
    bow.width = 25
    leftArm.x2 = arrow.left
    rightArm.x2 = bow.right

def arrowToTarget():
    arrow.right = 325
    bow.startAngle = 0
    bow.sweepAngle = 180
    bow.width = 25
    rightArm.x2 = bow.right
    score.value += 10

def onMousePress(mouseX, mouseY):
    resetBowAndArrow()

def onMouseRelease(mouseX, mouseY):
    if (arrow.centerX < 150):
        arrowToTarget()

def onMouseDrag(mouseX, mouseY):
    if (bow.sweepAngle >= 125):
        # Pull back the arrow.
        # Move the arrow back and increase the startAngle of the bow by 1 pixel
        # each. Then decrease the sweepAngle of the bow and increase the width
        # of the bow.
        arrow.left -= 1
        bow.startAngle += 1
        bow.sweepAngle -= 2
        bow.width += 1
        # Moves the arms.
        leftArm.x2 = arrow.left
        rightArm.x2 = bow.right


onMouseDrag(200, 200)
onMouseDrag(200, 200)


# -
# background
Rect(0, 0, 400, 300, fill=gradient('lightSkyBlue', 'lightCyan', start='top'))
Rect(0, 300, 400, 100, fill=gradient('seaGreen', 'darkOliveGreen', start='top'))

# stick person
Circle(80, 140, 20)
Line(80, 140, 80, 250, lineWidth=3)
Line(80, 250, 100, 300, lineWidth=3)
Line(80, 250, 60, 300, lineWidth=3)
leftArm = Line(80, 175, 50, 200, lineWidth=3)
rightArm = Line(80, 175, 115, 200, lineWidth=3)

# points
Label('Score:', 10, 25, size=24, align='left')
score = Label(0, 110, 26, size=28)

# target
Line(325, 200, 365, 300, fill='burlyWood', lineWidth=8)
Line(325, 200, 285, 300, fill='burlyWood', lineWidth=8)
Circle(325, 200, 68, fill='burlyWood')
Circle(325, 200, 60, border='ghostWhite', borderWidth=10)
Circle(325, 200, 40, fill='crimson', border='deepSkyBlue', borderWidth=10)
Circle(325, 200, 10, fill='yellow')

# bow and arrow
### (HINT: The bow is defined as an arc!)
bow = Arc(100, 200, 50, 80, 0, 180, fill=None,
          border=gradient('saddleBrown', 'burlyWood', start='left'), borderWidth=5)

arrow = Line(50, 200, 150, 200, lineWidth=3, arrowEnd=True,
             fill=gradient('lightGrey', 'saddleBrown', start='right'))

def resetBowAndArrow():
    arrow.centerX = 100
    bow.width = 25
    leftArm.x2 = arrow.left
    rightArm.x2 = bow.right

def arrowToTarget():
    arrow.right = 325
    bow.startAngle = 0
    bow.sweepAngle = 180
    bow.width = 25
    rightArm.x2 = bow.right
    score.value += 10

def onMousePress(mouseX, mouseY):
    resetBowAndArrow()

def onMouseRelease(mouseX, mouseY):
    if (arrow.centerX < 150):
        arrowToTarget()

def onMouseDrag(mouseX, mouseY):
    if (bow.sweepAngle >= 125):
        # Pull back the arrow.
        # Move the arrow back and increase the startAngle of the bow by 1 pixel
        # each. Then decrease the sweepAngle of the bow and increase the width
        # of the bow.
        arrow.left -= 1
        bow.startAngle += 1
        bow.sweepAngle -= 2
        bow.width += 1
        # Moves the arms.
        leftArm.x2 = arrow.left
        rightArm.x2 = bow.right



