# background
Rect(190, 0, 10, 400)
Rect(200, 0, 10, 400, fill='brown')

def drawFootstep(x, y, color):
    Oval(x, y - 5, 22, 40, fill=color)
    Circle(x, y + 20, 8, fill=color)
    Rect(x, y + 13, 16, 3, fill='white', align='center')

def onMousePress(mouseX, mouseY):
    # Draw a black footstep if the click is on left half, brown footstep otherwise.
    if (mouseX < 200):
        drawFootstep(mouseX, mouseY, 'black')
    else:
        drawFootstep(mouseX, mouseY, 'brown')

onMousePress(100, 100)
onMousePress(70, 120)
onMousePress(100, 300)
onMousePress(70, 320)
onMousePress(300, 200)
onMousePress(270, 220)


# -
# background
Rect(190, 0, 10, 400)
Rect(200, 0, 10, 400, fill='brown')

def drawFootstep(x, y, color):
    Oval(x, y - 5, 22, 40, fill=color)
    Circle(x, y + 20, 8, fill=color)
    Rect(x, y + 13, 16, 3, fill='white', align='center')

def onMousePress(mouseX, mouseY):
    # Draw a black footstep if the click is on left half, brown footstep otherwise.
    if (mouseX < 200):
        drawFootstep(mouseX, mouseY, 'black')
    else:
        drawFootstep(mouseX, mouseY, 'brown')

onMousePress(100, 100)
onMousePress(70, 120)
onMousePress(100, 300)
onMousePress(70, 320)
onMousePress(300, 200)
onMousePress(270, 220)


# -
# background
Rect(190, 0, 10, 400)
Rect(200, 0, 10, 400, fill='brown')

def drawFootstep(x, y, color):
    Oval(x, y - 5, 22, 40, fill=color)
    Circle(x, y + 20, 8, fill=color)
    Rect(x, y + 13, 16, 3, fill='white', align='center')

def onMousePress(mouseX, mouseY):
    # Draw a black footstep if the click is on left half, brown footstep otherwise.
    if (mouseX < 200):
        drawFootstep(mouseX, mouseY, 'black')
    else:
        drawFootstep(mouseX, mouseY, 'brown')

onMousePress(100, 100)
onMousePress(50, 200)
onMousePress(150, 300)

