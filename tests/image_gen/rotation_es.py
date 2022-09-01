r = Círculo(100, 100, 50)
o = Óvalo(100, 100, 100, 30, relleno='rojo')
rp =  PolígonoRegular(100, 100, 50, 3, relleno='verde')

centro = Círculo(0, 0, 2, relleno='azul')

def mover():
    for s in [r, rp, o]:
        s.izquierda += 10
        s.superior += 10
        s.rotarÁngulo += 15
    for s in [r, rp, o]:
        assert rounded(s.centroX) == rounded(r.centroX)
        assert rounded(s.centroY) == rounded(r.centroY)
    centro.centroX = s.centroX
    centro.centroY = s.centroY

# -
mover()

# -
mover()

# -
mover()

# -
for _ in range(15): mover()




# -
def probarRotar(ángulos):
    luna = Círculo(0, 200, 50, relleno=gradiente('gris', 'azulpolvo', inicio='izquierda'))

    baseX = luna.centroX
    baseY = luna.centroY
    assert (baseX, baseY) == (0, 200)

    ángulos = list(ángulos)
    for ángulo in ángulos:
        baseX += 27
        luna.centroX += 27
        baseY += 13
        luna.centroY += 13
        luna.rotarÁngulo = ángulo

        assert (luna.izquierda, luna.centroX, luna.derecha) == (baseX-50, baseX, baseX+50), (
            ángulo, baseX, (luna.izquierda, luna.centroX, luna.derecha))
        assert (luna.superior, luna.centroY, luna.inferior) == (baseY-50, baseY, baseY+50), (
            ángulo, baseY, (luna.superior, luna.centroY, luna.inferior))
    luna.visible = Falso
    print(ángulos, 'pasado')


probarRotar([0] * 10)
probarRotar([90] * 10)
probarRotar([180] * 10)
probarRotar(x * 90 for x in range(10))
probarRotar(x * 450 for x in range(10))
probarRotar(x * 360 for x in range(10))


# -
# Prueba rotando un arco alrededor de un centro que no es el centro del círculo
a = Arco(200, 200, 150, 150, 90, 180, db='all')
r = Rect(0, 0, 10, 10)
g = Grupo(a, r)
g.rotarÁngulo += 45

Rect(390, 390, 10, 10, relleno='verde')
