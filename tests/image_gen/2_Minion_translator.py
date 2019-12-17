app.background = 'paleGreen'

# chatbox
Oval(240, 150, 200, 150, fill='white')
Oval(215, 175, 220, 145, fill='paleGreen')
Oval(200, 85, 300, 80, fill='white')

# face and mouth
Rect(120, 200, 155, 300, fill='gold')
Circle(198, 210, 78, fill='gold')
Oval(200, 270, 50, 30)
Oval(200, 260, 50, 30, fill='gold')

# glasses and eyes
Rect(120, 200, 155, 20)
Circle(165, 210, 30, fill='snow', border='dimGray', borderWidth=8)
Circle(235, 210, 30, fill='snow', border='dimGray', borderWidth=8)
Circle(165, 210, 13, border='saddleBrown', borderWidth=5)
Circle(235, 210, 13, border='saddleBrown', borderWidth=5)
Circle(160, 205, 3, fill='white')
Circle(230, 205, 3, fill='white')

# arms and hands
Line(125, 300, 105, 325, fill='gold', lineWidth=8)
Line(106, 320, 110, 370, fill='gold', lineWidth=8)
Line(270, 285, 290, 325, fill='gold', lineWidth=8)
Line(290, 325, 290, 370, fill='gold', lineWidth=8)
Line(110, 360, 120, 370, lineWidth=8)
Line(290, 360, 280, 370, lineWidth=8)
Oval(110, 370, 15, 25)
Oval(290, 370, 15, 25)

# trousers
Line(120, 300, 160, 320, fill='steelBlue', lineWidth=10)
Line(275, 290, 240, 320, fill='steelBlue', lineWidth=10)
Rect(155, 315, 90, 80, fill='steelBlue')
Rect(120, 385, 155, 30, fill='steelBlue')
Rect(185, 340, 30, 20, fill='steelBlue', border='black', borderWidth=3,
     dashes=True)

Label('Press space to enter text to translate', 200, 20, size=15)
minionLabel = Label('', 200, 85, size=20, bold=True)

def onKeyPress(key):
    if (key == 'space'):
        # Gets the text to translate and creates the minion's alphabet.
        text = app.getTextInput('Minion, please translate this sentence for me:')
        minionAlphabet = text + '~!#? &@'
        minionText = ''

        # Add letters to minionText until it is the same length as minionAlphabet.
        while (len(minionText) < len(minionAlphabet)):
            # In the loop, get a random letter from the minion's alphabet.
            randomIndex = randrange(0, len(minionAlphabet))
            randomLetter = minionAlphabet[randomIndex]
            # Starting with the first letter, every other letter in minionText
            # should be uppercase. If the random letter picked should be
            # uppercase, make it uppercase then add it to minionText!
            if (len(minionText) % 2 == 0):
                randomLetter = randomLetter.upper()
            minionText += randomLetter
        minionLabel.value = minionText



# -
app.background = 'paleGreen'

# chatbox
Oval(240, 150, 200, 150, fill='white')
Oval(215, 175, 220, 145, fill='paleGreen')
Oval(200, 85, 300, 80, fill='white')

# face and mouth
Rect(120, 200, 155, 300, fill='gold')
Circle(198, 210, 78, fill='gold')
Oval(200, 270, 50, 30)
Oval(200, 260, 50, 30, fill='gold')

# glasses and eyes
Rect(120, 200, 155, 20)
Circle(165, 210, 30, fill='snow', border='dimGray', borderWidth=8)
Circle(235, 210, 30, fill='snow', border='dimGray', borderWidth=8)
Circle(165, 210, 13, border='saddleBrown', borderWidth=5)
Circle(235, 210, 13, border='saddleBrown', borderWidth=5)
Circle(160, 205, 3, fill='white')
Circle(230, 205, 3, fill='white')

# arms and hands
Line(125, 300, 105, 325, fill='gold', lineWidth=8)
Line(106, 320, 110, 370, fill='gold', lineWidth=8)
Line(270, 285, 290, 325, fill='gold', lineWidth=8)
Line(290, 325, 290, 370, fill='gold', lineWidth=8)
Line(110, 360, 120, 370, lineWidth=8)
Line(290, 360, 280, 370, lineWidth=8)
Oval(110, 370, 15, 25)
Oval(290, 370, 15, 25)

