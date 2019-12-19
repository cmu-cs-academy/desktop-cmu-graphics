# background
Rect(0, 0, 400, 400, fill='lightBlue')

Label('Click near here for light circles', 200, 50)
Label('Click near here for dark circles', 200, 350)

def onMousePress(mouseX, mouseY):
    # Add an opacity to the circle below to make it lighter. The opacity
    # should depend on where the mouse was pressed.
    Circle(mouseX, mouseY, 50, fill='navy', opacity=mouseY/4)

onMousePress(100, 100)


# -
# background
Rect(0, 0, 400, 400, fill='lightBlue')

Label('Click near here for light circles', 200, 50)
Label('Click near here for dark circles', 200, 350)

def onMousePress(mouseX, mouseY):
    # Add an opacity to the circle below to make it lighter. The opacity
    # should depend on where the mouse was pressed.
    Circle(mouseX, mouseY, 50, fill='navy', opacity=mouseY/4)

onMousePress(300, 300)


# -
# background
Rect(0, 0, 400, 400, fill='lightBlue')

Label('Click near here for light circles', 200, 50)
Label('Click near here for dark circles', 200, 350)

def onMousePress(mouseX, mouseY):
    # Add an opacity to the circle below to make it lighter. The opacity
    # should depend on where the mouse was pressed.
    Circle(mouseX, mouseY, 50, fill='navy', opacity=mouseY/4)

onMousePress(300, 300)

