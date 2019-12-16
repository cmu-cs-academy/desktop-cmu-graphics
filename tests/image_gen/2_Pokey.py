# Write the function drawPokeyBodyPiece(x, y), which takes an x,y point
# which is the center of the body piece, to draw the Pokey from Super Mario!

def drawBackground():
    Rect(0, 0, 400, 400, fill=gradient('skyBlue', 'orange', start='top'))
    Rect(0, 275, 400, 125, fill='gold')
    Polygon(140, 275, 240, 155, 290, 175, 330, 120, 465, 275,
            fill=rgb(235, 185, 0))
    Polygon(0, 275, 60, 185, 100, 240, 135, 220, 190, 275,
            fill=rgb(255, 235, 60))

def drawPokeyHead(x, y):
    # head spikes
    Star(x, y - 10, 32, 6, fill=rgb(255, 235, 60), border='white')

    # head and eyes
    Circle(x, y, 30, fill=gradient('gold', 'orange', start='left-top'),
           border='black')
    Oval(x - 10, y - 5, 15, 18)
    Oval(x + 10, y - 5, 15, 18)
    Circle(x - 7, y - 7, 3, fill='white')
    Circle(x + 7, y - 2, 3, fill='white')

    # mouth
    Oval(x, y + 15, 30, 15)
    Oval(x, y + 10, 30, 10, fill=gradient('gold', 'orange', start='left-top'))

def drawPokeyBodyPiece(x, y):
    # Draw the thorns with 2 lines.
    Line(x - 25, y + 25, x + 25, y - 25)
    Line(x - 25, y - 25, x + 25, y + 25)
    # Draw the spikes with 2 regularPolygons.
    RegularPolygon(x - 25, y - 5, 12, 4, fill=rgb(255, 235, 60), border='white')
    RegularPolygon(x + 28, y + 5, 12, 3, fill=rgb(255, 235, 60), border='white')
    # Draw the body.
    Circle(x, y, 30, fill=gradient('gold', 'orange', start='left-top'),
           border='black')

drawBackground()
drawPokeyBodyPiece(100, 320)
drawPokeyHead(100, 255)
drawPokeyBodyPiece(200, 320)
drawPokeyBodyPiece(200, 255)
drawPokeyHead(200, 190)
drawPokeyBodyPiece(300, 320)
drawPokeyBodyPiece(300, 255)
drawPokeyBodyPiece(300, 190)
drawPokeyHead(300, 125)


# -
# Write the function drawPokeyBodyPiece(x, y), which takes an x,y point
# which is the center of the body piece, to draw the Pokey from Super Mario!

def drawBackground():
    Rect(0, 0, 400, 400, fill=gradient('skyBlue', 'orange', start='top'))
    Rect(0, 275, 400, 125, fill='gold')
    Polygon(140, 275, 240, 155, 290, 175, 330, 120, 465, 275,
            fill=rgb(235, 185, 0))
    Polygon(0, 275, 60, 185, 100, 240, 135, 220, 190, 275,
            fill=rgb(255, 235, 60))

def drawPokeyHead(x, y):
    # head spikes
    Star(x, y - 10, 32, 6, fill=rgb(255, 235, 60), border='white')

    # head and eyes
    Circle(x, y, 30, fill=gradient('gold', 'orange', start='left-top'),
           border='black')
    Oval(x - 10, y - 5, 15, 18)
    Oval(x + 10, y - 5, 15, 18)
    Circle(x - 7, y - 7, 3, fill='white')
    Circle(x + 7, y - 2, 3, fill='white')

    # mouth
    Oval(x, y + 15, 30, 15)
    Oval(x, y + 10, 30, 10, fill=gradient('gold', 'orange', start='left-top'))

def drawPokeyBodyPiece(x, y):
    # Draw the thorns with 2 lines.
    Line(x - 25, y + 25, x + 25, y - 25)
    Line(x - 25, y - 25, x + 25, y + 25)
    # Draw the spikes with 2 regularPolygons.
    RegularPolygon(x - 25, y - 5, 12, 4, fill=rgb(255, 235, 60), border='white')
    RegularPolygon(x + 28, y + 5, 12, 3, fill=rgb(255, 235, 60), border='white')
    # Draw the body.
    Circle(x, y, 30, fill=gradient('gold', 'orange', start='left-top'),
           border='black')

drawBackground()
drawPokeyBodyPiece(100, 320)
drawPokeyHead(100, 255)
drawPokeyBodyPiece(200, 320)
drawPokeyBodyPiece(200, 255)
drawPokeyHead(200, 190)
drawPokeyBodyPiece(300, 320)
drawPokeyBodyPiece(300, 255)
drawPokeyBodyPiece(300, 190)
drawPokeyHead(300, 125)


# -
# Write the function drawPokeyBodyPiece(x, y), which takes an x,y point
# which is the center of the body piece, to draw the Pokey from Super Mario!

def drawBackground():
    Rect(0, 0, 400, 400, fill=gradient('skyBlue', 'orange', start='top'))
    Rect(0, 275, 400, 125, fill='gold')
    Polygon(140, 275, 240, 155, 290, 175, 330, 120, 465, 275,
            fill=rgb(235, 185, 0))
    Polygon(0, 275, 60, 185, 100, 240, 135, 220, 190, 275,
            fill=rgb(255, 235, 60))

def drawPokeyHead(x, y):
    # head spikes
    Star(x, y - 10, 32, 6, fill=rgb(255, 235, 60), border='white')

    # head and eyes
    Circle(x, y, 30, fill=gradient('gold', 'orange', start='left-top'),
           border='black')
    Oval(x - 10, y - 5, 15, 18)
    Oval(x + 10, y - 5, 15, 18)
    Circle(x - 7, y - 7, 3, fill='white')
    Circle(x + 7, y - 2, 3, fill='white')

    # mouth
    Oval(x, y + 15, 30, 15)
    Oval(x, y + 10, 30, 10, fill=gradient('gold', 'orange', start='left-top'))

def drawPokeyBodyPiece(x, y):
    # Draw the thorns with 2 lines.
    Line(x - 25, y + 25, x + 25, y - 25)
    Line(x - 25, y - 25, x + 25, y + 25)
    # Draw the spikes with 2 regularPolygons.
    RegularPolygon(x - 25, y - 5, 12, 4, fill=rgb(255, 235, 60), border='white')
    RegularPolygon(x + 28, y + 5, 12, 3, fill=rgb(255, 235, 60), border='white')
    # Draw the body.
    Circle(x, y, 30, fill=gradient('gold', 'orange', start='left-top'),
           border='black')

drawBackground()
drawPokeyBodyPiece(200, 320)
drawPokeyHead(200, 255)

