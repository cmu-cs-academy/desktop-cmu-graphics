# Draw the head.
Circle(200, 140, 80, fill=rgb(164, 198, 57))
Rect(120, 140, 160, 10, fill='white')

# Draw the eyes and then the antennas.
Circle(160, 105, 5, fill='white')
Circle(240, 105, 5, fill='white')
Line(200, 140, 250, 45, fill=rgb(164, 198, 57))
Line(200, 140, 150, 45, fill=rgb(164, 198, 57))

# Draw the main body (with rounded bottom corners).
Circle(135, 270, 15, fill=rgb(164, 198, 57))
Circle(265, 270, 15, fill=rgb(164, 198, 57))
Rect(120, 150, 160, 120, fill=rgb(164, 198, 57))
Rect(135, 270, 130, 15, fill=rgb(164, 198, 57))

# Draw the legs.
Rect(150, 285, 40, 40, fill=rgb(164, 198, 57))
Circle(170, 325, 20, fill=rgb(164, 198, 57))
Rect(210, 285, 40, 40, fill=rgb(164, 198, 57))
Circle(230, 325, 20, fill=rgb(164, 198, 57))

# Draw the arms.
Rect(70, 165, 40, 80, fill=rgb(164, 198, 57))
Circle(90, 165, 20, fill=rgb(164, 198, 57))
Circle(90, 245, 20, fill=rgb(164, 198, 57))
Rect(290, 165, 40, 80, fill=rgb(164, 198, 57))
Circle(310, 165, 20, fill=rgb(164, 198, 57))
Circle(310, 245, 20, fill=rgb(164, 198, 57))

# This test case is intentionally left blank.

