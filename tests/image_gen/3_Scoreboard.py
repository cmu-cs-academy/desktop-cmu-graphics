app.background = 'cornflowerBlue'

# time section
Rect(50, 0, 300, 100)
Rect(35, 0, 330, 115, fill=None, border='white', borderWidth=5)
Rect(165, 150, 70, 30, fill='cornflowerBlue')
Label('TIME', 200, 130, fill='white', size=20)
Label('00:00', 200, 50, fill='goldenrod', size=80, font='monospace', bold=True)

# home section
Label('HOME', 100, 160, fill='white', size=60, font='monospace', bold=True)
Rect(25, 190, 150, 100)
homeLabel = Label(0, 100, 240, fill='red', size=100, font='monospace', bold=True)

# away section
Label('AWAY', 300, 160, fill='white', size=60, font='monospace', bold=True)
Rect(225, 190, 150, 100)
awayLabel = Label(0, 300, 240, fill='red', size=100, font='monospace', bold=True)

# wins
Label('WINS', 100, 320, fill='white', size=40, font='monospace', bold=True)
Rect(25, 340, 150, 40)
wins = Label(0, 100, 360, fill='red', size=50, font='monospace', bold=True)

# losses
Label('LOSSES', 300, 320, fill='white', size=40, font='monospace', bold=True)
Rect(225, 340, 150, 40)
losses = Label(0, 300, 360, fill='red', size=50, font='monospace', bold=True)

def finalScoreboard(homeScore, awayScore):
    # Display the final scores.
    homeLabel.value = homeScore
    awayLabel.value = awayScore

    # Update the number of wins and losses (ties wont be tested by the autograder),
    # and change the color of the winning score to green.
    if (homeScore > awayScore):
        wins.value += 1
        homeLabel.fill = 'green'
        awayLabel.fill = 'red'
    else:
        losses.value += 1
        awayLabel.fill = 'green'
        homeLabel.fill = 'red'


finalScoreboard(32, 26)
finalScoreboard(41, 51)


# -
app.background = 'cornflowerBlue'

# time section
Rect(50, 0, 300, 100)
Rect(35, 0, 330, 115, fill=None, border='white', borderWidth=5)
Rect(165, 150, 70, 30, fill='cornflowerBlue')
Label('TIME', 200, 130, fill='white', size=20)
Label('00:00', 200, 50, fill='goldenrod', size=80, font='monospace', bold=True)

# home section
Label('HOME', 100, 160, fill='white', size=60, font='monospace', bold=True)
Rect(25, 190, 150, 100)
homeLabel = Label(0, 100, 240, fill='red', size=100, font='monospace', bold=True)

# away section
Label('AWAY', 300, 160, fill='white', size=60, font='monospace', bold=True)
Rect(225, 190, 150, 100)
awayLabel = Label(0, 300, 240, fill='red', size=100, font='monospace', bold=True)

# wins
Label('WINS', 100, 320, fill='white', size=40, font='monospace', bold=True)
Rect(25, 340, 150, 40)
wins = Label(0, 100, 360, fill='red', size=50, font='monospace', bold=True)

# losses
Label('LOSSES', 300, 320, fill='white', size=40, font='monospace', bold=True)
Rect(225, 340, 150, 40)
losses = Label(0, 300, 360, fill='red', size=50, font='monospace', bold=True)

def finalScoreboard(homeScore, awayScore):
    # Display the final scores.
    homeLabel.value = homeScore
    awayLabel.value = awayScore

    # Update the number of wins and losses (ties wont be tested by the autograder),
    # and change the color of the winning score to green.
    if (homeScore > awayScore):
        wins.value += 1
        homeLabel.fill = 'green'
        awayLabel.fill = 'red'
    else:
        losses.value += 1
        awayLabel.fill = 'green'
        homeLabel.fill = 'red'


finalScoreboard(32, 19)
finalScoreboard(25, 24)


# -
app.background = 'cornflowerBlue'

# time section
Rect(50, 0, 300, 100)
Rect(35, 0, 330, 115, fill=None, border='white', borderWidth=5)
Rect(165, 150, 70, 30, fill='cornflowerBlue')
Label('TIME', 200, 130, fill='white', size=20)
Label('00:00', 200, 50, fill='goldenrod', size=80, font='monospace', bold=True)

# home section
Label('HOME', 100, 160, fill='white', size=60, font='monospace', bold=True)
Rect(25, 190, 150, 100)
homeLabel = Label(0, 100, 240, fill='red', size=100, font='monospace', bold=True)

# away section
Label('AWAY', 300, 160, fill='white', size=60, font='monospace', bold=True)
Rect(225, 190, 150, 100)
awayLabel = Label(0, 300, 240, fill='red', size=100, font='monospace', bold=True)

# wins
Label('WINS', 100, 320, fill='white', size=40, font='monospace', bold=True)
Rect(25, 340, 150, 40)
wins = Label(0, 100, 360, fill='red', size=50, font='monospace', bold=True)

# losses
Label('LOSSES', 300, 320, fill='white', size=40, font='monospace', bold=True)
Rect(225, 340, 150, 40)
losses = Label(0, 300, 360, fill='red', size=50, font='monospace', bold=True)

def finalScoreboard(homeScore, awayScore):
    # Display the final scores.
    homeLabel.value = homeScore
    awayLabel.value = awayScore

    # Update the number of wins and losses (ties wont be tested by the autograder),
    # and change the color of the winning score to green.
    if (homeScore > awayScore):
        wins.value += 1
        homeLabel.fill = 'green'
        awayLabel.fill = 'red'
    else:
        losses.value += 1
        awayLabel.fill = 'green'
        homeLabel.fill = 'red'


finalScoreboard(24, 27)
finalScoreboard(40, 56)

