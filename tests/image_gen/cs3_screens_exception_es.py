def enInicioDeApp(app):
    pass

def a_enInicioDeApp(app):
    pass

def b_enInicioDeApp(app):
    pass

def a_enRatónPresionado(app, mouseX, mouseY):
    assertRaises(lambda: establecePantallaActiva('b'), "Pantalla 'b' requiere 'b_redibujaTodo()'")

def a_redrawAll(app):
    # Just for funsies, the point of the test is to ensure an exception is raised
    # when trying to activate a screen without an associated redrawAll definition
    dibujaRect(0, 0, 400, 400, fill='verdeBosque')
    dibujaPolígono(200, 60, 340, 200, 200, 340, 60, 200, fill='oro')
    dibujaCírculo(200, 200, 70, fill='azulOscuro')
