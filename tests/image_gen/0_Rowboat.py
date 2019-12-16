app.background = gradient('midnightBlue', 'midnightBlue', 'orchid', start='top')

# background grass
Rect(0, 290, 400, 30, fill='darkGreen')

# trees
Polygon(0, 0, 25, 20, 35, 50, 60, 20, 90, 15, 105, 30, 100, 75, 90, 120,
        105, 135, 100, 190, 75, 210, 50, 240, 0, 250,
        fill=gradient('green', 'darkGreen', rgb(0, 40, 0)))
Polygon(340, 240, 275, 215, 255, 190, 240, 40, 305, 25, 340, 15, 400, 15,
        400, 240, fill=gradient('green', 'darkGreen', rgb(0, 40, 0)))
Polygon(0, 10, 20, 110, 50, 60, 85, 35, 60, 65, 40, 125, 65, 100, 30, 175,
        90, 150, 55, 207, 50, 250, 100, 320, 0, 320,
        fill=gradient('peru', 'sienna', 'saddleBrown', rgb(80, 40, 20)))
Polygon(150, 260, 105, 240, 75, 185, 70, 150, 80, 125, 90, 110, 70, 80, 90, 45,
        110, 15, 160, 30, 210, 10, 240, 40, 265, 100, 270, 170, 210, 235,
        fill=gradient('green', 'darkGreen', rgb(0, 40, 0)))
Polygon(110, 320, 135, 250, 90, 170, 130, 185, 120, 120, 90, 70, 125, 100,
        140, 140, 145, 85, 120, 40, 150, 70, 175, 100, 205, 40, 200, 120,
        235, 100, 200, 170, 250, 140, 200, 220, 225, 250, 275, 320,
        fill=gradient('peru', 'sienna', 'saddleBrown', rgb(80, 40, 20)))
Polygon(305, 320, 335, 220, 270, 170, 345, 195, 310, 135, 270, 120, 315, 120,
        350, 135, 310, 85, 265, 55, 325, 70, 360, 100, 375, 25, 380, 65, 400,
        140, 400, 320,
        fill=gradient('peru', 'sienna', 'saddleBrown', rgb(80, 40, 20)))
Rect(0, 320, 400, 400, fill=gradient('blue', 'darkBlue', 'black', start='top'))

# stars
Star(260, 240, 4, 20, fill='gold', opacity=50)
Star(85, 225, 3, 20, fill='gold', opacity=50)
Star(40, 15, 4, 20, fill='gold', opacity=80)
Star(320, 10, 4, 20, fill='gold', opacity=80)
Star(235, 20, 3, 20, fill='gold', opacity=80)
Star(170, 5, 3, 20, fill='gold', opacity=80)

# boat
boatBottom = Polygon(0, 300, 25, 350, 65, 360, 100, 362, 135, 360, 175, 350,
                     200, 300, fill=gradient(rgb(100, 40, 20), rgb(80, 20, 0)))
boatInside = Oval(100, 300, 200, 30, fill='saddleBrown')
boatSeats = Polygon(38, 292, 38, 313, 52, 315, 63, 315, 78, 315, 104, 315, 125,
                    315, 149, 315, 104, 288, 104, 315, 78, 315)
boatSeatCovers = Polygon(78, 315, 38, 292, 45, 285, 85, 308, 78, 315, 149, 315,
                         104, 288, 111, 281, 156, 308, 149, 315, fill='sienna')

# person
head = Circle(70, 250, 15)
forwardBody = Polygon(69, 250, 54, 301, 80, 301, 89, 315, 91, 315, 80, 299,
                      56, 299, 63, 279, 82, 291, 101, 275, 99, 275, 82, 289,
                      63, 277, 71, 250)
backwardBody = Polygon(39, 250, 64, 301, 90, 301, 99, 315, 101, 315, 90, 299,
                       66, 299, 52, 274, 85, 284, 85, 282, 52, 272, 41, 250,
                       visible=False)

# paddle
paddleStick = Line(92, 246, 130, 364, fill='saddleBrown', lineWidth=5)

# water
Rect(0, 340, 400, 60, fill='darkBlue', opacity=30)

# grass
grass = Star(50, 475, 150, 75, roundness=65,
             fill=gradient('lime', rgb(0, 50, 0), 'darkGreen', 'darkGreen',
                           start='top'))
Star(175, 455, 150, 65, fill=grass.fill, roundness=50)
Star(250, 465, 140, 90, fill=grass.fill, roundness=60)
Star(325, 480, 175, 75, fill=grass.fill, roundness=60)

def onMousePress(mouseX, mouseY):
    # Switches person to front position.
    head.centerX = boatBottom.centerX - 30
    forwardBody.visible = True
    backwardBody.visible = False
    paddleStick.x2 = boatBottom.centerX + 30

def onMouseRelease(mouseX, mouseY):
    # Switches person to back position.
    head.centerX = boatBottom.centerX - 60
    forwardBody.visible = False
    backwardBody.visible = True
    paddleStick.x2 = boatBottom.centerX - 30

    # Moves boat and person to the right.
    boatBottom.centerX += 20
    boatInside.centerX += 20
    boatSeats.centerX += 20
    boatSeatCovers.centerX += 20
    head.centerX += 20
    forwardBody.centerX += 20
    backwardBody.centerX += 20
    paddleStick.centerX += 20


# This test case is intentionally left blank.

