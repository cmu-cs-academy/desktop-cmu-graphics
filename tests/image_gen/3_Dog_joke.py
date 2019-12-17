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

onMouseDrag(200, 200)


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

onMouseDrag(280, 300)
onMouseDrag(370, 350)
onMouseDrag(330, 320)
onMouseDrag(50, 130)
onMouseDrag(200, 200)


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


