# background
Rect(0, 0, 400, 400, fill=gradient('lightCyan', 'lightBlue'))

# message
Label('Click within the frame to make a pattern!', 200, 20, size=20)

# frame
Circle(170, 200, 140, fill='lightYellow', border='tan', borderWidth=20)

# needle
Line(350, 215, 380, 335, fill='darkGrey')
Circle(345, 205, 15, fill=None, border='darkGrey')

# thread
Polygon(315, 315, 325, 315, 325, 300, 310, 300, fill='tan')
Polygon(310, 315, 310, 390, 360, 375, 335, 310, fill='pink')
Line(340, 345, 345, 205, fill='pink')
Polygon(370, 365, 370, 375, 305, 400, 300, 390, fill='tan')

def onMousePress(mouseX, mouseY):
    # Draw a snowflake where the mouse was clicked.
    Label('X', mouseX, mouseY, fill='lightBlue', size=10)
    Label('X', mouseX - 5, mouseY - 5, fill='lightBlue', size=8)
    Label('X', mouseX + 5, mouseY - 5, fill='lightBlue', size=8)
    Label('X', mouseX - 5, mouseY + 5, fill='lightBlue', size=8)
    Label('X', mouseX + 5, mouseY + 5, fill='lightBlue', size=8)

onMousePress(200, 200)
onMousePress(85, 207)


# -
# background
Rect(0, 0, 400, 400, fill=gradient('lightCyan', 'lightBlue'))

# message
Label('Click within the frame to make a pattern!', 200, 20, size=20)

# frame
Circle(170, 200, 140, fill='lightYellow', border='tan', borderWidth=20)

# needle
Line(350, 215, 380, 335, fill='darkGrey')
Circle(345, 205, 15, fill=None, border='darkGrey')

# thread
Polygon(315, 315, 325, 315, 325, 300, 310, 300, fill='tan')
Polygon(310, 315, 310, 390, 360, 375, 335, 310, fill='pink')
Line(340, 345, 345, 205, fill='pink')
Polygon(370, 365, 370, 375, 305, 400, 300, 390, fill='tan')

def onMousePress(mouseX, mouseY):
    # Draw a snowflake where the mouse was clicked.
    Label('X', mouseX, mouseY, fill='lightBlue', size=10)
    Label('X', mouseX - 5, mouseY - 5, fill='lightBlue', size=8)
    Label('X', mouseX + 5, mouseY - 5, fill='lightBlue', size=8)
    Label('X', mouseX - 5, mouseY + 5, fill='lightBlue', size=8)
    Label('X', mouseX + 5, mouseY + 5, fill='lightBlue', size=8)



# -
# background
Rect(0, 0, 400, 400, fill=gradient('lightCyan', 'lightBlue'))

# message
Label('Click within the frame to make a pattern!', 200, 20, size=20)

# frame
Circle(170, 200, 140, fill='lightYellow', border='tan', borderWidth=20)

# needle
Line(350, 215, 380, 335, fill='darkGrey')
Circle(345, 205, 15, fill=None, border='darkGrey')

# thread
Polygon(315, 315, 325, 315, 325, 300, 310, 300, fill='tan')
Polygon(310, 315, 310, 390, 360, 375, 335, 310, fill='pink')
Line(340, 345, 345, 205, fill='pink')
Polygon(370, 365, 370, 375, 305, 400, 300, 390, fill='tan')

def onMousePress(mouseX, mouseY):
    # Draw a snowflake where the mouse was clicked.
    Label('X', mouseX, mouseY, fill='lightBlue', size=10)
    Label('X', mouseX - 5, mouseY - 5, fill='lightBlue', size=8)
    Label('X', mouseX + 5, mouseY - 5, fill='lightBlue', size=8)
    Label('X', mouseX - 5, mouseY + 5, fill='lightBlue', size=8)
    Label('X', mouseX + 5, mouseY + 5, fill='lightBlue', size=8)


