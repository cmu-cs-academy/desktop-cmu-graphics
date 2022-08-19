###########
# Ensure i18n for list remove works

a = [0, 1, 2]
a.quitar(0)
assert a == [1, 2]

# Calling class methods with too few arguments
# On Desktop, Python handles missing arguments on its own
assertError(lambda: g.toca(), ['Falta un argumento requerido'])
assertError(lambda: g.quitar(), ['Falta un argumento requerido'])