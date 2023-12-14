# Correctness tests for hitsShape

# Test 1: No Intersection
rect1 = Rect(10, 10, 50, 50)
rect2 = Rect(100, 100, 50, 50)
assert not rect1.hitsShape(rect2)

circle1 = Circle(30, 30, 20)
circle2 = Circle(200, 200, 30)
assert not circle1.hitsShape(circle2)

# Test 2: Single Point Intersection
rect1 = Rect(10, 10, 50, 50)
line1 = Line(60, 60, 100, 100)
assert rect1.hitsShape(line1)

rect1 = Rect(10, 10, 50, 50)
rect2 = Rect(60, 60, 50, 50)
assert rect1.hitsShape(rect2)

# Test 3: Edge Intersection
rect1 = Rect(10, 10, 50, 50)
rect2 = Rect(60, 10, 50, 50)
assert rect1.hitsShape(rect2)

rect1 = Rect(10, 10, 50, 50)
rect2 = Rect(10, 60, 50, 50)
assert rect1.hitsShape(rect2)

polygon1 = Polygon(10, 10, 30, 50, 50, 10)
line1 = Line(0, 30, 60, 30)
assert polygon1.hitsShape(line1)

polygon1 = Polygon(10, 10, 30, 50, 50, 10)
line1 = Line(10, 10, 30, 50)
assert polygon1.hitsShape(line1)

# Test 4: Partial Overlap
rect1 = Rect(20, 20, 50, 50)
rect2 = Rect(40, 40, 50, 50)
assert rect1.hitsShape(rect2)

circle1 = Circle(50, 50, 30)
rect1 = Rect(40, 40, 60, 60)
assert circle1.hitsShape(rect1)

# Test 5: Total Overlap
rect1 = Rect(20, 20, 100, 100)
rect2 = Rect(40, 40, 30, 30)
assert rect1.hitsShape(rect2)

circle1 = Circle(50, 50, 30)
circle2 = Circle(50, 50, 10)
assert circle1.hitsShape(circle2)

# Test 6: Complex Shapes
star1 = Star(50, 50, 30, 5)
star2 = Star(70, 70, 30, 5)
assert star1.hitsShape(star2)

regPoly1 = RegularPolygon(50, 50, 30, 6)
regPoly2 = RegularPolygon(80, 50, 30, 6)
assert regPoly1.hitsShape(regPoly2)

regPoly1 = RegularPolygon(50, 50, 30, 6)
polygon1 = Polygon(60, 60, 80, 90, 100, 60)
assert regPoly1.hitsShape(polygon1)

# Test 8: Concave and Convex Polygons
star1 = Star(50, 50, 30, 5)
rect1 = Rect(40, 40, 50, 50)
assert star1.hitsShape(rect1)