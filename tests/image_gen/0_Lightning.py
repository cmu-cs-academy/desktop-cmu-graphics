# sky and grass
Rect(0, 0, 400, 275, fill=gradient('grey', 'midnightBlue', start='top'))
Rect(0, 275, 400, 50, fill=gradient('green', 'darkGreen', start='top'))
backgroundLight = Rect(0, 0, 400, 275, fill='white', opacity=0)

# tree and lightning
tree = Polygon(85, 275, 90, 260, 80, 250, 90, 255, 85, 235, 80, 210, 90, 190,
               85, 210, 90, 225, 100, 220, 90, 230, 100, 265, 105, 275,
               fill=rgb(180, 160, 140))

lightning = Polygon(260, 0, 210, 60, 250, 60, 160, 100, 210, 100, 120, 150, 160,
                    150, 90, 190, 220, 140, 160, 140, 270, 80, 240, 80, 310, 40,
                    270, 40, 340, 0, fill='gold', border='yellow',
                    borderWidth=1, opacity=0)

# windows and control panel
Rect(0, 0, 200, 325, fill=None, border='dimGrey', borderWidth=8)
Rect(200, 0, 200, 325, fill=None, border='dimGrey', borderWidth=8)
Rect(0, 325, 400, 75, fill=gradient('silver', 'grey', start='left-top'))
Line(10, 360, 130, 360, fill='green', lineWidth=40, dashes=True)
Line(270, 360, 390, 360, fill='green', lineWidth=40, dashes=True)
Label('Do not Press!', 200, 385, fill='red', size=12, bold=True)

# button
button = Oval(200, 355, 25, 20, fill=gradient('red', 'darkRed', start='left-top'),
              border='fireBrick')
Circle(200, 355, 19, fill=None,
       border=gradient('silver', 'grey', start='left-top'), borderWidth=5)

def onMousePress(mouseX, mouseY):
    # Push the button.
    button.fill = 'darkRed'
    # Show the lightning strike and effects.
    tree.fill = 'black'
    lightning.opacity = 70
    backgroundLight.opacity = 30
def onMouseRelease(mouseX, mouseY):
    # Unpress the button.
    button.fill = gradient('red', 'darkRed', start='left-top')
    # Remove the lighning.
    backgroundLight.opacity = 0
    lightning.opacity = 0

onMousePress(200, 200)


# -
# sky and grass
Rect(0, 0, 400, 275, fill=gradient('grey', 'midnightBlue', start='top'))
Rect(0, 275, 400, 50, fill=gradient('green', 'darkGreen', start='top'))
backgroundLight = Rect(0, 0, 400, 275, fill='white', opacity=0)

# tree and lightning
tree = Polygon(85, 275, 90, 260, 80, 250, 90, 255, 85, 235, 80, 210, 90, 190,
               85, 210, 90, 225, 100, 220, 90, 230, 100, 265, 105, 275,
               fill=rgb(180, 160, 140))

lightning = Polygon(260, 0, 210, 60, 250, 60, 160, 100, 210, 100, 120, 150, 160,
                    150, 90, 190, 220, 140, 160, 140, 270, 80, 240, 80, 310, 40,
                    270, 40, 340, 0, fill='gold', border='yellow',
                    borderWidth=1, opacity=0)

# windows and control panel
Rect(0, 0, 200, 325, fill=None, border='dimGrey', borderWidth=8)
Rect(200, 0, 200, 325, fill=None, border='dimGrey', borderWidth=8)
Rect(0, 325, 400, 75, fill=gradient('silver', 'grey', start='left-top'))
Line(10, 360, 130, 360, fill='green', lineWidth=40, dashes=True)
Line(270, 360, 390, 360, fill='green', lineWidth=40, dashes=True)
Label('Do not Press!', 200, 385, fill='red', size=12, bold=True)

# button
button = Oval(200, 355, 25, 20, fill=gradient('red', 'darkRed', start='left-top'),
              border='fireBrick')
Circle(200, 355, 19, fill=None,
       border=gradient('silver', 'grey', start='left-top'), borderWidth=5)

def onMousePress(mouseX, mouseY):
    # Push the button.
    button.fill = 'darkRed'
    # Show the lightning strike and effects.
    tree.fill = 'black'
    lightning.opacity = 70
    backgroundLight.opacity = 30
def onMouseRelease(mouseX, mouseY):
    # Unpress the button.
    button.fill = gradient('red', 'darkRed', start='left-top')
    # Remove the lighning.
    backgroundLight.opacity = 0
    lightning.opacity = 0



# -
# sky and grass
Rect(0, 0, 400, 275, fill=gradient('grey', 'midnightBlue', start='top'))
Rect(0, 275, 400, 50, fill=gradient('green', 'darkGreen', start='top'))
backgroundLight = Rect(0, 0, 400, 275, fill='white', opacity=0)

# tree and lightning
tree = Polygon(85, 275, 90, 260, 80, 250, 90, 255, 85, 235, 80, 210, 90, 190,
               85, 210, 90, 225, 100, 220, 90, 230, 100, 265, 105, 275,
               fill=rgb(180, 160, 140))

lightning = Polygon(260, 0, 210, 60, 250, 60, 160, 100, 210, 100, 120, 150, 160,
                    150, 90, 190, 220, 140, 160, 140, 270, 80, 240, 80, 310, 40,
                    270, 40, 340, 0, fill='gold', border='yellow',
                    borderWidth=1, opacity=0)

# windows and control panel
Rect(0, 0, 200, 325, fill=None, border='dimGrey', borderWidth=8)
Rect(200, 0, 200, 325, fill=None, border='dimGrey', borderWidth=8)
Rect(0, 325, 400, 75, fill=gradient('silver', 'grey', start='left-top'))
Line(10, 360, 130, 360, fill='green', lineWidth=40, dashes=True)
Line(270, 360, 390, 360, fill='green', lineWidth=40, dashes=True)
Label('Do not Press!', 200, 385, fill='red', size=12, bold=True)

# button
button = Oval(200, 355, 25, 20, fill=gradient('red', 'darkRed', start='left-top'),
              border='fireBrick')
Circle(200, 355, 19, fill=None,
       border=gradient('silver', 'grey', start='left-top'), borderWidth=5)

def onMousePress(mouseX, mouseY):
    # Push the button.
    button.fill = 'darkRed'
    # Show the lightning strike and effects.
    tree.fill = 'black'
    lightning.opacity = 70
    backgroundLight.opacity = 30
def onMouseRelease(mouseX, mouseY):
    # Unpress the button.
    button.fill = gradient('red', 'darkRed', start='left-top')
    # Remove the lighning.
    backgroundLight.opacity = 0
    lightning.opacity = 0

onMousePress(200, 200)
onMouseRelease(200, 200)
onMousePress(200, 200)
onMouseRelease(200, 200)
onMousePress(200, 200)
onMouseRelease(200, 200)
onMousePress(200, 200)
onMouseRelease(200, 200)

