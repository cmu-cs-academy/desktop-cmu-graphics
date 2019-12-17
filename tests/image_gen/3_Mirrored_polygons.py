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
onMousePress(150, 320)
onMousePress(300, 200)
onMousePress(30, 250)


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
onMousePress(150, 320)
onMousePress(300, 200)
onMousePress(30, 250)


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

onMousePress(140, 30)
onMousePress(40, 150)
onMousePress(120, 300)
onMousePress(190, 100)
onMousePress(60, 240)

