# background
Rect(0, 0, 400, 400, fill=gradient('white', 'skyBlue'))

# wings
Rect(110, 130, 200, 130, fill='orange')
Polygon(190, 100, 200, 80, 210, 100, 210, 285, 200, 330, 190, 285)
Circle(290, 130, 80)
Circle(110, 130, 80)
Oval(270, 240, 150, 100)
Oval(130, 240, 150, 100)

# dots
Circle(99, 68, 7, fill='white')
Circle(301, 68, 7, fill='white')
Circle(69, 85, 7, fill='white')
Circle(331, 85, 7, fill='white')
Circle(50, 111, 7, fill='white')
Circle(350, 111, 7, fill='white')

# antennae
Line(195, 92, 174, 57)
Line(205, 92, 226, 57)

# top half of the pattern
Polygon(220, 150, 255, 85, 280, 75, 275, 100, fill='orange')
Polygon(240, 165, 275, 115, 330, 100, 300, 140, fill='orange')
Polygon(260, 180, 295, 155, 330, 155, 310, 185, fill='orange')

# Finish the top half of the pattern.
Polygon(180, 150, 145, 85, 120, 75, 125, 100, fill='orange')
Polygon(160, 165, 125, 115, 70, 100, 100, 140, fill='orange')
Polygon(140, 180, 105, 155, 70, 155, 90, 185, fill='orange')
# bottom half of the pattern
Polygon(80, 225, 120, 210, 160, 230, 115, 240, fill='white')
Polygon(180, 250, 125, 245, 105, 270, 145, 270, fill='white')
Polygon(75, 250, 80, 235, 110, 245, 95, 265, fill='white')

# Finish the bottom half of the pattern.
Polygon(320, 225, 280, 210, 240, 230, 285, 240, fill='white')
Polygon(220, 250, 275, 245, 295, 270, 255, 270, fill='white')
Polygon(325, 250, 320, 235, 290, 245, 305, 265, fill='white')

# This test case is intentionally left blank.

