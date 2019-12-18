# background
app.background = gradient('deepSkyBlue', 'white', 'forestGreen', start='top')

Oval(390, 90, 400, 150, fill=gradient('snow', 'white', start='bottom'))
Oval(205, 315, 400, 150, fill=rgb(185, 245, 150))

# swing set top bar
Line(110, 98, 330, 113, fill=gradient('saddleBrown', 'sienna', 'saddleBrown',
                                      start='left'), lineWidth=10)

# swing set left side
Line(115, 100, 140, 270, fill='saddleBrown', lineWidth=10)
Line(115, 100, 65, 320, fill=gradient('saddleBrown', 'sienna', start='bottom'),
     lineWidth=10)

# ropes and seat
leftRope = Line(175, 105, 175, 260)
seat = Line(175, 260, 225, 270, fill=gradient('red', 'fireBrick'), lineWidth=15)
rightRope = Line(225, 110, 225, 270)

# swing set right side
Line(325, 115, 355, 330, fill='saddleBrown', lineWidth=10)
Line(325, 115, 290, 365, fill=gradient('saddleBrown', 'sienna', start='bottom'),
     lineWidth=10)

def onMouseMove(mouseX, mouseY):
    # First update the seat location with mouseX and mouseY.
    seat.centerX = mouseX
    seat.centerY = mouseY

    # Then change properties of the leftRope and rightRope with respect to
    # the seat.
    leftRope.x2 = seat.x1
    leftRope.y2 = seat.y1

    rightRope.x2 = seat.x2
    rightRope.y2 = seat.y2



# -
# background
app.background = gradient('deepSkyBlue', 'white', 'forestGreen', start='top')

Oval(390, 90, 400, 150, fill=gradient('snow', 'white', start='bottom'))
Oval(205, 315, 400, 150, fill=rgb(185, 245, 150))

# swing set top bar
Line(110, 98, 330, 113, fill=gradient('saddleBrown', 'sienna', 'saddleBrown',
                                      start='left'), lineWidth=10)

# swing set left side
Line(115, 100, 140, 270, fill='saddleBrown', lineWidth=10)
Line(115, 100, 65, 320, fill=gradient('saddleBrown', 'sienna', start='bottom'),
     lineWidth=10)

# ropes and seat
leftRope = Line(175, 105, 175, 260)
seat = Line(175, 260, 225, 270, fill=gradient('red', 'fireBrick'), lineWidth=15)
rightRope = Line(225, 110, 225, 270)

# swing set right side
Line(325, 115, 355, 330, fill='saddleBrown', lineWidth=10)
Line(325, 115, 290, 365, fill=gradient('saddleBrown', 'sienna', start='bottom'),
     lineWidth=10)

def onMouseMove(mouseX, mouseY):
    # First update the seat location with mouseX and mouseY.
    seat.centerX = mouseX
    seat.centerY = mouseY

    # Then change properties of the leftRope and rightRope with respect to
    # the seat.
    leftRope.x2 = seat.x1
    leftRope.y2 = seat.y1

    rightRope.x2 = seat.x2
    rightRope.y2 = seat.y2

onMouseMove(240, 360)


# -
# background
app.background = gradient('deepSkyBlue', 'white', 'forestGreen', start='top')

Oval(390, 90, 400, 150, fill=gradient('snow', 'white', start='bottom'))
Oval(205, 315, 400, 150, fill=rgb(185, 245, 150))

# swing set top bar
Line(110, 98, 330, 113, fill=gradient('saddleBrown', 'sienna', 'saddleBrown',
                                      start='left'), lineWidth=10)

# swing set left side
Line(115, 100, 140, 270, fill='saddleBrown', lineWidth=10)
Line(115, 100, 65, 320, fill=gradient('saddleBrown', 'sienna', start='bottom'),
     lineWidth=10)

# ropes and seat
leftRope = Line(175, 105, 175, 260)
seat = Line(175, 260, 225, 270, fill=gradient('red', 'fireBrick'), lineWidth=15)
rightRope = Line(225, 110, 225, 270)

# swing set right side
Line(325, 115, 355, 330, fill='saddleBrown', lineWidth=10)
Line(325, 115, 290, 365, fill=gradient('saddleBrown', 'sienna', start='bottom'),
     lineWidth=10)

def onMouseMove(mouseX, mouseY):
    # First update the seat location with mouseX and mouseY.
    seat.centerX = mouseX
    seat.centerY = mouseY

    # Then change properties of the leftRope and rightRope with respect to
    # the seat.
    leftRope.x2 = seat.x1
    leftRope.y2 = seat.y1

    rightRope.x2 = seat.x2
    rightRope.y2 = seat.y2


