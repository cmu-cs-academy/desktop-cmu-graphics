# background
Rect(0, 0, 150, 400, fill='red', opacity=10)
Rect(250, 0, 150, 400, fill='blue', opacity=10)

# left person body
Oval(65, 275, 60, 120, fill='salmon')
Circle(65, 200, 20, fill='fireBrick')

# right person body
Oval(335, 275, 55, 120, fill='dodgerBlue')
Circle(335, 200, 20, fill='blue')

# rope
rope = Line(25, 270, 375, 270)
ropeCenter = RegularPolygon(200, 275, 10, 3, fill='red', rotateAngle=180)

# arms
leftPersonArm = Line(60, 255, 100, 275, fill='fireBrick', lineWidth=8)
rightPersonArm = Line(340, 255, 300, 275, fill='blue', lineWidth=8)

# header
header = Label('Tug of War!', 200, 50, size=30)
Label('Press a to pull', 65, 110)
Label('Press l to pull', 335, 110)

def onKeyPress(key):
    # Reset the header.
    header.value = 'Tug of War!'

    # Depending on the key pressed, pull the rope and move the arm.
    # If a key other than a or l is pressed, change the header value.
    if (key == 'a'):
        ropeCenter.centerX -= 10
        rope.centerX -= 10
        leftPersonArm.centerX -= 10
    elif (key == 'l'):
        ropeCenter.centerX += 10
        rope.centerX += 10
        rightPersonArm.centerX += 10
    else:
        header.value = 'Wrong Key!'

    # Check if either side wins and change the header value accordingly.
    if (ropeCenter.centerX < 150):
        header.value = 'Red wins!'
    elif (ropeCenter.centerX > 250):
        header.value = 'Blue wins!'

def onKeyRelease(key):
    # Move the arm back to original position.
    if (key == 'a'):
        leftPersonArm.centerX += 10
    elif (key == 'l'):
        rightPersonArm.centerX -= 10

onKeyPress('s')
onKeyPress('u')
onKeyPress('1')
onKeyPress('space')


# -
# background
Rect(0, 0, 150, 400, fill='red', opacity=10)
Rect(250, 0, 150, 400, fill='blue', opacity=10)

# left person body
Oval(65, 275, 60, 120, fill='salmon')
Circle(65, 200, 20, fill='fireBrick')

# right person body
Oval(335, 275, 55, 120, fill='dodgerBlue')
Circle(335, 200, 20, fill='blue')

# rope
rope = Line(25, 270, 375, 270)
ropeCenter = RegularPolygon(200, 275, 10, 3, fill='red', rotateAngle=180)

# arms
leftPersonArm = Line(60, 255, 100, 275, fill='fireBrick', lineWidth=8)
rightPersonArm = Line(340, 255, 300, 275, fill='blue', lineWidth=8)

# header
header = Label('Tug of War!', 200, 50, size=30)
Label('Press a to pull', 65, 110)
Label('Press l to pull', 335, 110)

def onKeyPress(key):
    # Reset the header.
    header.value = 'Tug of War!'

    # Depending on the key pressed, pull the rope and move the arm.
    # If a key other than a or l is pressed, change the header value.
    if (key == 'a'):
        ropeCenter.centerX -= 10
        rope.centerX -= 10
        leftPersonArm.centerX -= 10
    elif (key == 'l'):
        ropeCenter.centerX += 10
        rope.centerX += 10
        rightPersonArm.centerX += 10
    else:
        header.value = 'Wrong Key!'

    # Check if either side wins and change the header value accordingly.
    if (ropeCenter.centerX < 150):
        header.value = 'Red wins!'
    elif (ropeCenter.centerX > 250):
        header.value = 'Blue wins!'

def onKeyRelease(key):
    # Move the arm back to original position.
    if (key == 'a'):
        leftPersonArm.centerX += 10
    elif (key == 'l'):
        rightPersonArm.centerX -= 10

onKeyPress('a')
onKeyRelease('a')
onKeyPress('a')
onKeyRelease('a')
onKeyPress('a')
onKeyRelease('a')
onKeyPress('a')
onKeyRelease('a')
onKeyPress('a')
onKeyRelease('a')


# -
# background
Rect(0, 0, 150, 400, fill='red', opacity=10)
Rect(250, 0, 150, 400, fill='blue', opacity=10)

# left person body
Oval(65, 275, 60, 120, fill='salmon')
Circle(65, 200, 20, fill='fireBrick')

# right person body
Oval(335, 275, 55, 120, fill='dodgerBlue')
Circle(335, 200, 20, fill='blue')

# rope
rope = Line(25, 270, 375, 270)
ropeCenter = RegularPolygon(200, 275, 10, 3, fill='red', rotateAngle=180)

# arms
leftPersonArm = Line(60, 255, 100, 275, fill='fireBrick', lineWidth=8)
rightPersonArm = Line(340, 255, 300, 275, fill='blue', lineWidth=8)

# header
header = Label('Tug of War!', 200, 50, size=30)
Label('Press a to pull', 65, 110)
Label('Press l to pull', 335, 110)

def onKeyPress(key):
    # Reset the header.
    header.value = 'Tug of War!'

    # Depending on the key pressed, pull the rope and move the arm.
    # If a key other than a or l is pressed, change the header value.
    if (key == 'a'):
        ropeCenter.centerX -= 10
        rope.centerX -= 10
        leftPersonArm.centerX -= 10
    elif (key == 'l'):
        ropeCenter.centerX += 10
        rope.centerX += 10
        rightPersonArm.centerX += 10
    else:
        header.value = 'Wrong Key!'

    # Check if either side wins and change the header value accordingly.
    if (ropeCenter.centerX < 150):
        header.value = 'Red wins!'
    elif (ropeCenter.centerX > 250):
        header.value = 'Blue wins!'

def onKeyRelease(key):
    # Move the arm back to original position.
    if (key == 'a'):
        leftPersonArm.centerX += 10
    elif (key == 'l'):
        rightPersonArm.centerX -= 10

onKeyPress('l')

