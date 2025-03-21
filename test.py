from cmu_graphics import *

def inRange(app, x1, y1, rx, ry, width, height):
    return rx <= x1 <= rx + width and ry <= y1 <= ry + height

def a_onMousePress(app, mouseX, mouseY):
    setActiveScreen('b')

def a_redrawAll(app):
    print("a redraw all start")
    drawRect(200,100,100,300, fill="yellow")
    # drawCircle(200,400,50, fill="yellow")
    # drawCircle(300,400,50, fill="yellow")

    print("a redraw all end")

def a_onScreenActivate(app):
    print("a on screen activate start")
    app.width = 600
    app.height = 600
    app.x = 5
    print("a on screen activate end")


def b_onScreenActivate(app):
    print("changed screens")
    print("b on screen activate start")
    app.width = 300
    app.height = 300
    app.x = 5
    app.color = "red"
    print("b on screen activate end")

def b_onResize(app):
    print("b on resized")
    app.color = "green"

def b_onMousePress(app, mouseX, mouseY):
    app.width = 400

def b_redrawAll(app):
    print("b redraw all start")
    drawRect(200,200,20,20,fill=app.color)
    print("b redraw all end")


runAppWithScreens('a')

# def onResize(app):
#     app.color = "green"

# def redrawAll(app):
#     print("b redraw all start")
#     drawRect(200,200,20,20,fill=app.color)
#     print("b redraw all end")

# def onAppStart(app):
#     app.color = "blue"
#     app.width = 300
#     app.height = 300


# def onMousePress(app, mouseX, mouseY):
#     app.width = 400

# runApp()