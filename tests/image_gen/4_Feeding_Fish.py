app.background = gradient('cyan', 'deepSkyBlue', 'royalBlue', start='top')

# Run faster than the default.
app.stepsPerSecond = 60

# food
food = Circle(275, 0, 5, fill='orange')
Label('Food eaten:', 200, 345, fill='white', size=25)
foodCount = Label(0, 200, 375, fill='white', size=25)

# fish
fishBody = Oval(100, 200, 60, 40, fill=gradient('gold', 'yellow', start='left'))
fishTail = Polygon(70, 200, 60, 180, 60, 220,
                   fill=gradient('gold', 'yellow', start='left'))
fishEye = Circle(115, 195, 2)
fish = Group(fishBody, fishTail, fishEye)

# Start the fish right in the center of the canvas.
fish.centerX = 200
fish.centerY = 300

def onStep():
    # Move the fish horizontally by 5 pixels and the food vertically by 2 pixels.
    # Don't forget to wraparound!
    fish.centerX += 5
    food.centerY += 2
    if (fish.left > 400):
        fish.right = 0
    if (food.centerY > 400):
        food.centerY = 0

    # If the fish eats the food, put it at the top again and increase the fish's
    # size by 5 pixels.
    if (fishBody.hitsShape(food) == True):
        foodCount.value += 1
        food.centerY = 0
        fish.height += 5
        fish.width += 5

    # Otherwise, move the fish up or down 1 pixel towards the food.
    elif (fishBody.centerY <= food.centerY):
        fish.centerY += 1
    else:
        fish.centerY -= 1

onSteps(5)
app.paused = True


# -
app.background = gradient('cyan', 'deepSkyBlue', 'royalBlue', start='top')

# Run faster than the default.
app.stepsPerSecond = 60

# food
food = Circle(275, 0, 5, fill='orange')
Label('Food eaten:', 200, 345, fill='white', size=25)
foodCount = Label(0, 200, 375, fill='white', size=25)

# fish
fishBody = Oval(100, 200, 60, 40, fill=gradient('gold', 'yellow', start='left'))
fishTail = Polygon(70, 200, 60, 180, 60, 220,
                   fill=gradient('gold', 'yellow', start='left'))
fishEye = Circle(115, 195, 2)
fish = Group(fishBody, fishTail, fishEye)

# Start the fish right in the center of the canvas.
fish.centerX = 200
fish.centerY = 300

def onStep():
    # Move the fish horizontally by 5 pixels and the food vertically by 2 pixels.
    # Don't forget to wraparound!
    fish.centerX += 5
    food.centerY += 2
    if (fish.left > 400):
        fish.right = 0
    if (food.centerY > 400):
        food.centerY = 0

    # If the fish eats the food, put it at the top again and increase the fish's
    # size by 5 pixels.
    if (fishBody.hitsShape(food) == True):
        foodCount.value += 1
        food.centerY = 0
        fish.height += 5
        fish.width += 5

    # Otherwise, move the fish up or down 1 pixel towards the food.
    elif (fishBody.centerY <= food.centerY):
        fish.centerY += 1
    else:
        fish.centerY -= 1

onSteps(170)
app.paused = True


# -
app.background = gradient('cyan', 'deepSkyBlue', 'royalBlue', start='top')

# Run faster than the default.
app.stepsPerSecond = 60

# food
food = Circle(275, 0, 5, fill='orange')
Label('Food eaten:', 200, 345, fill='white', size=25)
foodCount = Label(0, 200, 375, fill='white', size=25)

# fish
fishBody = Oval(100, 200, 60, 40, fill=gradient('gold', 'yellow', start='left'))
fishTail = Polygon(70, 200, 60, 180, 60, 220,
                   fill=gradient('gold', 'yellow', start='left'))
fishEye = Circle(115, 195, 2)
fish = Group(fishBody, fishTail, fishEye)

# Start the fish right in the center of the canvas.
fish.centerX = 200
fish.centerY = 300

def onStep():
    # Move the fish horizontally by 5 pixels and the food vertically by 2 pixels.
    # Don't forget to wraparound!
    fish.centerX += 5
    food.centerY += 2
    if (fish.left > 400):
        fish.right = 0
    if (food.centerY > 400):
        food.centerY = 0

    # If the fish eats the food, put it at the top again and increase the fish's
    # size by 5 pixels.
    if (fishBody.hitsShape(food) == True):
        foodCount.value += 1
        food.centerY = 0
        fish.height += 5
        fish.width += 5

    # Otherwise, move the fish up or down 1 pixel towards the food.
    elif (fishBody.centerY <= food.centerY):
        fish.centerY += 1
    else:
        fish.centerY -= 1

onSteps(170)
app.paused = True

