app.background = 'black'
app.rippleSpace = 40

ripples = Group()

def drawRipples():
    ripples.clear()

    # Draw ripples from the middle of the canvas to the edges.
    # The distance between ripples is determined by app.rippleSpace.
    for radius in range(20, 200, app.rippleSpace):
        ripples.add(
            Circle(200, 200, radius, fill=None,
                   border=gradient('red', 'orange', 'yellow', 'lawnGreen',
                                   start='top'))
            )
drawRipples()

def onKeyHold(keys):
    if ('up' in keys):
        app.rippleSpace += 2
    elif (('down' in keys) and (app.rippleSpace > 2)):
        app.rippleSpace -= 2
    drawRipples()



# -
app.background = 'black'
app.rippleSpace = 40

ripples = Group()

def drawRipples():
    ripples.clear()

    # Draw ripples from the middle of the canvas to the edges.
    # The distance between ripples is determined by app.rippleSpace.
    for radius in range(20, 200, app.rippleSpace):
        ripples.add(
            Circle(200, 200, radius, fill=None,
                   border=gradient('red', 'orange', 'yellow', 'lawnGreen',
                                   start='top'))
            )
drawRipples()

def onKeyHold(keys):
    if ('up' in keys):
        app.rippleSpace += 2
    elif (('down' in keys) and (app.rippleSpace > 2)):
        app.rippleSpace -= 2
    drawRipples()

onKeyHolds(['up'], 20)


# -
app.background = 'black'
app.rippleSpace = 40

ripples = Group()

def drawRipples():
    ripples.clear()

    # Draw ripples from the middle of the canvas to the edges.
    # The distance between ripples is determined by app.rippleSpace.
    for radius in range(20, 200, app.rippleSpace):
        ripples.add(
            Circle(200, 200, radius, fill=None,
                   border=gradient('red', 'orange', 'yellow', 'lawnGreen',
                                   start='top'))
            )
drawRipples()

def onKeyHold(keys):
    if ('up' in keys):
        app.rippleSpace += 2
    elif (('down' in keys) and (app.rippleSpace > 2)):
        app.rippleSpace -= 2
    drawRipples()

onKeyHolds(['up'], 10)
onKeyHolds(['down'], 10)

