Rect(0, 0, 400, 400, fill=gradient('steelBlue', 'lightSteelBlue', start='top'))

leftThrow = Label('Rock', 100, 275, size=25)
rightThrow = Label('Rock', 300, 275, size=25)
leftInstructions = Label('Use s, d, f key to control left', 200, 375, size=14)
rightInstructions = Label('Use j, k, l key to control right', 200, 390, size=14)

def drawFinger(x1, y1, x2, y2):
    Line(x1, y1, x2, y2, fill='gold', lineWidth=20)
    Circle(x1, y1, 10, fill='gold')

def drawLeftHand():
    Circle(100, 200, 50, fill='gold')
    if (leftThrow.value != 'Rock'):
        drawFinger(85, 90, 85, 200)
        drawFinger(60, 100, 60, 200)
    if (leftThrow.value == 'Paper'):
        drawFinger(110, 90, 110, 200)
        drawFinger(135, 100, 135, 200)
        drawFinger(160, 170, 125, 230)
    leftThrow.toFront()

def drawRightHand():
    Circle(300, 200, 50, fill='gold')
    if (rightThrow.value != 'Rock'):
        drawFinger(285, 90, 285, 200)
        drawFinger(260, 100, 260, 200)
    if (rightThrow.value == 'Paper'):
        drawFinger(310, 90, 310, 200)
        drawFinger(335, 100, 335, 200)
        drawFinger(360, 170, 325, 230)
    rightThrow.toFront()

def drawWinner(leftMove, rightMove):
    # Check leftMove and rightMove and draw == , > , < accordingly.
    if (leftMove == rightMove):
        Label('==', 200, 200, size=60)
    elif (((leftMove == 'Rock') and (rightMove == 'Scissors')) or
          ((leftMove == 'Paper') and (rightMove == 'Rock')) or
          ((leftMove == 'Scissors') and (rightMove == 'Paper'))):
        Label('>', 200, 200, size=60)
    else:
        Label('<', 200, 200, size=60)

def throwdown():
    # Draw over the old hand and redraw the hands.
    Rect(0, 0, 400, 400, fill=gradient('steelBlue', 'lightSteelBlue', start='top'))
    drawLeftHand()
    drawRightHand()
    drawWinner(leftThrow.value, rightThrow.value)

    leftInstructions.toFront()
    rightInstructions.toFront()

def onKeyPress(key):
    if (key == 's'):
        leftThrow.value = 'Rock'
    elif (key == 'd'):
        leftThrow.value = 'Paper'
    elif (key == 'f'):
        leftThrow.value = 'Scissors'
    elif (key == 'l'):
        rightThrow.value = 'Rock'
    elif (key == 'k'):
        rightThrow.value = 'Paper'
    elif (key == 'j'):
        rightThrow.value = 'Scissors'
    throwdown()

drawLeftHand()
drawRightHand()

onKeyPress('f')
onKeyPress('d')
onKeyPress('s')
onKeyPress('l')
onKeyPress('d')
onKeyPress('j')
onKeyPress('k')
onKeyPress('s')


# -
Rect(0, 0, 400, 400, fill=gradient('steelBlue', 'lightSteelBlue', start='top'))

leftThrow = Label('Rock', 100, 275, size=25)
rightThrow = Label('Rock', 300, 275, size=25)
leftInstructions = Label('Use s, d, f key to control left', 200, 375, size=14)
rightInstructions = Label('Use j, k, l key to control right', 200, 390, size=14)

def drawFinger(x1, y1, x2, y2):
    Line(x1, y1, x2, y2, fill='gold', lineWidth=20)
    Circle(x1, y1, 10, fill='gold')

def drawLeftHand():
    Circle(100, 200, 50, fill='gold')
    if (leftThrow.value != 'Rock'):
        drawFinger(85, 90, 85, 200)
        drawFinger(60, 100, 60, 200)
    if (leftThrow.value == 'Paper'):
        drawFinger(110, 90, 110, 200)
        drawFinger(135, 100, 135, 200)
        drawFinger(160, 170, 125, 230)
    leftThrow.toFront()

def drawRightHand():
    Circle(300, 200, 50, fill='gold')
    if (rightThrow.value != 'Rock'):
        drawFinger(285, 90, 285, 200)
        drawFinger(260, 100, 260, 200)
    if (rightThrow.value == 'Paper'):
        drawFinger(310, 90, 310, 200)
        drawFinger(335, 100, 335, 200)
        drawFinger(360, 170, 325, 230)
    rightThrow.toFront()

