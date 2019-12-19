app.background = 'aliceBlue'

# legs
flamingoLegs = Group(
    Line(230, 280, 230, 400, fill='gold', lineWidth=5),
    Line(230, 290, 255, 315, fill='gold', lineWidth=5),
    Line(255, 315, 200, 325, fill='gold', lineWidth=5)
    )

# body
flamingoBody = Group(
    Oval(190, 255, 100, 70, fill='lightPink', align='left'),
    Oval(257, 245, 95, 60, fill=rgb(225, 130, 170), rotateAngle=15),
    Line(195, 250, 205, 125, fill='lightPink', lineWidth=10),
    Circle(180, 130, 10),
    Circle(180, 140, 10, fill='aliceBlue'),
    Circle(215, 123, 16, fill='lightPink', align='right'),
    Circle(195, 120, 3)
    )

# water
water = Rect(200, 400, 400, 20, align='bottom',
             fill=gradient('lightSkyBlue', 'deepSkyBlue', start='top'))

def onStep():
    # Move the water up until it gets close to the top of the screen.
    # Move the flamingo so that it floats on the rising water. It should rest
    # so that 20 pixels of body are in the water.
    if (water.top > 170):
        water.height += 1
        water.top -= 1
        if (flamingoBody.bottom > water.top + 20):
            flamingoBody.bottom = water.top + 20


onSteps(50)
app.paused = True


# -
app.background = 'aliceBlue'

# legs
flamingoLegs = Group(
    Line(230, 280, 230, 400, fill='gold', lineWidth=5),
    Line(230, 290, 255, 315, fill='gold', lineWidth=5),
    Line(255, 315, 200, 325, fill='gold', lineWidth=5)
    )

# body
flamingoBody = Group(
    Oval(190, 255, 100, 70, fill='lightPink', align='left'),
    Oval(257, 245, 95, 60, fill=rgb(225, 130, 170), rotateAngle=15),
    Line(195, 250, 205, 125, fill='lightPink', lineWidth=10),
    Circle(180, 130, 10),
    Circle(180, 140, 10, fill='aliceBlue'),
    Circle(215, 123, 16, fill='lightPink', align='right'),
    Circle(195, 120, 3)
    )

# water
water = Rect(200, 400, 400, 20, align='bottom',
             fill=gradient('lightSkyBlue', 'deepSkyBlue', start='top'))

def onStep():
    # Move the water up until it gets close to the top of the screen.
    # Move the flamingo so that it floats on the rising water. It should rest
    # so that 20 pixels of body are in the water.
    if (water.top > 170):
        water.height += 1
        water.top -= 1
        if (flamingoBody.bottom > water.top + 20):
            flamingoBody.bottom = water.top + 20


onSteps(20)
app.paused = True


# -
app.background = 'aliceBlue'

# legs
flamingoLegs = Group(
    Line(230, 280, 230, 400, fill='gold', lineWidth=5),
    Line(230, 290, 255, 315, fill='gold', lineWidth=5),
    Line(255, 315, 200, 325, fill='gold', lineWidth=5)
    )

# body
flamingoBody = Group(
    Oval(190, 255, 100, 70, fill='lightPink', align='left'),
    Oval(257, 245, 95, 60, fill=rgb(225, 130, 170), rotateAngle=15),
    Line(195, 250, 205, 125, fill='lightPink', lineWidth=10),
    Circle(180, 130, 10),
    Circle(180, 140, 10, fill='aliceBlue'),
    Circle(215, 123, 16, fill='lightPink', align='right'),
    Circle(195, 120, 3)
    )

# water
water = Rect(200, 400, 400, 20, align='bottom',
             fill=gradient('lightSkyBlue', 'deepSkyBlue', start='top'))

def onStep():
    # Move the water up until it gets close to the top of the screen.
    # Move the flamingo so that it floats on the rising water. It should rest
    # so that 20 pixels of body are in the water.
    if (water.top > 170):
        water.height += 1
        water.top -= 1
        if (flamingoBody.bottom > water.top + 20):
            flamingoBody.bottom = water.top + 20



