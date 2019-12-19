app.background = 'black'

Line(200, 0, 200, 400, fill='lightGrey')
Line(0, 200, 400, 200, fill='lightGrey')

def onMousePress(mouseX, mouseY):
    if (mouseX < 200):
        if (mouseY < 200):
            Star(mouseX, mouseY, 30, 7, fill='springGreen')
        else:
            Circle(mouseX, mouseY, 35, fill='fuchsia')
            Label('Woohoo!', mouseX, mouseY)
    else:
        RegularPolygon(mouseX, mouseY, 25, 6, fill='orange')

onMousePress(300, 100)


# -
app.background = 'black'

Line(200, 0, 200, 400, fill='lightGrey')
Line(0, 200, 400, 200, fill='lightGrey')

def onMousePress(mouseX, mouseY):
    if (mouseX < 200):
        if (mouseY < 200):
            Star(mouseX, mouseY, 30, 7, fill='springGreen')
        else:
            Circle(mouseX, mouseY, 35, fill='fuchsia')
            Label('Woohoo!', mouseX, mouseY)
    else:
        RegularPolygon(mouseX, mouseY, 25, 6, fill='orange')

onMousePress(300, 300)


# -
app.background = 'black'

Line(200, 0, 200, 400, fill='lightGrey')
Line(0, 200, 400, 200, fill='lightGrey')

def onMousePress(mouseX, mouseY):
    if (mouseX < 200):
        if (mouseY < 200):
            Star(mouseX, mouseY, 30, 7, fill='springGreen')
        else:
            Circle(mouseX, mouseY, 35, fill='fuchsia')
            Label('Woohoo!', mouseX, mouseY)
    else:
        RegularPolygon(mouseX, mouseY, 25, 6, fill='orange')

onMousePress(300, 300)

