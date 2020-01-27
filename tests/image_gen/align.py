def makeShapes(shapeType, args):
    shapeType(*args, fill='gray')

    for align in [
            'left', 'top-left', 'right', 'right-top',
            'bottom', 'bottom-right', 'bottom-left',
            'top', 'center'
        ]:
        r = shapeType(*args, fill='blue', align=align, opacity=50, rotateAngle=10, db='bbox')
        if 'left' in align:
            assert r.left == 100, r.left
        elif 'right' in align:
            assert r.right == 100, r.right
        else:
            assert r.centerX == 100, r.centerX

        if 'top' in align:
            assert r.top == 200, r.top
        elif 'bottom' in align:
            assert r.bottom == 200, r.bottom
        else:
            assert r.centerY == 200, r.centerY

    # Try to get or set the align property
    r = shapeType(*args, fill='blue', align=align, opacity=50, rotateAngle=10, db='bbox')
    for align in [
            'left', 'top-left', 'right', 'right-top',
            'bottom', 'bottom-right', 'bottom-left',
            'top', 'center'
        ]:
        errorMsg = ''
        try:
            print(r.align)
        except Exception as e:
            errorMsg = str(e)

        try:
            r.align = align
        except Exception as e:
            errorMsg = str(e)

        if (errorMsg != "You can't get or set the align property"):
            assert False



makeShapes(Rect, [100, 200, 100, 150])

# -
def makeShapes(shapeType, args):
    shapeType(*args, fill='gray')

    for align in [
            'left', 'top-left', 'right', 'right-top',
            'bottom', 'bottom-right', 'bottom-left',
            'top', 'center'
        ]:
        r = shapeType(*args, fill='blue', align=align, opacity=50, rotateAngle=10, db='bbox')
        if 'left' in align:
            assert r.left == 100, r.left
        elif 'right' in align:
            assert r.right == 100, r.right
        else:
            assert r.centerX == 100, r.centerX

        if 'top' in align:
            assert r.top == 200, r.top
        elif 'bottom' in align:
            assert r.bottom == 200, r.bottom
        else:
            assert r.centerY == 200, r.centerY
for shape in app.group: shape.visible = False
makeShapes(Oval, [100, 200, 100, 150])

# -
def makeShapes(shapeType, args):
    shapeType(*args, fill='gray')

    for align in [
            'left', 'top-left', 'right', 'right-top',
            'bottom', 'bottom-right', 'bottom-left',
            'top', 'center'
        ]:
        r = shapeType(*args, fill='blue', align=align, opacity=50, rotateAngle=10, db='bbox')
        if 'left' in align:
            assert r.left == 100, r.left
        elif 'right' in align:
            assert r.right == 100, r.right
        else:
            assert r.centerX == 100, r.centerX

        if 'top' in align:
            assert r.top == 200, r.top
        elif 'bottom' in align:
            assert r.bottom == 200, r.bottom
        else:
            assert r.centerY == 200, r.centerY
for shape in app.group: shape.visible = False
makeShapes(Star, [100, 200, 50, 5])
