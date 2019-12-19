# background
Rect(0, 0, 400, 200, fill='cornSilk')
Rect(0, 200, 400, 200, fill='steelBlue')
Circle(200, 200, 55, fill='white', border='black', borderWidth=1, dashes=True)
Label('reversed is', 200, 200, size=20)

def drawSentence(L, centerX, centerY, isReversed):
    # Constructs a sentence using the words in L.
    sentence = ''
    for word in L:
        sentence += word

        # Adds spaces in-between the words in our sentence.
        sentence += ' '

    color = 'aquaMarine'
    if (isReversed == False):
        color = 'salmon'

    Label(sentence, centerX, centerY, fill=color, size=33)

def reverseSentence(wordList):
    # Draws the normal sentence.
    drawSentence(wordList, 200, 100, False)

    reversedList = [ ]

    # Loop through the list of words and pop each word.
    # Then add it to reversedList, building up the list in reverse order!
    for num in range(len(wordList)):
        word = wordList.pop()
        reversedList.append(word)
    # Draws the reversed sentence.
    drawSentence(reversedList, 200, 300, True)



# -
# background
Rect(0, 0, 400, 200, fill='cornSilk')
Rect(0, 200, 400, 200, fill='steelBlue')
Circle(200, 200, 55, fill='white', border='black', borderWidth=1, dashes=True)
Label('reversed is', 200, 200, size=20)

def drawSentence(L, centerX, centerY, isReversed):
    # Constructs a sentence using the words in L.
    sentence = ''
    for word in L:
        sentence += word

        # Adds spaces in-between the words in our sentence.
        sentence += ' '

    color = 'aquaMarine'
    if (isReversed == False):
        color = 'salmon'

    Label(sentence, centerX, centerY, fill=color, size=33)

def reverseSentence(wordList):
    # Draws the normal sentence.
    drawSentence(wordList, 200, 100, False)

    reversedList = [ ]

    # Loop through the list of words and pop each word.
    # Then add it to reversedList, building up the list in reverse order!
    for num in range(len(wordList)):
        word = wordList.pop()
        reversedList.append(word)
    # Draws the reversed sentence.
    drawSentence(reversedList, 200, 300, True)



# -
# background
Rect(0, 0, 400, 200, fill='cornSilk')
Rect(0, 200, 400, 200, fill='steelBlue')
Circle(200, 200, 55, fill='white', border='black', borderWidth=1, dashes=True)
Label('reversed is', 200, 200, size=20)

def drawSentence(L, centerX, centerY, isReversed):
    # Constructs a sentence using the words in L.
    sentence = ''
    for word in L:
        sentence += word

        # Adds spaces in-between the words in our sentence.
        sentence += ' '

    color = 'aquaMarine'
    if (isReversed == False):
        color = 'salmon'

    Label(sentence, centerX, centerY, fill=color, size=33)

def reverseSentence(wordList):
    # Draws the normal sentence.
    drawSentence(wordList, 200, 100, False)

    reversedList = [ ]

    # Loop through the list of words and pop each word.
    # Then add it to reversedList, building up the list in reverse order!
    for num in range(len(wordList)):
        word = wordList.pop()
        reversedList.append(word)
    # Draws the reversed sentence.
    drawSentence(reversedList, 200, 300, True)

reverseSentence([ 'fall', 'leaves', 'after', 'leaves', 'fall' ])

