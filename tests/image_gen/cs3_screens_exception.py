def onAppStart(app):
    pass

def a_onAppStart(app):
    pass

def b_onAppStart(app):
    pass

def a_onMousePress(app, mouseX, mouseY):
    assertRaises(lambda: setActiveScreen('b'), "Screen 'b' requires 'b_redrawAll()'")

def a_redrawAll(app):
    # Just for funsies, the point of the test is to ensure an exception is raised
    # when trying to activate a screen without an associated redrawAll definition
    drawRect(0, 0, 400, 400, fill="forestGreen")
    drawPolygon(200, 60, 340, 200, 200, 340, 60, 200, fill='gold')
    drawCircle(200, 200, 70, fill='darkBlue')
