app.background = gradient('dodgerBlue', 'navy')

dot1 = Circle(100, 100, 10, fill=gradient('lightCoral', 'crimson'))
dot2 = Circle(300, 100, 10, fill=gradient('lightCoral', 'crimson'))
dot3 = Circle(100, 300, 10, fill=gradient('lightCoral', 'crimson'))
dot4 = Circle(300, 300, 10, fill=gradient('lightCoral', 'crimson'))

Line(0, 200, 400, 200, dashes=True)
Line(200, 400, 200, 0, dashes=True)

def onMouseMove(mouseX, mouseY):
    # Dot 1 should follow the mouse exactly.
    dot1.centerX = mouseX
    dot1.centerY = mouseY

    # Dot 2 should follow the mouse but reflected in horizontal movement.
    dot2.centerX = 400 - mouseX
    dot2.centerY = mouseY

    # Dot 3 should follow the mouse but reflected in vertical movement.
    dot3.centerX = mouseX
    dot3.centerY = 400 - mouseY

    # Dot 4 should follow the mouse but reflected in both horizontal and
    # vertical movement.
    dot4.centerX = 400 - mouseX
    dot4.centerY = 400 - mouseY

onMouseMove(110, 180)


# -
app.background = gradient('dodgerBlue', 'navy')

dot1 = Circle(100, 100, 10, fill=gradient('lightCoral', 'crimson'))
dot2 = Circle(300, 100, 10, fill=gradient('lightCoral', 'crimson'))
dot3 = Circle(100, 300, 10, fill=gradient('lightCoral', 'crimson'))
dot4 = Circle(300, 300, 10, fill=gradient('lightCoral', 'crimson'))

Line(0, 200, 400, 200, dashes=True)
Line(200, 400, 200, 0, dashes=True)

def onMouseMove(mouseX, mouseY):
    # Dot 1 should follow the mouse exactly.
    dot1.centerX = mouseX
    dot1.centerY = mouseY

    # Dot 2 should follow the mouse but reflected in horizontal movement.
    dot2.centerX = 400 - mouseX
    dot2.centerY = mouseY

    # Dot 3 should follow the mouse but reflected in vertical movement.
    dot3.centerX = mouseX
    dot3.centerY = 400 - mouseY

    # Dot 4 should follow the mouse but reflected in both horizontal and
    # vertical movement.
    dot4.centerX = 400 - mouseX
    dot4.centerY = 400 - mouseY



# -
app.background = gradient('dodgerBlue', 'navy')

dot1 = Circle(100, 100, 10, fill=gradient('lightCoral', 'crimson'))
dot2 = Circle(300, 100, 10, fill=gradient('lightCoral', 'crimson'))
dot3 = Circle(100, 300, 10, fill=gradient('lightCoral', 'crimson'))
dot4 = Circle(300, 300, 10, fill=gradient('lightCoral', 'crimson'))

Line(0, 200, 400, 200, dashes=True)
Line(200, 400, 200, 0, dashes=True)

def onMouseMove(mouseX, mouseY):
    # Dot 1 should follow the mouse exactly.
    dot1.centerX = mouseX
    dot1.centerY = mouseY

    # Dot 2 should follow the mouse but reflected in horizontal movement.
    dot2.centerX = 400 - mouseX
    dot2.centerY = mouseY

    # Dot 3 should follow the mouse but reflected in vertical movement.
    dot3.centerX = mouseX
    dot3.centerY = 400 - mouseY

    # Dot 4 should follow the mouse but reflected in both horizontal and
    # vertical movement.
    dot4.centerX = 400 - mouseX
    dot4.centerY = 400 - mouseY

onMouseMove(50, 50)
onMouseMove(5, 100)
onMouseMove(250, 50)
onMouseMove(300, 140)
onMouseMove(100, 250)
onMouseMove(280, 230)
onMouseMove(350, 300)

