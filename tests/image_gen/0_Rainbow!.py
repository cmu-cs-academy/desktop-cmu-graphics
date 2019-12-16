# Change the background.
Rect(0, 0, 400, 400, fill='lightSkyBlue')

# Draw the rainbow using circles and gradients.
Circle(200, 300, 200, fill=gradient('white', 'red', 'white', start='top'))
Circle(200, 300, 170, fill=gradient('white', 'orange', 'white', start='top'))
Circle(200, 300, 140, fill=gradient('white', 'yellow', 'white', start='top'))
Circle(200, 300, 110, fill=gradient('white', 'green', 'white', start='top'))
Circle(200, 300, 80, fill=gradient('white', 'blue', 'white', start='top'))
Circle(200, 300, 50, fill=gradient('white', 'indigo', 'white', start='top'))
Circle(200, 300, 20, fill=gradient('white', 'violet', 'white', start='top'))

# Now draw grass that covers the bottom half of the circles.
Rect(0, 300, 400, 100, fill=gradient('limeGreen', 'forestGreen', start='top'))

# This test case is intentionally left blank.

