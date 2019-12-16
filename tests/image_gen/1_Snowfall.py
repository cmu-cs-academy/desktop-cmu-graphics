app.background = gradient(rgb(220, 245, 255), 'black', start='left-top')
app.stepsPerSecond = 20

fallingSnowflakes = Group()

def createSnowflakes():
    for i in range(85):
        # Create a randomly placed, sized, and opaque snowflake.
        flakeX = randrange(0, 400)
        flakeY = randrange(0, 400)
        size = randrange(2, 4)
        opacity = randrange(0, 80)
        flake = Circle(flakeX, flakeY, size, fill='white', opacity=opacity)

        # Only some of the snowflakes will fall, the rest are stuck to the window.
        if (i < 65):
            fallingSnowflakes.add(flake)

createSnowflakes()

# window and curtains
Line(200, 0, 200, 400, fill='sienna', lineWidth=4)
Line(0, 200, 400, 200, fill='sienna', lineWidth=4)
Rect(0, 0, 400, 400, fill=None, border='sienna', borderWidth=10)
Oval(0, 0, 180, 360, fill='crimson', rotateAngle=15)
Oval(400, 0, 180, 360, fill='crimson', rotateAngle=-15)

def onStep():
    # Move each flake right and down a random distance, with wraparound.
    for flake in fallingSnowflakes.children:
        flake.centerX += randrange(0, 100)
        flake.centerY += randrange(-2, 25)

        # Wrap the flake around
        if (flake.left >= 400):
            flake.right = 0
        if (flake.top >= 400):
            flake.bottom = 0


