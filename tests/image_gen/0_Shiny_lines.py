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

onMouseMove(175, 175)
onMouseMove(175, 225)
onMouseMove(225, 175)
onMouseMove(225, 225)


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

