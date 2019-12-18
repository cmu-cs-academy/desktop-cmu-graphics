app.background = gradient('deepSkyBlue', 'skyBlue', start='top')

# clouds
Circle(-10, 350, 60, fill='white', border='gainsboro', borderWidth=3)
Circle(55, 380, 50, fill='white', border='gainsboro', borderWidth=3)
Rect(0, 340, 30, 60, fill='white')
Circle(340, 75, 50, fill='white', border='gainsboro', borderWidth=3)
Circle(260, 120, 70, fill='white', border='gainsboro', borderWidth=3)
Circle(410, 120, 60, fill='white', border='gainsboro', borderWidth=3)
Circle(330, 150, 80, fill='white', border='gainsboro')
Rect(295, 60, 20, 11, fill='white')
Rect(365, 65, 20, 13, fill='white')
Rect(245, 90, 155, 95, fill='white')

# bird wings
leftWing = Polygon(175, 230, 185, 205, 145, 195, 130, 195, 155, 210,
                   fill='violet')
rightWing = Polygon(225, 230, 215, 205, 255, 195, 270, 195, 245, 210,
                    fill='violet')
app.wingsMovingUp = True

# bird body
body = Oval(200, 250, 80, 65, fill='violet', align='bottom')
belly = Oval(200, 250, 65, 40, fill='pink', align='bottom')

# bird eyes
leftEye = Circle(190, 190, 12, border='white', borderWidth=7)
rightEye = Circle(210, 190, 12, border='white', borderWidth=7)

# bird beak
beak = Polygon(200, 195, 210, 200, 200, 215, 190, 200, fill='gold')

def moveBird(bodyX, bodyY):
    # Moves all the individual pieces of the bird (besides the body).
    belly.centerX = bodyX
    belly.bottom = body.bottom

    leftEye.centerX = bodyX - 10
    rightEye.centerX = bodyX + 10
    leftEye.centerY = body.top + 5
    rightEye.centerY = body.top + 5

    beak.centerX = bodyX
    beak.bottom = belly.top + 5

    leftWing.centerX = body.left - 8
    rightWing.centerX = body.right + 8
    leftWing.centerY = bodyY - 5
    rightWing.centerY = bodyY - 5

def onKeyHold(keys):
    # Change the center of the body based on the 'w','a','s','d' keys.
    if ('a' in keys):
        body.centerX -= 2
    if ('d' in keys):
        body.centerX += 2
    if ('s' in keys):
        body.centerY += 2
    if ('w' in keys):
        body.centerY -= 2
    # When moving up or down, flap the wings 5 degrees in the direction that
    # app.wingsMovingUp indicates. If the angle is less than -40 or larger
    # than 0, app.wingsMovingUp should change.
    if (('s' in keys) or ('w' in keys)):
        if (app.wingsMovingUp == True):
            leftWing.rotateAngle -= 5
            rightWing.rotateAngle += 5
        else:
            leftWing.rotateAngle += 5
            rightWing.rotateAngle -= 5
        if ((leftWing.rotateAngle < -40) or (leftWing.rotateAngle > 0)):
            if ( app.wingsMovingUp == True):
                app.wingsMovingUp = False
            else:
                app.wingsMovingUp = True
    # Move the bird based on the new center of the body.
    moveBird(body.centerX, body.centerY)

onKeyHolds(['w'], 30)
onKeyHolds(['a'], 20)


# -
app.background = gradient('deepSkyBlue', 'skyBlue', start='top')

# clouds
Circle(-10, 350, 60, fill='white', border='gainsboro', borderWidth=3)
Circle(55, 380, 50, fill='white', border='gainsboro', borderWidth=3)
Rect(0, 340, 30, 60, fill='white')
Circle(340, 75, 50, fill='white', border='gainsboro', borderWidth=3)
Circle(260, 120, 70, fill='white', border='gainsboro', borderWidth=3)
Circle(410, 120, 60, fill='white', border='gainsboro', borderWidth=3)
Circle(330, 150, 80, fill='white', border='gainsboro')
Rect(295, 60, 20, 11, fill='white')
Rect(365, 65, 20, 13, fill='white')
Rect(245, 90, 155, 95, fill='white')

# bird wings
leftWing = Polygon(175, 230, 185, 205, 145, 195, 130, 195, 155, 210,
                   fill='violet')
rightWing = Polygon(225, 230, 215, 205, 255, 195, 270, 195, 245, 210,
                    fill='violet')
app.wingsMovingUp = True

# bird body
body = Oval(200, 250, 80, 65, fill='violet', align='bottom')
belly = Oval(200, 250, 65, 40, fill='pink', align='bottom')

# bird eyes
leftEye = Circle(190, 190, 12, border='white', borderWidth=7)
rightEye = Circle(210, 190, 12, border='white', borderWidth=7)

# bird beak
beak = Polygon(200, 195, 210, 200, 200, 215, 190, 200, fill='gold')

