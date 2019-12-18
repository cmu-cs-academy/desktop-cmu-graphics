app.background = gradient('yellow', 'crimson', start='top')
app.stepsPerSecond = 20

# window
Line(200, 0, 200, 400, lineWidth=4)
Line(0, 200, 400, 200, lineWidth=4)
Rect(0, 0, 400, 400, fill=None, border='black', borderWidth=10)

# table
Rect(100, 375, 200, 10)
Rect(100, 385, 10, 15)
Rect(290, 385, 10, 15)

# Initialize empty blob group.
blobs = Group()

def createBlobs():
    newBlobRadius = 5
    newBlobX = 160
    newBlobSpeed = 6

    # Creates 6 blobs that increase in size and decrease in speed.
    for i in range(6):
        blob = Circle(newBlobX, 200, newBlobRadius, fill='red', opacity=90)
        blob.dy = newBlobSpeed
        blobs.add(blob)

        newBlobRadius += 5
        newBlobX += 10
        newBlobSpeed -= 1

# Populates the blob group.
createBlobs()

# lamp
Oval(200, 200, 130, 300, fill=gradient('yellow', 'red'), opacity=65)
Oval(200, 200, 130, 300, fill=None, border='black')
Polygon(150, 100, 175, 50, 225, 50, 250, 100,
        fill=gradient('orange', 'fireBrick', start='left'), border='black')
Polygon(150, 300, 175, 350, 225, 350, 250, 300,
        fill=gradient('orange', 'fireBrick', start='left'), border='black')
Polygon(175, 350, 160, 375, 240, 375, 225, 350,
        fill=gradient('orange', 'fireBrick', start='left'), border='black')

def onStep():
    # Move each blob based off of the speed defined in createBlobs(),
    # and bounce it when it reaches the bounds of the lamp.
    for blob in blobs.children:
        blob.centerY += blob.dy
        if ((blob.centerY + blob.radius > 300) or
            (blob.centerY - blob.radius < 100)):
            blob.dy *= -1



# -
app.background = gradient('yellow', 'crimson', start='top')
app.stepsPerSecond = 20

# window
Line(200, 0, 200, 400, lineWidth=4)
Line(0, 200, 400, 200, lineWidth=4)
Rect(0, 0, 400, 400, fill=None, border='black', borderWidth=10)

# table
Rect(100, 375, 200, 10)
Rect(100, 385, 10, 15)
Rect(290, 385, 10, 15)

# Initialize empty blob group.
blobs = Group()

def createBlobs():
    newBlobRadius = 5
    newBlobX = 160
    newBlobSpeed = 6

    # Creates 6 blobs that increase in size and decrease in speed.
    for i in range(6):
        blob = Circle(newBlobX, 200, newBlobRadius, fill='red', opacity=90)
        blob.dy = newBlobSpeed
        blobs.add(blob)

        newBlobRadius += 5
        newBlobX += 10
        newBlobSpeed -= 1

# Populates the blob group.
createBlobs()

# lamp
Oval(200, 200, 130, 300, fill=gradient('yellow', 'red'), opacity=65)
Oval(200, 200, 130, 300, fill=None, border='black')
Polygon(150, 100, 175, 50, 225, 50, 250, 100,
        fill=gradient('orange', 'fireBrick', start='left'), border='black')
Polygon(150, 300, 175, 350, 225, 350, 250, 300,
        fill=gradient('orange', 'fireBrick', start='left'), border='black')
Polygon(175, 350, 160, 375, 240, 375, 225, 350,
        fill=gradient('orange', 'fireBrick', start='left'), border='black')

def onStep():
    # Move each blob based off of the speed defined in createBlobs(),
    # and bounce it when it reaches the bounds of the lamp.
    for blob in blobs.children:
        blob.centerY += blob.dy
        if ((blob.centerY + blob.radius > 300) or
            (blob.centerY - blob.radius < 100)):
            blob.dy *= -1

onSteps(5)
app.paused = True


# -
app.background = gradient('yellow', 'crimson', start='top')
app.stepsPerSecond = 20

# window
Line(200, 0, 200, 400, lineWidth=4)
Line(0, 200, 400, 200, lineWidth=4)
Rect(0, 0, 400, 400, fill=None, border='black', borderWidth=10)

# table
Rect(100, 375, 200, 10)
Rect(100, 385, 10, 15)
Rect(290, 385, 10, 15)

# Initialize empty blob group.
blobs = Group()

def createBlobs():
    newBlobRadius = 5
    newBlobX = 160
    newBlobSpeed = 6

    # Creates 6 blobs that increase in size and decrease in speed.
    for i in range(6):
        blob = Circle(newBlobX, 200, newBlobRadius, fill='red', opacity=90)
        blob.dy = newBlobSpeed
        blobs.add(blob)

        newBlobRadius += 5
        newBlobX += 10
        newBlobSpeed -= 1

# Populates the blob group.
createBlobs()

# lamp
Oval(200, 200, 130, 300, fill=gradient('yellow', 'red'), opacity=65)
Oval(200, 200, 130, 300, fill=None, border='black')
Polygon(150, 100, 175, 50, 225, 50, 250, 100,
        fill=gradient('orange', 'fireBrick', start='left'), border='black')
Polygon(150, 300, 175, 350, 225, 350, 250, 300,
        fill=gradient('orange', 'fireBrick', start='left'), border='black')
Polygon(175, 350, 160, 375, 240, 375, 225, 350,
        fill=gradient('orange', 'fireBrick', start='left'), border='black')

def onStep():
    # Move each blob based off of the speed defined in createBlobs(),
    # and bounce it when it reaches the bounds of the lamp.
    for blob in blobs.children:
        blob.centerY += blob.dy
        if ((blob.centerY + blob.radius > 300) or
            (blob.centerY - blob.radius < 100)):
            blob.dy *= -1


