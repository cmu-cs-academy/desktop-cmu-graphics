# Check that there is no floating point error in the values of x1, y1, x2, y2
arm = Line(125, 200, 115, 110)
assert arm.x1 == 125
assert arm.y1 == 200
assert arm.x2 == 115
assert arm.y2 == 110

# Check that exact integer values are preserved across translations
arm.centerY += 5
assert arm.x1 == 125
assert arm.y1 == 205
assert arm.x2 == 115
assert arm.y2 == 115

arm.centerX += 5
assert arm.x1 == 130
assert arm.y1 == 205
assert arm.x2 == 120
assert arm.y2 == 115

# Check that rotating throws out the exact integer values
arm.rotateAngle = 91
assert rounded(arm.x1) == 80
assert rounded(arm.y1) == 164
assert rounded(arm.x2) == 170
assert rounded(arm.y2) == 156

# Check that exact integer values can be set one at a time
arm.y2 = 156
assert rounded(arm.x1) == 80
assert rounded(arm.y1) == 164
assert rounded(arm.x2) == 170
assert arm.y2 == 156

Line(100, 300, 200, 300, dashes=True)
Line(100, 310, 200, 310, dashes=False)
Line(100, 320, 200, 320, dashes=(5, 10))
Line(100, 330, 200, 330, dashes=(5, 10, 20, 10))
assertRaises(lambda: Line(100, 330, 200, 330, dashes='asdf'),
             "Line.dashes should be bool (but 'asdf' is of type str)")

