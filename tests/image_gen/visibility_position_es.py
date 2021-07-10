r1 = Rect(100, 0, 200, 200, relleno='naranja')
r2 = Rect(100, 100, 200, 200, relleno='verde', visible=Falso)

c1 = Círculo(100, 180, 60, relleno='azul')
c2 = Círculo(200, 180, 60, relleno='cian')
c3 = Círculo(300, 180, 60, relleno='azulmarino')
g = Grupo(c1, c2, c3)

r3 = Rect(100, 200, 200, 200, relleno='amarillo')

# -
r2.visible = Verdadero

# -
r2.visible = Falso

# -
r2.visible = Verdadero
r1.visible = Falso

# -
r1.visible = Verdadero
g.visible = Falso

# -
g.visible = Verdadero

# -
c1.visible = Falso

# -
c1.visible = Verdadero
c2.visible = Falso

# -
c2.visible = Verdadero
c3.visible = Falso

# -
c3.visible = Verdadero

# -
x = 50
a = Círculo(x, 370, 30)
b = Círculo(x, 370, 10, relleno="rojo")
c = Círculo(x, 370, 5, relleno="verde")
a.visible = Falso
b.visible = Falso
a.visible = Verdadero
b.visible = Verdadero

x += 50
a = Círculo(x, 370, 30)
b = Círculo(x, 370, 10, relleno="rojo")
c = Círculo(x, 370, 5, relleno="verde")
a.visible = Falso
b.visible = Falso
b.visible = Verdadero
a.visible = Verdadero

x += 50
a = Círculo(x, 370, 30)
b = Círculo(x, 370, 10, relleno="rojo")
c = Círculo(x, 370, 5, relleno="verde")
b.visible = Falso
a.visible = Falso
b.visible = Verdadero
a.visible = Verdadero

x += 50
a = Círculo(x, 370, 30)
b = Círculo(x, 370, 10, relleno="rojo")
c = Círculo(x, 370, 5, relleno="verde")
b.visible = Falso
a.visible = Falso
a.visible = Verdadero
b.visible = Verdadero
