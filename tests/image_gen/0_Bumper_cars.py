app.background = 'darkRed'

# players
player1 = Group(
    Oval(30, 30, 60, 40, fill=gradient('salmon', 'white', start='left'),
         border='white', borderWidth=5),
    Line(10, 10, 25, 10, lineWidth=8),
    Line(40, 10, 55, 10, lineWidth=8),
    Line(10, 50, 25, 50, lineWidth=8),
    Line(40, 50, 55, 50, lineWidth=8),
    Oval(50, 30, 5, 20),
    Line(25, 20, 50, 25, fill='dimGrey'),
    Line(25, 40, 50, 35, fill='dimGrey'),
    Oval(30, 30, 20, 30, fill='dimGrey'),
    Circle(30, 30, 10),
    Polygon(5, 30, -5, -10, -10, -10, -10, -8)
    )

player2 = Group(
    Oval(370, 370, 60, 40, fill=gradient('cornflowerBlue', 'white', start='left'),
         border='white', borderWidth=5),
    Line(390, 390, 375, 390, lineWidth=8),
    Line(360, 390, 345, 390, lineWidth=8),
    Line(390, 350, 375, 350, lineWidth=8),
    Line(360, 350, 345, 350, lineWidth=8),
    Oval(350, 370, 5, 20),
    Line(375, 380, 350, 375, fill='dimGrey'),
    Line(375, 360, 350, 365, fill='dimGrey'),
    Oval(370, 370, 20, 30, fill='dimGrey'),
    Circle(370, 370, 10),
    Polygon(395, 370, 405, 410, 410, 410, 410, 408)
    )

offenseInfo = Label('Player 1 is on Offense', 200, 20, fill='salmon', size=24)
Label('Time until switch:', 180, 50, fill='white', size=15)
timer = Label(50, 250, 50, fill='white', size=15)

def wrapPlayer(player):
    if (player.centerX > 400):
        player.centerX = 0
    elif (player.centerX < 0):
        player.centerX = 400

    if (player.centerY > 400):
        player.centerY = 0
    elif (player.centerY < 0):
        player.centerY = 400

def onKeyHold(keys):
    # Move player1 in response to the keys w-a-s-d (up-left-down-right).
    # Turn the car to the appropriate angle for each direction it moves.
    if ('w' in keys):
        player1.centerY -= 10
        player1.rotateAngle = -90
    if ('s' in keys):
        player1.centerY += 10
        player1.rotateAngle = 90
    if ('a' in keys):
        player1.centerX -= 10
        player1.rotateAngle = 180
    if ('d' in keys):
        player1.centerX += 10
        player1.rotateAngle = 0

    # Move player2 in response to the respective arrow keys. Turn the car
    # to the appropriate angle for each direction it moves.
    if ('up' in keys):
        player2.centerY -= 10
        player2.rotateAngle = 90
    if ('down' in keys):
        player2.centerY += 10
        player2.rotateAngle = -90
    if ('left' in keys):
        player2.centerX -= 10
        player2.rotateAngle = 0
    if ('right' in keys):
        player2.centerX += 10
        player2.rotateAngle = 180

    # Call the helper function to wrap the players around when they leave the
    # canvas.
    wrapPlayer(player1)
    wrapPlayer(player2)

    # End the game if the cars collide, and then display the winner.
    if (player1.hitsShape(player2) == True):
        if (offenseInfo.fill == 'salmon'):
            Label('Player 1 Wins!', 200, 20, fill='salmon', size=24)
        else:
            Label('Player 2 Wins!', 200, 20, fill='cornflowerBlue', size=24)

        offenseInfo.visible = False
        app.stop()

def onStep():
    # When the timer is 0, change who is on offense and reset the timer.
    timer.value -= 1
    if (timer.value <= 0):
        if (offenseInfo.fill == 'cornflowerBlue'):
            offenseInfo.value = 'Player 1 is on Offense'
            offenseInfo.fill = 'salmon'
            app.background = 'darkRed'
        else:
            offenseInfo.value = 'Player 2 is on Offense'
            offenseInfo.fill = 'cornflowerBlue'
            app.background = 'darkBlue'

        timer.value = 50

onKeyHolds(['up', 'left'], 20)
onKeyHolds(['d', 's'], 10)
app.paused = True


