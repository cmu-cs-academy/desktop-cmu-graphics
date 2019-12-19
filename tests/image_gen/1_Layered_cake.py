app.background = gradient('plum', 'thistle', start='left')

Label('Layers:', 380, 20, size=20, bold=True, align='right')
layersCountLabel = Label(5, 345, 50, size=30, bold=True)

# table
Polygon(0, 300, 30, 245, 400, 245, 400, 400, 0, 400, fill='saddleBrown')

layers = Group()
layers.colorNum = 0

def drawCake(layersCount):
    for i in range(layersCount):
        # Define the size and location of this layer.
        width = 300 - 30 * i
        height = 300 / layersCount
        top = 380 - height * (i + 1)
        centerY = top + height / 2

        # Set the color of the layer based on the layers.colorNum property.
        if (layers.colorNum == 0):
            layers.colorNum = 1
            layerColor = gradient('lightGreen', 'paleGreen', start='left')
            topColor = gradient('paleGreen', 'honeyDew', start='left')
        elif (layers.colorNum == 1):
            layers.colorNum = 2
            layerColor = gradient('lightBlue', 'paleTurquoise', start='left')
            topColor = gradient('powderBlue', 'aliceBlue', start='left')
        elif (layers.colorNum == 2):
            layers.colorNum = 0
            layerColor = gradient('lightPink', 'pink', start='left')
            topColor = gradient('pink', 'lavenderBlush', start='left')

        # Draw and add this layer to the layers group.
        layers.add(
            Oval(200, centerY + height / 2, width, height / 2, fill=layerColor,
                 border='black'),
            Rect(200, centerY, width, height, fill=layerColor, align='center'),
            Oval(200, centerY - height / 2, width, height / 2, fill=topColor,
                 border='black')
            )

    # Draw a candle on top of the cake and add it to the layers group.
    layers.add(
        Line(200, top, 200, top - 25, fill='red', lineWidth=4),
        Line(200, top - 25, 200, top - 27),
        Oval(200, top - 27, 5, 10, fill=gradient('yellow', 'red', start='bottom'),
             align='bottom')
        )

def onKeyPress(key):
    # Change the number of layers when the 'up' or 'down' keys are pressed.
    # A cake has at most 10 layers, otherwise the width gets too small.
    if (key == 'up'):
        if (layersCountLabel.value < 10):
            layersCountLabel.value += 1
    elif (key == 'down'):
        if (layersCountLabel.value > 1):
            layersCountLabel.value -= 1

    # Always remove the old layers and draw new ones.
    layers.clear()
    drawCake(layersCountLabel.value)

# Start with the 5 layers already drawn.
drawCake(layersCountLabel.value)



# -
app.background = gradient('plum', 'thistle', start='left')

Label('Layers:', 380, 20, size=20, bold=True, align='right')
layersCountLabel = Label(5, 345, 50, size=30, bold=True)

# table
Polygon(0, 300, 30, 245, 400, 245, 400, 400, 0, 400, fill='saddleBrown')

layers = Group()
layers.colorNum = 0

def drawCake(layersCount):
    for i in range(layersCount):
        # Define the size and location of this layer.
        width = 300 - 30 * i
        height = 300 / layersCount
        top = 380 - height * (i + 1)
        centerY = top + height / 2

        # Set the color of the layer based on the layers.colorNum property.
        if (layers.colorNum == 0):
            layers.colorNum = 1
            layerColor = gradient('lightGreen', 'paleGreen', start='left')
            topColor = gradient('paleGreen', 'honeyDew', start='left')
        elif (layers.colorNum == 1):
            layers.colorNum = 2
            layerColor = gradient('lightBlue', 'paleTurquoise', start='left')
            topColor = gradient('powderBlue', 'aliceBlue', start='left')
        elif (layers.colorNum == 2):
            layers.colorNum = 0
            layerColor = gradient('lightPink', 'pink', start='left')
            topColor = gradient('pink', 'lavenderBlush', start='left')

        # Draw and add this layer to the layers group.
        layers.add(
            Oval(200, centerY + height / 2, width, height / 2, fill=layerColor,
                 border='black'),
            Rect(200, centerY, width, height, fill=layerColor, align='center'),
            Oval(200, centerY - height / 2, width, height / 2, fill=topColor,
                 border='black')
            )

    # Draw a candle on top of the cake and add it to the layers group.
    layers.add(
        Line(200, top, 200, top - 25, fill='red', lineWidth=4),
        Line(200, top - 25, 200, top - 27),
        Oval(200, top - 27, 5, 10, fill=gradient('yellow', 'red', start='bottom'),
             align='bottom')
        )

