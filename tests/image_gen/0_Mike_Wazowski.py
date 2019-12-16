# background
Rect(0, 0, 400, 400, fill='crimson')
Line(0, 200, 400, 200, fill='darkRed', lineWidth=400, opacity=20, dashes=(5, 75))
# horns
Polygon(130, 125, 135, 90, 150, 105,
        fill=gradient('whiteSmoke', 'khaki', start='top'))
Polygon(270, 125, 265, 90, 250, 105,
        fill=gradient('whiteSmoke', 'khaki', start='top'))
# arms
Line(112, 240, 105, 265, lineWidth=8,
     fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))
Line(106, 260, 110, 310, lineWidth=8,
     fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))
Line(293, 225, 290, 310, lineWidth=8,
     fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))
# hands
Line(110, 300, 120, 310, lineWidth=8,
     fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))
Line(290, 300, 280, 310, lineWidth=8,
     fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))
Oval(110, 310, 15, 25,
     fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))
Oval(290, 310, 15, 25,
     fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))
# legs
Line(170, 300, 170, 360, lineWidth=15,
     fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))
Line(230, 300, 230, 360, lineWidth=15,
     fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))
# leg cover
Oval(200, 333, 55, 110, fill='crimson')
# feet
Oval(170, 360, 30, 20,
     fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))
Oval(230, 360, 30, 20,
     fill=gradient('mediumSeaGreen', 'greenYellow', start='left'))
# body
Oval(200, 200, 200, 220,
     fill=gradient('greenYellow', 'greenYellow', 'mediumSeaGreen'))
# mouth
Circle(155, 233, 10, fill='darkGreen')
Circle(155, 235, 10, fill='greenYellow')
Circle(245, 233, 10, fill='darkGreen')
Circle(245, 235, 10, fill='greenYellow')
Oval(200, 232, 100, 50, fill='darkGreen')
Oval(200, 230, 100, 50, fill='greenYellow')
# eye
Circle(200, 160, 50, fill='white')
Circle(200, 160, 25, fill=gradient('mediumSeaGreen', 'seaGreen'))
Star(200, 160, 25, 25, fill=gradient('springGreen', 'mediumSeaGreen'),
     roundness=50)
Circle(200, 160, 15)
Circle(190, 150, 5, fill='white')
Circle(180, 150, 2, fill='white')

# This test case is intentionally left blank.

