from cmu_graphics import *

# Setting app.width and app.height resizes the window, without calling
# onResize. The screenshot is only 400x400 if the window grew from 200x200.
# The blue square is in the bottom-right corner; red means onResize ran.

def onAppStart(app):
    app.stepNum = 0
    app.resizeCalls = 0

def onResize(app):
    app.resizeCalls += 1

def redrawAll(app):
    drawRect(app.width - 50, app.height - 50, 50, 50, fill='blue')
    if app.resizeCalls > 0:
        drawRect(0, 0, 50, 50, fill='red')

def onStep(app):
    app.stepNum += 1
    if app.stepNum == 2:
        app.width = 400
        app.height = 400
    elif app.stepNum == 15:
        screenshotAndQuit()

runApp(width=200, height=200)
