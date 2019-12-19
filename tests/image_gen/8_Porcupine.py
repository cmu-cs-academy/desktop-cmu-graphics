app.background = 'cornflowerBlue'

spikes = Star(200, 335, 130, 30, fill='saddleBrown', roundness=80)

# body
Circle(140, 330, 15, fill='navajoWhite', border='tan', borderWidth=5)
Circle(260, 330, 15, fill='navajoWhite', border='tan', borderWidth=5)
Oval(200, 310, 160, 110, fill='tan', align='top')

# eyes
Circle(175, 360, 7)
Circle(225, 360, 7)

# nose
RegularPolygon(200, 390, 15, 3, rotateAngle=180)

leftEyebrow = Line(155, 345, 170, 345, rotateAngle=-15)
rightEyebrow = Line(245, 345, 230, 345, rotateAngle=15)

def onMouseMove(mouseX, mouseY):
    # If the mouse is on the porcupine, puff out the spikes and change the
    # eyebrows.
    if (spikes.contains(mouseX, mouseY) == True):
        spikes.radius = 250
        spikes.roundness = 40
        leftEyebrow.rotateAngle = 30
        rightEyebrow.rotateAngle = -30
    else:
        spikes.radius = 130
        spikes.roundness = 80
        leftEyebrow.rotateAngle = -15
        rightEyebrow.rotateAngle = 15



# -
app.background = 'cornflowerBlue'

spikes = Star(200, 335, 130, 30, fill='saddleBrown', roundness=80)

# body
Circle(140, 330, 15, fill='navajoWhite', border='tan', borderWidth=5)
Circle(260, 330, 15, fill='navajoWhite', border='tan', borderWidth=5)
Oval(200, 310, 160, 110, fill='tan', align='top')

# eyes
Circle(175, 360, 7)
Circle(225, 360, 7)

# nose
RegularPolygon(200, 390, 15, 3, rotateAngle=180)

leftEyebrow = Line(155, 345, 170, 345, rotateAngle=-15)
rightEyebrow = Line(245, 345, 230, 345, rotateAngle=15)

def onMouseMove(mouseX, mouseY):
    # If the mouse is on the porcupine, puff out the spikes and change the
    # eyebrows.
    if (spikes.contains(mouseX, mouseY) == True):
        spikes.radius = 250
        spikes.roundness = 40
        leftEyebrow.rotateAngle = 30
        rightEyebrow.rotateAngle = -30
    else:
        spikes.radius = 130
        spikes.roundness = 80
        leftEyebrow.rotateAngle = -15
        rightEyebrow.rotateAngle = 15



# -
app.background = 'cornflowerBlue'

spikes = Star(200, 335, 130, 30, fill='saddleBrown', roundness=80)

# body
Circle(140, 330, 15, fill='navajoWhite', border='tan', borderWidth=5)
Circle(260, 330, 15, fill='navajoWhite', border='tan', borderWidth=5)
Oval(200, 310, 160, 110, fill='tan', align='top')

# eyes
Circle(175, 360, 7)
Circle(225, 360, 7)

# nose
RegularPolygon(200, 390, 15, 3, rotateAngle=180)

leftEyebrow = Line(155, 345, 170, 345, rotateAngle=-15)
rightEyebrow = Line(245, 345, 230, 345, rotateAngle=15)

def onMouseMove(mouseX, mouseY):
    # If the mouse is on the porcupine, puff out the spikes and change the
    # eyebrows.
    if (spikes.contains(mouseX, mouseY) == True):
        spikes.radius = 250
        spikes.roundness = 40
        leftEyebrow.rotateAngle = 30
        rightEyebrow.rotateAngle = -30
    else:
        spikes.radius = 130
        spikes.roundness = 80
        leftEyebrow.rotateAngle = -15
        rightEyebrow.rotateAngle = 15

onMouseMove(200, 300)
onMouseMove(140, 120)
onMouseMove(50, 375)
onMouseMove(300, 300)
onMouseMove(250, 270)
onMouseMove(340, 120)
onMouseMove(170, 300)
onMouseMove(240, 80)

