Label('Count to 3', 200, 20, size=20, bold=True)
Label('Click to increase the counter by 1', 200, 45)
Label('Until it gets to 3, then it ignores you!', 200, 65)

app.background = gradient('aliceBlue', 'lightCyan', 'cyan', 'blue')
counter = Label(0, 200, 200, size=200, bold=True)

def onMousePress(mouseX, mouseY):
    # Increase the counter if the value is less than 3.
    if (counter.value < 3):
       counter.value += 1



# -
Label('Count to 3', 200, 20, size=20, bold=True)
Label('Click to increase the counter by 1', 200, 45)
Label('Until it gets to 3, then it ignores you!', 200, 65)

app.background = gradient('aliceBlue', 'lightCyan', 'cyan', 'blue')
counter = Label(0, 200, 200, size=200, bold=True)

def onMousePress(mouseX, mouseY):
    # Increase the counter if the value is less than 3.
    if (counter.value < 3):
       counter.value += 1

onMousePress(100, 100)
onMousePress(100, 300)
onMousePress(100, 100)
onMousePress(100, 300)


# -
Label('Count to 3', 200, 20, size=20, bold=True)
Label('Click to increase the counter by 1', 200, 45)
Label('Until it gets to 3, then it ignores you!', 200, 65)

app.background = gradient('aliceBlue', 'lightCyan', 'cyan', 'blue')
counter = Label(0, 200, 200, size=200, bold=True)

def onMousePress(mouseX, mouseY):
    # Increase the counter if the value is less than 3.
    if (counter.value < 3):
       counter.value += 1

onMousePress(100, 100)
onMousePress(100, 300)
onMousePress(100, 100)
onMousePress(100, 300)

