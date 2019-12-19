app.background = rgb(205, 230, 240)

season = Label('Spring', 200, 50, size=30)

leaves1 = Circle(200, 260, 75, fill=rgb(140, 195, 30))
leaves2 = Circle(200, 210, 60, fill=rgb(140, 195, 30))
leaves3 = Circle(200, 160, 45, fill=rgb(140, 195, 30))

apple1 = Star(180, 160, 10, 8, fill=gradient('pink', 'violet'), roundness=50)
apple2 = Star(250, 230, 10, 8, fill=gradient('pink', 'violet'), roundness=50)
apple3 = Star(150, 250, 10, 8, fill=gradient('pink', 'violet'), roundness=50)
apple4 = Star(170, 290, 10, 8, fill=gradient('pink', 'violet'), roundness=50)

# trunk
Line(200, 180, 200, 400)

# branches
Line(170, 210, 200, 230)
Line(170, 260, 200, 280)
Line(230, 240, 200, 260)
Line(230, 195, 200, 215)

def colorLeaves(leafColor):
    leaves1.fill = leafColor
    leaves2.fill = leafColor
    leaves3.fill = leafColor

def showApplesOrFlowers(isVisible):
    apple1.visible = isVisible
    apple2.visible = isVisible
    apple3.visible = isVisible
    apple4.visible = isVisible

def changeApples(color, roundness):
    showApplesOrFlowers(True)
    apple1.fill = color
    apple1.roundness = roundness
    apple2.fill = color
    apple2.roundness = roundness
    apple3.fill = color
    apple3.roundness = roundness
    apple4.fill = color
    apple4.roundness = roundness

def onMousePress(mouseX, mouseY):
    # Depending on what season it is, change the leaf, change the Label,
    # and either show or hide the flowers and apples.
    if (season.value == 'Spring'):
        colorLeaves(rgb(50, 153, 50))
        changeApples('red', 100)
        season.value = 'Summer'
    elif (season.value == 'Summer'):
        colorLeaves(rgb(255, 175, 25))
        showApplesOrFlowers(False)
        season.value = 'Fall'
    elif (season.value == 'Fall'):
        colorLeaves('snow')
        showApplesOrFlowers(False)
        season.value = 'Winter'
    elif (season.value == 'Winter'):
        colorLeaves(rgb(140, 195, 30))
        changeApples(gradient('pink', 'violet'), 50)
        season.value = 'Spring'

onMousePress(200, 200)
onMousePress(200, 200)


# -
app.background = rgb(205, 230, 240)

season = Label('Spring', 200, 50, size=30)

leaves1 = Circle(200, 260, 75, fill=rgb(140, 195, 30))
leaves2 = Circle(200, 210, 60, fill=rgb(140, 195, 30))
leaves3 = Circle(200, 160, 45, fill=rgb(140, 195, 30))

apple1 = Star(180, 160, 10, 8, fill=gradient('pink', 'violet'), roundness=50)
apple2 = Star(250, 230, 10, 8, fill=gradient('pink', 'violet'), roundness=50)
apple3 = Star(150, 250, 10, 8, fill=gradient('pink', 'violet'), roundness=50)
apple4 = Star(170, 290, 10, 8, fill=gradient('pink', 'violet'), roundness=50)

# trunk
Line(200, 180, 200, 400)

# branches
Line(170, 210, 200, 230)
Line(170, 260, 200, 280)
Line(230, 240, 200, 260)
Line(230, 195, 200, 215)

def colorLeaves(leafColor):
    leaves1.fill = leafColor
    leaves2.fill = leafColor
    leaves3.fill = leafColor

def showApplesOrFlowers(isVisible):
    apple1.visible = isVisible
    apple2.visible = isVisible
    apple3.visible = isVisible
    apple4.visible = isVisible

def changeApples(color, roundness):
    showApplesOrFlowers(True)
    apple1.fill = color
    apple1.roundness = roundness
    apple2.fill = color
    apple2.roundness = roundness
    apple3.fill = color
    apple3.roundness = roundness
    apple4.fill = color
    apple4.roundness = roundness

def onMousePress(mouseX, mouseY):
    # Depending on what season it is, change the leaf, change the Label,
    # and either show or hide the flowers and apples.
    if (season.value == 'Spring'):
        colorLeaves(rgb(50, 153, 50))
        changeApples('red', 100)
        season.value = 'Summer'
    elif (season.value == 'Summer'):
        colorLeaves(rgb(255, 175, 25))
        showApplesOrFlowers(False)
        season.value = 'Fall'
    elif (season.value == 'Fall'):
        colorLeaves('snow')
        showApplesOrFlowers(False)
        season.value = 'Winter'
    elif (season.value == 'Winter'):
        colorLeaves(rgb(140, 195, 30))
        changeApples(gradient('pink', 'violet'), 50)
        season.value = 'Spring'

onMousePress(200, 200)
onMousePress(200, 200)
onMousePress(200, 200)
onMousePress(200, 200)
onMousePress(200, 200)


# -
app.background = rgb(205, 230, 240)

season = Label('Spring', 200, 50, size=30)

leaves1 = Circle(200, 260, 75, fill=rgb(140, 195, 30))
leaves2 = Circle(200, 210, 60, fill=rgb(140, 195, 30))
leaves3 = Circle(200, 160, 45, fill=rgb(140, 195, 30))

apple1 = Star(180, 160, 10, 8, fill=gradient('pink', 'violet'), roundness=50)
apple2 = Star(250, 230, 10, 8, fill=gradient('pink', 'violet'), roundness=50)
apple3 = Star(150, 250, 10, 8, fill=gradient('pink', 'violet'), roundness=50)
apple4 = Star(170, 290, 10, 8, fill=gradient('pink', 'violet'), roundness=50)

# trunk
Line(200, 180, 200, 400)

# branches
Line(170, 210, 200, 230)
Line(170, 260, 200, 280)
Line(230, 240, 200, 260)
Line(230, 195, 200, 215)

def colorLeaves(leafColor):
    leaves1.fill = leafColor
    leaves2.fill = leafColor
    leaves3.fill = leafColor

def showApplesOrFlowers(isVisible):
    apple1.visible = isVisible
    apple2.visible = isVisible
    apple3.visible = isVisible
    apple4.visible = isVisible

def changeApples(color, roundness):
    showApplesOrFlowers(True)
    apple1.fill = color
    apple1.roundness = roundness
    apple2.fill = color
    apple2.roundness = roundness
    apple3.fill = color
    apple3.roundness = roundness
    apple4.fill = color
    apple4.roundness = roundness

def onMousePress(mouseX, mouseY):
    # Depending on what season it is, change the leaf, change the Label,
    # and either show or hide the flowers and apples.
    if (season.value == 'Spring'):
        colorLeaves(rgb(50, 153, 50))
        changeApples('red', 100)
        season.value = 'Summer'
    elif (season.value == 'Summer'):
        colorLeaves(rgb(255, 175, 25))
        showApplesOrFlowers(False)
        season.value = 'Fall'
    elif (season.value == 'Fall'):
        colorLeaves('snow')
        showApplesOrFlowers(False)
        season.value = 'Winter'
    elif (season.value == 'Winter'):
        colorLeaves(rgb(140, 195, 30))
        changeApples(gradient('pink', 'violet'), 50)
        season.value = 'Spring'

onMousePress(200, 200)

