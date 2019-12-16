app.background = gradient('cornSilk', 'tan', start='top')

Polygon(30, 400, 275, 365, 400, 400, fill='cornSilk')
Polygon(170, 400, 275, 385, 330, 400, fill='royalBlue')

footsteps = Group()

def drawFootstep(x, y):
    newFootstep = Group(
        Arc(x, y - 5, 22, 40, 220, 280, fill='burlyWood'),
        Polygon(x, y - 5, x - 7, y + 10, x + 7, y + 10, fill='burlyWood'),
        Rect(x, y + 15, 16, 5, fill='burlyWood', align='top'),
        Arc(x, y + 20, 16, 16, 90, 180, fill='burlyWood')
        )

    footsteps.add(newFootstep)

def onMousePress(mouseX, mouseY):
    for footstep in footsteps.children:
        # If the footstep's opacity is greater than 0, integer divide it in half.
        # Otherwise, remove it from the group.
        if (footstep.opacity > 0):
            footstep.opacity = footstep.opacity // 2
        else:
            footsteps.remove(footstep)
    drawFootstep(mouseX, mouseY)

onMousePress(100, 200)
onMousePress(120, 180)
onMousePress(140, 220)
onMousePress(160, 160)
onMousePress(180, 240)
onMousePress(200, 140)
onMousePress(220, 260)
onMousePress(240, 120)
onMousePress(260, 280)


# -
app.background = gradient('cornSilk', 'tan', start='top')

Polygon(30, 400, 275, 365, 400, 400, fill='cornSilk')
Polygon(170, 400, 275, 385, 330, 400, fill='royalBlue')

footsteps = Group()

def drawFootstep(x, y):
    newFootstep = Group(
        Arc(x, y - 5, 22, 40, 220, 280, fill='burlyWood'),
        Polygon(x, y - 5, x - 7, y + 10, x + 7, y + 10, fill='burlyWood'),
        Rect(x, y + 15, 16, 5, fill='burlyWood', align='top'),
        Arc(x, y + 20, 16, 16, 90, 180, fill='burlyWood')
        )

    footsteps.add(newFootstep)

def onMousePress(mouseX, mouseY):
    for footstep in footsteps.children:
        # If the footstep's opacity is greater than 0, integer divide it in half.
        # Otherwise, remove it from the group.
        if (footstep.opacity > 0):
            footstep.opacity = footstep.opacity // 2
        else:
            footsteps.remove(footstep)
    drawFootstep(mouseX, mouseY)

onMousePress(100, 320)


# -
app.background = gradient('cornSilk', 'tan', start='top')

Polygon(30, 400, 275, 365, 400, 400, fill='cornSilk')
Polygon(170, 400, 275, 385, 330, 400, fill='royalBlue')

footsteps = Group()

def drawFootstep(x, y):
    newFootstep = Group(
        Arc(x, y - 5, 22, 40, 220, 280, fill='burlyWood'),
        Polygon(x, y - 5, x - 7, y + 10, x + 7, y + 10, fill='burlyWood'),
        Rect(x, y + 15, 16, 5, fill='burlyWood', align='top'),
        Arc(x, y + 20, 16, 16, 90, 180, fill='burlyWood')
        )

    footsteps.add(newFootstep)

def onMousePress(mouseX, mouseY):
    for footstep in footsteps.children:
        # If the footstep's opacity is greater than 0, integer divide it in half.
        # Otherwise, remove it from the group.
        if (footstep.opacity > 0):
            footstep.opacity = footstep.opacity // 2
        else:
            footsteps.remove(footstep)
    drawFootstep(mouseX, mouseY)

onMousePress(100, 320)