def onKeyPress(key):
    # Change the number of layers when the 'up' or 'down' keys are pressed.
    # A cake has at most 10 layers, otherwise the width gets too small.
    if (key == 'up'):
        if (layersCountLabel.value < 10):
            layersCountLabel.value += 1
    elif (key == 'down'):
        if (layersCountLabel.value > 1):
            layersCountLabel.value -= 1

    # Always remove the old layers and draw new ones.
    layers.clear()
    drawCake(layersCountLabel.value)

# Start with the 5 layers already drawn.
drawCake(layersCountLabel.value)

onKeyPresses('down', 5)


# -
app.background = gradient('plum', 'thistle', start='left')

Label('Layers:', 380, 20, size=20, bold=True, align='right')
layersCountLabel = Label(5, 345, 50, size=30, bold=True)

# table
Polygon(0, 300, 30, 245, 400, 245, 400, 400, 0, 400, fill='saddleBrown')

layers = Group()
layers.colorNum = 0

def drawCake(layersCount):
    for i in range(layersCount):
        # Define the size and location of this layer.
        width = 300 - 30 * i
        height = 300 / layersCount
        top = 380 - height * (i + 1)
        centerY = top + height / 2

        # Set the color of the layer based on the layers.colorNum property.
        if (layers.colorNum == 0):
            layers.colorNum = 1
            layerColor = gradient('lightGreen', 'paleGreen', start='left')
            topColor = gradient('paleGreen', 'honeyDew', start='left')
        elif (layers.colorNum == 1):
            layers.colorNum = 2
            layerColor = gradient('lightBlue', 'paleTurquoise', start='left')
            topColor = gradient('powderBlue', 'aliceBlue', start='left')
        elif (layers.colorNum == 2):
            layers.colorNum = 0
            layerColor = gradient('lightPink', 'pink', start='left')
            topColor = gradient('pink', 'lavenderBlush', start='left')

        # Draw and add this layer to the layers group.
        layers.add(
            Oval(200, centerY + height / 2, width, height / 2, fill=layerColor,
                 border='black'),
            Rect(200, centerY, width, height, fill=layerColor, align='center'),
            Oval(200, centerY - height / 2, width, height / 2, fill=topColor,
                 border='black')
            )

    # Draw a candle on top of the cake and add it to the layers group.
    layers.add(
        Line(200, top, 200, top - 25, fill='red', lineWidth=4),
        Line(200, top - 25, 200, top - 27),
        Oval(200, top - 27, 5, 10, fill=gradient('yellow', 'red', start='bottom'),
             align='bottom')
        )

def onKeyPress(key):
    # Change the number of layers when the 'up' or 'down' keys are pressed.
    # A cake has at most 10 layers, otherwise the width gets too small.
    if (key == 'up'):
        if (layersCountLabel.value < 10):
            layersCountLabel.value += 1
    elif (key == 'down'):
        if (layersCountLabel.value > 1):
            layersCountLabel.value -= 1

    # Always remove the old layers and draw new ones.
    layers.clear()
    drawCake(layersCountLabel.value)

# Start with the 5 layers already drawn.
drawCake(layersCountLabel.value)


