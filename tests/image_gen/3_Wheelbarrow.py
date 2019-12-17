# sky
Rect(0, 0, 400, 225, fill=gradient('deepSkyBlue', 'lightCyan', start='top'))

# barn
Polygon(160, 150, 190, 85, 250, 50, 310, 85, 340, 150,
        fill=gradient('darkRed', 'crimson', start='left'),
        border='white', borderWidth=3)
Rect(160, 150, 180, 80, fill=gradient('darkRed', 'crimson', start='left'),
     border='white', borderWidth=3)

# barn door
Rect(250, 200, 80, 55, fill=None, border='white', align='center')
Line(250, 175, 250, 225, fill='white')
Line(210, 175, 250, 225, fill='white')
Line(290, 175, 250, 225, fill='white')
Line(210, 225, 250, 175, fill='white')
Line(290, 225, 250, 175, fill='white')

# windows
Rect(250, 100, 30, 35, border='white', borderWidth=3, align='center')
Rect(185, 180, 25, 30, border='white', borderWidth=3, align='center')
Rect(315, 180, 25, 30, border='white', borderWidth=3, align='center')

# grass
Rect(0, 225, 400, 175, fill=gradient('forestGreen', 'mediumSeaGreen', start='top'))

# sheep
Line(105, 355, 105, 380, lineWidth=4)
Line(150, 355, 150, 380, lineWidth=4)
Circle(105, 320, 20, fill='white', border='gainsboro')
Oval(75, 340, 45, 35, rotateAngle=-30)
Circle(70, 335, 3, fill='ghostWhite')
Circle(69, 336, 1)

# grass for the sheep
Line(50, 375, 45, 360, fill='darkGreen')
Line(53, 375, 55, 363, fill='darkGreen')
Line(51, 375, 50, 360, fill='darkGreen')

# wool
Circle(100, 340, 20, fill='white', border='gainsboro')
Circle(125, 350, 20, fill='white', border='gainsboro')
Circle(160, 345, 20, fill='white', border='gainsboro')
Circle(130, 310, 20, fill='white', border='gainsboro')
Circle(155, 315, 20, fill='white', border='gainsboro')
Circle(130, 330, 30, fill='white')

# wheelbarrow
wheel = Circle(110, 215, 12, fill=gradient('white', 'black', 'black'))
barrow = Polygon(45, 195, 40, 175, 120, 175, 95, 210,
                 fill=gradient('crimson', 'maroon', start='bottom'),
                 border='brown')
stand = Polygon(45, 200, 65, 205, 55, 225, fill=None,
                border='saddleBrown', borderWidth=3)
handle = Line(20, 190, 110, 215, fill='saddleBrown', lineWidth=4)

# person
head = Circle(70, 150, 10)
body = Line(70, 150, 70, 175)
arm = Line(70, 165, 90, 185)

def moveWheelbarrow(dx):
    head.centerX += dx
    body.centerX += dx
    arm.centerX += dx

    wheel.centerX += dx
    barrow.centerX += dx
    handle.centerX += dx
    stand.centerX += dx

def liftWheelbarrow():
    handle.y1 = 170

    head.centerY -= 8
    body.centerY -= 8
    arm.centerY -= 8

    barrow.angle = 10
    barrow.centerY -= 9
    stand.angle = 12
    stand.centerY -= 12

def placeWheelbarrow():
    handle.y1 = 190

    head.centerY += 8
    body.centerY += 8
    arm.centerY += 8

    barrow.centerX = handle.x1 + 60
    barrow.angle = 0
    barrow.centerY = 192

    stand.centerX = handle.x1 + 35
    stand.angle = 0
    stand.centerY = 212

def onKeyPress(key):
    # If the wheelbarrow is set down, only the up key will lift it up.
    if (handle.y1 == 190):
        if (key == 'up'):
            liftWheelbarrow()
    # Otherwise, left and right keys should move it horizontally, and the
    # down key should place it back down.
    else:
        if (key == 'down'):
            placeWheelbarrow()
        elif (key == 'right'):
            moveWheelbarrow(35)
        elif (key == 'left'):
            moveWheelbarrow(-35)



