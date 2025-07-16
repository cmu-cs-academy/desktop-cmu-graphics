def redrawAll(app):
    drawLine(0, 0, app.width, app.height, fill='red')


def onKeyPress(app, key):
    # This function must be here in order for the test harness to work
    pass


assertRaises(
    lambda: runApp(width=200, ancho=250),
    "runApp() got multiple values for argument 'ancho'",
)

assertRaises(
    lambda: runApp(ancho=200, width=250),
    "runApp() got multiple values for argument 'width'",
)

assertRaises(
    lambda: runApp(breite=200, width=250),
    "runApp() got multiple values for argument 'width'",
)

assertRaises(
    lambda: runApp(width=200, breite=250),
    "runApp() got multiple values for argument 'breite'",
)

assertRaises(
    lambda: runApp(200, width=250),
    "runApp() got multiple values for argument 'width'",
)

assertRaises(
    lambda: runApp(200, ancho=250),
    "runApp() got multiple values for argument 'ancho'",
)

assertRaises(
    lambda: runApp(200, breite=250),
    "runApp() got multiple values for argument 'breite'",
)

assertRaises(
    lambda: runApp(height=200, altura=250),
    "runApp() got multiple values for argument 'altura'",
)

assertRaises(
    lambda: runApp(altura=200, height=250),
    "runApp() got multiple values for argument 'height'",
)

assertRaises(
    lambda: runApp(altura=200, foo='bar', fizz='buzz', height=250),
    "runApp() got multiple values for argument 'height'",
)

assertRaises(
    lambda: runApp(höhe=200, height=250),
    "runApp() got multiple values for argument 'height'",
)

assertRaises(
    lambda: runApp(height=200, höhe=250),
    "runApp() got multiple values for argument 'höhe'",
)

assertRaises(
    lambda: runApp(100, 200, height=250),
    "runApp() got multiple values for argument 'height'",
)

assertRaises(
    lambda: runApp(100, 200, altura=250),
    "runApp() got multiple values for argument 'altura'",
)

assertRaises(
    lambda: runApp(100, 200, höhe=250),
    "runApp() got multiple values for argument 'höhe'",
)

assertRaises(
    lambda: runApp(width=100, ancho=150, height=200, altura=250),
    "runApp() got multiple values for argument 'ancho'",
)

assertRaises(
    lambda: runApp(ancho=100, altura=200, height=250, width=150),
    "runApp() got multiple values for argument 'height'",
)

assertRaises(
    lambda: runApp(100, width=150, height=200, foo='bar'),
    "runApp() got multiple values for argument 'width'",
)

assertRaises(
    lambda: runApp(100, 200, foo='bar', altura=250, width=300),
    "runApp() got multiple values for argument 'altura'",
)

# The language used for runApp() in the error message depends on the cmuGraphicsLanguage 
# variable, so calling ejecutaApp() will raise the same error as runApp().
assertRaises(
    lambda: ejecutaApp(100, 200, altura=250),
    "runApp() got multiple values for argument 'altura'",
)

assertRaises(
    lambda: ejecutaApp(100, 200, höhe=250),
    "runApp() got multiple values for argument 'höhe'",
)

assertRaises(
    lambda: ejecutaApp(width=100, ancho=150, height=200, altura=250),
    "runApp() got multiple values for argument 'ancho'",
)

assertRaises(
    lambda: ejecutaApp(altura=200, height=250, ancho=100, width=150),
    "runApp() got multiple values for argument 'height'",
)

assertRaises(
    lambda: ejecutaApp(100, width=150, height=200),
    "runApp() got multiple values for argument 'width'",
)

assertRaises(
    lambda: ejecutaApp(100, 200, altura=250, width=300),
    "runApp() got multiple values for argument 'altura'",
)