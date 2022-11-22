def redrawAll(app):
    drawRect(0,0,200,200,fill='blue')

# -

def onAppStart(app):
    app.centers = []

def onMousePress(app, mouseX, mouseY):
    app.centers.append((mouseX, mouseY))

def redrawAll(app):
    for cx, cy in app.centers:
        drawCircle(cx, cy, 40, fill='orange')

# -

# Make sure you can't use CS1 shapes in CS3 mode
def onMousePress(app, mouseX, mouseY):
    assertRaises(lambda: Rect(0, 0, 200, 200))

# -

# Make sure the red error box appears
def onMousePress(app, mouseX, mouseY):
    a = 1 / 0

# Label
# ^ included to trick the test_image_gen harness into giving us some extra
# wiggle room. The red error box does include labels, so the Windows result
# looks a litttle different from the mac one.

# -

# app.paused should not be available in CS3 mode
def onMousePress(app, mouseX, mouseY):
    print(app.paused)

# Label
# ^ included to trick the test_image_gen harness into giving us some extra
# wiggle room. The red error box does include labels, so the Windows result
# looks a litttle different from the mac one.