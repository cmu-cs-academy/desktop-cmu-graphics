from cmu_graphics import *

# Mouse moves are throttled, but a click still lands where the cursor really
# is, and the last position of a burst of moves is delivered, not dropped.
# The blue press (on its orange release) should be at the end of the diagonal
# burst, and the green square marks the final onMouseMove position.

def onAppStart(app):
    # Slower than the mouse throttle, so each burst starts unthrottled
    app.stepsPerSecond = 10
    app.stepNum = 0
    app.moves = []
    app.presses = []
    app.releases = []

def onMouseMove(app, mouseX, mouseY):
    app.moves.append((mouseX, mouseY))

def onMousePress(app, mouseX, mouseY):
    app.presses.append((mouseX, mouseY))

def onMouseRelease(app, mouseX, mouseY):
    app.releases.append((mouseX, mouseY))

def redrawAll(app):
    for x, y in app.moves:
        drawRect(x - 3, y - 3, 6, 6, fill='gray')
    for x, y in app.releases:
        drawRect(x - 8, y - 8, 16, 16, fill='orange')
    for x, y in app.presses:
        drawRect(x - 5, y - 5, 10, 10, fill='blue')
    if app.moves:
        x, y = app.moves[-1]
        drawRect(x - 5, y - 5, 10, 10, fill='green')

def onStep(app):
    app.stepNum += 1
    n = app.stepNum
    if n == 2:
        injectMouseMove(50, 50)
    elif n == 4:
        # All within one throttle window: only the first is sent right away
        for i in range(1, 6):
            injectMouseMove(50 + 50 * i, 50 + 50 * i)
        injectMousePress()
        injectMouseRelease()
    elif n == 7:
        # No click follows, so the second move must be sent once the
        # throttle window passes
        injectMouseMove(320, 80)
        injectMouseMove(340, 60)
    elif n == 10:
        screenshotAndQuit()

runApp()
