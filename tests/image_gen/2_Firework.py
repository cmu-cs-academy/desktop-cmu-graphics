# background
Rect(0, 0, 400, 400)

def onMousePress(mouseX, mouseY):
    # Check if the firework is high enough up to explode.
    if (mouseY < 150):
        Star(mouseX, mouseY, 100, 12, fill=gradient('red', 'white'), roundness=10)

        Star(mouseX, mouseY, 100, 12, fill=gradient('yellow', 'white'),
             roundness=10, rotateAngle=10)

        Star(mouseX, mouseY, 100, 12, roundness=10, rotateAngle=5)
    # If the firework is not high enough, draw a rising pre-firework line.
    else:
        Line(mouseX, mouseY, mouseX, 400,
             fill=gradient('black', 'red', 'yellow', 'black', start='top'))

onMousePress(200, 200)


# -
# background
Rect(0, 0, 400, 400)

def onMousePress(mouseX, mouseY):
    # Check if the firework is high enough up to explode.
    if (mouseY < 150):
        Star(mouseX, mouseY, 100, 12, fill=gradient('red', 'white'), roundness=10)

        Star(mouseX, mouseY, 100, 12, fill=gradient('yellow', 'white'),
             roundness=10, rotateAngle=10)

        Star(mouseX, mouseY, 100, 12, roundness=10, rotateAngle=5)
    # If the firework is not high enough, draw a rising pre-firework line.
    else:
        Line(mouseX, mouseY, mouseX, 400,
             fill=gradient('black', 'red', 'yellow', 'black', start='top'))

onMousePress(150, 145)
onMousePress(150, 155)


# -
# background
Rect(0, 0, 400, 400)

def onMousePress(mouseX, mouseY):
    # Check if the firework is high enough up to explode.
    if (mouseY < 150):
        Star(mouseX, mouseY, 100, 12, fill=gradient('red', 'white'), roundness=10)

        Star(mouseX, mouseY, 100, 12, fill=gradient('yellow', 'white'),
             roundness=10, rotateAngle=10)

        Star(mouseX, mouseY, 100, 12, roundness=10, rotateAngle=5)
    # If the firework is not high enough, draw a rising pre-firework line.
    else:
        Line(mouseX, mouseY, mouseX, 400,
             fill=gradient('black', 'red', 'yellow', 'black', start='top'))

onMousePress(200, 200)

