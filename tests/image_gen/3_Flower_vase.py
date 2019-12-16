# background
Rect(0, 0, 400, 400, fill=gradient('ghostWhite', 'powderBlue'))

# vase
Oval(200, 300, 50, 10, fill='limeGreen')
Rect(175, 300, 50, 100, fill='silver')
Oval(200, 370, 100, 135,
     fill=gradient('dimGray', 'silver', 'silver', start='left-bottom'))

def onMousePress(mouseX, mouseY):
    # Draw a flower where you click the mouse and connect its stem to the vase!
    Line(200, 300, mouseX, mouseY, fill='limeGreen', lineWidth=5)
    Star(mouseX, mouseY, 20, 6, fill='hotPink', roundness=70)
    Circle(mouseX, mouseY, 8, fill=gradient('orange', 'yellow'))

onMousePress(150, 150)
onMousePress(200, 100)
onMousePress(250, 150)
onMousePress(100, 250)
onMousePress(260, 260)
onMousePress(150, 210)
onMousePress(280, 195)


# -
# background
Rect(0, 0, 400, 400, fill=gradient('ghostWhite', 'powderBlue'))

# vase
Oval(200, 300, 50, 10, fill='limeGreen')
Rect(175, 300, 50, 100, fill='silver')
Oval(200, 370, 100, 135,
     fill=gradient('dimGray', 'silver', 'silver', start='left-bottom'))

def onMousePress(mouseX, mouseY):
    # Draw a flower where you click the mouse and connect its stem to the vase!
    Line(200, 300, mouseX, mouseY, fill='limeGreen', lineWidth=5)
    Star(mouseX, mouseY, 20, 6, fill='hotPink', roundness=70)
    Circle(mouseX, mouseY, 8, fill=gradient('orange', 'yellow'))

onMousePress(200, 100)


# -
# background
Rect(0, 0, 400, 400, fill=gradient('ghostWhite', 'powderBlue'))

# vase
Oval(200, 300, 50, 10, fill='limeGreen')
Rect(175, 300, 50, 100, fill='silver')
Oval(200, 370, 100, 135,
     fill=gradient('dimGray', 'silver', 'silver', start='left-bottom'))

def onMousePress(mouseX, mouseY):
    # Draw a flower where you click the mouse and connect its stem to the vase!
    Line(200, 300, mouseX, mouseY, fill='limeGreen', lineWidth=5)
    Star(mouseX, mouseY, 20, 6, fill='hotPink', roundness=70)
    Circle(mouseX, mouseY, 8, fill=gradient('orange', 'yellow'))


