# sky
sky = Rect(0, 0, 400, 600, fill=gradient('skyBlue', 'lightSkyBlue', 'pink',
                                         'lightSalmon', start='top'))

# sun
outerSun = Circle(200, 0, 5, fill='orange', opacity=50)
innerSun = Circle(200, 0, 70, fill='gold')

# ocean
topWave = Rect(0, 200, 400, 60, fill='dodgerBlue')
midWave = Rect(0, 260, 400, 40, fill='deepSkyBlue')
lowWave = Rect(0, 300, 400, 200, fill='turquoise')

# The sun's reflections on the water.
sunReflections = Group(
    Oval(200, 204, 120, 5, fill='gold'),
    Oval(165, 210, 80, 5, fill='gold'),
    Oval(255, 210, 70, 5, fill='gold'),
    Oval(230, 217, 95, 5, fill='gold'),
    Oval(190, 223, 60, 5, fill='gold'),
    Oval(235, 232, 60, 5, fill='gold'),
    Oval(155, 232, 60, 5, fill='gold')
    )
sunReflections.opacity = 0

# foam
Polygon(0, 400, 0, 280, 300, 335, 400, 320, 400, 400, fill='white')

# sand
Polygon(0, 400, 0, 290, 300, 360, 400, 330, 400, 400, fill='wheat')
Polygon(0, 335, 400, 390, 400, 400, 0, 400, fill='burlyWood')

def onMouseMove(mouseX, mouseY):
    # Move the waves.
    topWave.height = 40 + (mouseY / 60)
    midWave.top = topWave.bottom
    midWave.height = 30 + (mouseY / 20)
    lowWave.top = midWave.bottom

def onStep():
    # As long as the sun hasn't reached the horizon, make the sun reflections
    # gradually appear.
    if (innerSun.centerY < 200):
        if ((sunReflections.opacity < 100) and (innerSun.bottom > 200)):
            sunReflections.opacity += 3

        # Change the sky color (shift the sky down).
        sky.top -= 5

        # Move the sun and increase the radius of the glow.
        innerSun.centerY += 3
        outerSun.centerY += 3
        outerSun.radius = innerSun.centerY / 2


