app.background = rgb(60, 30, 20)

Rect(0, 280, 400, 120, fill='peru')

# spring and glove
spring1 = Oval(0, 200, 40, 75, fill=None, border='grey')
spring2 = Oval(10, 200, 40, 75, fill=None, border='grey')
spring3 = Oval(20, 200, 40, 75, fill=None, border='grey')
spring4 = Oval(30, 200, 40, 75, fill=None, border='grey')
spring5 = Oval(40, 200, 40, 75, fill=None, border='grey')

glove = Group(
    Oval(80, 170, 42, 32, fill=gradient('red', 'crimson', start='right-top'),
         border='darkRed', rotateAngle=-30),
    Oval(80, 200, 85, 75, fill=gradient('red', 'crimson', start='right-bottom'),
         border='darkRed'),
    Oval(80, 170, 40, 30, fill=gradient('red', 'crimson', start='right-top'),
         rotateAngle=-30),
    Rect(50, 200, 30, 75, fill=gradient('red', 'crimson', start='right'),
         border='darkRed', align='center'),
    Line(100, 167, 85, 175, fill='darkRed')
    )

# punching bag
punchingBag = Group(
    Oval(325, 350, 100, 50, fill=gradient('red', 'crimson', start='left'),
         border='darkRed'),
    Rect(275, 100, 100, 250, fill=gradient('red', 'crimson', start='left')),
    Oval(325, 100, 100, 50, fill=gradient('red', 'crimson', start='left'),
         border='darkRed')
    )
cord = Line(325, 0, 325, 100, fill='white', lineWidth=4, dashes=True)

# comic-style hit symbol
hit = Star(275, 200, 40, 11, fill=gradient('yellow', 'orange'),
           border='darkRed', visible=False)

def onMouseMove(mouseX, mouseY):
    gapSize = mouseX / 5

    # Move each of the springs the same distance from each other.
    spring2.centerX = spring1.centerX + gapSize
    spring3.centerX = spring2.centerX + gapSize
    spring4.centerX = spring3.centerX + gapSize
    spring5.centerX = spring4.centerX + gapSize
    glove.centerX = mouseX
    # If the glove's centerX value is too large, display the hit star and
    # update the position of it and the punching bag appropriately.
    if (glove.centerX >= 230):
        punchingBag.left = glove.right
        hit.centerX = glove.right
        hit.visible = True
    # Otherwise, reset both the hit star and the punching bag.
    else:
        punchingBag.left = 275
        hit.visible = False
    cord.x2 = punchingBag.centerX



# -
app.background = rgb(60, 30, 20)

Rect(0, 280, 400, 120, fill='peru')

# spring and glove
spring1 = Oval(0, 200, 40, 75, fill=None, border='grey')
spring2 = Oval(10, 200, 40, 75, fill=None, border='grey')
spring3 = Oval(20, 200, 40, 75, fill=None, border='grey')
spring4 = Oval(30, 200, 40, 75, fill=None, border='grey')
spring5 = Oval(40, 200, 40, 75, fill=None, border='grey')

glove = Group(
    Oval(80, 170, 42, 32, fill=gradient('red', 'crimson', start='right-top'),
         border='darkRed', rotateAngle=-30),
    Oval(80, 200, 85, 75, fill=gradient('red', 'crimson', start='right-bottom'),
         border='darkRed'),
    Oval(80, 170, 40, 30, fill=gradient('red', 'crimson', start='right-top'),
         rotateAngle=-30),
    Rect(50, 200, 30, 75, fill=gradient('red', 'crimson', start='right'),
         border='darkRed', align='center'),
    Line(100, 167, 85, 175, fill='darkRed')
    )

# punching bag
punchingBag = Group(
    Oval(325, 350, 100, 50, fill=gradient('red', 'crimson', start='left'),
         border='darkRed'),
    Rect(275, 100, 100, 250, fill=gradient('red', 'crimson', start='left')),
    Oval(325, 100, 100, 50, fill=gradient('red', 'crimson', start='left'),
         border='darkRed')
    )
cord = Line(325, 0, 325, 100, fill='white', lineWidth=4, dashes=True)

# comic-style hit symbol
hit = Star(275, 200, 40, 11, fill=gradient('yellow', 'orange'),
           border='darkRed', visible=False)

def onMouseMove(mouseX, mouseY):
    gapSize = mouseX / 5

    # Move each of the springs the same distance from each other.
    spring2.centerX = spring1.centerX + gapSize
    spring3.centerX = spring2.centerX + gapSize
    spring4.centerX = spring3.centerX + gapSize
    spring5.centerX = spring4.centerX + gapSize
    glove.centerX = mouseX
    # If the glove's centerX value is too large, display the hit star and
    # update the position of it and the punching bag appropriately.
    if (glove.centerX >= 230):
        punchingBag.left = glove.right
        hit.centerX = glove.right
        hit.visible = True
    # Otherwise, reset both the hit star and the punching bag.
    else:
        punchingBag.left = 275
        hit.visible = False
    cord.x2 = punchingBag.centerX

onMouseMove(230, 200)


# -
app.background = rgb(60, 30, 20)

Rect(0, 280, 400, 120, fill='peru')

# spring and glove
spring1 = Oval(0, 200, 40, 75, fill=None, border='grey')
spring2 = Oval(10, 200, 40, 75, fill=None, border='grey')
spring3 = Oval(20, 200, 40, 75, fill=None, border='grey')
spring4 = Oval(30, 200, 40, 75, fill=None, border='grey')
spring5 = Oval(40, 200, 40, 75, fill=None, border='grey')

glove = Group(
    Oval(80, 170, 42, 32, fill=gradient('red', 'crimson', start='right-top'),
         border='darkRed', rotateAngle=-30),
    Oval(80, 200, 85, 75, fill=gradient('red', 'crimson', start='right-bottom'),
         border='darkRed'),
    Oval(80, 170, 40, 30, fill=gradient('red', 'crimson', start='right-top'),
         rotateAngle=-30),
    Rect(50, 200, 30, 75, fill=gradient('red', 'crimson', start='right'),
         border='darkRed', align='center'),
    Line(100, 167, 85, 175, fill='darkRed')
    )

# punching bag
punchingBag = Group(
    Oval(325, 350, 100, 50, fill=gradient('red', 'crimson', start='left'),
         border='darkRed'),
    Rect(275, 100, 100, 250, fill=gradient('red', 'crimson', start='left')),
    Oval(325, 100, 100, 50, fill=gradient('red', 'crimson', start='left'),
         border='darkRed')
    )
cord = Line(325, 0, 325, 100, fill='white', lineWidth=4, dashes=True)

# comic-style hit symbol
hit = Star(275, 200, 40, 11, fill=gradient('yellow', 'orange'),
           border='darkRed', visible=False)

def onMouseMove(mouseX, mouseY):
    gapSize = mouseX / 5

    # Move each of the springs the same distance from each other.
    spring2.centerX = spring1.centerX + gapSize
    spring3.centerX = spring2.centerX + gapSize
    spring4.centerX = spring3.centerX + gapSize
    spring5.centerX = spring4.centerX + gapSize
    glove.centerX = mouseX
    # If the glove's centerX value is too large, display the hit star and
    # update the position of it and the punching bag appropriately.
    if (glove.centerX >= 230):
        punchingBag.left = glove.right
        hit.centerX = glove.right
        hit.visible = True
    # Otherwise, reset both the hit star and the punching bag.
    else:
        punchingBag.left = 275
        hit.visible = False
    cord.x2 = punchingBag.centerX

onMouseMove(229, 200)

