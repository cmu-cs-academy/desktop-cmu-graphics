from cmu_graphics import *

c = Circle(200, 200, 50)
g = Group(c)

def onMousePress(x,y):
    g.clear()
    print(c.visible)

cmu_graphics.loop()
