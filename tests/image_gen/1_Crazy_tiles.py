app.stepsPerSecond = 20

blocks = Group()
blocks.rowHeight = 20
blocks.columnWidth = 20

def makeBlockRow(rowNumber):
    # A row is formed by 20 blocks.
    for columnNumber in range(20):
        # Use the rowNumber and columnNumber to find the position of the
        # next rect.
        blockX = columnNumber * blocks.columnWidth
        blockY = rowNumber * blocks.rowHeight
        blocks.add(
            Rect(blockX, blockY, blocks.columnWidth, blocks.rowHeight,
                 border='black', borderWidth=1)
            )
# Each pass of this loop creates another row (a horizontal strip) of 20 blocks.
for rowNumber in range(20):
    makeBlockRow(rowNumber)

def onStep():
    # Change each block's fill to a random rgb with a green value of 0.
    for block in blocks.children:
        block.fill = rgb(randrange(0, 256), 0, randrange(0, 256))

onSteps(12)
app.paused = True


# -
app.stepsPerSecond = 20

blocks = Group()
blocks.rowHeight = 20
blocks.columnWidth = 20

def makeBlockRow(rowNumber):
    # A row is formed by 20 blocks.
    for columnNumber in range(20):
        # Use the rowNumber and columnNumber to find the position of the
        # next rect.
        blockX = columnNumber * blocks.columnWidth
        blockY = rowNumber * blocks.rowHeight
        blocks.add(
            Rect(blockX, blockY, blocks.columnWidth, blocks.rowHeight,
                 border='black', borderWidth=1)
            )
# Each pass of this loop creates another row (a horizontal strip) of 20 blocks.
for rowNumber in range(20):
    makeBlockRow(rowNumber)

def onStep():
    # Change each block's fill to a random rgb with a green value of 0.
    for block in blocks.children:
        block.fill = rgb(randrange(0, 256), 0, randrange(0, 256))

onSteps(20)
app.paused = True


# -
app.stepsPerSecond = 20

blocks = Group()
blocks.rowHeight = 20
blocks.columnWidth = 20

def makeBlockRow(rowNumber):
    # A row is formed by 20 blocks.
    for columnNumber in range(20):
        # Use the rowNumber and columnNumber to find the position of the
        # next rect.
        blockX = columnNumber * blocks.columnWidth
        blockY = rowNumber * blocks.rowHeight
        blocks.add(
            Rect(blockX, blockY, blocks.columnWidth, blocks.rowHeight,
                 border='black', borderWidth=1)
            )
# Each pass of this loop creates another row (a horizontal strip) of 20 blocks.
for rowNumber in range(20):
    makeBlockRow(rowNumber)

def onStep():
    # Change each block's fill to a random rgb with a green value of 0.
    for block in blocks.children:
        block.fill = rgb(randrange(0, 256), 0, randrange(0, 256))


