app.background = gradient('white', 'dodgerBlue', start='bottom')

# the earth
earth = Circle(200, 200, 100, fill='royalBlue', border='black')
Polygon(176, 107, 188, 131, 167, 151, 170, 180, 150, 170, 130, 180, 115, 180,
        110, 160, 135, 130, fill='darkGreen')
Polygon(170, 180, 220, 170, 210, 190, 205, 200, 200, 220, 180, 280, 170, 250,
        160, 220, 160, 180, fill='darkGreen')
Polygon(230, 140, 240, 110, 290, 165, fill='darkGreen')
Circle(200, 200, 100, fill=None, border='black', borderWidth=6)

def drawMessage():
    message = 'PEACE ON EARTH '

    # Calculates the amount the angle should change between each letter.
    stepAngle = 360 / len(message)

    # Loops through the letters of the message to draw them separately.
    for i in range(len(message)):
        # Use getPointInDir and the stepAngle to calculate the (x, y) point for
        # each letter.
        ### (HINT: Use the radius of the circle + 15 for the distance.)
        x, y = getPointInDir(200, 200, i * stepAngle, earth.radius + 15)
        # Use the stepAngle to also calculate the rotateAngle for each letter.
        rAngle = i * stepAngle
        # Draw a label using the current character, position, and rotateAngle.
        Label(message[i], x, y, size=30, rotateAngle=rAngle, bold=True)
drawMessage()


