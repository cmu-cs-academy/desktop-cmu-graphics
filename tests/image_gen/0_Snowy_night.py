app.background = gradient('navy', 'midnightBlue', start='top')

# the two snow piles
snowPile1 = Circle(450, 500, 250, fill='ghostWhite')
snowPile2 = Circle(-100, 1000, 700, fill='snow')

lamp = Group(
    Line(275, 130, 275, 350, lineWidth=10),
    Oval(275, 85, 40, 50),
    Polygon(255, 130, 295, 130, 305, 125, 245, 125),
    Polygon(260, 125, 290, 125, 295, 90, 255, 90,
            fill=gradient('white', 'yellow', 'gold')),
    Polygon(240, 90, 310, 90, 305, 85, 245, 85)
    )

lampCover = Group(
    Rect(265, 350, 20, 300, fill='ghostWhite'),
    Polygon(270, 350, 280, 350, 270, 355),
    Oval(275, 352, 15, 4, fill='darkGrey', lineWidth=4, rotateAngle=-30)
    )

snowFlakes = Group()

def onMousePress(mouseX, mouseY):
    snowFlakes.add(
        Star(mouseX, mouseY, 8, 8, fill='white')
        )

def onStep():
    # Move each snowflake down by 5 pixels.
    for flake in snowFlakes.children:
        flake.centerY += 5

        # If it reaches either snow pile, increase the pile radius by 5 pixels,
        # and hide the snowflake. If it hit the right snow pile, move the
        # lampCover up by 2 pixels.
        if (snowPile1.hitsShape(flake) == True):
            snowPile1.radius += 5
            flake.visible = False
            lampCover.centerY -= 2
        elif (snowPile2.hitsShape(flake) == True):
            snowPile2.radius += 5
            flake.visible = False

onMousePress(100, 100)
onSteps(10)
app.paused = True


# -
app.background = gradient('navy', 'midnightBlue', start='top')

# the two snow piles
snowPile1 = Circle(450, 500, 250, fill='ghostWhite')
snowPile2 = Circle(-100, 1000, 700, fill='snow')

lamp = Group(
    Line(275, 130, 275, 350, lineWidth=10),
    Oval(275, 85, 40, 50),
    Polygon(255, 130, 295, 130, 305, 125, 245, 125),
    Polygon(260, 125, 290, 125, 295, 90, 255, 90,
            fill=gradient('white', 'yellow', 'gold')),
    Polygon(240, 90, 310, 90, 305, 85, 245, 85)
    )

lampCover = Group(
    Rect(265, 350, 20, 300, fill='ghostWhite'),
    Polygon(270, 350, 280, 350, 270, 355),
    Oval(275, 352, 15, 4, fill='darkGrey', lineWidth=4, rotateAngle=-30)
    )

snowFlakes = Group()

def onMousePress(mouseX, mouseY):
    snowFlakes.add(
        Star(mouseX, mouseY, 8, 8, fill='white')
        )

def onStep():
    # Move each snowflake down by 5 pixels.
    for flake in snowFlakes.children:
        flake.centerY += 5

        # If it reaches either snow pile, increase the pile radius by 5 pixels,
        # and hide the snowflake. If it hit the right snow pile, move the
        # lampCover up by 2 pixels.
        if (snowPile1.hitsShape(flake) == True):
            snowPile1.radius += 5
            flake.visible = False
            lampCover.centerY -= 2
        elif (snowPile2.hitsShape(flake) == True):
            snowPile2.radius += 5
            flake.visible = False

onMousePress(100, 100)
app.paused = True


# -
app.background = gradient('navy', 'midnightBlue', start='top')

# the two snow piles
snowPile1 = Circle(450, 500, 250, fill='ghostWhite')
snowPile2 = Circle(-100, 1000, 700, fill='snow')

lamp = Group(
    Line(275, 130, 275, 350, lineWidth=10),
    Oval(275, 85, 40, 50),
    Polygon(255, 130, 295, 130, 305, 125, 245, 125),
    Polygon(260, 125, 290, 125, 295, 90, 255, 90,
            fill=gradient('white', 'yellow', 'gold')),
    Polygon(240, 90, 310, 90, 305, 85, 245, 85)
    )

lampCover = Group(
    Rect(265, 350, 20, 300, fill='ghostWhite'),
    Polygon(270, 350, 280, 350, 270, 355),
    Oval(275, 352, 15, 4, fill='darkGrey', lineWidth=4, rotateAngle=-30)
    )

snowFlakes = Group()

def onMousePress(mouseX, mouseY):
    snowFlakes.add(
        Star(mouseX, mouseY, 8, 8, fill='white')
        )

def onStep():
    # Move each snowflake down by 5 pixels.
    for flake in snowFlakes.children:
        flake.centerY += 5

        # If it reaches either snow pile, increase the pile radius by 5 pixels,
        # and hide the snowflake. If it hit the right snow pile, move the
        # lampCover up by 2 pixels.
        if (snowPile1.hitsShape(flake) == True):
            snowPile1.radius += 5
            flake.visible = False
            lampCover.centerY -= 2
        elif (snowPile2.hitsShape(flake) == True):
            snowPile2.radius += 5
            flake.visible = False

onMousePress(100, 200)
onMousePress(300, 200)
onSteps(20)
app.paused = True

