def drawBackground(skyColor, groundColor, moatColor):
    # Draws background of the image.
    Rect(0, 325, 400, 75, fill=groundColor)
    Line(0, 375, 400, 375, fill=moatColor, lineWidth=25)
    Rect(0, 0, 400, 325, fill=skyColor)

def drawBushes(x, y, bushColor):
    Circle(x, y, 15, fill=bushColor, border='green')
    Circle(x + 15, y, 15, fill=bushColor, border='green')
    Circle(x + 20, y - 10, 15, fill=bushColor, border='green')
    Circle(x + 30, y, 15, fill=bushColor, border='green')
    Circle(x + 10, y - 10, 15, fill=bushColor)

def drawGate(gateColor, gateLineColor, windowColor):
    Rect(150, 300, 100, 50, fill=windowColor)
    Circle(200, 300, 50, fill=windowColor)
    Rect(150, 350, 100, 50, fill=gateColor)
    Line(175, 350, 175, 400, fill=gateLineColor, lineWidth=4)
    Line(200, 350, 200, 400, fill=gateLineColor, lineWidth=4)
    Line(225, 350, 225, 400, fill=gateLineColor, lineWidth=4)

def drawCone(x, y, width, coneColor):
    RegularPolygon(x, y, width, 3, fill=coneColor)

def drawCover(x, y, width, height):
    # Draws the lip at the top of every tower.
    Rect(x, y + 10, width, height, fill='dimGrey')
    Circle(x, y + height, height, fill='grey')
    Circle(x + width, y + height, height, fill='grey')
    Rect(x, y, width, 2 * height, fill='grey')

def drawWindow(x, y, windowColor):
    Oval(x, y, 30, 50, fill=windowColor)
    Rect(x - 20, y + 5, 40, 20, fill='darkGrey')

def drawTinyCastleTower(x, y, width, height, castleColor):
    # Draws the top pillar of a tower.
    Rect(x, y, width, height, fill=castleColor, border='grey')
    drawCover(x, y - 5, width, 6)

def drawCastleTower(x, y, castleColor, coneColor, windowColor):
    # Draws the small tower with body, cover, and window.
    drawCone(x + 40, y - 60, 30, coneColor)
    drawTinyCastleTower(x + 10, y - 40, 60, 100, castleColor)

    Rect(x, y, 80, 200, fill=castleColor, border='grey')
    drawCover(x, y - 5, 80, 8)
    drawWindow(x + 40, y + 60, windowColor)

def drawCastleHelper(bushColor1, bushColor2, castleColor, coneColor,
                     windowColor):
    # Draws the three towers and bushes of the castle.
    drawCastleTower(45, 150, castleColor, coneColor, windowColor)
    drawCastleTower(275, 150, castleColor, coneColor, windowColor)
    drawCastleTower(160, 100, castleColor, coneColor, windowColor)

    drawBushes(30, 335, bushColor1)
    drawBushes(340, 335, bushColor1)
    drawBushes(50, 340, bushColor2)
    drawBushes(330, 340, bushColor2)

def drawCastleScene(skyColor, groundColor, moatColor, bushColor1, bushColor2,
                    castleColor, coneColor, windowColor, gateColor, gateLineColor):
    # Draw the background, the towers and bushes.
    drawBackground(skyColor, groundColor, moatColor)
    drawCastleHelper(bushColor1, bushColor2, castleColor, coneColor,
                     windowColor)
    # Draw the bottom of the center castle around the gate
    # and the gate itself.
    Rect(125, 225, 150, 125, fill=castleColor, border='grey')
    drawCover(125, 220, 150, 5)
    drawGate(gateColor, gateLineColor, windowColor)

drawCastleScene(rgb(20, 25, 70), 'darkGreen', rgb(50, 55, 110), 'darkGreen',
                'forestGreen', 'silver', rgb(55, 70, 140), 'gold', 'sienna',
                rgb(80, 30, 15))


