from collections import defaultdict

def enInicioDeApp(app):
    assert not hasattr(app, 'activeScreen')
    assert not hasattr(app, 'function_call_count')
    app.function_call_count = defaultdict(int)

def b_enInicioDeApp(app):
    assert 'a_enInicioDeApp' in app.function_call_count
    assert 'b_enInicioDeApp' not in app.function_call_count
    app.function_call_count['b_enInicioDeApp'] += 1

def a_enInicioDeApp(app):
    assert 'a_enInicioDeApp' not in app.function_call_count
    assert 'b_enInicioDeApp' not in app.function_call_count
    app.function_call_count['a_enInicioDeApp'] += 1

def a_enPantallaActivada(app):
    assert 'a_enInicioDeApp' in app.function_call_count
    assert 'b_enInicioDeApp' in app.function_call_count
    assert app._app.activeScreen == 'a'
    app.function_call_count['a_enPantallaActivada'] += 1

def b_enPantallaActivada(app):
    assert app._app.activeScreen == 'b'
    assert app.function_call_count['a_redibujaTodo'] == 2
    app.function_call_count['b_enPantallaActivada'] += 1

def a_enRatónPresionado(app, ratónX, ratónY):
    app.function_call_count['a_enRatónPresionado'] += 1
    establecePantallaActiva('b')
    assert app._app.activeScreen == 'a'
    assert 'b_enPantallaActivada' not in app.function_call_count
    assert 'b_redibujaTodo' not in app.function_call_count

def a_redibujaTodo(app):
    assert app._app.activeScreen == 'a'
    assert 'b_enPantallaActivada' not in app.function_call_count
    if app.function_call_count['a_redibujaTodo'] == 0:
        assert 'a_enPantallaActivada' in app.function_call_count
    if app.function_call_count['a_redibujaTodo'] == 1:
        assert 'a_enRatónPresionado' in app.function_call_count
    app.function_call_count['a_redibujaTodo'] += 1
    dibujaRect(0,0,200,200,relleno='azul')

def b_redibujaTodo(app):
    assert app._app.activeScreen == 'b'
    assert app.function_call_count['b_enPantallaActivada'] == 1
    dibujaRect(200,200,200,200,relleno='rojo')
