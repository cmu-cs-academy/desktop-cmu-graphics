# background and environment
sky = Rect(0, 0, 400, 250, fill=gradient('lightBlue', 'burlyWood', start='top'))
ground = Rect(0, 250, 400, 150, fill='lemonChiffon')
path = Polygon(175, 300, 225, 300, 250, 400, 150, 400, fill='navajoWhite')

windows = Group()
door = Group()

def drawWindow(x1, y1, x2, y2):
    # Use a line to create the brown window panes and add it to the
    # windows group.
    windows.add(
        Line(x1, y1, x2, y2, fill='saddleBrown', lineWidth=14, dashes=(15, 2))
        )
def drawAllWindows():
    # bottom windows
    Rect(115, 230, 35, 55, fill='peru', border='brown')
    drawWindow(125, 233, 125, 283)
    drawWindow(140, 233, 140, 283)

    Rect(250, 230, 35, 55, fill='peru', border='brown')
    drawWindow(260, 233, 260, 283)
    drawWindow(275, 233, 275, 283)

    # top windows
    Rect(115, 157, 35, 55, fill='peru', border='brown')
    drawWindow(125, 160, 125, 210)
    drawWindow(140, 160, 140, 210)

    Rect(183, 157, 35, 55, fill='peru', border='brown')
    drawWindow(193, 160, 193, 210)
    drawWindow(208, 160, 208, 210)

    Rect(250, 157, 35, 55, fill='peru', border='brown')
    drawWindow(260, 160, 260, 210)
    drawWindow(275, 160, 275, 210)

    windows.toFront()

def drawDoor():
    # Add the rectangular door to the door group.
    door.add(
        Rect(175, 250, 50, 50, fill='saddleBrown', border='sienna')
        )
    door.toFront()

    Line(200, 250, 200, 300, fill='sienna')
    Line(185, 265, 185, 285, fill='peru', lineWidth=20, dashes=(1, 2))
    Line(215, 265, 215, 285, fill='peru', lineWidth=20, dashes=(1, 2))

def drawPorch():
    Polygon(100, 220, 300, 220, 325, 245, 75, 245,
            fill=gradient('saddleBrown', 'sienna', start='top'),
            border='saddleBrown')
    Rect(80, 300, 240, 10, fill='sienna', border='brown')
    Line(85, 245, 85, 300, fill='brown', lineWidth=8, dashes=(15, 1))
    Line(315, 245, 315, 300, fill='brown', lineWidth=8, dashes=(15, 1))
    Line(140, 245, 140, 300, fill='brown', lineWidth=8, dashes=(15, 1))
    Line(260, 245, 260, 300, fill='brown', lineWidth=8, dashes=(15, 1))

def drawSaloon():
    # bottom floor
    Rect(100, 150, 200, 150, fill='sienna')
    Line(200, 150, 200, 300, fill='burlyWood', lineWidth=200, dashes=(10, 1))

    # Add windows and doors to each group.
    drawAllWindows()
    drawDoor()

    # top floor
    Rect(125, 75, 150, 75, fill='sienna')
    Line(200, 75, 200, 150, fill='burlyWood', lineWidth=150, dashes=(12, 1))
    Rect(90, 140, 220, 10, fill='sienna', border='brown')
    Rect(120, 65, 160, 10, fill='sienna', border='brown')

    # building name
    Rect(150, 80, 100, 50, fill=gradient('peru', 'burlyWood', start='bottom'),
         border='saddleBrown', borderWidth=4)
    Label('Saloon', 200, 105, fill='saddleBrown', size=30)

    drawPorch()

drawSaloon()

def onMousePress(mouseX, mouseY):
    sky.fill = gradient('navy', 'rosyBrown', start='top')
    ground.fill = 'paleGoldenrod'
    path.fill = 'burlyWood'

    # Change the fill of all the windows and doors to their nighttime colors.
    windows.fill = 'yellow'
    door.fill = 'yellow'
def onMouseRelease(mouseX, mouseY):
    sky.fill = gradient('lightBlue', 'burlyWood', start='top')
    ground.fill = 'lemonChiffon'
    path.fill = 'navajoWhite'

    # Change the fill of all the windows and doors to their daytime colors.
    windows.fill = 'saddleBrown'
    door.fill = 'saddleBrown'



