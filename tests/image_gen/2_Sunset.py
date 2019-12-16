# sky and sun
Rect(0, 0, 400, 200, fill=gradient('lightSkyBlue', 'pink', 'coral', start='top'))
Circle(200, 200, 70, fill='orange', opacity=50)
Circle(200, 200, 50, fill='gold')
# ocean
Rect(0, 200, 400, 60, fill='dodgerBlue')
Rect(0, 260, 400, 40, fill='deepSkyBlue')
Rect(0, 300, 400, 100, fill='turquoise')
# the sun's reflections on the water
Oval(200, 204, 120, 5, fill='gold', opacity=80)
Oval(165, 210, 80, 5, fill='gold', opacity=70)
Oval(255, 210, 70, 5, fill='gold', opacity=70)
Oval(230, 217, 95, 5, fill='gold', opacity=70)
Oval(190, 223, 60, 5, fill='gold', opacity=60)
Oval(235, 232, 60, 5, fill='gold', opacity=40)
Oval(155, 232, 60, 5, fill='gold', opacity=40)
# foam
Polygon(0, 400, 0, 280, 300, 335, 400, 320, 400, 400, fill='white')
# sand
Polygon(0, 400, 0, 290, 300, 360, 400, 330, 400, 400, fill='wheat')
Polygon(35, 280, 30, 360, 55, 360, 50, 275, 60, 175, 50, 175, fill='sienna',
        lineWidth=20)
Polygon(0, 335, 400, 390, 400, 400, 0, 400, fill='burlyWood')
# tree
Star(55, 175, 60, 9, fill='limeGreen', roundness=50)
Circle(20, 185, 7, fill='maroon')
Star(55, 175, 50, 8, fill='green', roundness=50)
Circle(40, 180, 7, fill='maroon')
Circle(40, 200, 7, fill='maroon')

# This test case is intentionally left blank.

