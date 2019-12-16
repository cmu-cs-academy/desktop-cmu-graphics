# front face of the cube
Rect(70, 150, 200, 200, fill=None, border='limeGreen')

# Draw the rest of the cube using lines.
Line(130, 70, 330, 70, fill='darkViolet')
Line(330, 70, 330, 270, fill='darkViolet')
Line(70, 150, 130, 70, fill=gradient('limeGreen', 'darkViolet', start='left'))
Line(270, 350, 330, 270, fill=gradient('limeGreen', 'darkViolet', start='left'))
Line(270, 150, 330, 70, fill=gradient('limeGreen', 'darkViolet', start='left'))
# Use dashes to distinguish the back part of the cube from the front.
Line(70, 350, 130, 270, fill=gradient('limeGreen', 'darkViolet', start='left'),
     dashes=True)
Line(130, 270, 330, 270, fill='darkViolet', dashes=True)
Line(130, 270, 130, 70, fill='darkViolet', dashes=True)

# This test case is intentionally left blank.

