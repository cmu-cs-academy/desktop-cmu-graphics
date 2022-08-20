assert str(rgb(1, 2, 3)) == 'rgb(1, 2, 3)'
assert str(gradient('red', 'blue')) == "gradient('red', 'blue', start='center')"
assert str(gradient('red', 'blue', rgb(1, 2, 3))) == "gradient('red', 'blue', rgb(1, 2, 3), start='center')"
assert str(gradient('red', 'blue', start='top-left')) == "gradient('red', 'blue', start='top-left')"

assert str(type(gradient('red', 'yellow'))) == "<class 'gradient'>"

assertRaises(lambda: rgb('x', 2, 3), "rgb.red should be number (but 'x' is of type str)")
assertRaises(lambda: rgb(['x'], 2, 3), "rgb.red should be number (but ['x'] is of type list)")
class A:
    pass
assertRaises(lambda: rgb(A(), 2, 3), "rgb.red should be number (but <__main__.A object")
assertRaises(lambda: rgb(A(), 2, 3), "> is of type A)")

assertRaises(lambda: rgb(1, 2, 3).x, "'rgb' object has no attribute 'x'")
assertRaises(lambda: gradient('red', 'blue').x, "'gradient' object has no attribute 'x'")

color = rgb(2, 4, 6)
r = Rect(20, 20, 20, 20, border=color)
assertRaises(lambda: setattr(color, 'red', 123), "Cannot modify attribute 'red' of 'rgb' object")
assertRaises(lambda: setattr(r.border, 'red', 123), "Cannot modify attribute 'red' of 'rgb' object")
r.visible = False

# Test default color attributes
x = Rect(200, 200, 100, 100)
assert x.fill == 'black'
assert x.border is None
x.visible = False

# Test getting Shape border property
for border_value in ['green', gradient('red', 'blue'), rgb(20, 40, 60)]:
    r = Rect(20, 20, 50, 50, border=border_value)
    assert r.border == border_value
    r.visible = False

# Test PTA Group fill
for (fill, other_fill) in [
    (rgb(100, 100, 100), rgb(120, 100, 100)),
    ('red', 'blue'),
    (gradient('red', 'blue'), gradient('red', 'blue', start='top')),
    ('red', gradient('red', 'blue')),
]:
    r = Rect(200, 200, 100, 100, fill=fill)
    r2 = Rect(200, 200, 100, 100, fill=fill)
    g = Group(r, r2)

    assert r.fill == fill
    assert g.fill == fill
    g.visible = False

    r = Rect(200, 200, 100, 100, fill=fill)
    r2 = Rect(200, 200, 100, 100, fill=other_fill)
    g = Group(r, r2)
    assertRaises(lambda: g.fill, 'Group.fill has no value because its children')
    g.visible = False

# Test that Group fill properly detects equivalent reflected gradients
r = Rect(200, 200, 100, 100)
r2 = Rect(200, 200, 100, 100)
g = Group(r, r2)
r.fill = gradient('red', 'blue', start='left')
r2.fill = gradient('blue', 'red', start='right')
assert g.fill == gradient('red', 'blue', start='left')

# Test setting Group fill
g.fill = gradient('green', 'yellow', start='center')
assert r.fill == gradient('green', 'yellow', start='center')
assert r2.fill == gradient('green', 'yellow', start='center')

g.visible = False

# Simple test to make sure that drawing works
Rect(50, 50, 200, 200, fill=gradient(rgb(50, 100, 150), 'red', 'yellow', start='bottom'))
