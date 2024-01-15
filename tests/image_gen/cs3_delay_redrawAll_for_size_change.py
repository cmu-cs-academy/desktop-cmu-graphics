# Setting app.width shouldn't immediately trigger a call to redrawAll

def onAppStart(app):
    app.width = 500
    app.xyz = 0

def redrawAll(app):
    assert(hasattr(app, 'xyz'))
    drawRect(0, 0, 200, 200, fill='blue')
