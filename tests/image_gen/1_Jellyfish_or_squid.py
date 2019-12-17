app.background = rgb(55, 225, 205)
app.stepsPerSecond = 25

# body
outerHead = Oval(200, 300, 210, 220, fill=rgb(250, 200, 230))
animal = Oval(200, 300,  180, 200, fill=rgb(250, 220, 240))
animal.type = 'jellyfish'
Rect(95, 300, 210, 100, fill=rgb(55, 225, 205))

# tentacles
tentacles = Line(120, 340, 280, 340, fill=rgb(250, 220, 240), lineWidth=80,
                 dashes=(20, 15))

# eyes
Circle(155, 265, 10)
Circle(245, 265, 10)
Circle(155, 260, 5, fill='grey')
Circle(245, 260, 5, fill='grey')

# mouth
Circle(200, 265, 15, fill=rgb(250, 120, 180))
mouthCover = Rect(185, 250, 30, 15, fill=rgb(250, 220, 240))

# bubbles
bubble1 = Circle(120, 30, 40, fill=gradient('lightCyan', 'lavender'), opacity=20,
                 border=gradient('powderBlue', 'cornflowerBlue', start='top'))
bubble2 = Circle(120, 90, 30, fill=bubble1.fill, border=bubble1.border,
                 opacity=40)
bubble3 = Circle(120, 150, 20, fill=bubble1.fill, border=bubble1.border,
                 opacity=60)
bubble4 = Circle(120, 210, 10, fill=bubble1.fill, border=bubble1.border,
                 opacity=80)
bubble5 = Circle(120, 270, 1, fill=bubble1.fill, border=bubble1.border)

ink = Polygon(180, 300, 170, 335, 145, 375, 110, 400, 290, 400, 255, 375,
              230, 335, 220, 300, opacity=85, visible=False)

def moveBubble(bubble):
    bubble.centerY -= 3
    bubble.radius += 1
    bubble.opacity -= 1
    if (bubble.opacity <= 2):
        bubble.centerY = 270
        bubble.radius = 1
        bubble.opacity = 90

def onMousePress(mouseX, mouseY):
    if (animal.type == 'squid'):
        ink.visible = True
        tentacles.toFront()

def onKeyPress(key):
    # Define these local variables depending on what animal is showing.
    if (animal.type == 'jellyfish'):
        backColor = 'black'
        frontColor = 'dimGrey'
        animalHeight = 380
        animal.type = 'squid'
    else:
        backColor = rgb(250, 200, 230)
        frontColor = rgb(250, 220, 240)
        animalHeight = 200
        animal.type = 'jellyfish'
    # Uses the local variables to set the animal's properties.
    outerHead.fill = backColor
    outerHead.height = animalHeight + 20
    animal.fill = frontColor
    animal.height = animalHeight

    mouthCover.fill = frontColor
    tentacles.fill = frontColor

    ink.visible = False

def onStep():
    # Moves each of the bubbles and wrap them around when needed.
    moveBubble(bubble1)
    moveBubble(bubble2)
    moveBubble(bubble3)
    moveBubble(bubble4)
    moveBubble(bubble5)

onKeyPress('a')


# -
app.background = rgb(55, 225, 205)
app.stepsPerSecond = 25

# body
outerHead = Oval(200, 300, 210, 220, fill=rgb(250, 200, 230))
animal = Oval(200, 300,  180, 200, fill=rgb(250, 220, 240))
animal.type = 'jellyfish'
Rect(95, 300, 210, 100, fill=rgb(55, 225, 205))

# tentacles
tentacles = Line(120, 340, 280, 340, fill=rgb(250, 220, 240), lineWidth=80,
                 dashes=(20, 15))

# eyes
Circle(155, 265, 10)
Circle(245, 265, 10)
Circle(155, 260, 5, fill='grey')
Circle(245, 260, 5, fill='grey')

# mouth
Circle(200, 265, 15, fill=rgb(250, 120, 180))
mouthCover = Rect(185, 250, 30, 15, fill=rgb(250, 220, 240))

# bubbles
bubble1 = Circle(120, 30, 40, fill=gradient('lightCyan', 'lavender'), opacity=20,
                 border=gradient('powderBlue', 'cornflowerBlue', start='top'))
bubble2 = Circle(120, 90, 30, fill=bubble1.fill, border=bubble1.border,
                 opacity=40)
bubble3 = Circle(120, 150, 20, fill=bubble1.fill, border=bubble1.border,
                 opacity=60)
bubble4 = Circle(120, 210, 10, fill=bubble1.fill, border=bubble1.border,
                 opacity=80)
bubble5 = Circle(120, 270, 1, fill=bubble1.fill, border=bubble1.border)

