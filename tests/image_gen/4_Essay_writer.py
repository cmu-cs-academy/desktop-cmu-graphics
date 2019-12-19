app.background = gradient('midnightBlue', 'royalBlue', start='top')

Rect(50, 10, 300, 380, fill=gradient('whiteSmoke', 'white', start='top'))
essay = Line(200, 20, 200, 30, lineWidth=250, dashes=True)

pageNumber = Label(1, 335, 375, size=20)

def onKeyPress(key):
    # On any key press, the essay should get longer.
    # If you reach the end of the page, go to a new page.
    essay.y2 += 10
    if (essay.y2 > 380):
        essay.y2 = 30
        pageNumber.value += 1

onKeyPresses('G', 10)
onKeyPresses('space', 20)
onKeyPresses('9', 5)
onKeyPress('d')


# -
app.background = gradient('midnightBlue', 'royalBlue', start='top')

Rect(50, 10, 300, 380, fill=gradient('whiteSmoke', 'white', start='top'))
essay = Line(200, 20, 200, 30, lineWidth=250, dashes=True)

pageNumber = Label(1, 335, 375, size=20)

def onKeyPress(key):
    # On any key press, the essay should get longer.
    # If you reach the end of the page, go to a new page.
    essay.y2 += 10
    if (essay.y2 > 380):
        essay.y2 = 30
        pageNumber.value += 1

onKeyPress('a')
onKeyPress('b')
onKeyPress('C')


# -
app.background = gradient('midnightBlue', 'royalBlue', start='top')

Rect(50, 10, 300, 380, fill=gradient('whiteSmoke', 'white', start='top'))
essay = Line(200, 20, 200, 30, lineWidth=250, dashes=True)

pageNumber = Label(1, 335, 375, size=20)

def onKeyPress(key):
    # On any key press, the essay should get longer.
    # If you reach the end of the page, go to a new page.
    essay.y2 += 10
    if (essay.y2 > 380):
        essay.y2 = 30
        pageNumber.value += 1

onKeyPress('a')
onKeyPress('b')
onKeyPress('c')
onKeyPress('backspace')
onKeyPress('backspace')
onKeyPress('a')

