# Check that there is no floating point error in the values of x1, y1, x2, y2
arm = Línea(125, 200, 115, 110)
assert arm.x1 == 125
assert arm.y1 == 200
assert arm.x2 == 115
assert arm.y2 == 110

# Check that exact integer values are preserved across translations
arm.centroY += 5
assert arm.x1 == 125
assert arm.y1 == 205
assert arm.x2 == 115
assert arm.y2 == 115

arm.centroX += 5
assert arm.x1 == 130
assert arm.y1 == 205
assert arm.x2 == 120
assert arm.y2 == 115

# Check that rotating throws out the exact integer values
arm.rotarÁngulo = 91
assert redondeado(arm.x1) == 80
assert redondeado(arm.y1) == 164
assert redondeado(arm.x2) == 170
assert redondeado(arm.y2) == 156

# Check that exact integer values can be set one at a time
arm.y2 = 156
assert redondeado(arm.x1) == 80
assert redondeado(arm.y1) == 164
assert redondeado(arm.x2) == 170
assert arm.y2 == 156

Línea(100, 300, 200, 300, guión=True)
Línea(100, 310, 200, 310, guión=False)
Línea(100, 320, 200, 320, guión=(5, 10))
Línea(100, 330, 200, 330, guión=(5, 10, 20, 10))