ink = Polygon(180, 300, 170, 335, 145, 375, 110, 400, 290, 400, 255, 375,
              230, 335, 220, 300, opacity=85, visible=False)

def moveBubble(bubble):
    bubble.centerY -= 3
    bubble.radius += 1
    bubble.opacity -= 1
    if (bubble.opacity <= 2):
        bubble.centerY = 270
        bubble.radius = 1
        bubble.opacity = 90

def onMousePress(mouseX, mouseY):
    if (animal.type == 'squid'):
        ink.visible = True
        tentacles.toFront()

def onKeyPress(key):
    # Define these local variables depending on what animal is showing.
    if (animal.type == 'jellyfish'):
        backColor = 'black'
        frontColor = 'dimGrey'
        animalHeight = 380
        animal.type = 'squid'
    else:
        backColor = rgb(250, 200, 230)
        frontColor = rgb(250, 220, 240)
        animalHeight = 200
        animal.type = 'jellyfish'
    # Uses the local variables to set the animal's properties.
    outerHead.fill = backColor
    outerHead.height = animalHeight + 20
    animal.fill = frontColor
    animal.height = animalHeight

    mouthCover.fill = frontColor
    tentacles.fill = frontColor

    ink.visible = False

def onStep():
    # Moves each of the bubbles and wrap them around when needed.
    moveBubble(bubble1)
    moveBubble(bubble2)
    moveBubble(bubble3)
    moveBubble(bubble4)
    moveBubble(bubble5)

onKeyPress('space')
onKeyPress('space')
onKeyPress('space')


# -
app.background = rgb(55, 225, 205)
app.stepsPerSecond = 25

# body
outerHead = Oval(200, 300, 210, 220, fill=rgb(250, 200, 230))
animal = Oval(200, 300,  180, 200, fill=rgb(250, 220, 240))
animal.type = 'jellyfish'
Rect(95, 300, 210, 100, fill=rgb(55, 225, 205))

# tentacles
tentacles = Line(120, 340, 280, 340, fill=rgb(250, 220, 240), lineWidth=80,
                 dashes=(20, 15))

# eyes
Circle(155, 265, 10)
Circle(245, 265, 10)
Circle(155, 260, 5, fill='grey')
Circle(245, 260, 5, fill='grey')

# mouth
Circle(200, 265, 15, fill=rgb(250, 120, 180))
mouthCover = Rect(185, 250, 30, 15, fill=rgb(250, 220, 240))

# bubbles
bubble1 = Circle(120, 30, 40, fill=gradient('lightCyan', 'lavender'), opacity=20,
                 border=gradient('powderBlue', 'cornflowerBlue', start='top'))
bubble2 = Circle(120, 90, 30, fill=bubble1.fill, border=bubble1.border,
                 opacity=40)
bubble3 = Circle(120, 150, 20, fill=bubble1.fill, border=bubble1.border,
                 opacity=60)
bubble4 = Circle(120, 210, 10, fill=bubble1.fill, border=bubble1.border,
                 opacity=80)
bubble5 = Circle(120, 270, 1, fill=bubble1.fill, border=bubble1.border)

ink = Polygon(180, 300, 170, 335, 145, 375, 110, 400, 290, 400, 255, 375,
              230, 335, 220, 300, opacity=85, visible=False)

def moveBubble(bubble):
    bubble.centerY -= 3
    bubble.radius += 1
    bubble.opacity -= 1
    if (bubble.opacity <= 2):
        bubble.centerY = 270
        bubble.radius = 1
        bubble.opacity = 90

def onMousePress(mouseX, mouseY):
    if (animal.type == 'squid'):
        ink.visible = True
        tentacles.toFront()

def onKeyPress(key):
    # Define these local variables depending on what animal is showing.
    if (animal.type == 'jellyfish'):
        backColor = 'black'
        frontColor = 'dimGrey'
        animalHeight = 380
        animal.type = 'squid'
    else:
        backColor = rgb(250, 200, 230)
        frontColor = rgb(250, 220, 240)
        animalHeight = 200
        animal.type = 'jellyfish'
    # Uses the local variables to set the animal's properties.
    outerHead.fill = backColor
    outerHead.height = animalHeight + 20
    animal.fill = frontColor
    animal.height = animalHeight

    mouthCover.fill = frontColor
    tentacles.fill = frontColor

    ink.visible = False

def onStep():
    # Moves each of the bubbles and wrap them around when needed.
    moveBubble(bubble1)
    moveBubble(bubble2)
    moveBubble(bubble3)
    moveBubble(bubble4)
    moveBubble(bubble5)

onKeyPress('space')
onKeyPress('space')
onKeyPress('space')