# -
# sky
Rect(0, 0, 400, 225, fill=gradient('deepSkyBlue', 'lightCyan', start='top'))

# barn
Polygon(160, 150, 190, 85, 250, 50, 310, 85, 340, 150,
        fill=gradient('darkRed', 'crimson', start='left'),
        border='white', borderWidth=3)
Rect(160, 150, 180, 80, fill=gradient('darkRed', 'crimson', start='left'),
     border='white', borderWidth=3)

# barn door
Rect(250, 200, 80, 55, fill=None, border='white', align='center')
Line(250, 175, 250, 225, fill='white')
Line(210, 175, 250, 225, fill='white')
Line(290, 175, 250, 225, fill='white')
Line(210, 225, 250, 175, fill='white')
Line(290, 225, 250, 175, fill='white')

# windows
Rect(250, 100, 30, 35, border='white', borderWidth=3, align='center')
Rect(185, 180, 25, 30, border='white', borderWidth=3, align='center')
Rect(315, 180, 25, 30, border='white', borderWidth=3, align='center')

# grass
Rect(0, 225, 400, 175, fill=gradient('forestGreen', 'mediumSeaGreen', start='top'))

# sheep
Line(105, 355, 105, 380, lineWidth=4)
Line(150, 355, 150, 380, lineWidth=4)
Circle(105, 320, 20, fill='white', border='gainsboro')
Oval(75, 340, 45, 35, rotateAngle=-30)
Circle(70, 335, 3, fill='ghostWhite')
Circle(69, 336, 1)

# grass for the sheep
Line(50, 375, 45, 360, fill='darkGreen')
Line(53, 375, 55, 363, fill='darkGreen')
Line(51, 375, 50, 360, fill='darkGreen')

# wool
Circle(100, 340, 20, fill='white', border='gainsboro')
Circle(125, 350, 20, fill='white', border='gainsboro')
Circle(160, 345, 20, fill='white', border='gainsboro')
Circle(130, 310, 20, fill='white', border='gainsboro')
Circle(155, 315, 20, fill='white', border='gainsboro')
Circle(130, 330, 30, fill='white')

# wheelbarrow
wheel = Circle(110, 215, 12, fill=gradient('white', 'black', 'black'))
barrow = Polygon(45, 195, 40, 175, 120, 175, 95, 210,
                 fill=gradient('crimson', 'maroon', start='bottom'),
                 border='brown')
stand = Polygon(45, 200, 65, 205, 55, 225, fill=None,
                border='saddleBrown', borderWidth=3)
handle = Line(20, 190, 110, 215, fill='saddleBrown', lineWidth=4)

# person
head = Circle(70, 150, 10)
body = Line(70, 150, 70, 175)
arm = Line(70, 165, 90, 185)

def moveWheelbarrow(dx):
    head.centerX += dx
    body.centerX += dx
    arm.centerX += dx

    wheel.centerX += dx
    barrow.centerX += dx
    handle.centerX += dx
    stand.centerX += dx

def liftWheelbarrow():
    handle.y1 = 170

    head.centerY -= 8
    body.centerY -= 8
    arm.centerY -= 8

    barrow.angle = 10
    barrow.centerY -= 9
    stand.angle = 12
    stand.centerY -= 12

def placeWheelbarrow():
    handle.y1 = 190

    head.centerY += 8
    body.centerY += 8
    arm.centerY += 8

    barrow.centerX = handle.x1 + 60
    barrow.angle = 0
    barrow.centerY = 192

    stand.centerX = handle.x1 + 35
    stand.angle = 0
    stand.centerY = 212

def onKeyPress(key):
    # If the wheelbarrow is set down, only the up key will lift it up.
    if (handle.y1 == 190):
        if (key == 'up'):
            liftWheelbarrow()
    # Otherwise, left and right keys should move it horizontally, and the
    # down key should place it back down.
    else:
        if (key == 'down'):
            placeWheelbarrow()
        elif (key == 'right'):
            moveWheelbarrow(35)
        elif (key == 'left'):
            moveWheelbarrow(-35)

onKeyPress('up')
onKeyPress('left')
onKeyPress('left')


