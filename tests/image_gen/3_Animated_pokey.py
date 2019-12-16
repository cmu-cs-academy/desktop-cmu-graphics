app.background = gradient('skyBlue', 'orange', start='top')

app.stepsPerSecond = 10
app.steps = 0

# background
Rect(0, 275, 400, 125, fill='gold')
Polygon(140, 275, 240, 155, 290, 175, 330, 120, 465, 275, fill=rgb(235, 185, 0))
Polygon(0, 275, 60, 185, 100, 240, 135, 220, 190, 275, fill=rgb(255, 235, 60))

pokeys = Group()
pokeys.bodyPieceDx = 2
pokeyEyes = Group()
pokeyEyes.dy = 1

def drawPokeyFace(x, y):
    pokeyColor = gradient('gold', 'orange', start='left-top')
    head = Group(
        # head spikes
        RegularPolygon(x - 20, y - 15, 18, 3, fill=pokeyColor,
                       border='gainsboro', borderWidth=1, rotateAngle=-45),
        RegularPolygon(x, y - 25, 18, 3, fill=pokeyColor,
                       border='gainsboro', borderWidth=1),
        RegularPolygon(x + 20, y - 15, 18, 3, fill=pokeyColor,
                       border='gainsboro', borderWidth=1, rotateAngle=45),

        # head and eyes
        Circle(x, y, 30, fill=pokeyColor, border='black', borderWidth=1),
        Oval(x - 10, y - 5, 15, 18),
        Oval(x + 10, y - 5, 15, 18),

        # mouth
        Oval(x, y + 15, 30, 15),
        Oval(x, y + 10, 30, 10, fill=pokeyColor)
        )

    # eyes
    eye1 = Circle(x - 7, y - 7, 3, fill='white')
    eye2 = Circle(x + 7, y - 2, 3, fill='white')
    pokeyEyes.add(eye1, eye2)

    head.add(pokeyEyes)
    pokeys.add(head)

def drawPokeyBodyPiece(x, y):
    pokeyColor = gradient('gold', 'orange', start='left-top')
    bodyPiece = Group(
        # whiskers
        Line(x - 25, y + 25, x + 25, y - 25),
        Line(x - 25, y - 25, x + 25, y + 25),

        # spikes and body
        RegularPolygon(x - 30, y - 5, 12, 3, fill=pokeyColor,
                       border='gainsboro', borderWidth=1, rotateAngle=35),
        RegularPolygon(x + 30, y + 5, 15, 3, fill=pokeyColor,
                       border='gainsboro', borderWidth=1, rotateAngle=-25),

        # body
        Circle(x, y, 30, fill=pokeyColor, border='black', borderWidth=1)
        )

    pokeys.add(bodyPiece)

def onStep():
    # Every 5 steps, switches the direction of the eyes and body pieces.
    if (app.steps == 5):
        pokeys.bodyPieceDx *= -1
        pokeyEyes.dy *= -1
        app.steps = 0

    # Sway each body piece side to side, alternating the direction of the
    # movement.
    dx = pokeys.bodyPieceDx
    for pokeyPiece in pokeys.children:
        pokeyPiece.centerX += dx
        dx *= -1
    # Move the eyes up and down, alternating the direction each eye moves.
    dy = pokeyEyes.dy
    for pokeyEye in pokeyEyes.children:
        pokeyEye.centerY += dy
        dy *= -1
    app.steps += 1


drawPokeyBodyPiece(195, 300)
drawPokeyFace(205, 235)


# -
app.background = gradient('skyBlue', 'orange', start='top')

app.stepsPerSecond = 10
app.steps = 0

# background
Rect(0, 275, 400, 125, fill='gold')
Polygon(140, 275, 240, 155, 290, 175, 330, 120, 465, 275, fill=rgb(235, 185, 0))
Polygon(0, 275, 60, 185, 100, 240, 135, 220, 190, 275, fill=rgb(255, 235, 60))

pokeys = Group()
pokeys.bodyPieceDx = 2
pokeyEyes = Group()
pokeyEyes.dy = 1

def drawPokeyFace(x, y):
    pokeyColor = gradient('gold', 'orange', start='left-top')
    head = Group(
        # head spikes
        RegularPolygon(x - 20, y - 15, 18, 3, fill=pokeyColor,
                       border='gainsboro', borderWidth=1, rotateAngle=-45),
        RegularPolygon(x, y - 25, 18, 3, fill=pokeyColor,
                       border='gainsboro', borderWidth=1),
        RegularPolygon(x + 20, y - 15, 18, 3, fill=pokeyColor,
                       border='gainsboro', borderWidth=1, rotateAngle=45),

        # head and eyes
        Circle(x, y, 30, fill=pokeyColor, border='black', borderWidth=1),
        Oval(x - 10, y - 5, 15, 18),
        Oval(x + 10, y - 5, 15, 18),

        # mouth
        Oval(x, y + 15, 30, 15),
        Oval(x, y + 10, 30, 10, fill=pokeyColor)
        )

    # eyes
    eye1 = Circle(x - 7, y - 7, 3, fill='white')
    eye2 = Circle(x + 7, y - 2, 3, fill='white')
    pokeyEyes.add(eye1, eye2)

    head.add(pokeyEyes)
    pokeys.add(head)

