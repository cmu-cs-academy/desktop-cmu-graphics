# background
Rect(0, 0, 400, 400, fill='lightSkyBlue')

# string
Line(200, 330, 200, 400, fill='white', lineWidth=5, dashes=True)

# balloon
RegularPolygon(200, 370, 20, 3, fill='crimson')
Oval(200, 185, 300, 340,
     fill=gradient('lightCoral', 'crimson', start='right-top'))

def onMousePress(mouseX, mouseY):
    # Draw the pin.
    Line(mouseX, mouseY, mouseX + 40, mouseY - 20, lineWidth=1)
    Circle(mouseX + 40, mouseY - 20, 5, fill='blue')
def onMouseRelease(mouseX, mouseY):
    # Pop the balloon.
    Star(200, 200, 210, 9, fill='grey', roundness=10)
    Star(200, 200, 190, 9, fill='lightSkyBlue', roundness=70)

onMousePress(200, 200)
onMouseRelease(100, 100)
onMousePress(150, 250)
onMouseRelease(300, 150)
onMousePress(280, 280)
onMouseRelease(300, 200)


# -
# background
Rect(0, 0, 400, 400, fill='lightSkyBlue')

# string
Line(200, 330, 200, 400, fill='white', lineWidth=5, dashes=True)

# balloon
RegularPolygon(200, 370, 20, 3, fill='crimson')
Oval(200, 185, 300, 340,
     fill=gradient('lightCoral', 'crimson', start='right-top'))

def onMousePress(mouseX, mouseY):
    # Draw the pin.
    Line(mouseX, mouseY, mouseX + 40, mouseY - 20, lineWidth=1)
    Circle(mouseX + 40, mouseY - 20, 5, fill='blue')
def onMouseRelease(mouseX, mouseY):
    # Pop the balloon.
    Star(200, 200, 210, 9, fill='grey', roundness=10)
    Star(200, 200, 190, 9, fill='lightSkyBlue', roundness=70)

onMousePress(200, 200)


# -
# background
Rect(0, 0, 400, 400, fill='lightSkyBlue')

# string
Line(200, 330, 200, 400, fill='white', lineWidth=5, dashes=True)

# balloon
RegularPolygon(200, 370, 20, 3, fill='crimson')
Oval(200, 185, 300, 340,
     fill=gradient('lightCoral', 'crimson', start='right-top'))

def onMousePress(mouseX, mouseY):
    # Draw the pin.
    Line(mouseX, mouseY, mouseX + 40, mouseY - 20, lineWidth=1)
    Circle(mouseX + 40, mouseY - 20, 5, fill='blue')
def onMouseRelease(mouseX, mouseY):
    # Pop the balloon.
    Star(200, 200, 210, 9, fill='grey', roundness=10)
    Star(200, 200, 190, 9, fill='lightSkyBlue', roundness=70)

onMousePress(200, 200)
onMouseRelease(100, 100)
onMousePress(150, 250)
onMouseRelease(300, 150)
onMousePress(280, 280)
onMouseRelease(300, 200)