def drawWinner(leftMove, rightMove):
    # Check leftMove and rightMove and draw == , > , < accordingly.
    if (leftMove == rightMove):
        Label('==', 200, 200, size=60)
    elif (((leftMove == 'Rock') and (rightMove == 'Scissors')) or
          ((leftMove == 'Paper') and (rightMove == 'Rock')) or
          ((leftMove == 'Scissors') and (rightMove == 'Paper'))):
        Label('>', 200, 200, size=60)
    else:
        Label('<', 200, 200, size=60)

def throwdown():
    # Draw over the old hand and redraw the hands.
    Rect(0, 0, 400, 400, fill=gradient('steelBlue', 'lightSteelBlue', start='top'))
    drawLeftHand()
    drawRightHand()
    drawWinner(leftThrow.value, rightThrow.value)

    leftInstructions.toFront()
    rightInstructions.toFront()

def onKeyPress(key):
    if (key == 's'):
        leftThrow.value = 'Rock'
    elif (key == 'd'):
        leftThrow.value = 'Paper'
    elif (key == 'f'):
        leftThrow.value = 'Scissors'
    elif (key == 'l'):
        rightThrow.value = 'Rock'
    elif (key == 'k'):
        rightThrow.value = 'Paper'
    elif (key == 'j'):
        rightThrow.value = 'Scissors'
    throwdown()

drawLeftHand()
drawRightHand()

onKeyPress('s')
onKeyPress('j')


# -
Rect(0, 0, 400, 400, fill=gradient('steelBlue', 'lightSteelBlue', start='top'))

leftThrow = Label('Rock', 100, 275, size=25)
rightThrow = Label('Rock', 300, 275, size=25)
leftInstructions = Label('Use s, d, f key to control left', 200, 375, size=14)
rightInstructions = Label('Use j, k, l key to control right', 200, 390, size=14)

def drawFinger(x1, y1, x2, y2):
    Line(x1, y1, x2, y2, fill='gold', lineWidth=20)
    Circle(x1, y1, 10, fill='gold')

def drawLeftHand():
    Circle(100, 200, 50, fill='gold')
    if (leftThrow.value != 'Rock'):
        drawFinger(85, 90, 85, 200)
        drawFinger(60, 100, 60, 200)
    if (leftThrow.value == 'Paper'):
        drawFinger(110, 90, 110, 200)
        drawFinger(135, 100, 135, 200)
        drawFinger(160, 170, 125, 230)
    leftThrow.toFront()

def drawRightHand():
    Circle(300, 200, 50, fill='gold')
    if (rightThrow.value != 'Rock'):
        drawFinger(285, 90, 285, 200)
        drawFinger(260, 100, 260, 200)
    if (rightThrow.value == 'Paper'):
        drawFinger(310, 90, 310, 200)
        drawFinger(335, 100, 335, 200)
        drawFinger(360, 170, 325, 230)
    rightThrow.toFront()

def drawWinner(leftMove, rightMove):
    # Check leftMove and rightMove and draw == , > , < accordingly.
    if (leftMove == rightMove):
        Label('==', 200, 200, size=60)
    elif (((leftMove == 'Rock') and (rightMove == 'Scissors')) or
          ((leftMove == 'Paper') and (rightMove == 'Rock')) or
          ((leftMove == 'Scissors') and (rightMove == 'Paper'))):
        Label('>', 200, 200, size=60)
    else:
        Label('<', 200, 200, size=60)

def throwdown():
    # Draw over the old hand and redraw the hands.
    Rect(0, 0, 400, 400, fill=gradient('steelBlue', 'lightSteelBlue', start='top'))
    drawLeftHand()
    drawRightHand()
    drawWinner(leftThrow.value, rightThrow.value)

    leftInstructions.toFront()
    rightInstructions.toFront()

def onKeyPress(key):
    if (key == 's'):
        leftThrow.value = 'Rock'
    elif (key == 'd'):
        leftThrow.value = 'Paper'
    elif (key == 'f'):
        leftThrow.value = 'Scissors'
    elif (key == 'l'):
        rightThrow.value = 'Rock'
    elif (key == 'k'):
        rightThrow.value = 'Paper'
    elif (key == 'j'):
        rightThrow.value = 'Scissors'
    throwdown()

drawLeftHand()
drawRightHand()


