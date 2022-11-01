def assertError(fn, errorKeywords):
    raised = True
    try:
        fn()
        raised = False
    except Exception as e:
        msg = str(e).lower()
        for kw in errorKeywords:
          if not kw.lower() in msg:
            raise Exception(f'error message should contain {kw} but was {msg}')
    if not raised:
        raise Exception('fn failed to raise an exception')

############
# Ensure i18n for list remove works

a = [0, 1, 2]
a.quitar(0)
assert a == [1, 2]

############
# Calling class methods with too few arguments
# On Desktop, Python handles missing arguments on its own
assertError(lambda: Group().toca(), ['Falta un argumento requerido'])
assertError(lambda: Group().quitar(), ['Falta un argumento requerido'])

############
# Passing in a user-defined object as an rgb color
# On Desktop, the A object is printed like <__main__.f.<locals>.A object at 0x7faf2e5d3730>
class A:
    pass
assertRaises(lambda: rgb(A(), 2, 3), "rgb.red debe ser número (pero <__main__.A object> es de tipo A)")
