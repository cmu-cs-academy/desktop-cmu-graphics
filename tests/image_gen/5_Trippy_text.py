app.background ='ivory'

cursor = Label('', 30, 30)

def drawFancyLabel(key, x, y):
    # Draws one trippy letter at position (x, y).
    Label(key, x, y, fill='cyan', size=50, opacity=80)
    Label(key, x + 5, y - 5, fill='yellow', size=50, opacity=80)
    Label(key, x - 5, y + 5, fill='magenta', size=50, opacity=80)

def moveToNextLine():
    cursor.centerY += 60
    cursor.centerX = 30

def onKeyPress(key):
    # When space is pressed, move the cursor. When enter is pressed, move
    # to the next line. When backspace is pressed, cover up the previous
    # letter on that line. If none of these keys were pressed, draw a
    # fancy label for the key pressed.
    if (key == 'space'):
        cursor.centerX += 30
    elif (key == 'enter'):
        moveToNextLine()
    elif (key == 'backspace'):
        cursor.centerX -= 30
        Rect(cursor.centerX - 20, cursor.centerY - 30, 40, 80, fill='ivory')
    else:
        drawFancyLabel(key, cursor.centerX, cursor.centerY)
        cursor.centerX += 30
    # If the new centerX is greater than 370, move to next line.
    if (cursor.centerX >= 370):
        moveToNextLine()

onKeyPress('a')


# -
app.background ='ivory'

cursor = Label('', 30, 30)

def drawFancyLabel(key, x, y):
    # Draws one trippy letter at position (x, y).
    Label(key, x, y, fill='cyan', size=50, opacity=80)
    Label(key, x + 5, y - 5, fill='yellow', size=50, opacity=80)
    Label(key, x - 5, y + 5, fill='magenta', size=50, opacity=80)

def moveToNextLine():
    cursor.centerY += 60
    cursor.centerX = 30

def onKeyPress(key):
    # When space is pressed, move the cursor. When enter is pressed, move
    # to the next line. When backspace is pressed, cover up the previous
    # letter on that line. If none of these keys were pressed, draw a
    # fancy label for the key pressed.
    if (key == 'space'):
        cursor.centerX += 30
    elif (key == 'enter'):
        moveToNextLine()
    elif (key == 'backspace'):
        cursor.centerX -= 30
        Rect(cursor.centerX - 20, cursor.centerY - 30, 40, 80, fill='ivory')
    else:
        drawFancyLabel(key, cursor.centerX, cursor.centerY)
        cursor.centerX += 30
    # If the new centerX is greater than 370, move to next line.
    if (cursor.centerX >= 370):
        moveToNextLine()

onKeyPress('I')
onKeyPress('space')
onKeyPress('c')
onKeyPress('a')
onKeyPress('n')
onKeyPress('o')
onKeyPress('backspace')
onKeyPress('n')
onKeyPress('o')
onKeyPress('t')
onKeyPress('space')
onKeyPress('t')
onKeyPress('i')
onKeyPress('backspace')
onKeyPress('y')
onKeyPress('p')
onKeyPress('e')


# -
app.background ='ivory'

cursor = Label('', 30, 30)

def drawFancyLabel(key, x, y):
    # Draws one trippy letter at position (x, y).
    Label(key, x, y, fill='cyan', size=50, opacity=80)
    Label(key, x + 5, y - 5, fill='yellow', size=50, opacity=80)
    Label(key, x - 5, y + 5, fill='magenta', size=50, opacity=80)

def moveToNextLine():
    cursor.centerY += 60
    cursor.centerX = 30

def onKeyPress(key):
    # When space is pressed, move the cursor. When enter is pressed, move
    # to the next line. When backspace is pressed, cover up the previous
    # letter on that line. If none of these keys were pressed, draw a
    # fancy label for the key pressed.
    if (key == 'space'):
        cursor.centerX += 30
    elif (key == 'enter'):
        moveToNextLine()
    elif (key == 'backspace'):
        cursor.centerX -= 30
        Rect(cursor.centerX - 20, cursor.centerY - 30, 40, 80, fill='ivory')
    else:
        drawFancyLabel(key, cursor.centerX, cursor.centerY)
        cursor.centerX += 30
    # If the new centerX is greater than 370, move to next line.
    if (cursor.centerX >= 370):
        moveToNextLine()

onKeyPress('I')
onKeyPress('space')
onKeyPress('c')
onKeyPress('a')
onKeyPress('n')
onKeyPress('o')
onKeyPress('backspace')
onKeyPress('n')
onKeyPress('o')
onKeyPress('t')
onKeyPress('space')
onKeyPress('t')
onKeyPress('i')
onKeyPress('backspace')
onKeyPress('y')
onKeyPress('p')
onKeyPress('e')

