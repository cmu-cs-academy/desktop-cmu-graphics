app.background = 'black'

light = Circle(200, 200, 55, fill='white', visible=False)
message = Label('Delighted.', 200, 200, size=48)

Label('How did the dog feel when', 200, 30, fill='gold', size=24)
Label('he lost his flashlight?', 200, 60, fill='gold', size=24)
Label('Turn on the flashlight to find the answer!', 200, 370, fill='gold',
      size=15)

def onMouseRelease(mouseX, mouseY):
    # The light should disappear.
    light.visible = False
def onMouseDrag(mouseX, mouseY):
    # The light should appear and follow the mouse.
    light.visible = True
    light.centerX = mouseX
    light.centerY = mouseY

onMouseRelease(200, 340)
onMouseDrag(120, 250)


# -
app.background = 'black'

light = Circle(200, 200, 55, fill='white', visible=False)
message = Label('Delighted.', 200, 200, size=48)

Label('How did the dog feel when', 200, 30, fill='gold', size=24)
Label('he lost his flashlight?', 200, 60, fill='gold', size=24)
Label('Turn on the flashlight to find the answer!', 200, 370, fill='gold',
      size=15)

def onMouseRelease(mouseX, mouseY):
    # The light should disappear.
    light.visible = False
def onMouseDrag(mouseX, mouseY):
    # The light should appear and follow the mouse.
    light.visible = True
    light.centerX = mouseX
    light.centerY = mouseY

onMouseDrag(250, 200)
onMouseRelease(300, 200)
onMouseDrag(100, 250)
onMouseRelease(100, 50)
onMouseDrag(100, 50)


# -
app.background = 'black'

light = Circle(200, 200, 55, fill='white', visible=False)
message = Label('Delighted.', 200, 200, size=48)

Label('How did the dog feel when', 200, 30, fill='gold', size=24)
Label('he lost his flashlight?', 200, 60, fill='gold', size=24)
Label('Turn on the flashlight to find the answer!', 200, 370, fill='gold',
      size=15)

def onMouseRelease(mouseX, mouseY):
    # The light should disappear.
    light.visible = False
def onMouseDrag(mouseX, mouseY):
    # The light should appear and follow the mouse.
    light.visible = True
    light.centerX = mouseX
    light.centerY = mouseY

onMouseDrag(250, 200)
onMouseRelease(300, 200)
onMouseDrag(100, 250)
onMouseRelease(100, 50)
onMouseDrag(100, 50)

