app.background = gradient(rgb(135, 250, 250), rgb(15, 125, 195), start='top')

# fish
yellowFish = Polygon(140, 100, 100, 60, 110, 95, 90, 85, 100, 100, 90, 120,
                     110, 105, 100, 140,
                     fill=gradient('white', 'lemonChiffon', 'gold', 'darkOrange',
                                   start='right'))
yellowFishEye = Circle(130, 95, 3)
yellowFishScore = Label(0, 50, 100, fill='yellow', size=50)

purpleFish = Polygon(140, 300, 100, 260, 110, 295, 90, 285, 100, 300, 90, 320,
                     110, 305, 100, 340,
                     fill=gradient('white', 'lavender', 'orchid', 'darkOrchid',
                                   start='right'))
purpleFishEye = Circle(130, 295, 3)
purpleFishScore = Label(0, 50, 300, fill=rgb(210, 190, 255), size=50)

Label('Underwater Tag', 200, 20, size=22)
Label('When two fish collide, the fish on the left scores that point.', 200, 40)
Label('One fish moves faster up/down, the other moves faster left/right!', 200, 55)

def checkFishIntersection():
    # Check if the fish intersect and add point to the left one.
    # Then, reset the location for both fish.
    if (yellowFish.hitsShape(purpleFish) == True):
        if (yellowFish.centerX < purpleFish.centerX):
            yellowFishScore.value += 1
        else:
            purpleFishScore.value += 1
        yellowFish.centerX = 115
        yellowFish.centerY = 100
        yellowFishEye.centerX = 130
        yellowFishEye.centerY = 95
        purpleFish.centerX = 115
        purpleFish.centerY = 300
        purpleFishEye.centerX = 130
        purpleFishEye.centerY = 295
def checkFishBounds(fish):
    # Check if a fish is outside the canvas bounds and wraparound.
    if (fish.centerY < 0):
        fish.centerY = 400
    elif (fish.centerY > 400):
        fish.centerY = 0
    if (fish.centerX < 0):
        fish.centerX = 400
    elif (fish.centerX > 400):
        fish.centerX = 0
def moveEyes():
    # Move the eyes of both fish relative to its body.
    yellowFishEye.centerX = yellowFish.centerX + 15
    yellowFishEye.centerY = yellowFish.centerY - 5
    purpleFishEye.centerX = purpleFish.centerX + 15
    purpleFishEye.centerY = purpleFish.centerY - 5
def onKeyHold(keys):
    # Move the fish in their respective directions.
    if ('w' in keys):
        yellowFish.centerY -= 10
    elif ('s' in keys):
        yellowFish.centerY += 10
    elif ('a' in keys):
        yellowFish.centerX -= 5
    elif ('d' in keys):
        yellowFish.centerX += 5

    if ('up' in keys):
        purpleFish.centerY -= 5
    elif ('down' in keys):
        purpleFish.centerY += 5
    elif ('left' in keys):
        purpleFish.centerX -= 10
    elif ('right' in keys):
        purpleFish.centerX += 10

    checkFishBounds(yellowFish)
    checkFishBounds(purpleFish)

    # Move the eyes.
    moveEyes()

    # Update score appropriately, if fish intersect each other.
    checkFishIntersection()

onKeyHolds(['up'], 20)
onKeyHolds(['right'], 20)


# -
app.background = gradient(rgb(135, 250, 250), rgb(15, 125, 195), start='top')

# fish
yellowFish = Polygon(140, 100, 100, 60, 110, 95, 90, 85, 100, 100, 90, 120,
                     110, 105, 100, 140,
                     fill=gradient('white', 'lemonChiffon', 'gold', 'darkOrange',
                                   start='right'))
yellowFishEye = Circle(130, 95, 3)
yellowFishScore = Label(0, 50, 100, fill='yellow', size=50)

purpleFish = Polygon(140, 300, 100, 260, 110, 295, 90, 285, 100, 300, 90, 320,
                     110, 305, 100, 340,
                     fill=gradient('white', 'lavender', 'orchid', 'darkOrchid',
                                   start='right'))
purpleFishEye = Circle(130, 295, 3)
purpleFishScore = Label(0, 50, 300, fill=rgb(210, 190, 255), size=50)

Label('Underwater Tag', 200, 20, size=22)
Label('When two fish collide, the fish on the left scores that point.', 200, 40)
Label('One fish moves faster up/down, the other moves faster left/right!', 200, 55)

def checkFishIntersection():
    # Check if the fish intersect and add point to the left one.
    # Then, reset the location for both fish.
    if (yellowFish.hitsShape(purpleFish) == True):
        if (yellowFish.centerX < purpleFish.centerX):
            yellowFishScore.value += 1
        else:
            purpleFishScore.value += 1
        yellowFish.centerX = 115
        yellowFish.centerY = 100
        yellowFishEye.centerX = 130
        yellowFishEye.centerY = 95
        purpleFish.centerX = 115
        purpleFish.centerY = 300
        purpleFishEye.centerX = 130
        purpleFishEye.centerY = 295
