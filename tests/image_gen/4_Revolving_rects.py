app.background = 'black'

def drawRect(red, green, blue, index):
    # Draws a rectangle rotated slightly with a dashed border.
    side = 100 + index * 15
    angle = index * 10
    Rect(60, 60, side, side, fill=None, border=rgb(red, green, blue),
         borderWidth=3, rotateAngle=angle, dashes=(6, 2))

def drawChangingRects():
    red = randrange(50, 100)
    green = randrange(50, 100)
    blue = randrange(50, 100)
    index = 0

    # Loop until all of the rgb parts are greater than 200.
    while ((red < 200) or (green < 200) or (blue < 200)):
        # On each pass through the loop, draw a rectangle using the drawRect
        # function and increment the index.
        drawRect(red, green, blue, index)
        index = index + 1
        # On each pass, increase exactly one color by 25. Choose which color to
        # increase by generating a random number (increase red when the number
        # is 0, green when it is 1, and blue when it is 2).
        randomNum = randrange(0, 3)
        if ((red < 200) and (randomNum == 0)):
            red += 25
        if ((green < 200) and (randomNum == 1)):
            green += 25
        if ((blue < 200) and (randomNum == 2)):
            blue += 25
drawChangingRects()


