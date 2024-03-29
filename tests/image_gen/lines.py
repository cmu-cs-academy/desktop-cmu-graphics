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
