app.background = gradient('mediumSeaGreen', 'darkGreen')

# anthill
Circle(200, 200, 175, fill=gradient('peru', rgb(60, 30, 20)))
Star(200, 200, 175, 23, fill=gradient('peru', rgb(60, 30, 20)), opacity=70,
     roundness=5)
Circle(200, 200, 30, border=rgb(60, 30, 20), borderWidth=4)

ants = Star(200, 200, 25, 9, fill=None, border='black', dashes=True,
            roundness=1)

def onKeyHold(keys):
    # When the spacebar is held, change the size of the dashed shape
    # by 3 to make the ants look like they are moving.
    if ('space' in keys):
        ants.radius += 3

onKeyHolds(['space'], 50)


# -
app.background = gradient('mediumSeaGreen', 'darkGreen')

# anthill
Circle(200, 200, 175, fill=gradient('peru', rgb(60, 30, 20)))
Star(200, 200, 175, 23, fill=gradient('peru', rgb(60, 30, 20)), opacity=70,
     roundness=5)
Circle(200, 200, 30, border=rgb(60, 30, 20), borderWidth=4)

ants = Star(200, 200, 25, 9, fill=None, border='black', dashes=True,
            roundness=1)

def onKeyHold(keys):
    # When the spacebar is held, change the size of the dashed shape
    # by 3 to make the ants look like they are moving.
    if ('space' in keys):
        ants.radius += 3

onKeyHolds(['space'], 50)


# -
app.background = gradient('mediumSeaGreen', 'darkGreen')

# anthill
Circle(200, 200, 175, fill=gradient('peru', rgb(60, 30, 20)))
Star(200, 200, 175, 23, fill=gradient('peru', rgb(60, 30, 20)), opacity=70,
     roundness=5)
Circle(200, 200, 30, border=rgb(60, 30, 20), borderWidth=4)

ants = Star(200, 200, 25, 9, fill=None, border='black', dashes=True,
            roundness=1)

def onKeyHold(keys):
    # When the spacebar is held, change the size of the dashed shape
    # by 3 to make the ants look like they are moving.
    if ('space' in keys):
        ants.radius += 3

onKeyHolds(['a'], 10)
onKeyHolds(['5'], 10)
onKeyHolds(['left'], 10)

