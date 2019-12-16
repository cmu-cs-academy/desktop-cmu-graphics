# Repeatedly draw randomly positioned meteors until one hits the mountains.

app.background = gradient('black', 'darkBlue', start='top')

mountain = Polygon(-40, 400, 160, 310, 230, 330, 270, 290, 290, 300, 330, 240,
                   465, 400, opacity=50)
meteors = Group()

def drawMeteors():
    # Use a while loop to add meteors into the group until they hit
    # the mountain.
    while (meteors.hitsShape(mountain) == False):
        startX = randrange(0, 400)
        startY = randrange(0, 175)
        meteor = Line(startX, startY, startX + 50, startY + 50,
                      fill=gradient(rgb(0, 0, 50), rgb(0, 0, 80), 'lightCyan',
                                    start='top'))
        meteor.dx = randrange(-15, -10)
        meteor.dy = randrange(10, 15)
        meteors.add(meteor)
        # Uses a for loop to move each meteor in meteors.children.
        for meteor in meteors.children:
            meteor.x2 += meteor.dx
            meteor.y2 += meteor.dy
drawMeteors()


