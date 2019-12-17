app.background = gradient(rgb(50, 50, 50), 'black')

# stars
for i in range (50):
    Star(randrange(0, 400), randrange(0, 400), 2, 4, fill='white', opacity=50)

# black hole
Circle(200, 200, 75, fill=gradient('black', 'orange', 'orangeRed',
                                   rgb(40, 40, 40), rgb(35, 35, 35)))

letters = Group()

def onMouseMove(mouseX, mouseY):
    alphabet = 'abcdefghijklmnopqrstuvxyz'

    # Gets a new random index from the alphabet and randomly pick upper or lower.
    randomIndex = randrange(len(alphabet))
    letter = alphabet[randomIndex]
    chance = randrange(0, 2)
    if (chance == 0):
        letter = letter.upper()
        color = rgb(randrange(200, 256), 220, 120)
    else:
        color = rgb(255, 255, randrange(220, 256))

    # Adds a new letter at the mouse position.
    letters.add(
        Label(letter, mouseX, mouseY, fill=color, size=randrange(12, 50))
        )

def onStep():
    # Move each letter towards or away from the center.
    for letter in letters.children:
        # Get the angle from the letter to the center of the canvas and use that
        # angle to get the next point of the letter using getPointInDir.
        angle = angleTo(letter.centerX, letter.centerY, 200, 200)
        if (letter.value.islower() == True):
            dist = 5
            letter.size -= 1
            if (letter.size == 0):
                letters.remove(letter)
        else:
            dist = -5
        newX, newY = getPointInDir(letter.centerX, letter.centerY, angle, dist)
        # Move the letter to the new point and add the distance moved to its
        # rotateAngle.
        letter.centerX = newX
        letter.centerY = newY
        letter.rotateAngle += dist
        # Removes any letters that are off the canvas or in the center.
        if ((letter.centerX < 0) or (letter.centerX > 400) or
            (letter.centerY < 0) or (letter.centerY > 400)):
            letters.remove(letter)
        if (abs(letter.centerX - 200) < 25):
            letters.remove(letter)

onMouseMove(50, 50)
onSteps(2)
onMouseMove(50, 100)
onSteps(2)
onMouseMove(50, 150)
onSteps(2)
onMouseMove(50, 200)
onSteps(2)
onMouseMove(50, 250)
onSteps(2)
onMouseMove(50, 300)
onSteps(2)
onMouseMove(50, 350)
onSteps(2)
app.paused = True


# -
app.background = gradient(rgb(50, 50, 50), 'black')

# stars
for i in range (50):
    Star(randrange(0, 400), randrange(0, 400), 2, 4, fill='white', opacity=50)

# black hole
Circle(200, 200, 75, fill=gradient('black', 'orange', 'orangeRed',
                                   rgb(40, 40, 40), rgb(35, 35, 35)))

letters = Group()

def onMouseMove(mouseX, mouseY):
    alphabet = 'abcdefghijklmnopqrstuvxyz'

    # Gets a new random index from the alphabet and randomly pick upper or lower.
    randomIndex = randrange(len(alphabet))
    letter = alphabet[randomIndex]
    chance = randrange(0, 2)
    if (chance == 0):
        letter = letter.upper()
        color = rgb(randrange(200, 256), 220, 120)
    else:
        color = rgb(255, 255, randrange(220, 256))

    # Adds a new letter at the mouse position.
    letters.add(
        Label(letter, mouseX, mouseY, fill=color, size=randrange(12, 50))
        )

def onStep():
    # Move each letter towards or away from the center.
    for letter in letters.children:
        # Get the angle from the letter to the center of the canvas and use that
        # angle to get the next point of the letter using getPointInDir.
        angle = angleTo(letter.centerX, letter.centerY, 200, 200)
        if (letter.value.islower() == True):
            dist = 5
            letter.size -= 1
            if (letter.size == 0):
                letters.remove(letter)
        else:
            dist = -5
        newX, newY = getPointInDir(letter.centerX, letter.centerY, angle, dist)
        # Move the letter to the new point and add the distance moved to its
        # rotateAngle.
        letter.centerX = newX
        letter.centerY = newY
        letter.rotateAngle += dist
        # Removes any letters that are off the canvas or in the center.
        if ((letter.centerX < 0) or (letter.centerX > 400) or
            (letter.centerY < 0) or (letter.centerY > 400)):
            letters.remove(letter)
        if (abs(letter.centerX - 200) < 25):
            letters.remove(letter)

onMouseMove(50, 50)
onSteps(2)
onMouseMove(50, 100)
onSteps(2)
onMouseMove(50, 150)
onSteps(2)
onMouseMove(50, 200)
onSteps(2)
onMouseMove(50, 250)
onSteps(2)
onMouseMove(50, 300)
onSteps(2)
onMouseMove(50, 350)
onSteps(2)
app.paused = True


# -
app.background = gradient(rgb(50, 50, 50), 'black')

# stars
for i in range (50):
    Star(randrange(0, 400), randrange(0, 400), 2, 4, fill='white', opacity=50)

# black hole
Circle(200, 200, 75, fill=gradient('black', 'orange', 'orangeRed',
                                   rgb(40, 40, 40), rgb(35, 35, 35)))

letters = Group()

def onMouseMove(mouseX, mouseY):
    alphabet = 'abcdefghijklmnopqrstuvxyz'

    # Gets a new random index from the alphabet and randomly pick upper or lower.
    randomIndex = randrange(len(alphabet))
    letter = alphabet[randomIndex]
    chance = randrange(0, 2)
    if (chance == 0):
        letter = letter.upper()
        color = rgb(randrange(200, 256), 220, 120)
    else:
        color = rgb(255, 255, randrange(220, 256))

    # Adds a new letter at the mouse position.
    letters.add(
        Label(letter, mouseX, mouseY, fill=color, size=randrange(12, 50))
        )

def onStep():
    # Move each letter towards or away from the center.
    for letter in letters.children:
        # Get the angle from the letter to the center of the canvas and use that
        # angle to get the next point of the letter using getPointInDir.
        angle = angleTo(letter.centerX, letter.centerY, 200, 200)
        if (letter.value.islower() == True):
            dist = 5
            letter.size -= 1
            if (letter.size == 0):
                letters.remove(letter)
        else:
            dist = -5
        newX, newY = getPointInDir(letter.centerX, letter.centerY, angle, dist)
        # Move the letter to the new point and add the distance moved to its
        # rotateAngle.
        letter.centerX = newX
        letter.centerY = newY
        letter.rotateAngle += dist
        # Removes any letters that are off the canvas or in the center.
        if ((letter.centerX < 0) or (letter.centerX > 400) or
            (letter.centerY < 0) or (letter.centerY > 400)):
            letters.remove(letter)
        if (abs(letter.centerX - 200) < 25):
            letters.remove(letter)

onMouseMove(50, 50)
app.paused = True

