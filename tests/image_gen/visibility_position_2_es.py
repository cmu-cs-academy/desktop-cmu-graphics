r1 = Rect(100, 0, 200, 200, relleno='naranja')
r2 = Rect(110, 10, 200, 200, relleno='verde', visible=Falso)
r3 = Rect(180, 80, 200, 200, relleno='naranja')


r1.visible = Falso
r2.visible = Verdadero

# -

a = Rect(50, 250, 50, 50, relleno='negro', visible=Falso)
b = Rect(60, 260, 50, 50, relleno='rojo', visible=Falso)

a.visible=Verdadero
b.visible=Verdadero


# -

a = Rect(100, 250, 50, 50, relleno='negro', visible=Falso)
b = Rect(110, 260, 50, 50, relleno='rojo', visible=Falso)

b.visible=Verdadero
a.visible=Verdadero


# -

a = Rect(150, 250, 100, 100, relleno='negro')
c = Rect(170, 270, 100, 100, relleno='rosado')
b = Rect(160, 260, 100, 100, relleno='rojo')

c.alFrente()
b.visible = Falso
b.visible = Verdadero
