CENTRO_X = 200
CENTRO_Y = 200

o = Óvalo(CENTRO_X, CENTRO_Y, 200, 300, rotarÁngulo=10, relleno='rosado', db='bbox')

def redimensionar(w, h):
    o.ancho = w
    assert o.ancho == w, o.ancho
    assert o.centroX == CENTRO_X, o.centroX
    o.altura = h
    assert o.altura == h, o.altura
    assert o.centroY == CENTRO_Y, o.centroY

# -
redimensionar(100, 100)
# -
redimensionar(50, 200)
# -
redimensionar(200, 50)


# -
o = Óvalo(300, 300, 200, 100, db='bbox')

while o.ancho > 10e-12:
    o.ancho /= 2
    assert o.altura == 100
    assert o.ancho > 0
    assert o.rotarÁngulo == 0 or o.rotarÁngulo == 90, o.rotarÁngulo

o = Óvalo(300, 300, 200, 100, db='bbox')

while o.altura > 10e-12:
    o.altura /= 2
    assert o.ancho == 200
    assert o.altura > 0
    assert o.rotarÁngulo == 0 or o.rotarÁngulo == 90, o.rotarÁngulo



#-
c2 = Óvalo(200, 200, 100, 20, relleno=None, borde='negro')

def sacudir(ancho, altura):
    c2.ancho = ancho
    assert c2.ancho == ancho, c2.ancho
    c2.altura = altura
    assert c2.altura == altura, c2.altura
    c2.rotarÁngulo += 1
    c2.centroX = 200
    c2.centroY = 200
    assert c2.centroX == 200, c2.centroX
    assert c2.centroY == 200, c2.centroY

for _ in range(400):
    sacudir(200, 100)

Círculo(100, 100, 30, relleno='rojo', borde='azul')
Óvalo(200, 100, 30, 60, relleno='rojo', borde='azul')

Óvalo(50, 350, 100, 150, relleno=gradiente('rojo', 'blanco', 'blanco', 'rojo'))
Círculo(150, 350, 45, relleno=gradiente('rojo', 'blanco', 'blanco', 'rojo'))
