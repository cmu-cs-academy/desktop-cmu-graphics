Label('Purple Click Counter', 200, 20, size=20, bold=True)
Label('Click in the purple part of', 200, 45)
Label('the canvas to increase the counter!', 200, 65)

Polygon(0, 0, 0, 400, 400, 400, fill='purple')
counter = Label(0, 125, 275, fill='plum', size=100, bold=True)

def onMousePress(mouseX, mouseY):
    # The counter value should increase if the click is on the purple side of
    # the canvas.
    if (mouseX <= mouseY):
       counter.value += 1

onMousePress(100, 100)


# -
Label('Purple Click Counter', 200, 20, size=20, bold=True)
Label('Click in the purple part of', 200, 45)
Label('the canvas to increase the counter!', 200, 65)

Polygon(0, 0, 0, 400, 400, 400, fill='purple')
counter = Label(0, 125, 275, fill='plum', size=100, bold=True)

def onMousePress(mouseX, mouseY):
    # The counter value should increase if the click is on the purple side of
    # the canvas.
    if (mouseX <= mouseY):
       counter.value += 1

onMousePress(200, 200)
onMousePress(300, 300)
onMousePress(100, 300)
onMousePress(300, 100)
onMousePress(100, 100)


# -
Label('Purple Click Counter', 200, 20, size=20, bold=True)
Label('Click in the purple part of', 200, 45)
Label('the canvas to increase the counter!', 200, 65)

Polygon(0, 0, 0, 400, 400, 400, fill='purple')
counter = Label(0, 125, 275, fill='plum', size=100, bold=True)

def onMousePress(mouseX, mouseY):
    # The counter value should increase if the click is on the purple side of
    # the canvas.
    if (mouseX <= mouseY):
       counter.value += 1

onMousePress(100, 100)
onMousePress(100, 300)
onMousePress(200, 250)

