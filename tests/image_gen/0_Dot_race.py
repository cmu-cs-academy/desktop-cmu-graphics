app.background = 'paleGreen'

track = Rect(200, 200, 360, 360, align='center')
innerGrass = Rect(200, 200, 260, 260, fill='paleGreen', align='center')
Rect(200, 200, 310, 310, fill=None, border='white', dashes=True, align='center')

message = Label('Dot Race!', 200, 200, size=25)

finishLine = Line(320, 200, 390, 200, fill='white', lineWidth=30)
Line(315, 200, 390, 200, fill='red', lineWidth=30, dashes=True)

purpleDot = Circle(45, 175, 15, fill='darkOrchid')
blueDot = Circle(45, 225, 15, fill='dodgerBlue')

def onKeyHold(keys):
    # While the race is still going, move the dots and check if the race ends.
    if (message.value == 'Dot Race!'):
        if ('up' in keys):
            purpleDot.centerY -= 10
        if ('down' in keys):
            purpleDot.centerY += 10
        if ('left' in keys):
            purpleDot.centerX -= 10
        if ('right' in keys):
            purpleDot.centerX += 10
        if ('w' in keys):
            blueDot.centerY -= 10
        if ('s' in keys):
            blueDot.centerY += 10
        if ('a' in keys):
            blueDot.centerX -= 10
        if ('d' in keys):
            blueDot.centerX += 10

        # Check if one of the dots wins and if so change the value of the message.
        # A dot wins if either it touches the finish line or the center of the
        # other dot is not on the track.
        if ((track.contains(purpleDot.centerX, purpleDot.centerY) == False) or
            (innerGrass.contains(purpleDot.centerX, purpleDot.centerY) == True)):
            message.value = 'Blue dot won!'
        elif ((track.contains(blueDot.centerX, blueDot.centerY) == False) or
              (innerGrass.contains(blueDot.centerX, blueDot.centerY) == True)):
            message.value = 'Purple dot won!'
        elif (purpleDot.hitsShape(finishLine) == True):
            message.value = 'Purple dot won!'
        elif (blueDot.hitsShape(finishLine) == True):
            message.value = 'Blue dot won!'

def onKeyPress(key):
    # Do not change this function! It is for testing purposes only!
    if (key == 'q'):
        message.value = 'Dot Race!'
        purpleDot.centerX = 350
        purpleDot.centerY = 165
        blueDot.centerX = 350
        blueDot.centerY = 240

onKeyHold(['w'])


# -
app.background = 'paleGreen'

track = Rect(200, 200, 360, 360, align='center')
innerGrass = Rect(200, 200, 260, 260, fill='paleGreen', align='center')
Rect(200, 200, 310, 310, fill=None, border='white', dashes=True, align='center')

message = Label('Dot Race!', 200, 200, size=25)

finishLine = Line(320, 200, 390, 200, fill='white', lineWidth=30)
Line(315, 200, 390, 200, fill='red', lineWidth=30, dashes=True)

purpleDot = Circle(45, 175, 15, fill='darkOrchid')
blueDot = Circle(45, 225, 15, fill='dodgerBlue')

def onKeyHold(keys):
    # While the race is still going, move the dots and check if the race ends.
    if (message.value == 'Dot Race!'):
        if ('up' in keys):
            purpleDot.centerY -= 10
        if ('down' in keys):
            purpleDot.centerY += 10
        if ('left' in keys):
            purpleDot.centerX -= 10
        if ('right' in keys):
            purpleDot.centerX += 10
        if ('w' in keys):
            blueDot.centerY -= 10
        if ('s' in keys):
            blueDot.centerY += 10
        if ('a' in keys):
            blueDot.centerX -= 10
        if ('d' in keys):
            blueDot.centerX += 10

        # Check if one of the dots wins and if so change the value of the message.
        # A dot wins if either it touches the finish line or the center of the
        # other dot is not on the track.
        if ((track.contains(purpleDot.centerX, purpleDot.centerY) == False) or
            (innerGrass.contains(purpleDot.centerX, purpleDot.centerY) == True)):
            message.value = 'Blue dot won!'
        elif ((track.contains(blueDot.centerX, blueDot.centerY) == False) or
              (innerGrass.contains(blueDot.centerX, blueDot.centerY) == True)):
            message.value = 'Purple dot won!'
        elif (purpleDot.hitsShape(finishLine) == True):
            message.value = 'Purple dot won!'
        elif (blueDot.hitsShape(finishLine) == True):
            message.value = 'Blue dot won!'

def onKeyPress(key):
    # Do not change this function! It is for testing purposes only!
    if (key == 'q'):
        message.value = 'Dot Race!'
        purpleDot.centerX = 350
        purpleDot.centerY = 165
        blueDot.centerX = 350
        blueDot.centerY = 240

onKeyHold(['down'])


# -
app.background = 'paleGreen'

track = Rect(200, 200, 360, 360, align='center')
innerGrass = Rect(200, 200, 260, 260, fill='paleGreen', align='center')
Rect(200, 200, 310, 310, fill=None, border='white', dashes=True, align='center')

message = Label('Dot Race!', 200, 200, size=25)

finishLine = Line(320, 200, 390, 200, fill='white', lineWidth=30)
Line(315, 200, 390, 200, fill='red', lineWidth=30, dashes=True)

purpleDot = Circle(45, 175, 15, fill='darkOrchid')
blueDot = Circle(45, 225, 15, fill='dodgerBlue')

def onKeyHold(keys):
    # While the race is still going, move the dots and check if the race ends.
    if (message.value == 'Dot Race!'):
        if ('up' in keys):
            purpleDot.centerY -= 10
        if ('down' in keys):
            purpleDot.centerY += 10
        if ('left' in keys):
            purpleDot.centerX -= 10
        if ('right' in keys):
            purpleDot.centerX += 10
        if ('w' in keys):
            blueDot.centerY -= 10
        if ('s' in keys):
            blueDot.centerY += 10
        if ('a' in keys):
            blueDot.centerX -= 10
        if ('d' in keys):
            blueDot.centerX += 10

        # Check if one of the dots wins and if so change the value of the message.
        # A dot wins if either it touches the finish line or the center of the
        # other dot is not on the track.
        if ((track.contains(purpleDot.centerX, purpleDot.centerY) == False) or
            (innerGrass.contains(purpleDot.centerX, purpleDot.centerY) == True)):
            message.value = 'Blue dot won!'
        elif ((track.contains(blueDot.centerX, blueDot.centerY) == False) or
              (innerGrass.contains(blueDot.centerX, blueDot.centerY) == True)):
            message.value = 'Purple dot won!'
        elif (purpleDot.hitsShape(finishLine) == True):
            message.value = 'Purple dot won!'
        elif (blueDot.hitsShape(finishLine) == True):
            message.value = 'Blue dot won!'

def onKeyPress(key):
    # Do not change this function! It is for testing purposes only!
    if (key == 'q'):
        message.value = 'Dot Race!'
        purpleDot.centerX = 350
        purpleDot.centerY = 165
        blueDot.centerX = 350
        blueDot.centerY = 240

onKeyHolds(['s'], 20)

