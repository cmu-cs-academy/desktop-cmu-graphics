def probarFigura(s, delta):
    assert s.centroX == 200, s.centroX
    assert s.centroY == 200, s.centroY
    assert s.izquierda < s.centroX, s.izquierda
    assert s.centroX < s.derecha, s.derecha

    original_izquierda = s.izquierda
    s.derecha += delta
    assert rounded(s.izquierda - original_izquierda) == delta, s.izquierda - original_izquierda
    assert s.centroX == 200 + delta, s.centroX

    s.puntos += 4
    assert s.centroX == 200 + delta, s.centroX


poliReg = PolígonoRegular(200, 200, 50, 3, opacidad=50)
probarFigura(poliReg, 10)

estrella = Estrella(200, 200, 50, 10, opacidad=50)
probarFigura(estrella, -10)


def dibujarLímitesDeEstrella(s):
    Rect(s.centroX - 50, s.superior, 100, 1, relleno='rojo')
    Rect(s.centroX - 50, s.inferior, 100, 1, relleno='azul')
    Rect(s.izquierda, s.centroY - 50, 1, 100, relleno='verde')
    Rect(s.derecha, s.centroY - 50, 1, 100, relleno='amarillo')

s = Estrella(100, 100, 50, 3, rotarÁngulo=10)
dibujarLímitesDeEstrella(s)

s = Estrella(100, 300, 50, 3)
dibujarLímitesDeEstrella(s)
