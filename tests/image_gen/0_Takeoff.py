app.background = gradient('deepSkyBlue', 'lightBlue', start='top')

# ground
grass = Rect(200, 270, 800, 260, fill=gradient('mediumSeaGreen', 'darkGreen'),
             align='center')
runway = Rect(200, 280, 800, 160, fill='grey', align='center')
centerLines = Line(0, 280, 400, 280, fill='yellow', lineWidth=5, dashes=(20, 15))

# airplane landing gear
frontWheel = Circle(295, 280, 3)
frontSupport = Line(295, 270, 295, 280)
backWheel1 = Circle(140, 280, 3)
backSupport1 = Line(140, 270, 140, 280)

# airplane body and tail
Polygon(80, 235, 40, 235, 30, 175, fill='gainsboro')
Rect(190, 250, 180, 40, fill=gradient('whiteSmoke', 'darkGrey', start='top'),
     align='center')
Polygon(280, 230, 300, 233, 312, 238, 322, 245, 328, 255, 320, 265, 310, 270,
        280, 270, fill=gradient('whiteSmoke', 'darkGrey', start='top'))
Polygon(100, 230, 35, 235, 35, 240, 100, 270,
        fill=gradient('whiteSmoke', 'darkGrey', start='top'))

# airplane wings
Polygon(185, 270, 175, 270, 170, 280, fill='darkGrey')
Polygon(165, 255, 200, 255, 145, 285, fill='gainsboro')

# airplane windows
Line(100, 245, 295, 245, dashes=True)
Polygon(300, 238, 300, 245, 320, 245, 310, 238)

# sun
sun = Circle(375, 30, 50, fill=gradient('yellow', 'beige'), border='gold')

# clouds (cloud1 farthest left, cloud2 middle, cloud3 farthest right)
cloud1 = Oval(650, -225, 750, 450, fill='white')
cloud2 = Oval(800, -350, 500, 350, fill='white')
cloud3 = Oval(1000, -200, 600, 400, fill='white')

def moveSun(dy):
    sun.centerY += dy

def moveClouds(dx, dy):
    # dx is the amount the clouds move left, dy the amount they move down.
    cloud1.centerX -= dx
    cloud2.centerX -= dx
    cloud3.centerX -= dx
    cloud1.centerY += dy
    cloud2.centerY += dy
    cloud3.centerY += dy

    # Wrap the clouds around.
    if (cloud3.right < 0):
        cloud1.centerX = 800
        cloud2.centerX = 950
        cloud3.centerX = 1150

def liftLandingGear():
    # Hide all of the wheels.
    frontWheel.visible = False
    frontSupport.visible = False
    backWheel1.visible = False
    backSupport1.visible = False

def takeOff():
    # Rotate the ground as if the plane tilted up.
    grass.rotateAngle += 0.25
    runway.rotateAngle += 0.25
    centerLines.rotateAngle += 0.25

    # Move the ground down as if the plane is lifting off.
    grass.centerY += 5
    runway.centerY += 5
    centerLines.centerY += 5

def onKeyPress(key):
    if (key == 'space'):
        liftLandingGear()

def onKeyHold(keys):
    # Move the runway lines to make it seem like the runway is moving.
    if ('right' in keys):
        centerLines.centerX -= 10
        centerLines.x2 = 400

    # If both right and up keys are held down, the plane should be flying.
    # Until the grass has dropped below the canvas, the plane should in takeoff
    # mode and the sun should move down by 2 pixels at a time.
    if (('right' in keys) and ('up' in keys)):
        if (grass.top < 400):
            takeOff()
            moveSun(2)

        # Once the ground is gone, check if the 3rd cloud's top value is
        # less than 350. If it is, move the cloud down and to the left by 5.
        elif (cloud3.top < 350):
            moveClouds(5, 5)

        # If the first two statements are false, then check if the
        # sun's centerY value is greater than 30. If it is, then move the
        # clouds left by 5 and the sun up by 2.
        elif (sun.centerY > 30):
            moveClouds(5, 0)
            moveSun(-2)

        # If nothing above was true, you should just move the clouds left by 5.
        else:
            moveClouds(5, 0)