# -
# background and environment
sky = Rect(0, 0, 400, 250, fill=gradient('lightBlue', 'burlyWood', start='top'))
ground = Rect(0, 250, 400, 150, fill='lemonChiffon')
path = Polygon(175, 300, 225, 300, 250, 400, 150, 400, fill='navajoWhite')

windows = Group()
door = Group()

def drawWindow(x1, y1, x2, y2):
    # Use a line to create the brown window panes and add it to the
    # windows group.
    windows.add(
        Line(x1, y1, x2, y2, fill='saddleBrown', lineWidth=14, dashes=(15, 2))
        )
def drawAllWindows():
    # bottom windows
    Rect(115, 230, 35, 55, fill='peru', border='brown')
    drawWindow(125, 233, 125, 283)
    drawWindow(140, 233, 140, 283)

    Rect(250, 230, 35, 55, fill='peru', border='brown')
    drawWindow(260, 233, 260, 283)
    drawWindow(275, 233, 275, 283)

    # top windows
    Rect(115, 157, 35, 55, fill='peru', border='brown')
    drawWindow(125, 160, 125, 210)
    drawWindow(140, 160, 140, 210)

    Rect(183, 157, 35, 55, fill='peru', border='brown')
    drawWindow(193, 160, 193, 210)
    drawWindow(208, 160, 208, 210)

    Rect(250, 157, 35, 55, fill='peru', border='brown')
    drawWindow(260, 160, 260, 210)
    drawWindow(275, 160, 275, 210)

    windows.toFront()

def drawDoor():
    # Add the rectangular door to the door group.
    door.add(
        Rect(175, 250, 50, 50, fill='saddleBrown', border='sienna')
        )
    door.toFront()

    Line(200, 250, 200, 300, fill='sienna')
    Line(185, 265, 185, 285, fill='peru', lineWidth=20, dashes=(1, 2))
    Line(215, 265, 215, 285, fill='peru', lineWidth=20, dashes=(1, 2))

def drawPorch():
    Polygon(100, 220, 300, 220, 325, 245, 75, 245,
            fill=gradient('saddleBrown', 'sienna', start='top'),
            border='saddleBrown')
    Rect(80, 300, 240, 10, fill='sienna', border='brown')
    Line(85, 245, 85, 300, fill='brown', lineWidth=8, dashes=(15, 1))
    Line(315, 245, 315, 300, fill='brown', lineWidth=8, dashes=(15, 1))
    Line(140, 245, 140, 300, fill='brown', lineWidth=8, dashes=(15, 1))
    Line(260, 245, 260, 300, fill='brown', lineWidth=8, dashes=(15, 1))

def drawSaloon():
    # bottom floor
    Rect(100, 150, 200, 150, fill='sienna')
    Line(200, 150, 200, 300, fill='burlyWood', lineWidth=200, dashes=(10, 1))

    # Add windows and doors to each group.
    drawAllWindows()
    drawDoor()

    # top floor
    Rect(125, 75, 150, 75, fill='sienna')
    Line(200, 75, 200, 150, fill='burlyWood', lineWidth=150, dashes=(12, 1))
    Rect(90, 140, 220, 10, fill='sienna', border='brown')
    Rect(120, 65, 160, 10, fill='sienna', border='brown')

    # building name
    Rect(150, 80, 100, 50, fill=gradient('peru', 'burlyWood', start='bottom'),
         border='saddleBrown', borderWidth=4)
    Label('Saloon', 200, 105, fill='saddleBrown', size=30)

    drawPorch()

drawSaloon()

def onMousePress(mouseX, mouseY):
    sky.fill = gradient('navy', 'rosyBrown', start='top')
    ground.fill = 'paleGoldenrod'
    path.fill = 'burlyWood'

    # Change the fill of all the windows and doors to their nighttime colors.
    windows.fill = 'yellow'
    door.fill = 'yellow'
def onMouseRelease(mouseX, mouseY):
    sky.fill = gradient('lightBlue', 'burlyWood', start='top')
    ground.fill = 'lemonChiffon'
    path.fill = 'navajoWhite'

    # Change the fill of all the windows and doors to their daytime colors.
    windows.fill = 'saddleBrown'
    door.fill = 'saddleBrown'

onMousePress(200, 200)


