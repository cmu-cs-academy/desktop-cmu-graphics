def drawMountains():
    Polygon(0, 175, 150, 175, 50, 100, fill='steelBlue')
    Polygon(210, 175, 400, 175, 300, 100, fill='midnightBlue')
    Polygon(50, 175, 190, 175, 130, 120, fill='midnightBlue')

def drawOcean():
    Polygon(0, 285, 180, 175, 0, 175, fill='dodgerBlue')
    Polygon(0, 285, 180, 175, 190, 175, 0, 350, fill='tan')

def drawGroundAndSky(groundColor):
    Rect(0, 0, 400, 175, fill='lightSkyBlue')
    Rect(0, 175, 400, 225, fill=groundColor)
    Polygon(0, 350, 0, 400, 400, 400, 400, 350, 210, 175, 190, 175, fill='grey')
    Line(200, 175, 200, 400, lineWidth=10, dashes=True,
         fill=gradient('grey', 'silver', start='top'))

def drawScene(isMountainous, isDesert, isBeach, isNightTime, destination,
              milesToGo):
    # Draw the ground and ocean based on the values of the first three parameters.
    if (isMountainous == True):
        drawGroundAndSky('lightGreen')
        drawMountains()
    elif (isDesert == True):
        drawGroundAndSky('burlyWood')
    elif (isBeach == True):
        drawGroundAndSky('lightGreen')
        drawOcean()

    # Draw the sign board with destination and milesToGo.
    Line(290, 230, 290, 200)
    Line(370, 230, 370, 200)
    Rect(330, 200, 100, 60, fill='green', border='white', align='bottom')
    Label(destination, 330, 160, fill='white', size=16)
    Label(milesToGo, 330, 180, fill='white', size=18)

    # Make the scene darker if it is night-time.
    if (isNightTime == True):
        Rect(0, 0, 400, 400, opacity=50)


drawScene(True, True, False, False, 'Pittsburgh', 35)


# -
def drawMountains():
    Polygon(0, 175, 150, 175, 50, 100, fill='steelBlue')
    Polygon(210, 175, 400, 175, 300, 100, fill='midnightBlue')
    Polygon(50, 175, 190, 175, 130, 120, fill='midnightBlue')

def drawOcean():
    Polygon(0, 285, 180, 175, 0, 175, fill='dodgerBlue')
    Polygon(0, 285, 180, 175, 190, 175, 0, 350, fill='tan')

def drawGroundAndSky(groundColor):
    Rect(0, 0, 400, 175, fill='lightSkyBlue')
    Rect(0, 175, 400, 225, fill=groundColor)
    Polygon(0, 350, 0, 400, 400, 400, 400, 350, 210, 175, 190, 175, fill='grey')
    Line(200, 175, 200, 400, lineWidth=10, dashes=True,
         fill=gradient('grey', 'silver', start='top'))

def drawScene(isMountainous, isDesert, isBeach, isNightTime, destination,
              milesToGo):
    # Draw the ground and ocean based on the values of the first three parameters.
    if (isMountainous == True):
        drawGroundAndSky('lightGreen')
        drawMountains()
    elif (isDesert == True):
        drawGroundAndSky('burlyWood')
    elif (isBeach == True):
        drawGroundAndSky('lightGreen')
        drawOcean()

    # Draw the sign board with destination and milesToGo.
    Line(290, 230, 290, 200)
    Line(370, 230, 370, 200)
    Rect(330, 200, 100, 60, fill='green', border='white', align='bottom')
    Label(destination, 330, 160, fill='white', size=16)
    Label(milesToGo, 330, 180, fill='white', size=18)

    # Make the scene darker if it is night-time.
    if (isNightTime == True):
        Rect(0, 0, 400, 400, opacity=50)


drawScene(True, True, False, False, 'Pittsburgh', 35)


# -
def drawMountains():
    Polygon(0, 175, 150, 175, 50, 100, fill='steelBlue')
    Polygon(210, 175, 400, 175, 300, 100, fill='midnightBlue')
    Polygon(50, 175, 190, 175, 130, 120, fill='midnightBlue')

def drawOcean():
    Polygon(0, 285, 180, 175, 0, 175, fill='dodgerBlue')
    Polygon(0, 285, 180, 175, 190, 175, 0, 350, fill='tan')

def drawGroundAndSky(groundColor):
    Rect(0, 0, 400, 175, fill='lightSkyBlue')
    Rect(0, 175, 400, 225, fill=groundColor)
    Polygon(0, 350, 0, 400, 400, 400, 400, 350, 210, 175, 190, 175, fill='grey')
    Line(200, 175, 200, 400, lineWidth=10, dashes=True,
         fill=gradient('grey', 'silver', start='top'))

def drawScene(isMountainous, isDesert, isBeach, isNightTime, destination,
              milesToGo):
    # Draw the ground and ocean based on the values of the first three parameters.
    if (isMountainous == True):
        drawGroundAndSky('lightGreen')
        drawMountains()
    elif (isDesert == True):
        drawGroundAndSky('burlyWood')
    elif (isBeach == True):
        drawGroundAndSky('lightGreen')
        drawOcean()

    # Draw the sign board with destination and milesToGo.
    Line(290, 230, 290, 200)
    Line(370, 230, 370, 200)
    Rect(330, 200, 100, 60, fill='green', border='white', align='bottom')
    Label(destination, 330, 160, fill='white', size=16)
    Label(milesToGo, 330, 180, fill='white', size=18)

    # Make the scene darker if it is night-time.
    if (isNightTime == True):
        Rect(0, 0, 400, 400, opacity=50)


drawScene(False, False, True, False, 'Miami', 10)

