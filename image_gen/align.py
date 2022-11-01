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

makeShapes(Rect, [100, 200, 100, 150])
# -
for shape in app.group: shape.visible = False
makeShapes(Oval, [100, 200, 100, 150])
# -
for shape in app.group: shape.visible = False
makeShapes(Star, [100, 200, 50, 5])
