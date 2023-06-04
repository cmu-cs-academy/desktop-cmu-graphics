"""A simple demo of using a PS4 controller to move a circle."""
from cmu_graphics import *
import sys

class Player(object):
    def __init__(self, cx, cy):
        self.body = Circle(cx, cy, 7, fill = 'white', border = 'black')
        self.dx = 3
        self.dy = 3

    def getBigger(self):
        self.body.radius += 1

    def getSmaller(self):
        self.body.radius -= 1

def onJoyPress(button, joystick):
    """Pressing Triangle and X triggers a size change in the circle"""
    if button == "3":
        player.getBigger()
    elif button == "0":
        player.getSmaller()

def onJoyButtonHold(button, joystick):
    """This handles movement from the DPAD
    Pushing the DPAD results in buttons H0-H3 being pushed
    Not all operating systems support this properly.
    (Mac, for example, seems to have some trouble.)
    """
    if 'H0' in button:
        player.body.centerY -= player.dy
    elif 'H2' in button:
        player.body.centerY += player.dy

    if 'H3' in button:
        player.body.centerX -= player.dx
    elif 'H1' in button:
        player.body.centerX += player.dx

def onDigitalJoyAxis(results, joystick):
    """This handles movement using the left analog stick.
    Axis 1 is Up/Down (-1 up, 1 down)
    Axis 0 is Left/Right (-1 left, 1 right)
    So, (1,-1) is up, while (0,1) is right.
    """
    if (1, -1) in results:
        player.body.centerY -= player.dy
    elif (1, 1) in results:
        player.body.centerY += player.dy

    if (0, -1) in results:
        player.body.centerX -= player.dx
    elif (0, 1) in results:
        player.body.centerX += player.dx

player = Player(200, 75)
cmu_graphics.run()