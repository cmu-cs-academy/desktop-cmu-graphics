def drawRect(row, col):
    # Picks the color based on the col.
    if (col % 2 == 0):
        color = 'white'
    else:
        color = 'black'

    # Set startX to create the optical illusion. Even rows start
    # at -10 while odd rows start at -20.
    if (row % 2 == 0):
        startX = -10
    else:
        startX = -20
    Rect(startX + 40 * col, 40 * row, 40, 40, fill=color, border='gray',
         borderWidth=1)

def drawIllusion():
    # Draw rectangles over the entire canvas.
    for row in range(10):
        for col in range(10):
            drawRect(row, col)
drawIllusion()


