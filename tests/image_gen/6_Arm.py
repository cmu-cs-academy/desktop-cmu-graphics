app.background = gradient('black', 'midnightBlue', start='left-top')

# Randomly draws 40 stars.
for i in range(40):
    Circle(randrange(0, 400), randrange(0, 400), 1, fill='white', opacity=50)

# astronaut
astronaut = Group(
    Rect(180, 205, 40, 40, fill='darkGray'),
    Circle(200, 200, 15, fill='white'),
    Rect(185, 215, 30, 40, fill='white'),
    Rect(175, 215, 50, 12, fill='white'),
    Rect(190, 193, 20, 14, fill='steelBlue'),
    Line(200, 240, 200, 255),
    Rect(195, 222, 10, 10, fill='gray'),
    Rect(180, 215, 3, 12, fill='fireBrick'),
    Rect(217, 215, 3, 12, fill='fireBrick')
    )
astronaut.centerX = 90
astronaut.centerY = 70
astronaut.rotateAngle = 20

# satellite
Rect(220, 250, 130, 200, fill=gradient('darkGray', 'dimGray', start='left'),
     rotateAngle=330)
Line(110, 330, 360, 190, fill='dimGray', lineWidth=5)
Oval(234, 262, 130, 50, rotateAngle=330,
     fill=gradient('darkGray', 'dimGray', start='right-bottom'))
Oval(110, 330, 130, 50, fill=gradient('peru', 'chocolate'), rotateAngle=330)
Oval(360, 190, 130, 50, fill=gradient('peru', 'chocolate'), rotateAngle=330)

# arm
firstArm = Line(235, 260, 180, 180, fill='white', lineWidth=30)
secondArm = Line(180, 180, 250, 100, fill='white', lineWidth=30)
firstArmPivot = Circle(180, 180, 15, fill='silver')
secondArmPivot = Circle(250, 100, 15, fill='silver')
Circle(235, 260, 15, fill='gray')

def turnArm(arm, angle, x1, y1):
    # Find the x2, y2 for each arm using the parameters provided.
    newX2, newY2 = getPointInDir(x1, y1, angle, 100)
    # Sets the new values of the arm.
    arm.x2 = newX2
    arm.y2 = newY2

def onMouseMove(mouseX, mouseY):
    # Set scale to be 360 divided by 400.
    scale = 360 / 400
    # Set the firstArmAngle to be the mouseX times scale and fix the arguments
    # to the turnArm function to properly turn the first arm.
    firstArmAngle = mouseX * scale
    turnArm(firstArm, firstArmAngle, 235, 260)
    # Similarly, set secondArmAngle but use mouseY and fix the arguments
    # to the turnArm function to properly turn the second arm.
    secondArmAngle = mouseY * scale
    turnArm(secondArm, secondArmAngle, firstArm.x2, firstArm.y2)
    # Moves the arm pivots to the new value
    firstArmPivot.centerX = firstArm.x2
    firstArmPivot.centerY = firstArm.y2
    secondArmPivot.centerX = secondArm.x2
    secondArmPivot.centerY = secondArm.y2

    secondArm.x1 = firstArm.x2
    secondArm.y1 = firstArm.y2



# -
app.background = gradient('black', 'midnightBlue', start='left-top')

# Randomly draws 40 stars.
for i in range(40):
    Circle(randrange(0, 400), randrange(0, 400), 1, fill='white', opacity=50)

# astronaut
astronaut = Group(
    Rect(180, 205, 40, 40, fill='darkGray'),
    Circle(200, 200, 15, fill='white'),
    Rect(185, 215, 30, 40, fill='white'),
    Rect(175, 215, 50, 12, fill='white'),
    Rect(190, 193, 20, 14, fill='steelBlue'),
    Line(200, 240, 200, 255),
    Rect(195, 222, 10, 10, fill='gray'),
    Rect(180, 215, 3, 12, fill='fireBrick'),
    Rect(217, 215, 3, 12, fill='fireBrick')
    )
astronaut.centerX = 90
astronaut.centerY = 70
astronaut.rotateAngle = 20

# satellite
Rect(220, 250, 130, 200, fill=gradient('darkGray', 'dimGray', start='left'),
     rotateAngle=330)
Line(110, 330, 360, 190, fill='dimGray', lineWidth=5)
Oval(234, 262, 130, 50, rotateAngle=330,
     fill=gradient('darkGray', 'dimGray', start='right-bottom'))
Oval(110, 330, 130, 50, fill=gradient('peru', 'chocolate'), rotateAngle=330)
Oval(360, 190, 130, 50, fill=gradient('peru', 'chocolate'), rotateAngle=330)

