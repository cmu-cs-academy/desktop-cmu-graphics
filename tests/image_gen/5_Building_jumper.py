app.background = gradient('black', 'midnightBlue', start='top')

app.buildingHeights = [ ]

def drawBuildings():
    # Draws 16 buildings, each with three windows.
    for x in range(0, 400, 25):
        height = randrange(100, 400)
        Rect(x, height, 25, 400 - height,
             fill=gradient('dimGray', 'slateGray', start='top'))

        # Draws three windows on each building.
        for i in range(3):
            Rect(x + randrange(5, 10), randrange(height, 400), 10, 5, fill='gold')

        # Store the top of the rectangle in buildingHeights.
        app.buildingHeights.append(height)
drawBuildings()

spiderman = Group(
    Circle(200, 200, 8, fill='red'),
    Rect(188, 208, 24, 6, fill='red'),
    Rect(192, 214, 16, 16, fill='red'),
    Arc(197, 199, 5, 5, 110, 180, fill='white', border='black', borderWidth=0.5),
    Arc(203, 199, 5, 5, 70, 180, fill='white', border='black', borderWidth=0.5),
    Rect(192, 220, 16, 6, fill='blue'),
    Rect(192, 214, 4, 5, fill='blue'),
    Rect(204, 214, 4, 5, fill='blue'),
    Circle(200, 213, 1),
    Line(200, 232, 200, 223, opacity=40)
    )
spiderman.centerX = -50

def onMouseMove(mouseX, mouseY):
    # Move spiderman to follow mouseX and set the bottom of the group equal
    # to the height of the building it is currently on.
    spiderman.centerX = mouseX
    index = mouseX // 25
    spiderman.bottom = app.buildingHeights[index]



# -
app.background = gradient('black', 'midnightBlue', start='top')

app.buildingHeights = [ ]

def drawBuildings():
    # Draws 16 buildings, each with three windows.
    for x in range(0, 400, 25):
        height = randrange(100, 400)
        Rect(x, height, 25, 400 - height,
             fill=gradient('dimGray', 'slateGray', start='top'))

        # Draws three windows on each building.
        for i in range(3):
            Rect(x + randrange(5, 10), randrange(height, 400), 10, 5, fill='gold')

        # Store the top of the rectangle in buildingHeights.
        app.buildingHeights.append(height)
drawBuildings()

spiderman = Group(
    Circle(200, 200, 8, fill='red'),
    Rect(188, 208, 24, 6, fill='red'),
    Rect(192, 214, 16, 16, fill='red'),
    Arc(197, 199, 5, 5, 110, 180, fill='white', border='black', borderWidth=0.5),
    Arc(203, 199, 5, 5, 70, 180, fill='white', border='black', borderWidth=0.5),
    Rect(192, 220, 16, 6, fill='blue'),
    Rect(192, 214, 4, 5, fill='blue'),
    Rect(204, 214, 4, 5, fill='blue'),
    Circle(200, 213, 1),
    Line(200, 232, 200, 223, opacity=40)
    )
spiderman.centerX = -50

def onMouseMove(mouseX, mouseY):
    # Move spiderman to follow mouseX and set the bottom of the group equal
    # to the height of the building it is currently on.
    spiderman.centerX = mouseX
    index = mouseX // 25
    spiderman.bottom = app.buildingHeights[index]

onMouseMove(110, 300)
onMouseMove(310, 100)


# -
app.background = gradient('black', 'midnightBlue', start='top')

app.buildingHeights = [ ]

def drawBuildings():
    # Draws 16 buildings, each with three windows.
    for x in range(0, 400, 25):
        height = randrange(100, 400)
        Rect(x, height, 25, 400 - height,
             fill=gradient('dimGray', 'slateGray', start='top'))

        # Draws three windows on each building.
        for i in range(3):
            Rect(x + randrange(5, 10), randrange(height, 400), 10, 5, fill='gold')

        # Store the top of the rectangle in buildingHeights.
        app.buildingHeights.append(height)
drawBuildings()

spiderman = Group(
    Circle(200, 200, 8, fill='red'),
    Rect(188, 208, 24, 6, fill='red'),
    Rect(192, 214, 16, 16, fill='red'),
    Arc(197, 199, 5, 5, 110, 180, fill='white', border='black', borderWidth=0.5),
    Arc(203, 199, 5, 5, 70, 180, fill='white', border='black', borderWidth=0.5),
    Rect(192, 220, 16, 6, fill='blue'),
    Rect(192, 214, 4, 5, fill='blue'),
    Rect(204, 214, 4, 5, fill='blue'),
    Circle(200, 213, 1),
    Line(200, 232, 200, 223, opacity=40)
    )
spiderman.centerX = -50

def onMouseMove(mouseX, mouseY):
    # Move spiderman to follow mouseX and set the bottom of the group equal
    # to the height of the building it is currently on.
    spiderman.centerX = mouseX
    index = mouseX // 25
    spiderman.bottom = app.buildingHeights[index]


