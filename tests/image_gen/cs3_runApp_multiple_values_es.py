def redrawAll(app):
    drawLine(0, 0, app.width, app.height, fill='red')


def onKeyPress(app, key):
    # This function must be here in order for the test harness to work
    pass


assertRaises(
    lambda: runApp(width=200, ancho=250),
    "ejecutaApp() got multiple values for argument 'ancho'",
)

assertRaises(
    lambda: runApp(breite=200, width=250),
    "ejecutaApp() got multiple values for argument 'width'",
)

assertRaises(
    lambda: runApp(200, width=250),
    "ejecutaApp() got multiple values for argument 'width'",
)

assertRaises(
    lambda: ejecutaApp(width=100, ancho=150, height=200, altura=250),
    "ejecutaApp() got multiple values for argument 'ancho'",
)
