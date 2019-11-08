def rotateAll(degrees):
    for s in app.group:
        s.rotateAngle += degrees

Rect(0, 0, 100, 100, fill=gradient('red', 'orange', start='left'))
Rect(150, 0, 100, 100, fill=gradient('red', 'orange'))

Star(100, 100, 50, 5, fill=gradient('pink', 'blue'))
Star(150, 100, 50, 5, fill=gradient('pink', 'blue', start='bottom'))

Polygon(40, 170, 60, 110, 90, 170, 90, 200, 170, 250, 90, 210, 70, 240, 20, 220,
fill=gradient('pink', 'green'))
Polygon(140, 170, 160, 110, 190, 170, 190, 200, 270, 250, 190, 210, 170, 240, 120, 220,
fill=gradient('pink', 'green', start='right-bottom'))

# -
rotateAll(10)
# -
rotateAll(90)
# -
rotateAll(90)
# -
rotateAll(90)
