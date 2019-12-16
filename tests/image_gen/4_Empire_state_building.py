app.background = gradient(rgb(165, 115, 180), rgb(235, 160, 130),
                          rgb(225, 190, 165), start='top')

# background buildings
Rect(30, 200, 70, 200, fill=rgb(98, 86, 110))
Rect(0, 240, 50, 202, fill=rgb(60, 46, 75))
Rect(80, 230, 60, 172, fill=rgb(60, 46, 75))

Rect(320, 190, 50, 212, fill=rgb(98, 86, 110))
Rect(360, 220, 40, 182, fill=rgb(60, 46, 75))
Rect(290, 260, 60, 142, fill=rgb(60, 46, 75))

# building
Polygon(110, 400, 290, 400, 290, 340, 280, 340, 280, 300, 250, 300, 250, 85,
        230, 85, 230, 65, 170, 65, 170, 85, 150, 85, 150, 300, 120, 300, 120,
        340, 110, 340, fill=rgb(16, 5, 16))
Polygon(195, 65, 200, 0, 205, 65, fill=rgb(15, 5, 15))

Line(170, 85, 170, 400, fill=rgb(80, 70, 85))
Line(230, 85, 230, 400, fill=rgb(80, 70, 85))
Line(200, 80, 200, 400, fill=rgb(225, 225, 190), lineWidth=10, dashes=True)

# elevator
elevator = Rect(190, 378, 20, 22, fill=rgb(70, 65, 85))

# display the floor we are on
Label('Floor', 320, 60, fill='snow', size=26)
floor = Label(0, 320, 100, fill='snow', size=38)

def onKeyHold(keys):
    # Move the elevator up and down the floor when those arrow keys are
    # pressed. There are 102 floors in the Empire State Building, the elevator
    # cannot go higher than that. You also cannot go below floor 0.
    if ('up' in keys):
        if (floor.value < 102):
            elevator.centerY -= 3
            floor.value += 1
    if ('down' in keys):
        if (floor.value > 0):
            elevator.centerY += 3
            floor.value -= 1

onKeyHolds(['up'], 10)
onKeyHolds(['down'], 20)


# -
app.background = gradient(rgb(165, 115, 180), rgb(235, 160, 130),
                          rgb(225, 190, 165), start='top')

# background buildings
Rect(30, 200, 70, 200, fill=rgb(98, 86, 110))
Rect(0, 240, 50, 202, fill=rgb(60, 46, 75))
Rect(80, 230, 60, 172, fill=rgb(60, 46, 75))

Rect(320, 190, 50, 212, fill=rgb(98, 86, 110))
Rect(360, 220, 40, 182, fill=rgb(60, 46, 75))
Rect(290, 260, 60, 142, fill=rgb(60, 46, 75))

# building
Polygon(110, 400, 290, 400, 290, 340, 280, 340, 280, 300, 250, 300, 250, 85,
        230, 85, 230, 65, 170, 65, 170, 85, 150, 85, 150, 300, 120, 300, 120,
        340, 110, 340, fill=rgb(16, 5, 16))
Polygon(195, 65, 200, 0, 205, 65, fill=rgb(15, 5, 15))

Line(170, 85, 170, 400, fill=rgb(80, 70, 85))
Line(230, 85, 230, 400, fill=rgb(80, 70, 85))
Line(200, 80, 200, 400, fill=rgb(225, 225, 190), lineWidth=10, dashes=True)

# elevator
elevator = Rect(190, 378, 20, 22, fill=rgb(70, 65, 85))

# display the floor we are on
Label('Floor', 320, 60, fill='snow', size=26)
floor = Label(0, 320, 100, fill='snow', size=38)

def onKeyHold(keys):
    # Move the elevator up and down the floor when those arrow keys are
    # pressed. There are 102 floors in the Empire State Building, the elevator
    # cannot go higher than that. You also cannot go below floor 0.
    if ('up' in keys):
        if (floor.value < 102):
            elevator.centerY -= 3
            floor.value += 1
    if ('down' in keys):
        if (floor.value > 0):
            elevator.centerY += 3
            floor.value -= 1

onKeyHolds(['down'], 10)


# -
app.background = gradient(rgb(165, 115, 180), rgb(235, 160, 130),
                          rgb(225, 190, 165), start='top')

# background buildings
Rect(30, 200, 70, 200, fill=rgb(98, 86, 110))
Rect(0, 240, 50, 202, fill=rgb(60, 46, 75))
Rect(80, 230, 60, 172, fill=rgb(60, 46, 75))

Rect(320, 190, 50, 212, fill=rgb(98, 86, 110))
Rect(360, 220, 40, 182, fill=rgb(60, 46, 75))
Rect(290, 260, 60, 142, fill=rgb(60, 46, 75))

# building
Polygon(110, 400, 290, 400, 290, 340, 280, 340, 280, 300, 250, 300, 250, 85,
        230, 85, 230, 65, 170, 65, 170, 85, 150, 85, 150, 300, 120, 300, 120,
        340, 110, 340, fill=rgb(16, 5, 16))
Polygon(195, 65, 200, 0, 205, 65, fill=rgb(15, 5, 15))

Line(170, 85, 170, 400, fill=rgb(80, 70, 85))
Line(230, 85, 230, 400, fill=rgb(80, 70, 85))
Line(200, 80, 200, 400, fill=rgb(225, 225, 190), lineWidth=10, dashes=True)

# elevator
elevator = Rect(190, 378, 20, 22, fill=rgb(70, 65, 85))

# display the floor we are on
Label('Floor', 320, 60, fill='snow', size=26)
floor = Label(0, 320, 100, fill='snow', size=38)

def onKeyHold(keys):
    # Move the elevator up and down the floor when those arrow keys are
    # pressed. There are 102 floors in the Empire State Building, the elevator
    # cannot go higher than that. You also cannot go below floor 0.
    if ('up' in keys):
        if (floor.value < 102):
            elevator.centerY -= 3
            floor.value += 1
    if ('down' in keys):
        if (floor.value > 0):
            elevator.centerY += 3
            floor.value -= 1

onKeyHolds(['up'], 125)

