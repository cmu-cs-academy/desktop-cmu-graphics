app.background = gradient('skyBlue', 'lightBlue', start='top')

o = Oval(200, 200, 200, 200, fill=gradient('lemonChiffon', 'gold'))

def onMouseMove(mouseX, mouseY):
    # Change the width and height of the oval based on mouse position.
    # Make sure there are no issues when mouseX or mouseY is 0!
    o.width = mouseX + 1
    o.height = mouseY + 1

onMouseMove(100, 250)


# -
app.background = gradient('skyBlue', 'lightBlue', start='top')

o = Oval(200, 200, 200, 200, fill=gradient('lemonChiffon', 'gold'))

def onMouseMove(mouseX, mouseY):
    # Change the width and height of the oval based on mouse position.
    # Make sure there are no issues when mouseX or mouseY is 0!
    o.width = mouseX + 1
    o.height = mouseY + 1

onMouseMove(0, 250)
onMouseMove(0, 300)


# -
app.background = gradient('skyBlue', 'lightBlue', start='top')

o = Oval(200, 200, 200, 200, fill=gradient('lemonChiffon', 'gold'))

def onMouseMove(mouseX, mouseY):
    # Change the width and height of the oval based on mouse position.
    # Make sure there are no issues when mouseX or mouseY is 0!
    o.width = mouseX + 1
    o.height = mouseY + 1

onMouseMove(300, 100)

