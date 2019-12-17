app.background = 'darkBlue'

icon = Group(
    Label('DVD', 220, 200, fill='white', size=50, bold=True),
    Oval(220, 230, 110, 20, fill='white'),
    Label('video', 220, 230, fill='darkBlue', size=15)
    )
icon.dx = 5
icon.dy = 5

def onStep():
    # Move the icon by the amount indicated by icon.dx and icon.dy.
    icon.centerX += icon.dx
    icon.centerY += icon.dy

    # Reverse the direction of the icon if it reaches an edge of the canvas.
    if ((icon.left <= 0) or (icon.right >= 400)):
        icon.dx = -icon.dx
    if ((icon.top <= 0) or (icon.bottom >= 400)):
        icon.dy = -icon.dy

onStep()
app.paused = True


# -
app.background = 'darkBlue'

icon = Group(
    Label('DVD', 220, 200, fill='white', size=50, bold=True),
    Oval(220, 230, 110, 20, fill='white'),
    Label('video', 220, 230, fill='darkBlue', size=15)
    )
icon.dx = 5
icon.dy = 5

def onStep():
    # Move the icon by the amount indicated by icon.dx and icon.dy.
    icon.centerX += icon.dx
    icon.centerY += icon.dy

    # Reverse the direction of the icon if it reaches an edge of the canvas.
    if ((icon.left <= 0) or (icon.right >= 400)):
        icon.dx = -icon.dx
    if ((icon.top <= 0) or (icon.bottom >= 400)):
        icon.dy = -icon.dy

onSteps(30)
app.paused = True


# -
app.background = 'darkBlue'

icon = Group(
    Label('DVD', 220, 200, fill='white', size=50, bold=True),
    Oval(220, 230, 110, 20, fill='white'),
    Label('video', 220, 230, fill='darkBlue', size=15)
    )
icon.dx = 5
icon.dy = 5

def onStep():
    # Move the icon by the amount indicated by icon.dx and icon.dy.
    icon.centerX += icon.dx
    icon.centerY += icon.dy

    # Reverse the direction of the icon if it reaches an edge of the canvas.
    if ((icon.left <= 0) or (icon.right >= 400)):
        icon.dx = -icon.dx
    if ((icon.top <= 0) or (icon.bottom >= 400)):
        icon.dy = -icon.dy

onSteps(85)
app.paused = True

