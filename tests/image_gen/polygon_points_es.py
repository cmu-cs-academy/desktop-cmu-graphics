# Test polygon point access errors and functionality
# This tests both error cases and the new feature for modifying polygon points

# Create a polygon for testing
p = Polígono(50, 50, 350, 100, 300, 200, 100, 350)


# Test error cases - accessing x0/y0 (should fail because points start from 1)
def test_x0_error():
    x = p.x0


assertRaises(
    test_x0_error,
    "El objeto de polígono no puede acceder a 'x0' porque los números de puntos comienzan desde 1",
)


def test_y0_error():
    p.y0 = 100


assertRaises(
    test_y0_error,
    "El objeto de polígono no puede acceder a 'y0' porque los números de puntos comienzan desde 1",
)


# Test accessing non-existent point (y5 when polygon only has 4 points)
def test_y5_error():
    y = p.y5


assertRaises(
    test_y5_error,
    "El objeto de polígono no puede acceder a 'y5' porque sólo tiene 4 puntos",
)


# Test accessing non-existent point on a polygon with only 1 point
p2 = Polígono(50, 50)


def test_x5_error():
    x = p2.x5


assertRaises(
    test_x5_error,
    "El objeto de polígono no puede acceder a 'x5' porque sólo tiene 1 punto",
)

# -
p.visible = False
p2.visible = False

# Now test the basic functionality - reading and writing valid points
# Create a hexagon for testing point modifications
hexagon = Polígono(200, 100, 300, 150, 300, 250, 200, 300, 100, 250, 100, 150)

# Test reading points
assert hexagon.x1 == 200
assert hexagon.y1 == 100
assert hexagon.x6 == 100
assert hexagon.y6 == 150

# -
# Test modifying points
hexagon.x1 = 180
hexagon.y1 = 80
assert hexagon.x1 == 180
assert hexagon.y1 == 80

# -
# Modify another point
hexagon.x3 = 320
hexagon.y3 = 270
assert hexagon.x3 == 320
assert hexagon.y3 == 270

# -
# Modify the last point
hexagon.x6 = 120
hexagon.y6 = 170
assert hexagon.x6 == 120
assert hexagon.y6 == 170

# -
# Test modifying multiple points in sequence to create a different shape
hexagon.x1 = 150
hexagon.y1 = 120
hexagon.x2 = 350
hexagon.y2 = 180
hexagon.x3 = 350
hexagon.y3 = 280
hexagon.x4 = 150
hexagon.y4 = 320
hexagon.x5 = 50
hexagon.y5 = 280
hexagon.x6 = 50
hexagon.y6 = 180

# -
# Test with a triangle - modify all three points
hexagon.visible = False
triangle = Polígono(100, 100, 200, 100, 150, 200)
triangle.x1 = 80
triangle.y1 = 80
triangle.x2 = 220
triangle.y2 = 120
triangle.x3 = 170
triangle.y3 = 220

# -
# Test with a rectangle (4 points) - modify each corner
triangle.visible = False
rect = Polígono(50, 50, 250, 50, 250, 150, 50, 150)
rect.x1 = 30
rect.y1 = 30
rect.x2 = 270
rect.y2 = 70
rect.x3 = 270
rect.y3 = 170
rect.x4 = 30
rect.y4 = 130