# arm
firstArm = Line(235, 260, 180, 180, fill='white', lineWidth=30)
secondArm = Line(180, 180, 250, 100, fill='white', lineWidth=30)
firstArmPivot = Circle(180, 180, 15, fill='silver')
secondArmPivot = Circle(250, 100, 15, fill='silver')
Circle(235, 260, 15, fill='gray')

def turnArm(arm, angle, x1, y1):
    # Find the x2, y2 for each arm using the parameters provided.
    newX2, newY2 = getPointInDir(x1, y1, angle, 100)
    # Sets the new values of the arm.
    arm.x2 = newX2
    arm.y2 = newY2

def onMouseMove(mouseX, mouseY):
    # Set scale to be 360 divided by 400.
    scale = 360 / 400
    # Set the firstArmAngle to be the mouseX times scale and fix the arguments
    # to the turnArm function to properly turn the first arm.
    firstArmAngle = mouseX * scale
    turnArm(firstArm, firstArmAngle, 235, 260)
    # Similarly, set secondArmAngle but use mouseY and fix the arguments
    # to the turnArm function to properly turn the second arm.
    secondArmAngle = mouseY * scale
    turnArm(secondArm, secondArmAngle, firstArm.x2, firstArm.y2)
    # Moves the arm pivots to the new value
    firstArmPivot.centerX = firstArm.x2
    firstArmPivot.centerY = firstArm.y2
    secondArmPivot.centerX = secondArm.x2
    secondArmPivot.centerY = secondArm.y2

    secondArm.x1 = firstArm.x2
    secondArm.y1 = firstArm.y2

onMouseMove(50, 300)


# -
app.background = gradient('black', 'midnightBlue', start='left-top')

# Randomly draws 40 stars.
for i in range(40):
    Circle(randrange(0, 400), randrange(0, 400), 1, fill='white', opacity=50)

# astronaut
astronaut = Group(
    Rect(180, 205, 40, 40, fill='darkGray'),
    Circle(200, 200, 15, fill='white'),
    Rect(185, 215, 30, 40, fill='white'),
    Rect(175, 215, 50, 12, fill='white'),
    Rect(190, 193, 20, 14, fill='steelBlue'),
    Line(200, 240, 200, 255),
    Rect(195, 222, 10, 10, fill='gray'),
    Rect(180, 215, 3, 12, fill='fireBrick'),
    Rect(217, 215, 3, 12, fill='fireBrick')
    )
astronaut.centerX = 90
astronaut.centerY = 70
astronaut.rotateAngle = 20

# satellite
Rect(220, 250, 130, 200, fill=gradient('darkGray', 'dimGray', start='left'),
     rotateAngle=330)
Line(110, 330, 360, 190, fill='dimGray', lineWidth=5)
Oval(234, 262, 130, 50, rotateAngle=330,
     fill=gradient('darkGray', 'dimGray', start='right-bottom'))
Oval(110, 330, 130, 50, fill=gradient('peru', 'chocolate'), rotateAngle=330)
Oval(360, 190, 130, 50, fill=gradient('peru', 'chocolate'), rotateAngle=330)

# arm
firstArm = Line(235, 260, 180, 180, fill='white', lineWidth=30)
secondArm = Line(180, 180, 250, 100, fill='white', lineWidth=30)
firstArmPivot = Circle(180, 180, 15, fill='silver')
secondArmPivot = Circle(250, 100, 15, fill='silver')
Circle(235, 260, 15, fill='gray')

def turnArm(arm, angle, x1, y1):
    # Find the x2, y2 for each arm using the parameters provided.
    newX2, newY2 = getPointInDir(x1, y1, angle, 100)
    # Sets the new values of the arm.
    arm.x2 = newX2
    arm.y2 = newY2

def onMouseMove(mouseX, mouseY):
    # Set scale to be 360 divided by 400.
    scale = 360 / 400
    # Set the firstArmAngle to be the mouseX times scale and fix the arguments
    # to the turnArm function to properly turn the first arm.
    firstArmAngle = mouseX * scale
    turnArm(firstArm, firstArmAngle, 235, 260)
    # Similarly, set secondArmAngle but use mouseY and fix the arguments
    # to the turnArm function to properly turn the second arm.
    secondArmAngle = mouseY * scale
    turnArm(secondArm, secondArmAngle, firstArm.x2, firstArm.y2)
    # Moves the arm pivots to the new value
    firstArmPivot.centerX = firstArm.x2
    firstArmPivot.centerY = firstArm.y2
    secondArmPivot.centerX = secondArm.x2
    secondArmPivot.centerY = secondArm.y2

    secondArm.x1 = firstArm.x2
    secondArm.y1 = firstArm.y2