# -
def drawBackground(skyColor, groundColor, moatColor):
    # Draws background of the image.
    Rect(0, 325, 400, 75, fill=groundColor)
    Line(0, 375, 400, 375, fill=moatColor, lineWidth=25)
    Rect(0, 0, 400, 325, fill=skyColor)

def drawBushes(x, y, bushColor):
    Circle(x, y, 15, fill=bushColor, border='green')
    Circle(x + 15, y, 15, fill=bushColor, border='green')
    Circle(x + 20, y - 10, 15, fill=bushColor, border='green')
    Circle(x + 30, y, 15, fill=bushColor, border='green')
    Circle(x + 10, y - 10, 15, fill=bushColor)

def drawGate(gateColor, gateLineColor, windowColor):
    Rect(150, 300, 100, 50, fill=windowColor)
    Circle(200, 300, 50, fill=windowColor)
    Rect(150, 350, 100, 50, fill=gateColor)
    Line(175, 350, 175, 400, fill=gateLineColor, lineWidth=4)
    Line(200, 350, 200, 400, fill=gateLineColor, lineWidth=4)
    Line(225, 350, 225, 400, fill=gateLineColor, lineWidth=4)

def drawCone(x, y, width, coneColor):
    RegularPolygon(x, y, width, 3, fill=coneColor)

def drawCover(x, y, width, height):
    # Draws the lip at the top of every tower.
    Rect(x, y + 10, width, height, fill='dimGrey')
    Circle(x, y + height, height, fill='grey')
    Circle(x + width, y + height, height, fill='grey')
    Rect(x, y, width, 2 * height, fill='grey')

def drawWindow(x, y, windowColor):
    Oval(x, y, 30, 50, fill=windowColor)
    Rect(x - 20, y + 5, 40, 20, fill='darkGrey')

def drawTinyCastleTower(x, y, width, height, castleColor):
    # Draws the top pillar of a tower.
    Rect(x, y, width, height, fill=castleColor, border='grey')
    drawCover(x, y - 5, width, 6)

def drawCastleTower(x, y, castleColor, coneColor, windowColor):
    # Draws the small tower with body, cover, and window.
    drawCone(x + 40, y - 60, 30, coneColor)
    drawTinyCastleTower(x + 10, y - 40, 60, 100, castleColor)

    Rect(x, y, 80, 200, fill=castleColor, border='grey')
    drawCover(x, y - 5, 80, 8)
    drawWindow(x + 40, y + 60, windowColor)

def drawCastleHelper(bushColor1, bushColor2, castleColor, coneColor,
                     windowColor):
    # Draws the three towers and bushes of the castle.
    drawCastleTower(45, 150, castleColor, coneColor, windowColor)
    drawCastleTower(275, 150, castleColor, coneColor, windowColor)
    drawCastleTower(160, 100, castleColor, coneColor, windowColor)

    drawBushes(30, 335, bushColor1)
    drawBushes(340, 335, bushColor1)
    drawBushes(50, 340, bushColor2)
    drawBushes(330, 340, bushColor2)

def drawCastleScene(skyColor, groundColor, moatColor, bushColor1, bushColor2,
                    castleColor, coneColor, windowColor, gateColor, gateLineColor):
    # Draw the background, the towers and bushes.
    drawBackground(skyColor, groundColor, moatColor)
    drawCastleHelper(bushColor1, bushColor2, castleColor, coneColor,
                     windowColor)
    # Draw the bottom of the center castle around the gate
    # and the gate itself.
    Rect(125, 225, 150, 125, fill=castleColor, border='grey')
    drawCover(125, 220, 150, 5)
    drawGate(gateColor, gateLineColor, windowColor)

drawCastleScene(rgb(20, 25, 70), 'darkGreen', rgb(50, 55, 110), 'darkGreen',
                'forestGreen', 'silver', rgb(55, 70, 140), 'gold', 'sienna',
                rgb(80, 30, 15))

