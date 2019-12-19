# The scoreboard function below draws the scoreboard but currently ignores
# the parameters that would draw the time remaining and the score.
def scoreboard(timeLeft, homeScore, awayScore):
    Rect(0, 0, 400, 400, fill='cornflowerBlue')

    # time section
    Rect(50, 0, 300, 150)
    Rect(35, 0, 330, 165, fill=None, border='white', borderWidth=5)
    Rect(165, 150, 70, 30, fill='cornflowerBlue')
    Label('TIME', 200, 165, fill='white', size=20)
    Label(timeLeft, 200, 75, fill='goldenrod', size=80, font='monospace',
          bold=True)

    # home section
    Label('HOME', 100, 220, fill='white', size=60, font='monospace', bold=True)
    Rect(25, 250, 150, 100)
    Label(homeScore, 100, 300, fill='red', size=100, font='monospace', bold=True)

    # away section
    Label('AWAY', 300, 220, fill='white', size=60, font='monospace', bold=True)
    Rect(225, 250, 150, 100)
    Label(awayScore, 300, 300, fill='red', size=100, font='monospace', bold=True)


scoreboard('01:02', 50, 48)


# -
# The scoreboard function below draws the scoreboard but currently ignores
# the parameters that would draw the time remaining and the score.
def scoreboard(timeLeft, homeScore, awayScore):
    Rect(0, 0, 400, 400, fill='cornflowerBlue')

    # time section
    Rect(50, 0, 300, 150)
    Rect(35, 0, 330, 165, fill=None, border='white', borderWidth=5)
    Rect(165, 150, 70, 30, fill='cornflowerBlue')
    Label('TIME', 200, 165, fill='white', size=20)
    Label(timeLeft, 200, 75, fill='goldenrod', size=80, font='monospace',
          bold=True)

    # home section
    Label('HOME', 100, 220, fill='white', size=60, font='monospace', bold=True)
    Rect(25, 250, 150, 100)
    Label(homeScore, 100, 300, fill='red', size=100, font='monospace', bold=True)

    # away section
    Label('AWAY', 300, 220, fill='white', size=60, font='monospace', bold=True)
    Rect(225, 250, 150, 100)
    Label(awayScore, 300, 300, fill='red', size=100, font='monospace', bold=True)


scoreboard('10:53', 13, 24)


# -
# The scoreboard function below draws the scoreboard but currently ignores
# the parameters that would draw the time remaining and the score.
def scoreboard(timeLeft, homeScore, awayScore):
    Rect(0, 0, 400, 400, fill='cornflowerBlue')

    # time section
    Rect(50, 0, 300, 150)
    Rect(35, 0, 330, 165, fill=None, border='white', borderWidth=5)
    Rect(165, 150, 70, 30, fill='cornflowerBlue')
    Label('TIME', 200, 165, fill='white', size=20)
    Label(timeLeft, 200, 75, fill='goldenrod', size=80, font='monospace',
          bold=True)

    # home section
    Label('HOME', 100, 220, fill='white', size=60, font='monospace', bold=True)
    Rect(25, 250, 150, 100)
    Label(homeScore, 100, 300, fill='red', size=100, font='monospace', bold=True)

    # away section
    Label('AWAY', 300, 220, fill='white', size=60, font='monospace', bold=True)
    Rect(225, 250, 150, 100)
    Label(awayScore, 300, 300, fill='red', size=100, font='monospace', bold=True)


scoreboard('01:02', 50, 48)

