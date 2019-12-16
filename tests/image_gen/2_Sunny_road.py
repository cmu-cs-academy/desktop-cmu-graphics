# sky
Rect(0, 0, 400, 250, fill=gradient('deepSkyBlue', 'lightSkyBlue', start='top'))

# grass
Rect(0, 250, 400, 150, fill=gradient('lawnGreen', 'green', 'lawnGreen',
                                     'lawnGreen', 'green', start='top'))

# The center line in the road is missing. Add it in!
Rect(0, 275, 400, 100, fill=gradient('darkGray', 'dimGray', start='top'))
Line(0, 325, 400, 325, fill='white', lineWidth=3, dashes=True)
# car 1
Rect(20, 270, 70, 30, fill=gradient('crimson', 'darkRed', start='top'))
Rect(30, 250, 50, 20, fill=gradient('red', 'crimson', start='top'))
Circle(35, 300, 10)
Circle(75, 300, 10)

# car 2
Rect(300, 330, 70, 30, fill=gradient('darkOrange', 'orangeRed', start='top'))
Rect(310, 310, 50, 20, fill=gradient('orange', 'darkOrange', start='top'))
Circle(315, 360, 10)
Circle(355, 360, 10)

# Fix the rays of the sun so that they are dashed.
Circle(0, 0, 70, fill=gradient('orange', 'yellow'))
Line(10, 75, 10, 155, fill=gradient('yellow',  'skyBlue', start='top'),
     lineWidth=5, dashes=True)
Line(35, 70, 75, 140, fill=gradient('yellow',  'skyBlue', start='top'),
     lineWidth=5, dashes=True)
Line(55, 55, 125, 100, fill=gradient('yellow',  'skyBlue', start='top'),
     lineWidth=5, dashes=True)
Line(70, 30, 145, 50, fill=gradient('yellow',  'skyBlue', start='top'),
     lineWidth=5, dashes=True)
Line(75, 5, 155, 5, fill=gradient('yellow',  'skyBlue', start='top'),
     lineWidth=5, dashes=True)

# This test case is intentionally left blank.

