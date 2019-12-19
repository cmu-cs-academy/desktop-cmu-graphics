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

onMousePress(300, 100)


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

onMousePress(205, 50)

