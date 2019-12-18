app.background = 'black'

# header
Rect(0, 370, 400, 30, fill='white', opacity=70)
Label('File', 60, 385, size=18)
Label('Edit', 120, 385, size=18)
Label('View', 180, 385, size=18)
Label('History', 255, 385, size=18)
Label('Help', 330, 385, size=18)

# Math folder
Polygon(50, 40, 85, 40, 90, 50, 50, 50,
        fill=gradient('skyBlue', 'lightBlue', start='top'))
Rect(50, 50, 100, 70, fill=gradient('skyBlue', 'lightSkyBlue', start='top'))
Label('Math', 100, 140, fill='white', size=16)

# Science folder
Polygon(230, 40, 265, 40, 270, 50, 230, 50,
        fill=gradient('skyBlue', 'lightBlue', start='top'))
Rect(230, 50, 100, 70, fill=gradient('skyBlue', 'lightSkyBlue', start='top'))
Label('Science', 280, 140, fill='white', size=16)

# essay
Rect(60, 200, 80, 100, fill=gradient('gainsboro', 'white', start='top'))
Label('Essay', 100, 320, fill='white', size=16)

selected = Rect(0, 0, 200, 170, fill='white', border='white', opacity=30)

def onMouseDrag(mouseX, mouseY):
    # Drag the selected rectangle's right-bottom corner with the mouse.
    ### (HINT: Add 1 to the mouse values since the width and height of a Rect
    #          can never be 0!)
    selected.width = mouseX + 1
    selected.height = mouseY + 1

onMouseDrag(0, 120)
onMouseDrag(0, 300)
onMouseDrag(0, 0)


# -
app.background = 'black'

# header
Rect(0, 370, 400, 30, fill='white', opacity=70)
Label('File', 60, 385, size=18)
Label('Edit', 120, 385, size=18)
Label('View', 180, 385, size=18)
Label('History', 255, 385, size=18)
Label('Help', 330, 385, size=18)

# Math folder
Polygon(50, 40, 85, 40, 90, 50, 50, 50,
        fill=gradient('skyBlue', 'lightBlue', start='top'))
Rect(50, 50, 100, 70, fill=gradient('skyBlue', 'lightSkyBlue', start='top'))
Label('Math', 100, 140, fill='white', size=16)

# Science folder
Polygon(230, 40, 265, 40, 270, 50, 230, 50,
        fill=gradient('skyBlue', 'lightBlue', start='top'))
Rect(230, 50, 100, 70, fill=gradient('skyBlue', 'lightSkyBlue', start='top'))
Label('Science', 280, 140, fill='white', size=16)

# essay
Rect(60, 200, 80, 100, fill=gradient('gainsboro', 'white', start='top'))
Label('Essay', 100, 320, fill='white', size=16)

selected = Rect(0, 0, 200, 170, fill='white', border='white', opacity=30)

def onMouseDrag(mouseX, mouseY):
    # Drag the selected rectangle's right-bottom corner with the mouse.
    ### (HINT: Add 1 to the mouse values since the width and height of a Rect
    #          can never be 0!)
    selected.width = mouseX + 1
    selected.height = mouseY + 1

onMouseDrag(150, 270)
onMouseDrag(330, 50)


# -
app.background = 'black'

# header
Rect(0, 370, 400, 30, fill='white', opacity=70)
Label('File', 60, 385, size=18)
Label('Edit', 120, 385, size=18)
Label('View', 180, 385, size=18)
Label('History', 255, 385, size=18)
Label('Help', 330, 385, size=18)

# Math folder
Polygon(50, 40, 85, 40, 90, 50, 50, 50,
        fill=gradient('skyBlue', 'lightBlue', start='top'))
Rect(50, 50, 100, 70, fill=gradient('skyBlue', 'lightSkyBlue', start='top'))
Label('Math', 100, 140, fill='white', size=16)

# Science folder
Polygon(230, 40, 265, 40, 270, 50, 230, 50,
        fill=gradient('skyBlue', 'lightBlue', start='top'))
Rect(230, 50, 100, 70, fill=gradient('skyBlue', 'lightSkyBlue', start='top'))
Label('Science', 280, 140, fill='white', size=16)

# essay
Rect(60, 200, 80, 100, fill=gradient('gainsboro', 'white', start='top'))
Label('Essay', 100, 320, fill='white', size=16)

selected = Rect(0, 0, 200, 170, fill='white', border='white', opacity=30)

def onMouseDrag(mouseX, mouseY):
    # Drag the selected rectangle's right-bottom corner with the mouse.
    ### (HINT: Add 1 to the mouse values since the width and height of a Rect
    #          can never be 0!)
    selected.width = mouseX + 1
    selected.height = mouseY + 1

onMouseDrag(280, 300)

