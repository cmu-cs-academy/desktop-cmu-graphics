from cmu_graphics import *

def a_onMousePress(app, mouseX, mouseY):
    setActiveScreen('b')

def a_redrawAll(app):
    pass

# Setting app.width and app.height should not immediately
# trigger a call to onResize and redrawAll. If it does,
# b_redrawAll will be called before app.x is set
def b_onScreenActivate(app):
    app.width = 400
    app.height = 400
    app.x = 5

def b_onResize(app):
    pass

def b_redrawAll(app):
    drawRect(0,0,200,200,fill="blue")
    assert hasattr(app,"x")