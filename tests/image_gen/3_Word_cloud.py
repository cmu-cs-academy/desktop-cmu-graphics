app.background = rgb(205, 210, 215)

seenWords = Group()

def countWord(paragraph, targetWord):
    # Counts the number of times the targetWord appears in the paragraph.
    count = 0
    for word in paragraph:
        # If the word is the target word, adds one to count.
        if (word == targetWord):
            count += 1

    # Return count.
    return count
def drawWordCloud(text):
    colors = [ 'indigo', 'navy', 'royalBlue', 'dodgerBlue', 'mediumSlateBlue' ]

    # Loops over each word in the paragraph.
    for word in text:
        # The size should be 10 + 2 times the word count and the color is random.
        # The angle is one of 0, 90, or 270 and the position should be between
        # 50 and 350 (inclusive).
        size = 10 + 2 * countWord(text, word)
        color = choice(colors)
        angle = choice([ 0, 90, 270 ])
        x = randrange(50, 351)
        y = randrange(50, 351)
        # Draws the word with the properties generated above.
        label = Label(word, x, y, fill=color, size=size, rotateAngle=angle,
                      bold=True)

        # Tries to reposition the word so it doesn't hit any other words.
        attempts = 0
        while ((label.hitsShape(seenWords) == True) and (attempts <= 500)):
            x = randrange(50, 351)
            y = randrange(50, 351)
            label.centerX = x
            label.centerY = y

            attempts += 1

        seenWords.add(label)

drawWordCloud([
    'in', 'the', 'town', 'where', 'I', 'was', 'born', 'lived', 'a', 'man',
    'who', 'sailed', 'to', 'sea', 'and', 'he', 'told', 'us', 'of', 'his',
    'life', 'in', 'the', 'land', 'of', 'submarines', 'so', 'we', 'sailed',
    'up', 'to', 'the', 'sun', 'till', 'we', 'found', 'a', 'sea', 'of',
    'green', 'and', 'we', 'lived', 'beneath', 'the', 'waves', 'in', 'our',
    'yellow', 'submarine', 'we', 'all', 'live', 'in', 'a', 'yellow',
    'submarine', 'yellow', 'submarine', 'yellow', 'submarine', 'we', 'all',
    'live', 'in', 'a', 'yellow', 'submarine', 'yellow', 'submarine',
    'yellow', 'submarine'
    ])


# -
app.background = rgb(205, 210, 215)

seenWords = Group()

def countWord(paragraph, targetWord):
    # Counts the number of times the targetWord appears in the paragraph.
    count = 0
    for word in paragraph:
        # If the word is the target word, adds one to count.
        if (word == targetWord):
            count += 1

    # Return count.
    return count
def drawWordCloud(text):
    colors = [ 'indigo', 'navy', 'royalBlue', 'dodgerBlue', 'mediumSlateBlue' ]

    # Loops over each word in the paragraph.
    for word in text:
        # The size should be 10 + 2 times the word count and the color is random.
        # The angle is one of 0, 90, or 270 and the position should be between
        # 50 and 350 (inclusive).
        size = 10 + 2 * countWord(text, word)
        color = choice(colors)
        angle = choice([ 0, 90, 270 ])
        x = randrange(50, 351)
        y = randrange(50, 351)
        # Draws the word with the properties generated above.
        label = Label(word, x, y, fill=color, size=size, rotateAngle=angle,
                      bold=True)

        # Tries to reposition the word so it doesn't hit any other words.
        attempts = 0
        while ((label.hitsShape(seenWords) == True) and (attempts <= 500)):
            x = randrange(50, 351)
            y = randrange(50, 351)
            label.centerX = x
            label.centerY = y

            attempts += 1

        seenWords.add(label)

drawWordCloud([
    'CS', 'Academy', 'computer', 'science', 'CS', 'bugs', 'debug',
    'for loop', 'CS', 'computer', 'program', 'code', 'Python', 'functions',
    'Python', 'animation', 'conditional', 'if', 'else', 'functions',
    'Academy', 'CS', 'Academy', 'Python', 'code', 'Rect', 'Label', 'if',
    'if', 'else', 'functions', 'bugs', 'CS', 'conditional', 'loops',
    'strings', 'ints', 'lists', 'locals', 'globals', 'variables', 'shape',
    'strings', 'strings', 'lists', 'CS', 'Academy', 'bugs', 'code', 'conditional',
    'loops', 'loops', 'lists', 'Python', 'Rect', 'if', 'if', 'strings'
    ])


# -
app.background = rgb(205, 210, 215)

seenWords = Group()

def countWord(paragraph, targetWord):
    # Counts the number of times the targetWord appears in the paragraph.
    count = 0
    for word in paragraph:
        # If the word is the target word, adds one to count.
        if (word == targetWord):
            count += 1

    # Return count.
    return count
def drawWordCloud(text):
    colors = [ 'indigo', 'navy', 'royalBlue', 'dodgerBlue', 'mediumSlateBlue' ]

    # Loops over each word in the paragraph.
    for word in text:
        # The size should be 10 + 2 times the word count and the color is random.
        # The angle is one of 0, 90, or 270 and the position should be between
        # 50 and 350 (inclusive).
        size = 10 + 2 * countWord(text, word)
        color = choice(colors)
        angle = choice([ 0, 90, 270 ])
        x = randrange(50, 351)
        y = randrange(50, 351)
        # Draws the word with the properties generated above.
        label = Label(word, x, y, fill=color, size=size, rotateAngle=angle,
                      bold=True)

        # Tries to reposition the word so it doesn't hit any other words.
        attempts = 0
        while ((label.hitsShape(seenWords) == True) and (attempts <= 500)):
            x = randrange(50, 351)
            y = randrange(50, 351)
            label.centerX = x
            label.centerY = y

            attempts += 1

        seenWords.add(label)

drawWordCloud([
    'CS', 'Academy', 'computer', 'science', 'CS', 'bugs', 'debug',
    'for loop', 'CS', 'computer', 'program', 'code', 'Python', 'functions',
    'Python', 'animation', 'conditional', 'if', 'else', 'functions',
    'Academy', 'CS', 'Academy', 'Python', 'code', 'Rect', 'Label', 'if',
    'if', 'else', 'functions', 'bugs', 'CS', 'conditional', 'loops',
    'strings', 'ints', 'lists', 'locals', 'globals', 'variables', 'shape',
    'strings', 'strings', 'lists', 'CS', 'Academy', 'bugs', 'code', 'conditional',
    'loops', 'loops', 'lists', 'Python', 'Rect', 'if', 'if', 'strings'
    ])

