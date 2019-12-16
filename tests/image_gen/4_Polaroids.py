app.background = 'tan'

covers = Group()

# Use nested loops to draw all of the photos. Name the loop variables
# row and col to replace the definitions below and then define x and
# y to be the top left of each photograph using row and col.
for row in range(3):
    for col in range(4):
        x = col * 100 + 10
        y = row * 125 + 10
        # Draw photo backgrounds thumbtacks.
        Rect(x, y, 80, 105, fill='white', border='black')
        Rect(x + 10, y + 10, 60, 70, fill='lightSteelBlue')
        Circle(x + 40, y, 5, fill='fireBrick')
        # Draws the photo of a flower.
        Line(x + 40, y + 45, x + 40, y + 80, fill='green', lineWidth=5)
        Star(x + 40, y + 45, 20, 10,
             fill=rgb(row * 75, col * 75, (row + col) * 50), roundness=75)
        Circle(x + 40, y + 45, 5, fill='gold')
        # Add a black cover over the photo.
        covers.add(
            Rect(x + 10, y + 10, 60, 70)
            )
covers.toFront()

def onKeyHold(keys):
    # Decreases each cover's opacity until it reaches 0.
    for cover in covers.children:
        if (cover.opacity >= 5):
            cover.opacity -= 5

onKeyHolds(['space'], 5)


# -
app.background = 'tan'

covers = Group()

# Use nested loops to draw all of the photos. Name the loop variables
# row and col to replace the definitions below and then define x and
# y to be the top left of each photograph using row and col.
for row in range(3):
    for col in range(4):
        x = col * 100 + 10
        y = row * 125 + 10
        # Draw photo backgrounds thumbtacks.
        Rect(x, y, 80, 105, fill='white', border='black')
        Rect(x + 10, y + 10, 60, 70, fill='lightSteelBlue')
        Circle(x + 40, y, 5, fill='fireBrick')
        # Draws the photo of a flower.
        Line(x + 40, y + 45, x + 40, y + 80, fill='green', lineWidth=5)
        Star(x + 40, y + 45, 20, 10,
             fill=rgb(row * 75, col * 75, (row + col) * 50), roundness=75)
        Circle(x + 40, y + 45, 5, fill='gold')
        # Add a black cover over the photo.
        covers.add(
            Rect(x + 10, y + 10, 60, 70)
            )
covers.toFront()

def onKeyHold(keys):
    # Decreases each cover's opacity until it reaches 0.
    for cover in covers.children:
        if (cover.opacity >= 5):
            cover.opacity -= 5

onKeyHold('space')


# -
app.background = 'tan'

covers = Group()

# Use nested loops to draw all of the photos. Name the loop variables
# row and col to replace the definitions below and then define x and
# y to be the top left of each photograph using row and col.
for row in range(3):
    for col in range(4):
        x = col * 100 + 10
        y = row * 125 + 10
        # Draw photo backgrounds thumbtacks.
        Rect(x, y, 80, 105, fill='white', border='black')
        Rect(x + 10, y + 10, 60, 70, fill='lightSteelBlue')
        Circle(x + 40, y, 5, fill='fireBrick')
        # Draws the photo of a flower.
        Line(x + 40, y + 45, x + 40, y + 80, fill='green', lineWidth=5)
        Star(x + 40, y + 45, 20, 10,
             fill=rgb(row * 75, col * 75, (row + col) * 50), roundness=75)
        Circle(x + 40, y + 45, 5, fill='gold')
        # Add a black cover over the photo.
        covers.add(
            Rect(x + 10, y + 10, 60, 70)
            )
covers.toFront()

def onKeyHold(keys):
    # Decreases each cover's opacity until it reaches 0.
    for cover in covers.children:
        if (cover.opacity >= 5):
            cover.opacity -= 5

onKeyHolds(['space'], 5)

