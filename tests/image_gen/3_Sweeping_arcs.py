app.background = 'black'

arcs = Group()

# Draw a 5x5 grid of equally-spaced arcs on the screen, and add the arcs to
# the arcs group.
for x in range(40, 400, 80):
    for y in range(40, 400, 80):
        arcs.add(
            Arc(x, y, 40, 40, 0, 180, fill=None, border='lime')
            )
def onMouseMove(mouseX, mouseY):
    # Change the sweep angle of each arc based on mouseX as long as mouseX is
    # larger than 0.
    for arc in arcs:
        if (mouseX > 0):
            newSweepAngle = (mouseX / 400) * 360
            arc.sweepAngle = newSweepAngle



# -
app.background = 'black'

arcs = Group()

# Draw a 5x5 grid of equally-spaced arcs on the screen, and add the arcs to
# the arcs group.
for x in range(40, 400, 80):
    for y in range(40, 400, 80):
        arcs.add(
            Arc(x, y, 40, 40, 0, 180, fill=None, border='lime')
            )
def onMouseMove(mouseX, mouseY):
    # Change the sweep angle of each arc based on mouseX as long as mouseX is
    # larger than 0.
    for arc in arcs:
        if (mouseX > 0):
            newSweepAngle = (mouseX / 400) * 360
            arc.sweepAngle = newSweepAngle



# -
app.background = 'black'

arcs = Group()

# Draw a 5x5 grid of equally-spaced arcs on the screen, and add the arcs to
# the arcs group.
for x in range(40, 400, 80):
    for y in range(40, 400, 80):
        arcs.add(
            Arc(x, y, 40, 40, 0, 180, fill=None, border='lime')
            )
def onMouseMove(mouseX, mouseY):
    # Change the sweep angle of each arc based on mouseX as long as mouseX is
    # larger than 0.
    for arc in arcs:
        if (mouseX > 0):
            newSweepAngle = (mouseX / 400) * 360
            arc.sweepAngle = newSweepAngle

onMouseMove(100, 100)

