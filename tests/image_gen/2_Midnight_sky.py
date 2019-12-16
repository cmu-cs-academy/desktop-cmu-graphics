# background
Rect(0, 0, 400, 400)

# Saturn with rings
Circle(50, 50, 30, fill=None, border='white', opacity=30)
Circle(50, 50, 25, fill=gradient('peru', 'wheat'))

# Venus
Circle(150, 100, 20, fill=gradient('orangeRed', 'lightSalmon', start='left-bottom'),
       opacity=70)

# shooting star
Line(100, 200, 275, 125, fill=gradient('black', 'white', start='right'),
     lineWidth=3)

# moon
Circle(250, 250, 60, fill=gradient('black', 'grey', start='left'))

# clouds
Oval(150, 275, 100, 50, fill=gradient('black', 'grey', start='left'), opacity=90)
Oval(125, 300, 100, 50, fill=gradient('black', 'grey', start='left'), opacity=90)
Oval(200, 300, 100, 50, fill=gradient('black', 'grey', start='right'), opacity=90)

# This test case is intentionally left blank.

