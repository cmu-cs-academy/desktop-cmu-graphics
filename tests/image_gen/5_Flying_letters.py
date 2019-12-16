app.background = 'aliceBlue'
app.stepsPerSecond = 30
app.steps = 0

score = Label(0, 200, 200, fill='midnightBlue', size=80, font='monospace',
              bold=True)
keyWord = Label('keyword', 200, 50, fill='midnightBlue', size=40,
                font='monospace', bold=True)
Label('Press space to enter a new keyword', 200, 85, fill='midnightBlue',
      size=16, font='monospace')

bubbles = Group()

def onKeyPress(key):
    if (key == 'space'):
        # Lets the user enter a keyword.
        keyWord.value = app.getTextInput('Type in Your KeyWord')
    else:
        for bubble in bubbles.children:
            # If the key equals the bubble's letter, remove the bubble, and
            # add 1 to the score.
            if (key == bubble.letter):
                score.value += 1
                bubbles.remove(bubble)
def onStep():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    app.steps += 1

    # Every 10 steps, creates a new bubble with a random position and radius.
    if (app.steps % 10 == 0):
        bubbleX = randrange(0, 400)
        radius = randrange(30, 50)
        bubbleY = 400 + radius

        # Get a random letter from the alphabet.
        letterIndex = randrange(0, 26)
        letterInBubble = alphabet[letterIndex]
        # If the letter is in the keyword, make its fill hotPink.
        # Otherwise, it should be deepSkyBlue.
        if (letterInBubble in keyWord.value):
            bubbleColor = 'hotPink'
        else:
            bubbleColor = 'deepSkyBlue'
        # Draws the bubble and the letter and adds them to the bubbles group.
        letterAndBubble = Group(
            Circle(bubbleX, bubbleY, radius, fill=bubbleColor, opacity=25),
            Label('i', bubbleX - (radius // 2), bubbleY + (radius // 2),
                  fill='aliceBlue', size=radius, rotateAngle=320, opacity=60,
                  bold=True),
            Label(letterInBubble, bubbleX, bubbleY, fill='white', size=40)
            )

        # Keeps track of the letter.
        letterAndBubble.letter = letterInBubble
        bubbles.add(letterAndBubble)

    # Updates the bubble's positions, removes any that move off the canvas,
    # and updates the score.
    for bubble in bubbles.children:
        bubble.centerY -= 5
        if (bubble.bottom < 0):
            bubbles.remove(bubble)

            # If the bubble's letter is in the keyWord, subtract 1 from the
            # score. Otherwise add 1.
            if (bubble.letter in keyWord.value):
                score.value -= 1
            else:
                score.value += 1

onSteps(50)
app.paused = True


# -
app.background = 'aliceBlue'
app.stepsPerSecond = 30
app.steps = 0

score = Label(0, 200, 200, fill='midnightBlue', size=80, font='monospace',
              bold=True)
keyWord = Label('keyword', 200, 50, fill='midnightBlue', size=40,
                font='monospace', bold=True)
Label('Press space to enter a new keyword', 200, 85, fill='midnightBlue',
      size=16, font='monospace')

bubbles = Group()

def onKeyPress(key):
    if (key == 'space'):
        # Lets the user enter a keyword.
        keyWord.value = app.getTextInput('Type in Your KeyWord')
    else:
        for bubble in bubbles.children:
            # If the key equals the bubble's letter, remove the bubble, and
            # add 1 to the score.
            if (key == bubble.letter):
                score.value += 1
                bubbles.remove(bubble)
def onStep():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    app.steps += 1

    # Every 10 steps, creates a new bubble with a random position and radius.
    if (app.steps % 10 == 0):
        bubbleX = randrange(0, 400)
        radius = randrange(30, 50)
        bubbleY = 400 + radius

        # Get a random letter from the alphabet.
        letterIndex = randrange(0, 26)
        letterInBubble = alphabet[letterIndex]
        # If the letter is in the keyword, make its fill hotPink.
        # Otherwise, it should be deepSkyBlue.
        if (letterInBubble in keyWord.value):
            bubbleColor = 'hotPink'
        else:
            bubbleColor = 'deepSkyBlue'
        # Draws the bubble and the letter and adds them to the bubbles group.
        letterAndBubble = Group(
            Circle(bubbleX, bubbleY, radius, fill=bubbleColor, opacity=25),
            Label('i', bubbleX - (radius // 2), bubbleY + (radius // 2),
                  fill='aliceBlue', size=radius, rotateAngle=320, opacity=60,
                  bold=True),
            Label(letterInBubble, bubbleX, bubbleY, fill='white', size=40)
            )

        # Keeps track of the letter.
        letterAndBubble.letter = letterInBubble
        bubbles.add(letterAndBubble)

    # Updates the bubble's positions, removes any that move off the canvas,
    # and updates the score.
    for bubble in bubbles.children:
        bubble.centerY -= 5
        if (bubble.bottom < 0):
            bubbles.remove(bubble)

            # If the bubble's letter is in the keyWord, subtract 1 from the
            # score. Otherwise add 1.
            if (bubble.letter in keyWord.value):
                score.value -= 1
            else:
                score.value += 1

onSteps(200)
for letter in 'abcdefghijklmnopqrstuvwxyz':
  onKeyPress(letter)
app.paused = True


# -
app.background = 'aliceBlue'
app.stepsPerSecond = 30
app.steps = 0

score = Label(0, 200, 200, fill='midnightBlue', size=80, font='monospace',
              bold=True)
keyWord = Label('keyword', 200, 50, fill='midnightBlue', size=40,
                font='monospace', bold=True)
Label('Press space to enter a new keyword', 200, 85, fill='midnightBlue',
      size=16, font='monospace')

bubbles = Group()

def onKeyPress(key):
    if (key == 'space'):
        # Lets the user enter a keyword.
        keyWord.value = app.getTextInput('Type in Your KeyWord')
    else:
        for bubble in bubbles.children:
            # If the key equals the bubble's letter, remove the bubble, and
            # add 1 to the score.
            if (key == bubble.letter):
                score.value += 1
                bubbles.remove(bubble)
def onStep():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    app.steps += 1

    # Every 10 steps, creates a new bubble with a random position and radius.
    if (app.steps % 10 == 0):
        bubbleX = randrange(0, 400)
        radius = randrange(30, 50)
        bubbleY = 400 + radius

        # Get a random letter from the alphabet.
        letterIndex = randrange(0, 26)
        letterInBubble = alphabet[letterIndex]
        # If the letter is in the keyword, make its fill hotPink.
        # Otherwise, it should be deepSkyBlue.
        if (letterInBubble in keyWord.value):
            bubbleColor = 'hotPink'
        else:
            bubbleColor = 'deepSkyBlue'
        # Draws the bubble and the letter and adds them to the bubbles group.
        letterAndBubble = Group(
            Circle(bubbleX, bubbleY, radius, fill=bubbleColor, opacity=25),
            Label('i', bubbleX - (radius // 2), bubbleY + (radius // 2),
                  fill='aliceBlue', size=radius, rotateAngle=320, opacity=60,
                  bold=True),
            Label(letterInBubble, bubbleX, bubbleY, fill='white', size=40)
            )

        # Keeps track of the letter.
        letterAndBubble.letter = letterInBubble
        bubbles.add(letterAndBubble)

    # Updates the bubble's positions, removes any that move off the canvas,
    # and updates the score.
    for bubble in bubbles.children:
        bubble.centerY -= 5
        if (bubble.bottom < 0):
            bubbles.remove(bubble)

            # If the bubble's letter is in the keyWord, subtract 1 from the
            # score. Otherwise add 1.
            if (bubble.letter in keyWord.value):
                score.value -= 1
            else:
                score.value += 1

onSteps(50)
for letter in 'abcdefghijklmnopqrstuvwxyz':
  onKeyPress(letter)
app.paused = True

