# background
Rect(0, 0, 400, 400, fill='wheat')

# Picture shadow.
### (HINT: This should be a RegularPolygon, like the sky.)
RegularPolygon(210, 210, 180, 7, fill='tan')

# sky and sun
RegularPolygon(200, 200, 180, 7, fill='powderBlue')
Circle(270, 200, 65, fill='orangeRed', opacity=70)
Circle(270, 200, 55, fill=gradient('orange', 'orangeRed'))

# Draw the boat hull, left sail, and right sail.
Polygon(60, 205, 90, 240, 160, 240, 190, 205, fill='dimGray')
Polygon(130, 145, 130, 205, 190, 205, fill='limeGreen')
Polygon(60, 205, 125, 205, 125, 135, fill='forestGreen')

# Draw the sea.
Polygon(25, 240, 120, 365, 280, 365, 375, 240, fill='cadetBlue')

# This test case is intentionally left blank.

