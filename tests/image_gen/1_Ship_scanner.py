app.background = 'black'
app.stepsPerSecond = 15

Rect(200, 225, 500, 500, fill=gradient('lime', 'black', 'black'), opacity=80,
     align='center')

Label('Scanning for ships...', 200, 25, fill='white', size=20)

scanner = Group(
    Circle(200, 225, 10, fill='green')
    )
scanLine = Line(200, 50, 200, 400, fill='white', lineWidth=1)

signals = Group()

def drawOuterScanner():
    # Draw the rings of the scanner, and add them to the scanner group.
    for scannerNum in range(1, 7):
        scannerRadius = 30 * scannerNum
        scanner.add(
            Circle(200, 225, scannerRadius, fill=None, border='green')
            )
drawOuterScanner()

def drawShipAndSignals(x, y, radius):
    # Draw the red circles around the ship and add the circles to the signals
    # group. The radius of each circle is half of that of the next largest
    # circle.
    while (radius > 0):
        signals.add(
            Circle(x, y, radius, fill=None, border='red', opacity=70)
            )
        radius = radius // 2
    # ship
    Oval(x, y, randrange(5, 20), randrange(5, 20), fill='steelBlue')

def onMousePress(mouseX, mouseY):
    if (scanner.contains(mouseX, mouseY) == True):
        drawShipAndSignals(mouseX, mouseY, randrange(20, 100))

def onStep():
    scanLine.rotateAngle += 3

    # Increases the radius of each signal.
    for signal in signals:
        signal.radius *= 1.05

        # Removes signals that are too large and add a new one.
        if (signal.radius >= 75):
            signals.remove(signal)
            signals.add(
                Circle(signal.centerX, signal.centerY, 5, fill=None,
                       border='red', opacity=70)
                )

onMousePress(100, 100)
onSteps(5)
onMousePress(100, 300)
onSteps(5)
onMousePress(300, 100)
onSteps(5)
onMousePress(300, 300)
onSteps(5)
app.paused = True


# -
app.background = 'black'
app.stepsPerSecond = 15

Rect(200, 225, 500, 500, fill=gradient('lime', 'black', 'black'), opacity=80,
     align='center')

Label('Scanning for ships...', 200, 25, fill='white', size=20)

scanner = Group(
    Circle(200, 225, 10, fill='green')
    )
scanLine = Line(200, 50, 200, 400, fill='white', lineWidth=1)

signals = Group()

def drawOuterScanner():
    # Draw the rings of the scanner, and add them to the scanner group.
    for scannerNum in range(1, 7):
        scannerRadius = 30 * scannerNum
        scanner.add(
            Circle(200, 225, scannerRadius, fill=None, border='green')
            )
drawOuterScanner()

def drawShipAndSignals(x, y, radius):
    # Draw the red circles around the ship and add the circles to the signals
    # group. The radius of each circle is half of that of the next largest
    # circle.
    while (radius > 0):
        signals.add(
            Circle(x, y, radius, fill=None, border='red', opacity=70)
            )
        radius = radius // 2
    # ship
    Oval(x, y, randrange(5, 20), randrange(5, 20), fill='steelBlue')

def onMousePress(mouseX, mouseY):
    if (scanner.contains(mouseX, mouseY) == True):
        drawShipAndSignals(mouseX, mouseY, randrange(20, 100))

def onStep():
    scanLine.rotateAngle += 3

    # Increases the radius of each signal.
    for signal in signals:
        signal.radius *= 1.05

        # Removes signals that are too large and add a new one.
        if (signal.radius >= 75):
            signals.remove(signal)
            signals.add(
                Circle(signal.centerX, signal.centerY, 5, fill=None,
                       border='red', opacity=70)
                )

onMousePress(175, 300)
onMousePress(280, 350)
app.paused = True


# -
app.background = 'black'
app.stepsPerSecond = 15

Rect(200, 225, 500, 500, fill=gradient('lime', 'black', 'black'), opacity=80,
     align='center')

Label('Scanning for ships...', 200, 25, fill='white', size=20)

scanner = Group(
    Circle(200, 225, 10, fill='green')
    )
scanLine = Line(200, 50, 200, 400, fill='white', lineWidth=1)

signals = Group()

def drawOuterScanner():
    # Draw the rings of the scanner, and add them to the scanner group.
    for scannerNum in range(1, 7):
        scannerRadius = 30 * scannerNum
        scanner.add(
            Circle(200, 225, scannerRadius, fill=None, border='green')
            )
drawOuterScanner()

def drawShipAndSignals(x, y, radius):
    # Draw the red circles around the ship and add the circles to the signals
    # group. The radius of each circle is half of that of the next largest
    # circle.
    while (radius > 0):
        signals.add(
            Circle(x, y, radius, fill=None, border='red', opacity=70)
            )
        radius = radius // 2
    # ship
    Oval(x, y, randrange(5, 20), randrange(5, 20), fill='steelBlue')

def onMousePress(mouseX, mouseY):
    if (scanner.contains(mouseX, mouseY) == True):
        drawShipAndSignals(mouseX, mouseY, randrange(20, 100))

def onStep():
    scanLine.rotateAngle += 3

    # Increases the radius of each signal.
    for signal in signals:
        signal.radius *= 1.05

        # Removes signals that are too large and add a new one.
        if (signal.radius >= 75):
            signals.remove(signal)
            signals.add(
                Circle(signal.centerX, signal.centerY, 5, fill=None,
                       border='red', opacity=70)
                )

onMousePress(175, 300)
onMousePress(280, 350)
app.paused = True

