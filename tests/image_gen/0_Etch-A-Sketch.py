# This Creative Task is inspired by the toy, Etch-A-Sketch.
# Arrow keys are used to draw the lines in the 'sand' as the Etch-A-Sketch
# knobs would.

Label('Etch-a-Sketch', 200, 30, fill='beige', size=30, bold=True)
Label('Use the arrow keys to draw!', 200, 360, fill='beige', size=15)
Label('Use the space key to clear the screen!', 200, 60, fill='beige', size=15,
      align='right')

app.background = 'red'

Circle(45, 360, 25, fill='white')
Circle(355, 360, 25, fill='white')

Circle(30, 85, 10, fill='darkGrey')
Circle(370, 85, 10, fill='darkGrey')
Circle(30, 305, 10, fill='darkGrey')
Circle(370, 305, 10, fill='darkGrey')
Line(30, 85, 370, 85, fill='darkGrey', lineWidth=20)
Line(30, 85, 30, 305, fill='darkGrey', lineWidth=20)
Line(370, 85, 370, 305, fill='darkGrey', lineWidth=20)
Line(30, 305, 370, 305, fill='darkGrey', lineWidth=20)

screen = Rect(30, 85, 340, 220, fill='darkGrey')
cursor = Star(200, 200, 5, 4, opacity=50)

def onKeyPress(key):
    cursor.newX = cursor.centerX
    cursor.newY = cursor.centerY

    if (key == 'up'):
        cursor.newY -= 15
    elif (key == 'down'):
        cursor.newY += 15
    elif (key == 'left'):
        cursor.newX -= 15
    elif (key == 'right'):
        cursor.newX += 15
    elif (key == 'space'):
        screen.toFront()
        cursor.toFront()

    if (screen.contains(cursor.newX, cursor.newY) == True):
        Line(cursor.centerX, cursor.centerY, cursor.newX, cursor.newY)
        cursor.centerX = cursor.newX
        cursor.centerY = cursor.newY


