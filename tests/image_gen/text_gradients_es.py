l = Rótulo('Hi', 50, 50, tamaño=50, relleno=gradiente('rojo', 'azul', inicio='izquierda-superior'))

Rótulo('Hi', l.derecha + 50, 50, tamaño=50, rotarÁngulo=180, relleno=gradiente('rojo', 'azul', inicio='izquierda-superior'))


Rótulo('Hello, world!', 200, 175, tamaño=60, db='bbox center', relleno=gradiente('rojo', 'naranja'))
Rótulo('Hello, world!', 200, 200, tamaño=60, rotarÁngulo=135, db='bbox center', relleno=gradiente('rojo', 'naranja'))
Rótulo('Hello, world!', 200, 250, tamaño=60, rotarÁngulo=180, db='bbox center', relleno=gradiente('rojo', 'naranja'))

Rótulo('Hello, world!', 200, 300, tamaño=60, rotarÁngulo=195, db='bbox center',
    relleno='naranja', borde=gradiente('verde', 'azul', inicio='inferior'),
    anchuraDeBorde=2)
