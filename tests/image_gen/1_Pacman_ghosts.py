# background
Rect(0, 0, 400, 400, fill='midnightBlue')

# Parameters give the center of the white part of the eye.
def drawEye(eyeCenterX, eyeCenterY):
    Circle(eyeCenterX, eyeCenterY, 20, fill='white')
    Circle(eyeCenterX, eyeCenterY, 10, fill='cornflowerBlue', align='right')

# x is the centerX of the body, y is the centerY of all feet.
def drawFeet(x, y, color):
    Circle(x - 40, y, 20, fill=color)
    Circle(x + 40, y, 20, fill=color)
    Circle(x, y, 20, fill=color)

# centerX and centerY are the center of the body of the ghost.
def drawGhost(centerX, centerY, name, color):
    # body
    Rect(centerX, centerY, 120, 80, fill=color, align='center')

    # head
    Circle(centerX, centerY - 40, 60, fill=color)

    # Draw the eyes.
    drawEye(centerX - 25, centerY - 55)
    drawEye(centerX + 20, centerY - 55)
    # Draw the feet.
    drawFeet(centerX, centerY + 40, color)
    # Create a label with the name of the ghost.
    Label(name, centerX, centerY + 70, fill='white', size=25, font='monospace')

drawGhost(100, 100, 'Dave', 'red')
drawGhost(300, 300, 'Markus', 'blue')


# -
# background
Rect(0, 0, 400, 400, fill='midnightBlue')

# Parameters give the center of the white part of the eye.
def drawEye(eyeCenterX, eyeCenterY):
    Circle(eyeCenterX, eyeCenterY, 20, fill='white')
    Circle(eyeCenterX, eyeCenterY, 10, fill='cornflowerBlue', align='right')

# x is the centerX of the body, y is the centerY of all feet.
def drawFeet(x, y, color):
    Circle(x - 40, y, 20, fill=color)
    Circle(x + 40, y, 20, fill=color)
    Circle(x, y, 20, fill=color)

# centerX and centerY are the center of the body of the ghost.
def drawGhost(centerX, centerY, name, color):
    # body
    Rect(centerX, centerY, 120, 80, fill=color, align='center')

    # head
    Circle(centerX, centerY - 40, 60, fill=color)

    # Draw the eyes.
    drawEye(centerX - 25, centerY - 55)
    drawEye(centerX + 20, centerY - 55)
    # Draw the feet.
    drawFeet(centerX, centerY + 40, color)
    # Create a label with the name of the ghost.
    Label(name, centerX, centerY + 70, fill='white', size=25, font='monospace')

drawGhost(200, 200, 'Sue', 'forestGreen')


# -
# background
Rect(0, 0, 400, 400, fill='midnightBlue')

# Parameters give the center of the white part of the eye.
def drawEye(eyeCenterX, eyeCenterY):
    Circle(eyeCenterX, eyeCenterY, 20, fill='white')
    Circle(eyeCenterX, eyeCenterY, 10, fill='cornflowerBlue', align='right')

# x is the centerX of the body, y is the centerY of all feet.
def drawFeet(x, y, color):
    Circle(x - 40, y, 20, fill=color)
    Circle(x + 40, y, 20, fill=color)
    Circle(x, y, 20, fill=color)

# centerX and centerY are the center of the body of the ghost.
def drawGhost(centerX, centerY, name, color):
    # body
    Rect(centerX, centerY, 120, 80, fill=color, align='center')

    # head
    Circle(centerX, centerY - 40, 60, fill=color)

    # Draw the eyes.
    drawEye(centerX - 25, centerY - 55)
    drawEye(centerX + 20, centerY - 55)
    # Draw the feet.
    drawFeet(centerX, centerY + 40, color)
    # Create a label with the name of the ghost.
    Label(name, centerX, centerY + 70, fill='white', size=25, font='monospace')

drawGhost(200, 200, 'Sue', 'violet')

