app.background = 'dodgerBlue'

# watch band
Rect(200, 200, 145, 420, border='black', align='center')
Oval(200, 40, 180, 40, fill='gold', border='black')
Oval(200, 360, 180, 40, fill='gold', border='black')
Circle(200, 200, 165, fill=gradient('white', 'lightGrey', start='left'),
       border='black', borderWidth=8)
Arc(200, 200, 225, 225, 45, 270,
    fill=gradient('lightGrey', 'white', start='left'))
Arc(200, 200, 225, 225, 315, 90,
    fill=gradient('gainsboro', 'silver', start='right-top'))

def makeWatch(centerX, centerY, smallerTickRadius, largerTickRadius, outerRadius):
    # Draw a line for each second hand tick on the watch.
    # There should be 60 ticks in total, all equally spaced apart.
    for i in range(60):
        angle = i * 6
        # Every fifth tick should be longer.
        if (i % 5 == 0):
            innerRadius = smallerTickRadius
        else:
            innerRadius = largerTickRadius
        # Then get the appropriate points and draw the tick.
        innerX, innerY = getPointInDir(centerX, centerY, angle, innerRadius)
        outerX, outerY = getPointInDir(centerX, centerY, angle, outerRadius)
        Line(innerX, innerY, outerX, outerY)

makeWatch(200, 200, 120, 145, 165)
makeWatch(245, 235, 25, 35, 45)
makeWatch(140, 205, 20, 28, 30)


# -
app.background = 'dodgerBlue'

# watch band
Rect(200, 200, 145, 420, border='black', align='center')
Oval(200, 40, 180, 40, fill='gold', border='black')
Oval(200, 360, 180, 40, fill='gold', border='black')
Circle(200, 200, 165, fill=gradient('white', 'lightGrey', start='left'),
       border='black', borderWidth=8)
Arc(200, 200, 225, 225, 45, 270,
    fill=gradient('lightGrey', 'white', start='left'))
Arc(200, 200, 225, 225, 315, 90,
    fill=gradient('gainsboro', 'silver', start='right-top'))

def makeWatch(centerX, centerY, smallerTickRadius, largerTickRadius, outerRadius):
    # Draw a line for each second hand tick on the watch.
    # There should be 60 ticks in total, all equally spaced apart.
    for i in range(60):
        angle = i * 6
        # Every fifth tick should be longer.
        if (i % 5 == 0):
            innerRadius = smallerTickRadius
        else:
            innerRadius = largerTickRadius
        # Then get the appropriate points and draw the tick.
        innerX, innerY = getPointInDir(centerX, centerY, angle, innerRadius)
        outerX, outerY = getPointInDir(centerX, centerY, angle, outerRadius)
        Line(innerX, innerY, outerX, outerY)



# -
app.background = 'dodgerBlue'

# watch band
Rect(200, 200, 145, 420, border='black', align='center')
Oval(200, 40, 180, 40, fill='gold', border='black')
Oval(200, 360, 180, 40, fill='gold', border='black')
Circle(200, 200, 165, fill=gradient('white', 'lightGrey', start='left'),
       border='black', borderWidth=8)
Arc(200, 200, 225, 225, 45, 270,
    fill=gradient('lightGrey', 'white', start='left'))
Arc(200, 200, 225, 225, 315, 90,
    fill=gradient('gainsboro', 'silver', start='right-top'))

def makeWatch(centerX, centerY, smallerTickRadius, largerTickRadius, outerRadius):
    # Draw a line for each second hand tick on the watch.
    # There should be 60 ticks in total, all equally spaced apart.
    for i in range(60):
        angle = i * 6
        # Every fifth tick should be longer.
        if (i % 5 == 0):
            innerRadius = smallerTickRadius
        else:
            innerRadius = largerTickRadius
        # Then get the appropriate points and draw the tick.
        innerX, innerY = getPointInDir(centerX, centerY, angle, innerRadius)
        outerX, outerY = getPointInDir(centerX, centerY, angle, outerRadius)
        Line(innerX, innerY, outerX, outerY)


