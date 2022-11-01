def crearFiguras(tipoDeFigura, args):
    tipoDeFigura(*args, relleno='gris')

    for alinear in [
            'izquierda', 'superior-izquierda', 'derecha', 'derecha-superior',
            'inferior', 'inferior-derecha', 'inferior-izquierda',
            'superior', 'centro'
        ]:
        r = tipoDeFigura(*args, relleno='azul', alinear=alinear, opacidad=50, rotarÁngulo=10, db='bbox')
        if 'izquierda' in alinear:
            assert r.izquierda == 100, r.izquierda
        elif 'derecha' in alinear:
            assert r.derecha == 100, r.derecha
        else:
            assert r.centroX == 100, r.centroX

        if 'superior' in alinear:
            assert r.superior == 200, r.superior
        elif 'inferior' in alinear:
            assert r.inferior == 200, r.inferior
        else:
            assert r.centroY == 200, r.centroY

crearFiguras(Rect, [100, 200, 100, 150])
# -
for figura in app.grupo: figura.visible = Falso
crearFiguras(Óvalo, [100, 200, 100, 150])
# -
for figura in app.grupo: figura.visible = Falso
crearFiguras(Estrella, [100, 200, 50, 5])
