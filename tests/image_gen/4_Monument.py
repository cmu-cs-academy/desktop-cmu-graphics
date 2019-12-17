# These are facts about the Washington Monument that are helpful for this
# exercise:
#    The American flag was planted in 1776.
#    The bottom section of the monument was built in 1854.
#    The top section of the monument was built in 1884.
#    The reflecting pool was added in 1923.

# sky and grass
Rect(0, 0, 400, 350,
     fill=gradient('lightSkyBlue', 'lightSkyBlue', 'lightCyan', start='top'))
Rect(0, 350, 400, 150, fill='forestGreen')

def drawMonument(year):
    # Draw the flag, sections of the monument, and Reflecting Pool based
    # on the year.
    # Label for the year
    Label(year, 10, 10, size=50, align='left-top')

    # American Flag
    if (year >= 1776):
        Rect(270, 300, 30, 20, fill='red')
        Line(285, 302, 285, 320, fill='white', lineWidth=30, dashes=(1, 2))
        Rect(270, 300, 15, 10, fill='blue')
        Line(270, 300, 270, 350)

    # bottom section of monument
    if (year >= 1854):
        Polygon(170, 350, 175, 275, 225, 275, 230, 350, fill='cornSilk')

    # top section of monument
    if (year >= 1884):
        Polygon(175, 275, 185, 70, 200, 40, 215, 70, 225, 275,
                fill='blanchedAlmond')

    # Reflecting Pool
    if (year >= 1923):
        Polygon(150, 350, 120, 400, 280, 400, 250, 350, border='grey',
                fill=gradient('paleTurquoise', 'deepSkyBlue', start='top'))

drawMonument(1692)


# -
# These are facts about the Washington Monument that are helpful for this
# exercise:
#    The American flag was planted in 1776.
#    The bottom section of the monument was built in 1854.
#    The top section of the monument was built in 1884.
#    The reflecting pool was added in 1923.

# sky and grass
Rect(0, 0, 400, 350,
     fill=gradient('lightSkyBlue', 'lightSkyBlue', 'lightCyan', start='top'))
Rect(0, 350, 400, 150, fill='forestGreen')

def drawMonument(year):
    # Draw the flag, sections of the monument, and Reflecting Pool based
    # on the year.
    # Label for the year
    Label(year, 10, 10, size=50, align='left-top')

    # American Flag
    if (year >= 1776):
        Rect(270, 300, 30, 20, fill='red')
        Line(285, 302, 285, 320, fill='white', lineWidth=30, dashes=(1, 2))
        Rect(270, 300, 15, 10, fill='blue')
        Line(270, 300, 270, 350)

    # bottom section of monument
    if (year >= 1854):
        Polygon(170, 350, 175, 275, 225, 275, 230, 350, fill='cornSilk')

    # top section of monument
    if (year >= 1884):
        Polygon(175, 275, 185, 70, 200, 40, 215, 70, 225, 275,
                fill='blanchedAlmond')

    # Reflecting Pool
    if (year >= 1923):
        Polygon(150, 350, 120, 400, 280, 400, 250, 350, border='grey',
                fill=gradient('paleTurquoise', 'deepSkyBlue', start='top'))

drawMonument(1884)


# -
# These are facts about the Washington Monument that are helpful for this
# exercise:
#    The American flag was planted in 1776.
#    The bottom section of the monument was built in 1854.
#    The top section of the monument was built in 1884.
#    The reflecting pool was added in 1923.

# sky and grass
Rect(0, 0, 400, 350,
     fill=gradient('lightSkyBlue', 'lightSkyBlue', 'lightCyan', start='top'))
Rect(0, 350, 400, 150, fill='forestGreen')

def drawMonument(year):
    # Draw the flag, sections of the monument, and Reflecting Pool based
    # on the year.
    # Label for the year
    Label(year, 10, 10, size=50, align='left-top')

    # American Flag
    if (year >= 1776):
        Rect(270, 300, 30, 20, fill='red')
        Line(285, 302, 285, 320, fill='white', lineWidth=30, dashes=(1, 2))
        Rect(270, 300, 15, 10, fill='blue')
        Line(270, 300, 270, 350)

    # bottom section of monument
    if (year >= 1854):
        Polygon(170, 350, 175, 275, 225, 275, 230, 350, fill='cornSilk')

    # top section of monument
    if (year >= 1884):
        Polygon(175, 275, 185, 70, 200, 40, 215, 70, 225, 275,
                fill='blanchedAlmond')

    # Reflecting Pool
    if (year >= 1923):
        Polygon(150, 350, 120, 400, 280, 400, 250, 350, border='grey',
                fill=gradient('paleTurquoise', 'deepSkyBlue', start='top'))

drawMonument(2000)

