app.background = gradient('skyBlue', 'paleTurquoise', start='top')

star1 = Star(200, 200, 175, 8, fill=gradient('darkViolet', 'mediumOrchid'),
             roundness=50, opacity=40)
star2 = Star(200, 200, 175, 8, fill=gradient('mediumBlue', 'midnightBlue'),
             roundness=50, opacity=40)

def onKeyHold(keys):
    # When holding the up key, increase the roundness of star1 and
    # decrease that of star2.
    # When holding the down key, change the roundness in the opposite directions
    if ('up' in keys):
        if (star2.roundness == 0):
            star1.roundness = 0
            star2.roundness = 100
        else:
            star1.roundness += 2
            star2.roundness -= 2
    elif ('down' in keys):
        if (star1.roundness == 0):
            star1.roundness = 100
            star2.roundness = 0
        else:
            star1.roundness -= 2
            star2.roundness += 2



# -
app.background = gradient('skyBlue', 'paleTurquoise', start='top')

star1 = Star(200, 200, 175, 8, fill=gradient('darkViolet', 'mediumOrchid'),
             roundness=50, opacity=40)
star2 = Star(200, 200, 175, 8, fill=gradient('mediumBlue', 'midnightBlue'),
             roundness=50, opacity=40)

def onKeyHold(keys):
    # When holding the up key, increase the roundness of star1 and
    # decrease that of star2.
    # When holding the down key, change the roundness in the opposite directions
    if ('up' in keys):
        if (star2.roundness == 0):
            star1.roundness = 0
            star2.roundness = 100
        else:
            star1.roundness += 2
            star2.roundness -= 2
    elif ('down' in keys):
        if (star1.roundness == 0):
            star1.roundness = 100
            star2.roundness = 0
        else:
            star1.roundness -= 2
            star2.roundness += 2

onKeyHolds(['up'], 8)
onKeyHolds(['down'], 8)


# -
app.background = gradient('skyBlue', 'paleTurquoise', start='top')

star1 = Star(200, 200, 175, 8, fill=gradient('darkViolet', 'mediumOrchid'),
             roundness=50, opacity=40)
star2 = Star(200, 200, 175, 8, fill=gradient('mediumBlue', 'midnightBlue'),
             roundness=50, opacity=40)

def onKeyHold(keys):
    # When holding the up key, increase the roundness of star1 and
    # decrease that of star2.
    # When holding the down key, change the roundness in the opposite directions
    if ('up' in keys):
        if (star2.roundness == 0):
            star1.roundness = 0
            star2.roundness = 100
        else:
            star1.roundness += 2
            star2.roundness -= 2
    elif ('down' in keys):
        if (star1.roundness == 0):
            star1.roundness = 100
            star2.roundness = 0
        else:
            star1.roundness -= 2
            star2.roundness += 2

onKeyHolds(['up'], 10)
onKeyHolds(['down'], 12)

