app.background = gradient('deepSkyBlue', 'lightSkyBlue', start='top')

leftBlade = Polygon(190, 165, 130, 135, 130, 145, fill='lightGrey')
rightBlade = Polygon(205, 165, 265, 135, 265, 145, fill='grey')

helicopter = Group(
    Oval(200, 200, 100, 50, rotateAngle=-5),
    Circle(200, 165, 8),
    Polygon(190, 180, 192, 165, 208, 165, 210, 175),
    Polygon(235, 185, 245, 205, 320, 190, 320, 180),
    Polygon(325, 205, 330, 195, 325, 180, 330, 160, 325, 155, 320, 170, 315, 185)
    )
helicopter.fill = gradient('crimson', 'crimson', 'darkRed', start='top')

helicopter.add(
    Polygon(185, 180, 165, 190, 155, 205, 180, 200, fill='aqua'),
    Polygon(190, 180, 210, 180, 215, 200, 185, 200, fill='aqua'),
    Oval(168, 193, 36, 12, fill=gradient('azure', 'aqua', 'aqua'), rotateAngle=-35),
    Line(180, 220, 170, 235, fill=rgb(70, 75, 75)),
    Line(210, 220, 220, 235, fill=rgb(70, 75, 75)),
    Line(145, 235, 250, 235, fill=rgb(70, 75, 75), lineWidth=3),
    leftBlade, rightBlade
    )

def onKeyHold(keys):
    # Change the helicopter's position by 2 pixels depending on the key that is
    # pressed. Change the rotateAngle as well depending on if 'left' or 'right'
    # is pressed.
    if ('up' in keys):
        helicopter.centerY -= 2
    elif ('down' in keys):
        helicopter.centerY += 2
    if ('left' in keys):
        helicopter.centerX -= 2
        helicopter.rotateAngle = -15
    elif ('right' in keys):
        helicopter.centerX += 2
        helicopter.rotateAngle = 15
    else:
        helicopter.rotateAngle = 0
    # Alternate the color of the blades so they appear to be spinning.
    if (leftBlade.fill == 'lightGrey'):
        leftBlade.fill = 'grey'
        rightBlade.fill = 'lightGrey'
    else:
        leftBlade.fill = 'lightGrey'
        rightBlade.fill = 'grey'



# -
app.background = gradient('deepSkyBlue', 'lightSkyBlue', start='top')

leftBlade = Polygon(190, 165, 130, 135, 130, 145, fill='lightGrey')
rightBlade = Polygon(205, 165, 265, 135, 265, 145, fill='grey')

helicopter = Group(
    Oval(200, 200, 100, 50, rotateAngle=-5),
    Circle(200, 165, 8),
    Polygon(190, 180, 192, 165, 208, 165, 210, 175),
    Polygon(235, 185, 245, 205, 320, 190, 320, 180),
    Polygon(325, 205, 330, 195, 325, 180, 330, 160, 325, 155, 320, 170, 315, 185)
    )
helicopter.fill = gradient('crimson', 'crimson', 'darkRed', start='top')

helicopter.add(
    Polygon(185, 180, 165, 190, 155, 205, 180, 200, fill='aqua'),
    Polygon(190, 180, 210, 180, 215, 200, 185, 200, fill='aqua'),
    Oval(168, 193, 36, 12, fill=gradient('azure', 'aqua', 'aqua'), rotateAngle=-35),
    Line(180, 220, 170, 235, fill=rgb(70, 75, 75)),
    Line(210, 220, 220, 235, fill=rgb(70, 75, 75)),
    Line(145, 235, 250, 235, fill=rgb(70, 75, 75), lineWidth=3),
    leftBlade, rightBlade
    )

def onKeyHold(keys):
    # Change the helicopter's position by 2 pixels depending on the key that is
    # pressed. Change the rotateAngle as well depending on if 'left' or 'right'
    # is pressed.
    if ('up' in keys):
        helicopter.centerY -= 2
    elif ('down' in keys):
        helicopter.centerY += 2
    if ('left' in keys):
        helicopter.centerX -= 2
        helicopter.rotateAngle = -15
    elif ('right' in keys):
        helicopter.centerX += 2
        helicopter.rotateAngle = 15
    else:
        helicopter.rotateAngle = 0
    # Alternate the color of the blades so they appear to be spinning.
    if (leftBlade.fill == 'lightGrey'):
        leftBlade.fill = 'grey'
        rightBlade.fill = 'lightGrey'
    else:
        leftBlade.fill = 'lightGrey'
        rightBlade.fill = 'grey'

onKeyHolds(['up'], 4)
onKeyHolds(['left'], 4)


# -
app.background = gradient('deepSkyBlue', 'lightSkyBlue', start='top')

leftBlade = Polygon(190, 165, 130, 135, 130, 145, fill='lightGrey')
rightBlade = Polygon(205, 165, 265, 135, 265, 145, fill='grey')

helicopter = Group(
    Oval(200, 200, 100, 50, rotateAngle=-5),
    Circle(200, 165, 8),
    Polygon(190, 180, 192, 165, 208, 165, 210, 175),
    Polygon(235, 185, 245, 205, 320, 190, 320, 180),
    Polygon(325, 205, 330, 195, 325, 180, 330, 160, 325, 155, 320, 170, 315, 185)
    )
helicopter.fill = gradient('crimson', 'crimson', 'darkRed', start='top')

helicopter.add(
    Polygon(185, 180, 165, 190, 155, 205, 180, 200, fill='aqua'),
    Polygon(190, 180, 210, 180, 215, 200, 185, 200, fill='aqua'),
    Oval(168, 193, 36, 12, fill=gradient('azure', 'aqua', 'aqua'), rotateAngle=-35),
    Line(180, 220, 170, 235, fill=rgb(70, 75, 75)),
    Line(210, 220, 220, 235, fill=rgb(70, 75, 75)),
    Line(145, 235, 250, 235, fill=rgb(70, 75, 75), lineWidth=3),
    leftBlade, rightBlade
    )

def onKeyHold(keys):
    # Change the helicopter's position by 2 pixels depending on the key that is
    # pressed. Change the rotateAngle as well depending on if 'left' or 'right'
    # is pressed.
    if ('up' in keys):
        helicopter.centerY -= 2
    elif ('down' in keys):
        helicopter.centerY += 2
    if ('left' in keys):
        helicopter.centerX -= 2
        helicopter.rotateAngle = -15
    elif ('right' in keys):
        helicopter.centerX += 2
        helicopter.rotateAngle = 15
    else:
        helicopter.rotateAngle = 0
    # Alternate the color of the blades so they appear to be spinning.
    if (leftBlade.fill == 'lightGrey'):
        leftBlade.fill = 'grey'
        rightBlade.fill = 'lightGrey'
    else:
        leftBlade.fill = 'lightGrey'
        rightBlade.fill = 'grey'

onKeyHolds(['down', 'left'], 50)

