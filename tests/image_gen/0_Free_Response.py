app.background = 'green'

app.plantedFlowers = makeList(5, 5)
app.groundPlacements = [ ]
app.index = 1

farmer = Group(
    Rect(190, 190, 20, 25, fill='dodgerBlue'),
    Circle(200, 185, 10, fill='tan'),
    Arc(200, 180, 25, 20, 90, 180, fill='papayaWhip', border='darkKhaki',
        borderWidth=1),
    Oval(200, 180, 20, 10, fill='papayaWhip', border='darkKhaki', borderWidth=1),
    Line(190, 215, 210, 215, fill='darkBlue', lineWidth=8),
    Line(190, 220, 210, 220, fill='darkBlue', lineWidth=10, dashes=(9, 2)),
    Line(186, 200, 214, 200, fill='tan', lineWidth=20, dashes=(4, 20)),
    Line(190, 190, 210, 190, fill='gold', lineWidth=10, dashes=(2, 16))
    )
farmer.targetX = 40
farmer.targetY = 80
farmer.standing = 0

def placeGroundSpots():
    for y in range(80, 401, 80):
        for x in range(40, 361, 80):
            app.groundPlacements.append([ x, y ])

placeGroundSpots()

def plant(x, y):
    # As long as we haven't placed all of the flowers, creates a mound
    # where a flower will grow out of.
    if (app.index <= len(app.groundPlacements)):
        flower = Group(
            Arc(x, y, 30, 20, 270, 180, fill='peru')
            )
        flower.state = 'mound'
        flower.timeInState = 0

        farmer.toFront()

        # Add the flower to the app.plantedFlowers list.
        col = x // 80
        row = y // 80 - 1
        app.plantedFlowers[row][col] = flower
def sprout(flower):
    # Adds a stem to the mound so the plant sprouts.
    x = flower.centerX
    y = flower.bottom
    flower.add(
        Line(x, y - 10, x, y - 25, fill='springGreen', lineWidth=3)
        )
    flower.state = 'sprout'

def leaf(flower):
    # Adds a leaf to the plant.
    x = flower.centerX
    y = flower.top
    leaf = Oval(x, y - 10, 15, 10, fill='springGreen', rotateAngle=-30)
    leaf.left = x
    flower.add(
        Line(x, y, x, y - 30, fill='springGreen', lineWidth=3),
        leaf
        )
    flower.state = 'leaf'

def bloom(flower):
    # Adds a flower to the top of the plant.
    x = flower.centerX
    y = flower.top
    flower.add(
        Line(x, y, x, y - 10, fill='springGreen', lineWidth=3),
        Star(x, y - 10, 20, 12, fill='gold'),
        Circle(x, y - 10, 10, fill='saddleBrown')
        )
    flower.state = 'flower'

def onStep():
    if ((abs(farmer.centerX - farmer.targetX) <= 3) and
        (abs(farmer.centerY - farmer.targetY) <= 3)):
        farmer.standing += 1

        # If the farmer has been standing for 10 steps, plants a flower.
        if (farmer.standing >= 5):
            plant(farmer.targetX, farmer.targetY)
            farmer.standing = 0

            # Set the next target position as the next location in
            # app.groundPlacements.
            if (app.index < len(app.groundPlacements)):
                farmer.targetX = app.groundPlacements[app.index][0]
                farmer.targetY = app.groundPlacements[app.index][1]
            app.index += 1

    else:
        # Move towards the next mound.
        angle = angleTo(farmer.centerX, farmer.centerY,
                        farmer.targetX, farmer.targetY)
        x, y = getPointInDir(farmer.centerX, farmer.centerY, angle, 5)
        farmer.centerX = x
        farmer.centerY = y

    # For each flower that has been planted, increase its timeInState property and,
    # if timeInState is at least 150, move to the next state by calling a
    # provided helper function.
    for row in range(len(app.plantedFlowers)):
        for col in range(len(app.plantedFlowers[0])):
            flower = app.plantedFlowers[row][col]
            if (flower != None):
                flower.timeInState += 1
                if (flower.timeInState >= 150):
                    flower.timeInState = 0
                    if (flower.state == 'mound'):
                        sprout(flower)
                    elif (flower.state == 'sprout'):
                        leaf(flower)
                    elif (flower.state == 'leaf'):
                        bloom(flower)



