app.background = 'black'

t = Label('tickle', 200, 200, fill='cyan', size=50)
fadedTickles = Group()

def onMouseMove(mouseX, mouseY):
    # If the mouse moves over the tickle label, add a new tickle label to the
    # group. Also change the original label's center to a new random position!
    if (t.contains(mouseX, mouseY) == True):
        fadedTickles.add(
            Label('tickle', t.centerX, t.centerY, fill='cyan', size=50)
            )
        t.centerX += randrange(-10, 11)
        t.centerY += randrange(-10, 11)
def onStep():
    # Loop through each tickle label in the group and reduce opacity by 20.
    # If the opacity of the label is equal to 0, remove it from the group.
    for tickle in fadedTickles:
        tickle.opacity -= 20
        if (tickle.opacity == 0):
            fadedTickles.remove(tickle)

onMouseMove(200, 200)
onSteps(5)
app.paused = True


# -
app.background = 'black'

t = Label('tickle', 200, 200, fill='cyan', size=50)
fadedTickles = Group()

def onMouseMove(mouseX, mouseY):
    # If the mouse moves over the tickle label, add a new tickle label to the
    # group. Also change the original label's center to a new random position!
    if (t.contains(mouseX, mouseY) == True):
        fadedTickles.add(
            Label('tickle', t.centerX, t.centerY, fill='cyan', size=50)
            )
        t.centerX += randrange(-10, 11)
        t.centerY += randrange(-10, 11)
def onStep():
    # Loop through each tickle label in the group and reduce opacity by 20.
    # If the opacity of the label is equal to 0, remove it from the group.
    for tickle in fadedTickles:
        tickle.opacity -= 20
        if (tickle.opacity == 0):
            fadedTickles.remove(tickle)

onMouseMove(200, 200)
onSteps(5)
app.paused = True


# -
app.background = 'black'

t = Label('tickle', 200, 200, fill='cyan', size=50)
fadedTickles = Group()

def onMouseMove(mouseX, mouseY):
    # If the mouse moves over the tickle label, add a new tickle label to the
    # group. Also change the original label's center to a new random position!
    if (t.contains(mouseX, mouseY) == True):
        fadedTickles.add(
            Label('tickle', t.centerX, t.centerY, fill='cyan', size=50)
            )
        t.centerX += randrange(-10, 11)
        t.centerY += randrange(-10, 11)
def onStep():
    # Loop through each tickle label in the group and reduce opacity by 20.
    # If the opacity of the label is equal to 0, remove it from the group.
    for tickle in fadedTickles:
        tickle.opacity -= 20
        if (tickle.opacity == 0):
            fadedTickles.remove(tickle)

onMouseMove(200, 200)
app.paused = True

