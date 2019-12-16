# First, draw the actual illusion.
Line(0, 0, 100, 200)
Line(100, 200, 200, 400, fill='red')
Line(100, 185, 200, 385, fill='blue')
Rect(85, 0, 30, 400, fill='grey')

# Now, draw a repeat of the illusion, but making the rectangle partly
# transparent, so we can see what's really going on underneath.
Line(200, 0, 300, 200)
Line(300, 200, 400, 400, fill='red')
Line(300, 185, 400, 385, fill='blue')
Rect(285, 0, 30, 400, fill='grey', opacity=50)

# This test case is intentionally left blank.

