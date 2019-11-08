l1 = Label('     Hello', 200, 175, size=40, db='all')
l2 = Label('Hello', 200, 125, size=40, db='all')
l3 = Label('Hello     ', 200, 225, size=40, db='all')

g = Group(l1, l2, l3)

# -

g.rotateAngle += 45
