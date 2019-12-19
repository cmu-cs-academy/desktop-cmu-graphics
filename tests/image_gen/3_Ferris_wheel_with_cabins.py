# background
app.background = gradient('moccasin', 'papayaWhip', start='top')
Polygon(200, 400, 360, 340, 450, 400,
        fill=gradient('gold', 'goldenrod', start='top'))
Polygon(-100, 400, 40, 300, 300, 400,
        fill=gradient('orange', 'tomato', start='top'))

# rotating piece of ferris wheel
rotatingSpikes = Star(200, 200, 150, 10, fill=gradient('gainsboro', 'gray'),
                      roundness=15)

# rings
rings = Group(
    Circle(200, 200, 75, fill=None, border='blue', borderWidth=8, opacity=70),
    Circle(200, 200, 50, fill=None, border='red', borderWidth=6, opacity=70),
    Circle(200, 200, 150, fill=None, borderWidth=10, opacity=70,
           border=gradient('blue', 'red', 'green', 'yellow', start='top')),
    Circle(200, 200, 146, fill=None, border='white'),
    Circle(200, 200, 154, fill=None, border='white')
    )

cabins = Group()

# legs
Line(120, 400, 200, 200, fill='white', lineWidth=12)
Line(280, 400, 200, 200, fill='white', lineWidth=12)
Circle(200, 200, 6, fill='white')

def makeCabins(numberOfCabins):
    stepAngle = 360 / numberOfCabins
    for i in range(numberOfCabins):
        # Gets a random color for the cabin.
        color = rgb(randrange(0, 256), 0, randrange(150, 256))

        # Get the new centerX and centerY for the cabins by using the
        # getPointInDir function. The angle should be i * stepAngle and the
        # distance should be 155.
        centerX, centerY = getPointInDir(200, 200, i * stepAngle, 155)
        # Makes a new cabin.
        cabin = Group(
            Arc(centerX, centerY, 50, 60, 90, 180, fill=color),
            Arc(centerX, centerY - 20, 50, 30, 270, 180, fill=color),
            Line(centerX - 20, centerY, centerX - 20, centerY - 20),
            Line(centerX + 20, centerY, centerX + 20, centerY - 20)
            )

        # Sets a custom property of the cabin to use for rotating later.
        cabin.currentAngle = i * stepAngle

        # Adds the cabin to the cabins Group.
        cabins.add(cabin)

makeCabins(rotatingSpikes.points)

def onStep():
    rotatingSpikes.rotateAngle += 1
    rings.rotateAngle += 1

    # Loop through each cabin.
    for cabin in cabins:
        # Prepare to move the cabin by 1 degree by using a custom property.
        cabin.currentAngle += 1
        # Get the new centerX and centerY of the cabin by using
        # getPointInDir with the currentAngle property used above
        # and 155 for the distance.
        newCenterX, newCenterY = getPointInDir(200, 200, cabin.currentAngle, 155)
        # Set the centerX and centerY of the cabin to the new point.
        cabin.centerX = newCenterX
        cabin.centerY = newCenterY

onSteps(50)
app.paused = True


# -
# background
app.background = gradient('moccasin', 'papayaWhip', start='top')
Polygon(200, 400, 360, 340, 450, 400,
        fill=gradient('gold', 'goldenrod', start='top'))
Polygon(-100, 400, 40, 300, 300, 400,
        fill=gradient('orange', 'tomato', start='top'))

# rotating piece of ferris wheel
rotatingSpikes = Star(200, 200, 150, 10, fill=gradient('gainsboro', 'gray'),
                      roundness=15)

# rings
rings = Group(
    Circle(200, 200, 75, fill=None, border='blue', borderWidth=8, opacity=70),
    Circle(200, 200, 50, fill=None, border='red', borderWidth=6, opacity=70),
    Circle(200, 200, 150, fill=None, borderWidth=10, opacity=70,
           border=gradient('blue', 'red', 'green', 'yellow', start='top')),
    Circle(200, 200, 146, fill=None, border='white'),
    Circle(200, 200, 154, fill=None, border='white')
    )

cabins = Group()

# legs
Line(120, 400, 200, 200, fill='white', lineWidth=12)
Line(280, 400, 200, 200, fill='white', lineWidth=12)
Circle(200, 200, 6, fill='white')

