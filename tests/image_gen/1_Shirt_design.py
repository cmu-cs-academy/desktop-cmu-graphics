app.background = 'pink'

# shirt
Polygon(5, 175, 85, 60, 315, 60, 395, 175, 330, 235, 290, 190, 300, 355,
        100, 355, 110, 190, 70, 237, fill='lavenderBlush')
Arc(200, 60, 95, 70, 90, 180, opacity=10)

# Add a step value of 5 to the loop, and fix the end-value so that the
# last value that the radius gets set to is 95.
for radius in range(10, 100, 5):
    # Draw a crimson star whenever the radius is a multiple of 10 and
    # a white star otherwise.
    if (radius % 10 == 0):
        Star(200, 210, 100 - radius, 6, fill='crimson')
    else:
        Star(200, 210, 100 - radius, 6, fill='white')


