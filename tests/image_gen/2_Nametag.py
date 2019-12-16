# Draws the background.
Rect(0, 0, 400, 400, fill=gradient('silver', 'black', start='left-top'))

# Draws the nametag rope and card.
Line(200, 95, 275, -15, fill='crimson', lineWidth=35)
Rect(25, 75, 350, 275, fill=gradient('red', 'orange', 'yellow', 'limeGreen',
                                     'blue', 'purple', start='bottom'))
Line(200, 95, 145, -15, fill='red', lineWidth=35)
Oval(200, 95, 85, 15, fill='grey')

# Draws the blank name-writing section.
Rect(50, 190, 300, 120, fill='white')
Rect(65, 175, 270, 150, fill='white')
Circle(65, 190, 15, fill='white')
Circle(65, 310, 15, fill='white')
Circle(335, 190, 15, fill='white')
Circle(335, 310, 15, fill='white')

# Add the labels to finish the nametag.
Label('Hello, my name is', 200, 140, fill='white', size=35, bold=True)
Label('Python', 200, 250, border='black', size=75, bold=True,
      fill=gradient('limeGreen', 'yellow', 'orange', start='top'))

# This test case is intentionally left blank.