# trousers
Line(120, 300, 160, 320, fill='steelBlue', lineWidth=10)
Line(275, 290, 240, 320, fill='steelBlue', lineWidth=10)
Rect(155, 315, 90, 80, fill='steelBlue')
Rect(120, 385, 155, 30, fill='steelBlue')
Rect(185, 340, 30, 20, fill='steelBlue', border='black', borderWidth=3,
     dashes=True)

Label('Press space to enter text to translate', 200, 20, size=15)
minionLabel = Label('', 200, 85, size=20, bold=True)

def onKeyPress(key):
    if (key == 'space'):
        # Gets the text to translate and creates the minion's alphabet.
        text = app.getTextInput('Minion, please translate this sentence for me:')
        minionAlphabet = text + '~!#? &@'
        minionText = ''

        # Add letters to minionText until it is the same length as minionAlphabet.
        while (len(minionText) < len(minionAlphabet)):
            # In the loop, get a random letter from the minion's alphabet.
            randomIndex = randrange(0, len(minionAlphabet))
            randomLetter = minionAlphabet[randomIndex]
            # Starting with the first letter, every other letter in minionText
            # should be uppercase. If the random letter picked should be
            # uppercase, make it uppercase then add it to minionText!
            if (len(minionText) % 2 == 0):
                randomLetter = randomLetter.upper()
            minionText += randomLetter
        minionLabel.value = minionText

app.setTextInputs("I love CS~")
onKeyPress('space')


# -
app.background = 'paleGreen'

# chatbox
Oval(240, 150, 200, 150, fill='white')
Oval(215, 175, 220, 145, fill='paleGreen')
Oval(200, 85, 300, 80, fill='white')

# face and mouth
Rect(120, 200, 155, 300, fill='gold')
Circle(198, 210, 78, fill='gold')
Oval(200, 270, 50, 30)
Oval(200, 260, 50, 30, fill='gold')

# glasses and eyes
Rect(120, 200, 155, 20)
Circle(165, 210, 30, fill='snow', border='dimGray', borderWidth=8)
Circle(235, 210, 30, fill='snow', border='dimGray', borderWidth=8)
Circle(165, 210, 13, border='saddleBrown', borderWidth=5)
Circle(235, 210, 13, border='saddleBrown', borderWidth=5)
Circle(160, 205, 3, fill='white')
Circle(230, 205, 3, fill='white')

# arms and hands
Line(125, 300, 105, 325, fill='gold', lineWidth=8)
Line(106, 320, 110, 370, fill='gold', lineWidth=8)
Line(270, 285, 290, 325, fill='gold', lineWidth=8)
Line(290, 325, 290, 370, fill='gold', lineWidth=8)
Line(110, 360, 120, 370, lineWidth=8)
Line(290, 360, 280, 370, lineWidth=8)
Oval(110, 370, 15, 25)
Oval(290, 370, 15, 25)

# trousers
Line(120, 300, 160, 320, fill='steelBlue', lineWidth=10)
Line(275, 290, 240, 320, fill='steelBlue', lineWidth=10)
Rect(155, 315, 90, 80, fill='steelBlue')
Rect(120, 385, 155, 30, fill='steelBlue')
Rect(185, 340, 30, 20, fill='steelBlue', border='black', borderWidth=3,
     dashes=True)

Label('Press space to enter text to translate', 200, 20, size=15)
minionLabel = Label('', 200, 85, size=20, bold=True)

def onKeyPress(key):
    if (key == 'space'):
        # Gets the text to translate and creates the minion's alphabet.
        text = app.getTextInput('Minion, please translate this sentence for me:')
        minionAlphabet = text + '~!#? &@'
        minionText = ''

        # Add letters to minionText until it is the same length as minionAlphabet.
        while (len(minionText) < len(minionAlphabet)):
            # In the loop, get a random letter from the minion's alphabet.
            randomIndex = randrange(0, len(minionAlphabet))
            randomLetter = minionAlphabet[randomIndex]
            # Starting with the first letter, every other letter in minionText
            # should be uppercase. If the random letter picked should be
            # uppercase, make it uppercase then add it to minionText!
            if (len(minionText) % 2 == 0):
                randomLetter = randomLetter.upper()
            minionText += randomLetter
        minionLabel.value = minionText

app.setTextInputs("Happy birthday!")
onKeyPress('space')

