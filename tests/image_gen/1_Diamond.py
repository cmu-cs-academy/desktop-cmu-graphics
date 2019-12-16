# draws a background
Rect(0, 0, 400, 400, fill=gradient('powderBlue', 'lightCyan', start='top'))

# Create the outer shape of the diamond using a Polygon.
Polygon(60, 150, 100, 100, 300, 100, 340, 150, 200, 300,
        fill=gradient('white', 'lightBlue'), border='black', borderWidth=4)

# Create the brighter inner part of the diamond using a Polygon.
Polygon(200, 100, 125, 150, 200, 300, 275, 150, fill='azure', border='black')

# Create the cut lines.
Line(60, 150, 340, 150)
Line(100, 100, 125, 150)
Line(300, 100, 275, 150)

# Finish by adding a sparkle to the diamond!
Star(265, 120, 15, 6, fill='white', roundness=15)

# This test case is intentionally left blank.

