app.background = 'darkSlateBlue'

path = Polygon(150, 230, 150, 380, 20, 380, 20, 250, 0, 250, 0, 200, 70, 200,
               70, 310, 90, 310, 90, 180, 20, 180, 20, 20, 130, 20, 130, 120,
               150, 120, 150, 20, 300, 20, 300, 220, 320, 220, 320, 20, 380, 20,
               380, 380, 170, 380, 170, 250, 220, 250, 220, 320, 330, 320,
               330, 300, 240, 300, 240, 100, 220, 100, 220, 230, fill='white')

Polygon(0, 220, 0, 230, 20, 230, 20, 240, 35, 225, 20, 210, 20, 220,
        fill='deepSkyBlue')
greenStar = Star(195, 280, 20, 5, fill='springGreen')

def drawEndScreen(boxColor, message, messageColor):
    Rect(55, 155, 290, 90, fill=boxColor, border=messageColor, borderWidth=10)
    Label(message, 200, 200, fill=messageColor, size=40)
    app.stop()

def onMouseMove(mouseX, mouseY):
    # If the mouse is not on path, you lose the game.
    # If you reach the gree star, you win the game.
    if (path.contains(mouseX, mouseY) == False):
        drawEndScreen('lavender', 'GAME OVER!', 'red')
    elif (greenStar.contains(mouseX, mouseY) == True):
        drawEndScreen('honeydew', 'YOU WIN!', 'green')

onMouseMove(195, 280)


# -
app.background = 'darkSlateBlue'

path = Polygon(150, 230, 150, 380, 20, 380, 20, 250, 0, 250, 0, 200, 70, 200,
               70, 310, 90, 310, 90, 180, 20, 180, 20, 20, 130, 20, 130, 120,
               150, 120, 150, 20, 300, 20, 300, 220, 320, 220, 320, 20, 380, 20,
               380, 380, 170, 380, 170, 250, 220, 250, 220, 320, 330, 320,
               330, 300, 240, 300, 240, 100, 220, 100, 220, 230, fill='white')

Polygon(0, 220, 0, 230, 20, 230, 20, 240, 35, 225, 20, 210, 20, 220,
        fill='deepSkyBlue')
greenStar = Star(195, 280, 20, 5, fill='springGreen')

def drawEndScreen(boxColor, message, messageColor):
    Rect(55, 155, 290, 90, fill=boxColor, border=messageColor, borderWidth=10)
    Label(message, 200, 200, fill=messageColor, size=40)
    app.stop()

def onMouseMove(mouseX, mouseY):
    # If the mouse is not on path, you lose the game.
    # If you reach the gree star, you win the game.
    if (path.contains(mouseX, mouseY) == False):
        drawEndScreen('lavender', 'GAME OVER!', 'red')
    elif (greenStar.contains(mouseX, mouseY) == True):
        drawEndScreen('honeydew', 'YOU WIN!', 'green')

onMouseMove(50, 250)


# -
app.background = 'darkSlateBlue'

path = Polygon(150, 230, 150, 380, 20, 380, 20, 250, 0, 250, 0, 200, 70, 200,
               70, 310, 90, 310, 90, 180, 20, 180, 20, 20, 130, 20, 130, 120,
               150, 120, 150, 20, 300, 20, 300, 220, 320, 220, 320, 20, 380, 20,
               380, 380, 170, 380, 170, 250, 220, 250, 220, 320, 330, 320,
               330, 300, 240, 300, 240, 100, 220, 100, 220, 230, fill='white')

Polygon(0, 220, 0, 230, 20, 230, 20, 240, 35, 225, 20, 210, 20, 220,
        fill='deepSkyBlue')
greenStar = Star(195, 280, 20, 5, fill='springGreen')

def drawEndScreen(boxColor, message, messageColor):
    Rect(55, 155, 290, 90, fill=boxColor, border=messageColor, borderWidth=10)
    Label(message, 200, 200, fill=messageColor, size=40)
    app.stop()

def onMouseMove(mouseX, mouseY):
    # If the mouse is not on path, you lose the game.
    # If you reach the gree star, you win the game.
    if (path.contains(mouseX, mouseY) == False):
        drawEndScreen('lavender', 'GAME OVER!', 'red')
    elif (greenStar.contains(mouseX, mouseY) == True):
        drawEndScreen('honeydew', 'YOU WIN!', 'green')

onMouseMove(195, 280)
onMouseMove(200, 350)

