app.background = 'seaGreen'

# eyes
Oval(110, 120, 70, 120, fill='white')
Oval(290, 120, 70, 120, fill='white')
Oval(110, 120, 50, 80, fill=gradient('skyBlue', 'skyBlue', 'blue'))
Oval(290, 120, 50, 80, fill=gradient('skyBlue', 'skyBlue', 'blue'))
Oval(110, 120, 30, 50)
Oval(290, 120, 30, 50)

mouth = Oval(200, 320, 40, 5, fill='pink', border='black', borderWidth=4)

def expandHorizontal():
    mouth.left -= 2
    mouth.width += 2
    mouth.centerX = 200

def expandVertical():
    mouth.top -= 2
    mouth.height += 2
    mouth.centerY = 320

def onKeyHold(keys):
    # Expand based on the keys held.
    if (('left' in keys) and ('right' in keys)):
        expandHorizontal()
    if (('up' in keys) and ('down' in keys)):
        expandVertical()

onKeyHolds(['left'], 20)


# -
app.background = 'seaGreen'

# eyes
Oval(110, 120, 70, 120, fill='white')
Oval(290, 120, 70, 120, fill='white')
Oval(110, 120, 50, 80, fill=gradient('skyBlue', 'skyBlue', 'blue'))
Oval(290, 120, 50, 80, fill=gradient('skyBlue', 'skyBlue', 'blue'))
Oval(110, 120, 30, 50)
Oval(290, 120, 30, 50)

mouth = Oval(200, 320, 40, 5, fill='pink', border='black', borderWidth=4)

def expandHorizontal():
    mouth.left -= 2
    mouth.width += 2
    mouth.centerX = 200

def expandVertical():
    mouth.top -= 2
    mouth.height += 2
    mouth.centerY = 320

def onKeyHold(keys):
    # Expand based on the keys held.
    if (('left' in keys) and ('right' in keys)):
        expandHorizontal()
    if (('up' in keys) and ('down' in keys)):
        expandVertical()

onKeyHolds(['left', 'right'], 100)


# -
app.background = 'seaGreen'

# eyes
Oval(110, 120, 70, 120, fill='white')
Oval(290, 120, 70, 120, fill='white')
Oval(110, 120, 50, 80, fill=gradient('skyBlue', 'skyBlue', 'blue'))
Oval(290, 120, 50, 80, fill=gradient('skyBlue', 'skyBlue', 'blue'))
Oval(110, 120, 30, 50)
Oval(290, 120, 30, 50)

mouth = Oval(200, 320, 40, 5, fill='pink', border='black', borderWidth=4)

def expandHorizontal():
    mouth.left -= 2
    mouth.width += 2
    mouth.centerX = 200

def expandVertical():
    mouth.top -= 2
    mouth.height += 2
    mouth.centerY = 320

def onKeyHold(keys):
    # Expand based on the keys held.
    if (('left' in keys) and ('right' in keys)):
        expandHorizontal()
    if (('up' in keys) and ('down' in keys)):
        expandVertical()

onKeyHolds(['left', 'right'], 100)

