app.stepsPerSecond = 20
app.background = gradient('dodgerBlue', 'paleTurquoise', start='top')

# Organize the balloons together.
balloons = Group(
    Line(145, 50, 185, 270, fill='white', lineWidth=1),
    Circle(145, 50, 50,
           fill=gradient('plum', 'indigo', 'indigo', start='right-top')),
    Line(185, 110, 185, 270, fill='white', lineWidth=1),
    Circle(185, 110, 45,
           fill=gradient('lavender', 'mediumPurple', 'mediumPurple',
                         start='right-top')),
    Line(225, 50, 185, 270, fill='white', lineWidth=1),
    Circle(225, 50, 35,
           fill=gradient('plum', 'darkViolet', 'darkViolet', start='right-top')),
    Line(105, 120, 185, 270, fill='white', lineWidth=1),
    Circle(105, 120, 40,
           fill=gradient('plum', 'mediumVioletRed', 'mediumVioletRed',
                         start='right-top')),
    Line(265, 120, 185, 270, fill='white', lineWidth=1),
    Circle(265, 120, 35,
           fill=gradient('plum', 'purple', 'purple', start='right-top'))
    )

# Organize the house parts together.
house = Group(
    Rect(150, 350, 50, 50, fill='pink', border='white'),
    Rect(200, 350, 50, 50, fill='limeGreen', border='white'),
    Polygon(140, 350, 260, 350, 260, 300, 150, 300, fill='mediumSlateBlue',
            border='white', borderWidth=1),
    Polygon(200, 360, 200, 340, 225, 310, 250, 340, 250, 360,
            fill='lemonChiffon', border='white'),
    Polygon(160, 340, 160, 330, 170, 320, 180, 330, 180, 340,
            fill='lemonChiffon', border='white'),
    Rect(175, 380, 10, 20, fill='maroon', border='white'),
    Rect(150, 350, 50, 15, fill='cornflowerBlue', border='white'),
    Rect(180, 270, 10, 40, fill='brown', border='white', borderWidth=1),
    Rect(225, 380, 12, 20, fill='silver', border='mistyRose', align='center'),
    Rect(225, 340, 10, 18, fill='silver', border='mistyRose', align='center'),
    Rect(170, 333, 5, 9, fill='silver', border='mistyRose', align='center'),
    Rect(162, 385, 6, 12, fill='silver', border='mistyRose', align='center')
    )

# Combine the house and balloons into a single group.
upHouse = Group(balloons, house)

def onStep():
    # Move the house up 8 pixels, with wraparound.
    upHouse.centerY -= 8
    if (upHouse.bottom < 0):
        upHouse.top = 400
def onKeyHold(keys):
    # If right or left keys are held, move in that direction by 5 with wraparound.
    if ('right' in keys):
        upHouse.right += 5
    if ('left' in keys):
        upHouse.right -= 5
    if (upHouse.left > 400):
        upHouse.right = 0
    elif (upHouse.right < 0):
        upHouse.left = 400

onKeyHolds(['left'], 20)
app.paused = True


# -
app.stepsPerSecond = 20
app.background = gradient('dodgerBlue', 'paleTurquoise', start='top')

# Organize the balloons together.
balloons = Group(
    Line(145, 50, 185, 270, fill='white', lineWidth=1),
    Circle(145, 50, 50,
           fill=gradient('plum', 'indigo', 'indigo', start='right-top')),
    Line(185, 110, 185, 270, fill='white', lineWidth=1),
    Circle(185, 110, 45,
           fill=gradient('lavender', 'mediumPurple', 'mediumPurple',
                         start='right-top')),
    Line(225, 50, 185, 270, fill='white', lineWidth=1),
    Circle(225, 50, 35,
           fill=gradient('plum', 'darkViolet', 'darkViolet', start='right-top')),
    Line(105, 120, 185, 270, fill='white', lineWidth=1),
    Circle(105, 120, 40,
           fill=gradient('plum', 'mediumVioletRed', 'mediumVioletRed',
                         start='right-top')),
    Line(265, 120, 185, 270, fill='white', lineWidth=1),
    Circle(265, 120, 35,
           fill=gradient('plum', 'purple', 'purple', start='right-top'))
    )

