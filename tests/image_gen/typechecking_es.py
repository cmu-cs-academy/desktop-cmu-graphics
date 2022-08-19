def assertError(fn, errorKeywords):
    raised = True
    try:
        fn()
        raised = False
    except Exception as e:
        msg = str(e).lower()
        for kw in errorKeywords:
          if not kw.lower() in msg:
            raise Exception('error message should contain ' + kw)
    if not raised:
        raise Exception('fn failed to raise an exception')

# Normal definitions should still work
c = Círculo(100, 200, 30)
r = Rect(200, 200, 100, 100)
g = Grupo(c, r)

# Error should differentiate between tuples and lists
assertError(lambda: Círculo((1, 2), 10, 10), ['tuple', 'Círculo', 'centroX', '(1, 2)'])
assertError(lambda: Círculo(10, [1, 2], 10), ['list', 'Círculo', 'centroY', '[1, 2]'])

# Error should work if shapes passed as argument
assertError(lambda: Círculo(c, 20, 20), ['Círculo(100, 200, 30)', 'centroX'])

# Error should work on functions
assertError(lambda: Círculo(lambda x: x * x, 20, 20), ['centroX', 'Círculo', 'lambda'])

# Grupo.agregar typechecking
assertError(lambda: Grupo(1), ['int', 'Grupo', 'agregar'])
assertError(lambda: Grupo().agregar(1), ['int', 'Grupo', 'agregar'])
assertError(lambda: Grupo((1, 2)), ['tuple', 'Grupo', 'agregar', '(1, 2)'])
assertError(lambda: Grupo().agregar((1, 2)), ['tuple', 'Grupo', 'agregar', '(1, 2)'])
assertError(lambda: Grupo().agregar([1, 2]), ['list', 'Grupo', 'agregar', '[1, 2]'])

# Shape.contiene
assertError(lambda: c.contiene((2, 3), 1), ['tuple', 'contiene', 'x', '(2, 3)'])

# Rect typechecking should say Rect, not Polygon
assertError(lambda: Rect(0, 0, "hi", 0), ['str', 'Rect.ancho'])

# type() should work without printing module name
assert(str(type(c)) == "<class 'Círculo'>")
assert(repr(type(c)) == "<class 'Círculo'>")

# Grupo should disallow fill/border in constructor
assertError(lambda: Grupo(Círculo(100, 100, 20), Círculo(200, 200, 20), fill='blue'), [])

# Check incorrect aligns
assertError(lambda: Círculo(100, 100, 20, alinear='hi'), ['hi', 'alinear'])

# Check invalid colors
assertError(lambda: Círculo(100, 100, 20, relleno='hi'), ['hi', 'relleno'])
assertError(lambda: Círculo(100, 100, 20, borde='hi'), ['hi', 'borde'])

# Check invalid gradients colors/starts
assertError(lambda: gradiente('rojo', 'azul', inicio='hi'), ['hi', 'inicio'])
assertError(lambda: gradiente(None, 'azul'), ['None'])
assertError(lambda: gradiente(gradiente('rojo', 'azul'), 'azul'), ["gradiente('rojo', 'azul'"])

def changeBackground():
    app.fondo = 20
assertError(changeBackground, ['20', 'fondo'])

# Checks pointList
p = Polígono(200, 200, 300, 200, 300, 300, 200, 300)
assert(p.pointList == [[200, 200], [300, 200], [300, 300], [200, 300]])

def changePointList(val):
    p.pointList = val

changePointList([[300, 300], [300, 400], [400, 400], [400, 300]])

# RGBs / Gradients should typecheck correctly
assertError(lambda: rgb(None, 2, 3), ['RGB.red', 'None'])
assertError(lambda: rgb([2, 3], 2, 3), ['RGB.red', 'list'])
assertError(lambda: gradiente(None, None), ['colores', 'None'])
assertError(lambda: gradiente('hi', 'rojo'), ['hi'])
assertError(lambda: rgb(300, 100, 100), ['RGB.red', '300'])

# Calling class methods with too few arguments
assertError(lambda: g.toca(), ['Falta un argumento requerido'])
assertError(lambda: g.quitar(), ['Falta un argumento requerido'])
