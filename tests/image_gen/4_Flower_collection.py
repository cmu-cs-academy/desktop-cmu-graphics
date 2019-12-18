app.background = 'aliceBlue'

# vase
Oval(200, 300, 50, 10, fill='limeGreen')
Rect(175, 300, 50, 100, fill='silver')
Oval(200, 370, 100, 135,
     fill=gradient('gray', 'silver', 'silver', start='left-bottom'))

def drawLeaf(mouseX, mouseY):
    Star(mouseX, mouseY, 30, 4, fill='green', rotateAngle=45)

def drawFlower(mouseX, mouseY):
    Line(mouseX, mouseY, 200, 300, fill='limeGreen', lineWidth=4)
    Star(mouseX, mouseY, 25, 6, fill=gradient('lavender', 'plum', 'plum'))
    Circle(mouseX, mouseY, 9, fill='lemonChiffon')

def onMousePress(mouseX, mouseY):
    if (mouseY > 200):
        drawLeaf(mouseX, mouseY)
    drawFlower(mouseX, mouseY)

onMousePress(100, 10)
onMousePress(150, 50)
onMousePress(200, 100)
onMousePress(250, 150)


# -
app.background = 'aliceBlue'

# vase
Oval(200, 300, 50, 10, fill='limeGreen')
Rect(175, 300, 50, 100, fill='silver')
Oval(200, 370, 100, 135,
     fill=gradient('gray', 'silver', 'silver', start='left-bottom'))

def drawLeaf(mouseX, mouseY):
    Star(mouseX, mouseY, 30, 4, fill='green', rotateAngle=45)

def drawFlower(mouseX, mouseY):
    Line(mouseX, mouseY, 200, 300, fill='limeGreen', lineWidth=4)
    Star(mouseX, mouseY, 25, 6, fill=gradient('lavender', 'plum', 'plum'))
    Circle(mouseX, mouseY, 9, fill='lemonChiffon')

def onMousePress(mouseX, mouseY):
    if (mouseY > 200):
        drawLeaf(mouseX, mouseY)
    drawFlower(mouseX, mouseY)

onMousePress(210, 60)
onMousePress(100, 180)
onMousePress(280, 240)
onMousePress(60, 40)
onMousePress(380, 250)


# -
app.background = 'aliceBlue'

# vase
Oval(200, 300, 50, 10, fill='limeGreen')
Rect(175, 300, 50, 100, fill='silver')
Oval(200, 370, 100, 135,
     fill=gradient('gray', 'silver', 'silver', start='left-bottom'))

def drawLeaf(mouseX, mouseY):
    Star(mouseX, mouseY, 30, 4, fill='green', rotateAngle=45)

def drawFlower(mouseX, mouseY):
    Line(mouseX, mouseY, 200, 300, fill='limeGreen', lineWidth=4)
    Star(mouseX, mouseY, 25, 6, fill=gradient('lavender', 'plum', 'plum'))
    Circle(mouseX, mouseY, 9, fill='lemonChiffon')

def onMousePress(mouseX, mouseY):
    if (mouseY > 200):
        drawLeaf(mouseX, mouseY)
    drawFlower(mouseX, mouseY)


