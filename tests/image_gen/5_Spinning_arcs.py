app.background = rgb(0, 0, 60)

arcs = Group()

for i in range(10):
    # Each green strip is an arc with the center covered by another arc.
    # The strips are drawn from big to small so the covering arcs only cover
    # the arcs that are bigger than them.
    arc1 = Arc(200, 200, 401 - (40 * i), 401 - (40 * i), 0, 10,
               fill=rgb(0, 25 * (i + 1), 20 * (i + 1)))
    arc2 = Arc(200, 200, 370 - (40 * i), 370 - (40 * i), 0, 10,
               fill=rgb(0, 0, 60))

    # dA is the change in the start angle, dS is the change in the sweep angle.
    arc1.dA = i + 1
    arc1.dS = 2 * (i + 1)
    arc2.dA = i + 1
    arc2.dS = 2 * (i + 1)

    arcs.add(arc1, arc2)

def moveArcs(arc):
    # If the sweepAngle will become too small or is bigger than 340, change the
    # direction that the sweep angle changes.
    if ((arc.sweepAngle + arc.dS <= 0) or (arc.sweepAngle >= 340)):
        arc.dS *= -1
    # Update the start and sweep angles of the arc.
    arc.startAngle += arc.dA
    arc.sweepAngle += arc.dS
    # When the start angle gets to 360, reset it to 0.
    if (arc.startAngle >= 360):
        arc.startAngle = 0
def onStep():
    for arc in arcs:
        moveArcs(arc)

onSteps(75)
app.paused = True


# -
app.background = rgb(0, 0, 60)

arcs = Group()

for i in range(10):
    # Each green strip is an arc with the center covered by another arc.
    # The strips are drawn from big to small so the covering arcs only cover
    # the arcs that are bigger than them.
    arc1 = Arc(200, 200, 401 - (40 * i), 401 - (40 * i), 0, 10,
               fill=rgb(0, 25 * (i + 1), 20 * (i + 1)))
    arc2 = Arc(200, 200, 370 - (40 * i), 370 - (40 * i), 0, 10,
               fill=rgb(0, 0, 60))

    # dA is the change in the start angle, dS is the change in the sweep angle.
    arc1.dA = i + 1
    arc1.dS = 2 * (i + 1)
    arc2.dA = i + 1
    arc2.dS = 2 * (i + 1)

    arcs.add(arc1, arc2)

def moveArcs(arc):
    # If the sweepAngle will become too small or is bigger than 340, change the
    # direction that the sweep angle changes.
    if ((arc.sweepAngle + arc.dS <= 0) or (arc.sweepAngle >= 340)):
        arc.dS *= -1
    # Update the start and sweep angles of the arc.
    arc.startAngle += arc.dA
    arc.sweepAngle += arc.dS
    # When the start angle gets to 360, reset it to 0.
    if (arc.startAngle >= 360):
        arc.startAngle = 0
def onStep():
    for arc in arcs:
        moveArcs(arc)

onStep()
app.paused = True


# -
app.background = rgb(0, 0, 60)

arcs = Group()

for i in range(10):
    # Each green strip is an arc with the center covered by another arc.
    # The strips are drawn from big to small so the covering arcs only cover
    # the arcs that are bigger than them.
    arc1 = Arc(200, 200, 401 - (40 * i), 401 - (40 * i), 0, 10,
               fill=rgb(0, 25 * (i + 1), 20 * (i + 1)))
    arc2 = Arc(200, 200, 370 - (40 * i), 370 - (40 * i), 0, 10,
               fill=rgb(0, 0, 60))

    # dA is the change in the start angle, dS is the change in the sweep angle.
    arc1.dA = i + 1
    arc1.dS = 2 * (i + 1)
    arc2.dA = i + 1
    arc2.dS = 2 * (i + 1)

    arcs.add(arc1, arc2)

def moveArcs(arc):
    # If the sweepAngle will become too small or is bigger than 340, change the
    # direction that the sweep angle changes.
    if ((arc.sweepAngle + arc.dS <= 0) or (arc.sweepAngle >= 340)):
        arc.dS *= -1
    # Update the start and sweep angles of the arc.
    arc.startAngle += arc.dA
    arc.sweepAngle += arc.dS
    # When the start angle gets to 360, reset it to 0.
    if (arc.startAngle >= 360):
        arc.startAngle = 0
def onStep():
    for arc in arcs:
        moveArcs(arc)

onStep()
app.paused = True

