app.background = gradient('lightSkyBlue', 'lightCyan', start='top')

# flower and tree
Rect(375, 200, 25, 200, fill=gradient('peru', 'saddleBrown', start='left'))
Circle(325, 200, 50, fill=gradient('mediumSeaGreen', 'green', 'green',
                                   start='left'))
Circle(400, 200, 50, fill='green')
Circle(350, 150, 50, fill=gradient('mediumSeaGreen', 'green', 'green',
                                   start='left-top'))
Circle(375, 100, 50, fill=gradient('mediumSeaGreen', 'green', 'green',
                                   start='left-top'))
Circle(400, 50, 50, fill=gradient('mediumSeaGreen', 'green', 'green',
                                  start='left-top'))

stickyHoney = Line(200, 275, 200, 200, lineWidth=40,
                   fill=gradient('chocolate', 'goldenrod', 'goldenrod',
                                 start='bottom'))
dipperStick = Line(200, 200, 400, 100,
                   fill=gradient('sienna', 'burlyWood', start='top'), lineWidth=20)
dipperTop = Line(200, 200, 240, 180,
                 fill=gradient('goldenrod', 'maroon', start='bottom'),
                 lineWidth=40, dashes=True)

Polygon(125, 265, 140, 275, 125, 300, 125, 375, 140, 400, 260, 400, 275, 375,
        275, 300, 260, 275, 275, 265,
        fill=gradient('chocolate', 'goldenrod', start='left'), border='goldenrod')

Rect(200, 340, 100, 50, fill='goldenrod', align='center')
Label('HONEY', 200, 340, fill='white', size=25, italic=True)

def onMousePress(mouseX, mouseY):
    # This changes the lineWidth and position of the honey.
    stickyHoney.y2 = mouseY
    stickyHoney.lineWidth = mouseY / 5 + 1

    # Change the y1 and y2 values of the dipperStick to move to the
    # location of click.
    dipperStick.y1 = mouseY
    dipperStick.y2 = mouseY - 100
    # Change the y1 and y2 values of dipperTop.
    dipperTop.y1 = mouseY
    dipperTop.y2 = mouseY - 20



# -
app.background = gradient('lightSkyBlue', 'lightCyan', start='top')

# flower and tree
Rect(375, 200, 25, 200, fill=gradient('peru', 'saddleBrown', start='left'))
Circle(325, 200, 50, fill=gradient('mediumSeaGreen', 'green', 'green',
                                   start='left'))
Circle(400, 200, 50, fill='green')
Circle(350, 150, 50, fill=gradient('mediumSeaGreen', 'green', 'green',
                                   start='left-top'))
Circle(375, 100, 50, fill=gradient('mediumSeaGreen', 'green', 'green',
                                   start='left-top'))
Circle(400, 50, 50, fill=gradient('mediumSeaGreen', 'green', 'green',
                                  start='left-top'))

stickyHoney = Line(200, 275, 200, 200, lineWidth=40,
                   fill=gradient('chocolate', 'goldenrod', 'goldenrod',
                                 start='bottom'))
dipperStick = Line(200, 200, 400, 100,
                   fill=gradient('sienna', 'burlyWood', start='top'), lineWidth=20)
dipperTop = Line(200, 200, 240, 180,
                 fill=gradient('goldenrod', 'maroon', start='bottom'),
                 lineWidth=40, dashes=True)

Polygon(125, 265, 140, 275, 125, 300, 125, 375, 140, 400, 260, 400, 275, 375,
        275, 300, 260, 275, 275, 265,
        fill=gradient('chocolate', 'goldenrod', start='left'), border='goldenrod')

Rect(200, 340, 100, 50, fill='goldenrod', align='center')
Label('HONEY', 200, 340, fill='white', size=25, italic=True)

def onMousePress(mouseX, mouseY):
    # This changes the lineWidth and position of the honey.
    stickyHoney.y2 = mouseY
    stickyHoney.lineWidth = mouseY / 5 + 1

    # Change the y1 and y2 values of the dipperStick to move to the
    # location of click.
    dipperStick.y1 = mouseY
    dipperStick.y2 = mouseY - 100
    # Change the y1 and y2 values of dipperTop.
    dipperTop.y1 = mouseY
    dipperTop.y2 = mouseY - 20



# -
app.background = gradient('lightSkyBlue', 'lightCyan', start='top')

# flower and tree
Rect(375, 200, 25, 200, fill=gradient('peru', 'saddleBrown', start='left'))
Circle(325, 200, 50, fill=gradient('mediumSeaGreen', 'green', 'green',
                                   start='left'))
Circle(400, 200, 50, fill='green')
Circle(350, 150, 50, fill=gradient('mediumSeaGreen', 'green', 'green',
                                   start='left-top'))
Circle(375, 100, 50, fill=gradient('mediumSeaGreen', 'green', 'green',
                                   start='left-top'))
Circle(400, 50, 50, fill=gradient('mediumSeaGreen', 'green', 'green',
                                  start='left-top'))

stickyHoney = Line(200, 275, 200, 200, lineWidth=40,
                   fill=gradient('chocolate', 'goldenrod', 'goldenrod',
                                 start='bottom'))
dipperStick = Line(200, 200, 400, 100,
                   fill=gradient('sienna', 'burlyWood', start='top'), lineWidth=20)
dipperTop = Line(200, 200, 240, 180,
                 fill=gradient('goldenrod', 'maroon', start='bottom'),
                 lineWidth=40, dashes=True)

Polygon(125, 265, 140, 275, 125, 300, 125, 375, 140, 400, 260, 400, 275, 375,
        275, 300, 260, 275, 275, 265,
        fill=gradient('chocolate', 'goldenrod', start='left'), border='goldenrod')

Rect(200, 340, 100, 50, fill='goldenrod', align='center')
Label('HONEY', 200, 340, fill='white', size=25, italic=True)

def onMousePress(mouseX, mouseY):
    # This changes the lineWidth and position of the honey.
    stickyHoney.y2 = mouseY
    stickyHoney.lineWidth = mouseY / 5 + 1

    # Change the y1 and y2 values of the dipperStick to move to the
    # location of click.
    dipperStick.y1 = mouseY
    dipperStick.y2 = mouseY - 100
    # Change the y1 and y2 values of dipperTop.
    dipperTop.y1 = mouseY
    dipperTop.y2 = mouseY - 20

onMousePress(300, 20)