# Organize the house parts together.
house = Group(
    Rect(150, 350, 50, 50, fill='pink', border='white'),
    Rect(200, 350, 50, 50, fill='limeGreen', border='white'),
    Polygon(140, 350, 260, 350, 260, 300, 150, 300, fill='mediumSlateBlue',
            border='white', borderWidth=1),
    Polygon(200, 360, 200, 340, 225, 310, 250, 340, 250, 360,
            fill='lemonChiffon', border='white'),
    Polygon(160, 340, 160, 330, 170, 320, 180, 330, 180, 340,
            fill='lemonChiffon', border='white'),
    Rect(175, 380, 10, 20, fill='maroon', border='white'),
    Rect(150, 350, 50, 15, fill='cornflowerBlue', border='white'),
    Rect(180, 270, 10, 40, fill='brown', border='white', borderWidth=1),
    Rect(225, 380, 12, 20, fill='silver', border='mistyRose', align='center'),
    Rect(225, 340, 10, 18, fill='silver', border='mistyRose', align='center'),
    Rect(170, 333, 5, 9, fill='silver', border='mistyRose', align='center'),
    Rect(162, 385, 6, 12, fill='silver', border='mistyRose', align='center')
    )

# Combine the house and balloons into a single group.
upHouse = Group(balloons, house)

def onStep():
    # Move the house up 8 pixels, with wraparound.
    upHouse.centerY -= 8
    if (upHouse.bottom < 0):
        upHouse.top = 400
def onKeyHold(keys):
    # If right or left keys are held, move in that direction by 5 with wraparound.
    if ('right' in keys):
        upHouse.right += 5
    if ('left' in keys):
        upHouse.right -= 5
    if (upHouse.left > 400):
        upHouse.right = 0
    elif (upHouse.right < 0):
        upHouse.left = 400

onStep()
app.paused = True


# -
app.stepsPerSecond = 20
app.background = gradient('dodgerBlue', 'paleTurquoise', start='top')

# Organize the balloons together.
balloons = Group(
    Line(145, 50, 185, 270, fill='white', lineWidth=1),
    Circle(145, 50, 50,
           fill=gradient('plum', 'indigo', 'indigo', start='right-top')),
    Line(185, 110, 185, 270, fill='white', lineWidth=1),
    Circle(185, 110, 45,
           fill=gradient('lavender', 'mediumPurple', 'mediumPurple',
                         start='right-top')),
    Line(225, 50, 185, 270, fill='white', lineWidth=1),
    Circle(225, 50, 35,
           fill=gradient('plum', 'darkViolet', 'darkViolet', start='right-top')),
    Line(105, 120, 185, 270, fill='white', lineWidth=1),
    Circle(105, 120, 40,
           fill=gradient('plum', 'mediumVioletRed', 'mediumVioletRed',
                         start='right-top')),
    Line(265, 120, 185, 270, fill='white', lineWidth=1),
    Circle(265, 120, 35,
           fill=gradient('plum', 'purple', 'purple', start='right-top'))
    )

# Organize the house parts together.
house = Group(
    Rect(150, 350, 50, 50, fill='pink', border='white'),
    Rect(200, 350, 50, 50, fill='limeGreen', border='white'),
    Polygon(140, 350, 260, 350, 260, 300, 150, 300, fill='mediumSlateBlue',
            border='white', borderWidth=1),
    Polygon(200, 360, 200, 340, 225, 310, 250, 340, 250, 360,
            fill='lemonChiffon', border='white'),
    Polygon(160, 340, 160, 330, 170, 320, 180, 330, 180, 340,
            fill='lemonChiffon', border='white'),
    Rect(175, 380, 10, 20, fill='maroon', border='white'),
    Rect(150, 350, 50, 15, fill='cornflowerBlue', border='white'),
    Rect(180, 270, 10, 40, fill='brown', border='white', borderWidth=1),
    Rect(225, 380, 12, 20, fill='silver', border='mistyRose', align='center'),
    Rect(225, 340, 10, 18, fill='silver', border='mistyRose', align='center'),
    Rect(170, 333, 5, 9, fill='silver', border='mistyRose', align='center'),
    Rect(162, 385, 6, 12, fill='silver', border='mistyRose', align='center')
    )

# Combine the house and balloons into a single group.
upHouse = Group(balloons, house)

def onStep():
    # Move the house up 8 pixels, with wraparound.
    upHouse.centerY -= 8
    if (upHouse.bottom < 0):
        upHouse.top = 400
def onKeyHold(keys):
    # If right or left keys are held, move in that direction by 5 with wraparound.
    if ('right' in keys):
        upHouse.right += 5
    if ('left' in keys):
        upHouse.right -= 5
    if (upHouse.left > 400):
        upHouse.right = 0
    elif (upHouse.right < 0):
        upHouse.left = 400


