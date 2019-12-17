app.background = 'black'
Rect(0, 0, 400, 250, fill=gradient(rgb(15, 25, 40), rgb(20, 40, 80), start='top'))

Circle(130, 90, 60, fill=gradient('lemonChiffon', rgb(245, 240, 170)))
Circle(200, 400, 60, fill=gradient('lemonChiffon', rgb(245, 240, 170)), opacity=20)

def drawReflection(buildingTopX):
    Polygon(buildingTopX - 30, 250, buildingTopX + 30, 250,
            buildingTopX + 100, 400, buildingTopX + 40, 400, opacity=60,
            fill=gradient(rgb(115, 105, 80), rgb(50, 40, 35), 'black', start='top'))

def drawBuilding(buildingTopX, buildingTopY):
    Rect(buildingTopX, buildingTopY, 60, 250 - buildingTopY,
         fill=gradient(rgb(50, 50, 55), rgb(90, 90, 125), start='left-top'),
         align='top')

def onMousePress(mouseX, mouseY):
    # When mouse is above the skyline, draw a building and a reflection from
    # where you click.
    if (mouseY < 250):
        drawBuilding(mouseX, mouseY)
        drawReflection(mouseX)

onMousePress(100, 75)
onMousePress(200, 150)
onMousePress(300, 50)
onMousePress(350, 120)


# -
app.background = 'black'
Rect(0, 0, 400, 250, fill=gradient(rgb(15, 25, 40), rgb(20, 40, 80), start='top'))

Circle(130, 90, 60, fill=gradient('lemonChiffon', rgb(245, 240, 170)))
Circle(200, 400, 60, fill=gradient('lemonChiffon', rgb(245, 240, 170)), opacity=20)

def drawReflection(buildingTopX):
    Polygon(buildingTopX - 30, 250, buildingTopX + 30, 250,
            buildingTopX + 100, 400, buildingTopX + 40, 400, opacity=60,
            fill=gradient(rgb(115, 105, 80), rgb(50, 40, 35), 'black', start='top'))

def drawBuilding(buildingTopX, buildingTopY):
    Rect(buildingTopX, buildingTopY, 60, 250 - buildingTopY,
         fill=gradient(rgb(50, 50, 55), rgb(90, 90, 125), start='left-top'),
         align='top')

def onMousePress(mouseX, mouseY):
    # When mouse is above the skyline, draw a building and a reflection from
    # where you click.
    if (mouseY < 250):
        drawBuilding(mouseX, mouseY)
        drawReflection(mouseX)

onMousePress(100, 75)
onMousePress(200, 150)
onMousePress(300, 50)
onMousePress(350, 120)


# -
app.background = 'black'
Rect(0, 0, 400, 250, fill=gradient(rgb(15, 25, 40), rgb(20, 40, 80), start='top'))

Circle(130, 90, 60, fill=gradient('lemonChiffon', rgb(245, 240, 170)))
Circle(200, 400, 60, fill=gradient('lemonChiffon', rgb(245, 240, 170)), opacity=20)

def drawReflection(buildingTopX):
    Polygon(buildingTopX - 30, 250, buildingTopX + 30, 250,
            buildingTopX + 100, 400, buildingTopX + 40, 400, opacity=60,
            fill=gradient(rgb(115, 105, 80), rgb(50, 40, 35), 'black', start='top'))

def drawBuilding(buildingTopX, buildingTopY):
    Rect(buildingTopX, buildingTopY, 60, 250 - buildingTopY,
         fill=gradient(rgb(50, 50, 55), rgb(90, 90, 125), start='left-top'),
         align='top')

def onMousePress(mouseX, mouseY):
    # When mouse is above the skyline, draw a building and a reflection from
    # where you click.
    if (mouseY < 250):
        drawBuilding(mouseX, mouseY)
        drawReflection(mouseX)

onMousePress(250, 70)
onMousePress(300, 150)

