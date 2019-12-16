app.background = 'mediumseaGreen'
app.stepsPerSecond = 20

# glow
rays = Star(200, 200, 175, 25, fill='lemonChiffon', roundness=5, opacity=0)
raysCover = Polygon(130, 165, 270, 165, 200, 285, fill='mediumSeaGreen')

# triforce symbol
top = RegularPolygon(0, -175, 80, 3,
                     fill=gradient('yellow', 'darkGoldenrod', start='right-top'),
                     border='goldenrod', borderWidth=4, rotateAngle=40)
bottomLeft = RegularPolygon(-170, 445, 80, 3,
                            fill=gradient('yellow', 'darkGoldenrod',
                                          start='right-top'),
                            border='goldenrod', borderWidth=4, rotateAngle=40)
bottomRight = RegularPolygon(570, 445, 80, 3,
                             fill=gradient('yellow', 'darkGoldenrod',
                                           start='right-top'),
                             border='goldenrod', borderWidth=4, rotateAngle=80)

def onStep():
    # If the top polygon's centerX is less than 200, then increase
    # its angle and centerX, centerY.
    if (top.centerX < 200):
        top.rotateAngle += 2
        top.centerX += 2
        top.centerY += 3

    # If the bottomLeft polygon's centerX is less than 130, then rotate
    # and move it up and right.
    if (bottomLeft.centerX < 130):
        bottomLeft.rotateAngle += 2
        bottomLeft.centerX += 3
        bottomLeft.centerY -= 2
    # If the bottomRight polygon's centerX is greater than 270, then rotate
    # it and move it up and left.
    if (bottomRight.centerX > 270):
        bottomRight.rotateAngle -= 2
        bottomRight.centerX -= 3
        bottomRight.centerY -= 2
    # Otherwise, change the background, the fill for raysCover and
    # change the rays opacity.
    else:
        app.background = gradient('mediumSeaGreen', 'seaGreen')
        rays.opacity = 40
        raysCover.fill = gradient('mediumSeaGreen', 'seaGreen')

onSteps(101)
app.paused = True


# -
app.background = 'mediumseaGreen'
app.stepsPerSecond = 20

# glow
rays = Star(200, 200, 175, 25, fill='lemonChiffon', roundness=5, opacity=0)
raysCover = Polygon(130, 165, 270, 165, 200, 285, fill='mediumSeaGreen')

# triforce symbol
top = RegularPolygon(0, -175, 80, 3,
                     fill=gradient('yellow', 'darkGoldenrod', start='right-top'),
                     border='goldenrod', borderWidth=4, rotateAngle=40)
bottomLeft = RegularPolygon(-170, 445, 80, 3,
                            fill=gradient('yellow', 'darkGoldenrod',
                                          start='right-top'),
                            border='goldenrod', borderWidth=4, rotateAngle=40)
bottomRight = RegularPolygon(570, 445, 80, 3,
                             fill=gradient('yellow', 'darkGoldenrod',
                                           start='right-top'),
                             border='goldenrod', borderWidth=4, rotateAngle=80)

def onStep():
    # If the top polygon's centerX is less than 200, then increase
    # its angle and centerX, centerY.
    if (top.centerX < 200):
        top.rotateAngle += 2
        top.centerX += 2
        top.centerY += 3

    # If the bottomLeft polygon's centerX is less than 130, then rotate
    # and move it up and right.
    if (bottomLeft.centerX < 130):
        bottomLeft.rotateAngle += 2
        bottomLeft.centerX += 3
        bottomLeft.centerY -= 2
    # If the bottomRight polygon's centerX is greater than 270, then rotate
    # it and move it up and left.
    if (bottomRight.centerX > 270):
        bottomRight.rotateAngle -= 2
        bottomRight.centerX -= 3
        bottomRight.centerY -= 2
    # Otherwise, change the background, the fill for raysCover and
    # change the rays opacity.
    else:
        app.background = gradient('mediumSeaGreen', 'seaGreen')
        rays.opacity = 40
        raysCover.fill = gradient('mediumSeaGreen', 'seaGreen')

onSteps(60)
app.paused = True


# -
app.background = 'mediumseaGreen'
app.stepsPerSecond = 20

# glow
rays = Star(200, 200, 175, 25, fill='lemonChiffon', roundness=5, opacity=0)
raysCover = Polygon(130, 165, 270, 165, 200, 285, fill='mediumSeaGreen')

# triforce symbol
top = RegularPolygon(0, -175, 80, 3,
                     fill=gradient('yellow', 'darkGoldenrod', start='right-top'),
                     border='goldenrod', borderWidth=4, rotateAngle=40)
bottomLeft = RegularPolygon(-170, 445, 80, 3,
                            fill=gradient('yellow', 'darkGoldenrod',
                                          start='right-top'),
                            border='goldenrod', borderWidth=4, rotateAngle=40)
bottomRight = RegularPolygon(570, 445, 80, 3,
                             fill=gradient('yellow', 'darkGoldenrod',
                                           start='right-top'),
                             border='goldenrod', borderWidth=4, rotateAngle=80)

def onStep():
    # If the top polygon's centerX is less than 200, then increase
    # its angle and centerX, centerY.
    if (top.centerX < 200):
        top.rotateAngle += 2
        top.centerX += 2
        top.centerY += 3

    # If the bottomLeft polygon's centerX is less than 130, then rotate
    # and move it up and right.
    if (bottomLeft.centerX < 130):
        bottomLeft.rotateAngle += 2
        bottomLeft.centerX += 3
        bottomLeft.centerY -= 2
    # If the bottomRight polygon's centerX is greater than 270, then rotate
    # it and move it up and left.
    if (bottomRight.centerX > 270):
        bottomRight.rotateAngle -= 2
        bottomRight.centerX -= 3
        bottomRight.centerY -= 2
    # Otherwise, change the background, the fill for raysCover and
    # change the rays opacity.
    else:
        app.background = gradient('mediumSeaGreen', 'seaGreen')
        rays.opacity = 40
        raysCover.fill = gradient('mediumSeaGreen', 'seaGreen')

onSteps(100)
app.paused = True