# -
# sky
Rect(0, 0, 400, 225, fill=gradient('deepSkyBlue', 'lightCyan', start='top'))

# barn
Polygon(160, 150, 190, 85, 250, 50, 310, 85, 340, 150,
        fill=gradient('darkRed', 'crimson', start='left'),
        border='white', borderWidth=3)
Rect(160, 150, 180, 80, fill=gradient('darkRed', 'crimson', start='left'),
     border='white', borderWidth=3)

# barn door
Rect(250, 200, 80, 55, fill=None, border='white', align='center')
Line(250, 175, 250, 225, fill='white')
Line(210, 175, 250, 225, fill='white')
Line(290, 175, 250, 225, fill='white')
Line(210, 225, 250, 175, fill='white')
Line(290, 225, 250, 175, fill='white')

# windows
Rect(250, 100, 30, 35, border='white', borderWidth=3, align='center')
Rect(185, 180, 25, 30, border='white', borderWidth=3, align='center')
Rect(315, 180, 25, 30, border='white', borderWidth=3, align='center')

# grass
Rect(0, 225, 400, 175, fill=gradient('forestGreen', 'mediumSeaGreen', start='top'))

# sheep
Line(105, 355, 105, 380, lineWidth=4)
Line(150, 355, 150, 380, lineWidth=4)
Circle(105, 320, 20, fill='white', border='gainsboro')
Oval(75, 340, 45, 35, rotateAngle=-30)
Circle(70, 335, 3, fill='ghostWhite')
Circle(69, 336, 1)

# grass for the sheep
Line(50, 375, 45, 360, fill='darkGreen')
Line(53, 375, 55, 363, fill='darkGreen')
Line(51, 375, 50, 360, fill='darkGreen')

# wool
Circle(100, 340, 20, fill='white', border='gainsboro')
Circle(125, 350, 20, fill='white', border='gainsboro')
Circle(160, 345, 20, fill='white', border='gainsboro')
Circle(130, 310, 20, fill='white', border='gainsboro')
Circle(155, 315, 20, fill='white', border='gainsboro')
Circle(130, 330, 30, fill='white')

# wheelbarrow
wheel = Circle(110, 215, 12, fill=gradient('white', 'black', 'black'))
barrow = Polygon(45, 195, 40, 175, 120, 175, 95, 210,
                 fill=gradient('crimson', 'maroon', start='bottom'),
                 border='brown')
stand = Polygon(45, 200, 65, 205, 55, 225, fill=None,
                border='saddleBrown', borderWidth=3)
handle = Line(20, 190, 110, 215, fill='saddleBrown', lineWidth=4)

# person
head = Circle(70, 150, 10)
body = Line(70, 150, 70, 175)
arm = Line(70, 165, 90, 185)

def moveWheelbarrow(dx):
    head.centerX += dx
    body.centerX += dx
    arm.centerX += dx

    wheel.centerX += dx
    barrow.centerX += dx
    handle.centerX += dx
    stand.centerX += dx

def liftWheelbarrow():
    handle.y1 = 170

    head.centerY -= 8
    body.centerY -= 8
    arm.centerY -= 8

    barrow.angle = 10
    barrow.centerY -= 9
    stand.angle = 12
    stand.centerY -= 12

def placeWheelbarrow():
    handle.y1 = 190

    head.centerY += 8
    body.centerY += 8
    arm.centerY += 8

    barrow.centerX = handle.x1 + 60
    barrow.angle = 0
    barrow.centerY = 192

    stand.centerX = handle.x1 + 35
    stand.angle = 0
    stand.centerY = 212

def onKeyPress(key):
    # If the wheelbarrow is set down, only the up key will lift it up.
    if (handle.y1 == 190):
        if (key == 'up'):
            liftWheelbarrow()
    # Otherwise, left and right keys should move it horizontally, and the
    # down key should place it back down.
    else:
        if (key == 'down'):
            placeWheelbarrow()
        elif (key == 'right'):
            moveWheelbarrow(35)
        elif (key == 'left'):
            moveWheelbarrow(-35)

onKeyPress('up')
onKeyPress('up')

