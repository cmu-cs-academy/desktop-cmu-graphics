app.background = 'darkRed'

# brick background
Line(200, 0, 200, 400, fill='indianRed', lineWidth=400, dashes=True)
Line(0, 200, 400, 200, fill='fireBrick', lineWidth=400, dashes=True,
     opacity=50)

# poles and rope
Rect(0, 250, 10, 150, fill='silver', border='darkRed')
Rect(195, 250, 10, 150, fill='silver', border='darkRed')
Rect(390, 250, 10, 150, fill='silver', border='darkRed')
Rect(0, 250, 400, 20, fill='red', border='darkRed')

flashes = Group()

def makeCamera(centerX, centerY, cameraColor):
    # rounded edges
    Circle(centerX - 40, centerY - 15, 10, fill='white')
    Circle(centerX + 40, centerY - 15, 10, fill='white')
    Circle(centerX - 40, centerY + 15, 10, fill='white')
    Circle(centerX + 40, centerY + 15, 10, fill='white')

    # base
    Rect(centerX, centerY, 80, 50, fill='white', align='center')
    Rect(centerX, centerY, 100, 30, fill=cameraColor, align='center')

    # button
    Rect(centerX - 35, centerY - 30, 15, 5, fill=cameraColor)

    # lens
    Circle(centerX + 25, centerY, 15, fill='white', border=cameraColor,
           borderWidth=10)

    # flash
    flashes.add(
        Star(centerX + 25, centerY, 30, 12,
             fill=gradient('white', 'yellow', 'gold'), roundness=30, opacity=0)
        )
    flashes.toFront()

def onMousePress(mouseX, mouseY):
    # If the click was above the rope, place a camera at mouseX, mouseY with a
    # completely random color.
    if (mouseY + 25 < 250):
        color = rgb(randrange(0, 256), randrange(0, 256), randrange(0, 256))
        makeCamera(mouseX, mouseY, color)
        # After placing a camera, toggle each flash to turn it on.
        for flash in flashes.children:
            flash.opacity = 100
def onMouseRelease(mouseX, mouseY):
    # Toggles each flash so that it is off.
    for flash in flashes.children:
        flash.opacity = 0

onMousePress(160, 220)
onMouseRelease(160, 220)
onMousePress(300, 90)
onMouseRelease(300, 90)


# -
app.background = 'darkRed'

# brick background
Line(200, 0, 200, 400, fill='indianRed', lineWidth=400, dashes=True)
Line(0, 200, 400, 200, fill='fireBrick', lineWidth=400, dashes=True,
     opacity=50)

# poles and rope
Rect(0, 250, 10, 150, fill='silver', border='darkRed')
Rect(195, 250, 10, 150, fill='silver', border='darkRed')
Rect(390, 250, 10, 150, fill='silver', border='darkRed')
Rect(0, 250, 400, 20, fill='red', border='darkRed')

flashes = Group()

def makeCamera(centerX, centerY, cameraColor):
    # rounded edges
    Circle(centerX - 40, centerY - 15, 10, fill='white')
    Circle(centerX + 40, centerY - 15, 10, fill='white')
    Circle(centerX - 40, centerY + 15, 10, fill='white')
    Circle(centerX + 40, centerY + 15, 10, fill='white')

    # base
    Rect(centerX, centerY, 80, 50, fill='white', align='center')
    Rect(centerX, centerY, 100, 30, fill=cameraColor, align='center')

    # button
    Rect(centerX - 35, centerY - 30, 15, 5, fill=cameraColor)

    # lens
    Circle(centerX + 25, centerY, 15, fill='white', border=cameraColor,
           borderWidth=10)

    # flash
    flashes.add(
        Star(centerX + 25, centerY, 30, 12,
             fill=gradient('white', 'yellow', 'gold'), roundness=30, opacity=0)
        )
    flashes.toFront()

def onMousePress(mouseX, mouseY):
    # If the click was above the rope, place a camera at mouseX, mouseY with a
    # completely random color.
    if (mouseY + 25 < 250):
        color = rgb(randrange(0, 256), randrange(0, 256), randrange(0, 256))
        makeCamera(mouseX, mouseY, color)
        # After placing a camera, toggle each flash to turn it on.
        for flash in flashes.children:
            flash.opacity = 100
def onMouseRelease(mouseX, mouseY):
    # Toggles each flash so that it is off.
    for flash in flashes.children:
        flash.opacity = 0



# -
app.background = 'darkRed'

# brick background
Line(200, 0, 200, 400, fill='indianRed', lineWidth=400, dashes=True)
Line(0, 200, 400, 200, fill='fireBrick', lineWidth=400, dashes=True,
     opacity=50)

# poles and rope
Rect(0, 250, 10, 150, fill='silver', border='darkRed')
Rect(195, 250, 10, 150, fill='silver', border='darkRed')
Rect(390, 250, 10, 150, fill='silver', border='darkRed')
Rect(0, 250, 400, 20, fill='red', border='darkRed')

flashes = Group()

def makeCamera(centerX, centerY, cameraColor):
    # rounded edges
    Circle(centerX - 40, centerY - 15, 10, fill='white')
    Circle(centerX + 40, centerY - 15, 10, fill='white')
    Circle(centerX - 40, centerY + 15, 10, fill='white')
    Circle(centerX + 40, centerY + 15, 10, fill='white')

    # base
    Rect(centerX, centerY, 80, 50, fill='white', align='center')
    Rect(centerX, centerY, 100, 30, fill=cameraColor, align='center')

    # button
    Rect(centerX - 35, centerY - 30, 15, 5, fill=cameraColor)

    # lens
    Circle(centerX + 25, centerY, 15, fill='white', border=cameraColor,
           borderWidth=10)

    # flash
    flashes.add(
        Star(centerX + 25, centerY, 30, 12,
             fill=gradient('white', 'yellow', 'gold'), roundness=30, opacity=0)
        )
    flashes.toFront()

def onMousePress(mouseX, mouseY):
    # If the click was above the rope, place a camera at mouseX, mouseY with a
    # completely random color.
    if (mouseY + 25 < 250):
        color = rgb(randrange(0, 256), randrange(0, 256), randrange(0, 256))
        makeCamera(mouseX, mouseY, color)
        # After placing a camera, toggle each flash to turn it on.
        for flash in flashes.children:
            flash.opacity = 100
def onMouseRelease(mouseX, mouseY):
    # Toggles each flash so that it is off.
    for flash in flashes.children:
        flash.opacity = 0


