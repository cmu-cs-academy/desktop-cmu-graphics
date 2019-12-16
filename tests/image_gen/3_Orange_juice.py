# Draw the background.
Rect(0, 0, 400, 400, fill=gradient('turquoise', 'paleTurquoise'))
# Draw the glass and the orange juice.
Rect(110, 100, 180, 250, fill='azure')
Rect(120, 150, 160, 190, fill=gradient('gold', 'yellow', start='bottom'))
# Draw the ice cubes.
Rect(130, 170, 40, 40, fill=rgb(255, 255, 200))
Rect(190, 200, 30, 30, fill=rgb(255, 255, 200))
# Draw the straw.
Rect(240, 60, 10, 270,
     fill=gradient('orange', 'orange', 'orange', 'red', start='bottom'))
Rect(240, 50, 50, 10, fill='red')

# This test case is intentionally left blank.