# -
app.background = 'darkRed'

# players
player1 = Group(
    Oval(30, 30, 60, 40, fill=gradient('salmon', 'white', start='left'),
         border='white', borderWidth=5),
    Line(10, 10, 25, 10, lineWidth=8),
    Line(40, 10, 55, 10, lineWidth=8),
    Line(10, 50, 25, 50, lineWidth=8),
    Line(40, 50, 55, 50, lineWidth=8),
    Oval(50, 30, 5, 20),
    Line(25, 20, 50, 25, fill='dimGrey'),
    Line(25, 40, 50, 35, fill='dimGrey'),
    Oval(30, 30, 20, 30, fill='dimGrey'),
    Circle(30, 30, 10),
    Polygon(5, 30, -5, -10, -10, -10, -10, -8)
    )

player2 = Group(
    Oval(370, 370, 60, 40, fill=gradient('cornflowerBlue', 'white', start='left'),
         border='white', borderWidth=5),
    Line(390, 390, 375, 390, lineWidth=8),
    Line(360, 390, 345, 390, lineWidth=8),
    Line(390, 350, 375, 350, lineWidth=8),
    Line(360, 350, 345, 350, lineWidth=8),
    Oval(350, 370, 5, 20),
    Line(375, 380, 350, 375, fill='dimGrey'),
    Line(375, 360, 350, 365, fill='dimGrey'),
    Oval(370, 370, 20, 30, fill='dimGrey'),
    Circle(370, 370, 10),
    Polygon(395, 370, 405, 410, 410, 410, 410, 408)
    )

offenseInfo = Label('Player 1 is on Offense', 200, 20, fill='salmon', size=24)
Label('Time until switch:', 180, 50, fill='white', size=15)
timer = Label(50, 250, 50, fill='white', size=15)

def wrapPlayer(player):
    if (player.centerX > 400):
        player.centerX = 0
    elif (player.centerX < 0):
        player.centerX = 400

    if (player.centerY > 400):
        player.centerY = 0
    elif (player.centerY < 0):
        player.centerY = 400

def onKeyHold(keys):
    # Move player1 in response to the keys w-a-s-d (up-left-down-right).
    # Turn the car to the appropriate angle for each direction it moves.
    if ('w' in keys):
        player1.centerY -= 10
        player1.rotateAngle = -90
    if ('s' in keys):
        player1.centerY += 10
        player1.rotateAngle = 90
    if ('a' in keys):
        player1.centerX -= 10
        player1.rotateAngle = 180
    if ('d' in keys):
        player1.centerX += 10
        player1.rotateAngle = 0

    # Move player2 in response to the respective arrow keys. Turn the car
    # to the appropriate angle for each direction it moves.
    if ('up' in keys):
        player2.centerY -= 10
        player2.rotateAngle = 90
    if ('down' in keys):
        player2.centerY += 10
        player2.rotateAngle = -90
    if ('left' in keys):
        player2.centerX -= 10
        player2.rotateAngle = 0
    if ('right' in keys):
        player2.centerX += 10
        player2.rotateAngle = 180

    # Call the helper function to wrap the players around when they leave the
    # canvas.
    wrapPlayer(player1)
    wrapPlayer(player2)

    # End the game if the cars collide, and then display the winner.
    if (player1.hitsShape(player2) == True):
        if (offenseInfo.fill == 'salmon'):
            Label('Player 1 Wins!', 200, 20, fill='salmon', size=24)
        else:
            Label('Player 2 Wins!', 200, 20, fill='cornflowerBlue', size=24)

        offenseInfo.visible = False
        app.stop()

def onStep():
    # When the timer is 0, change who is on offense and reset the timer.
    timer.value -= 1
    if (timer.value <= 0):
        if (offenseInfo.fill == 'cornflowerBlue'):
            offenseInfo.value = 'Player 1 is on Offense'
            offenseInfo.fill = 'salmon'
            app.background = 'darkRed'
        else:
            offenseInfo.value = 'Player 2 is on Offense'
            offenseInfo.fill = 'cornflowerBlue'
            app.background = 'darkBlue'

        timer.value = 50



# -
app.background = 'darkRed'

