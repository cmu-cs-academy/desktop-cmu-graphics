Label('Press space to enter text', 200, 20, size=15)

mainText = Label('', 125, 275, fill='white', size=50)
trails = Group()

def onKeyPress(key):
    dx = randrange(5, 10)
    dy = randrange(5, 10)

    # Gets a word to display.
    if (key == 'space'):
        mainText.value = app.getTextInput()

    # Gets the change in x and y directions based on the key.
    if (key == 'right'):
        dy = 0
    elif (key == 'left'):
        dy = 0
        dx *= -1
    elif (key == 'down'):
        dx = 0
        dy *= -1
    elif (key == 'up'):
        dx = 0

    red = randrange(220, 256)
    green = randrange(220, 256)
    blue = randrange(220, 256)

    # Draw labels with changing colors (by changing the green and blue values),
    # and changing position (by changing the center coordinate by dx and dy).
    # Remember to make the mainText uppercase.
    for i in range(0, 10):
        mainText.centerX += dx
        mainText.centerY -= dy
        green -= 15
        blue -= 20
        mainText.value = mainText.value.upper()
        trails.add(
            Label(mainText.value, mainText.centerX, mainText.centerY,
                  fill=rgb(red, green, blue), size=50, bold=True)
            )
    # If r is pressed, reset the trails and put mainText back to its
    # original position.
    if (key == 'r'):
        trails.clear()
        mainText.value = ''
        mainText.centerX = 125
        mainText.centerY = 275



# -
Label('Press space to enter text', 200, 20, size=15)

mainText = Label('', 125, 275, fill='white', size=50)
trails = Group()

def onKeyPress(key):
    dx = randrange(5, 10)
    dy = randrange(5, 10)

    # Gets a word to display.
    if (key == 'space'):
        mainText.value = app.getTextInput()

    # Gets the change in x and y directions based on the key.
    if (key == 'right'):
        dy = 0
    elif (key == 'left'):
        dy = 0
        dx *= -1
    elif (key == 'down'):
        dx = 0
        dy *= -1
    elif (key == 'up'):
        dx = 0

    red = randrange(220, 256)
    green = randrange(220, 256)
    blue = randrange(220, 256)

    # Draw labels with changing colors (by changing the green and blue values),
    # and changing position (by changing the center coordinate by dx and dy).
    # Remember to make the mainText uppercase.
    for i in range(0, 10):
        mainText.centerX += dx
        mainText.centerY -= dy
        green -= 15
        blue -= 20
        mainText.value = mainText.value.upper()
        trails.add(
            Label(mainText.value, mainText.centerX, mainText.centerY,
                  fill=rgb(red, green, blue), size=50, bold=True)
            )
    # If r is pressed, reset the trails and put mainText back to its
    # original position.
    if (key == 'r'):
        trails.clear()
        mainText.value = ''
        mainText.centerX = 125
        mainText.centerY = 275

app.setTextInputs('hello world')
onKeyPress('space')
onKeyPress('right')
onKeyPress('down')
onKeyPress('left')
onKeyPress('up')


# -
Label('Press space to enter text', 200, 20, size=15)

mainText = Label('', 125, 275, fill='white', size=50)
trails = Group()

def onKeyPress(key):
    dx = randrange(5, 10)
    dy = randrange(5, 10)

    # Gets a word to display.
    if (key == 'space'):
        mainText.value = app.getTextInput()

    # Gets the change in x and y directions based on the key.
    if (key == 'right'):
        dy = 0
    elif (key == 'left'):
        dy = 0
        dx *= -1
    elif (key == 'down'):
        dx = 0
        dy *= -1
    elif (key == 'up'):
        dx = 0

    red = randrange(220, 256)
    green = randrange(220, 256)
    blue = randrange(220, 256)

    # Draw labels with changing colors (by changing the green and blue values),
    # and changing position (by changing the center coordinate by dx and dy).
    # Remember to make the mainText uppercase.
    for i in range(0, 10):
        mainText.centerX += dx
        mainText.centerY -= dy
        green -= 15
        blue -= 20
        mainText.value = mainText.value.upper()
        trails.add(
            Label(mainText.value, mainText.centerX, mainText.centerY,
                  fill=rgb(red, green, blue), size=50, bold=True)
            )
    # If r is pressed, reset the trails and put mainText back to its
    # original position.
    if (key == 'r'):
        trails.clear()
        mainText.value = ''
        mainText.centerX = 125
        mainText.centerY = 275


