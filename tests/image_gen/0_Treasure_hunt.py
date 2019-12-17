app.background = 'lightSkyBlue'

# islands
Oval(270, 140, 200, 100, fill='wheat', rotateAngle=25)
Oval(150, 270, 180, 150, fill='wheat', rotateAngle=15)
Oval(200, 200, 250, 180, fill='mediumAquamarine', border='wheat', borderWidth=20)
Oval(265, 145, 140, 60, fill='mediumAquamarine', rotateAngle=25)
Oval(155, 265, 140, 110, fill='mediumAquamarine', rotateAngle=15)
Oval(50, 5, 200, 150, fill='mediumAquamarine', border='wheat', borderWidth=20)

# boat
Arc(330, 330, 70, 50, 90, 180, fill='sienna')
RegularPolygon(330, 310, 25, 3, fill='white')
Line(330, 285, 330, 330, fill='saddleBrown', lineWidth=3)
Star(330, 400, 53, 20, fill='lightSkyBlue', roundness=95)

# treasure
Line(200, 110, 230, 140, fill='crimson', lineWidth=8)
Line(200, 140, 230, 110, fill='crimson', lineWidth=8)
Line(190, 140, 180, 150, fill='crimson', lineWidth=3)
Line(175, 155, 170, 170, fill='crimson', lineWidth=3)
Line(170, 175, 180, 190, fill='crimson', lineWidth=3)
Line(185, 195, 190, 215, fill='crimson', lineWidth=3)
Line(190, 220, 205, 235, fill='crimson', lineWidth=3)
Line(210, 240, 220, 255, fill='crimson', lineWidth=3)
Line(225, 260, 245, 270, fill='crimson', lineWidth=3)
Line(250, 273, 270, 288, fill='crimson', lineWidth=3)
Line(180, 215, 160, 215, fill='crimson', lineWidth=3)
Line(155, 220, 145, 240, fill='crimson', lineWidth=3)
Line(145, 245, 165, 260, fill='crimson', lineWidth=3)
Line(170, 260, 185, 250, fill='crimson', lineWidth=3)
Line(185, 245, 185, 225, fill='crimson', lineWidth=3)

xLabel = Label('x = ' + str(0), 0, 0, size=20, bold=True)
yLabel = Label('y = ' + str(20), 0, 20, size=20, bold=True)

message = Label('You are very cold.', 200, 20, size=15, bold=True)

def onMouseMove(mouseX, mouseY):
    # Set the x label's position and value using mouseX and mouseY.
    xLabel.centerX = mouseX
    xLabel.centerY = mouseY
    xLabel.value = 'x = ' + str(mouseX)
    # Set the y label's position and value using mouseX and mouseY.
    yLabel.centerX = mouseX
    yLabel.centerY = mouseY + 20
    yLabel.value = 'y = ' + str(mouseY)
    if (distance(mouseX, mouseY, 215, 125) <= 25):
        message.value = 'You are very close!!!'
    elif (distance(mouseX, mouseY, 215, 125) <= 100):
        message.value = 'Getting warmer!'
    else:
        message.value = 'You are very cold.'

onMouseMove(320, 250)


# -
app.background = 'lightSkyBlue'

# islands
Oval(270, 140, 200, 100, fill='wheat', rotateAngle=25)
Oval(150, 270, 180, 150, fill='wheat', rotateAngle=15)
Oval(200, 200, 250, 180, fill='mediumAquamarine', border='wheat', borderWidth=20)
Oval(265, 145, 140, 60, fill='mediumAquamarine', rotateAngle=25)
Oval(155, 265, 140, 110, fill='mediumAquamarine', rotateAngle=15)
Oval(50, 5, 200, 150, fill='mediumAquamarine', border='wheat', borderWidth=20)

# boat
Arc(330, 330, 70, 50, 90, 180, fill='sienna')
RegularPolygon(330, 310, 25, 3, fill='white')
Line(330, 285, 330, 330, fill='saddleBrown', lineWidth=3)
Star(330, 400, 53, 20, fill='lightSkyBlue', roundness=95)

