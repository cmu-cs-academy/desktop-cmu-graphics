def drawFace(x, y, backgroundColor):
    Rect(x - 100, y - 100, 200, 200, fill=backgroundColor)
    Circle(x - 25, y - 20, 20, fill='white')
    Circle(x - 25, y - 20, 7)
    Circle(x + 25, y - 20, 20, fill='white')
    Circle(x + 25, y - 20, 7)

drawFace(100, 100, 'salmon')
drawFace(300, 100, 'paleTurquoise')
drawFace(100, 300, 'paleGreen')
drawFace(300, 300, 'plum')

redMouth = Label('-', 100, 120, size=50)
blueMouth = Label('-', 300, 120, size=50)
greenMouth = Label('-', 100, 320, size=50)
purpleMouth = Label('-', 300, 320, size=50)

def onMousePress(mouseX, mouseY):
    # Based on the face you click, switch the mouth to either - or o.
    if ((mouseX < 200) and (mouseY < 200)):
        if (redMouth.value == '-'):
            redMouth.value = 'o'
        else:
            redMouth.value = '-'

    elif ((mouseX >= 200) and (mouseY < 200)):
        if (blueMouth.value == '-'):
            blueMouth.value = 'o'
        else:
            blueMouth.value = '-'

    elif ((mouseX < 200) and (mouseY >= 200)):
        if (greenMouth.value == '-'):
            greenMouth.value = 'o'
        else:
            greenMouth.value = '-'

    elif ((mouseX >= 200) and (mouseY >= 200)):
        if (purpleMouth.value == '-'):
            purpleMouth.value = 'o'
        else:
            purpleMouth.value = '-'

onMousePress(50, 340)
onMousePress(210, 40)
onMousePress(300, 280)
onMousePress(140, 100)


# -
def drawFace(x, y, backgroundColor):
    Rect(x - 100, y - 100, 200, 200, fill=backgroundColor)
    Circle(x - 25, y - 20, 20, fill='white')
    Circle(x - 25, y - 20, 7)
    Circle(x + 25, y - 20, 20, fill='white')
    Circle(x + 25, y - 20, 7)

drawFace(100, 100, 'salmon')
drawFace(300, 100, 'paleTurquoise')
drawFace(100, 300, 'paleGreen')
drawFace(300, 300, 'plum')

redMouth = Label('-', 100, 120, size=50)
blueMouth = Label('-', 300, 120, size=50)
greenMouth = Label('-', 100, 320, size=50)
purpleMouth = Label('-', 300, 320, size=50)

def onMousePress(mouseX, mouseY):
    # Based on the face you click, switch the mouth to either - or o.
    if ((mouseX < 200) and (mouseY < 200)):
        if (redMouth.value == '-'):
            redMouth.value = 'o'
        else:
            redMouth.value = '-'

    elif ((mouseX >= 200) and (mouseY < 200)):
        if (blueMouth.value == '-'):
            blueMouth.value = 'o'
        else:
            blueMouth.value = '-'

    elif ((mouseX < 200) and (mouseY >= 200)):
        if (greenMouth.value == '-'):
            greenMouth.value = 'o'
        else:
            greenMouth.value = '-'

    elif ((mouseX >= 200) and (mouseY >= 200)):
        if (purpleMouth.value == '-'):
            purpleMouth.value = 'o'
        else:
            purpleMouth.value = '-'

onMousePress(130, 250)
onMousePress(60, 320)
onMousePress(180, 210)


# -
def drawFace(x, y, backgroundColor):
    Rect(x - 100, y - 100, 200, 200, fill=backgroundColor)
    Circle(x - 25, y - 20, 20, fill='white')
    Circle(x - 25, y - 20, 7)
    Circle(x + 25, y - 20, 20, fill='white')
    Circle(x + 25, y - 20, 7)

drawFace(100, 100, 'salmon')
drawFace(300, 100, 'paleTurquoise')
drawFace(100, 300, 'paleGreen')
drawFace(300, 300, 'plum')

redMouth = Label('-', 100, 120, size=50)
blueMouth = Label('-', 300, 120, size=50)
greenMouth = Label('-', 100, 320, size=50)
purpleMouth = Label('-', 300, 320, size=50)

def onMousePress(mouseX, mouseY):
    # Based on the face you click, switch the mouth to either - or o.
    if ((mouseX < 200) and (mouseY < 200)):
        if (redMouth.value == '-'):
            redMouth.value = 'o'
        else:
            redMouth.value = '-'

    elif ((mouseX >= 200) and (mouseY < 200)):
        if (blueMouth.value == '-'):
            blueMouth.value = 'o'
        else:
            blueMouth.value = '-'

    elif ((mouseX < 200) and (mouseY >= 200)):
        if (greenMouth.value == '-'):
            greenMouth.value = 'o'
        else:
            greenMouth.value = '-'

    elif ((mouseX >= 200) and (mouseY >= 200)):
        if (purpleMouth.value == '-'):
            purpleMouth.value = 'o'
        else:
            purpleMouth.value = '-'

onMousePress(130, 250)
onMousePress(60, 320)
onMousePress(180, 210)

