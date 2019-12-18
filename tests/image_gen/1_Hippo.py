app.background = 'forestGreen'

hippoBody = Group(
    Oval(200, 265, 110, 80, fill='lightCoral'),
    Circle(170, 305, 15, fill='indianRed'),
    Circle(230, 305, 15, fill='indianRed'),
    Rect(200, 305, 90, 15, fill='forestGreen', align='top'),
    Line(200, 260, 210, 280, fill='indianRed', lineWidth=5)
    )

hippoFace = Group(
    Circle(220, 225, 10, fill='lightPink'),
    Circle(180, 225, 10, fill='lightPink'),
    Oval(200, 240, 65, 50, fill='lightPink'),
    Oval(200, 260, 75, 60, fill='lightPink'),
    Oval(190, 265, 6, 10, fill='hotPink'),
    Oval(210, 265, 6, 10, fill='hotPink'),
    Circle(185, 240, 12, fill='white'),
    Circle(215, 240, 12, fill='white'),
    Circle(185, 240, 4),
    Circle(215, 240, 4)
    )

hippo = Group(hippoBody, hippoFace)
hippo.isMovingForward = True

def onMousePress(mouseX, mouseY):
    # If the hippo is moving forward the width and height should increase.
    # If the hippo is moving backward the width and height should decrease.
    if (hippo.isMovingForward == True):
        hippo.width += 10
        hippo.height += 10
    else:
        if ((hippo.width > 10) and (hippo.height > 10)):
            hippo.width -= 10
            hippo.height -= 10

def onKeyPress(key):
    # If the 'f' key is pressed the hippo should be moving forward.
    # If the 'b' key is pressed the hippo should be moving backward.
    if (key == 'f'):
        hippo.isMovingForward = True
        hippoFace.toFront()
    elif (key == 'b'):
        hippo.isMovingForward = False
        hippoFace.toBack()



# -
app.background = 'forestGreen'

hippoBody = Group(
    Oval(200, 265, 110, 80, fill='lightCoral'),
    Circle(170, 305, 15, fill='indianRed'),
    Circle(230, 305, 15, fill='indianRed'),
    Rect(200, 305, 90, 15, fill='forestGreen', align='top'),
    Line(200, 260, 210, 280, fill='indianRed', lineWidth=5)
    )

hippoFace = Group(
    Circle(220, 225, 10, fill='lightPink'),
    Circle(180, 225, 10, fill='lightPink'),
    Oval(200, 240, 65, 50, fill='lightPink'),
    Oval(200, 260, 75, 60, fill='lightPink'),
    Oval(190, 265, 6, 10, fill='hotPink'),
    Oval(210, 265, 6, 10, fill='hotPink'),
    Circle(185, 240, 12, fill='white'),
    Circle(215, 240, 12, fill='white'),
    Circle(185, 240, 4),
    Circle(215, 240, 4)
    )

hippo = Group(hippoBody, hippoFace)
hippo.isMovingForward = True

def onMousePress(mouseX, mouseY):
    # If the hippo is moving forward the width and height should increase.
    # If the hippo is moving backward the width and height should decrease.
    if (hippo.isMovingForward == True):
        hippo.width += 10
        hippo.height += 10
    else:
        if ((hippo.width > 10) and (hippo.height > 10)):
            hippo.width -= 10
            hippo.height -= 10

def onKeyPress(key):
    # If the 'f' key is pressed the hippo should be moving forward.
    # If the 'b' key is pressed the hippo should be moving backward.
    if (key == 'f'):
        hippo.isMovingForward = True
        hippoFace.toFront()
    elif (key == 'b'):
        hippo.isMovingForward = False
        hippoFace.toBack()

onKeyPress('b')
onMousePress(200, 200)
onMousePress(200, 200)
onKeyPress('f')
onMousePress(200, 200)


# -
app.background = 'forestGreen'

hippoBody = Group(
    Oval(200, 265, 110, 80, fill='lightCoral'),
    Circle(170, 305, 15, fill='indianRed'),
    Circle(230, 305, 15, fill='indianRed'),
    Rect(200, 305, 90, 15, fill='forestGreen', align='top'),
    Line(200, 260, 210, 280, fill='indianRed', lineWidth=5)
    )

hippoFace = Group(
    Circle(220, 225, 10, fill='lightPink'),
    Circle(180, 225, 10, fill='lightPink'),
    Oval(200, 240, 65, 50, fill='lightPink'),
    Oval(200, 260, 75, 60, fill='lightPink'),
    Oval(190, 265, 6, 10, fill='hotPink'),
    Oval(210, 265, 6, 10, fill='hotPink'),
    Circle(185, 240, 12, fill='white'),
    Circle(215, 240, 12, fill='white'),
    Circle(185, 240, 4),
    Circle(215, 240, 4)
    )

hippo = Group(hippoBody, hippoFace)
hippo.isMovingForward = True

def onMousePress(mouseX, mouseY):
    # If the hippo is moving forward the width and height should increase.
    # If the hippo is moving backward the width and height should decrease.
    if (hippo.isMovingForward == True):
        hippo.width += 10
        hippo.height += 10
    else:
        if ((hippo.width > 10) and (hippo.height > 10)):
            hippo.width -= 10
            hippo.height -= 10

def onKeyPress(key):
    # If the 'f' key is pressed the hippo should be moving forward.
    # If the 'b' key is pressed the hippo should be moving backward.
    if (key == 'f'):
        hippo.isMovingForward = True
        hippoFace.toFront()
    elif (key == 'b'):
        hippo.isMovingForward = False
        hippoFace.toBack()

onMousePress(200, 200)
onMousePress(200, 200)
onKeyPress('b')
onMousePress(200, 200)
onMousePress(200, 200)
onMousePress(200, 200)

