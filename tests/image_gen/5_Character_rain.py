# background
app.background = gradient('white', 'lightCyan', start='top')

letters = Group()

# tank for letters
tanks = Group(
    Rect(0, 300, 200, 100, fill='lightSkyBlue'),
    Label('UPPERCASE', 100, 360, fill='white', size=18, bold=True),
    Rect(200, 300, 200, 100, fill='lightSkyBlue'),
    Label('lowercase', 300, 360, fill='white', size=18, bold=True),
    Rect(0, 300, 400, 25, fill='steelBlue'),
    Line(200, 300, 200, 400, fill='white', lineWidth=5)
    )

# cloud
Oval(50, 5, 180, 100, fill='silver')
Oval(160, 20, 160, 125, fill='silver')
Oval(270, 5, 130, 130, fill='silver')
Oval(360, 0, 140, 120, fill='silver')

def onStep():
    color = rgb(randrange(0, 100), randrange(100, 256), randrange(200, 256))
    alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

    # Draw a new random letter with a centerX between 100 and 300 (inclusive)
    # and the color defined above.
    randomLetter = alphabet[randrange(0, 52)]
    letter = Label(randomLetter, randrange(100, 301), 0,
                   fill=color, size=20, bold=True)
    # Then set a speed for the letter depending on if it is lowercase or
    # uppercase so that it will move into either the left or right pool.
    if (randomLetter.isupper() == True):
        letter.dx = randrange(-5, -2)
    elif (randomLetter.islower() == True):
        letter.dx = randrange(2, 5)
    letter.dy = randrange(5, 10)
    letters.add(letter)
    # Updates locations of letters and removes letters that leave the canvas.
    for letter in letters.children:
        letter.centerX += letter.dx
        letter.centerY += letter.dy
        if ((letter.right < 0) or (letter.top > 400) or (letter.left > 400)):
            letters.remove(letter)

    tanks.toFront()

onSteps(30)
app.paused = True


# -
# background
app.background = gradient('white', 'lightCyan', start='top')

letters = Group()

# tank for letters
tanks = Group(
    Rect(0, 300, 200, 100, fill='lightSkyBlue'),
    Label('UPPERCASE', 100, 360, fill='white', size=18, bold=True),
    Rect(200, 300, 200, 100, fill='lightSkyBlue'),
    Label('lowercase', 300, 360, fill='white', size=18, bold=True),
    Rect(0, 300, 400, 25, fill='steelBlue'),
    Line(200, 300, 200, 400, fill='white', lineWidth=5)
    )

# cloud
Oval(50, 5, 180, 100, fill='silver')
Oval(160, 20, 160, 125, fill='silver')
Oval(270, 5, 130, 130, fill='silver')
Oval(360, 0, 140, 120, fill='silver')

def onStep():
    color = rgb(randrange(0, 100), randrange(100, 256), randrange(200, 256))
    alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

    # Draw a new random letter with a centerX between 100 and 300 (inclusive)
    # and the color defined above.
    randomLetter = alphabet[randrange(0, 52)]
    letter = Label(randomLetter, randrange(100, 301), 0,
                   fill=color, size=20, bold=True)
    # Then set a speed for the letter depending on if it is lowercase or
    # uppercase so that it will move into either the left or right pool.
    if (randomLetter.isupper() == True):
        letter.dx = randrange(-5, -2)
    elif (randomLetter.islower() == True):
        letter.dx = randrange(2, 5)
    letter.dy = randrange(5, 10)
    letters.add(letter)
    # Updates locations of letters and removes letters that leave the canvas.
    for letter in letters.children:
        letter.centerX += letter.dx
        letter.centerY += letter.dy
        if ((letter.right < 0) or (letter.top > 400) or (letter.left > 400)):
            letters.remove(letter)

    tanks.toFront()

onStep()
app.paused = True


# -
# background
app.background = gradient('white', 'lightCyan', start='top')

letters = Group()

# tank for letters
tanks = Group(
    Rect(0, 300, 200, 100, fill='lightSkyBlue'),
    Label('UPPERCASE', 100, 360, fill='white', size=18, bold=True),
    Rect(200, 300, 200, 100, fill='lightSkyBlue'),
    Label('lowercase', 300, 360, fill='white', size=18, bold=True),
    Rect(0, 300, 400, 25, fill='steelBlue'),
    Line(200, 300, 200, 400, fill='white', lineWidth=5)
    )

# cloud
Oval(50, 5, 180, 100, fill='silver')
Oval(160, 20, 160, 125, fill='silver')
Oval(270, 5, 130, 130, fill='silver')
Oval(360, 0, 140, 120, fill='silver')

def onStep():
    color = rgb(randrange(0, 100), randrange(100, 256), randrange(200, 256))
    alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

    # Draw a new random letter with a centerX between 100 and 300 (inclusive)
    # and the color defined above.
    randomLetter = alphabet[randrange(0, 52)]
    letter = Label(randomLetter, randrange(100, 301), 0,
                   fill=color, size=20, bold=True)
    # Then set a speed for the letter depending on if it is lowercase or
    # uppercase so that it will move into either the left or right pool.
    if (randomLetter.isupper() == True):
        letter.dx = randrange(-5, -2)
    elif (randomLetter.islower() == True):
        letter.dx = randrange(2, 5)
    letter.dy = randrange(5, 10)
    letters.add(letter)
    # Updates locations of letters and removes letters that leave the canvas.
    for letter in letters.children:
        letter.centerX += letter.dx
        letter.centerY += letter.dy
        if ((letter.right < 0) or (letter.top > 400) or (letter.left > 400)):
            letters.remove(letter)

    tanks.toFront()

onStep()
app.paused = True

