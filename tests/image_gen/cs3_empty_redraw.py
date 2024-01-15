def onAppStart(app):
    app.items = ['x']

def onMousePress(app, x, y):
    app.items = []

def redrawAll(app):
    for item in app.items:
        drawLabel(item, 200, 200)
