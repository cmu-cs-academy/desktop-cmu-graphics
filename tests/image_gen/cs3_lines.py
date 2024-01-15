def redrawAll(app):
    drawLine(100, 300, 200, 300, dashes=True)
    drawLine(100, 310, 200, 310, dashes=False)
    drawLine(100, 320, 200, 320, dashes=(5, 10))
    drawLine(100, 330, 200, 330, dashes=(5, 10, 20, 10))
    assertRaises(lambda: drawLine(100, 330, 200, 330, dashes='asdf'),
                 "Line.dashes should be bool (but 'asdf' is of type str)")
