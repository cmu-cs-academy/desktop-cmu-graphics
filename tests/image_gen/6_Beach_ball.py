app.background = gradient('lightSteelBlue', 'skyBlue', start='top')

# ocean and beach
Rect(0, 190, 400, 190, fill=gradient('darkBlue', 'royalBlue', start='top'))
Polygon(0, 300, 270, 335, 400, 300, 400, 400, 0, 400,
        fill=gradient('paleGoldenrod', 'burlyWood', start='top'))
Polygon(0, 295, 270, 330, 400, 295, 400, 300, 270, 340, 0, 300, fill='white')

wave = Oval(220, 250, 700, 60, fill='darkBlue', border='steelBlue', opacity=50)
Rect(0, 200, 400, 30, fill='darkBlue')

shadow = Oval(200, 370, 125, 12, fill='darkKhaki', opacity=60)

beachBall = Group(
    Polygon(200, 300, 150, 250, 200, 225, fill='red'),
    Polygon(200, 300, 200, 225, 250, 250, fill='blue'),
    Polygon(200, 300, 250, 250, 275, 300, fill='green'),
    Polygon(275, 300, 200, 300, 250, 350, fill='purple'),
    Polygon(250, 350, 200, 300, 200, 375, fill='yellow'),
    Polygon(200, 375, 200, 300, 150, 350, fill='orange'),
    Polygon(200, 300, 150, 350, 125, 300, fill='fuchsia'),
    Polygon(150, 250, 200, 300, 125, 300, fill='slateBlue'),
    Circle(200, 300, 68, fill=gradient('white', 'black'), opacity=15)
    )
beachBall.direction = 1

def onKeyHold(keys):
    # Moves the wave in and out and fade appropriately.
    wave.opacity += 2 * beachBall.direction
    wave.height += beachBall.direction

    # The ball should rotate and roll until it reaches the end of the canvas
    # at which point it should reverse direction.
    beachBall.rotateAngle += 5 * beachBall.direction
    beachBall.centerX += 6 * beachBall.direction
    if ((beachBall.right >= 400) or (beachBall.left <= 0)):
        beachBall.direction *= -1
    shadow.centerX = beachBall.centerX

onKeyHold(['space'])


# -
app.background = gradient('lightSteelBlue', 'skyBlue', start='top')

# ocean and beach
Rect(0, 190, 400, 190, fill=gradient('darkBlue', 'royalBlue', start='top'))
Polygon(0, 300, 270, 335, 400, 300, 400, 400, 0, 400,
        fill=gradient('paleGoldenrod', 'burlyWood', start='top'))
Polygon(0, 295, 270, 330, 400, 295, 400, 300, 270, 340, 0, 300, fill='white')

wave = Oval(220, 250, 700, 60, fill='darkBlue', border='steelBlue', opacity=50)
Rect(0, 200, 400, 30, fill='darkBlue')

shadow = Oval(200, 370, 125, 12, fill='darkKhaki', opacity=60)

beachBall = Group(
    Polygon(200, 300, 150, 250, 200, 225, fill='red'),
    Polygon(200, 300, 200, 225, 250, 250, fill='blue'),
    Polygon(200, 300, 250, 250, 275, 300, fill='green'),
    Polygon(275, 300, 200, 300, 250, 350, fill='purple'),
    Polygon(250, 350, 200, 300, 200, 375, fill='yellow'),
    Polygon(200, 375, 200, 300, 150, 350, fill='orange'),
    Polygon(200, 300, 150, 350, 125, 300, fill='fuchsia'),
    Polygon(150, 250, 200, 300, 125, 300, fill='slateBlue'),
    Circle(200, 300, 68, fill=gradient('white', 'black'), opacity=15)
    )
beachBall.direction = 1

def onKeyHold(keys):
    # Moves the wave in and out and fade appropriately.
    wave.opacity += 2 * beachBall.direction
    wave.height += beachBall.direction

    # The ball should rotate and roll until it reaches the end of the canvas
    # at which point it should reverse direction.
    beachBall.rotateAngle += 5 * beachBall.direction
    beachBall.centerX += 6 * beachBall.direction
    if ((beachBall.right >= 400) or (beachBall.left <= 0)):
        beachBall.direction *= -1
    shadow.centerX = beachBall.centerX

onKeyHolds(['space'], 23)


# -
app.background = gradient('lightSteelBlue', 'skyBlue', start='top')

# ocean and beach
Rect(0, 190, 400, 190, fill=gradient('darkBlue', 'royalBlue', start='top'))
Polygon(0, 300, 270, 335, 400, 300, 400, 400, 0, 400,
        fill=gradient('paleGoldenrod', 'burlyWood', start='top'))
Polygon(0, 295, 270, 330, 400, 295, 400, 300, 270, 340, 0, 300, fill='white')

wave = Oval(220, 250, 700, 60, fill='darkBlue', border='steelBlue', opacity=50)
Rect(0, 200, 400, 30, fill='darkBlue')

shadow = Oval(200, 370, 125, 12, fill='darkKhaki', opacity=60)

beachBall = Group(
    Polygon(200, 300, 150, 250, 200, 225, fill='red'),
    Polygon(200, 300, 200, 225, 250, 250, fill='blue'),
    Polygon(200, 300, 250, 250, 275, 300, fill='green'),
    Polygon(275, 300, 200, 300, 250, 350, fill='purple'),
    Polygon(250, 350, 200, 300, 200, 375, fill='yellow'),
    Polygon(200, 375, 200, 300, 150, 350, fill='orange'),
    Polygon(200, 300, 150, 350, 125, 300, fill='fuchsia'),
    Polygon(150, 250, 200, 300, 125, 300, fill='slateBlue'),
    Circle(200, 300, 68, fill=gradient('white', 'black'), opacity=15)
    )
beachBall.direction = 1

def onKeyHold(keys):
    # Moves the wave in and out and fade appropriately.
    wave.opacity += 2 * beachBall.direction
    wave.height += beachBall.direction

    # The ball should rotate and roll until it reaches the end of the canvas
    # at which point it should reverse direction.
    beachBall.rotateAngle += 5 * beachBall.direction
    beachBall.centerX += 6 * beachBall.direction
    if ((beachBall.right >= 400) or (beachBall.left <= 0)):
        beachBall.direction *= -1
    shadow.centerX = beachBall.centerX

onKeyHolds(['space'], 22)

