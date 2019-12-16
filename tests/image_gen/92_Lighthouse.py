# background
Rect(0, 0, 400, 250, fill=gradient('midnightBlue', 'steelBlue', start='top'))
Rect(0, 250, 400, 150, fill=gradient('slateBlue', 'darkSlateBlue', start='top'))

# Draw the rock behind the lighthouse and its reflection.
### (HINT: There is a point of the rock behind the lighthouse!)
Polygon(160, 280, 205, 240, 295, 210, 400, 230, 400, 280,
        fill=gradient('darkSlateBlue', 'darkBlue', start='top'))
Polygon(160, 280, 295, 300, 400, 290, 400, 280,
        fill=gradient('darkSlateBlue', 'darkBlue', start='top'), opacity=20)

# Draw the lighthouse from the top down.
Polygon(200, 120, 185, 130, 215, 130,
        fill=gradient('crimson', 'darkRed', start='bottom'))
Rect(190, 130, 20, 20, fill='crimson')
Rect(195, 130, 10, 20, fill='yellow')
Rect(185, 150, 30, 10, fill='fireBrick')
Polygon(190, 160, 185, 220, 215, 220, 210, 160,
        fill=gradient('crimson', 'darkRed', start='top'))
Rect(203, 190, 5, 10)
Polygon(185, 220, 180, 285, 220, 285, 215, 220,
        fill=gradient('snow', 'darkGray', start='top'))

# Draw the light coming from the lighthouse.
Circle(200, 140, 40, fill=gradient('yellow', 'gold', 'orange', start='top'),
       opacity=10)
Polygon(400, 260, 400, 340, 200, 140,
        fill=gradient('yellow', 'gold', 'orange', start='top'), opacity=30)

# Draw the rock in front of the lighthouse and its reflection.
Polygon(145, 240, 235, 265, 270, 290, 120, 290,
        fill=gradient('darkSlateBlue', 'midnightBlue', start='top'))
Polygon(145, 340, 235, 315, 270, 290, 120, 290,
        fill=gradient('darkSlateBlue', 'midnightBlue', start='top'), opacity=30)

# This test case is intentionally left blank.

