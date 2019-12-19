app.background = gradient('red', 'blue', start='bottom')
app.stepsPerSecond = 20

Line(0, 200, 400, 200, fill='white', lineWidth=3)

# spikes
spikes = Group()
spikes.isNewSpikeStart = True
spikes.currentRandY = 0

def moveAndRemoveLines():
    # Move the spikes to the left by 10 pixels and remove any that have moved
    # completely off of the canvas.
    spikes.left -= 10
    for spikeHalf in spikes.children:
        if (spikeHalf.right <= 0):
            spikes.remove(spikeHalf)
def onStep():
    # Use spikes.isNewSpikeStart to determine if this step is drawing the left
    # or the right half of the spike.
    if (spikes.isNewSpikeStart == True):
        spikes.currentRandY = randrange(0, 400)
        spikes.add(
            Line(390, 200, 400, spikes.currentRandY, fill='white',
                 lineWidth=5)
            )
    else:
        spikes.add(
            Line(390, spikes.currentRandY, 400, 200, fill='white',
                 lineWidth=5)
            )
    # Alternates between left and right halves of the spikes.
    if (spikes.isNewSpikeStart == True):
        spikes.isNewSpikeStart = False
    else:
        spikes.isNewSpikeStart = True

    moveAndRemoveLines()


onSteps(25)
app.paused = True


# -
app.background = gradient('red', 'blue', start='bottom')
app.stepsPerSecond = 20

Line(0, 200, 400, 200, fill='white', lineWidth=3)

# spikes
spikes = Group()
spikes.isNewSpikeStart = True
spikes.currentRandY = 0

def moveAndRemoveLines():
    # Move the spikes to the left by 10 pixels and remove any that have moved
    # completely off of the canvas.
    spikes.left -= 10
    for spikeHalf in spikes.children:
        if (spikeHalf.right <= 0):
            spikes.remove(spikeHalf)
def onStep():
    # Use spikes.isNewSpikeStart to determine if this step is drawing the left
    # or the right half of the spike.
    if (spikes.isNewSpikeStart == True):
        spikes.currentRandY = randrange(0, 400)
        spikes.add(
            Line(390, 200, 400, spikes.currentRandY, fill='white',
                 lineWidth=5)
            )
    else:
        spikes.add(
            Line(390, spikes.currentRandY, 400, 200, fill='white',
                 lineWidth=5)
            )
    # Alternates between left and right halves of the spikes.
    if (spikes.isNewSpikeStart == True):
        spikes.isNewSpikeStart = False
    else:
        spikes.isNewSpikeStart = True

    moveAndRemoveLines()


onSteps(50)
app.paused = True


# -
app.background = gradient('red', 'blue', start='bottom')
app.stepsPerSecond = 20

Line(0, 200, 400, 200, fill='white', lineWidth=3)

# spikes
spikes = Group()
spikes.isNewSpikeStart = True
spikes.currentRandY = 0

def moveAndRemoveLines():
    # Move the spikes to the left by 10 pixels and remove any that have moved
    # completely off of the canvas.
    spikes.left -= 10
    for spikeHalf in spikes.children:
        if (spikeHalf.right <= 0):
            spikes.remove(spikeHalf)
def onStep():
    # Use spikes.isNewSpikeStart to determine if this step is drawing the left
    # or the right half of the spike.
    if (spikes.isNewSpikeStart == True):
        spikes.currentRandY = randrange(0, 400)
        spikes.add(
            Line(390, 200, 400, spikes.currentRandY, fill='white',
                 lineWidth=5)
            )
    else:
        spikes.add(
            Line(390, spikes.currentRandY, 400, 200, fill='white',
                 lineWidth=5)
            )
    # Alternates between left and right halves of the spikes.
    if (spikes.isNewSpikeStart == True):
        spikes.isNewSpikeStart = False
    else:
        spikes.isNewSpikeStart = True

    moveAndRemoveLines()



