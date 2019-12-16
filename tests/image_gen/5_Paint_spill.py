# background
Line(200, 0, 200, 400, fill='lightGrey', lineWidth=400, dashes=(30, 30))
Line(0, 200, 400, 200, fill='cornflowerBlue', lineWidth=400, opacity=50,
     dashes=(30, 30))
Line(0, 200, 400, 200, fill='grey', lineWidth=400, opacity=50, dashes=(3, 27))
Line(200, 0, 200, 400, fill='grey', lineWidth=400, opacity=50, dashes=(3, 27))

Label('All clean!', 200, 200, size=35)
Rect(360, 400, 100, 100, fill='grey', rotateAngle=-125, align='center')
Oval(330, 358, 100, 30, fill='dimGrey', border='slateGrey', borderWidth=5,
     rotateAngle=-35)

paint1 = Group(
    Circle(300, 300, 75, fill='mediumTurquoise'),
    Circle(350, 265, 75, fill='mediumTurquoise'),
    Circle(240, 325, 75, fill='mediumTurquoise')
    )

paint2 = Group(
    Circle(125, 280, 100, fill='mediumTurquoise'),
    Circle(200, 180, 100, fill='mediumTurquoise'),
    Circle(110, 180, 75, fill='mediumTurquoise')
    )

paint3 = Group(
    Circle(300, 180, 70, fill='mediumTurquoise'),
    Circle(270, 100, 60, fill='mediumTurquoise'),
    Circle(355, 140, 70, fill='mediumTurquoise')
    )

sponge = Rect(10, 10, 25, 50, fill='gold')

def onMouseMove(mouseX, mouseY):
    sponge.centerX = mouseX
    sponge.centerY = mouseY

    # Check if any of the paint groups hit the sponge and decrease their opacity
    # if so. When an opacity gets below 3, clear that paint group.
    if (paint1.hitsShape(sponge) == True):
        paint1.opacity -= 2
        if (paint1.opacity <= 2):
            paint1.clear()
    if (paint2.hitsShape(sponge) == True):
        paint2.opacity -= 2
        if (paint2.opacity <= 2):
            paint2.clear()
    if (paint3.hitsShape(sponge) == True):
        paint3.opacity -= 2
        if (paint3.opacity <= 2):
            paint3.clear()

onMouseMove(100, 100)
onMouseMove(100, 200)
onMouseMove(50, 300)
onMouseMove(100, 100)
onMouseMove(330, 70)
onMouseMove(270, 100)
onMouseMove(350, 130)
onMouseMove(330, 70)
onMouseMove(300, 300)
onMouseMove(250, 350)
onMouseMove(350, 200)
onMouseMove(300, 300)


# -
# background
Line(200, 0, 200, 400, fill='lightGrey', lineWidth=400, dashes=(30, 30))
Line(0, 200, 400, 200, fill='cornflowerBlue', lineWidth=400, opacity=50,
     dashes=(30, 30))
Line(0, 200, 400, 200, fill='grey', lineWidth=400, opacity=50, dashes=(3, 27))
Line(200, 0, 200, 400, fill='grey', lineWidth=400, opacity=50, dashes=(3, 27))

Label('All clean!', 200, 200, size=35)
Rect(360, 400, 100, 100, fill='grey', rotateAngle=-125, align='center')
Oval(330, 358, 100, 30, fill='dimGrey', border='slateGrey', borderWidth=5,
     rotateAngle=-35)

paint1 = Group(
    Circle(300, 300, 75, fill='mediumTurquoise'),
    Circle(350, 265, 75, fill='mediumTurquoise'),
    Circle(240, 325, 75, fill='mediumTurquoise')
    )

paint2 = Group(
    Circle(125, 280, 100, fill='mediumTurquoise'),
    Circle(200, 180, 100, fill='mediumTurquoise'),
    Circle(110, 180, 75, fill='mediumTurquoise')
    )

