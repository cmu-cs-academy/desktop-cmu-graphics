l1 = Rótulo('     Hello', 200, 175, tamaño=40, db='all')
l2 = Rótulo('Hello', 200, 125, tamaño=40, db='all')
l3 = Rótulo('Hello     ', 200, 225, tamaño=40, db='all')

g = Grupo(l1, l2, l3)

# -

g.rotarÁngulo += 45

# -
g.visible = Falso
l = Rótulo([1, 2, 3], 200, 200)

# -
l.valor = [None]

# -
d = {'a': 1}
l.valor = d

d['a'] = 10

# Ensure __repr__ for labels is correct
assert str(l) == "Rótulo({'a': 10}, 200, 200)"

# -
l.valor = ""
l.valor = "--------------------"
l.izquierda = 200