# players
player1 = Group(
    Oval(30, 30, 60, 40, fill=gradient('salmon', 'white', start='left'),
         border='white', borderWidth=5),
    Line(10, 10, 25, 10, lineWidth=8),
    Line(40, 10, 55, 10, lineWidth=8),
    Line(10, 50, 25, 50, lineWidth=8),
    Line(40, 50, 55, 50, lineWidth=8),
    Oval(50, 30, 5, 20),
    Line(25, 20, 50, 25, fill='dimGrey'),
    Line(25, 40, 50, 35, fill='dimGrey'),
    Oval(30, 30, 20, 30, fill='dimGrey'),
    Circle(30, 30, 10),
    Polygon(5, 30, -5, -10, -10, -10, -10, -8)
    )

player2 = Group(
    Oval(370, 370, 60, 40, fill=gradient('cornflowerBlue', 'white', start='left'),
         border='white', borderWidth=5),
    Line(390, 390, 375, 390, lineWidth=8),
    Line(360, 390, 345, 390, lineWidth=8),
    Line(390, 350, 375, 350, lineWidth=8),
    Line(360, 350, 345, 350, lineWidth=8),
    Oval(350, 370, 5, 20),
    Line(375, 380, 350, 375, fill='dimGrey'),
    Line(375, 360, 350, 365, fill='dimGrey'),
    Oval(370, 370, 20, 30, fill='dimGrey'),
    Circle(370, 370, 10),
    Polygon(395, 370, 405, 410, 410, 410, 410, 408)
    )

offenseInfo = Label('Player 1 is on Offense', 200, 20, fill='salmon', size=24)
Label('Time until switch:', 180, 50, fill='white', size=15)
timer = Label(50, 250, 50, fill='white', size=15)

def wrapPlayer(player):
    if (player.centerX > 400):
        player.centerX = 0
    elif (player.centerX < 0):
        player.centerX = 400

    if (player.centerY > 400):
        player.centerY = 0
    elif (player.centerY < 0):
        player.centerY = 400

def onKeyHold(keys):
    # Move player1 in response to the keys w-a-s-d (up-left-down-right).
    # Turn the car to the appropriate angle for each direction it moves.
    if ('w' in keys):
        player1.centerY -= 10
        player1.rotateAngle = -90
    if ('s' in keys):
        player1.centerY += 10
        player1.rotateAngle = 90
    if ('a' in keys):
        player1.centerX -= 10
        player1.rotateAngle = 180
    if ('d' in keys):
        player1.centerX += 10
        player1.rotateAngle = 0

    # Move player2 in response to the respective arrow keys. Turn the car
    # to the appropriate angle for each direction it moves.
    if ('up' in keys):
        player2.centerY -= 10
        player2.rotateAngle = 90
    if ('down' in keys):
        player2.centerY += 10
        player2.rotateAngle = -90
    if ('left' in keys):
        player2.centerX -= 10
        player2.rotateAngle = 0
    if ('right' in keys):
        player2.centerX += 10
        player2.rotateAngle = 180

    # Call the helper function to wrap the players around when they leave the
    # canvas.
    wrapPlayer(player1)
    wrapPlayer(player2)

    # End the game if the cars collide, and then display the winner.
    if (player1.hitsShape(player2) == True):
        if (offenseInfo.fill == 'salmon'):
            Label('Player 1 Wins!', 200, 20, fill='salmon', size=24)
        else:
            Label('Player 2 Wins!', 200, 20, fill='cornflowerBlue', size=24)

        offenseInfo.visible = False
        app.stop()

def onStep():
    # When the timer is 0, change who is on offense and reset the timer.
    timer.value -= 1
    if (timer.value <= 0):
        if (offenseInfo.fill == 'cornflowerBlue'):
            offenseInfo.value = 'Player 1 is on Offense'
            offenseInfo.fill = 'salmon'
            app.background = 'darkRed'
        else:
            offenseInfo.value = 'Player 2 is on Offense'
            offenseInfo.fill = 'cornflowerBlue'
            app.background = 'darkBlue'

        timer.value = 50

onKeyHolds(['left', 'd'], 30)
onKeyHolds(['up', 's'], 20)
onKeyHolds(['right', 'a'], 10)
app.paused = True

