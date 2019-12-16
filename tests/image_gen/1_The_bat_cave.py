# roof layers
Circle(200, 275, 340,
       fill=gradient(rgb(30, 15, 10), rgb(60, 20, 10), start='top'))
Polygon(0, 35, 20, 30, 40, 10, 70, 0, 330, 0, 365, 25, 400, 30, 400, 70, 0, 70,
        fill=gradient('black', rgb(30, 15, 10), rgb(60, 20, 10), start='top'))
Polygon(0, 70, 70, 30, 115, 20, 165, 0, 255, 0, 315, 15, 370, 60, 400, 70,
        400, 120, 0, 120, fill=gradient('black', rgb(30, 15, 10), rgb(60, 20, 10),
                                        start='top'))
Polygon(0, 110, 33, 73, 95, 45, 155, 25, 240, 20, 340, 55, 365, 85, 400, 100,
        400, 140, 0, 140, fill=gradient('black', rgb(30, 15, 10), rgb(60, 20, 10),
                                        start='top'))

caveBackground = Circle(200, 275, 240, fill=gradient('black', rgb(60, 20, 10)))
caveRoof = Polygon(-20, 140, 58, 75, 140, 38, 200, 30, 275, 45, 320, 65,
                   420, 140, 290, 170, 260, 180, 230, 165, 190, 195, 80, 170,
                   45, 150, fill=gradient('black', rgb(30, 15, 10), start='top'))

# cave floor
Polygon(0, 400, 0, 370, 40, 350, 70, 315, 140, 295, 240, 285, 260, 320, 350, 340,
        400, 380, 400, 400, fill=gradient('black', rgb(80, 30, 15), start='top'))

def drawBat(x, y):
    # body
    Polygon(x, y - 16, x + 6, y, x, y + 7, x - 6, y)

    # ears
    Label('X', x, y + 7, size=20)

    # eyes
    Circle(x - 3, y + 9, 1, fill='red')
    Circle(x + 3, y + 9, 1, fill='red')

# bats
drawBat(75, 175)
drawBat(95, 180)
drawBat(110, 185)
drawBat(160, 190)
drawBat(205, 185)
drawBat(220, 175)
drawBat(280, 175)

# stalagmites
Polygon(100, 325, 105, 310, 110, 290, 115, 270, 120, 265, 125, 270, 120, 290,
        135, 325, fill=gradient(rgb(40, 15, 10), rgb(30, 20, 10),
                                rgb(20, 10, 10), start='top'))
Polygon(250, 360, 260, 345, 260, 325, 255, 305, 260, 302, 270, 305, 275, 335,
        285, 360, fill=gradient(rgb(45, 25, 10), rgb(40, 20, 10),
                                rgb(30, 20, 10), start='top'))

# flashlight
Rect(40, 330, 100, 20, fill='forestGreen')
Polygon(40, 350, 140, 350, 120, 380, 60, 380, fill='green')
Oval(90, 350, 100, 10, fill='forestGreen')
Rect(60, 380, 60, 20, fill='forestGreen')
Oval(90, 380, 60, 6, fill='green')
light = Oval(90, 330, 100, 10, border='forestGreen')

def onMousePress(mouseX, mouseY):
    # Turn the flashlight on and make the cave brighter.
    caveBackground.fill = gradient(rgb(30, 15, 10), 'saddleBrown')
    caveRoof.fill = gradient(rgb(30, 15, 10), rgb(60, 20, 10), start='top')
    light.fill = 'gold'
def onMouseRelease(mouseX, mouseY):
    # Turn the flashlight off and make the cave darker.
    caveBackground.fill = gradient('black', rgb(60, 20, 10))
    caveRoof.fill = gradient('black', rgb(30, 15, 10), start='top')
    light.fill = 'black'

onMousePress(200, 200)


# -
# roof layers
Circle(200, 275, 340,
       fill=gradient(rgb(30, 15, 10), rgb(60, 20, 10), start='top'))
Polygon(0, 35, 20, 30, 40, 10, 70, 0, 330, 0, 365, 25, 400, 30, 400, 70, 0, 70,
        fill=gradient('black', rgb(30, 15, 10), rgb(60, 20, 10), start='top'))
Polygon(0, 70, 70, 30, 115, 20, 165, 0, 255, 0, 315, 15, 370, 60, 400, 70,
        400, 120, 0, 120, fill=gradient('black', rgb(30, 15, 10), rgb(60, 20, 10),
                                        start='top'))
Polygon(0, 110, 33, 73, 95, 45, 155, 25, 240, 20, 340, 55, 365, 85, 400, 100,
        400, 140, 0, 140, fill=gradient('black', rgb(30, 15, 10), rgb(60, 20, 10),
                                        start='top'))

caveBackground = Circle(200, 275, 240, fill=gradient('black', rgb(60, 20, 10)))
caveRoof = Polygon(-20, 140, 58, 75, 140, 38, 200, 30, 275, 45, 320, 65,
                   420, 140, 290, 170, 260, 180, 230, 165, 190, 195, 80, 170,
                   45, 150, fill=gradient('black', rgb(30, 15, 10), start='top'))

# cave floor
Polygon(0, 400, 0, 370, 40, 350, 70, 315, 140, 295, 240, 285, 260, 320, 350, 340,
        400, 380, 400, 400, fill=gradient('black', rgb(80, 30, 15), start='top'))

def drawBat(x, y):
    # body
    Polygon(x, y - 16, x + 6, y, x, y + 7, x - 6, y)

    # ears
    Label('X', x, y + 7, size=20)

    # eyes
    Circle(x - 3, y + 9, 1, fill='red')
    Circle(x + 3, y + 9, 1, fill='red')

