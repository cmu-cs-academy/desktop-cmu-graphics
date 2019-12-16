app.background = gradient('dodgerBlue', 'dodgerBlue', 'lightCyan', start='bottom')

# ocean stars
Star(65, 65, 10, 6, fill='paleGreen')
Star(345, 300, 10, 7, fill='paleGreen', opacity=70)
Star(315, 125, 10, 4, fill='aliceBlue', roundness=20, rotateAngle=45)
Star(75, 300, 10, 8, fill='hotPink', rotateAngle=20, roundness=30, opacity=80)

# jellyfish body
Circle(240, 350, 50, fill=rgb(250, 200, 230))
Circle(240, 350, 45, fill=rgb(250, 220, 240))
Rect(185, 350, 110, 150, fill='dodgerBlue')
Line(205, 370, 275, 370, fill=rgb(250, 220, 240), lineWidth=40, dashes=(10, 5))

# jellyfish eyes and mouth
Circle(218, 332, 5)
Circle(263, 332, 5)
Circle(218, 330, 2, fill='grey')
Circle(263, 330, 2, fill='grey')
Circle(240, 332, 7, fill=rgb(250, 120, 180))
Rect(230, 325, 20, 7, fill=rgb(250, 220, 240))

# bubble
bubble = Circle(200, 330, 10, fill=gradient('lightCyan', 'lavender'), opacity=30,
                border=gradient('plum', 'darkTurquoise', 'hotPink',
                                'gold', start='top'))

def onKeyHold(keys):
    # When the up key is held, move the bubble up by 5 pixels.
    if ('up' in keys):
        bubble.centerY -= 5
    # Increase the radius by 1, and reset if the radius gets bigger than 80.
    bubble.radius += 1
    if (bubble.radius > 80):
        bubble.radius = 10
        bubble.centerY = 330

onKeyHolds(['right'], 71)


# -
app.background = gradient('dodgerBlue', 'dodgerBlue', 'lightCyan', start='bottom')

# ocean stars
Star(65, 65, 10, 6, fill='paleGreen')
Star(345, 300, 10, 7, fill='paleGreen', opacity=70)
Star(315, 125, 10, 4, fill='aliceBlue', roundness=20, rotateAngle=45)
Star(75, 300, 10, 8, fill='hotPink', rotateAngle=20, roundness=30, opacity=80)

# jellyfish body
Circle(240, 350, 50, fill=rgb(250, 200, 230))
Circle(240, 350, 45, fill=rgb(250, 220, 240))
Rect(185, 350, 110, 150, fill='dodgerBlue')
Line(205, 370, 275, 370, fill=rgb(250, 220, 240), lineWidth=40, dashes=(10, 5))

# jellyfish eyes and mouth
Circle(218, 332, 5)
Circle(263, 332, 5)
Circle(218, 330, 2, fill='grey')
Circle(263, 330, 2, fill='grey')
Circle(240, 332, 7, fill=rgb(250, 120, 180))
Rect(230, 325, 20, 7, fill=rgb(250, 220, 240))

# bubble
bubble = Circle(200, 330, 10, fill=gradient('lightCyan', 'lavender'), opacity=30,
                border=gradient('plum', 'darkTurquoise', 'hotPink',
                                'gold', start='top'))

def onKeyHold(keys):
    # When the up key is held, move the bubble up by 5 pixels.
    if ('up' in keys):
        bubble.centerY -= 5
    # Increase the radius by 1, and reset if the radius gets bigger than 80.
    bubble.radius += 1
    if (bubble.radius > 80):
        bubble.radius = 10
        bubble.centerY = 330

onKeyHold('up')


# -
app.background = gradient('dodgerBlue', 'dodgerBlue', 'lightCyan', start='bottom')

# ocean stars
Star(65, 65, 10, 6, fill='paleGreen')
Star(345, 300, 10, 7, fill='paleGreen', opacity=70)
Star(315, 125, 10, 4, fill='aliceBlue', roundness=20, rotateAngle=45)
Star(75, 300, 10, 8, fill='hotPink', rotateAngle=20, roundness=30, opacity=80)

# jellyfish body
Circle(240, 350, 50, fill=rgb(250, 200, 230))
Circle(240, 350, 45, fill=rgb(250, 220, 240))
Rect(185, 350, 110, 150, fill='dodgerBlue')
Line(205, 370, 275, 370, fill=rgb(250, 220, 240), lineWidth=40, dashes=(10, 5))

# jellyfish eyes and mouth
Circle(218, 332, 5)
Circle(263, 332, 5)
Circle(218, 330, 2, fill='grey')
Circle(263, 330, 2, fill='grey')
Circle(240, 332, 7, fill=rgb(250, 120, 180))
Rect(230, 325, 20, 7, fill=rgb(250, 220, 240))

# bubble
bubble = Circle(200, 330, 10, fill=gradient('lightCyan', 'lavender'), opacity=30,
                border=gradient('plum', 'darkTurquoise', 'hotPink',
                                'gold', start='top'))

def onKeyHold(keys):
    # When the up key is held, move the bubble up by 5 pixels.
    if ('up' in keys):
        bubble.centerY -= 5
    # Increase the radius by 1, and reset if the radius gets bigger than 80.
    bubble.radius += 1
    if (bubble.radius > 80):
        bubble.radius = 10
        bubble.centerY = 330

onKeyHolds(['up'], 50)

