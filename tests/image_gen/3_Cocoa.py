app.background = 'lightCyan'

# table
Polygon(0, 325, 100, 200, 400, 200, 400, 400, 0, 400, fill='tan')

# clock
Circle(60, 75, 50, fill='white', border='black')
Circle(60, 75, 45, fill='white', border='black', dashes=True)

# hand draws a line centered at the center of the clock. handCover covers half
# of the hand so that the hand only points in only one direction.
hand = Line(60, 40, 60, 110)
handCover = Line(60, 75, 60, 110, fill='white', lineWidth=5)

# mug handle
Circle(330, 260, 40, fill=None, border='brown', borderWidth=12)

# mug
Rect(170, 180, 160, 150, fill='brown')
Oval(250, 330, 160, 60, fill='brown')
Oval(250, 180, 160, 80, fill='maroon')
Oval(250, 185, 140, 50, fill='saddleBrown')

def drawMarshmallow(x, y):
    Rect(x, y, 20, 10, fill='white')
    Oval(x, y - 5, 20, 10, fill='white', border='brown', borderWidth=1,
         align='left-top')
    Oval(x, y + 5, 20, 10, fill='white', align='left-top')

def drawMarshmallows():
    drawMarshmallow(200, 170)
    drawMarshmallow(275, 175)
    drawMarshmallow(240, 190)

def drawSteamPart(x):
    Circle(x, 60, 20, fill='grey', opacity=20)
    Circle(x - 10, 60, 20, fill='lightCyan')
    Circle(x, 100, 20, fill='grey', opacity=20)
    Circle(x + 10, 100, 20, fill='lightCyan')

def drawSteam():
    drawSteamPart(190)
    drawSteamPart(250)
    drawSteamPart(310)

drawSteam()
drawMarshmallows()

marshmallowCover = Oval(250, 185, 140, 50, fill='saddleBrown', opacity=0)
steamCover = Rect(160, 30, 170, 100, fill='lightCyan', opacity=0)

def onKeyHold(keys):
    # Rotate the clock hand, and make sure to move the handCover as well. Cover
    # up the marshmallows and steam gradually so it looks like disappearing.
    hand.rotateAngle += 5
    handCover.x2 = hand.x2
    handCover.y2 = hand.y2
    if (marshmallowCover.opacity < 99):
        marshmallowCover.opacity += 2
    if (steamCover.opacity < 99):
        steamCover.opacity += 1



# -
app.background = 'lightCyan'

# table
Polygon(0, 325, 100, 200, 400, 200, 400, 400, 0, 400, fill='tan')

# clock
Circle(60, 75, 50, fill='white', border='black')
Circle(60, 75, 45, fill='white', border='black', dashes=True)

# hand draws a line centered at the center of the clock. handCover covers half
# of the hand so that the hand only points in only one direction.
hand = Line(60, 40, 60, 110)
handCover = Line(60, 75, 60, 110, fill='white', lineWidth=5)

# mug handle
Circle(330, 260, 40, fill=None, border='brown', borderWidth=12)

# mug
Rect(170, 180, 160, 150, fill='brown')
Oval(250, 330, 160, 60, fill='brown')
Oval(250, 180, 160, 80, fill='maroon')
Oval(250, 185, 140, 50, fill='saddleBrown')

def drawMarshmallow(x, y):
    Rect(x, y, 20, 10, fill='white')
    Oval(x, y - 5, 20, 10, fill='white', border='brown', borderWidth=1,
         align='left-top')
    Oval(x, y + 5, 20, 10, fill='white', align='left-top')

def drawMarshmallows():
    drawMarshmallow(200, 170)
    drawMarshmallow(275, 175)
    drawMarshmallow(240, 190)

def drawSteamPart(x):
    Circle(x, 60, 20, fill='grey', opacity=20)
    Circle(x - 10, 60, 20, fill='lightCyan')
    Circle(x, 100, 20, fill='grey', opacity=20)
    Circle(x + 10, 100, 20, fill='lightCyan')

def drawSteam():
    drawSteamPart(190)
    drawSteamPart(250)
    drawSteamPart(310)

drawSteam()
drawMarshmallows()

marshmallowCover = Oval(250, 185, 140, 50, fill='saddleBrown', opacity=0)
steamCover = Rect(160, 30, 170, 100, fill='lightCyan', opacity=0)

def onKeyHold(keys):
    # Rotate the clock hand, and make sure to move the handCover as well. Cover
    # up the marshmallows and steam gradually so it looks like disappearing.
    hand.rotateAngle += 5
    handCover.x2 = hand.x2
    handCover.y2 = hand.y2
    if (marshmallowCover.opacity < 99):
        marshmallowCover.opacity += 2
    if (steamCover.opacity < 99):
        steamCover.opacity += 1



# -
app.background = 'lightCyan'

# table
Polygon(0, 325, 100, 200, 400, 200, 400, 400, 0, 400, fill='tan')

# clock
Circle(60, 75, 50, fill='white', border='black')
Circle(60, 75, 45, fill='white', border='black', dashes=True)

# hand draws a line centered at the center of the clock. handCover covers half
# of the hand so that the hand only points in only one direction.
hand = Line(60, 40, 60, 110)
handCover = Line(60, 75, 60, 110, fill='white', lineWidth=5)

# mug handle
Circle(330, 260, 40, fill=None, border='brown', borderWidth=12)

# mug
Rect(170, 180, 160, 150, fill='brown')
Oval(250, 330, 160, 60, fill='brown')
Oval(250, 180, 160, 80, fill='maroon')
Oval(250, 185, 140, 50, fill='saddleBrown')

def drawMarshmallow(x, y):
    Rect(x, y, 20, 10, fill='white')
    Oval(x, y - 5, 20, 10, fill='white', border='brown', borderWidth=1,
         align='left-top')
    Oval(x, y + 5, 20, 10, fill='white', align='left-top')

def drawMarshmallows():
    drawMarshmallow(200, 170)
    drawMarshmallow(275, 175)
    drawMarshmallow(240, 190)

def drawSteamPart(x):
    Circle(x, 60, 20, fill='grey', opacity=20)
    Circle(x - 10, 60, 20, fill='lightCyan')
    Circle(x, 100, 20, fill='grey', opacity=20)
    Circle(x + 10, 100, 20, fill='lightCyan')

def drawSteam():
    drawSteamPart(190)
    drawSteamPart(250)
    drawSteamPart(310)

drawSteam()
drawMarshmallows()

marshmallowCover = Oval(250, 185, 140, 50, fill='saddleBrown', opacity=0)
steamCover = Rect(160, 30, 170, 100, fill='lightCyan', opacity=0)

def onKeyHold(keys):
    # Rotate the clock hand, and make sure to move the handCover as well. Cover
    # up the marshmallows and steam gradually so it looks like disappearing.
    hand.rotateAngle += 5
    handCover.x2 = hand.x2
    handCover.y2 = hand.y2
    if (marshmallowCover.opacity < 99):
        marshmallowCover.opacity += 2
    if (steamCover.opacity < 99):
        steamCover.opacity += 1

onKeyHolds(['space'], 50)