paint3 = Group(
    Circle(300, 180, 70, fill='mediumTurquoise'),
    Circle(270, 100, 60, fill='mediumTurquoise'),
    Circle(355, 140, 70, fill='mediumTurquoise')
    )

sponge = Rect(10, 10, 25, 50, fill='gold')

def onMouseMove(mouseX, mouseY):
    sponge.centerX = mouseX
    sponge.centerY = mouseY

    # Check if any of the paint groups hit the sponge and decrease their opacity
    # if so. When an opacity gets below 3, clear that paint group.
    if (paint1.hitsShape(sponge) == True):
        paint1.opacity -= 2
        if (paint1.opacity <= 2):
            paint1.clear()
    if (paint2.hitsShape(sponge) == True):
        paint2.opacity -= 2
        if (paint2.opacity <= 2):
            paint2.clear()
    if (paint3.hitsShape(sponge) == True):
        paint3.opacity -= 2
        if (paint3.opacity <= 2):
            paint3.clear()

onMouseMove(100, 100)
onMouseMove(100, 200)
onMouseMove(50, 300)
onMouseMove(100, 100)
onMouseMove(330, 70)
onMouseMove(270, 100)
onMouseMove(350, 130)
onMouseMove(330, 70)
onMouseMove(300, 300)
onMouseMove(250, 350)
onMouseMove(350, 200)
onMouseMove(300, 300)


# -
# background
Line(200, 0, 200, 400, fill='lightGrey', lineWidth=400, dashes=(30, 30))
Line(0, 200, 400, 200, fill='cornflowerBlue', lineWidth=400, opacity=50,
     dashes=(30, 30))
Line(0, 200, 400, 200, fill='grey', lineWidth=400, opacity=50, dashes=(3, 27))
Line(200, 0, 200, 400, fill='grey', lineWidth=400, opacity=50, dashes=(3, 27))

Label('All clean!', 200, 200, size=35)
Rect(360, 400, 100, 100, fill='grey', rotateAngle=-125, align='center')
Oval(330, 358, 100, 30, fill='dimGrey', border='slateGrey', borderWidth=5,
     rotateAngle=-35)

paint1 = Group(
    Circle(300, 300, 75, fill='mediumTurquoise'),
    Circle(350, 265, 75, fill='mediumTurquoise'),
    Circle(240, 325, 75, fill='mediumTurquoise')
    )

paint2 = Group(
    Circle(125, 280, 100, fill='mediumTurquoise'),
    Circle(200, 180, 100, fill='mediumTurquoise'),
    Circle(110, 180, 75, fill='mediumTurquoise')
    )

paint3 = Group(
    Circle(300, 180, 70, fill='mediumTurquoise'),
    Circle(270, 100, 60, fill='mediumTurquoise'),
    Circle(355, 140, 70, fill='mediumTurquoise')
    )

sponge = Rect(10, 10, 25, 50, fill='gold')

def onMouseMove(mouseX, mouseY):
    sponge.centerX = mouseX
    sponge.centerY = mouseY

    # Check if any of the paint groups hit the sponge and decrease their opacity
    # if so. When an opacity gets below 3, clear that paint group.
    if (paint1.hitsShape(sponge) == True):
        paint1.opacity -= 2
        if (paint1.opacity <= 2):
            paint1.clear()
    if (paint2.hitsShape(sponge) == True):
        paint2.opacity -= 2
        if (paint2.opacity <= 2):
            paint2.clear()
    if (paint3.hitsShape(sponge) == True):
        paint3.opacity -= 2
        if (paint3.opacity <= 2):
            paint3.clear()

onMouseMove(100, 100)
onMouseMove(100, 200)
onMouseMove(50, 300)
onMouseMove(100, 100)
onMouseMove(330, 70)
onMouseMove(270, 100)
onMouseMove(350, 130)
onMouseMove(330, 70)

