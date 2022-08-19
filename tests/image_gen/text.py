l1 = Label('     Hello', 200, 175, size=40, db='all')
l2 = Label('Hello', 200, 125, size=40, db='all')
l3 = Label('Hello     ', 200, 225, size=40, db='all')

g = Group(l1, l2, l3)

# -

g.rotateAngle += 45

# -
g.visible = False
l = Label([1, 2, 3], 200, 200)

# -
l.value = [None]

# -
# Mutate l.value
d = {'a': 1}
l.value = d

d['a'] = 10

# Ensure __repr__ for labels is correct
assert str(l) == "Label({'a': 10}, 200, 200)", str(l)

# -
# Change l.value and ensure label dimensions are updated
l.value = ""
l.value = "--------------------"
l.left = 200
