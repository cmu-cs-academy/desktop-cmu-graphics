app.synonyms = [ [ 'like', 'love' ],
                 [ 'code.', 'program.' ],
                 [ 'very', 'super' ],
                 [ 'fun.', 'cool.' ],
                 [ 'happy.', 'excited.' ],
                 [ 'great.', 'awesome.' ],
                 [ 'program', 'code' ] ]

# paper
Line(60, 0, 60, 400, fill=rgb(240, 205, 205))
Line(200, 50, 200, 350, fill='dimGray', lineWidth=400, dashes=(2, 57))

essay = Group()

def drawSentence():
    newX = 120
    newY = 40
    sentence = [ 'I', 'like', 'to', 'code.', 'It', 'is', 'very', 'fun.', 'When',
                 'I', 'program', 'I', 'feel', 'very', 'happy.', 'Python', 'is',
                 'great.' ]

    # Draws each word in the sentence and add it to the sentenceGroup.
    for i in range(len(sentence)):
        essay.add(
            Label(sentence[i], newX, newY, size=30, align='bottom')
            )

        # Gets the starting location of the next word.
        if (i != len(sentence) - 1):
            newX += 15 * (len(sentence[i]) + len(sentence[i + 1])) // 2 + 40
        else:
            newX += 15 * len(sentence[i]) + 50

        # Wraparound.
        if (newX >= 340):
            newY += 60
            newX = 120

drawSentence()

def onMousePress(mouseX, mouseY):
    # Check if we clicked on a word in the essay.
    wordLabel = essay.hitTest(mouseX, mouseY)
    if (wordLabel != None):
        # Check if the word has a synonym. If so, change its value and fill.
        for i in range(len(app.synonyms)):
            if (app.synonyms[i][0] == wordLabel.value):
                wordLabel.value = app.synonyms[i][1]
                wordLabel.fill = 'dodgerBlue'
            elif (app.synonyms[i][1] == wordLabel.value):
                wordLabel.value = app.synonyms[i][0]
                wordLabel.fill = 'dodgerBlue'

onMousePress(200, 30)
onMousePress(120, 90)
onMousePress(120, 150)
onMousePress(200, 150)
onMousePress(220, 210)
onMousePress(220, 270)
onMousePress(340, 270)
onMousePress(340, 330)


# -
app.synonyms = [ [ 'like', 'love' ],
                 [ 'code.', 'program.' ],
                 [ 'very', 'super' ],
                 [ 'fun.', 'cool.' ],
                 [ 'happy.', 'excited.' ],
                 [ 'great.', 'awesome.' ],
                 [ 'program', 'code' ] ]

# paper
Line(60, 0, 60, 400, fill=rgb(240, 205, 205))
Line(200, 50, 200, 350, fill='dimGray', lineWidth=400, dashes=(2, 57))

essay = Group()

def drawSentence():
    newX = 120
    newY = 40
    sentence = [ 'I', 'like', 'to', 'code.', 'It', 'is', 'very', 'fun.', 'When',
                 'I', 'program', 'I', 'feel', 'very', 'happy.', 'Python', 'is',
                 'great.' ]

    # Draws each word in the sentence and add it to the sentenceGroup.
    for i in range(len(sentence)):
        essay.add(
            Label(sentence[i], newX, newY, size=30, align='bottom')
            )

        # Gets the starting location of the next word.
        if (i != len(sentence) - 1):
            newX += 15 * (len(sentence[i]) + len(sentence[i + 1])) // 2 + 40
        else:
            newX += 15 * len(sentence[i]) + 50

        # Wraparound.
        if (newX >= 340):
            newY += 60
            newX = 120

drawSentence()

def onMousePress(mouseX, mouseY):
    # Check if we clicked on a word in the essay.
    wordLabel = essay.hitTest(mouseX, mouseY)
    if (wordLabel != None):
        # Check if the word has a synonym. If so, change its value and fill.
        for i in range(len(app.synonyms)):
            if (app.synonyms[i][0] == wordLabel.value):
                wordLabel.value = app.synonyms[i][1]
                wordLabel.fill = 'dodgerBlue'
            elif (app.synonyms[i][1] == wordLabel.value):
                wordLabel.value = app.synonyms[i][0]
                wordLabel.fill = 'dodgerBlue'

onMousePress(120, 90)
onMousePress(200, 150)


# -
app.synonyms = [ [ 'like', 'love' ],
                 [ 'code.', 'program.' ],
                 [ 'very', 'super' ],
                 [ 'fun.', 'cool.' ],
                 [ 'happy.', 'excited.' ],
                 [ 'great.', 'awesome.' ],
                 [ 'program', 'code' ] ]

# paper
Line(60, 0, 60, 400, fill=rgb(240, 205, 205))
Line(200, 50, 200, 350, fill='dimGray', lineWidth=400, dashes=(2, 57))

essay = Group()

def drawSentence():
    newX = 120
    newY = 40
    sentence = [ 'I', 'like', 'to', 'code.', 'It', 'is', 'very', 'fun.', 'When',
                 'I', 'program', 'I', 'feel', 'very', 'happy.', 'Python', 'is',
                 'great.' ]

    # Draws each word in the sentence and add it to the sentenceGroup.
    for i in range(len(sentence)):
        essay.add(
            Label(sentence[i], newX, newY, size=30, align='bottom')
            )

        # Gets the starting location of the next word.
        if (i != len(sentence) - 1):
            newX += 15 * (len(sentence[i]) + len(sentence[i + 1])) // 2 + 40
        else:
            newX += 15 * len(sentence[i]) + 50

        # Wraparound.
        if (newX >= 340):
            newY += 60
            newX = 120

drawSentence()

def onMousePress(mouseX, mouseY):
    # Check if we clicked on a word in the essay.
    wordLabel = essay.hitTest(mouseX, mouseY)
    if (wordLabel != None):
        # Check if the word has a synonym. If so, change its value and fill.
        for i in range(len(app.synonyms)):
            if (app.synonyms[i][0] == wordLabel.value):
                wordLabel.value = app.synonyms[i][1]
                wordLabel.fill = 'dodgerBlue'
            elif (app.synonyms[i][1] == wordLabel.value):
                wordLabel.value = app.synonyms[i][0]
                wordLabel.fill = 'dodgerBlue'

onMousePress(200, 30)
onMousePress(200, 30)

