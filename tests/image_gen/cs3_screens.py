def onAppStart(app):
    assert not hasattr(app, 'init_dict')
    app.init_dict = {}

def b_onAppStart(app):
    assert 'a_onAppStart' in app.init_dict
    assert 'b_onAppStart' not in app.init_dict
    app.init_dict['b_onAppStart'] = True

def a_onAppStart(app):
    assert 'a_onAppStart' not in app.init_dict
    assert 'b_onAppStart' not in app.init_dict
    app.init_dict['a_onAppStart'] = True


def a_onScreenActivate(app):
    assert app.init_dict['b_onAppStart']
    app.init_dict['a_onScreenActivate'] = True
    app.calledKey = False

def a_redrawAll(app):
    assert app.init_dict['a_onScreenActivate']
    drawRect(0,0,200,200,fill='blue')
    if app.calledKey:
        drawRect(50,0,200,200,fill='green')

def a_onKeyPress(app, key):
    app.calledKey = True

def b_redrawAll(app):
    drawRect(0,0,200,200,fill='red')
