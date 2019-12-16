app.background = 'black'

def drawLights():
    # Create a nested for loop to draw all the circles.
    for xVal in range(20, 400, 30):
        for yVal in range(0, 400, 30):
            # Calculates what the radius and color should be based on the
            # x and y position.
            distanceX = abs(200 - xVal)
            distanceY = abs(200 - yVal)
            radius = 0
            # Gets the radius based on where the circle is on the canvas.
            if (distanceX < distanceY):
                radius = distanceY / 10
            else:
                radius = distanceX / 10
            color = radius * 10 + 55
            # Draw the circle.
            Circle(xVal, yVal, radius, fill=gradient(rgb(0, 0, color), 'black'))
drawLights()


