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

# Normal definitions should still work
c = Circle(100, 200, 30)
r = Rect(200, 200, 100, 100)
g = Group(c, r)

# Error should differentiate between tuples and lists
assertError(lambda: Circle((1, 2), 10, 10), ['tuple', 'Circle', 'centerX', '(1, 2)'])
assertError(lambda: Circle(10, [1, 2], 10), ['list', 'Circle', 'centerY', '[1, 2]'])

# Error should work if shapes passed as argument
assertError(lambda: Circle(c, 20, 20), ['Circle(100, 200, 30)', 'centerX'])

# Error should work on functions
assertError(lambda: Circle(lambda x: x * x, 20, 20), ['centerX', 'Circle', 'lambda'])

# Group.add typechecking
assertError(lambda: Group(1), ['int', 'Group', 'add'])
assertError(lambda: Group().add(1), ['int', 'Group', 'add'])
assertError(lambda: Group((1, 2)), ['tuple', 'Group', 'add', '(1, 2)'])
assertError(lambda: Group().add((1, 2)), ['tuple', 'Group', 'add', '(1, 2)'])
assertError(lambda: Group().add([1, 2]), ['list', 'Group', 'add', '[1, 2]'])

# Shape.contains
assertError(lambda: c.contains((2, 3), 1), ['tuple', 'contains', 'x', '(2, 3)'])

# Rect typechecking should say Rect, not Polygon
assertError(lambda: Rect(0, 0, "hi", 0), ['str', 'Rect.width'])

# type() should work without printing module name
assert(str(type(c)) == "<class 'Circle'>")
assert(repr(type(c)) == "<class 'Circle'>")

# Group should disallow fill/border in constructor
assertError(lambda: Group(Circle(100, 100, 20), Circle(200, 200, 20), fill='blue'), [])

# Check incorrect aligns
assertError(lambda: Circle(100, 100, 20, align='hi'), ['hi', 'align'])

# Check invalid colors
assertError(lambda: Circle(100, 100, 20, fill='hi'), ['hi', 'fill'])
assertError(lambda: Circle(100, 100, 20, border='hi'), ['hi', 'border'])

# Check invalid gradients colors/starts
assertError(lambda: gradient('red', 'blue', start='hi'), ['hi', 'start'])
assertError(lambda: gradient(None, 'blue'), ['None'])
assertError(lambda: gradient(gradient('red', 'blue'), 'blue'), ["gradient('red', 'blue'"])

def changeBackground():
    app.background = 20
assertError(changeBackground, ['20', 'background'])

# Checks pointList
p = Polygon(200, 200, 300, 200, 300, 300, 200, 300)
assert(p.pointList == [[200, 200], [300, 200], [300, 300], [200, 300]])

def changePointList(val):
    p.pointList = val
assertError(lambda: changePointList('hi'), ['pointList', 'hi', 'str'])
assertError(lambda: changePointList(None), ['pointList', 'None', 'NoneType'])
assertError(lambda: changePointList([100]), ['pointList', '100'])
assertError(lambda: changePointList([[100, 200], [100]]), ['pointList', '[100]', 'length'])

changePointList([[300, 300], [300, 400], [400, 400], [400, 300]])

# RGBs / Gradients should typecheck correctly
assertError(lambda: rgb(None, 2, 3), ['RGB.red', 'None'])
assertError(lambda: rgb([2, 3], 2, 3), ['RGB.red', 'list'])
assertError(lambda: gradient(None, None), ['gradient.colors', 'None'])
assertError(lambda: gradient('hi', 'red'), ['hi'])
assertError(lambda: rgb(300, 100, 100), ['RGB.red', '300'])

# Typecheck app properties
def setMaxShapes(val):
    app.maxShapeCount = val

assertError(lambda: setMaxShapes(-20), ['maxShapeCount', '-20'])
assertError(lambda: setMaxShapes(None), ['maxShapeCount', 'None', 'NoneType'])
assertError(lambda: setMaxShapes((1, 2)), ['maxShapeCount', '(1, 2)', 'tuple'])
assertError(lambda: setMaxShapes([1, 2]), ['maxShapeCount', '[1, 2]', 'list'])
app.maxShapeCount = 100

# Images should typecheck
assertError(lambda: Image(''), ['Arg Count'])
assertError(lambda: Image(None, 20, 20), ['Image.url', 'None', 'NoneType'])
assertError(lambda: Image('https://s3.amazonaws.com/cmu-cs-academy.lib.prod/default_avatar.png', None, 20), ['Image.left', 'None', 'NoneType'])

# Sounds should typecheck
assertError(lambda: Sound(None), ['Sound.url', 'None', 'NoneType'])

# Fix kwarg typechecking
assertError(lambda: Rect(200, 200, 200, 200, fill={1:2}), ['{1: 2}', 'Rect.fill', 'dict'])

assertError(lambda: Line(5, 5, 20, 20, align='center'), ['unexpected keyword', 'align'])
assertError(lambda: Arc(0, 0, 20, 20, 0, 180, align='center'), ['unexpected keyword', 'align'])
assertError(lambda: Polygon(0, 0, 20, 20, 0, 180, align='center'), ['unexpected keyword', 'align'])
assertError(lambda: Label('Hello', 20, 20, dashes=True), ['unexpected keyword', 'dashes'])

def assignToMethod(obj, attr):
    setattr(obj, attr, 0)

assertError(lambda: assignToMethod(r, 'hits'), ["can't assign"])
assertError(lambda: assignToMethod(g, 'add'), ["can't assign"])
