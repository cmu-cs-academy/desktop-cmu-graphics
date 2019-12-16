dotGrid = Group()

# Create an evenly spaced 9x9 grid of dots.
for cx in range(40, 400, 40):
    for cy in range(40, 400, 40):
        dotGrid.add(
            Circle(cx, cy, 5)
            )
# magnifying glass
magnifyingGlass = Group(
    Circle(200, 200, 50, fill=gradient('white', 'steelBlue', start='left'),
           opacity=25),
    Circle(200, 200, 50, fill=None, border='silver'),
    Line(200, 250, 200, 300, lineWidth=10)
    )
magnifyingGlass.glassX = 200
magnifyingGlass.glassY = 200

def onMouseMove(mouseX, mouseY):
    magnifyingGlass.centerX = mouseX
    magnifyingGlass.centerY = mouseY
    magnifyingGlass.glassX = magnifyingGlass.centerX
    magnifyingGlass.glassY = magnifyingGlass.centerY - 25

    # Resize any dots who's centers are inside the glass.
    for dot in dotGrid:
        if (distance(magnifyingGlass.glassX, magnifyingGlass.glassY,
                     dot.centerX, dot.centerY) < 50):
            dot.radius = 15
        else:
            dot.radius = 5

onMouseMove(120, 310)


# -
dotGrid = Group()

# Create an evenly spaced 9x9 grid of dots.
for cx in range(40, 400, 40):
    for cy in range(40, 400, 40):
        dotGrid.add(
            Circle(cx, cy, 5)
            )
# magnifying glass
magnifyingGlass = Group(
    Circle(200, 200, 50, fill=gradient('white', 'steelBlue', start='left'),
           opacity=25),
    Circle(200, 200, 50, fill=None, border='silver'),
    Line(200, 250, 200, 300, lineWidth=10)
    )
magnifyingGlass.glassX = 200
magnifyingGlass.glassY = 200

def onMouseMove(mouseX, mouseY):
    magnifyingGlass.centerX = mouseX
    magnifyingGlass.centerY = mouseY
    magnifyingGlass.glassX = magnifyingGlass.centerX
    magnifyingGlass.glassY = magnifyingGlass.centerY - 25

    # Resize any dots who's centers are inside the glass.
    for dot in dotGrid:
        if (distance(magnifyingGlass.glassX, magnifyingGlass.glassY,
                     dot.centerX, dot.centerY) < 50):
            dot.radius = 15
        else:
            dot.radius = 5

onMouseMove(120, 310)


# -
dotGrid = Group()

# Create an evenly spaced 9x9 grid of dots.
for cx in range(40, 400, 40):
    for cy in range(40, 400, 40):
        dotGrid.add(
            Circle(cx, cy, 5)
            )
# magnifying glass
magnifyingGlass = Group(
    Circle(200, 200, 50, fill=gradient('white', 'steelBlue', start='left'),
           opacity=25),
    Circle(200, 200, 50, fill=None, border='silver'),
    Line(200, 250, 200, 300, lineWidth=10)
    )
magnifyingGlass.glassX = 200
magnifyingGlass.glassY = 200

def onMouseMove(mouseX, mouseY):
    magnifyingGlass.centerX = mouseX
    magnifyingGlass.centerY = mouseY
    magnifyingGlass.glassX = magnifyingGlass.centerX
    magnifyingGlass.glassY = magnifyingGlass.centerY - 25

    # Resize any dots who's centers are inside the glass.
    for dot in dotGrid:
        if (distance(magnifyingGlass.glassX, magnifyingGlass.glassY,
                     dot.centerX, dot.centerY) < 50):
            dot.radius = 15
        else:
            dot.radius = 5