# -
app.background = 'green'

app.plantedFlowers = makeList(5, 5)
app.groundPlacements = [ ]
app.index = 1

farmer = Group(
    Rect(190, 190, 20, 25, fill='dodgerBlue'),
    Circle(200, 185, 10, fill='tan'),
    Arc(200, 180, 25, 20, 90, 180, fill='papayaWhip', border='darkKhaki',
        borderWidth=1),
    Oval(200, 180, 20, 10, fill='papayaWhip', border='darkKhaki', borderWidth=1),
    Line(190, 215, 210, 215, fill='darkBlue', lineWidth=8),
    Line(190, 220, 210, 220, fill='darkBlue', lineWidth=10, dashes=(9, 2)),
    Line(186, 200, 214, 200, fill='tan', lineWidth=20, dashes=(4, 20)),
    Line(190, 190, 210, 190, fill='gold', lineWidth=10, dashes=(2, 16))
    )
farmer.targetX = 40
farmer.targetY = 80
farmer.standing = 0

def placeGroundSpots():
    for y in range(80, 401, 80):
        for x in range(40, 361, 80):
            app.groundPlacements.append([ x, y ])

placeGroundSpots()

def plant(x, y):
    # As long as we haven't placed all of the flowers, creates a mound
    # where a flower will grow out of.
    if (app.index <= len(app.groundPlacements)):
        flower = Group(
            Arc(x, y, 30, 20, 270, 180, fill='peru')
            )
        flower.state = 'mound'
        flower.timeInState = 0

        farmer.toFront()

        # Add the flower to the app.plantedFlowers list.
        col = x // 80
        row = y // 80 - 1
        app.plantedFlowers[row][col] = flower
def sprout(flower):
    # Adds a stem to the mound so the plant sprouts.
    x = flower.centerX
    y = flower.bottom
    flower.add(
        Line(x, y - 10, x, y - 25, fill='springGreen', lineWidth=3)
        )
    flower.state = 'sprout'

def leaf(flower):
    # Adds a leaf to the plant.
    x = flower.centerX
    y = flower.top
    leaf = Oval(x, y - 10, 15, 10, fill='springGreen', rotateAngle=-30)
    leaf.left = x
    flower.add(
        Line(x, y, x, y - 30, fill='springGreen', lineWidth=3),
        leaf
        )
    flower.state = 'leaf'

def bloom(flower):
    # Adds a flower to the top of the plant.
    x = flower.centerX
    y = flower.top
    flower.add(
        Line(x, y, x, y - 10, fill='springGreen', lineWidth=3),
        Star(x, y - 10, 20, 12, fill='gold'),
        Circle(x, y - 10, 10, fill='saddleBrown')
        )
    flower.state = 'flower'

def onStep():
    if ((abs(farmer.centerX - farmer.targetX) <= 3) and
        (abs(farmer.centerY - farmer.targetY) <= 3)):
        farmer.standing += 1

        # If the farmer has been standing for 10 steps, plants a flower.
        if (farmer.standing >= 5):
            plant(farmer.targetX, farmer.targetY)
            farmer.standing = 0

            # Set the next target position as the next location in
            # app.groundPlacements.
            if (app.index < len(app.groundPlacements)):
                farmer.targetX = app.groundPlacements[app.index][0]
                farmer.targetY = app.groundPlacements[app.index][1]
            app.index += 1

    else:
        # Move towards the next mound.
        angle = angleTo(farmer.centerX, farmer.centerY,
                        farmer.targetX, farmer.targetY)
        x, y = getPointInDir(farmer.centerX, farmer.centerY, angle, 5)
        farmer.centerX = x
        farmer.centerY = y

    # For each flower that has been planted, increase its timeInState property and,
    # if timeInState is at least 150, move to the next state by calling a
    # provided helper function.
    for row in range(len(app.plantedFlowers)):
        for col in range(len(app.plantedFlowers[0])):
            flower = app.plantedFlowers[row][col]
            if (flower != None):
                flower.timeInState += 1
                if (flower.timeInState >= 150):
                    flower.timeInState = 0
                    if (flower.state == 'mound'):
                        sprout(flower)
                    elif (flower.state == 'sprout'):
                        leaf(flower)
                    elif (flower.state == 'leaf'):
                        bloom(flower)