def drawPokeyBodyPiece(x, y):
    pokeyColor = gradient('gold', 'orange', start='left-top')
    bodyPiece = Group(
        # whiskers
        Line(x - 25, y + 25, x + 25, y - 25),
        Line(x - 25, y - 25, x + 25, y + 25),

        # spikes and body
        RegularPolygon(x - 30, y - 5, 12, 3, fill=pokeyColor,
                       border='gainsboro', borderWidth=1, rotateAngle=35),
        RegularPolygon(x + 30, y + 5, 15, 3, fill=pokeyColor,
                       border='gainsboro', borderWidth=1, rotateAngle=-25),

        # body
        Circle(x, y, 30, fill=pokeyColor, border='black', borderWidth=1)
        )

    pokeys.add(bodyPiece)

def onStep():
    # Every 5 steps, switches the direction of the eyes and body pieces.
    if (app.steps == 5):
        pokeys.bodyPieceDx *= -1
        pokeyEyes.dy *= -1
        app.steps = 0

    # Sway each body piece side to side, alternating the direction of the
    # movement.
    dx = pokeys.bodyPieceDx
    for pokeyPiece in pokeys.children:
        pokeyPiece.centerX += dx
        dx *= -1
    # Move the eyes up and down, alternating the direction each eye moves.
    dy = pokeyEyes.dy
    for pokeyEye in pokeyEyes.children:
        pokeyEye.centerY += dy
        dy *= -1
    app.steps += 1




# -
app.background = gradient('skyBlue', 'orange', start='top')

app.stepsPerSecond = 10
app.steps = 0

# background
Rect(0, 275, 400, 125, fill='gold')
Polygon(140, 275, 240, 155, 290, 175, 330, 120, 465, 275, fill=rgb(235, 185, 0))
Polygon(0, 275, 60, 185, 100, 240, 135, 220, 190, 275, fill=rgb(255, 235, 60))

pokeys = Group()
pokeys.bodyPieceDx = 2
pokeyEyes = Group()
pokeyEyes.dy = 1

def drawPokeyFace(x, y):
    pokeyColor = gradient('gold', 'orange', start='left-top')
    head = Group(
        # head spikes
        RegularPolygon(x - 20, y - 15, 18, 3, fill=pokeyColor,
                       border='gainsboro', borderWidth=1, rotateAngle=-45),
        RegularPolygon(x, y - 25, 18, 3, fill=pokeyColor,
                       border='gainsboro', borderWidth=1),
        RegularPolygon(x + 20, y - 15, 18, 3, fill=pokeyColor,
                       border='gainsboro', borderWidth=1, rotateAngle=45),

        # head and eyes
        Circle(x, y, 30, fill=pokeyColor, border='black', borderWidth=1),
        Oval(x - 10, y - 5, 15, 18),
        Oval(x + 10, y - 5, 15, 18),

        # mouth
        Oval(x, y + 15, 30, 15),
        Oval(x, y + 10, 30, 10, fill=pokeyColor)
        )

    # eyes
    eye1 = Circle(x - 7, y - 7, 3, fill='white')
    eye2 = Circle(x + 7, y - 2, 3, fill='white')
    pokeyEyes.add(eye1, eye2)

    head.add(pokeyEyes)
    pokeys.add(head)

def drawPokeyBodyPiece(x, y):
    pokeyColor = gradient('gold', 'orange', start='left-top')
    bodyPiece = Group(
        # whiskers
        Line(x - 25, y + 25, x + 25, y - 25),
        Line(x - 25, y - 25, x + 25, y + 25),

        # spikes and body
        RegularPolygon(x - 30, y - 5, 12, 3, fill=pokeyColor,
                       border='gainsboro', borderWidth=1, rotateAngle=35),
        RegularPolygon(x + 30, y + 5, 15, 3, fill=pokeyColor,
                       border='gainsboro', borderWidth=1, rotateAngle=-25),

        # body
        Circle(x, y, 30, fill=pokeyColor, border='black', borderWidth=1)
        )

    pokeys.add(bodyPiece)

def onStep():
    # Every 5 steps, switches the direction of the eyes and body pieces.
    if (app.steps == 5):
        pokeys.bodyPieceDx *= -1
        pokeyEyes.dy *= -1
        app.steps = 0

    # Sway each body piece side to side, alternating the direction of the
    # movement.
    dx = pokeys.bodyPieceDx
    for pokeyPiece in pokeys.children:
        pokeyPiece.centerX += dx
        dx *= -1
    # Move the eyes up and down, alternating the direction each eye moves.
    dy = pokeyEyes.dy
    for pokeyEye in pokeyEyes.children:
        pokeyEye.centerY += dy
        dy *= -1
    app.steps += 1


drawPokeyBodyPiece(195, 320)
drawPokeyBodyPiece(205, 255)
drawPokeyFace(195, 190)
drawPokeyBodyPiece(105, 320)
drawPokeyFace(95, 255)
drawPokeyBodyPiece(305, 320)
drawPokeyBodyPiece(295, 255)
drawPokeyBodyPiece(305, 190)
drawPokeyFace(295, 125)
onSteps(10)
app.paused = True

