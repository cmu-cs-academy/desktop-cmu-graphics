app.background = gradient(rgb(0, 30, 70), 'black')
app.stepsPerSecond = 15

tardis = Group(
    Rect(200, 390, 200, 20, fill=rgb(55, 105, 155), border=rgb(0, 30, 70),
         borderWidth=4, align='center'),
    Rect(200, 245, 180, 270, fill=rgb(55, 105, 155), border=rgb(0, 30, 70),
         borderWidth=4, align='center'),
    Rect(200, 255, 140, 250, fill=rgb(55, 105, 155), border=rgb(0, 30, 70),
         borderWidth=4, align='center'),
    Rect(200, 95, 200, 40, fill=rgb(55, 105, 155), border=rgb(0, 30, 70),
         borderWidth=4, align='center'),

    # frame
    Rect(200, 95, 180, 25, align='center'),
    Rect(200, 75, 180, 10, fill=rgb(55, 105, 155), border=rgb(0, 30, 70),
         borderWidth=4, align='center'),
    Polygon(120, 70, 120, 50, 190, 30, 210, 30, 280, 50, 280, 70,
            fill=rgb(55, 105, 155), border=rgb(0, 30, 70)),
    Rect(200, 20, 20, 15, fill='lightYellow', border=rgb(0, 30, 70),
         borderWidth=3, align='center'),
    Polygon(185, 10, 200, 0, 215, 10, fill=rgb(55, 105, 155),
            border=rgb(0, 30, 70)),

    # top windows
    Rect(145, 150, 50, 50, fill='lightYellow', border=rgb(0, 30, 70)),
    Rect(205, 150, 50, 50, fill='lightYellow', border=rgb(0, 30, 70)),
    Line(170, 150, 170, 200, fill=rgb(0, 30, 70)),
    Line(230, 150, 230, 200, fill=rgb(0, 30, 70)),
    Line(145, 175, 195, 175, fill=rgb(0, 30, 70)),
    Line(205, 175, 255, 175, fill=rgb(0, 30, 70)),

    # more windows
    Rect(145, 210, 45, 50, fill=None, border=rgb(0, 30, 70)),
    Rect(150, 215, 35, 40, fill='gainsboro', border=rgb(0, 30, 70)),
    Rect(210, 210, 45, 50, fill=None, border=rgb(0, 30, 70)),
    Rect(145, 270, 45, 50, fill=None, border=rgb(0, 30, 70)),
    Rect(210, 270, 45, 50, fill=None, border=rgb(0, 30, 70)),
    Rect(145, 330, 45, 40, fill=None, border=rgb(0, 30, 70)),
    Rect(210, 330, 45, 40, fill=None, border=rgb(0, 30, 70))
    )


def onStep():
    # Move the Tardis right by 25 pixels, rotate it clockwise 5 degrees, and
    # increase the size by 5.
    tardis.centerX += 25
    tardis.rotateAngle += 5
    tardis.width += 5
    tardis.height += 5
    # If the width of the Tardis reaches 400 pixels make the Tardis upright,
    # reset the width and height to 25 and 50, and center the Tardis
    # vertically in the canvas.
    if (tardis.width >= 400):
        tardis.rotateAngle = 0
        tardis.width = 25
        tardis.height = 50
        tardis.centerY = 200
    # Implement wraparound.
    if (tardis.left > 400):
        tardis.right = 0

onStep()
app.paused = True


# -
app.background = gradient(rgb(0, 30, 70), 'black')
app.stepsPerSecond = 15

tardis = Group(
    Rect(200, 390, 200, 20, fill=rgb(55, 105, 155), border=rgb(0, 30, 70),
         borderWidth=4, align='center'),
    Rect(200, 245, 180, 270, fill=rgb(55, 105, 155), border=rgb(0, 30, 70),
         borderWidth=4, align='center'),
    Rect(200, 255, 140, 250, fill=rgb(55, 105, 155), border=rgb(0, 30, 70),
         borderWidth=4, align='center'),
    Rect(200, 95, 200, 40, fill=rgb(55, 105, 155), border=rgb(0, 30, 70),
         borderWidth=4, align='center'),

    # frame
    Rect(200, 95, 180, 25, align='center'),
    Rect(200, 75, 180, 10, fill=rgb(55, 105, 155), border=rgb(0, 30, 70),
         borderWidth=4, align='center'),
    Polygon(120, 70, 120, 50, 190, 30, 210, 30, 280, 50, 280, 70,
            fill=rgb(55, 105, 155), border=rgb(0, 30, 70)),
    Rect(200, 20, 20, 15, fill='lightYellow', border=rgb(0, 30, 70),
         borderWidth=3, align='center'),
    Polygon(185, 10, 200, 0, 215, 10, fill=rgb(55, 105, 155),
            border=rgb(0, 30, 70)),

    # top windows
    Rect(145, 150, 50, 50, fill='lightYellow', border=rgb(0, 30, 70)),
    Rect(205, 150, 50, 50, fill='lightYellow', border=rgb(0, 30, 70)),
    Line(170, 150, 170, 200, fill=rgb(0, 30, 70)),
    Line(230, 150, 230, 200, fill=rgb(0, 30, 70)),
    Line(145, 175, 195, 175, fill=rgb(0, 30, 70)),
    Line(205, 175, 255, 175, fill=rgb(0, 30, 70)),

    # more windows
    Rect(145, 210, 45, 50, fill=None, border=rgb(0, 30, 70)),
    Rect(150, 215, 35, 40, fill='gainsboro', border=rgb(0, 30, 70)),
    Rect(210, 210, 45, 50, fill=None, border=rgb(0, 30, 70)),
    Rect(145, 270, 45, 50, fill=None, border=rgb(0, 30, 70)),
    Rect(210, 270, 45, 50, fill=None, border=rgb(0, 30, 70)),
    Rect(145, 330, 45, 40, fill=None, border=rgb(0, 30, 70)),
    Rect(210, 330, 45, 40, fill=None, border=rgb(0, 30, 70))
    )


