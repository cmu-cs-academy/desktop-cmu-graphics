def rotarTodos(grados):
    for s in app.grupo:
        s.rotarÁngulo += grados

Rect(0, 0, 100, 100, relleno=gradiente('rojo', 'naranja', inicio='izquierda'))
Rect(150, 0, 100, 100, relleno=gradiente('rojo', 'naranja'))

Estrella(100, 100, 50, 5, relleno=gradiente('rosado', 'azul'))
Estrella(150, 100, 50, 5, relleno=gradiente('rosado', 'azul', inicio='inferior'))

Polígono(40, 170, 60, 110, 90, 170, 90, 200, 170, 250, 90, 210, 70, 240, 20, 220,
relleno=gradiente('rosado', 'verde'))
Polígono(140, 170, 160, 110, 190, 170, 190, 200, 270, 250, 190, 210, 170, 240, 120, 220,
relleno=gradiente('rosado', 'verde', inicio='derecha-inferior'))

# -
rotarTodos(10)
# -
rotarTodos(90)
# -
rotarTodos(90)
# -
rotarTodos(90)
