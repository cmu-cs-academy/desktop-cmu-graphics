assert gradiente('rojo', 'azul') == gradiente('rojo', 'azul')
assert gradiente('rojo', 'azul', inicio='centro') == gradiente('rojo', 'azul')
assert gradiente('rojo', 'azul', inicio='izquierda') == gradiente('rojo', 'azul', inicio='izquierda')

assert gradiente('rojo', 'azul') != gradiente('rojo', 'azul', inicio='izquierda')
assert gradiente('rojo', 'azul', inicio='izquierda') != gradiente('rojo', 'azul')
assert gradiente('rojo', 'verde') != gradiente('rojo', 'azul')
assert gradiente('rojo', 'azul', 'naranja') != gradiente('rojo', 'azul')


assert rgb(0, 0, 0) == rgb(0, 0, 0)
assert rgb(1, 0, 0) != rgb(0, 0, 0)
assert rgb(0, 1, 0) != rgb(0, 0, 0)
assert rgb(0, 0, 1) != rgb(0, 0, 0)

assert gradiente('rojo', rgb(0, 0, 5)) == gradiente('rojo', rgb(0, 0, 5))

assert gradiente('rojo', rgb(0, 0, 5)) != gradiente('rojo', rgb(0, 5, 0))
assert gradiente('rojo', rgb(0, 0, 5)) != gradiente('rojo', 'verde')
assert gradiente('rojo', 'verde') != gradiente('rojo', rgb(0, 0, 5))

rect = Rect(50, 50, 150, 150, relleno=gradiente('naranja', 'rojo'))
assert rect.relleno == gradiente('naranja', 'rojo')
