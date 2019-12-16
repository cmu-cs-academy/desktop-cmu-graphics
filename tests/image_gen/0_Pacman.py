app.background = 'black'

# background
Line(125, 0, 125, 400, fill='blue', lineWidth=20, opacity=20, dashes=(100, 200))
Line(275, 0, 275, 400, fill='blue', lineWidth=20, opacity=20, dashes=(100, 200))
Line(0, 100, 400, 100, fill='blue', lineWidth=20, opacity=20, dashes=(125, 150))
Line(0, 300, 400, 300, fill='blue', lineWidth=20, opacity=20, dashes=(125, 150))

# pellets
Circle(200, 415, 30, fill='gold', opacity=40)
Circle(200, -15, 30, fill='gold', opacity=40)
Circle(200, 70, 30, fill='gold', opacity=40)
Circle(200, 330, 30, fill='gold', opacity=40)

# cherry
Line(255, 230, 285, 145, fill='gold', lineWidth=5)
Line(315, 230, 280, 160, fill='gold', lineWidth=5)
Rect(280, 145, 10, 22, fill='gold', rotateAngle=20)
Circle(255, 235, 25, fill='red')
Circle(315, 235, 25, fill='red')

# Draw Pacman.
Arc(100, 200, 175, 175, 135, 270, fill='yellow')
Circle(105, 150, 10)


