app.background = 'black'

# moon
outerMoon = Circle(200, 200, 165,
                   fill=gradient(rgb(120, 120, 120), rgb(218, 218, 218),
                                 start='left'))
innerMoon = Circle(200, 200, 135, fill=gradient('grey', 'lightGrey', start='left'))
innerMoon.nextRadius = 30

def onMousePress(mouseX, mouseY):
    # Check if the inner portion of the moon was clicked on. If it was, draw a
    # crater with radius innerMoon.nextRadius and set the nextRadius for the
    # next crater.
    if (innerMoon.hits(mouseX, mouseY) == True):
        Circle(mouseX, mouseY, innerMoon.nextRadius,
               fill=gradient('darkGrey', 'grey', start='left'))
        if (innerMoon.nextRadius == 20):
            innerMoon.nextRadius = 30
        else:
            innerMoon.nextRadius = 20
    # If none of the moon was clicked on, draw a star.
    elif (outerMoon.hits(mouseX, mouseY) == False):
        Star(mouseX, mouseY, 5, 4, fill='white')

onMousePress(130, 100)
onMousePress(260, 10)
onMousePress(330, 190)
onMousePress(60, 380)
onMousePress(200, 320)
onMousePress(180, 20)
onMousePress(80, 210)


# -
app.background = 'black'

# moon
outerMoon = Circle(200, 200, 165,
                   fill=gradient(rgb(120, 120, 120), rgb(218, 218, 218),
                                 start='left'))
innerMoon = Circle(200, 200, 135, fill=gradient('grey', 'lightGrey', start='left'))
innerMoon.nextRadius = 30

def onMousePress(mouseX, mouseY):
    # Check if the inner portion of the moon was clicked on. If it was, draw a
    # crater with radius innerMoon.nextRadius and set the nextRadius for the
    # next crater.
    if (innerMoon.hits(mouseX, mouseY) == True):
        Circle(mouseX, mouseY, innerMoon.nextRadius,
               fill=gradient('darkGrey', 'grey', start='left'))
        if (innerMoon.nextRadius == 20):
            innerMoon.nextRadius = 30
        else:
            innerMoon.nextRadius = 20
    # If none of the moon was clicked on, draw a star.
    elif (outerMoon.hits(mouseX, mouseY) == False):
        Star(mouseX, mouseY, 5, 4, fill='white')

onMousePress(120, 300)


# -
app.background = 'black'

# moon
outerMoon = Circle(200, 200, 165,
                   fill=gradient(rgb(120, 120, 120), rgb(218, 218, 218),
                                 start='left'))
innerMoon = Circle(200, 200, 135, fill=gradient('grey', 'lightGrey', start='left'))
innerMoon.nextRadius = 30

def onMousePress(mouseX, mouseY):
    # Check if the inner portion of the moon was clicked on. If it was, draw a
    # crater with radius innerMoon.nextRadius and set the nextRadius for the
    # next crater.
    if (innerMoon.hits(mouseX, mouseY) == True):
        Circle(mouseX, mouseY, innerMoon.nextRadius,
               fill=gradient('darkGrey', 'grey', start='left'))
        if (innerMoon.nextRadius == 20):
            innerMoon.nextRadius = 30
        else:
            innerMoon.nextRadius = 20
    # If none of the moon was clicked on, draw a star.
    elif (outerMoon.hits(mouseX, mouseY) == False):
        Star(mouseX, mouseY, 5, 4, fill='white')

onMousePress(50, 50)

