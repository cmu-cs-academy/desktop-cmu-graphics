from cmu_graphics import *

def a_onMousePress(app, mouseX, mouseY):
    setActiveScreen('b')

def a_redrawAll(app):
    pass

def b_onScreenActivate(app):
    app.width = 400
    app.height = 400
    app.x = 5

def b_redrawAll(app):
    drawRect(0,0,200,200,fill="blue")
    assert hasattr(app,"x")