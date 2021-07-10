CENTRO_X = 200
CENTRO_Y = 250

Rect(CENTRO_X, CENTRO_Y, 200, 200, alinear='centro', relleno='verde')
Rect(CENTRO_X, CENTRO_Y, 100, 100, alinear='centro', relleno='rojo')

c = Círculo(CENTRO_X, CENTRO_Y, 50)

###
# Prueba interactiva que se puede utilizar para garantizar que el
# examinador también está funcionando correctamente:
# def enRatónPresionado(x, y):
#     c.radio = 50
#     comprobar(50)
# def enRatónSoltado(x, y):
#     c.radio = 100
#     comprobar(100)

def round_eq(a, b):
    return rounded(a) == rounded(b)

def comprobar(r):
    assert round_eq(c.radio, r)
    assert round_eq(c.ancho, 2 * r)
    assert round_eq(c.altura, 2 * r)
    assert c.rotarÁngulo == 0

comprobar(50)

# -
c.radio = 100
comprobar(100)

# -
c.radio = 50
comprobar(50)

# -
c.radio = 100
comprobar(100)

# -
c.radio = 50
c.ancho = 200
assert c.ancho == 200
assert c.altura == 100
assert rounded(c.radio) == 75
assert c.rotarÁngulo == 0

# Check if circle is resized by group
# -
c.radio = 50
g = Grupo(c)
g.ancho += 100
g.altura += 100
comprobar(100)