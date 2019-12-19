app.background = 'powderBlue'
skyMask = Rect(0, 0, 400, 400, opacity=0)

sun = Circle(200, 200, 80, fill=gradient('yellow', 'gold'))
sunMask = Circle(200, 200, 80, fill='orangeRed', opacity=0)

moon = Circle(0, 200, 78, fill=gradient('grey', 'powderBlue', start='left'))
moonMask = Circle(0, 200, 78, opacity=0)

def onKeyPress(key):
    # When the space key is pressed, move the moon and moonMask.
    if (key == 'space'):
        moon.centerX += 20
        moonMask.centerX += 20
    # If the moon's center value is off the canvas, set the moon and moonMask
    # back to their initial x-values and set all of the masks' opacities to 0.
    if (moon.centerX >= 400):
        moon.centerX = 20
        moonMask.centerX = 20
        skyMask.opacity = 0
        sunMask.opacity = 0
        moonMask.opacity = 0
    # Decrease the opacities of the masks if the moon is to the right of the
    # sun. Otherwise, increase the opacities. Also, rotate the moon so that
    # the light side of the gradient is on the sun side.
    if (moon.centerX > 200):
        skyMask.opacity -= 10
        sunMask.opacity -= 10
        moonMask.opacity -= 10
        moon.rotateAngle = 180
    else:
        skyMask.opacity += 10
        sunMask.opacity += 10
        moonMask.opacity += 10
        moon.rotateAngle = 0

onKeyPresses('space', 200)


# -
app.background = 'powderBlue'
skyMask = Rect(0, 0, 400, 400, opacity=0)

sun = Circle(200, 200, 80, fill=gradient('yellow', 'gold'))
sunMask = Circle(200, 200, 80, fill='orangeRed', opacity=0)

moon = Circle(0, 200, 78, fill=gradient('grey', 'powderBlue', start='left'))
moonMask = Circle(0, 200, 78, opacity=0)

def onKeyPress(key):
    # When the space key is pressed, move the moon and moonMask.
    if (key == 'space'):
        moon.centerX += 20
        moonMask.centerX += 20
    # If the moon's center value is off the canvas, set the moon and moonMask
    # back to their initial x-values and set all of the masks' opacities to 0.
    if (moon.centerX >= 400):
        moon.centerX = 20
        moonMask.centerX = 20
        skyMask.opacity = 0
        sunMask.opacity = 0
        moonMask.opacity = 0
    # Decrease the opacities of the masks if the moon is to the right of the
    # sun. Otherwise, increase the opacities. Also, rotate the moon so that
    # the light side of the gradient is on the sun side.
    if (moon.centerX > 200):
        skyMask.opacity -= 10
        sunMask.opacity -= 10
        moonMask.opacity -= 10
        moon.rotateAngle = 180
    else:
        skyMask.opacity += 10
        sunMask.opacity += 10
        moonMask.opacity += 10
        moon.rotateAngle = 0

onKeyPresses('space', 200)


# -
app.background = 'powderBlue'
skyMask = Rect(0, 0, 400, 400, opacity=0)

sun = Circle(200, 200, 80, fill=gradient('yellow', 'gold'))
sunMask = Circle(200, 200, 80, fill='orangeRed', opacity=0)

moon = Circle(0, 200, 78, fill=gradient('grey', 'powderBlue', start='left'))
moonMask = Circle(0, 200, 78, opacity=0)

def onKeyPress(key):
    # When the space key is pressed, move the moon and moonMask.
    if (key == 'space'):
        moon.centerX += 20
        moonMask.centerX += 20
    # If the moon's center value is off the canvas, set the moon and moonMask
    # back to their initial x-values and set all of the masks' opacities to 0.
    if (moon.centerX >= 400):
        moon.centerX = 20
        moonMask.centerX = 20
        skyMask.opacity = 0
        sunMask.opacity = 0
        moonMask.opacity = 0
    # Decrease the opacities of the masks if the moon is to the right of the
    # sun. Otherwise, increase the opacities. Also, rotate the moon so that
    # the light side of the gradient is on the sun side.
    if (moon.centerX > 200):
        skyMask.opacity -= 10
        sunMask.opacity -= 10
        moonMask.opacity -= 10
        moon.rotateAngle = 180
    else:
        skyMask.opacity += 10
        sunMask.opacity += 10
        moonMask.opacity += 10
        moon.rotateAngle = 0

onKeyPresses('space', 19)
onKeyPress('space')
onKeyPress('space')
onKeyPress('space')
onKeyPress('space')

