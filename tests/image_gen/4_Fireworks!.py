app.background = 'black'

# background hills
Polygon(140, 400, 220, 310, 245, 330, 270, 290, 290, 300, 330, 245, 465, 400,
        fill=rgb(13, 34, 39))
Polygon(0, 400, 60, 310, 100, 365, 135, 345, 190, 400, fill=rgb(15, 24, 35))

fireworkTrail = Line(200, 380, 200, 580,
                     fill=gradient('red', 'yellow', 'black', start='top'))
firework = Star(200, 150, 150, 12, fill=None,
                border=gradient('red', 'yellow', 'black'), roundness=10,
                dashes=True, visible=False)

def explodeFirework():
    firework.centerY = fireworkTrail.top
    fireworkTrail.visible = False
    firework.visible = True

def onKeyPress(key):
    # Resets the firework on 'enter'.
    if (key == 'enter'):
        fireworkTrail.visible = True
        fireworkTrail.top = 380
        firework.visible = False

    # If space is pressed, explode the firework.
    if (key == 'space'):
        explodeFirework()

def onKeyHold(keys):
    if (firework.visible == False):
        # If left or right are held and the firework is not too close to the
        # edge of the canvas, move it in the corresponding direction by 5 pixels.
        if (('left' in keys) and (fireworkTrail.centerX > 15)):
            fireworkTrail.centerX -= 5
            firework.centerX -= 5
        elif (('right' in keys) and (fireworkTrail.centerX < 385)):
            fireworkTrail.centerX += 5
            firework.centerX += 5

        # If 'up' is held, keep moving the firework up.
        if ('up' in keys):
            fireworkTrail.top -= 5

    # Once at a height of 150, explode the firework.
    if (fireworkTrail.y1 <= 150):
        explodeFirework()

onKeyHolds(['up'], 50)


# -
app.background = 'black'

# background hills
Polygon(140, 400, 220, 310, 245, 330, 270, 290, 290, 300, 330, 245, 465, 400,
        fill=rgb(13, 34, 39))
Polygon(0, 400, 60, 310, 100, 365, 135, 345, 190, 400, fill=rgb(15, 24, 35))

fireworkTrail = Line(200, 380, 200, 580,
                     fill=gradient('red', 'yellow', 'black', start='top'))
firework = Star(200, 150, 150, 12, fill=None,
                border=gradient('red', 'yellow', 'black'), roundness=10,
                dashes=True, visible=False)

def explodeFirework():
    firework.centerY = fireworkTrail.top
    fireworkTrail.visible = False
    firework.visible = True

def onKeyPress(key):
    # Resets the firework on 'enter'.
    if (key == 'enter'):
        fireworkTrail.visible = True
        fireworkTrail.top = 380
        firework.visible = False

    # If space is pressed, explode the firework.
    if (key == 'space'):
        explodeFirework()

def onKeyHold(keys):
    if (firework.visible == False):
        # If left or right are held and the firework is not too close to the
        # edge of the canvas, move it in the corresponding direction by 5 pixels.
        if (('left' in keys) and (fireworkTrail.centerX > 15)):
            fireworkTrail.centerX -= 5
            firework.centerX -= 5
        elif (('right' in keys) and (fireworkTrail.centerX < 385)):
            fireworkTrail.centerX += 5
            firework.centerX += 5

        # If 'up' is held, keep moving the firework up.
        if ('up' in keys):
            fireworkTrail.top -= 5

    # Once at a height of 150, explode the firework.
    if (fireworkTrail.y1 <= 150):
        explodeFirework()

onKeyHolds(['left'], 5)


# -
app.background = 'black'

# background hills
Polygon(140, 400, 220, 310, 245, 330, 270, 290, 290, 300, 330, 245, 465, 400,
        fill=rgb(13, 34, 39))
Polygon(0, 400, 60, 310, 100, 365, 135, 345, 190, 400, fill=rgb(15, 24, 35))

fireworkTrail = Line(200, 380, 200, 580,
                     fill=gradient('red', 'yellow', 'black', start='top'))
firework = Star(200, 150, 150, 12, fill=None,
                border=gradient('red', 'yellow', 'black'), roundness=10,
                dashes=True, visible=False)

def explodeFirework():
    firework.centerY = fireworkTrail.top
    fireworkTrail.visible = False
    firework.visible = True

def onKeyPress(key):
    # Resets the firework on 'enter'.
    if (key == 'enter'):
        fireworkTrail.visible = True
        fireworkTrail.top = 380
        firework.visible = False

    # If space is pressed, explode the firework.
    if (key == 'space'):
        explodeFirework()

def onKeyHold(keys):
    if (firework.visible == False):
        # If left or right are held and the firework is not too close to the
        # edge of the canvas, move it in the corresponding direction by 5 pixels.
        if (('left' in keys) and (fireworkTrail.centerX > 15)):
            fireworkTrail.centerX -= 5
            firework.centerX -= 5
        elif (('right' in keys) and (fireworkTrail.centerX < 385)):
            fireworkTrail.centerX += 5
            firework.centerX += 5

        # If 'up' is held, keep moving the firework up.
        if ('up' in keys):
            fireworkTrail.top -= 5

    # Once at a height of 150, explode the firework.
    if (fireworkTrail.y1 <= 150):
        explodeFirework()

onKeyHolds(['right'], 5)

