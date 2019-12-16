app.background = 'black'

Line(200, 0, 200, 400, fill='white')
Line(0, 200, 400, 200, fill='white')

def onMouseMove(mouseX, mouseY):
    # Depending on the quadrant the mouse is on, draw a gradient line from
    # the closest corner.
    if (mouseY < 200):
        if (mouseX < 200):
            Line(0, 0, mouseX, mouseY, fill=gradient('red', 'black'))
        else:
            Line(400, 0, mouseX, mouseY, fill=gradient('green', 'black'))
    else:
        if (mouseX < 200):
            Line(0, 400, mouseX, mouseY, fill=gradient('blue', 'black'))
        else:
            Line(400, 400, mouseX, mouseY, fill=gradient('yellow', 'black'))

onMouseMove(195, 55)
onMouseMove(205, 175)
onMouseMove(65, 195)
onMouseMove(25, 205)
onMouseMove(295, 195)
onMouseMove(340, 205)
onMouseMove(195, 290)
onMouseMove(205, 330)


# -
app.background = 'black'

Line(200, 0, 200, 400, fill='white')
Line(0, 200, 400, 200, fill='white')

def onMouseMove(mouseX, mouseY):
    # Depending on the quadrant the mouse is on, draw a gradient line from
    # the closest corner.
    if (mouseY < 200):
        if (mouseX < 200):
            Line(0, 0, mouseX, mouseY, fill=gradient('red', 'black'))
        else:
            Line(400, 0, mouseX, mouseY, fill=gradient('green', 'black'))
    else:
        if (mouseX < 200):
            Line(0, 400, mouseX, mouseY, fill=gradient('blue', 'black'))
        else:
            Line(400, 400, mouseX, mouseY, fill=gradient('yellow', 'black'))

onMouseMove(120, 300)
onMouseMove(380, 240)
onMouseMove(320, 320)
onMouseMove(50, 180)
onMouseMove(240, 160)
onMouseMove(190, 90)
onMouseMove(30, 300)


# -
app.background = 'black'

Line(200, 0, 200, 400, fill='white')
Line(0, 200, 400, 200, fill='white')

def onMouseMove(mouseX, mouseY):
    # Depending on the quadrant the mouse is on, draw a gradient line from
    # the closest corner.
    if (mouseY < 200):
        if (mouseX < 200):
            Line(0, 0, mouseX, mouseY, fill=gradient('red', 'black'))
        else:
            Line(400, 0, mouseX, mouseY, fill=gradient('green', 'black'))
    else:
        if (mouseX < 200):
            Line(0, 400, mouseX, mouseY, fill=gradient('blue', 'black'))
        else:
            Line(400, 400, mouseX, mouseY, fill=gradient('yellow', 'black'))

onMouseMove(100, 100)

