app.background = 'cornflowerBlue'

Line(200, 0, 200, 400, fill='silver', lineWidth=400, opacity=30, dashes=(1, 20))
Line(0, 200, 400, 200, fill='silver', lineWidth=400, opacity=30, dashes=(1, 20))

# divider
Line(200, 0, 200, 400, fill='white', dashes=True)

# left polygon
greenPolygon = Polygon(fill='lightGreen', border='black')

# right polygon
pinkPolygon = Polygon(fill='pink', border='black')

def onMousePress(mouseX, mouseY):
    # When the mouse is clicked on the left side, add a point to the green
    # polygon. Also, add a reflecting point to the pink polygon.
    if (mouseX < 200):
        greenPolygon.addPoint(mouseX, mouseY)
        pinkPolygon.addPoint(400 - mouseX, mouseY)

onMousePress(130, 150)
onMousePress(250, 320)
onMousePress(100, 200)
onMousePress(40, 40)
onMousePress(240, 160)
onMousePress(70, 330)
onMousePress(190, 250)
onMousePress(140, 110)
onMousePress(0, 0)


# -
app.background = 'cornflowerBlue'

Line(200, 0, 200, 400, fill='silver', lineWidth=400, opacity=30, dashes=(1, 20))
Line(0, 200, 400, 200, fill='silver', lineWidth=400, opacity=30, dashes=(1, 20))

# divider
Line(200, 0, 200, 400, fill='white', dashes=True)

# left polygon
greenPolygon = Polygon(fill='lightGreen', border='black')

# right polygon
pinkPolygon = Polygon(fill='pink', border='black')

def onMousePress(mouseX, mouseY):
    # When the mouse is clicked on the left side, add a point to the green
    # polygon. Also, add a reflecting point to the pink polygon.
    if (mouseX < 200):
        greenPolygon.addPoint(mouseX, mouseY)
        pinkPolygon.addPoint(400 - mouseX, mouseY)

onMousePress(100, 100)
onMousePress(150, 200)
onMousePress(50, 300)


# -
app.background = 'cornflowerBlue'

Line(200, 0, 200, 400, fill='silver', lineWidth=400, opacity=30, dashes=(1, 20))
Line(0, 200, 400, 200, fill='silver', lineWidth=400, opacity=30, dashes=(1, 20))

# divider
Line(200, 0, 200, 400, fill='white', dashes=True)

# left polygon
greenPolygon = Polygon(fill='lightGreen', border='black')

# right polygon
pinkPolygon = Polygon(fill='pink', border='black')

def onMousePress(mouseX, mouseY):
    # When the mouse is clicked on the left side, add a point to the green
    # polygon. Also, add a reflecting point to the pink polygon.
    if (mouseX < 200):
        greenPolygon.addPoint(mouseX, mouseY)
        pinkPolygon.addPoint(400 - mouseX, mouseY)

onMousePress(210, 120)
onMousePress(300, 340)
onMousePress(370, 50)

