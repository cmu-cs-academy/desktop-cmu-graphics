app.background = gradient('cyan', 'midnightBlue', start='top')

# Marlin (left fish)
RegularPolygon(150, 200, 15, 3, rotateAngle=30,
               fill=gradient('orange', 'darkOrange', start='top'))
Oval(128, 187, 30, 15, rotateAngle=12,
     fill=gradient('orange', 'darkOrange', start='top'))
Oval(118, 200, 56, 30, fill='white')
Oval(115, 200, 50, 30, fill=gradient('orange', 'darkOrange', start='top'))
Oval(110, 200, 40, 30, fill='white')
Oval(105, 200, 30, 30, fill=gradient('orange', 'darkOrange', start='top'))
Circle(100, 197, 5, fill='white')
Circle(99, 196, 3, border='violet', borderWidth=1)
Arc(118, 202, 40, 40, 95, 80, fill='darkOrange', border='black')
Arc(118, 202, 38, 38, 95, 80, fill='darkOrange')
Line(90, 205, 98, 208, lineWidth=0.5)

# Dory (right fish)
Polygon(260, 200, 215, 190, 219, 215, fill='yellow')
Polygon(275, 175, 293, 180, 305, 203, 295, 215, 285, 220, fill='dodgerBlue')
Oval(275, 197, 50, 45, fill='dodgerBlue')
Oval(270, 200, 55, 45, fill='dodgerBlue')
Oval(265, 200, 60, 40, fill='dodgerBlue')
Oval(262, 192, 45, 20, fill='midnightBlue', rotateAngle=350)
Oval(265, 192, 15, 7, fill='dodgerBlue')
Polygon(280, 205, 260, 200, 260, 216, fill='yellow')
Circle(293, 190, 5, fill='white')
Circle(294, 189, 3, border='violet', borderWidth=1)
Arc(297, 197, 20, 20, 150, 75, fill=None, border='darkBlue', borderWidth=0.5)
Arc(297, 196, 19, 19, 145, 85, fill='dodgerBlue')

leftBubble = Circle(125, 200, 75, fill=gradient('lightBlue', 'cornflowerBlue'))
rightBubble = Circle(275, 200, 75, fill=gradient('lightBlue', 'cornflowerBlue'))

def onMouseMove(mouseX, mouseY):
    if (mouseX > 0):
        # The opacity of the right bubble should be mouseX divided by 4.
        rightBubble.opacity = mouseX / 4
        # Set the left bubble's opacity using the right bubble's opacity.
        leftBubble.opacity = 100 - rightBubble.opacity
        # The width and height of the right bubble should be mouseX divided by 2.
        rightBubble.width = mouseX / 2
        rightBubble.height = mouseX / 2
        # Set the width and height of the left bubble using the right
        # bubble's width and height.
        leftBubble.width = 200 - rightBubble.width
        leftBubble.height = 200 - rightBubble.height
        # Re-center the bubbles.
        leftBubble.centerY = 200
        leftBubble.right = 200
        rightBubble.centerY = 200
        rightBubble.left = 200



# -
app.background = gradient('cyan', 'midnightBlue', start='top')

# Marlin (left fish)
RegularPolygon(150, 200, 15, 3, rotateAngle=30,
               fill=gradient('orange', 'darkOrange', start='top'))
Oval(128, 187, 30, 15, rotateAngle=12,
     fill=gradient('orange', 'darkOrange', start='top'))
Oval(118, 200, 56, 30, fill='white')
Oval(115, 200, 50, 30, fill=gradient('orange', 'darkOrange', start='top'))
Oval(110, 200, 40, 30, fill='white')
Oval(105, 200, 30, 30, fill=gradient('orange', 'darkOrange', start='top'))
Circle(100, 197, 5, fill='white')
Circle(99, 196, 3, border='violet', borderWidth=1)
Arc(118, 202, 40, 40, 95, 80, fill='darkOrange', border='black')
Arc(118, 202, 38, 38, 95, 80, fill='darkOrange')
Line(90, 205, 98, 208, lineWidth=0.5)

