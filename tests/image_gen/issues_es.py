###
# Comportamiento básico de hijos de grupo
r1 = Rect(10, 20, 30, 40)
r2 = Rect(40, 50, 60, 70)
g = Grupo(r1, r2)

assert len(g.hijos) == 2, g.hijos
g.figuras = 4
g._figuras = 1233

assert len(g.hijos) == 2, g.hijos
assert g.figuras == 4
assert g._figuras == 1233

g.foo = r2
assert g.foo == r2

###
g2 = Grupo()
assert len(g2) == 0
g2.agregar(Rect(50, 50, 50, 50))
assert len(g2) == 1
g2.agregar(Rect(100, 100, 50, 50))
assert len(g2) == 2

r2 = Rect(200, 200, 50, 50)
g2.agregar(r2)
assert len(g2) == 3
g2.quitar(r2)
assert len(g2) == 2
g2.visible = Falso

###
# Devolviendo gradientes o valores RGB como propiedades
r = Rect(100, 100, 200, 200, relleno=rgb(100, 200, 212))
assert r.relleno.red == 100
assert r.relleno.green == 200
assert r.relleno.blue == 212

r = Rect(100, 100, 200, 200, relleno=gradiente('rojo', 'azul'))
assert r.relleno.inicio == 'centro'
assert r.relleno.colores == ['rojo', 'azul']

###
# Redondez por defecto de Estrella
s = Estrella(355, 355, 45, 5)
assert rounded(s.redondez) == 38, s.redondez
s.puntos = 6
assert rounded(s.redondez) == 58, s.redondez
s.puntos = 16
assert rounded(s.redondez) == 58, s.redondez
s.redondez=12
assert s.redondez == 12, s.redondez

###
# Comprobación de tipo de gradiente
assertRaises(lambda: Rect(0, 0, 50, 50, relleno=gradiente('rojo', gradiente('rojo', 'azul'))))
assertRaises(lambda: Rect(0, 0, 50, 50, relleno=gradiente('rojo', None)))

###
# Propiedades personalizadas no se pueden usar en un constructor de figuras
assertRaises(lambda: Círculo(40, 40, 40, foo='bar'))


###
# No se puede establecer el ancho o la altura de una figura a 0
def setZeroShapeAttr(shape, attr):
    setattr(shape, attr, 0)

assertRaises(lambda: Rect(200, 200, 100, 0))
assertRaises(lambda: Rect(200, 200, 0, 100))
s = Rect(200, 200, 100, 100)
assertRaises(lambda: setZeroShapeAttr(s, 'ancho'))
s.visible = Falso

assertRaises(lambda: Óvalo(200, 200, 100, 0))
assertRaises(lambda: Óvalo(200, 200, 0, 100))
s = Óvalo(200, 200, 100, 100)
assertRaises(lambda: setZeroShapeAttr(s, 'ancho'))
s.visible = Falso

assertRaises(lambda: Círculo(200, 200, 0))
s = Círculo(200, 200, 100)
assertRaises(lambda: setZeroShapeAttr(s, 'radio'))
assertRaises(lambda: setZeroShapeAttr(s, 'ancho'))
assertRaises(lambda: setZeroShapeAttr(s, 'altura'))
s.visible = False

assertRaises(lambda: Línea(200, 200, 0, 0, anchuraDeLínea=0))


###
# No se puede usar "alinear" con Polígonos
assertRaises(lambda: Polígono(10, 10, 50, 50, alinear='izquierda'))

###
# No se puede obtener o establecer la propiedad "alinear"
r = Rect(0, 0, 100, 100)
def f():
    r.alinear = 'centro'
assertRaises(f)
assertRaises(lambda: print(r.alinear))
r.visible = Falso

###
# Gradientes radiales se deberían mover con su objeto
r = Rect(0, 380, 20, 20, relleno=gradiente('negro', 'blanco'))
# -
r.izquierda += 10

assert isinstance(app.grupo, Grupo)

Línea(320, 20, 370, 70, relleno=None)

# alinear debería funcionar incluso si centroX === 0
Óvalo(0, 0, 50, 50, alinear='izquierda')

# Levante un error si el ángulo de barrido no está en [0, 360]
assertRaises(lambda: Arco(200, 200, 200, 200, 90, -45))
assertRaises(lambda: Arco(200, 200, 200, 200, 90, -1))
assertRaises(lambda: Arco(200, 200, 200, 200, 90, 361))

# Levante un error si la redondez no está en [0, 100]
assertRaises(lambda: Estrella(355, 355, 45, 5, redondez=-1))
assertRaises(lambda: Estrella(355, 355, 45, 5, redondez=101))

