import sys
sys.path.insert(0, "..")
from cmu_graphics import *

def onMousePress(x, y):
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
            try:
                print(r.align)
            except Exception as e:
                if (str(e) != "You can't get or set the align property"):
                    assert False
    
            try:
                r.align = align
            except Exception as e:
                if (str(e) != "You can't get or set the align property"):
                    assert False
    
    
    
    makeShapes(Rect, [100, 200, 100, 150])
    app.background = "honeydew"
from threading import Timer

import time
def screenshotAndExit():
    app.callUserFn("onMousePress", (200,200))
    time.sleep(1)
    app.getScreenshot("C:/Users/311eh/Documents/Work/CS_Academy2/cpython-cmu-graphics/tests/image_gen/align/output_1.png")
    app.quit()
Timer(3, screenshotAndExit).start()
cmu_graphics.loop()