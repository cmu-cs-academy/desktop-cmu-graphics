from cmu_cs3_graphics import *
import random

def onAppStart(app):
    app.circles = []
    app.stepsPerSecond = 2
    app.steps = 0

def onStep(app):
    app.circles.append((random.randrange(0, app.width), random.randrange(0, app.height), random.randrange(10, 30), random.choice(['red', 'green', 'blue', 'orange', 'purple'])))
    app.steps += 1
    if app.steps == 5:
        raise Exception()

def redrawAll(app):
    for circle in app.circles:
        *circle, fill= circle
        drawCircle(*circle, fill=fill)

def onKeyPress(app, key):
    print(key)
    print(key / 0)

runApp()