# -
# background and environment
sky = Rect(0, 0, 400, 250, fill=gradient('lightBlue', 'burlyWood', start='top'))
ground = Rect(0, 250, 400, 150, fill='lemonChiffon')
path = Polygon(175, 300, 225, 300, 250, 400, 150, 400, fill='navajoWhite')

windows = Group()
door = Group()

def drawWindow(x1, y1, x2, y2):
    # Use a line to create the brown window panes and add it to the
    # windows group.
    windows.add(
        Line(x1, y1, x2, y2, fill='saddleBrown', lineWidth=14, dashes=(15, 2))
        )
def drawAllWindows():
    # bottom windows
    Rect(115, 230, 35, 55, fill='peru', border='brown')
    drawWindow(125, 233, 125, 283)
    drawWindow(140, 233, 140, 283)

    Rect(250, 230, 35, 55, fill='peru', border='brown')
    drawWindow(260, 233, 260, 283)
    drawWindow(275, 233, 275, 283)

    # top windows
    Rect(115, 157, 35, 55, fill='peru', border='brown')
    drawWindow(125, 160, 125, 210)
    drawWindow(140, 160, 140, 210)

    Rect(183, 157, 35, 55, fill='peru', border='brown')
    drawWindow(193, 160, 193, 210)
    drawWindow(208, 160, 208, 210)

    Rect(250, 157, 35, 55, fill='peru', border='brown')
    drawWindow(260, 160, 260, 210)
    drawWindow(275, 160, 275, 210)

    windows.toFront()

def drawDoor():
    # Add the rectangular door to the door group.
    door.add(
        Rect(175, 250, 50, 50, fill='saddleBrown', border='sienna')
        )
    door.toFront()

    Line(200, 250, 200, 300, fill='sienna')
    Line(185, 265, 185, 285, fill='peru', lineWidth=20, dashes=(1, 2))
    Line(215, 265, 215, 285, fill='peru', lineWidth=20, dashes=(1, 2))

def drawPorch():
    Polygon(100, 220, 300, 220, 325, 245, 75, 245,
            fill=gradient('saddleBrown', 'sienna', start='top'),
            border='saddleBrown')
    Rect(80, 300, 240, 10, fill='sienna', border='brown')
    Line(85, 245, 85, 300, fill='brown', lineWidth=8, dashes=(15, 1))
    Line(315, 245, 315, 300, fill='brown', lineWidth=8, dashes=(15, 1))
    Line(140, 245, 140, 300, fill='brown', lineWidth=8, dashes=(15, 1))
    Line(260, 245, 260, 300, fill='brown', lineWidth=8, dashes=(15, 1))

def drawSaloon():
    # bottom floor
    Rect(100, 150, 200, 150, fill='sienna')
    Line(200, 150, 200, 300, fill='burlyWood', lineWidth=200, dashes=(10, 1))

    # Add windows and doors to each group.
    drawAllWindows()
    drawDoor()

    # top floor
    Rect(125, 75, 150, 75, fill='sienna')
    Line(200, 75, 200, 150, fill='burlyWood', lineWidth=150, dashes=(12, 1))
    Rect(90, 140, 220, 10, fill='sienna', border='brown')
    Rect(120, 65, 160, 10, fill='sienna', border='brown')

    # building name
    Rect(150, 80, 100, 50, fill=gradient('peru', 'burlyWood', start='bottom'),
         border='saddleBrown', borderWidth=4)
    Label('Saloon', 200, 105, fill='saddleBrown', size=30)

    drawPorch()

drawSaloon()

def onMousePress(mouseX, mouseY):
    sky.fill = gradient('navy', 'rosyBrown', start='top')
    ground.fill = 'paleGoldenrod'
    path.fill = 'burlyWood'

    # Change the fill of all the windows and doors to their nighttime colors.
    windows.fill = 'yellow'
    door.fill = 'yellow'
def onMouseRelease(mouseX, mouseY):
    sky.fill = gradient('lightBlue', 'burlyWood', start='top')
    ground.fill = 'lemonChiffon'
    path.fill = 'navajoWhite'

    # Change the fill of all the windows and doors to their daytime colors.
    windows.fill = 'saddleBrown'
    door.fill = 'saddleBrown'

onMousePress(200, 200)

