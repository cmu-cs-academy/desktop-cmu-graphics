app.background = 'azure'

head = Circle(200, 200, 30, fill='mediumOrchid')

def getNewHeadColor():
    # Cycle through the three colors.
    if (head.fill == 'mediumOrchid'):
        head.fill = 'mediumSpringGreen'
    elif (head.fill == 'mediumSpringGreen'):
        head.fill = 'blue'
    else:
        head.fill = 'mediumOrchid'

def onKeyHold(keys):
    # Depending on the keys held down, move the head in an appropriate direction.
    if ('up' in keys):
        head.centerY -= 10
    if ('down' in keys):
        head.centerY += 10
    if ('left' in keys):
        head.centerX -= 10
    if ('right' in keys):
        head.centerX += 10
    # Draw a new circle where the head is with the same fill.
    Circle(head.centerX, head.centerY, 30, fill=head.fill)
    # Change the color of the head.
    getNewHeadColor()

onKeyHold(['left'])


# -
app.background = 'azure'

head = Circle(200, 200, 30, fill='mediumOrchid')

def getNewHeadColor():
    # Cycle through the three colors.
    if (head.fill == 'mediumOrchid'):
        head.fill = 'mediumSpringGreen'
    elif (head.fill == 'mediumSpringGreen'):
        head.fill = 'blue'
    else:
        head.fill = 'mediumOrchid'

def onKeyHold(keys):
    # Depending on the keys held down, move the head in an appropriate direction.
    if ('up' in keys):
        head.centerY -= 10
    if ('down' in keys):
        head.centerY += 10
    if ('left' in keys):
        head.centerX -= 10
    if ('right' in keys):
        head.centerX += 10
    # Draw a new circle where the head is with the same fill.
    Circle(head.centerX, head.centerY, 30, fill=head.fill)
    # Change the color of the head.
    getNewHeadColor()

onKeyHolds(['down'], 2)
onKeyHolds(['right'], 3)
onKeyHolds(['up'], 4)
onKeyHold(['left'])


# -
app.background = 'azure'

head = Circle(200, 200, 30, fill='mediumOrchid')

def getNewHeadColor():
    # Cycle through the three colors.
    if (head.fill == 'mediumOrchid'):
        head.fill = 'mediumSpringGreen'
    elif (head.fill == 'mediumSpringGreen'):
        head.fill = 'blue'
    else:
        head.fill = 'mediumOrchid'

def onKeyHold(keys):
    # Depending on the keys held down, move the head in an appropriate direction.
    if ('up' in keys):
        head.centerY -= 10
    if ('down' in keys):
        head.centerY += 10
    if ('left' in keys):
        head.centerX -= 10
    if ('right' in keys):
        head.centerX += 10
    # Draw a new circle where the head is with the same fill.
    Circle(head.centerX, head.centerY, 30, fill=head.fill)
    # Change the color of the head.
    getNewHeadColor()

onKeyHold(['down'])

