from cmu_graphics import *

# onMouseDrag fires while any button is held, with every held button, and
# onMouseMove fires otherwise. Green squares are left-button drags, blue are
# left+right drags, gray are plain moves.

def onAppStart(app):
    # Slower than the mouse throttle, so no two injected moves get merged
    app.stepsPerSecond = 10
    app.stepNum = 0
    app.moves = []
    app.drags = []
    app.presses = []
    app.releases = []

def onMouseMove(app, mouseX, mouseY):
    app.moves.append((mouseX, mouseY))

def onMouseDrag(app, mouseX, mouseY, buttons):
    app.drags.append((mouseX, mouseY, buttons))

def onMousePress(app, mouseX, mouseY, button):
    app.presses.append((mouseX, mouseY))

def onMouseRelease(app, mouseX, mouseY, button):
    app.releases.append((mouseX, mouseY))

def redrawAll(app):
    for x, y in app.releases:
        drawRect(x - 8, y - 8, 16, 16, fill='orange')
    for x, y in app.presses:
        drawRect(x - 6, y - 6, 12, 12, fill='black')
    for x, y, buttons in app.drags:
        if buttons == [0]:
            color = 'green'
        elif buttons == [0, 2]:
            color = 'blue'
        else:
            color = 'red'
        drawRect(x - 4, y - 4, 8, 8, fill=color)
    for x, y in app.moves:
        drawRect(x - 3, y - 3, 6, 6, fill='gray')

def onStep(app):
    app.stepNum += 1
    n = app.stepNum
    if n == 2:
        injectMouseMove(50, 100)
    elif n == 3:
        injectMousePress(0)
    elif 4 <= n <= 8:
        injectMouseMove(50 + 50 * (n - 3), 100)
    elif n == 9:
        injectMousePress(2)
    elif 10 <= n <= 12:
        injectMouseMove(300, 100 + 50 * (n - 9))
    elif n == 13:
        injectMouseRelease(2)
    elif n == 14:
        injectMouseRelease(0)
    elif n == 15:
        injectMouseMove(350, 300)
    elif n == 17:
        screenshotAndQuit()

runApp()