# Esto no debería tirar un error
Polígono(relleno=gradiente('rojo', 'orange'))

# Compruebe que rotar un grupo vacio está bien
g = Grupo()
assert g.rotarÁngulo == 0
g.rotarÁngulo += 20
g.rotarÁngulo += 20
assert g.rotarÁngulo == 40

import time
from collections import defaultdict

grad = gradiente('rojo', 'negro', inicio='izquierda-superior')
assert grad.inicio == 'izquierda-superior'
grad2 = gradiente('rojo', 'negro', inicio='superior-izquierda')
assert grad2.inicio == 'superior-izquierda'

r142 = Rect(50, 50, 200, 200)
g = Grupo(r142)
g.vaciar()
assert r142.visible == Falso
r142.visible = Falso
r142.visible = Verdadero
r142.visible = Falso

###
# Zero height/width lines
l = Línea(50, 200, 50, 300, relleno=gradiente('negro', 'rojo'))
l.y1 = l.y2 = 200
l.altura = 100

l2 = Línea(350, 200, 350, 400, relleno=gradiente('negro', 'rojo'))
g = Grupo(l2)

l2.y1 = l2.y2 = 200
g.altura = 100

l3 = Línea(50, 200, 100, 200, relleno=gradiente('negro', 'rojo'))
l3.x1 = l3.x2 = 50
l3.ancho = 100

l4 = Línea(350, 200, 350, 200, relleno=gradiente('negro', 'rojo'))
g2 = Group(l4)
g2.ancho = 100

g3 = Grupo()
g3.agregar(Grupo())
g3.agregar(Circulo(1, 1, 1))
# Make sure that resizing a group that contains an empty group doesn't crash
g3.ancho += 1

x = Grupo()
y = Grupo(x)
z = Grupo(y)
add_successful = False
try:
    x.agregar(z)
    add_successful = True
except Exception:
    pass
assert not add_successful, "Recursive groups should not be allowed"

# Ensure can have attributes that translate to the same word
custom = Rect(200, 200, 200, 200, visible=Falso)
custom.reiniciar = 'a'
custom.restart = 'b'
assert custom.reiniciar == 'a'
assert custom.restart == 'b'

# Ensure that star borders are closed
Estrella(200, 200, 150, 5, relleno=None, borde='negro', anchuraDeBorde=20)

# Ensure group attribute works correctly
c = Circulo(200, 20, 5)
g = Grupo(c)

def setGroup(shape, val):
  shape.grupo = val

# should not be possible to set group
assertRaises(lambda: setGroup(c, g))

assert app.grupo.grupo == None

c.visible = Falso
assert c.grupo == None

g2 = Grupo(c)
g2.quitar(c)

assert c.grupo == None

c.visible = True
assert c.grupo == g2
assert len(g2.hijos) == 1

g.visible = Falso
g2.visible = Falso

# Ensure .toFront() doesn't crash when group is null
removedRect = Rect(200, 200, 100, 100)
app.grupo.quitar(removedRect)
removedRect.alFrente()

###########
# Ensure hitsShape works with non-filled shapes
emptyCircle = Círculo(200, 200, 200, relleno=None, borde='negro', anchuraDeBorde=50)
c2 = Círculo(70, 200, 50)
assert emptyCircle.tocaFigura(c2)
assert c2.tocaFigura(emptyCircle)

c2.centroX = 120
c2.centroY = 300
assert emptyCircle.tocaFigura(c2)
assert c2.tocaFigura(emptyCircle)

c2.centroX = 270
c2.centroY = 100
assert emptyCircle.tocaFigura(c2)
assert c2.tocaFigura(emptyCircle)


c2.centroX = 260
c2.centroY = 121
assert not emptyCircle.tocaFigura(c2)
assert not c2.tocaFigura(emptyCircle)

g = Grupo(Círculo(70, 200, 50), Círculo(280, 200, 50))

g.centroX = 350
g.centroY = 250
assert g.tocaFigura(emptyCircle) == emptyCircle.tocaFigura(g)
assert not g.tocaFigura(emptyCircle)

g.centroX = 50
g.centroY = 300
assert g.tocaFigura(emptyCircle) == emptyCircle.tocaFigura(g)
assert g.tocaFigura(emptyCircle)

g.visible = Falso
emptyCircle.visible = Falso
c2.visible = Falso
###

assert app.fondo is None
app.fondo = 'rojo'
assert app.fondo == 'rojo'
app.fondo = None
assert app.fondo is None

assert app.pausada is False
assert app.pausada == False
