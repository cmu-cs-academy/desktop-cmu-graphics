# Draw the background.
Rect(0, 0, 400, 400, fill=rgb(55, 225, 205))

# Draw the body.
Circle(200, 300, 105, fill=rgb(250, 200, 230))
Circle(200, 300,  90, fill=rgb(250, 220, 240))
Rect(95, 300, 210, 100, fill=rgb(55, 225, 205))

# Then, draw the tentacles and the rest of the face.
Rect(120, 300, 20, 80, fill=rgb(250, 220, 240))
Rect(155, 300, 20, 80, fill=rgb(250, 220, 240))
Rect(190, 300, 20, 80, fill=rgb(250, 220, 240))
Rect(225, 300, 20, 80, fill=rgb(250, 220, 240))
Rect(260, 300, 20, 80, fill=rgb(250, 220, 240))

# eyes and pupils
Circle(155, 265, 10)
Circle(245, 265, 10)
Circle(155, 260, 5, fill='grey')
Circle(245, 260, 5, fill='grey')

# mouth
Circle(200, 265, 15, fill=rgb(250, 120, 180))
Rect(185, 250, 30, 15, fill=rgb(250, 220, 240))

# Finally, draw the bubbles!
Circle(120,  60, 40, fill='white', opacity=10)
Circle(120, 140, 30, fill='white', opacity=30)
Circle(120, 200, 20, fill='white', opacity=50)
Circle(120, 240, 10, fill='white', opacity=70)
Circle(120, 270, 5, fill='white', opacity=90)

# This test case is intentionally left blank.

