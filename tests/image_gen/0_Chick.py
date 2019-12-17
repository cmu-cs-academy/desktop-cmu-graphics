speechBubble = Polygon(280, 110, 310, 95, 390, 95, 390, 45, 290, 45, 290, 95,
                       fill=None, border='black', visible=False)
speechText = Label('...', 340, 70, size=25, visible=False)

def drawEggBottom():
    Circle(200, 260, 100, fill='lightBlue')
    Rect(200, 260, 200, 120, fill='white', align='bottom')

def drawCrack():
    Polygon(100, 260, 120, 220, 150, 255, 175, 215, 200, 260, 220, 230,
            250, 260, 275, 210, 300, 260, fill='lightBlue', border='grey',
            borderWidth=1)
    Line(100, 260, 300, 260, fill='lightBlue')

def drawEggTop():
    Oval(200, 230, 205, 260, fill='lightBlue')

def drawBabyChicken():
    # beak
    Polygon(245, 115, 250, 145, 270, 130, fill='orange')

    # body
    Oval(200, 235, 140, 150, fill=rgb(255, 205, 0))
    Oval(200, 135, 105, 100, fill=rgb(255, 205, 0))

    # cover the bottom half of the body
    Rect(135, 260, 130, 75, fill='lightBlue')

    # eye
    Oval(235, 115, 20, 20)
    Circle(240, 110, 5, fill='aliceBlue')

def onMousePress(mouseX, mouseY):
    # Show the speechBubble with appropriate text.
    speechText.visible = True
    speechBubble.visible = True

def onMouseRelease(mouseX, mouseY):
    # Hide the speechBubble.
    speechText.visible = False
    speechBubble.visible = False

def HatchedOrNot(hasHatched):
    # Draw image and text based on whether it has hatched or not.
    if (hasHatched == True):
        drawEggBottom()
        drawBabyChicken()
        drawCrack()
        speechText.value = 'Peep!'
    else:
        drawEggBottom()
        drawEggTop()
        drawCrack()
        speechText.value = '...'

drawEggBottom()
drawEggTop()
drawCrack()


# -
speechBubble = Polygon(280, 110, 310, 95, 390, 95, 390, 45, 290, 45, 290, 95,
                       fill=None, border='black', visible=False)
speechText = Label('...', 340, 70, size=25, visible=False)

def drawEggBottom():
    Circle(200, 260, 100, fill='lightBlue')
    Rect(200, 260, 200, 120, fill='white', align='bottom')

def drawCrack():
    Polygon(100, 260, 120, 220, 150, 255, 175, 215, 200, 260, 220, 230,
            250, 260, 275, 210, 300, 260, fill='lightBlue', border='grey',
            borderWidth=1)
    Line(100, 260, 300, 260, fill='lightBlue')

def drawEggTop():
    Oval(200, 230, 205, 260, fill='lightBlue')

def drawBabyChicken():
    # beak
    Polygon(245, 115, 250, 145, 270, 130, fill='orange')

    # body
    Oval(200, 235, 140, 150, fill=rgb(255, 205, 0))
    Oval(200, 135, 105, 100, fill=rgb(255, 205, 0))

    # cover the bottom half of the body
    Rect(135, 260, 130, 75, fill='lightBlue')

    # eye
    Oval(235, 115, 20, 20)
    Circle(240, 110, 5, fill='aliceBlue')

def onMousePress(mouseX, mouseY):
    # Show the speechBubble with appropriate text.
    speechText.visible = True
    speechBubble.visible = True

def onMouseRelease(mouseX, mouseY):
    # Hide the speechBubble.
    speechText.visible = False
    speechBubble.visible = False

def HatchedOrNot(hasHatched):
    # Draw image and text based on whether it has hatched or not.
    if (hasHatched == True):
        drawEggBottom()
        drawBabyChicken()
        drawCrack()
        speechText.value = 'Peep!'
    else:
        drawEggBottom()
        drawEggTop()
        drawCrack()
        speechText.value = '...'

HatchedOrNot(False)
onMousePress(200, 200)


# -
speechBubble = Polygon(280, 110, 310, 95, 390, 95, 390, 45, 290, 45, 290, 95,
                       fill=None, border='black', visible=False)
speechText = Label('...', 340, 70, size=25, visible=False)

def drawEggBottom():
    Circle(200, 260, 100, fill='lightBlue')
    Rect(200, 260, 200, 120, fill='white', align='bottom')

def drawCrack():
    Polygon(100, 260, 120, 220, 150, 255, 175, 215, 200, 260, 220, 230,
            250, 260, 275, 210, 300, 260, fill='lightBlue', border='grey',
            borderWidth=1)
    Line(100, 260, 300, 260, fill='lightBlue')

def drawEggTop():
    Oval(200, 230, 205, 260, fill='lightBlue')

def drawBabyChicken():
    # beak
    Polygon(245, 115, 250, 145, 270, 130, fill='orange')

    # body
    Oval(200, 235, 140, 150, fill=rgb(255, 205, 0))
    Oval(200, 135, 105, 100, fill=rgb(255, 205, 0))

    # cover the bottom half of the body
    Rect(135, 260, 130, 75, fill='lightBlue')

    # eye
    Oval(235, 115, 20, 20)
    Circle(240, 110, 5, fill='aliceBlue')

def onMousePress(mouseX, mouseY):
    # Show the speechBubble with appropriate text.
    speechText.visible = True
    speechBubble.visible = True

def onMouseRelease(mouseX, mouseY):
    # Hide the speechBubble.
    speechText.visible = False
    speechBubble.visible = False

def HatchedOrNot(hasHatched):
    # Draw image and text based on whether it has hatched or not.
    if (hasHatched == True):
        drawEggBottom()
        drawBabyChicken()
        drawCrack()
        speechText.value = 'Peep!'
    else:
        drawEggBottom()
        drawEggTop()
        drawCrack()
        speechText.value = '...'

drawEggBottom()
drawEggTop()
drawCrack()

