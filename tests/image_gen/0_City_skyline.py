app.background = gradient(rgb(210, 105, 100), rgb(240, 210, 185), start='top')

mainBuilding = Polygon(110, 400, 290, 400, 290, 340, 280, 340, 280, 300, 250, 300,
                       250, 120, 230, 120, 230, 100, 210, 100, 210, 80, 205, 80,
                       200, 5, 195, 80, 190, 80, 190, 100, 170, 100, 170, 120,
                       150, 120, 150, 300, 120, 300, 120, 340, 110, 340,
                       fill=gradient(rgb(40, 25, 40), rgb(75, 55, 75),
                                     start='left'))

Star(350, 200, 50, 500, fill=gradient('papayaWhip', 'moccasin'), roundness=80)

def drawBuilding(mouseX, mouseY):
    Rect(mouseX, mouseY + 10, 60, 400 - mouseY, align='top',
         fill=gradient(rgb(150, 95, 90), rgb(195, 110, 115), start='left'))
    Polygon(mouseX, mouseY - 50, mouseX - 30, mouseY + 10,
            mouseX + 30, mouseY + 10,
            fill=gradient(rgb(150, 95, 90), rgb(195, 110, 115), start='left'))

def onMousePress(mouseX, mouseY):
  # Draw a building behind the main building.
    drawBuilding(mouseX, mouseY)
    mainBuilding.toFront()

onMousePress(20, 50)
onMousePress(50, 230)
onMousePress(330, 100)
onMousePress(380, 150)
onMousePress(40, 100)


# -
app.background = gradient(rgb(210, 105, 100), rgb(240, 210, 185), start='top')

mainBuilding = Polygon(110, 400, 290, 400, 290, 340, 280, 340, 280, 300, 250, 300,
                       250, 120, 230, 120, 230, 100, 210, 100, 210, 80, 205, 80,
                       200, 5, 195, 80, 190, 80, 190, 100, 170, 100, 170, 120,
                       150, 120, 150, 300, 120, 300, 120, 340, 110, 340,
                       fill=gradient(rgb(40, 25, 40), rgb(75, 55, 75),
                                     start='left'))

Star(350, 200, 50, 500, fill=gradient('papayaWhip', 'moccasin'), roundness=80)

def drawBuilding(mouseX, mouseY):
    Rect(mouseX, mouseY + 10, 60, 400 - mouseY, align='top',
         fill=gradient(rgb(150, 95, 90), rgb(195, 110, 115), start='left'))
    Polygon(mouseX, mouseY - 50, mouseX - 30, mouseY + 10,
            mouseX + 30, mouseY + 10,
            fill=gradient(rgb(150, 95, 90), rgb(195, 110, 115), start='left'))

def onMousePress(mouseX, mouseY):
  # Draw a building behind the main building.
    drawBuilding(mouseX, mouseY)
    mainBuilding.toFront()

onMousePress(150, 50)
onMousePress(230, 140)
onMousePress(40, 40)
onMousePress(300, 100)
onMousePress(360, 280)
onMousePress(120, 300)


# -
app.background = gradient(rgb(210, 105, 100), rgb(240, 210, 185), start='top')

mainBuilding = Polygon(110, 400, 290, 400, 290, 340, 280, 340, 280, 300, 250, 300,
                       250, 120, 230, 120, 230, 100, 210, 100, 210, 80, 205, 80,
                       200, 5, 195, 80, 190, 80, 190, 100, 170, 100, 170, 120,
                       150, 120, 150, 300, 120, 300, 120, 340, 110, 340,
                       fill=gradient(rgb(40, 25, 40), rgb(75, 55, 75),
                                     start='left'))

Star(350, 200, 50, 500, fill=gradient('papayaWhip', 'moccasin'), roundness=80)

def drawBuilding(mouseX, mouseY):
    Rect(mouseX, mouseY + 10, 60, 400 - mouseY, align='top',
         fill=gradient(rgb(150, 95, 90), rgb(195, 110, 115), start='left'))
    Polygon(mouseX, mouseY - 50, mouseX - 30, mouseY + 10,
            mouseX + 30, mouseY + 10,
            fill=gradient(rgb(150, 95, 90), rgb(195, 110, 115), start='left'))

def onMousePress(mouseX, mouseY):
  # Draw a building behind the main building.
    drawBuilding(mouseX, mouseY)
    mainBuilding.toFront()

onMousePress(350, 200)

