l1 = Rótulo('     Hello', 200, 175, tamaño=40, db='all')
l2 = Rótulo('Hello', 200, 125, tamaño=40, db='all')
l3 = Rótulo('Hello     ', 200, 225, tamaño=40, db='all')

g = Grupo(l1, l2, l3)

# -

g.rotarÁngulo += 45