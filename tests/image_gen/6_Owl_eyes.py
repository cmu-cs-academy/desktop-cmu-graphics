app.background = 'slateGray'

# branch
Polygon(0, 380, 400, 360, 300, 380, 0, 400)

# body
Oval(200, 260, 280, 220, fill='tan')
Oval(200, 300, 200, 140, fill='wheat')

# wings
Oval(80, 265, 60, 130, fill='sienna', rotateAngle=10)
Oval(330, 265, 60, 130, fill='sienna', rotateAngle=-10)

# ear
Polygon(275, 60, 320, 20, 340, 110, fill='saddleBrown')
Polygon(125, 60, 80, 20, 60, 110, fill='saddleBrown')

# face
Oval(200, 150, 300, 220, fill='saddleBrown')
Circle(130, 150, 80, fill='tan')
Circle(270, 150, 80, fill='tan')
Oval(140, 140, 100, 120, fill='white')
Oval(260, 140, 100, 120, fill='white')

# feet
Polygon(135, 350, 145, 350, 155, 380, 145, 370, 140, 380, 135, 370, 125, 380,
        fill='sandyBrown')
Polygon(265, 350, 255, 350, 245, 380, 255, 370, 260, 380, 265, 370, 275, 380,
        fill='sandyBrown')

# nose
nose = Polygon(215, 170, 200, 210, 185, 170, fill='orange')

# eyes
Circle(150, 130, 35)
Circle(250, 130, 35)

leftEye = Circle(150, 130, 10, fill='white')
rightEye = Circle(250, 130, 10, fill='white')

def onMouseMove(mouseX, mouseY):
    # Move the centerX of the eyes to follow the mouse, but scale the movement
    # so that the iris stays in the eye!
    ### Fix Your Code Here ###
    leftEye.centerX = 130 + (mouseX / 10)
    leftEye.centerY = 110 + (mouseY / 10)
    rightEye.centerX = 230 + (mouseX / 10)
    rightEye.centerY = 110 + (mouseY / 10)

onMouseMove(330, 80)
onMouseMove(140, 160)


# -
app.background = 'slateGray'

# branch
Polygon(0, 380, 400, 360, 300, 380, 0, 400)

# body
Oval(200, 260, 280, 220, fill='tan')
Oval(200, 300, 200, 140, fill='wheat')

# wings
Oval(80, 265, 60, 130, fill='sienna', rotateAngle=10)
Oval(330, 265, 60, 130, fill='sienna', rotateAngle=-10)

# ear
Polygon(275, 60, 320, 20, 340, 110, fill='saddleBrown')
Polygon(125, 60, 80, 20, 60, 110, fill='saddleBrown')

# face
Oval(200, 150, 300, 220, fill='saddleBrown')
Circle(130, 150, 80, fill='tan')
Circle(270, 150, 80, fill='tan')
Oval(140, 140, 100, 120, fill='white')
Oval(260, 140, 100, 120, fill='white')

# feet
Polygon(135, 350, 145, 350, 155, 380, 145, 370, 140, 380, 135, 370, 125, 380,
        fill='sandyBrown')
Polygon(265, 350, 255, 350, 245, 380, 255, 370, 260, 380, 265, 370, 275, 380,
        fill='sandyBrown')

# nose
nose = Polygon(215, 170, 200, 210, 185, 170, fill='orange')

# eyes
Circle(150, 130, 35)
Circle(250, 130, 35)

leftEye = Circle(150, 130, 10, fill='white')
rightEye = Circle(250, 130, 10, fill='white')

def onMouseMove(mouseX, mouseY):
    # Move the centerX of the eyes to follow the mouse, but scale the movement
    # so that the iris stays in the eye!
    ### Fix Your Code Here ###
    leftEye.centerX = 130 + (mouseX / 10)
    leftEye.centerY = 110 + (mouseY / 10)
    rightEye.centerX = 230 + (mouseX / 10)
    rightEye.centerY = 110 + (mouseY / 10)

onMouseMove(370, 250)


# -
app.background = 'slateGray'

# branch
Polygon(0, 380, 400, 360, 300, 380, 0, 400)

# body
Oval(200, 260, 280, 220, fill='tan')
Oval(200, 300, 200, 140, fill='wheat')

# wings
Oval(80, 265, 60, 130, fill='sienna', rotateAngle=10)
Oval(330, 265, 60, 130, fill='sienna', rotateAngle=-10)

# ear
Polygon(275, 60, 320, 20, 340, 110, fill='saddleBrown')
Polygon(125, 60, 80, 20, 60, 110, fill='saddleBrown')

# face
Oval(200, 150, 300, 220, fill='saddleBrown')
Circle(130, 150, 80, fill='tan')
Circle(270, 150, 80, fill='tan')
Oval(140, 140, 100, 120, fill='white')
Oval(260, 140, 100, 120, fill='white')

# feet
Polygon(135, 350, 145, 350, 155, 380, 145, 370, 140, 380, 135, 370, 125, 380,
        fill='sandyBrown')
Polygon(265, 350, 255, 350, 245, 380, 255, 370, 260, 380, 265, 370, 275, 380,
        fill='sandyBrown')

# nose
nose = Polygon(215, 170, 200, 210, 185, 170, fill='orange')

# eyes
Circle(150, 130, 35)
Circle(250, 130, 35)

leftEye = Circle(150, 130, 10, fill='white')
rightEye = Circle(250, 130, 10, fill='white')

def onMouseMove(mouseX, mouseY):
    # Move the centerX of the eyes to follow the mouse, but scale the movement
    # so that the iris stays in the eye!
    ### Fix Your Code Here ###
    leftEye.centerX = 130 + (mouseX / 10)
    leftEye.centerY = 110 + (mouseY / 10)
    rightEye.centerX = 230 + (mouseX / 10)
    rightEye.centerY = 110 + (mouseY / 10)

onMouseMove(100, 100)

