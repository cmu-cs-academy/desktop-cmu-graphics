app.background = 'black'
app.bubbleColors = [ 'mediumPurple', 'orchid', 'powderBlue', 'lightCoral',
                     'lightSalmon' ]

bubbles = Group()

def createBubbles():
    for i in range(10):
        bubbleColor = choice(app.bubbleColors)
        bubbleX = randrange(50, 350)
        bubbleY = randrange(50, 350)

        bubble = Group(
            Circle(bubbleX, bubbleY, 30, fill=None, border=bubbleColor),
            Oval(bubbleX - 18, bubbleY - 18, 4, 12, fill='white', rotateAngle=45)
            )
        bubble.dx = randrange(-3, 4)
        bubble.dy = randrange(2, 5)
        bubbles.add(bubble)

createBubbles()

def moveBubbles():
    # Moves each of the bubbles.
    for bubble in bubbles.children:
        bubble.centerX += bubble.dx
        bubble.centerY += bubble.dy

def checkWallCollision():
    # Checks if any of the bubbles collide with a wall and bounce off.
    for bubble in bubbles.children:
        if ((bubble.left < 0) or (bubble.right > 400)):
            bubble.dx = -bubble.dx
            bubble.centerX += bubble.dx
        if ((bubble.top < 0) or (bubble.bottom > 400)):
            bubble.dy = -bubble.dy
            bubble.centerY += bubble.dy

def onMouseMove(mouseX, mouseY):
    # Check to see if the mouse is on a bubble.
    bubble = bubbles.hitTest(mouseX, mouseY)
    if (bubble != None):
        # Reset the dx and dy of the bubble based on where the mouse is
        # hitting the bubble.
        if (mouseX < bubble.centerX):
            bubble.dx = 3
        else:
            bubble.dx = -3
        if (mouseY < bubble.centerY):
            bubble.dy = 3
        else:
            bubble.dy = -3
def onStep():
    moveBubbles()
    checkWallCollision()

bubble0 = bubbles.children[0]
onMouseMove(bubble0.centerX, bubble0.centerY + 30)
onSteps(20)
app.paused = True


# -
app.background = 'black'
app.bubbleColors = [ 'mediumPurple', 'orchid', 'powderBlue', 'lightCoral',
                     'lightSalmon' ]

bubbles = Group()

def createBubbles():
    for i in range(10):
        bubbleColor = choice(app.bubbleColors)
        bubbleX = randrange(50, 350)
        bubbleY = randrange(50, 350)

        bubble = Group(
            Circle(bubbleX, bubbleY, 30, fill=None, border=bubbleColor),
            Oval(bubbleX - 18, bubbleY - 18, 4, 12, fill='white', rotateAngle=45)
            )
        bubble.dx = randrange(-3, 4)
        bubble.dy = randrange(2, 5)
        bubbles.add(bubble)

createBubbles()

def moveBubbles():
    # Moves each of the bubbles.
    for bubble in bubbles.children:
        bubble.centerX += bubble.dx
        bubble.centerY += bubble.dy

def checkWallCollision():
    # Checks if any of the bubbles collide with a wall and bounce off.
    for bubble in bubbles.children:
        if ((bubble.left < 0) or (bubble.right > 400)):
            bubble.dx = -bubble.dx
            bubble.centerX += bubble.dx
        if ((bubble.top < 0) or (bubble.bottom > 400)):
            bubble.dy = -bubble.dy
            bubble.centerY += bubble.dy

def onMouseMove(mouseX, mouseY):
    # Check to see if the mouse is on a bubble.
    bubble = bubbles.hitTest(mouseX, mouseY)
    if (bubble != None):
        # Reset the dx and dy of the bubble based on where the mouse is
        # hitting the bubble.
        if (mouseX < bubble.centerX):
            bubble.dx = 3
        else:
            bubble.dx = -3
        if (mouseY < bubble.centerY):
            bubble.dy = 3
        else:
            bubble.dy = -3
def onStep():
    moveBubbles()
    checkWallCollision()

onSteps(20)
app.paused = True


# -
app.background = 'black'
app.bubbleColors = [ 'mediumPurple', 'orchid', 'powderBlue', 'lightCoral',
                     'lightSalmon' ]

bubbles = Group()

def createBubbles():
    for i in range(10):
        bubbleColor = choice(app.bubbleColors)
        bubbleX = randrange(50, 350)
        bubbleY = randrange(50, 350)

        bubble = Group(
            Circle(bubbleX, bubbleY, 30, fill=None, border=bubbleColor),
            Oval(bubbleX - 18, bubbleY - 18, 4, 12, fill='white', rotateAngle=45)
            )
        bubble.dx = randrange(-3, 4)
        bubble.dy = randrange(2, 5)
        bubbles.add(bubble)

createBubbles()

def moveBubbles():
    # Moves each of the bubbles.
    for bubble in bubbles.children:
        bubble.centerX += bubble.dx
        bubble.centerY += bubble.dy

def checkWallCollision():
    # Checks if any of the bubbles collide with a wall and bounce off.
    for bubble in bubbles.children:
        if ((bubble.left < 0) or (bubble.right > 400)):
            bubble.dx = -bubble.dx
            bubble.centerX += bubble.dx
        if ((bubble.top < 0) or (bubble.bottom > 400)):
            bubble.dy = -bubble.dy
            bubble.centerY += bubble.dy

def onMouseMove(mouseX, mouseY):
    # Check to see if the mouse is on a bubble.
    bubble = bubbles.hitTest(mouseX, mouseY)
    if (bubble != None):
        # Reset the dx and dy of the bubble based on where the mouse is
        # hitting the bubble.
        if (mouseX < bubble.centerX):
            bubble.dx = 3
        else:
            bubble.dx = -3
        if (mouseY < bubble.centerY):
            bubble.dy = 3
        else:
            bubble.dy = -3
def onStep():
    moveBubbles()
    checkWallCollision()

onSteps(20)
app.paused = True

