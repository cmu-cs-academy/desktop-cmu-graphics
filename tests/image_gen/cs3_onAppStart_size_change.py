# Ensures setting width and height in onAppStart has an effect on the 
# rest of the program

WIDTH, HEIGHT = 600, 500

def onAppStart(app):
    app.width, app.height = WIDTH, HEIGHT

def onKeyPress(app, key):
    assert(app.width, app.height == (WIDTH, HEIGHT))

def redrawAll(app):
    assert(app.width, app.height == (WIDTH, HEIGHT))
    drawRect(0, 0, 200, 200, fill='blue')
