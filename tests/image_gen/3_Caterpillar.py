app.background = gradient('deepSkyBlue', 'lightSkyBlue', start='top')
app.stepsPerSecond = 5

evenPieces = Group()
evenPieces.dy = 1
oddPieces = Group()
oddPieces.dy = 0

worm = Group(evenPieces, oddPieces)

# leaves and twig
Oval(155, 315, 200, 110, rotateAngle=30,
     fill=gradient('mediumSeaGreen', 'darkGreen', start='bottom'))
Oval(420, 200, 175, 90, rotateAngle=-30,
     fill=gradient('mediumSeaGreen', 'darkGreen', start='top'))
Line(0, 250, 400, 250, lineWidth=35,
     fill=gradient('mediumSeaGreen', 'darkGreen', start='top'))

# Fix the for loop so that it draws the head (last circle) and
# colors the caterpillar properly.
for centerX in range(60, 331, 30):
    # This variable is used to check whether the next piece of the caterpillar
    # should be in the odd group or the even group.
    oddOrEven = (centerX - 60) // 30
    # Add a conditional to create the alternating color pattern.
    if (centerX == 330):
        head = Group(
            Circle(centerX, 200, 20, fill='crimson'),
            Circle(centerX, 200, 3),
            Circle(centerX + 20, 200, 3),
            Line(centerX + 2, 185, centerX + 2, 165),
            Line(centerX + 12, 185, centerX + 12, 165)
            )
        evenPieces.add(head)
    elif (oddOrEven % 2 == 0):
        piece = Group(
            Label('L', centerX, 225, fill='seaGreen', size=18, bold=True),
            Circle(centerX, 200, 20, fill='seaGreen')
            )
        evenPieces.add(piece)
    else:
        piece = Group(
            Label('L', centerX, 225, fill='lightGreen', size=18, bold=True),
            Circle(centerX, 200, 20, fill='lightGreen')
            )
        oddPieces.add(piece)
def onStep():
    for shape in evenPieces:
        shape.centerY += evenPieces.dy
    for shape in oddPieces:
        shape.centerY += oddPieces.dy

    # Moves the worm, with wraparound.
    worm.centerX += 2
    if (worm.left >= 400):
        worm.right = 0

    # Adjusts the direction the body parts move.
    evenPieces.dy *= -1
    if (oddPieces.dy == 0):
        oddPieces.dy = 1
    else:
        oddPieces.dy *= -1


onSteps(2)
app.paused = True


# -
app.background = gradient('deepSkyBlue', 'lightSkyBlue', start='top')
app.stepsPerSecond = 5

evenPieces = Group()
evenPieces.dy = 1
oddPieces = Group()
oddPieces.dy = 0

worm = Group(evenPieces, oddPieces)

# leaves and twig
Oval(155, 315, 200, 110, rotateAngle=30,
     fill=gradient('mediumSeaGreen', 'darkGreen', start='bottom'))
Oval(420, 200, 175, 90, rotateAngle=-30,
     fill=gradient('mediumSeaGreen', 'darkGreen', start='top'))
Line(0, 250, 400, 250, lineWidth=35,
     fill=gradient('mediumSeaGreen', 'darkGreen', start='top'))

# Fix the for loop so that it draws the head (last circle) and
# colors the caterpillar properly.
for centerX in range(60, 331, 30):
    # This variable is used to check whether the next piece of the caterpillar
    # should be in the odd group or the even group.
    oddOrEven = (centerX - 60) // 30
    # Add a conditional to create the alternating color pattern.
    if (centerX == 330):
        head = Group(
            Circle(centerX, 200, 20, fill='crimson'),
            Circle(centerX, 200, 3),
            Circle(centerX + 20, 200, 3),
            Line(centerX + 2, 185, centerX + 2, 165),
            Line(centerX + 12, 185, centerX + 12, 165)
            )
        evenPieces.add(head)
    elif (oddOrEven % 2 == 0):
        piece = Group(
            Label('L', centerX, 225, fill='seaGreen', size=18, bold=True),
            Circle(centerX, 200, 20, fill='seaGreen')
            )
        evenPieces.add(piece)
    else:
        piece = Group(
            Label('L', centerX, 225, fill='lightGreen', size=18, bold=True),
            Circle(centerX, 200, 20, fill='lightGreen')
            )
        oddPieces.add(piece)
def onStep():
    for shape in evenPieces:
        shape.centerY += evenPieces.dy
    for shape in oddPieces:
        shape.centerY += oddPieces.dy

    # Moves the worm, with wraparound.
    worm.centerX += 2
    if (worm.left >= 400):
        worm.right = 0

    # Adjusts the direction the body parts move.
    evenPieces.dy *= -1
    if (oddPieces.dy == 0):
        oddPieces.dy = 1
    else:
        oddPieces.dy *= -1


onSteps(10)
app.paused = True


# -
app.background = gradient('deepSkyBlue', 'lightSkyBlue', start='top')
app.stepsPerSecond = 5

evenPieces = Group()
evenPieces.dy = 1
oddPieces = Group()
oddPieces.dy = 0

worm = Group(evenPieces, oddPieces)

# leaves and twig
Oval(155, 315, 200, 110, rotateAngle=30,
     fill=gradient('mediumSeaGreen', 'darkGreen', start='bottom'))
Oval(420, 200, 175, 90, rotateAngle=-30,
     fill=gradient('mediumSeaGreen', 'darkGreen', start='top'))
Line(0, 250, 400, 250, lineWidth=35,
     fill=gradient('mediumSeaGreen', 'darkGreen', start='top'))

# Fix the for loop so that it draws the head (last circle) and
# colors the caterpillar properly.
for centerX in range(60, 331, 30):
    # This variable is used to check whether the next piece of the caterpillar
    # should be in the odd group or the even group.
    oddOrEven = (centerX - 60) // 30
    # Add a conditional to create the alternating color pattern.
    if (centerX == 330):
        head = Group(
            Circle(centerX, 200, 20, fill='crimson'),
            Circle(centerX, 200, 3),
            Circle(centerX + 20, 200, 3),
            Line(centerX + 2, 185, centerX + 2, 165),
            Line(centerX + 12, 185, centerX + 12, 165)
            )
        evenPieces.add(head)
    elif (oddOrEven % 2 == 0):
        piece = Group(
            Label('L', centerX, 225, fill='seaGreen', size=18, bold=True),
            Circle(centerX, 200, 20, fill='seaGreen')
            )
        evenPieces.add(piece)
    else:
        piece = Group(
            Label('L', centerX, 225, fill='lightGreen', size=18, bold=True),
            Circle(centerX, 200, 20, fill='lightGreen')
            )
        oddPieces.add(piece)
def onStep():
    for shape in evenPieces:
        shape.centerY += evenPieces.dy
    for shape in oddPieces:
        shape.centerY += oddPieces.dy

    # Moves the worm, with wraparound.
    worm.centerX += 2
    if (worm.left >= 400):
        worm.right = 0

    # Adjusts the direction the body parts move.
    evenPieces.dy *= -1
    if (oddPieces.dy == 0):
        oddPieces.dy = 1
    else:
        oddPieces.dy *= -1


onStep()
app.paused = True

