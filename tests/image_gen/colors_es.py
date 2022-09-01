assert str(rgb(1, 2, 3)) == 'rgb(1, 2, 3)'
print(str(gradiente('rojo', 'azul')))
assert str(gradiente('rojo', 'azul')) == "gradiente('rojo', 'azul', inicio='centro')"
assert str(gradiente('rojo', 'azul', rgb(1, 2, 3))) == "gradiente('rojo', 'azul', rgb(1, 2, 3), inicio='centro')"
assert str(gradiente('rojo', 'azul', inicio='superior-izquierda')) == "gradiente('rojo', 'azul', inicio='superior-izquierda')"

assert str(type(gradiente('rojo', 'amarillo'))) == "<class 'gradiente'>"

assertRaises(lambda: rgb('x', 2, 3), "rgb.red debe ser número (pero 'x' es de tipo str)")
assertRaises(lambda: rgb(['x'], 2, 3), "rgb.red debe ser número (pero ['x'] es de tipo list)")

# These strings are translated at a higher level, before they are printed to the console
assertRaises(lambda: rgb(1, 2, 3).x, "'rgb' object has no attribute 'x'")
assertRaises(lambda: gradiente('rojo', 'azul').x, "'gradiente' object has no attribute 'x'")

color = rgb(2, 4, 6)
r = Rect(20, 20, 20, 20, borde=color)
assertRaises(lambda: setattr(color, 'rojo', 123),
             "No se puede modificar el atributo 'rojo' del objeto de 'rgb'")
assertRaises(lambda: setattr(r.borde, 'rojo', 123),
             "No se puede modificar el atributo 'rojo' del objeto de 'rgb'")
r.visible = Falso

# Test default color attributes
x = Rect(200, 200, 100, 100)
assert x.relleno == 'negro'
assert x.borde is None
x.visible = Falso

# Test getting Shape borde property
for border_value in ['verde', gradiente('rojo', 'azul'), rgb(20, 40, 60)]:
    r = Rect(20, 20, 50, 50, borde=border_value)
    assert r.borde == border_value
    r.visible = Falso

# Test PTA Grupo relleno
for (relleno, other_fill) in [
    (rgb(100, 100, 100), rgb(120, 100, 100)),
    ('rojo', 'azul'),
    (gradiente('rojo', 'azul'), gradiente('rojo', 'azul', inicio='superior')),
    ('rojo', gradiente('rojo', 'azul')),
]:
    r = Rect(200, 200, 100, 100, relleno=relleno)
    r2 = Rect(200, 200, 100, 100, relleno=relleno)
    g = Grupo(r, r2)

    assert r.relleno == relleno
    assert g.relleno == relleno
    g.visible = Falso

    r = Rect(200, 200, 100, 100, relleno=relleno)
    r2 = Rect(200, 200, 100, 100, relleno=other_fill)
    g = Grupo(r, r2)
    assertRaises(lambda: g.relleno, 'Grupo.relleno no tiene valor porque no todos sus elementos')
    g.visible = Falso

# Test that Grupo relleno properly detects equivalent reflected gradients
r = Rect(200, 200, 100, 100)
r2 = Rect(200, 200, 100, 100)
g = Grupo(r, r2)
r.relleno = gradiente('rojo', 'azul', inicio='izquierda')
r2.relleno = gradiente('azul', 'rojo', inicio='derecha')
assert g.relleno == gradiente('rojo', 'azul', inicio='izquierda')

# Test setting Grupo relleno
g.relleno = gradiente('verde', 'amarillo', inicio='centro')
assert r.relleno == gradiente('verde', 'amarillo', inicio='centro')
assert r2.relleno == gradiente('verde', 'amarillo', inicio='centro')

g.visible = Falso

# Simple test to make sure that drawing works
Rect(50, 50, 200, 200, relleno=gradiente(rgb(50, 100, 150), 'rojo', 'amarillo', inicio='inferior'))
