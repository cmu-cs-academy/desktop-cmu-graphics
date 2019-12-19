app.background = gradient('deepSkyBlue', 'gold', start='top')

# sun
sun = Circle(200, 150, 40, fill=gradient('yellow', 'gold'))

def drawFlower(x, y):
    Line(x, y, x, y + 10, fill='springGreen')
    Star(x, y, 6, 8, fill='yellow')
    Circle(x, y, 2, fill='peru')

# hill
Oval(195, 400, 800, 300, fill=gradient('limeGreen', 'darkGreen', start='top'))
drawFlower(45, 275)
drawFlower(65, 335)
drawFlower(95, 290)
drawFlower(145, 260)
drawFlower(185, 350)
drawFlower(205, 285)
drawFlower(245, 300)
drawFlower(290, 275)
drawFlower(335, 325)
drawFlower(360, 345)

# window frame
Rect(0, 0, 400, 400, fill=None, border='saddleBrown', borderWidth=50)

# blinds and cord
cord = Line(390, 0, 390, 200, fill='white', lineWidth=3)
blinds = Line(195, 15, 195, 200, fill='beige', lineWidth=360, dashes=True)
Rect(10, 10, 370, 20, fill='wheat')

def onMousePress(mouseX, mouseY):
    # Change position of the sun and blinds.
    blinds.y2 = mouseY
    cord.y2 = 400 - mouseY
    sun.centerX = mouseY

onMousePress(200, 80)


# -
app.background = gradient('deepSkyBlue', 'gold', start='top')

# sun
sun = Circle(200, 150, 40, fill=gradient('yellow', 'gold'))

def drawFlower(x, y):
    Line(x, y, x, y + 10, fill='springGreen')
    Star(x, y, 6, 8, fill='yellow')
    Circle(x, y, 2, fill='peru')

# hill
Oval(195, 400, 800, 300, fill=gradient('limeGreen', 'darkGreen', start='top'))
drawFlower(45, 275)
drawFlower(65, 335)
drawFlower(95, 290)
drawFlower(145, 260)
drawFlower(185, 350)
drawFlower(205, 285)
drawFlower(245, 300)
drawFlower(290, 275)
drawFlower(335, 325)
drawFlower(360, 345)

# window frame
Rect(0, 0, 400, 400, fill=None, border='saddleBrown', borderWidth=50)

# blinds and cord
cord = Line(390, 0, 390, 200, fill='white', lineWidth=3)
blinds = Line(195, 15, 195, 200, fill='beige', lineWidth=360, dashes=True)
Rect(10, 10, 370, 20, fill='wheat')

def onMousePress(mouseX, mouseY):
    # Change position of the sun and blinds.
    blinds.y2 = mouseY
    cord.y2 = 400 - mouseY
    sun.centerX = mouseY

onMousePress(200, 50)


# -
app.background = gradient('deepSkyBlue', 'gold', start='top')

# sun
sun = Circle(200, 150, 40, fill=gradient('yellow', 'gold'))

def drawFlower(x, y):
    Line(x, y, x, y + 10, fill='springGreen')
    Star(x, y, 6, 8, fill='yellow')
    Circle(x, y, 2, fill='peru')

# hill
Oval(195, 400, 800, 300, fill=gradient('limeGreen', 'darkGreen', start='top'))
drawFlower(45, 275)
drawFlower(65, 335)
drawFlower(95, 290)
drawFlower(145, 260)
drawFlower(185, 350)
drawFlower(205, 285)
drawFlower(245, 300)
drawFlower(290, 275)
drawFlower(335, 325)
drawFlower(360, 345)

# window frame
Rect(0, 0, 400, 400, fill=None, border='saddleBrown', borderWidth=50)

# blinds and cord
cord = Line(390, 0, 390, 200, fill='white', lineWidth=3)
blinds = Line(195, 15, 195, 200, fill='beige', lineWidth=360, dashes=True)
Rect(10, 10, 370, 20, fill='wheat')

def onMousePress(mouseX, mouseY):
    # Change position of the sun and blinds.
    blinds.y2 = mouseY
    cord.y2 = 400 - mouseY
    sun.centerX = mouseY

onMousePress(200, 350)

