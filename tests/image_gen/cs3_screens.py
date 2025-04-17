# activeScreen should be set right before a call to onScreenActivate
# If event handler "onFoo" calls setActiveScreen, "onFoo" and its corresponding
# call to redrawAll should both complete before the next call to onScreenActivate

from collections import defaultdict

def onAppStart(app):
    assert not hasattr(app, 'activeScreen')
    assert not hasattr(app, 'function_call_count')
    app.function_call_count = defaultdict(int)

def b_onAppStart(app):
    assert 'a_onAppStart' in app.function_call_count
    assert 'b_onAppStart' not in app.function_call_count
    app.function_call_count['b_onAppStart'] += 1

def a_onAppStart(app):
    assert 'a_onAppStart' not in app.function_call_count
    assert 'b_onAppStart' not in app.function_call_count
    app.function_call_count['a_onAppStart'] += 1

def a_onScreenActivate(app):
    assert 'a_onAppStart' in app.function_call_count
    assert 'b_onAppStart' in app.function_call_count
    assert app._app.activeScreen == 'a'
    app.function_call_count['a_onScreenActivate'] += 1

def b_onScreenActivate(app):
    assert app._app.activeScreen == 'b'
    assert app.function_call_count['a_redrawAll'] == 2
    app.function_call_count['b_onScreenActivate'] += 1

def a_onMousePress(app, mouseX, mouseY):
    app.function_call_count['a_onMousePress'] += 1
    setActiveScreen('b')
    assert app._app.activeScreen == 'a'
    assert 'b_onScreenActivate' not in app.function_call_count
    assert 'b_redrawAll' not in app.function_call_count

def a_redrawAll(app):
    assert app._app.activeScreen == 'a'
    assert 'b_onScreenActivate' not in app.function_call_count
    if app.function_call_count['a_redrawAll'] == 0:
        assert 'a_onScreenActivate' in app.function_call_count
    if app.function_call_count['a_redrawAll'] == 1:
        assert 'a_onMousePress' in app.function_call_count
    app.function_call_count['a_redrawAll'] += 1
    drawRect(0,0,200,200,fill='blue')

def b_redrawAll(app):
    assert app._app.activeScreen == 'b'
    assert app.function_call_count['b_onScreenActivate'] == 1
    drawRect(200,200,200,200,fill='red')
