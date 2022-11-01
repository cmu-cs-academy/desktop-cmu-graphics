a = Arco(50, 100, 100, 200, 45, 135, db='all')

# -

a.rotarÁngulo = 90

# -

a.ancho = 300

# -
a.ánguloDeBarrido = 20

# -
a.rotarÁngulo += 20

Arco(350, 350, 100, 50, 0, 270, borde='rojo', relleno='azul')

Arco(250, 350, 100, 50, 0, 270, borde='rojo', relleno='azul', db='all')

# Verifique que la línea unida en el centro no se vuelva demasiado grande
Arco(300, 60, 80, 80, 0, 345, anchuraDeBorde=4, relleno=None, borde='verde')
