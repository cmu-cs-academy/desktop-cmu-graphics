app.background = 'black'

lines = Group()
Circle(200, 200, 125, fill=None, border='lime')

def makeCone(numberOfLines):
    stepAngle = 360 / numberOfLines
    for i in range(numberOfLines):
        # Define the angle variable so it equals 'i' times the stepAngle.
        angle = i * stepAngle
        # Define the getPointInDir function 'centered' so it uses a radius of 125.
        x1, y1 = getPointInDir(200, 200, angle, 125)
        # Adds a new line to the group lines using the variables defined.
        lines.add(
            Line(x1, y1, 200, 200, fill='lime')
            )

def onMouseMove(mouseX, mouseY):
    # Loop through each line in the group lines and set their x2, y2 to the
    # mouseX, mouseY.
    for line in lines:
        line.x2 = mouseX
        line.y2 = mouseY

makeCone(10)
onMouseMove(50, 350)


# -
app.background = 'black'

lines = Group()
Circle(200, 200, 125, fill=None, border='lime')

def makeCone(numberOfLines):
    stepAngle = 360 / numberOfLines
    for i in range(numberOfLines):
        # Define the angle variable so it equals 'i' times the stepAngle.
        angle = i * stepAngle
        # Define the getPointInDir function 'centered' so it uses a radius of 125.
        x1, y1 = getPointInDir(200, 200, angle, 125)
        # Adds a new line to the group lines using the variables defined.
        lines.add(
            Line(x1, y1, 200, 200, fill='lime')
            )

def onMouseMove(mouseX, mouseY):
    # Loop through each line in the group lines and set their x2, y2 to the
    # mouseX, mouseY.
    for line in lines:
        line.x2 = mouseX
        line.y2 = mouseY

makeCone(20)
onMouseMove(140, 220)
onMouseMove(250, 300)


# -
app.background = 'black'

lines = Group()
Circle(200, 200, 125, fill=None, border='lime')

def makeCone(numberOfLines):
    stepAngle = 360 / numberOfLines
    for i in range(numberOfLines):
        # Define the angle variable so it equals 'i' times the stepAngle.
        angle = i * stepAngle
        # Define the getPointInDir function 'centered' so it uses a radius of 125.
        x1, y1 = getPointInDir(200, 200, angle, 125)
        # Adds a new line to the group lines using the variables defined.
        lines.add(
            Line(x1, y1, 200, 200, fill='lime')
            )

def onMouseMove(mouseX, mouseY):
    # Loop through each line in the group lines and set their x2, y2 to the
    # mouseX, mouseY.
    for line in lines:
        line.x2 = mouseX
        line.y2 = mouseY

makeCone(20)
onMouseMove(140, 220)
onMouseMove(250, 300)

