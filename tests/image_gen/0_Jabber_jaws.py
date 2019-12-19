app.background = 'lavenderBlush'
app.isMouthGrowing = False

noiseLines = Star(160, 220, 60, 8, roundness=10)
Rect(100, 140, 75, 160, fill='lavenderBlush')

# face
Oval(30, 140, 230, 350, fill='lightSkyBlue')
Polygon(0, 0, 130, 0, 145, 60, 180, 130, 145, 155, 0, 210, fill='lightSkyBlue')
Circle(80, 50, 15)

mouth = Polygon(150, 185, 80, 185, 95, 225, 140, 250, fill='lavenderBlush')

def onKeyHold(keys):
    # Depending on the variable app.isMouthGrowing, change the mouth's size,
    # reposition it on the boundary of the face, and change noiseLines.
    if (app.isMouthGrowing == True):
        mouth.width += 5
        mouth.height += 5
        mouth.right = 145
        noiseLines.radius += 5
    else:
        mouth.width -= 5
        mouth.height -= 5
        mouth.right = 145
        noiseLines.radius -= 5
    # Switch app.isMouthGrowing when the size of the mouth is too big or small.
    if ((mouth.width >= 70) or (mouth.height <= 10)):
        if (app.isMouthGrowing == True):
            app.isMouthGrowing = False
        else:
            app.isMouthGrowing = True

onKeyHolds(['a'], 1)


# -
app.background = 'lavenderBlush'
app.isMouthGrowing = False

noiseLines = Star(160, 220, 60, 8, roundness=10)
Rect(100, 140, 75, 160, fill='lavenderBlush')

# face
Oval(30, 140, 230, 350, fill='lightSkyBlue')
Polygon(0, 0, 130, 0, 145, 60, 180, 130, 145, 155, 0, 210, fill='lightSkyBlue')
Circle(80, 50, 15)

mouth = Polygon(150, 185, 80, 185, 95, 225, 140, 250, fill='lavenderBlush')

def onKeyHold(keys):
    # Depending on the variable app.isMouthGrowing, change the mouth's size,
    # reposition it on the boundary of the face, and change noiseLines.
    if (app.isMouthGrowing == True):
        mouth.width += 5
        mouth.height += 5
        mouth.right = 145
        noiseLines.radius += 5
    else:
        mouth.width -= 5
        mouth.height -= 5
        mouth.right = 145
        noiseLines.radius -= 5
    # Switch app.isMouthGrowing when the size of the mouth is too big or small.
    if ((mouth.width >= 70) or (mouth.height <= 10)):
        if (app.isMouthGrowing == True):
            app.isMouthGrowing = False
        else:
            app.isMouthGrowing = True

onKeyHolds(['a'], 20)


# -
app.background = 'lavenderBlush'
app.isMouthGrowing = False

noiseLines = Star(160, 220, 60, 8, roundness=10)
Rect(100, 140, 75, 160, fill='lavenderBlush')

# face
Oval(30, 140, 230, 350, fill='lightSkyBlue')
Polygon(0, 0, 130, 0, 145, 60, 180, 130, 145, 155, 0, 210, fill='lightSkyBlue')
Circle(80, 50, 15)

mouth = Polygon(150, 185, 80, 185, 95, 225, 140, 250, fill='lavenderBlush')

def onKeyHold(keys):
    # Depending on the variable app.isMouthGrowing, change the mouth's size,
    # reposition it on the boundary of the face, and change noiseLines.
    if (app.isMouthGrowing == True):
        mouth.width += 5
        mouth.height += 5
        mouth.right = 145
        noiseLines.radius += 5
    else:
        mouth.width -= 5
        mouth.height -= 5
        mouth.right = 145
        noiseLines.radius -= 5
    # Switch app.isMouthGrowing when the size of the mouth is too big or small.
    if ((mouth.width >= 70) or (mouth.height <= 10)):
        if (app.isMouthGrowing == True):
            app.isMouthGrowing = False
        else:
            app.isMouthGrowing = True

onKeyHolds(['1'], 20)
onKeyHolds(['2'], 20)

