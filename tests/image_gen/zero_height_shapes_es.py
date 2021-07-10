o = Óvalo(100, 200, 100, 0.0000000001, rotarÁngulo=45, db='all')
assert o.centroX == 100, o.centroX
assert o.centroY == 200, o.centroY

l = Línea(0, 200, 400, 200, anchuraDeLínea=0.000000001)
# -
l.rotarÁngulo += 30
# -
l.rotarÁngulo += 30
# -
l.rotarÁngulo += 30

p = Polígono(10, 10, 10, 200, db='all')
assert p.centroX == 10
assert p.centroY == 105
