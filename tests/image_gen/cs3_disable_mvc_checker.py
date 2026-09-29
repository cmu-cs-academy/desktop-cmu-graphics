# app.disableMvcChecker has to turn off both layers of the checker: the direct
# check that runs when an app attribute is set during redrawAll, and the
# appHash comparison that catches changes deeper in the model.
def onAppStart(app):
    app.disableMvcChecker = True
    app.v1 = 0
    app.v2 = [0]

def redrawAll(app):
    app.v1 += 1
    drawRect(0, 0, 50, 50)
# -
def onAppStart(app):
    app.disableMvcChecker = True
    app.v1 = 0
    app.v2 = [0]

def redrawAll(app):
    app.v2[0] += 1
    drawRect(0, 0, 50, 50)
