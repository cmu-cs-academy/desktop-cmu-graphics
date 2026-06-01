# Ensure redrawAll is called after setActiveScreen, even if onScreenActivate is
# not written

def a_onMousePress(app, mouseX, mouseY):
    setActiveScreen('b')

def a_redrawAll(app):
    drawCircle(200, 200, 100, fill='blue')

def b_redrawAll(app):
    drawRect(0, 0, 50, 100)