app.background = 'lightYellow'
app.stepsPerSecond = 8

app.shouldAnimate = False
app.frameIndex = 0

# Stores the last position the mouse was dragged at.
app.x = None
app.y = None

# Stores the different frames to animate.
app.currFrame = Group()
app.frames = [ ]
app.frameNumber = 1

directions = Group(Label('Flip Book', 10, 20, size=20, align='left'))

def makeDirections():
    i = 0
    directionList = [ 'Change pen color by clicking on the colorBar',
                      "Press 'n' to add a new frame",
                      "Press 'a' to animate",
                      "Press 'z' to clear the current frame",
                      "Press 'space' to hide/unhide this guide." ]

    for direction in directionList:
        directions.add(
            Label(direction, 10, 50 +  i * 25, size=15, opacity=80, align='left')
            )
        i += 1

makeDirections()

colorBar = Group()
colors = [ 'crimson', 'darkOrange', 'gold', 'mediumSeaGreen',
           'lightSkyBlue', 'midnightBlue', 'lightYellow', 'black' ]
for i in range(8):
    colorBar.add(
        Rect(350, i * 50, 50, 50, fill=colors[i], border='black')
        )

penBar = Group()
smallestRadius = 2
for i in range(4):
    penBar.add(Circle(20 + i * 50, 380, smallestRadius + i * 4))

penTool = Group(
    Rect(275, 375, 10, 15, border='black'),
    Polygon(275, 375, 285, 375, 280, 370, border='black')
    )
penTool.rotateAngle = -30
penTool.drawSize = 2

def startAnimation():
    # Adds the current frame to the list of frames to animate.
    app.frames.append(app.currFrame)

    # Hides the toolbars, indicates that animation should begin, and sets all
    # the opacities to 100.
    colorBar.visible = False
    penBar.visible = False
    directions.visible = False
    app.shouldAnimate = True
    for frame in app.frames:
        frame.opacity = 100

def startNewFrame():
    # Adds the current frame to the list of frames.
    app.frames.append(app.currFrame)

    # Lowers the opacity of the previous frames.
    for frame in app.frames:
        frame.opacity = max(frame.opacity - 45, 0)

    # Creates a new frame.
    app.currFrame = Group()
    app.frameNumber += 1

def onKeyPress(key):
    if (key == 'n'):
        startNewFrame()
    elif (key == 'a'):
        startAnimation()
    elif (key == 'z'):
        app.currFrame.clear()
    elif (key == 'space'):
        directions.visible = not directions.visible

def onMousePress(mouseX, mouseY):
    # If the mouse is pressed on the color bar, changes the pen's color.
    targetColor = colorBar.hitTest(mouseX, mouseY)
    if (targetColor != None):
        penTool.fill = targetColor.fill

    # If the mouse is pressed on the size bar, changes the pen's size.
    targetPen = penBar.hitTest(mouseX, mouseY)
    if (targetPen != None):
        penTool.drawSize = targetPen.radius

def onMouseRelease(mouseX, mouseY):
    app.x = None
    app.y = None

def onMouseMove(mouseX, mouseY):
    # Moves the pen.
    penTool.left = mouseX
    penTool.top = mouseY

def onMouseDrag(mouseX, mouseY):
    # Draws at the mouse position onto the current frame.
    onMouseMove(mouseX, mouseY)
    if (app.x == None):
        app.x, app.y = mouseX, mouseY
    else:
        app.currFrame.add(
            Line(app.x, app.y, mouseX, mouseY, fill=penTool.fill,
                 lineWidth=penTool.drawSize)
            )
        app.x, app.y = mouseX, mouseY

def onStep():
    if (app.shouldAnimate == True):
        # For each of the frames, sets them invisble, then displays only the
        # current frame.
        for frame in app.frames:
            frame.visible = False
        app.frames[app.frameIndex].visible = True

        # Cycles through which frame is visible.
        app.frameIndex += 1
        if (app.frameIndex >= app.frameNumber):
            app.frameIndex = 0