def checkFishBounds(fish):
    # Check if a fish is outside the canvas bounds and wraparound.
    if (fish.centerY < 0):
        fish.centerY = 400
    elif (fish.centerY > 400):
        fish.centerY = 0
    if (fish.centerX < 0):
        fish.centerX = 400
    elif (fish.centerX > 400):
        fish.centerX = 0
def moveEyes():
    # Move the eyes of both fish relative to its body.
    yellowFishEye.centerX = yellowFish.centerX + 15
    yellowFishEye.centerY = yellowFish.centerY - 5
    purpleFishEye.centerX = purpleFish.centerX + 15
    purpleFishEye.centerY = purpleFish.centerY - 5
def onKeyHold(keys):
    # Move the fish in their respective directions.
    if ('w' in keys):
        yellowFish.centerY -= 10
    elif ('s' in keys):
        yellowFish.centerY += 10
    elif ('a' in keys):
        yellowFish.centerX -= 5
    elif ('d' in keys):
        yellowFish.centerX += 5

    if ('up' in keys):
        purpleFish.centerY -= 5
    elif ('down' in keys):
        purpleFish.centerY += 5
    elif ('left' in keys):
        purpleFish.centerX -= 10
    elif ('right' in keys):
        purpleFish.centerX += 10

    checkFishBounds(yellowFish)
    checkFishBounds(purpleFish)

    # Move the eyes.
    moveEyes()

    # Update score appropriately, if fish intersect each other.
    checkFishIntersection()



# -
app.background = gradient(rgb(135, 250, 250), rgb(15, 125, 195), start='top')

# fish
yellowFish = Polygon(140, 100, 100, 60, 110, 95, 90, 85, 100, 100, 90, 120,
                     110, 105, 100, 140,
                     fill=gradient('white', 'lemonChiffon', 'gold', 'darkOrange',
                                   start='right'))
yellowFishEye = Circle(130, 95, 3)
yellowFishScore = Label(0, 50, 100, fill='yellow', size=50)

purpleFish = Polygon(140, 300, 100, 260, 110, 295, 90, 285, 100, 300, 90, 320,
                     110, 305, 100, 340,
                     fill=gradient('white', 'lavender', 'orchid', 'darkOrchid',
                                   start='right'))
purpleFishEye = Circle(130, 295, 3)
purpleFishScore = Label(0, 50, 300, fill=rgb(210, 190, 255), size=50)

Label('Underwater Tag', 200, 20, size=22)
Label('When two fish collide, the fish on the left scores that point.', 200, 40)
Label('One fish moves faster up/down, the other moves faster left/right!', 200, 55)

def checkFishIntersection():
    # Check if the fish intersect and add point to the left one.
    # Then, reset the location for both fish.
    if (yellowFish.hitsShape(purpleFish) == True):
        if (yellowFish.centerX < purpleFish.centerX):
            yellowFishScore.value += 1
        else:
            purpleFishScore.value += 1
        yellowFish.centerX = 115
        yellowFish.centerY = 100
        yellowFishEye.centerX = 130
        yellowFishEye.centerY = 95
        purpleFish.centerX = 115
        purpleFish.centerY = 300
        purpleFishEye.centerX = 130
        purpleFishEye.centerY = 295
def checkFishBounds(fish):
    # Check if a fish is outside the canvas bounds and wraparound.
    if (fish.centerY < 0):
        fish.centerY = 400
    elif (fish.centerY > 400):
        fish.centerY = 0
    if (fish.centerX < 0):
        fish.centerX = 400
    elif (fish.centerX > 400):
        fish.centerX = 0
def moveEyes():
    # Move the eyes of both fish relative to its body.
    yellowFishEye.centerX = yellowFish.centerX + 15
    yellowFishEye.centerY = yellowFish.centerY - 5
    purpleFishEye.centerX = purpleFish.centerX + 15
    purpleFishEye.centerY = purpleFish.centerY - 5
def onKeyHold(keys):
    # Move the fish in their respective directions.
    if ('w' in keys):
        yellowFish.centerY -= 10
    elif ('s' in keys):
        yellowFish.centerY += 10
    elif ('a' in keys):
        yellowFish.centerX -= 5
    elif ('d' in keys):
        yellowFish.centerX += 5

    if ('up' in keys):
        purpleFish.centerY -= 5
    elif ('down' in keys):
        purpleFish.centerY += 5
    elif ('left' in keys):
        purpleFish.centerX -= 10
    elif ('right' in keys):
        purpleFish.centerX += 10

    checkFishBounds(yellowFish)
    checkFishBounds(purpleFish)

    # Move the eyes.
    moveEyes()

    # Update score appropriately, if fish intersect each other.
    checkFishIntersection()

onKeyHolds(['left'], 10)
onKeyHolds(['up'], 40)
onKeyHolds(['right'], 10)
onKeyHolds(['d'], 10)
onKeyHolds(['s'], 20)

