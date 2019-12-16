app.background = gradient('mediumPurple', 'darkSlateBlue', start='top')

# Initializes all the sentences.
app.sentences = [ 'a is for apple', 'b is for banana', 'c is for cherry',
                  'd is for dragon fruit', 'e is for elderberry', 'f is for fig',
                  'g is for grapes', 'h is for honeydew melon', 'i is for imbe',
                  'j is for jackfruit', 'k is for kiwi', 'l is for lime',
                  'm is for mango', 'n is for nectarine', 'o is for orange',
                  'p is for papaya', 'q is for quince', 'r is for raspberries',
                  's is for strawberries', 't is for tomato', 'u is for ugli fruit',
                  'v is for vanilla bean', 'w is for watermelon', 'x is for xigua',
                  'y is for yucca root', 'z is for zuchinni' ]

letters = Group()

def getFirstLetter():
    # Loop over all the sentences and get the first letter of each sentence.
    for sentence in app.sentences:
        letter = sentence[0]
        letters.add(
            Label(letter, randrange(30, 371), randrange(30, 371),
                  fill='lightCyan', size=30)
            )
getFirstLetter()
sentenceBox = Group()

def drawSentenceBox(letter):
    # Draws the box containing the 'is for' sentence.
    for line in app.sentences:
        if (line[0] == letter.value):
            centerX = letter.centerX
            centerY = letter.centerY - 30
            label = Label(line, centerX, centerY, fill='white', size=15)
            sentenceBox.add(
                Rect(centerX, centerY, label.width + 10, 20, opacity=40,
                     align='center'),
                RegularPolygon(centerX, centerY + 12, 5, 3, rotateAngle=180,
                               opacity=40),
                label
                )

def onMouseMove(mouseX, mouseY):
    sentenceBox.clear()

    # Checks if the mouse is hovering over a letter and draws a sentence if so.
    for letter in letters.children:
        if (letter.contains(mouseX, mouseY) == True):
            drawSentenceBox(letter)

letters.add(Label('d', 300, 150))
onMouseMove(300, 150)
app.paused


# -
app.background = gradient('mediumPurple', 'darkSlateBlue', start='top')

# Initializes all the sentences.
app.sentences = [ 'a is for apple', 'b is for banana', 'c is for cherry',
                  'd is for dragon fruit', 'e is for elderberry', 'f is for fig',
                  'g is for grapes', 'h is for honeydew melon', 'i is for imbe',
                  'j is for jackfruit', 'k is for kiwi', 'l is for lime',
                  'm is for mango', 'n is for nectarine', 'o is for orange',
                  'p is for papaya', 'q is for quince', 'r is for raspberries',
                  's is for strawberries', 't is for tomato', 'u is for ugli fruit',
                  'v is for vanilla bean', 'w is for watermelon', 'x is for xigua',
                  'y is for yucca root', 'z is for zuchinni' ]

letters = Group()

def getFirstLetter():
    # Loop over all the sentences and get the first letter of each sentence.
    for sentence in app.sentences:
        letter = sentence[0]
        letters.add(
            Label(letter, randrange(30, 371), randrange(30, 371),
                  fill='lightCyan', size=30)
            )
getFirstLetter()
sentenceBox = Group()

def drawSentenceBox(letter):
    # Draws the box containing the 'is for' sentence.
    for line in app.sentences:
        if (line[0] == letter.value):
            centerX = letter.centerX
            centerY = letter.centerY - 30
            label = Label(line, centerX, centerY, fill='white', size=15)
            sentenceBox.add(
                Rect(centerX, centerY, label.width + 10, 20, opacity=40,
                     align='center'),
                RegularPolygon(centerX, centerY + 12, 5, 3, rotateAngle=180,
                               opacity=40),
                label
                )

def onMouseMove(mouseX, mouseY):
    sentenceBox.clear()

    # Checks if the mouse is hovering over a letter and draws a sentence if so.
    for letter in letters.children:
        if (letter.contains(mouseX, mouseY) == True):
            drawSentenceBox(letter)

letters.add(Label('a', 200, 200))
onMouseMove(200, 200)
app.paused = True


# -
app.background = gradient('mediumPurple', 'darkSlateBlue', start='top')

# Initializes all the sentences.
app.sentences = [ 'a is for apple', 'b is for banana', 'c is for cherry',
                  'd is for dragon fruit', 'e is for elderberry', 'f is for fig',
                  'g is for grapes', 'h is for honeydew melon', 'i is for imbe',
                  'j is for jackfruit', 'k is for kiwi', 'l is for lime',
                  'm is for mango', 'n is for nectarine', 'o is for orange',
                  'p is for papaya', 'q is for quince', 'r is for raspberries',
                  's is for strawberries', 't is for tomato', 'u is for ugli fruit',
                  'v is for vanilla bean', 'w is for watermelon', 'x is for xigua',
                  'y is for yucca root', 'z is for zuchinni' ]

letters = Group()

def getFirstLetter():
    # Loop over all the sentences and get the first letter of each sentence.
    for sentence in app.sentences:
        letter = sentence[0]
        letters.add(
            Label(letter, randrange(30, 371), randrange(30, 371),
                  fill='lightCyan', size=30)
            )
getFirstLetter()
sentenceBox = Group()

def drawSentenceBox(letter):
    # Draws the box containing the 'is for' sentence.
    for line in app.sentences:
        if (line[0] == letter.value):
            centerX = letter.centerX
            centerY = letter.centerY - 30
            label = Label(line, centerX, centerY, fill='white', size=15)
            sentenceBox.add(
                Rect(centerX, centerY, label.width + 10, 20, opacity=40,
                     align='center'),
                RegularPolygon(centerX, centerY + 12, 5, 3, rotateAngle=180,
                               opacity=40),
                label
                )

def onMouseMove(mouseX, mouseY):
    sentenceBox.clear()

    # Checks if the mouse is hovering over a letter and draws a sentence if so.
    for letter in letters.children:
        if (letter.contains(mouseX, mouseY) == True):
            drawSentenceBox(letter)

shape = letters.children[0]
onMouseMove(shape.centerX, shape.centerY)
app.paused = True

