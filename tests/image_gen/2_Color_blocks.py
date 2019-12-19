app.rows = 4
app.cols = 4
app.board = makeList(app.rows, app.cols)
app.selectedRow = -1
app.selectedCol = -1

def makeBoard():
    for row in range(app.rows):
        for col in range(app.cols):
            # Gets a random blue value and the required x, y coordinates.
            blue = randrange(0, 256)
            x = 25 + col * 90
            y = 25 + row * 90

            # Create a rectangle with the correct blue value and store it in
            # the list.
            block = Rect(x, y, 70, 70, fill=rgb(0, 0, blue), borderWidth=5)
            block.blue = blue
            app.board[row][col] = block
makeBoard()

def swap(row1, col1, row2, col2):
    # Swaps the fills of the blocks at (row1, col1) and (row2, col2).
    color1 = app.board[row1][col1].blue
    color2 = app.board[row2][col2].blue
    app.board[row1][col1].blue = color2
    app.board[row2][col2].blue = color1
    app.board[row1][col1].fill = rgb(0, 0, color2)
    app.board[row2][col2].fill = rgb(0, 0, color1)

def findBlock(x, y):
    # Find which block was clicked.
    for row in range(app.rows):
        for col in range(app.cols):
            block = app.board[row][col]

            # If the block was clicked, set the selectedRow and selectedCol
            # and return the block.
            if (block.hits(x, y) == True):
                app.selectedRow = row
                app.selectedCol = col
                return block
    return None

def checkWin():
    # Checks each row to see if it is in decreasing order.
    for row in range(app.rows):
        for col in range(0, app.cols):
            if (col == 0):
                app.board[row][col].border = 'green'

            # Correct blocks are highlighted in green.
            elif (app.board[row][col].blue <= app.board[row][col - 1].blue):
                app.board[row][col].border = 'green'

            # Incorrect blocks are highlighted in red.
            else:
                app.board[row][col].border = 'red'

def onMousePress(mouseX, mouseY):
    row1 = -1
    col1 = -1

    # If a block was already clicked, stores its values.
    if (app.selectedRow != -1):
        row1 = app.selectedRow
        col1 = app.selectedCol
    block = findBlock(mouseX, mouseY)

    # Second time a block was clicked.
    if ((block != None) and (row1 != -1)):
        # Swaps the colors.
        swap(row1, col1, app.selectedRow, app.selectedCol)

        # Resets the selected row and col and update the correct blocks.
        app.selectedRow = -1
        app.selectedCol = -1
        checkWin()

onMousePress(250, 50)
onMousePress(150, 350)


# -
app.rows = 4
app.cols = 4
app.board = makeList(app.rows, app.cols)
app.selectedRow = -1
app.selectedCol = -1

def makeBoard():
    for row in range(app.rows):
        for col in range(app.cols):
            # Gets a random blue value and the required x, y coordinates.
            blue = randrange(0, 256)
            x = 25 + col * 90
            y = 25 + row * 90

            # Create a rectangle with the correct blue value and store it in
            # the list.
            block = Rect(x, y, 70, 70, fill=rgb(0, 0, blue), borderWidth=5)
            block.blue = blue
            app.board[row][col] = block
makeBoard()

def swap(row1, col1, row2, col2):
    # Swaps the fills of the blocks at (row1, col1) and (row2, col2).
    color1 = app.board[row1][col1].blue
    color2 = app.board[row2][col2].blue
    app.board[row1][col1].blue = color2
    app.board[row2][col2].blue = color1
    app.board[row1][col1].fill = rgb(0, 0, color2)
    app.board[row2][col2].fill = rgb(0, 0, color1)

def findBlock(x, y):
    # Find which block was clicked.
    for row in range(app.rows):
        for col in range(app.cols):
            block = app.board[row][col]

            # If the block was clicked, set the selectedRow and selectedCol
            # and return the block.
            if (block.hits(x, y) == True):
                app.selectedRow = row
                app.selectedCol = col
                return block
    return None

def checkWin():
    # Checks each row to see if it is in decreasing order.
    for row in range(app.rows):
        for col in range(0, app.cols):
            if (col == 0):
                app.board[row][col].border = 'green'

            # Correct blocks are highlighted in green.
            elif (app.board[row][col].blue <= app.board[row][col - 1].blue):
                app.board[row][col].border = 'green'

            # Incorrect blocks are highlighted in red.
            else:
                app.board[row][col].border = 'red'

def onMousePress(mouseX, mouseY):
    row1 = -1
    col1 = -1

    # If a block was already clicked, stores its values.
    if (app.selectedRow != -1):
        row1 = app.selectedRow
        col1 = app.selectedCol
    block = findBlock(mouseX, mouseY)

    # Second time a block was clicked.
    if ((block != None) and (row1 != -1)):
        # Swaps the colors.
        swap(row1, col1, app.selectedRow, app.selectedCol)

        # Resets the selected row and col and update the correct blocks.
        app.selectedRow = -1
        app.selectedCol = -1
        checkWin()

onMousePress(150, 150)
onMousePress(150, 150)


# -
app.rows = 4
app.cols = 4
app.board = makeList(app.rows, app.cols)
app.selectedRow = -1
app.selectedCol = -1

def makeBoard():
    for row in range(app.rows):
        for col in range(app.cols):
            # Gets a random blue value and the required x, y coordinates.
            blue = randrange(0, 256)
            x = 25 + col * 90
            y = 25 + row * 90

            # Create a rectangle with the correct blue value and store it in
            # the list.
            block = Rect(x, y, 70, 70, fill=rgb(0, 0, blue), borderWidth=5)
            block.blue = blue
            app.board[row][col] = block
makeBoard()

def swap(row1, col1, row2, col2):
    # Swaps the fills of the blocks at (row1, col1) and (row2, col2).
    color1 = app.board[row1][col1].blue
    color2 = app.board[row2][col2].blue
    app.board[row1][col1].blue = color2
    app.board[row2][col2].blue = color1
    app.board[row1][col1].fill = rgb(0, 0, color2)
    app.board[row2][col2].fill = rgb(0, 0, color1)

def findBlock(x, y):
    # Find which block was clicked.
    for row in range(app.rows):
        for col in range(app.cols):
            block = app.board[row][col]

            # If the block was clicked, set the selectedRow and selectedCol
            # and return the block.
            if (block.hits(x, y) == True):
                app.selectedRow = row
                app.selectedCol = col
                return block
    return None

def checkWin():
    # Checks each row to see if it is in decreasing order.
    for row in range(app.rows):
        for col in range(0, app.cols):
            if (col == 0):
                app.board[row][col].border = 'green'

            # Correct blocks are highlighted in green.
            elif (app.board[row][col].blue <= app.board[row][col - 1].blue):
                app.board[row][col].border = 'green'

            # Incorrect blocks are highlighted in red.
            else:
                app.board[row][col].border = 'red'

def onMousePress(mouseX, mouseY):
    row1 = -1
    col1 = -1

    # If a block was already clicked, stores its values.
    if (app.selectedRow != -1):
        row1 = app.selectedRow
        col1 = app.selectedCol
    block = findBlock(mouseX, mouseY)

    # Second time a block was clicked.
    if ((block != None) and (row1 != -1)):
        # Swaps the colors.
        swap(row1, col1, app.selectedRow, app.selectedCol)

        # Resets the selected row and col and update the correct blocks.
        app.selectedRow = -1
        app.selectedCol = -1
        checkWin()

onMousePress(150, 150)
onMousePress(150, 150)

