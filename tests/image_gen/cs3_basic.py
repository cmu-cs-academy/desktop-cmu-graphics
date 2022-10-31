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

def onAppStart(app):
    assertRaises(lambda: Rect(0, 0, 200, 200))

# -

def onMousePress(app, mouseX, mouseY):
    a = 1 / 0
