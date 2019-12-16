app.background = gradient('deepSkyBlue', 'lightBlue', start='top')

sun = Circle(200, 100, 50, fill='yellow')
moon = Circle(300, 100, 50, fill=gradient('gainsboro', 'white'), opacity=70,
              visible=False)
ground = Rect(0, 300, 400, 100, fill='mediumSeaGreen')

def changeFillsAndMoon(newSkyFill, newSunFill, newGroundFill, showMoon):
    app.background = newSkyFill
    sun.fill = newSunFill
    ground.fill = newGroundFill

    # Depending on the showMoon input parameter, change the visibility of the moon.
    if (showMoon == True):
        moon.visible = True
    else:
        moon.visible = False

def onMouseMove(mouseX, mouseY):
    sun.centerX = mouseX
    sun.centerY = mouseY

    # Change the fill of the sky. Also change the moon's visibility if the
    # sun has set.
    if (sun.top > ground.top):
        changeFillsAndMoon(gradient('black', 'midnightBlue', start='top'),
                           None, 'darkGreen', True)
    elif (sun.centerY > 250):
        changeFillsAndMoon(gradient('skyBlue', 'lightPink', start='top'),
                           'gold', 'seaGreen', False)
    elif (sun.centerY > 100):
        changeFillsAndMoon(gradient('deepSkyBlue', 'lightBlue', start='top'),
                           'yellow', 'mediumSeaGreen', False)
    else:
        changeFillsAndMoon('lightSkyBlue', 'yellow', 'mediumSeaGreen', False)

onMouseMove(200, 251)


# -
app.background = gradient('deepSkyBlue', 'lightBlue', start='top')

sun = Circle(200, 100, 50, fill='yellow')
moon = Circle(300, 100, 50, fill=gradient('gainsboro', 'white'), opacity=70,
              visible=False)
ground = Rect(0, 300, 400, 100, fill='mediumSeaGreen')

def changeFillsAndMoon(newSkyFill, newSunFill, newGroundFill, showMoon):
    app.background = newSkyFill
    sun.fill = newSunFill
    ground.fill = newGroundFill

    # Depending on the showMoon input parameter, change the visibility of the moon.
    if (showMoon == True):
        moon.visible = True
    else:
        moon.visible = False

def onMouseMove(mouseX, mouseY):
    sun.centerX = mouseX
    sun.centerY = mouseY

    # Change the fill of the sky. Also change the moon's visibility if the
    # sun has set.
    if (sun.top > ground.top):
        changeFillsAndMoon(gradient('black', 'midnightBlue', start='top'),
                           None, 'darkGreen', True)
    elif (sun.centerY > 250):
        changeFillsAndMoon(gradient('skyBlue', 'lightPink', start='top'),
                           'gold', 'seaGreen', False)
    elif (sun.centerY > 100):
        changeFillsAndMoon(gradient('deepSkyBlue', 'lightBlue', start='top'),
                           'yellow', 'mediumSeaGreen', False)
    else:
        changeFillsAndMoon('lightSkyBlue', 'yellow', 'mediumSeaGreen', False)



# -
app.background = gradient('deepSkyBlue', 'lightBlue', start='top')

sun = Circle(200, 100, 50, fill='yellow')
moon = Circle(300, 100, 50, fill=gradient('gainsboro', 'white'), opacity=70,
              visible=False)
ground = Rect(0, 300, 400, 100, fill='mediumSeaGreen')

def changeFillsAndMoon(newSkyFill, newSunFill, newGroundFill, showMoon):
    app.background = newSkyFill
    sun.fill = newSunFill
    ground.fill = newGroundFill

    # Depending on the showMoon input parameter, change the visibility of the moon.
    if (showMoon == True):
        moon.visible = True
    else:
        moon.visible = False

def onMouseMove(mouseX, mouseY):
    sun.centerX = mouseX
    sun.centerY = mouseY

    # Change the fill of the sky. Also change the moon's visibility if the
    # sun has set.
    if (sun.top > ground.top):
        changeFillsAndMoon(gradient('black', 'midnightBlue', start='top'),
                           None, 'darkGreen', True)
    elif (sun.centerY > 250):
        changeFillsAndMoon(gradient('skyBlue', 'lightPink', start='top'),
                           'gold', 'seaGreen', False)
    elif (sun.centerY > 100):
        changeFillsAndMoon(gradient('deepSkyBlue', 'lightBlue', start='top'),
                           'yellow', 'mediumSeaGreen', False)
    else:
        changeFillsAndMoon('lightSkyBlue', 'yellow', 'mediumSeaGreen', False)

onMouseMove(200, 251)