# Dory (right fish)
Polygon(260, 200, 215, 190, 219, 215, fill='yellow')
Polygon(275, 175, 293, 180, 305, 203, 295, 215, 285, 220, fill='dodgerBlue')
Oval(275, 197, 50, 45, fill='dodgerBlue')
Oval(270, 200, 55, 45, fill='dodgerBlue')
Oval(265, 200, 60, 40, fill='dodgerBlue')
Oval(262, 192, 45, 20, fill='midnightBlue', rotateAngle=350)
Oval(265, 192, 15, 7, fill='dodgerBlue')
Polygon(280, 205, 260, 200, 260, 216, fill='yellow')
Circle(293, 190, 5, fill='white')
Circle(294, 189, 3, border='violet', borderWidth=1)
Arc(297, 197, 20, 20, 150, 75, fill=None, border='darkBlue', borderWidth=0.5)
Arc(297, 196, 19, 19, 145, 85, fill='dodgerBlue')

leftBubble = Circle(125, 200, 75, fill=gradient('lightBlue', 'cornflowerBlue'))
rightBubble = Circle(275, 200, 75, fill=gradient('lightBlue', 'cornflowerBlue'))

def onMouseMove(mouseX, mouseY):
    if (mouseX > 0):
        # The opacity of the right bubble should be mouseX divided by 4.
        rightBubble.opacity = mouseX / 4
        # Set the left bubble's opacity using the right bubble's opacity.
        leftBubble.opacity = 100 - rightBubble.opacity
        # The width and height of the right bubble should be mouseX divided by 2.
        rightBubble.width = mouseX / 2
        rightBubble.height = mouseX / 2
        # Set the width and height of the left bubble using the right
        # bubble's width and height.
        leftBubble.width = 200 - rightBubble.width
        leftBubble.height = 200 - rightBubble.height
        # Re-center the bubbles.
        leftBubble.centerY = 200
        leftBubble.right = 200
        rightBubble.centerY = 200
        rightBubble.left = 200



# -
app.background = gradient('cyan', 'midnightBlue', start='top')

# Marlin (left fish)
RegularPolygon(150, 200, 15, 3, rotateAngle=30,
               fill=gradient('orange', 'darkOrange', start='top'))
Oval(128, 187, 30, 15, rotateAngle=12,
     fill=gradient('orange', 'darkOrange', start='top'))
Oval(118, 200, 56, 30, fill='white')
Oval(115, 200, 50, 30, fill=gradient('orange', 'darkOrange', start='top'))
Oval(110, 200, 40, 30, fill='white')
Oval(105, 200, 30, 30, fill=gradient('orange', 'darkOrange', start='top'))
Circle(100, 197, 5, fill='white')
Circle(99, 196, 3, border='violet', borderWidth=1)
Arc(118, 202, 40, 40, 95, 80, fill='darkOrange', border='black')
Arc(118, 202, 38, 38, 95, 80, fill='darkOrange')
Line(90, 205, 98, 208, lineWidth=0.5)

# Dory (right fish)
Polygon(260, 200, 215, 190, 219, 215, fill='yellow')
Polygon(275, 175, 293, 180, 305, 203, 295, 215, 285, 220, fill='dodgerBlue')
Oval(275, 197, 50, 45, fill='dodgerBlue')
Oval(270, 200, 55, 45, fill='dodgerBlue')
Oval(265, 200, 60, 40, fill='dodgerBlue')
Oval(262, 192, 45, 20, fill='midnightBlue', rotateAngle=350)
Oval(265, 192, 15, 7, fill='dodgerBlue')
Polygon(280, 205, 260, 200, 260, 216, fill='yellow')
Circle(293, 190, 5, fill='white')
Circle(294, 189, 3, border='violet', borderWidth=1)
Arc(297, 197, 20, 20, 150, 75, fill=None, border='darkBlue', borderWidth=0.5)
Arc(297, 196, 19, 19, 145, 85, fill='dodgerBlue')

leftBubble = Circle(125, 200, 75, fill=gradient('lightBlue', 'cornflowerBlue'))
rightBubble = Circle(275, 200, 75, fill=gradient('lightBlue', 'cornflowerBlue'))

def onMouseMove(mouseX, mouseY):
    if (mouseX > 0):
        # The opacity of the right bubble should be mouseX divided by 4.
        rightBubble.opacity = mouseX / 4
        # Set the left bubble's opacity using the right bubble's opacity.
        leftBubble.opacity = 100 - rightBubble.opacity
        # The width and height of the right bubble should be mouseX divided by 2.
        rightBubble.width = mouseX / 2
        rightBubble.height = mouseX / 2
        # Set the width and height of the left bubble using the right
        # bubble's width and height.
        leftBubble.width = 200 - rightBubble.width
        leftBubble.height = 200 - rightBubble.height
        # Re-center the bubbles.
        leftBubble.centerY = 200
        leftBubble.right = 200
        rightBubble.centerY = 200
        rightBubble.left = 200

onMouseMove(40, 140)