# bats
drawBat(75, 175)
drawBat(95, 180)
drawBat(110, 185)
drawBat(160, 190)
drawBat(205, 185)
drawBat(220, 175)
drawBat(280, 175)

# stalagmites
Polygon(100, 325, 105, 310, 110, 290, 115, 270, 120, 265, 125, 270, 120, 290,
        135, 325, fill=gradient(rgb(40, 15, 10), rgb(30, 20, 10),
                                rgb(20, 10, 10), start='top'))
Polygon(250, 360, 260, 345, 260, 325, 255, 305, 260, 302, 270, 305, 275, 335,
        285, 360, fill=gradient(rgb(45, 25, 10), rgb(40, 20, 10),
                                rgb(30, 20, 10), start='top'))

# flashlight
Rect(40, 330, 100, 20, fill='forestGreen')
Polygon(40, 350, 140, 350, 120, 380, 60, 380, fill='green')
Oval(90, 350, 100, 10, fill='forestGreen')
Rect(60, 380, 60, 20, fill='forestGreen')
Oval(90, 380, 60, 6, fill='green')
light = Oval(90, 330, 100, 10, border='forestGreen')

def onMousePress(mouseX, mouseY):
    # Turn the flashlight on and make the cave brighter.
    caveBackground.fill = gradient(rgb(30, 15, 10), 'saddleBrown')
    caveRoof.fill = gradient(rgb(30, 15, 10), rgb(60, 20, 10), start='top')
    light.fill = 'gold'
def onMouseRelease(mouseX, mouseY):
    # Turn the flashlight off and make the cave darker.
    caveBackground.fill = gradient('black', rgb(60, 20, 10))
    caveRoof.fill = gradient('black', rgb(30, 15, 10), start='top')
    light.fill = 'black'



# -
# roof layers
Circle(200, 275, 340,
       fill=gradient(rgb(30, 15, 10), rgb(60, 20, 10), start='top'))
Polygon(0, 35, 20, 30, 40, 10, 70, 0, 330, 0, 365, 25, 400, 30, 400, 70, 0, 70,
        fill=gradient('black', rgb(30, 15, 10), rgb(60, 20, 10), start='top'))
Polygon(0, 70, 70, 30, 115, 20, 165, 0, 255, 0, 315, 15, 370, 60, 400, 70,
        400, 120, 0, 120, fill=gradient('black', rgb(30, 15, 10), rgb(60, 20, 10),
                                        start='top'))
Polygon(0, 110, 33, 73, 95, 45, 155, 25, 240, 20, 340, 55, 365, 85, 400, 100,
        400, 140, 0, 140, fill=gradient('black', rgb(30, 15, 10), rgb(60, 20, 10),
                                        start='top'))

caveBackground = Circle(200, 275, 240, fill=gradient('black', rgb(60, 20, 10)))
caveRoof = Polygon(-20, 140, 58, 75, 140, 38, 200, 30, 275, 45, 320, 65,
                   420, 140, 290, 170, 260, 180, 230, 165, 190, 195, 80, 170,
                   45, 150, fill=gradient('black', rgb(30, 15, 10), start='top'))

# cave floor
Polygon(0, 400, 0, 370, 40, 350, 70, 315, 140, 295, 240, 285, 260, 320, 350, 340,
        400, 380, 400, 400, fill=gradient('black', rgb(80, 30, 15), start='top'))

def drawBat(x, y):
    # body
    Polygon(x, y - 16, x + 6, y, x, y + 7, x - 6, y)

    # ears
    Label('X', x, y + 7, size=20)

    # eyes
    Circle(x - 3, y + 9, 1, fill='red')
    Circle(x + 3, y + 9, 1, fill='red')

# bats
drawBat(75, 175)
drawBat(95, 180)
drawBat(110, 185)
drawBat(160, 190)
drawBat(205, 185)
drawBat(220, 175)
drawBat(280, 175)

# stalagmites
Polygon(100, 325, 105, 310, 110, 290, 115, 270, 120, 265, 125, 270, 120, 290,
        135, 325, fill=gradient(rgb(40, 15, 10), rgb(30, 20, 10),
                                rgb(20, 10, 10), start='top'))
Polygon(250, 360, 260, 345, 260, 325, 255, 305, 260, 302, 270, 305, 275, 335,
        285, 360, fill=gradient(rgb(45, 25, 10), rgb(40, 20, 10),
                                rgb(30, 20, 10), start='top'))

# flashlight
Rect(40, 330, 100, 20, fill='forestGreen')
Polygon(40, 350, 140, 350, 120, 380, 60, 380, fill='green')
Oval(90, 350, 100, 10, fill='forestGreen')
Rect(60, 380, 60, 20, fill='forestGreen')
Oval(90, 380, 60, 6, fill='green')
light = Oval(90, 330, 100, 10, border='forestGreen')

def onMousePress(mouseX, mouseY):
    # Turn the flashlight on and make the cave brighter.
    caveBackground.fill = gradient(rgb(30, 15, 10), 'saddleBrown')
    caveRoof.fill = gradient(rgb(30, 15, 10), rgb(60, 20, 10), start='top')
    light.fill = 'gold'
def onMouseRelease(mouseX, mouseY):
    # Turn the flashlight off and make the cave darker.
    caveBackground.fill = gradient('black', rgb(60, 20, 10))
    caveRoof.fill = gradient('black', rgb(30, 15, 10), start='top')
    light.fill = 'black'

onMousePress(200, 200)
onMouseRelease(200, 200)
onMousePress(200, 200)
onMouseRelease(200, 200)
onMousePress(200, 200)
onMouseRelease(200, 200)

