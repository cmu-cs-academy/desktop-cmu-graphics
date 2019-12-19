# background
Rect(0, 0, 400, 400, fill='lavenderBlush')

# This draws the voice.
voice = Star(140, 215, 75, 8, roundness=10, visible=False)
Rect(80, 135, 75, 160, fill='lavenderBlush')

# face
Oval(30, 140, 230, 350, fill='lightSkyBlue')
Polygon(0, 0, 130, 0, 145, 60, 180, 130, 145, 155, 0, 210, fill='lightSkyBlue')
eye = Circle(80, 50, 15)

mouth = Polygon(150, 185, 80, 185, 95, 225, 140, 250, fill='lavenderBlush',
                visible=False)

def onMousePress(x, y):
    voice.visible = True
    mouth.visible = True
    eye.radius = 20

def onMouseRelease(x, y):
    voice.visible = False
    mouth.visible = False
    eye.radius = 15

onMousePress(100, 100)
onMouseRelease(100, 100)
onMousePress(200, 200)


# -
# background
Rect(0, 0, 400, 400, fill='lavenderBlush')

# This draws the voice.
voice = Star(140, 215, 75, 8, roundness=10, visible=False)
Rect(80, 135, 75, 160, fill='lavenderBlush')

# face
Oval(30, 140, 230, 350, fill='lightSkyBlue')
Polygon(0, 0, 130, 0, 145, 60, 180, 130, 145, 155, 0, 210, fill='lightSkyBlue')
eye = Circle(80, 50, 15)

mouth = Polygon(150, 185, 80, 185, 95, 225, 140, 250, fill='lavenderBlush',
                visible=False)

def onMousePress(x, y):
    voice.visible = True
    mouth.visible = True
    eye.radius = 20

def onMouseRelease(x, y):
    voice.visible = False
    mouth.visible = False
    eye.radius = 15

onMousePress(100, 100)


# -
# background
Rect(0, 0, 400, 400, fill='lavenderBlush')

# This draws the voice.
voice = Star(140, 215, 75, 8, roundness=10, visible=False)
Rect(80, 135, 75, 160, fill='lavenderBlush')

# face
Oval(30, 140, 230, 350, fill='lightSkyBlue')
Polygon(0, 0, 130, 0, 145, 60, 180, 130, 145, 155, 0, 210, fill='lightSkyBlue')
eye = Circle(80, 50, 15)

mouth = Polygon(150, 185, 80, 185, 95, 225, 140, 250, fill='lavenderBlush',
                visible=False)

def onMousePress(x, y):
    voice.visible = True
    mouth.visible = True
    eye.radius = 20

def onMouseRelease(x, y):
    voice.visible = False
    mouth.visible = False
    eye.radius = 15

onMousePress(100, 200)
onMouseRelease(100, 200)