def makeCabins(numberOfCabins):
    stepAngle = 360 / numberOfCabins
    for i in range(numberOfCabins):
        # Gets a random color for the cabin.
        color = rgb(randrange(0, 256), 0, randrange(150, 256))

        # Get the new centerX and centerY for the cabins by using the
        # getPointInDir function. The angle should be i * stepAngle and the
        # distance should be 155.
        centerX, centerY = getPointInDir(200, 200, i * stepAngle, 155)
        # Makes a new cabin.
        cabin = Group(
            Arc(centerX, centerY, 50, 60, 90, 180, fill=color),
            Arc(centerX, centerY - 20, 50, 30, 270, 180, fill=color),
            Line(centerX - 20, centerY, centerX - 20, centerY - 20),
            Line(centerX + 20, centerY, centerX + 20, centerY - 20)
            )

        # Sets a custom property of the cabin to use for rotating later.
        cabin.currentAngle = i * stepAngle

        # Adds the cabin to the cabins Group.
        cabins.add(cabin)

makeCabins(rotatingSpikes.points)

def onStep():
    rotatingSpikes.rotateAngle += 1
    rings.rotateAngle += 1

    # Loop through each cabin.
    for cabin in cabins:
        # Prepare to move the cabin by 1 degree by using a custom property.
        cabin.currentAngle += 1
        # Get the new centerX and centerY of the cabin by using
        # getPointInDir with the currentAngle property used above
        # and 155 for the distance.
        newCenterX, newCenterY = getPointInDir(200, 200, cabin.currentAngle, 155)
        # Set the centerX and centerY of the cabin to the new point.
        cabin.centerX = newCenterX
        cabin.centerY = newCenterY

onStep()
app.paused = True


# -
# background
app.background = gradient('moccasin', 'papayaWhip', start='top')
Polygon(200, 400, 360, 340, 450, 400,
        fill=gradient('gold', 'goldenrod', start='top'))
Polygon(-100, 400, 40, 300, 300, 400,
        fill=gradient('orange', 'tomato', start='top'))

# rotating piece of ferris wheel
rotatingSpikes = Star(200, 200, 150, 10, fill=gradient('gainsboro', 'gray'),
                      roundness=15)

# rings
rings = Group(
    Circle(200, 200, 75, fill=None, border='blue', borderWidth=8, opacity=70),
    Circle(200, 200, 50, fill=None, border='red', borderWidth=6, opacity=70),
    Circle(200, 200, 150, fill=None, borderWidth=10, opacity=70,
           border=gradient('blue', 'red', 'green', 'yellow', start='top')),
    Circle(200, 200, 146, fill=None, border='white'),
    Circle(200, 200, 154, fill=None, border='white')
    )

cabins = Group()

# legs
Line(120, 400, 200, 200, fill='white', lineWidth=12)
Line(280, 400, 200, 200, fill='white', lineWidth=12)
Circle(200, 200, 6, fill='white')

def makeCabins(numberOfCabins):
    stepAngle = 360 / numberOfCabins
    for i in range(numberOfCabins):
        # Gets a random color for the cabin.
        color = rgb(randrange(0, 256), 0, randrange(150, 256))

        # Get the new centerX and centerY for the cabins by using the
        # getPointInDir function. The angle should be i * stepAngle and the
        # distance should be 155.
        centerX, centerY = getPointInDir(200, 200, i * stepAngle, 155)
        # Makes a new cabin.
        cabin = Group(
            Arc(centerX, centerY, 50, 60, 90, 180, fill=color),
            Arc(centerX, centerY - 20, 50, 30, 270, 180, fill=color),
            Line(centerX - 20, centerY, centerX - 20, centerY - 20),
            Line(centerX + 20, centerY, centerX + 20, centerY - 20)
            )

        # Sets a custom property of the cabin to use for rotating later.
        cabin.currentAngle = i * stepAngle

        # Adds the cabin to the cabins Group.
        cabins.add(cabin)

makeCabins(rotatingSpikes.points)

def onStep():
    rotatingSpikes.rotateAngle += 1
    rings.rotateAngle += 1

    # Loop through each cabin.
    for cabin in cabins:
        # Prepare to move the cabin by 1 degree by using a custom property.
        cabin.currentAngle += 1
        # Get the new centerX and centerY of the cabin by using
        # getPointInDir with the currentAngle property used above
        # and 155 for the distance.
        newCenterX, newCenterY = getPointInDir(200, 200, cabin.currentAngle, 155)
        # Set the centerX and centerY of the cabin to the new point.
        cabin.centerX = newCenterX
        cabin.centerY = newCenterY

onSteps(50)
app.paused = True

