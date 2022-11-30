calledStart = False
calledActivated = False

def a_onScreenStart(app):
    global calledStart
    assert not calledStart
    calledStart = True

def a_onScreenActivated(app):
    global calledActivated
    assert calledStart
    calledActivated = True

def a_redrawAll(app):
    assert calledStart and calledActivated
    drawRect(0,0,200,200,fill='blue')

def b_redrawAll(app):
    drawRect(0,0,200,200,fill='red')

