# background
Line(200, 0, 200, 400, fill='steelBlue', lineWidth=400, opacity=40,
     dashes=(2, 23))
Line(50, 0, 50, 400, fill='crimson', opacity=60)

def stickFigure(x, y, size):
    # The x, y parameters describe the location of where the head and body meet.
    # Use the test cases and Inspector to see how size parameter is used when
    # drawing the stick figure.
    # head
    Circle(x, y - size, size)
    # body
    Line(x, y, x, y + 2 * size)
    # arms
    Line(x - size, y, x, y + size)
    Line(x + size, y, x, y + size)
    # legs
    Line(x, y + 2 * size, x - size, y + 3 * size)
    Line(x, y + 2 * size, x + size, y + 3 * size)

stickFigure(50, 200, 4)
stickFigure(70, 200, 8)
stickFigure(95, 200, 12)
stickFigure(130, 200, 16)
stickFigure(170, 200, 20)
stickFigure(220, 200, 24)
stickFigure(280, 200, 28)
stickFigure(350, 200, 32)


# -
# background
Line(200, 0, 200, 400, fill='steelBlue', lineWidth=400, opacity=40,
     dashes=(2, 23))
Line(50, 0, 50, 400, fill='crimson', opacity=60)

def stickFigure(x, y, size):
    # The x, y parameters describe the location of where the head and body meet.
    # Use the test cases and Inspector to see how size parameter is used when
    # drawing the stick figure.
    # head
    Circle(x, y - size, size)
    # body
    Line(x, y, x, y + 2 * size)
    # arms
    Line(x - size, y, x, y + size)
    Line(x + size, y, x, y + size)
    # legs
    Line(x, y + 2 * size, x - size, y + 3 * size)
    Line(x, y + 2 * size, x + size, y + 3 * size)

stickFigure(100, 100, 10)
stickFigure(200, 150, 10)
stickFigure(300, 100, 10)


# -
# background
Line(200, 0, 200, 400, fill='steelBlue', lineWidth=400, opacity=40,
     dashes=(2, 23))
Line(50, 0, 50, 400, fill='crimson', opacity=60)

def stickFigure(x, y, size):
    # The x, y parameters describe the location of where the head and body meet.
    # Use the test cases and Inspector to see how size parameter is used when
    # drawing the stick figure.
    # head
    Circle(x, y - size, size)
    # body
    Line(x, y, x, y + 2 * size)
    # arms
    Line(x - size, y, x, y + size)
    Line(x + size, y, x, y + size)
    # legs
    Line(x, y + 2 * size, x - size, y + 3 * size)
    Line(x, y + 2 * size, x + size, y + 3 * size)

stickFigure(150, 300, 10)

