# Draw the top row.
Rect(25, 25, 100, 100, fill=gradient('red', 'yellow', start='left-top'))
Rect(150, 25, 100, 100, fill=gradient('red', 'yellow', start='top'))
Rect(275, 25, 100, 100, fill=gradient('red', 'yellow', start='right-top'))

# Draw the middle row.
Rect(25, 150, 100, 100, fill=gradient('red', 'yellow', start='left'))
Rect(150, 150, 100, 100, fill=gradient('red', 'yellow'))
Rect(275, 150, 100, 100, fill=gradient('red', 'yellow', start='right'))

# Draw the bottom row.
Rect(25, 275, 100, 100, fill=gradient('red', 'yellow', start='left-bottom'))
Rect(150, 275, 100, 100, fill=gradient('red', 'yellow', start='bottom'))
Rect(275, 275, 100, 100, fill=gradient('red', 'yellow', start='right-bottom'))

# This test case is intentionally left blank.

