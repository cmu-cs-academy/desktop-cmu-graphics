app.background = gradient('skyBlue', rgb(235, 235, 235), start='top')

# volcano
lava = Oval(200, 120, 90, 20, fill=rgb(255, 200, 0), border='peru',
            borderWidth=4)
lava.green = 200

rock = Polygon(0, 400, 0, 380, 50, 340, 70, 300, 125, 225, 140, 180, 153, 120,
               175, 125, 200, 120, 220, 108, 235, 105, 247, 110, 255, 175, 270,
               210, 310, 250, 350, 325, 400, 375, 400, 400,
               fill=gradient('peru', 'sienna', start='top'))

# lava explosion
burst = Polygon(100, 0, 310, 0, 260, 30, 245, 60, 240, 110, 235, 105, 220,
                108, 200, 120, 175, 125, 160, 120, 150, 60, 130, 25,
                fill=gradient(rgb(255, 200, 75), rgb(235, 10, 20), start='bottom'),
                visible=False)

def drawSpill():
    Polygon(153, 120, 175, 125, 165, 195, 145, 260,
            80, 315, 125, 260, 150, 200, 155, 160,
            fill=gradient(rgb(255, 200, 75), rgb(235, 10, 20), start='top'))
    Polygon(200, 120, 220, 108, 230, 160, 230, 210,
            240, 240, 310, 345, 245, 280, 215, 225, 210, 160,
            fill=gradient(rgb(255, 200, 75), rgb(235, 10, 20), start='top'))
    Polygon(235, 105, 247, 110, 255, 175, 270, 210,
            310, 250, 255, 215, 240, 170, 240, 130,
            fill=gradient(rgb(255, 200, 75), rgb(235, 10, 20), start='top'))

def onMousePress(mouseX, mouseY):
    # Decrease the green in the lava color until there is no green.
    if (lava.green > 0):
        lava.green -= 40
        lava.fill = rgb(255, lava.green, 0)
    # Otherwise, the volcano should explode.
    else:
        burst.visible = True
        app.background = gradient('lightSlateGrey', 'lightGrey', start='top')
        drawSpill()

onMousePress(100, 100)
onMousePress(100, 100)
onMousePress(100, 100)
onMousePress(100, 100)
onMousePress(100, 100)
onMousePress(100, 100)
onMousePress(100, 100)
onMousePress(100, 100)


# -
app.background = gradient('skyBlue', rgb(235, 235, 235), start='top')

# volcano
lava = Oval(200, 120, 90, 20, fill=rgb(255, 200, 0), border='peru',
            borderWidth=4)
lava.green = 200

rock = Polygon(0, 400, 0, 380, 50, 340, 70, 300, 125, 225, 140, 180, 153, 120,
               175, 125, 200, 120, 220, 108, 235, 105, 247, 110, 255, 175, 270,
               210, 310, 250, 350, 325, 400, 375, 400, 400,
               fill=gradient('peru', 'sienna', start='top'))

# lava explosion
burst = Polygon(100, 0, 310, 0, 260, 30, 245, 60, 240, 110, 235, 105, 220,
                108, 200, 120, 175, 125, 160, 120, 150, 60, 130, 25,
                fill=gradient(rgb(255, 200, 75), rgb(235, 10, 20), start='bottom'),
                visible=False)

def drawSpill():
    Polygon(153, 120, 175, 125, 165, 195, 145, 260,
            80, 315, 125, 260, 150, 200, 155, 160,
            fill=gradient(rgb(255, 200, 75), rgb(235, 10, 20), start='top'))
    Polygon(200, 120, 220, 108, 230, 160, 230, 210,
            240, 240, 310, 345, 245, 280, 215, 225, 210, 160,
            fill=gradient(rgb(255, 200, 75), rgb(235, 10, 20), start='top'))
    Polygon(235, 105, 247, 110, 255, 175, 270, 210,
            310, 250, 255, 215, 240, 170, 240, 130,
            fill=gradient(rgb(255, 200, 75), rgb(235, 10, 20), start='top'))

def onMousePress(mouseX, mouseY):
    # Decrease the green in the lava color until there is no green.
    if (lava.green > 0):
        lava.green -= 40
        lava.fill = rgb(255, lava.green, 0)
    # Otherwise, the volcano should explode.
    else:
        burst.visible = True
        app.background = gradient('lightSlateGrey', 'lightGrey', start='top')
        drawSpill()

onMousePress(100, 100)
onMousePress(100, 100)


# -
app.background = gradient('skyBlue', rgb(235, 235, 235), start='top')

# volcano
lava = Oval(200, 120, 90, 20, fill=rgb(255, 200, 0), border='peru',
            borderWidth=4)
lava.green = 200

rock = Polygon(0, 400, 0, 380, 50, 340, 70, 300, 125, 225, 140, 180, 153, 120,
               175, 125, 200, 120, 220, 108, 235, 105, 247, 110, 255, 175, 270,
               210, 310, 250, 350, 325, 400, 375, 400, 400,
               fill=gradient('peru', 'sienna', start='top'))

# lava explosion
burst = Polygon(100, 0, 310, 0, 260, 30, 245, 60, 240, 110, 235, 105, 220,
                108, 200, 120, 175, 125, 160, 120, 150, 60, 130, 25,
                fill=gradient(rgb(255, 200, 75), rgb(235, 10, 20), start='bottom'),
                visible=False)

def drawSpill():
    Polygon(153, 120, 175, 125, 165, 195, 145, 260,
            80, 315, 125, 260, 150, 200, 155, 160,
            fill=gradient(rgb(255, 200, 75), rgb(235, 10, 20), start='top'))
    Polygon(200, 120, 220, 108, 230, 160, 230, 210,
            240, 240, 310, 345, 245, 280, 215, 225, 210, 160,
            fill=gradient(rgb(255, 200, 75), rgb(235, 10, 20), start='top'))
    Polygon(235, 105, 247, 110, 255, 175, 270, 210,
            310, 250, 255, 215, 240, 170, 240, 130,
            fill=gradient(rgb(255, 200, 75), rgb(235, 10, 20), start='top'))

def onMousePress(mouseX, mouseY):
    # Decrease the green in the lava color until there is no green.
    if (lava.green > 0):
        lava.green -= 40
        lava.fill = rgb(255, lava.green, 0)
    # Otherwise, the volcano should explode.
    else:
        burst.visible = True
        app.background = gradient('lightSlateGrey', 'lightGrey', start='top')
        drawSpill()

onMousePress(100, 100)

