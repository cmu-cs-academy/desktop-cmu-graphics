# Initially sets the fill color to white.
app.color = 'white'

colorSwatches = Group()

def drawColorSwatches():
    # Creates a list of colors to pick from.
    colors = [ 'black', 'white', 'navy', 'yellow', 'red' ]
    colorX = 375
    colorY = 40
    colorHeight = 400 / len(colors)

    # Loops through the colors list and adds to the colorSwatches group.
    for i in range(len(colors)):
        colorSwatches.add(
            Circle(colorX, colorY + i * 80, 25, fill=colors[i], border='black',
                   borderWidth=3)
            )

drawColorSwatches()

# Creates a group for the mosaic.
mosaic = Group(
    Rect(150, 0, 200, 200, fill='white', border='black', borderWidth=3),
    Rect(150, 200, 200, 70, fill='white', border='black', borderWidth=3),
    Rect(150, 270, 100, 130, fill='white', border='black', borderWidth=3),
    Rect(250, 270, 100, 130, fill='white', border='black', borderWidth=3),
    Rect(0, 0, 75, 100, fill='white', border='black', borderWidth=3),
    Rect(75, 0, 75, 100, fill='white', border='black', borderWidth=3),
    Rect(0, 100, 50, 50, fill='white', border='black', borderWidth=3),
    Rect(0, 150, 50, 150, fill='white', border='black', borderWidth=3),
    Rect(50, 100, 100, 200, fill='white', border='black', borderWidth=3),
    Rect(0, 300, 150, 40, fill='white', border='black', borderWidth=3),
    Rect(0, 340, 150, 60, fill='white', border='black', borderWidth=3)
    )

def onMousePress(mouseX, mouseY):
    # Check if the click is in a box in the mosaic and fill it.
    block = mosaic.hitTest(mouseX, mouseY)
    if (block != None):
        block.fill = app.color
    # Check if the click is in a color swatch and change app.color.
    color = colorSwatches.hitTest(mouseX, mouseY)
    if (color != None):
        app.color = color.fill

onMousePress(370, 370)
onMousePress(370, 200)
onMousePress(20, 200)


# -
# Initially sets the fill color to white.
app.color = 'white'

colorSwatches = Group()

def drawColorSwatches():
    # Creates a list of colors to pick from.
    colors = [ 'black', 'white', 'navy', 'yellow', 'red' ]
    colorX = 375
    colorY = 40
    colorHeight = 400 / len(colors)

    # Loops through the colors list and adds to the colorSwatches group.
    for i in range(len(colors)):
        colorSwatches.add(
            Circle(colorX, colorY + i * 80, 25, fill=colors[i], border='black',
                   borderWidth=3)
            )

drawColorSwatches()

# Creates a group for the mosaic.
mosaic = Group(
    Rect(150, 0, 200, 200, fill='white', border='black', borderWidth=3),
    Rect(150, 200, 200, 70, fill='white', border='black', borderWidth=3),
    Rect(150, 270, 100, 130, fill='white', border='black', borderWidth=3),
    Rect(250, 270, 100, 130, fill='white', border='black', borderWidth=3),
    Rect(0, 0, 75, 100, fill='white', border='black', borderWidth=3),
    Rect(75, 0, 75, 100, fill='white', border='black', borderWidth=3),
    Rect(0, 100, 50, 50, fill='white', border='black', borderWidth=3),
    Rect(0, 150, 50, 150, fill='white', border='black', borderWidth=3),
    Rect(50, 100, 100, 200, fill='white', border='black', borderWidth=3),
    Rect(0, 300, 150, 40, fill='white', border='black', borderWidth=3),
    Rect(0, 340, 150, 60, fill='white', border='black', borderWidth=3)
    )

def onMousePress(mouseX, mouseY):
    # Check if the click is in a box in the mosaic and fill it.
    block = mosaic.hitTest(mouseX, mouseY)
    if (block != None):
        block.fill = app.color
    # Check if the click is in a color swatch and change app.color.
    color = colorSwatches.hitTest(mouseX, mouseY)
    if (color != None):
        app.color = color.fill



# -
# Initially sets the fill color to white.
app.color = 'white'

colorSwatches = Group()

def drawColorSwatches():
    # Creates a list of colors to pick from.
    colors = [ 'black', 'white', 'navy', 'yellow', 'red' ]
    colorX = 375
    colorY = 40
    colorHeight = 400 / len(colors)

    # Loops through the colors list and adds to the colorSwatches group.
    for i in range(len(colors)):
        colorSwatches.add(
            Circle(colorX, colorY + i * 80, 25, fill=colors[i], border='black',
                   borderWidth=3)
            )

drawColorSwatches()

# Creates a group for the mosaic.
mosaic = Group(
    Rect(150, 0, 200, 200, fill='white', border='black', borderWidth=3),
    Rect(150, 200, 200, 70, fill='white', border='black', borderWidth=3),
    Rect(150, 270, 100, 130, fill='white', border='black', borderWidth=3),
    Rect(250, 270, 100, 130, fill='white', border='black', borderWidth=3),
    Rect(0, 0, 75, 100, fill='white', border='black', borderWidth=3),
    Rect(75, 0, 75, 100, fill='white', border='black', borderWidth=3),
    Rect(0, 100, 50, 50, fill='white', border='black', borderWidth=3),
    Rect(0, 150, 50, 150, fill='white', border='black', borderWidth=3),
    Rect(50, 100, 100, 200, fill='white', border='black', borderWidth=3),
    Rect(0, 300, 150, 40, fill='white', border='black', borderWidth=3),
    Rect(0, 340, 150, 60, fill='white', border='black', borderWidth=3)
    )

def onMousePress(mouseX, mouseY):
    # Check if the click is in a box in the mosaic and fill it.
    block = mosaic.hitTest(mouseX, mouseY)
    if (block != None):
        block.fill = app.color
    # Check if the click is in a color swatch and change app.color.
    color = colorSwatches.hitTest(mouseX, mouseY)
    if (color != None):
        app.color = color.fill

onMousePress(370, 200)
onMousePress(100, 200)
onMousePress(70, 320)

