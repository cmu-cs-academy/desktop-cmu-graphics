# Spongebob's face
app.background = rgb(255, 250, 80)

# eyelashes
Line(75, 135, 100, 180, lineWidth=4)
Line(100, 125, 100, 180, lineWidth=4)
Line(130, 130, 100, 180, lineWidth=4)
Line(265, 130, 290, 180, lineWidth=4)
Line(285, 125, 290, 180, lineWidth=4)
Line(305, 125, 290, 180, lineWidth=4)

# eyes
Circle(110, 180, 40, fill='white', border='black')
Circle(100, 175, 17)
Circle(100, 175, 15, border=rgb(130, 190, 235), borderWidth=7)
Circle(290, 180, 40, fill='white', border='black')
Circle(310, 180, 17)
Circle(310, 180, 15, border=rgb(130, 190, 235), borderWidth=7)

Label('Press space to input a sentence', 200, 30, size=15)

# Defines the labels that keep track of the meme text.
inputLabel = Label('', 200, 60, size=20, bold=True)
memeLabel = Label('', 200, 300, fill='white', border='black', size=35, bold=True)

def memefy():
    memeText = ''
    for index in range(len(inputLabel.value)):
        # If the letter in the input is at an even index, it should be
        # lowercase. Otherwise, make it uppercase.
        letter = inputLabel.value[index]
        if (index % 2 == 0):
            memeText = memeText + letter.lower()
        else:
            memeText = memeText + letter.upper()
    memeLabel.value = memeText

def onKeyPress(key):
    # Gets the text input.
    if (key == 'space'):
        inputLabel.value = app.getTextInput('Memefy a sentence:')
        memefy()



# -
# Spongebob's face
app.background = rgb(255, 250, 80)

# eyelashes
Line(75, 135, 100, 180, lineWidth=4)
Line(100, 125, 100, 180, lineWidth=4)
Line(130, 130, 100, 180, lineWidth=4)
Line(265, 130, 290, 180, lineWidth=4)
Line(285, 125, 290, 180, lineWidth=4)
Line(305, 125, 290, 180, lineWidth=4)

# eyes
Circle(110, 180, 40, fill='white', border='black')
Circle(100, 175, 17)
Circle(100, 175, 15, border=rgb(130, 190, 235), borderWidth=7)
Circle(290, 180, 40, fill='white', border='black')
Circle(310, 180, 17)
Circle(310, 180, 15, border=rgb(130, 190, 235), borderWidth=7)

Label('Press space to input a sentence', 200, 30, size=15)

# Defines the labels that keep track of the meme text.
inputLabel = Label('', 200, 60, size=20, bold=True)
memeLabel = Label('', 200, 300, fill='white', border='black', size=35, bold=True)

def memefy():
    memeText = ''
    for index in range(len(inputLabel.value)):
        # If the letter in the input is at an even index, it should be
        # lowercase. Otherwise, make it uppercase.
        letter = inputLabel.value[index]
        if (index % 2 == 0):
            memeText = memeText + letter.lower()
        else:
            memeText = memeText + letter.upper()
    memeLabel.value = memeText

def onKeyPress(key):
    # Gets the text input.
    if (key == 'space'):
        inputLabel.value = app.getTextInput('Memefy a sentence:')
        memefy()



# -
# Spongebob's face
app.background = rgb(255, 250, 80)

# eyelashes
Line(75, 135, 100, 180, lineWidth=4)
Line(100, 125, 100, 180, lineWidth=4)
Line(130, 130, 100, 180, lineWidth=4)
Line(265, 130, 290, 180, lineWidth=4)
Line(285, 125, 290, 180, lineWidth=4)
Line(305, 125, 290, 180, lineWidth=4)

# eyes
Circle(110, 180, 40, fill='white', border='black')
Circle(100, 175, 17)
Circle(100, 175, 15, border=rgb(130, 190, 235), borderWidth=7)
Circle(290, 180, 40, fill='white', border='black')
Circle(310, 180, 17)
Circle(310, 180, 15, border=rgb(130, 190, 235), borderWidth=7)

Label('Press space to input a sentence', 200, 30, size=15)

# Defines the labels that keep track of the meme text.
inputLabel = Label('', 200, 60, size=20, bold=True)
memeLabel = Label('', 200, 300, fill='white', border='black', size=35, bold=True)

def memefy():
    memeText = ''
    for index in range(len(inputLabel.value)):
        # If the letter in the input is at an even index, it should be
        # lowercase. Otherwise, make it uppercase.
        letter = inputLabel.value[index]
        if (index % 2 == 0):
            memeText = memeText + letter.lower()
        else:
            memeText = memeText + letter.upper()
    memeLabel.value = memeText

def onKeyPress(key):
    # Gets the text input.
    if (key == 'space'):
        inputLabel.value = app.getTextInput('Memefy a sentence:')
        memefy()

app.setTextInputs('A SpongeBob Meme!')
onKeyPress('space')