app.stepsPerSecond = 300
onSteps(135)
app.paused = True


# -
app.background = 'green'

app.plantedFlowers = makeList(5, 5)
app.groundPlacements = [ ]
app.index = 1

farmer = Group(
    Rect(190, 190, 20, 25, fill='dodgerBlue'),
    Circle(200, 185, 10, fill='tan'),
    Arc(200, 180, 25, 20, 90, 180, fill='papayaWhip', border='darkKhaki',
        borderWidth=1),
    Oval(200, 180, 20, 10, fill='papayaWhip', border='darkKhaki', borderWidth=1),
    Line(190, 215, 210, 215, fill='darkBlue', lineWidth=8),
    Line(190, 220, 210, 220, fill='darkBlue', lineWidth=10, dashes=(9, 2)),
    Line(186, 200, 214, 200, fill='tan', lineWidth=20, dashes=(4, 20)),
    Line(190, 190, 210, 190, fill='gold', lineWidth=10, dashes=(2, 16))
    )
farmer.targetX = 40
farmer.targetY = 80
farmer.standing = 0

def placeGroundSpots():
    for y in range(80, 401, 80):
        for x in range(40, 361, 80):
            app.groundPlacements.append([ x, y ])

placeGroundSpots()

def plant(x, y):
    # As long as we haven't placed all of the flowers, creates a mound
    # where a flower will grow out of.
    if (app.index <= len(app.groundPlacements)):
        flower = Group(
            Arc(x, y, 30, 20, 270, 180, fill='peru')
            )
        flower.state = 'mound'
        flower.timeInState = 0

        farmer.toFront()

        # Add the flower to the app.plantedFlowers list.
        col = x // 80
        row = y // 80 - 1
        app.plantedFlowers[row][col] = flower
def sprout(flower):
    # Adds a stem to the mound so the plant sprouts.
    x = flower.centerX
    y = flower.bottom
    flower.add(
        Line(x, y - 10, x, y - 25, fill='springGreen', lineWidth=3)
        )
    flower.state = 'sprout'

def leaf(flower):
    # Adds a leaf to the plant.
    x = flower.centerX
    y = flower.top
    leaf = Oval(x, y - 10, 15, 10, fill='springGreen', rotateAngle=-30)
    leaf.left = x
    flower.add(
        Line(x, y, x, y - 30, fill='springGreen', lineWidth=3),
        leaf
        )
    flower.state = 'leaf'

def bloom(flower):
    # Adds a flower to the top of the plant.
    x = flower.centerX
    y = flower.top
    flower.add(
        Line(x, y, x, y - 10, fill='springGreen', lineWidth=3),
        Star(x, y - 10, 20, 12, fill='gold'),
        Circle(x, y - 10, 10, fill='saddleBrown')
        )
    flower.state = 'flower'

def onStep():
    if ((abs(farmer.centerX - farmer.targetX) <= 3) and
        (abs(farmer.centerY - farmer.targetY) <= 3)):
        farmer.standing += 1

        # If the farmer has been standing for 10 steps, plants a flower.
        if (farmer.standing >= 5):
            plant(farmer.targetX, farmer.targetY)
            farmer.standing = 0

            # Set the next target position as the next location in
            # app.groundPlacements.
            if (app.index < len(app.groundPlacements)):
                farmer.targetX = app.groundPlacements[app.index][0]
                farmer.targetY = app.groundPlacements[app.index][1]
            app.index += 1

    else:
        # Move towards the next mound.
        angle = angleTo(farmer.centerX, farmer.centerY,
                        farmer.targetX, farmer.targetY)
        x, y = getPointInDir(farmer.centerX, farmer.centerY, angle, 5)
        farmer.centerX = x
        farmer.centerY = y

    # For each flower that has been planted, increase its timeInState property and,
    # if timeInState is at least 150, move to the next state by calling a
    # provided helper function.
    for row in range(len(app.plantedFlowers)):
        for col in range(len(app.plantedFlowers[0])):
            flower = app.plantedFlowers[row][col]
            if (flower != None):
                flower.timeInState += 1
                if (flower.timeInState >= 150):
                    flower.timeInState = 0
                    if (flower.state == 'mound'):
                        sprout(flower)
                    elif (flower.state == 'sprout'):
                        leaf(flower)
                    elif (flower.state == 'leaf'):
                        bloom(flower)


