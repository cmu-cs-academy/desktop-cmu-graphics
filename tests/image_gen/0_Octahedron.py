# background
Rect(0, 0, 400, 400)

def onMousePress(mouseX, mouseY):
    # This code draws four green lines and a circle on each mouse click.
    Line(0, 0, mouseX, mouseY, fill=gradient('black', 'green'))
    Line(0, 400, mouseX, mouseY, fill=gradient('black', 'green'))
    Line(400, 0, mouseX, mouseY, fill=gradient('black', 'green'))
    Line(400, 400, mouseX, mouseY, fill=gradient('black', 'green'))
    Circle(mouseX, mouseY, 5, fill='green')

    # Draw 4 lines and a circle, mirroring the image already drawn.
    Line(0, 0, 400 - mouseX, 400 - mouseY, fill=gradient('black', 'lime'))
    Line(400, 0, 400 - mouseX, 400 - mouseY, fill=gradient('black', 'lime'))
    Line(0, 400, 400 - mouseX, 400 - mouseY, fill=gradient('black', 'lime'))
    Line(400, 400, 400 - mouseX, 400 - mouseY, fill=gradient('black', 'lime'))
    Circle(400 - mouseX, 400 - mouseY, 5, fill='lime')

onMousePress(250, 100)


# -
# background
Rect(0, 0, 400, 400)

def onMousePress(mouseX, mouseY):
    # This code draws four green lines and a circle on each mouse click.
    Line(0, 0, mouseX, mouseY, fill=gradient('black', 'green'))
    Line(0, 400, mouseX, mouseY, fill=gradient('black', 'green'))
    Line(400, 0, mouseX, mouseY, fill=gradient('black', 'green'))
    Line(400, 400, mouseX, mouseY, fill=gradient('black', 'green'))
    Circle(mouseX, mouseY, 5, fill='green')

    # Draw 4 lines and a circle, mirroring the image already drawn.
    Line(0, 0, 400 - mouseX, 400 - mouseY, fill=gradient('black', 'lime'))
    Line(400, 0, 400 - mouseX, 400 - mouseY, fill=gradient('black', 'lime'))
    Line(0, 400, 400 - mouseX, 400 - mouseY, fill=gradient('black', 'lime'))
    Line(400, 400, 400 - mouseX, 400 - mouseY, fill=gradient('black', 'lime'))
    Circle(400 - mouseX, 400 - mouseY, 5, fill='lime')

onMousePress(200, 200)


# -
# background
Rect(0, 0, 400, 400)

def onMousePress(mouseX, mouseY):
    # This code draws four green lines and a circle on each mouse click.
    Line(0, 0, mouseX, mouseY, fill=gradient('black', 'green'))
    Line(0, 400, mouseX, mouseY, fill=gradient('black', 'green'))
    Line(400, 0, mouseX, mouseY, fill=gradient('black', 'green'))
    Line(400, 400, mouseX, mouseY, fill=gradient('black', 'green'))
    Circle(mouseX, mouseY, 5, fill='green')

    # Draw 4 lines and a circle, mirroring the image already drawn.
    Line(0, 0, 400 - mouseX, 400 - mouseY, fill=gradient('black', 'lime'))
    Line(400, 0, 400 - mouseX, 400 - mouseY, fill=gradient('black', 'lime'))
    Line(0, 400, 400 - mouseX, 400 - mouseY, fill=gradient('black', 'lime'))
    Line(400, 400, 400 - mouseX, 400 - mouseY, fill=gradient('black', 'lime'))
    Circle(400 - mouseX, 400 - mouseY, 5, fill='lime')

onMousePress(200, 200)

