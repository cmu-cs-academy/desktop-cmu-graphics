# Draw the 5 Rects in the solution.
# Draw the top left and bottom right Rects first, with an opacity.
Rect(0, 0, 200, 200, fill='lime', opacity=50)
Rect(200, 200, 200, 200, fill='aqua', opacity=50)
# Then draw the middle Rect with no opacity.
Rect(50, 50, 300, 300, fill='midnightBlue')
# Finally, draw the bottom left and top right Rects, again with opacity.
Rect(200, 0, 200, 200, fill='red', opacity=50)
Rect(0, 200, 200, 200, fill='deepPink', opacity=50)

# This test case is intentionally left blank.

