def enInicioDeApp(app):
    pass

def a_enInicioDeApp(app):
    pass

def b_enInicioDeApp(app):
    pass

def a_enRatónPresionado(app, mouseX, mouseY):
    assertRaises(lambda: establecePantallaActiva('b'), "Pantalla 'b' requiere 'b_redibujaTodo()'")

def a_redrawAll(app):
    dibujaRect(0, 0, 400, 400, fill='verdeBosque')
    dibujaPolígono(200, 60, 340, 200, 200, 340, 60, 200, fill='oro')
    dibujaCírculo(200, 200, 70, fill='azulOscuro')
