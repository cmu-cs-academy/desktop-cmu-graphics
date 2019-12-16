def makeNArcs(n, centerX, centerY, width, height, color):
    sweepAngle = 360 / n
    for i in range(n):
        # Set the startAngle equal to i * sweepAngle.
        startAngle = i * sweepAngle
        # Gets a random value for the opacity.
        randOpacity = randrange(60, 100)
        # Draw an arc using the parameters given and the local variables
        # created in the function.
        Arc(centerX, centerY, width, height, startAngle, sweepAngle,
            fill=color, opacity=randOpacity)
# face
makeNArcs(9, 200, 200, 600, 600, 'burlyWood')

# left eye
Oval(115, 200, 150, 200, fill='white')
makeNArcs(10, 115, 200, 100, 100, 'skyBlue')
Circle(115, 200, 18)

# right eye
Oval(285, 200, 150, 200, fill='white')
makeNArcs(15, 285, 200, 100, 100, 'skyBlue')
Circle(285, 200, 18)

# eyebrows
Arc(105, 80, 120, 20, 270, 180, rotateAngle=-10)
Arc(295, 80, 120, 20, 270, 180, rotateAngle=10)


