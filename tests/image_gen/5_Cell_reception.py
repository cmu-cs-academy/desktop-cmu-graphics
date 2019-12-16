Rect(0, 0, 400, 400,
     fill=gradient('limeGreen', 'yellow', 'orange', 'red', start='top'),
     opacity=20)

cellPhone = Rect(350, 320, 50, 80, border='dimGrey', borderWidth=3, align='center')
cellPhoneButton = Circle(350, 350, 5, fill='dimGrey')

barLow = Rect(180, 340, 10, 15, fill=None, border='dodgerBlue', align='bottom')
barMid = Rect(200, 340, 10, 30, fill=None, border='dodgerBlue', align='bottom')
barHigh = Rect(220, 340, 10, 45, fill=None, border='dodgerBlue', align='bottom')

def onMouseMove(mouseX, mouseY):
    # Move the cellPhone to the mouse location and cellPhoneButton accordingly.
    cellPhone.centerX = mouseX
    cellPhone.centerY = mouseY
    cellPhoneButton.centerX = mouseX
    cellPhoneButton.centerY = mouseY + 30

    # Based on your mouseY value, fill the reception bars.
    if (mouseY <= 100):
        barLow.fill = 'dodgerBlue'
        barMid.fill = 'dodgerBlue'
        barHigh.fill = 'dodgerBlue'
    elif (mouseY <= 200):
        barLow.fill = 'dodgerBlue'
        barMid.fill = 'dodgerBlue'
        barHigh.fill = None
    elif (mouseY <= 300):
        barLow.fill = 'dodgerBlue'
        barMid.fill = None
        barHigh.fill = None
    else:
        barLow.fill = None
        barMid.fill = None
        barHigh.fill = None

onMouseMove(320, 310)


# -
Rect(0, 0, 400, 400,
     fill=gradient('limeGreen', 'yellow', 'orange', 'red', start='top'),
     opacity=20)

cellPhone = Rect(350, 320, 50, 80, border='dimGrey', borderWidth=3, align='center')
cellPhoneButton = Circle(350, 350, 5, fill='dimGrey')

barLow = Rect(180, 340, 10, 15, fill=None, border='dodgerBlue', align='bottom')
barMid = Rect(200, 340, 10, 30, fill=None, border='dodgerBlue', align='bottom')
barHigh = Rect(220, 340, 10, 45, fill=None, border='dodgerBlue', align='bottom')

def onMouseMove(mouseX, mouseY):
    # Move the cellPhone to the mouse location and cellPhoneButton accordingly.
    cellPhone.centerX = mouseX
    cellPhone.centerY = mouseY
    cellPhoneButton.centerX = mouseX
    cellPhoneButton.centerY = mouseY + 30

    # Based on your mouseY value, fill the reception bars.
    if (mouseY <= 100):
        barLow.fill = 'dodgerBlue'
        barMid.fill = 'dodgerBlue'
        barHigh.fill = 'dodgerBlue'
    elif (mouseY <= 200):
        barLow.fill = 'dodgerBlue'
        barMid.fill = 'dodgerBlue'
        barHigh.fill = None
    elif (mouseY <= 300):
        barLow.fill = 'dodgerBlue'
        barMid.fill = None
        barHigh.fill = None
    else:
        barLow.fill = None
        barMid.fill = None
        barHigh.fill = None

onMouseMove(200, 99)


# -
Rect(0, 0, 400, 400,
     fill=gradient('limeGreen', 'yellow', 'orange', 'red', start='top'),
     opacity=20)

cellPhone = Rect(350, 320, 50, 80, border='dimGrey', borderWidth=3, align='center')
cellPhoneButton = Circle(350, 350, 5, fill='dimGrey')

barLow = Rect(180, 340, 10, 15, fill=None, border='dodgerBlue', align='bottom')
barMid = Rect(200, 340, 10, 30, fill=None, border='dodgerBlue', align='bottom')
barHigh = Rect(220, 340, 10, 45, fill=None, border='dodgerBlue', align='bottom')

def onMouseMove(mouseX, mouseY):
    # Move the cellPhone to the mouse location and cellPhoneButton accordingly.
    cellPhone.centerX = mouseX
    cellPhone.centerY = mouseY
    cellPhoneButton.centerX = mouseX
    cellPhoneButton.centerY = mouseY + 30

    # Based on your mouseY value, fill the reception bars.
    if (mouseY <= 100):
        barLow.fill = 'dodgerBlue'
        barMid.fill = 'dodgerBlue'
        barHigh.fill = 'dodgerBlue'
    elif (mouseY <= 200):
        barLow.fill = 'dodgerBlue'
        barMid.fill = 'dodgerBlue'
        barHigh.fill = None
    elif (mouseY <= 300):
        barLow.fill = 'dodgerBlue'
        barMid.fill = None
        barHigh.fill = None
    else:
        barLow.fill = None
        barMid.fill = None
        barHigh.fill = None

onMouseMove(300, 10)

