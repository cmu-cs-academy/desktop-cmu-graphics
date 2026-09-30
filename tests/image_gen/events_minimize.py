from cmu_graphics import *

# Windows reports a 0x0 size when a window is minimized. The app keeps
# running through that and draws normally once restored, without calling
# onResize for a size that didn't change. Red means onResize ran.

def onAppStart(app):
    app.stepNum = 0
    app.resizeCalls = 0

def onResize(app):
    app.resizeCalls += 1

def redrawAll(app):
    drawRect(100, 100, 200, 200, fill='green')
    if app.resizeCalls > 0:
        drawRect(0, 0, 50, 50, fill='red')

def onStep(app):
    app.stepNum += 1
    if app.stepNum == 2:
        injectResize(0, 0)
    elif app.stepNum == 4:
        injectResize(400, 400)
    elif app.stepNum == 8:
        screenshotAndQuit()

runApp(width=400, height=400)