# treasure
Line(200, 110, 230, 140, fill='crimson', lineWidth=8)
Line(200, 140, 230, 110, fill='crimson', lineWidth=8)
Line(190, 140, 180, 150, fill='crimson', lineWidth=3)
Line(175, 155, 170, 170, fill='crimson', lineWidth=3)
Line(170, 175, 180, 190, fill='crimson', lineWidth=3)
Line(185, 195, 190, 215, fill='crimson', lineWidth=3)
Line(190, 220, 205, 235, fill='crimson', lineWidth=3)
Line(210, 240, 220, 255, fill='crimson', lineWidth=3)
Line(225, 260, 245, 270, fill='crimson', lineWidth=3)
Line(250, 273, 270, 288, fill='crimson', lineWidth=3)
Line(180, 215, 160, 215, fill='crimson', lineWidth=3)
Line(155, 220, 145, 240, fill='crimson', lineWidth=3)
Line(145, 245, 165, 260, fill='crimson', lineWidth=3)
Line(170, 260, 185, 250, fill='crimson', lineWidth=3)
Line(185, 245, 185, 225, fill='crimson', lineWidth=3)

xLabel = Label('x = ' + str(0), 0, 0, size=20, bold=True)
yLabel = Label('y = ' + str(20), 0, 20, size=20, bold=True)

message = Label('You are very cold.', 200, 20, size=15, bold=True)

def onMouseMove(mouseX, mouseY):
    # Set the x label's position and value using mouseX and mouseY.
    xLabel.centerX = mouseX
    xLabel.centerY = mouseY
    xLabel.value = 'x = ' + str(mouseX)
    # Set the y label's position and value using mouseX and mouseY.
    yLabel.centerX = mouseX
    yLabel.centerY = mouseY + 20
    yLabel.value = 'y = ' + str(mouseY)
    if (distance(mouseX, mouseY, 215, 125) <= 25):
        message.value = 'You are very close!!!'
    elif (distance(mouseX, mouseY, 215, 125) <= 100):
        message.value = 'Getting warmer!'
    else:
        message.value = 'You are very cold.'

onMouseMove(200, 190)


# -
app.background = 'lightSkyBlue'

# islands
Oval(270, 140, 200, 100, fill='wheat', rotateAngle=25)
Oval(150, 270, 180, 150, fill='wheat', rotateAngle=15)
Oval(200, 200, 250, 180, fill='mediumAquamarine', border='wheat', borderWidth=20)
Oval(265, 145, 140, 60, fill='mediumAquamarine', rotateAngle=25)
Oval(155, 265, 140, 110, fill='mediumAquamarine', rotateAngle=15)
Oval(50, 5, 200, 150, fill='mediumAquamarine', border='wheat', borderWidth=20)

# boat
Arc(330, 330, 70, 50, 90, 180, fill='sienna')
RegularPolygon(330, 310, 25, 3, fill='white')
Line(330, 285, 330, 330, fill='saddleBrown', lineWidth=3)
Star(330, 400, 53, 20, fill='lightSkyBlue', roundness=95)

# treasure
Line(200, 110, 230, 140, fill='crimson', lineWidth=8)
Line(200, 140, 230, 110, fill='crimson', lineWidth=8)
Line(190, 140, 180, 150, fill='crimson', lineWidth=3)
Line(175, 155, 170, 170, fill='crimson', lineWidth=3)
Line(170, 175, 180, 190, fill='crimson', lineWidth=3)
Line(185, 195, 190, 215, fill='crimson', lineWidth=3)
Line(190, 220, 205, 235, fill='crimson', lineWidth=3)
Line(210, 240, 220, 255, fill='crimson', lineWidth=3)
Line(225, 260, 245, 270, fill='crimson', lineWidth=3)
Line(250, 273, 270, 288, fill='crimson', lineWidth=3)
Line(180, 215, 160, 215, fill='crimson', lineWidth=3)
Line(155, 220, 145, 240, fill='crimson', lineWidth=3)
Line(145, 245, 165, 260, fill='crimson', lineWidth=3)
Line(170, 260, 185, 250, fill='crimson', lineWidth=3)
Line(185, 245, 185, 225, fill='crimson', lineWidth=3)

xLabel = Label('x = ' + str(0), 0, 0, size=20, bold=True)
yLabel = Label('y = ' + str(20), 0, 20, size=20, bold=True)

message = Label('You are very cold.', 200, 20, size=15, bold=True)

def onMouseMove(mouseX, mouseY):
    # Set the x label's position and value using mouseX and mouseY.
    xLabel.centerX = mouseX
    xLabel.centerY = mouseY
    xLabel.value = 'x = ' + str(mouseX)
    # Set the y label's position and value using mouseX and mouseY.
    yLabel.centerX = mouseX
    yLabel.centerY = mouseY + 20
    yLabel.value = 'y = ' + str(mouseY)
    if (distance(mouseX, mouseY, 215, 125) <= 25):
        message.value = 'You are very close!!!'
    elif (distance(mouseX, mouseY, 215, 125) <= 100):
        message.value = 'Getting warmer!'
    else:
        message.value = 'You are very cold.'


