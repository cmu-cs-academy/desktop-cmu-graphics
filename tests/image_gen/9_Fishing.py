app.background = gradient('lightSkyBlue', 'orange', start='top')

# sun and lake
Circle(250, 335, 50, fill='gold')
Rect(0, 300, 400, 100, fill='dodgerBlue')

# boat and fishing rod
Polygon(0, 270, 0, 350, 50, 350, 85, 315, 100, 270, fill='sienna')
Line(0, 240, 140, 160)

# fishing line, fish body, and fish tail
fishingLine = Line(140, 160, 140, 340, lineWidth=1)
fishBody = Oval(340, 340, 50, 30, fill='salmon')
fishTail = Polygon(345, 340, 380, 350, 380, 330, fill='salmon')

def pullUpFish():
    fishingLine.x2 = 140
    fishingLine.y2 = 225

    fishBody.rotateAngle = 90
    fishBody.centerX = 140
    fishBody.centerY = 250
    fishTail.rotateAngle = 90
    fishTail.centerX = 140
    fishTail.top = 255

def onKeyPress(key):
    # Release the fish if the correct key is pressed.
    if (key == 'r'):
        fishBody.rotateAngle = 0
        fishBody.centerX = 340
        fishBody.centerY = 340

        fishTail.rotateAngle = 0
        fishTail.left = 345
        fishTail.centerY = 340

def onMouseDrag(mouseX, mouseY):
    # If fish is very close to boat, pull it up.
    if (fishBody.centerX <= 165):
        pullUpFish()

    # If the line is behind fish, only move the line.
    elif (fishBody.centerX - mouseX < 0):
        fishingLine.x2 = mouseX
        fishingLine.y2 = mouseY

    # If the line is too far from fish, only move the line.
    elif (fishBody.centerX - mouseX > 80):
        fishingLine.x2 = mouseX
        fishingLine.y2 = mouseY

    # If the line is close enough to fish, the line should hook the fish.
    elif (mouseY > 300):
        fishingLine.x2 = mouseX
        fishingLine.y2 = mouseY

        fishBody.centerX = mouseX + 25
        fishBody.centerY = mouseY
        fishTail.centerX = mouseX + 50
        fishTail.centerY = mouseY

onMouseDrag(290, 340)
onMouseDrag(250, 340)
onMouseDrag(210, 340)
onMouseDrag(170, 340)
onMouseDrag(140, 340)
onMouseDrag(130, 340)


# -
app.background = gradient('lightSkyBlue', 'orange', start='top')

# sun and lake
Circle(250, 335, 50, fill='gold')
Rect(0, 300, 400, 100, fill='dodgerBlue')

# boat and fishing rod
Polygon(0, 270, 0, 350, 50, 350, 85, 315, 100, 270, fill='sienna')
Line(0, 240, 140, 160)

# fishing line, fish body, and fish tail
fishingLine = Line(140, 160, 140, 340, lineWidth=1)
fishBody = Oval(340, 340, 50, 30, fill='salmon')
fishTail = Polygon(345, 340, 380, 350, 380, 330, fill='salmon')

def pullUpFish():
    fishingLine.x2 = 140
    fishingLine.y2 = 225

    fishBody.rotateAngle = 90
    fishBody.centerX = 140
    fishBody.centerY = 250
    fishTail.rotateAngle = 90
    fishTail.centerX = 140
    fishTail.top = 255

def onKeyPress(key):
    # Release the fish if the correct key is pressed.
    if (key == 'r'):
        fishBody.rotateAngle = 0
        fishBody.centerX = 340
        fishBody.centerY = 340

        fishTail.rotateAngle = 0
        fishTail.left = 345
        fishTail.centerY = 340

def onMouseDrag(mouseX, mouseY):
    # If fish is very close to boat, pull it up.
    if (fishBody.centerX <= 165):
        pullUpFish()

    # If the line is behind fish, only move the line.
    elif (fishBody.centerX - mouseX < 0):
        fishingLine.x2 = mouseX
        fishingLine.y2 = mouseY

    # If the line is too far from fish, only move the line.
    elif (fishBody.centerX - mouseX > 80):
        fishingLine.x2 = mouseX
        fishingLine.y2 = mouseY

    # If the line is close enough to fish, the line should hook the fish.
    elif (mouseY > 300):
        fishingLine.x2 = mouseX
        fishingLine.y2 = mouseY

        fishBody.centerX = mouseX + 25
        fishBody.centerY = mouseY
        fishTail.centerX = mouseX + 50
        fishTail.centerY = mouseY

onMouseDrag(320, 340)


# -
app.background = gradient('lightSkyBlue', 'orange', start='top')

# sun and lake
Circle(250, 335, 50, fill='gold')
Rect(0, 300, 400, 100, fill='dodgerBlue')

# boat and fishing rod
Polygon(0, 270, 0, 350, 50, 350, 85, 315, 100, 270, fill='sienna')
Line(0, 240, 140, 160)

# fishing line, fish body, and fish tail
fishingLine = Line(140, 160, 140, 340, lineWidth=1)
fishBody = Oval(340, 340, 50, 30, fill='salmon')
fishTail = Polygon(345, 340, 380, 350, 380, 330, fill='salmon')

def pullUpFish():
    fishingLine.x2 = 140
    fishingLine.y2 = 225

    fishBody.rotateAngle = 90
    fishBody.centerX = 140
    fishBody.centerY = 250
    fishTail.rotateAngle = 90
    fishTail.centerX = 140
    fishTail.top = 255

def onKeyPress(key):
    # Release the fish if the correct key is pressed.
    if (key == 'r'):
        fishBody.rotateAngle = 0
        fishBody.centerX = 340
        fishBody.centerY = 340

        fishTail.rotateAngle = 0
        fishTail.left = 345
        fishTail.centerY = 340

def onMouseDrag(mouseX, mouseY):
    # If fish is very close to boat, pull it up.
    if (fishBody.centerX <= 165):
        pullUpFish()

    # If the line is behind fish, only move the line.
    elif (fishBody.centerX - mouseX < 0):
        fishingLine.x2 = mouseX
        fishingLine.y2 = mouseY

    # If the line is too far from fish, only move the line.
    elif (fishBody.centerX - mouseX > 80):
        fishingLine.x2 = mouseX
        fishingLine.y2 = mouseY

    # If the line is close enough to fish, the line should hook the fish.
    elif (mouseY > 300):
        fishingLine.x2 = mouseX
        fishingLine.y2 = mouseY

        fishBody.centerX = mouseX + 25
        fishBody.centerY = mouseY
        fishTail.centerX = mouseX + 50
        fishTail.centerY = mouseY

onMouseDrag(380, 380)

