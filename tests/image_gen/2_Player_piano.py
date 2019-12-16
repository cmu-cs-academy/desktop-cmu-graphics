app.stepsPerSecond = 50

app.currentNote = 'a'
app.stepsPerNote = 10
app.stepsUntilNote = 10

# keyboard
Rect(0, 200, 400, 200,
     fill=gradient('grey', 'springGreen', 'red', 'grey', 'yellow',
                   'deepSkyBlue', 'grey', start='left'))
Line(-60, 300, 460, 300, fill='white', lineWidth=200, dashes=True)

# keyboard keys
aButton = Rect(45, 200, 50, 160, border=rgb(105, 240, 120), borderWidth=0)
sButton = Rect(110, 200, 50, 160, border=rgb(245, 70, 65), borderWidth=0)
dButton = Rect(240, 200, 50, 160, border=rgb(255, 230, 75), borderWidth=0)
fButton = Rect(305, 200, 50, 160, border=rgb(55, 165, 255), borderWidth=0)

aButton.key = 'a'
sButton.key = 's'
dButton.key = 'd'
fButton.key = 'f'

buttons = Group(aButton, sButton, dButton, fButton)
buttons.fill = rgb(40, 45, 50)

# Label the buttons.
Label('a', 70, 330, fill='white', size=25)
Label('s', 135, 330, fill='white', size=25)
Label('d', 265, 330, fill='white', size=25)
Label('f', 330, 330, fill='white', size=25)

# upper background
Oval(200, 200, 310, 160, fill='white', opacity=15)
Rect(0, 0, 400, 200, fill=gradient(rgb(35, 60, 75), rgb(40, 45, 50), start='top'))
Label('Player Piano', 200, 30, fill='white', size=20)

notes = Group()

def setCurrentNote(nextNote):
    # Pick a note given the random value nextNote.
    if (nextNote == 1):
        app.currentNote = 'a'
    elif (nextNote == 2):
        app.currentNote = 's'
    elif (nextNote == 3):
        app.currentNote = 'd'
    elif (nextNote == 4):
        app.currentNote = 'f'
    else:
        app.currentNote = 'space'

def playNote():
    # Create a note, color the button, and add it to the notes group.
    nextNote = randrange(1, 6)
    setCurrentNote(nextNote)
    onKeyPress(app.currentNote)

def onKeyPress(key):
    for button in buttons.children:
        # If button.key matches the key pressed, make a new note.
        if (button.key == key):
            button.fill = button.border
            notes.add(
                Circle(button.centerX, button.top, 30, fill=button.border)
                )
        else:
            button.fill = 'black'

def onStep():
    # Move all notes up and make them fade out.
    notes.centerY -= 5
    for note in notes.children:
        note.opacity -= 2
        if (note.opacity <= 2):
            notes.remove(note)

    # Make a new note if enough steps have passed.
    app.stepsUntilNote -= 1
    if (app.stepsUntilNote == 0):
        app.stepsUntilNote = app.stepsPerNote
        playNote()