def moveBird(bodyX, bodyY):
    # Moves all the individual pieces of the bird (besides the body).
    belly.centerX = bodyX
    belly.bottom = body.bottom

    leftEye.centerX = bodyX - 10
    rightEye.centerX = bodyX + 10
    leftEye.centerY = body.top + 5
    rightEye.centerY = body.top + 5

    beak.centerX = bodyX
    beak.bottom = belly.top + 5

    leftWing.centerX = body.left - 8
    rightWing.centerX = body.right + 8
    leftWing.centerY = bodyY - 5
    rightWing.centerY = bodyY - 5

def onKeyHold(keys):
    # Change the center of the body based on the 'w','a','s','d' keys.
    if ('a' in keys):
        body.centerX -= 2
    if ('d' in keys):
        body.centerX += 2
    if ('s' in keys):
        body.centerY += 2
    if ('w' in keys):
        body.centerY -= 2
    # When moving up or down, flap the wings 5 degrees in the direction that
    # app.wingsMovingUp indicates. If the angle is less than -40 or larger
    # than 0, app.wingsMovingUp should change.
    if (('s' in keys) or ('w' in keys)):
        if (app.wingsMovingUp == True):
            leftWing.rotateAngle -= 5
            rightWing.rotateAngle += 5
        else:
            leftWing.rotateAngle += 5
            rightWing.rotateAngle -= 5
        if ((leftWing.rotateAngle < -40) or (leftWing.rotateAngle > 0)):
            if ( app.wingsMovingUp == True):
                app.wingsMovingUp = False
            else:
                app.wingsMovingUp = True
    # Move the bird based on the new center of the body.
    moveBird(body.centerX, body.centerY)

onKeyHolds(['w'], 20)


# -
app.background = gradient('deepSkyBlue', 'skyBlue', start='top')

# clouds
Circle(-10, 350, 60, fill='white', border='gainsboro', borderWidth=3)
Circle(55, 380, 50, fill='white', border='gainsboro', borderWidth=3)
Rect(0, 340, 30, 60, fill='white')
Circle(340, 75, 50, fill='white', border='gainsboro', borderWidth=3)
Circle(260, 120, 70, fill='white', border='gainsboro', borderWidth=3)
Circle(410, 120, 60, fill='white', border='gainsboro', borderWidth=3)
Circle(330, 150, 80, fill='white', border='gainsboro')
Rect(295, 60, 20, 11, fill='white')
Rect(365, 65, 20, 13, fill='white')
Rect(245, 90, 155, 95, fill='white')

# bird wings
leftWing = Polygon(175, 230, 185, 205, 145, 195, 130, 195, 155, 210,
                   fill='violet')
rightWing = Polygon(225, 230, 215, 205, 255, 195, 270, 195, 245, 210,
                    fill='violet')
app.wingsMovingUp = True

# bird body
body = Oval(200, 250, 80, 65, fill='violet', align='bottom')
belly = Oval(200, 250, 65, 40, fill='pink', align='bottom')

# bird eyes
leftEye = Circle(190, 190, 12, border='white', borderWidth=7)
rightEye = Circle(210, 190, 12, border='white', borderWidth=7)

# bird beak
beak = Polygon(200, 195, 210, 200, 200, 215, 190, 200, fill='gold')

def moveBird(bodyX, bodyY):
    # Moves all the individual pieces of the bird (besides the body).
    belly.centerX = bodyX
    belly.bottom = body.bottom

    leftEye.centerX = bodyX - 10
    rightEye.centerX = bodyX + 10
    leftEye.centerY = body.top + 5
    rightEye.centerY = body.top + 5

    beak.centerX = bodyX
    beak.bottom = belly.top + 5

    leftWing.centerX = body.left - 8
    rightWing.centerX = body.right + 8
    leftWing.centerY = bodyY - 5
    rightWing.centerY = bodyY - 5

def onKeyHold(keys):
    # Change the center of the body based on the 'w','a','s','d' keys.
    if ('a' in keys):
        body.centerX -= 2
    if ('d' in keys):
        body.centerX += 2
    if ('s' in keys):
        body.centerY += 2
    if ('w' in keys):
        body.centerY -= 2
    # When moving up or down, flap the wings 5 degrees in the direction that
    # app.wingsMovingUp indicates. If the angle is less than -40 or larger
    # than 0, app.wingsMovingUp should change.
    if (('s' in keys) or ('w' in keys)):
        if (app.wingsMovingUp == True):
            leftWing.rotateAngle -= 5
            rightWing.rotateAngle += 5
        else:
            leftWing.rotateAngle += 5
            rightWing.rotateAngle -= 5
        if ((leftWing.rotateAngle < -40) or (leftWing.rotateAngle > 0)):
            if ( app.wingsMovingUp == True):
                app.wingsMovingUp = False
            else:
                app.wingsMovingUp = True
    # Move the bird based on the new center of the body.
    moveBird(body.centerX, body.centerY)

onKeyHolds(['a'], 20)
onKeyHolds(['d'], 30)