def onStep():
    # Move the Tardis right by 25 pixels, rotate it clockwise 5 degrees, and
    # increase the size by 5.
    tardis.centerX += 25
    tardis.rotateAngle += 5
    tardis.width += 5
    tardis.height += 5
    # If the width of the Tardis reaches 400 pixels make the Tardis upright,
    # reset the width and height to 25 and 50, and center the Tardis
    # vertically in the canvas.
    if (tardis.width >= 400):
        tardis.rotateAngle = 0
        tardis.width = 25
        tardis.height = 50
        tardis.centerY = 200
    # Implement wraparound.
    if (tardis.left > 400):
        tardis.right = 0

onSteps(250)
app.paused = True


# -
app.background = gradient(rgb(0, 30, 70), 'black')
app.stepsPerSecond = 15

tardis = Group(
    Rect(200, 390, 200, 20, fill=rgb(55, 105, 155), border=rgb(0, 30, 70),
         borderWidth=4, align='center'),
    Rect(200, 245, 180, 270, fill=rgb(55, 105, 155), border=rgb(0, 30, 70),
         borderWidth=4, align='center'),
    Rect(200, 255, 140, 250, fill=rgb(55, 105, 155), border=rgb(0, 30, 70),
         borderWidth=4, align='center'),
    Rect(200, 95, 200, 40, fill=rgb(55, 105, 155), border=rgb(0, 30, 70),
         borderWidth=4, align='center'),

    # frame
    Rect(200, 95, 180, 25, align='center'),
    Rect(200, 75, 180, 10, fill=rgb(55, 105, 155), border=rgb(0, 30, 70),
         borderWidth=4, align='center'),
    Polygon(120, 70, 120, 50, 190, 30, 210, 30, 280, 50, 280, 70,
            fill=rgb(55, 105, 155), border=rgb(0, 30, 70)),
    Rect(200, 20, 20, 15, fill='lightYellow', border=rgb(0, 30, 70),
         borderWidth=3, align='center'),
    Polygon(185, 10, 200, 0, 215, 10, fill=rgb(55, 105, 155),
            border=rgb(0, 30, 70)),

    # top windows
    Rect(145, 150, 50, 50, fill='lightYellow', border=rgb(0, 30, 70)),
    Rect(205, 150, 50, 50, fill='lightYellow', border=rgb(0, 30, 70)),
    Line(170, 150, 170, 200, fill=rgb(0, 30, 70)),
    Line(230, 150, 230, 200, fill=rgb(0, 30, 70)),
    Line(145, 175, 195, 175, fill=rgb(0, 30, 70)),
    Line(205, 175, 255, 175, fill=rgb(0, 30, 70)),

    # more windows
    Rect(145, 210, 45, 50, fill=None, border=rgb(0, 30, 70)),
    Rect(150, 215, 35, 40, fill='gainsboro', border=rgb(0, 30, 70)),
    Rect(210, 210, 45, 50, fill=None, border=rgb(0, 30, 70)),
    Rect(145, 270, 45, 50, fill=None, border=rgb(0, 30, 70)),
    Rect(210, 270, 45, 50, fill=None, border=rgb(0, 30, 70)),
    Rect(145, 330, 45, 40, fill=None, border=rgb(0, 30, 70)),
    Rect(210, 330, 45, 40, fill=None, border=rgb(0, 30, 70))
    )


def onStep():
    # Move the Tardis right by 25 pixels, rotate it clockwise 5 degrees, and
    # increase the size by 5.
    tardis.centerX += 25
    tardis.rotateAngle += 5
    tardis.width += 5
    tardis.height += 5
    # If the width of the Tardis reaches 400 pixels make the Tardis upright,
    # reset the width and height to 25 and 50, and center the Tardis
    # vertically in the canvas.
    if (tardis.width >= 400):
        tardis.rotateAngle = 0
        tardis.width = 25
        tardis.height = 50
        tardis.centerY = 200
    # Implement wraparound.
    if (tardis.left > 400):
        tardis.right = 0


