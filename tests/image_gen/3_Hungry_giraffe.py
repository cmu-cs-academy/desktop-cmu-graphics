app.background = 'lightSkyBlue'

# neck
giraffeNeck = Group(
    Rect(200, 200, 75, 400, align='top',
         fill=gradient('goldenrod', 'gold', 'gold', start='top')),
    Circle(180, 300, 15, fill='sienna'),
    Circle(220, 325, 15, fill='sienna'),
    Circle(185, 375, 20, fill='sienna'),
    Circle(225, 400, 10, fill='sienna'),
    Circle(180, 430, 10, fill='sienna'),
    Circle(220, 455, 15, fill='sienna'),
    Circle(185, 510, 20, fill='sienna'),
    Circle(225, 535, 10, fill='sienna')
    )

# face
giraffeFace = Group(
    Line(160, 155, 135, 130, fill='sienna', lineWidth=12),
    Circle(135, 130, 10, fill='sienna'),
    Line(240, 155, 265, 130, fill='sienna', lineWidth=12),
    Circle(265, 130, 10, fill='sienna'),
    Oval(200, 200, 135, 150, fill='gold'),
    Oval(200, 200, 100, 75, fill='moccasin', align='top'),
    Oval(165, 175, 10, 20, align='top'),
    Oval(235, 175, 10, 20, align='top'),
    Circle(185, 220, 3, fill='sienna'),
    Circle(215, 220, 3, fill='sienna')
    )

# smile
giraffeSmile = Group(
    Circle(200, 350, 15, fill='pink'),
    Rect(200, 350, 30, 15, fill='moccasin', align='bottom')
    )
giraffeSmile.visible = False

# leaf
leaf = Group(
    Line(0, 20, 7, 20, fill='sienna', lineWidth=1),
    Line(5, 20, 5, 22, fill='lightGreen', lineWidth=5),
    Line(5, 22, 30, 45, fill='lightGreen', lineWidth=5),
    Oval(50, 50, 50, 30, fill='lightGreen', rotateAngle=15),
    Polygon(72, 47, 85, 65, 55, 66, fill='lightGreen')
    )

def onMouseMove(mouseX, mouseY):
    # Move the giraffe's face to the same height as the mouse,
    # and neck accordingly.
    giraffeNeck.top = mouseY
    giraffeFace.centerY = mouseY

    # If the giraffe reaches the leaf, it should eat the leaf and smile.
    # Otherwise, it shouldn't smile, and the leaf should stay in the
    # initial location.
    if (mouseY < 100):
        giraffeSmile.centerY = giraffeFace.centerY + 50
        leaf.left = giraffeSmile.centerX
        leaf.top = giraffeSmile.centerY
        giraffeSmile.visible = True
    else:
        giraffeSmile.visible = False
        leaf.left = 0
        leaf.top = 20

onMouseMove(200, 99)
onMouseMove(200, 200)


# -
app.background = 'lightSkyBlue'

# neck
giraffeNeck = Group(
    Rect(200, 200, 75, 400, align='top',
         fill=gradient('goldenrod', 'gold', 'gold', start='top')),
    Circle(180, 300, 15, fill='sienna'),
    Circle(220, 325, 15, fill='sienna'),
    Circle(185, 375, 20, fill='sienna'),
    Circle(225, 400, 10, fill='sienna'),
    Circle(180, 430, 10, fill='sienna'),
    Circle(220, 455, 15, fill='sienna'),
    Circle(185, 510, 20, fill='sienna'),
    Circle(225, 535, 10, fill='sienna')
    )

# face
giraffeFace = Group(
    Line(160, 155, 135, 130, fill='sienna', lineWidth=12),
    Circle(135, 130, 10, fill='sienna'),
    Line(240, 155, 265, 130, fill='sienna', lineWidth=12),
    Circle(265, 130, 10, fill='sienna'),
    Oval(200, 200, 135, 150, fill='gold'),
    Oval(200, 200, 100, 75, fill='moccasin', align='top'),
    Oval(165, 175, 10, 20, align='top'),
    Oval(235, 175, 10, 20, align='top'),
    Circle(185, 220, 3, fill='sienna'),
    Circle(215, 220, 3, fill='sienna')
    )

