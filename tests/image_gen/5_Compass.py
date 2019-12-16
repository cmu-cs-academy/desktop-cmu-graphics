app.background = rgb(60, 60, 60)

# ring
Circle(200, 200, 110, fill=None, border='ghostWhite', borderWidth=3, dashes=(40, 1))
Circle(200, 200, 145, fill=None, border='ghostWhite', borderWidth=3, dashes=(80, 1))

# compass labels
Label('N', 200, 75, fill='ghostWhite', size=30)
Label('S', 200, 325, fill='ghostWhite', size=30)
Label('W', 75, 200, fill='ghostWhite', size=30)
Label('E', 325, 200, fill='ghostWhite', size=30)

# fancy star background
Star(200, 200, 100, 12, fill='ghostWhite', roundness=20)
Star(200, 200, 100, 12, fill=app.background, roundness=10)
Star(200, 200, 100, 12, fill='ghostWhite', roundness=5)

# Create the needle as a line with the arrowEnd equal to True.
needle = Line(200, 200, 200, 120, fill='crimson', lineWidth=8, arrowEnd=True)
def onMouseMove(mouseX, mouseY):
    # Get the angle between the point (200, 200) and the current mouse position.
    angle = angleTo(200, 200, mouseX, mouseY)
    # Use getPointInDir function to get the newX2, and newY2 values for the needle.
    newX2, newY2 = getPointInDir(200, 200, angle, 80)
    # Set the needle's x2 and y2 to the values calculated above.
    needle.x2 = newX2
    needle.y2 = newY2

onMouseMove(300, 300)


# -
app.background = rgb(60, 60, 60)

# ring
Circle(200, 200, 110, fill=None, border='ghostWhite', borderWidth=3, dashes=(40, 1))
Circle(200, 200, 145, fill=None, border='ghostWhite', borderWidth=3, dashes=(80, 1))

# compass labels
Label('N', 200, 75, fill='ghostWhite', size=30)
Label('S', 200, 325, fill='ghostWhite', size=30)
Label('W', 75, 200, fill='ghostWhite', size=30)
Label('E', 325, 200, fill='ghostWhite', size=30)

# fancy star background
Star(200, 200, 100, 12, fill='ghostWhite', roundness=20)
Star(200, 200, 100, 12, fill=app.background, roundness=10)
Star(200, 200, 100, 12, fill='ghostWhite', roundness=5)

# Create the needle as a line with the arrowEnd equal to True.
needle = Line(200, 200, 200, 120, fill='crimson', lineWidth=8, arrowEnd=True)
def onMouseMove(mouseX, mouseY):
    # Get the angle between the point (200, 200) and the current mouse position.
    angle = angleTo(200, 200, mouseX, mouseY)
    # Use getPointInDir function to get the newX2, and newY2 values for the needle.
    newX2, newY2 = getPointInDir(200, 200, angle, 80)
    # Set the needle's x2 and y2 to the values calculated above.
    needle.x2 = newX2
    needle.y2 = newY2



# -
app.background = rgb(60, 60, 60)

# ring
Circle(200, 200, 110, fill=None, border='ghostWhite', borderWidth=3, dashes=(40, 1))
Circle(200, 200, 145, fill=None, border='ghostWhite', borderWidth=3, dashes=(80, 1))

# compass labels
Label('N', 200, 75, fill='ghostWhite', size=30)
Label('S', 200, 325, fill='ghostWhite', size=30)
Label('W', 75, 200, fill='ghostWhite', size=30)
Label('E', 325, 200, fill='ghostWhite', size=30)

# fancy star background
Star(200, 200, 100, 12, fill='ghostWhite', roundness=20)
Star(200, 200, 100, 12, fill=app.background, roundness=10)
Star(200, 200, 100, 12, fill='ghostWhite', roundness=5)

# Create the needle as a line with the arrowEnd equal to True.
needle = Line(200, 200, 200, 120, fill='crimson', lineWidth=8, arrowEnd=True)
def onMouseMove(mouseX, mouseY):
    # Get the angle between the point (200, 200) and the current mouse position.
    angle = angleTo(200, 200, mouseX, mouseY)
    # Use getPointInDir function to get the newX2, and newY2 values for the needle.
    newX2, newY2 = getPointInDir(200, 200, angle, 80)
    # Set the needle's x2 and y2 to the values calculated above.
    needle.x2 = newX2
    needle.y2 = newY2

onMouseMove(0, 200)

