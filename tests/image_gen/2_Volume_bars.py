app.background = 'black'

leftVolumeBar = Line(75, 300, 75, 400, lineWidth=100, dashes=True,
                     fill=gradient('black', 'red', 'orange', 'yellow',
                                   'lawnGreen', start='top'))
centerVolumeBar = Line(200, 300, 200, 400, lineWidth=100, dashes=True,
                       fill=gradient('black', 'red', 'orange', 'yellow',
                                     'lawnGreen', start='top'))
rightVolumeBar = Line(325, 300, 325, 400, lineWidth=100, dashes=True,
                      fill=gradient('black', 'red', 'orange', 'yellow',
                                    'lawnGreen', start='top'))

def setVolumeBars(newLeftBarY1, newCenterBarY1, newRightBarY1):
    # Set each volume bar to new y1 value.
    leftVolumeBar.y1 = newLeftBarY1
    centerVolumeBar.y1 = newCenterBarY1
    rightVolumeBar.y1 = newRightBarY1

def onMouseMove(mouseX, mouseY):
    # Change the height of volume bars based on which volume bar the mouse is above.
    if (mouseX < 125):
        setVolumeBars(mouseY, 400 - mouseY, 400 - mouseY)
    elif (mouseX < 275):
        setVolumeBars(400 - mouseY, mouseY, 400 - mouseY)
    else:
        setVolumeBars(400 - mouseY, 400 - mouseY, mouseY)

onMouseMove(200, 200)


# -
app.background = 'black'

leftVolumeBar = Line(75, 300, 75, 400, lineWidth=100, dashes=True,
                     fill=gradient('black', 'red', 'orange', 'yellow',
                                   'lawnGreen', start='top'))
centerVolumeBar = Line(200, 300, 200, 400, lineWidth=100, dashes=True,
                       fill=gradient('black', 'red', 'orange', 'yellow',
                                     'lawnGreen', start='top'))
rightVolumeBar = Line(325, 300, 325, 400, lineWidth=100, dashes=True,
                      fill=gradient('black', 'red', 'orange', 'yellow',
                                    'lawnGreen', start='top'))

def setVolumeBars(newLeftBarY1, newCenterBarY1, newRightBarY1):
    # Set each volume bar to new y1 value.
    leftVolumeBar.y1 = newLeftBarY1
    centerVolumeBar.y1 = newCenterBarY1
    rightVolumeBar.y1 = newRightBarY1

def onMouseMove(mouseX, mouseY):
    # Change the height of volume bars based on which volume bar the mouse is above.
    if (mouseX < 125):
        setVolumeBars(mouseY, 400 - mouseY, 400 - mouseY)
    elif (mouseX < 275):
        setVolumeBars(400 - mouseY, mouseY, 400 - mouseY)
    else:
        setVolumeBars(400 - mouseY, 400 - mouseY, mouseY)

onMouseMove(295, 325)


# -
app.background = 'black'

leftVolumeBar = Line(75, 300, 75, 400, lineWidth=100, dashes=True,
                     fill=gradient('black', 'red', 'orange', 'yellow',
                                   'lawnGreen', start='top'))
centerVolumeBar = Line(200, 300, 200, 400, lineWidth=100, dashes=True,
                       fill=gradient('black', 'red', 'orange', 'yellow',
                                     'lawnGreen', start='top'))
rightVolumeBar = Line(325, 300, 325, 400, lineWidth=100, dashes=True,
                      fill=gradient('black', 'red', 'orange', 'yellow',
                                    'lawnGreen', start='top'))

def setVolumeBars(newLeftBarY1, newCenterBarY1, newRightBarY1):
    # Set each volume bar to new y1 value.
    leftVolumeBar.y1 = newLeftBarY1
    centerVolumeBar.y1 = newCenterBarY1
    rightVolumeBar.y1 = newRightBarY1

def onMouseMove(mouseX, mouseY):
    # Change the height of volume bars based on which volume bar the mouse is above.
    if (mouseX < 125):
        setVolumeBars(mouseY, 400 - mouseY, 400 - mouseY)
    elif (mouseX < 275):
        setVolumeBars(400 - mouseY, mouseY, 400 - mouseY)
    else:
        setVolumeBars(400 - mouseY, 400 - mouseY, mouseY)

onMouseMove(180, 40)
onMouseMove(350, 200)
onMouseMove(290, 330)
onMouseMove(340, 70)
onMouseMove(360, 150)
onMouseMove(200, 270)