# smile
giraffeSmile = Group(
    Circle(200, 350, 15, fill='pink'),
    Rect(200, 350, 30, 15, fill='moccasin', align='bottom')
    )
giraffeSmile.visible = False

# leaf
leaf = Group(
    Line(0, 20, 7, 20, fill='sienna', lineWidth=1),
    Line(5, 20, 5, 22, fill='lightGreen', lineWidth=5),
    Line(5, 22, 30, 45, fill='lightGreen', lineWidth=5),
    Oval(50, 50, 50, 30, fill='lightGreen', rotateAngle=15),
    Polygon(72, 47, 85, 65, 55, 66, fill='lightGreen')
    )

def onMouseMove(mouseX, mouseY):
    # Move the giraffe's face to the same height as the mouse,
    # and neck accordingly.
    giraffeNeck.top = mouseY
    giraffeFace.centerY = mouseY

    # If the giraffe reaches the leaf, it should eat the leaf and smile.
    # Otherwise, it shouldn't smile, and the leaf should stay in the
    # initial location.
    if (mouseY < 100):
        giraffeSmile.centerY = giraffeFace.centerY + 50
        leaf.left = giraffeSmile.centerX
        leaf.top = giraffeSmile.centerY
        giraffeSmile.visible = True
    else:
        giraffeSmile.visible = False
        leaf.left = 0
        leaf.top = 20

onMouseMove(200, 400)


# -
app.background = 'lightSkyBlue'

# neck
giraffeNeck = Group(
    Rect(200, 200, 75, 400, align='top',
         fill=gradient('goldenrod', 'gold', 'gold', start='top')),
    Circle(180, 300, 15, fill='sienna'),
    Circle(220, 325, 15, fill='sienna'),
    Circle(185, 375, 20, fill='sienna'),
    Circle(225, 400, 10, fill='sienna'),
    Circle(180, 430, 10, fill='sienna'),
    Circle(220, 455, 15, fill='sienna'),
    Circle(185, 510, 20, fill='sienna'),
    Circle(225, 535, 10, fill='sienna')
    )

# face
giraffeFace = Group(
    Line(160, 155, 135, 130, fill='sienna', lineWidth=12),
    Circle(135, 130, 10, fill='sienna'),
    Line(240, 155, 265, 130, fill='sienna', lineWidth=12),
    Circle(265, 130, 10, fill='sienna'),
    Oval(200, 200, 135, 150, fill='gold'),
    Oval(200, 200, 100, 75, fill='moccasin', align='top'),
    Oval(165, 175, 10, 20, align='top'),
    Oval(235, 175, 10, 20, align='top'),
    Circle(185, 220, 3, fill='sienna'),
    Circle(215, 220, 3, fill='sienna')
    )

# smile
giraffeSmile = Group(
    Circle(200, 350, 15, fill='pink'),
    Rect(200, 350, 30, 15, fill='moccasin', align='bottom')
    )
giraffeSmile.visible = False

# leaf
leaf = Group(
    Line(0, 20, 7, 20, fill='sienna', lineWidth=1),
    Line(5, 20, 5, 22, fill='lightGreen', lineWidth=5),
    Line(5, 22, 30, 45, fill='lightGreen', lineWidth=5),
    Oval(50, 50, 50, 30, fill='lightGreen', rotateAngle=15),
    Polygon(72, 47, 85, 65, 55, 66, fill='lightGreen')
    )

def onMouseMove(mouseX, mouseY):
    # Move the giraffe's face to the same height as the mouse,
    # and neck accordingly.
    giraffeNeck.top = mouseY
    giraffeFace.centerY = mouseY

    # If the giraffe reaches the leaf, it should eat the leaf and smile.
    # Otherwise, it shouldn't smile, and the leaf should stay in the
    # initial location.
    if (mouseY < 100):
        giraffeSmile.centerY = giraffeFace.centerY + 50
        leaf.left = giraffeSmile.centerX
        leaf.top = giraffeSmile.centerY
        giraffeSmile.visible = True
    else:
        giraffeSmile.visible = False
        leaf.left = 0
        leaf.top = 20

onMouseMove(200, 400)
onMouseMove(400, 400)

