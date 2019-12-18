app.background = rgb(220, 215, 205)

# casing
Rect(50, 300, 300, 100, fill=rgb(55, 55, 55))
Rect(80, 315, 240, 30, fill='silver')
Label('DO NOT TOUCH', 200, 330, size=25)

meteorite = Polygon(150, 300, 120, 250, 140, 220, 170, 170, 210, 150, 260, 190,
                    270, 230, 300, 260, 280, 280, 240, 300,
                    fill=gradient(rgb(110, 185, 160), rgb(10, 50, 45),
                                  start='left-top'))
cover = Rect(50, 75, 300, 225, fill=gradient('white', 'azure', start='left-top'),
             opacity=20)

Rect(50, 75, 300, 275, fill=None, border=rgb(90, 80, 80))

alarm = Polygon(150, 0, 250, 0, 230, 40, 170, 40,
                fill=gradient('lightGrey', 'darkGrey'))
light = Polygon(170, 40, 230, 40, 320, 300, 80, 300, fill='lightYellow',
                opacity=20)
alarmCover = Rect(0, 0, 400, 400, fill='red', opacity=50, visible=False)
alarmLights = Star(200, 0, 500, 10, fill='white', opacity=50, visible=False,
                   roundness=20)

hand = Oval(25, 50, 50, 50, fill='whiteSmoke')

def onMouseMove(mouseX, mouseY):
    hand.centerX = mouseX
    hand.centerY = mouseY

    # If the hand (cursor) intersects the meteorite, show the alarm and rotate
    # the alarm lights. Otherwise, restore the original background.
    if (hand.hitsShape(meteorite) == True):
        app.background = 'fireBrick'
        alarmCover.visible = True
        alarmLights.visible = True
        light.visible = False
        alarmLights.rotateAngle += 5
    else:
        app.background = rgb(220, 215, 205)
        alarmCover.visible = False
        alarmLights.visible = False
        light.visible = True

onMouseMove(200, 200)


# -
app.background = rgb(220, 215, 205)

# casing
Rect(50, 300, 300, 100, fill=rgb(55, 55, 55))
Rect(80, 315, 240, 30, fill='silver')
Label('DO NOT TOUCH', 200, 330, size=25)

meteorite = Polygon(150, 300, 120, 250, 140, 220, 170, 170, 210, 150, 260, 190,
                    270, 230, 300, 260, 280, 280, 240, 300,
                    fill=gradient(rgb(110, 185, 160), rgb(10, 50, 45),
                                  start='left-top'))
cover = Rect(50, 75, 300, 225, fill=gradient('white', 'azure', start='left-top'),
             opacity=20)

Rect(50, 75, 300, 275, fill=None, border=rgb(90, 80, 80))

alarm = Polygon(150, 0, 250, 0, 230, 40, 170, 40,
                fill=gradient('lightGrey', 'darkGrey'))
light = Polygon(170, 40, 230, 40, 320, 300, 80, 300, fill='lightYellow',
                opacity=20)
alarmCover = Rect(0, 0, 400, 400, fill='red', opacity=50, visible=False)
alarmLights = Star(200, 0, 500, 10, fill='white', opacity=50, visible=False,
                   roundness=20)

hand = Oval(25, 50, 50, 50, fill='whiteSmoke')

def onMouseMove(mouseX, mouseY):
    hand.centerX = mouseX
    hand.centerY = mouseY

    # If the hand (cursor) intersects the meteorite, show the alarm and rotate
    # the alarm lights. Otherwise, restore the original background.
    if (hand.hitsShape(meteorite) == True):
        app.background = 'fireBrick'
        alarmCover.visible = True
        alarmLights.visible = True
        light.visible = False
        alarmLights.rotateAngle += 5
    else:
        app.background = rgb(220, 215, 205)
        alarmCover.visible = False
        alarmLights.visible = False
        light.visible = True



# -
app.background = rgb(220, 215, 205)

# casing
Rect(50, 300, 300, 100, fill=rgb(55, 55, 55))
Rect(80, 315, 240, 30, fill='silver')
Label('DO NOT TOUCH', 200, 330, size=25)

meteorite = Polygon(150, 300, 120, 250, 140, 220, 170, 170, 210, 150, 260, 190,
                    270, 230, 300, 260, 280, 280, 240, 300,
                    fill=gradient(rgb(110, 185, 160), rgb(10, 50, 45),
                                  start='left-top'))
cover = Rect(50, 75, 300, 225, fill=gradient('white', 'azure', start='left-top'),
             opacity=20)

Rect(50, 75, 300, 275, fill=None, border=rgb(90, 80, 80))

alarm = Polygon(150, 0, 250, 0, 230, 40, 170, 40,
                fill=gradient('lightGrey', 'darkGrey'))
light = Polygon(170, 40, 230, 40, 320, 300, 80, 300, fill='lightYellow',
                opacity=20)
alarmCover = Rect(0, 0, 400, 400, fill='red', opacity=50, visible=False)
alarmLights = Star(200, 0, 500, 10, fill='white', opacity=50, visible=False,
                   roundness=20)

hand = Oval(25, 50, 50, 50, fill='whiteSmoke')

def onMouseMove(mouseX, mouseY):
    hand.centerX = mouseX
    hand.centerY = mouseY

    # If the hand (cursor) intersects the meteorite, show the alarm and rotate
    # the alarm lights. Otherwise, restore the original background.
    if (hand.hitsShape(meteorite) == True):
        app.background = 'fireBrick'
        alarmCover.visible = True
        alarmLights.visible = True
        light.visible = False
        alarmLights.rotateAngle += 5
    else:
        app.background = rgb(220, 215, 205)
        alarmCover.visible = False
        alarmLights.visible = False
        light.visible = True


