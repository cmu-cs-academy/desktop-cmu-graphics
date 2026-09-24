from collections import defaultdict

function_call_count = defaultdict(int)

def enInicioDeApp(app):
    assert not hasattr(app, 'activeScreen')

def b_enInicioDeApp(app):
    assert 'a_enInicioDeApp' in function_call_count
    assert 'b_enInicioDeApp' not in function_call_count
    function_call_count['b_enInicioDeApp'] += 1

def a_enInicioDeApp(app):
    assert 'a_enInicioDeApp' not in function_call_count
    assert 'b_enInicioDeApp' not in function_call_count
    function_call_count['a_enInicioDeApp'] += 1

def a_enActivaciónDePantalla(app):
    assert 'a_enInicioDeApp' in function_call_count
    assert 'b_enInicioDeApp' in function_call_count
    assert app._app.activeScreen == 'a'
    function_call_count['a_enActivaciónDePantalla'] += 1

def b_enActivaciónDePantalla(app):
    assert app._app.activeScreen == 'b'
    assert function_call_count['a_redibujaTodo'] == 2
    function_call_count['b_enActivaciónDePantalla'] += 1

def a_enRatónPresionado(app, ratónX, ratónY):
    function_call_count['a_enRatónPresionado'] += 1
    establecePantallaActiva('b')
    assert app._app.activeScreen == 'a'
    assert 'b_enActivaciónDePantalla' not in function_call_count
    assert 'b_redibujaTodo' not in function_call_count

def a_redibujaTodo(app):
    assert app._app.activeScreen == 'a'
    assert 'b_enActivaciónDePantalla' not in function_call_count
    if function_call_count['a_redibujaTodo'] == 0:
        assert 'a_enActivaciónDePantalla' in function_call_count
    if function_call_count['a_redibujaTodo'] == 1:
        assert 'a_enRatónPresionado' in function_call_count
    function_call_count['a_redibujaTodo'] += 1
    dibujaRect(0,0,200,200,relleno='azul')

def b_redibujaTodo(app):
    assert app._app.activeScreen == 'b'
    assert function_call_count['b_enActivaciónDePantalla'] == 1
    dibujaRect(200,200,200,200,relleno='rojo')
