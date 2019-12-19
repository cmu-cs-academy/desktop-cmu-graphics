# background
Rect(0, 0, 400, 400, fill=gradient('silver', 'black', start='left-top'))

# The nameTag function below draws a nameTag, but it does not use the
# function parameters!
def nameTag(name, color1, color2, color3):
    # Fix the nametag rope so that it uses color1 instead of red!
    Line(200, 95, 275, -15, fill=color1, lineWidth=35)
    Rect(25, 75, 350, 275, fill=gradient('red', 'orange', 'yellow', 'limeGreen',
                                         'blue', 'purple', start='bottom'))
    Line(200, 95, 145, -15, fill=color1, lineWidth=35)
    Oval(200, 95, 85, 15, fill='grey')
    # Draws the blank name-writing section.
    Rect(50, 190, 300, 120, fill='white')
    Rect(65, 175, 270, 150, fill='white')
    Circle(65, 190, 15, fill='white')
    Circle(65, 310, 15, fill='white')
    Circle(335, 190, 15, fill='white')
    Circle(335, 310, 15, fill='white')

    # Modify all of the labels to use the correct parameters.
    Label('Hello, my name is', 200, 140, fill='white', size=35, bold=True)
    Label(name, 200, 250, border='black', size=75, bold=True,
          fill=gradient(color1, color2, color3, start='top'))

nameTag('Python', 'limeGreen', 'yellow', 'orange')


# -
# background
Rect(0, 0, 400, 400, fill=gradient('silver', 'black', start='left-top'))

# The nameTag function below draws a nameTag, but it does not use the
# function parameters!
def nameTag(name, color1, color2, color3):
    # Fix the nametag rope so that it uses color1 instead of red!
    Line(200, 95, 275, -15, fill=color1, lineWidth=35)
    Rect(25, 75, 350, 275, fill=gradient('red', 'orange', 'yellow', 'limeGreen',
                                         'blue', 'purple', start='bottom'))
    Line(200, 95, 145, -15, fill=color1, lineWidth=35)
    Oval(200, 95, 85, 15, fill='grey')
    # Draws the blank name-writing section.
    Rect(50, 190, 300, 120, fill='white')
    Rect(65, 175, 270, 150, fill='white')
    Circle(65, 190, 15, fill='white')
    Circle(65, 310, 15, fill='white')
    Circle(335, 190, 15, fill='white')
    Circle(335, 310, 15, fill='white')

    # Modify all of the labels to use the correct parameters.
    Label('Hello, my name is', 200, 140, fill='white', size=35, bold=True)
    Label(name, 200, 250, border='black', size=75, bold=True,
          fill=gradient(color1, color2, color3, start='top'))

nameTag('Owl', 'tan', 'saddleBrown', 'moccasin')


# -
# background
Rect(0, 0, 400, 400, fill=gradient('silver', 'black', start='left-top'))

# The nameTag function below draws a nameTag, but it does not use the
# function parameters!
def nameTag(name, color1, color2, color3):
    # Fix the nametag rope so that it uses color1 instead of red!
    Line(200, 95, 275, -15, fill=color1, lineWidth=35)
    Rect(25, 75, 350, 275, fill=gradient('red', 'orange', 'yellow', 'limeGreen',
                                         'blue', 'purple', start='bottom'))
    Line(200, 95, 145, -15, fill=color1, lineWidth=35)
    Oval(200, 95, 85, 15, fill='grey')
    # Draws the blank name-writing section.
    Rect(50, 190, 300, 120, fill='white')
    Rect(65, 175, 270, 150, fill='white')
    Circle(65, 190, 15, fill='white')
    Circle(65, 310, 15, fill='white')
    Circle(335, 190, 15, fill='white')
    Circle(335, 310, 15, fill='white')

    # Modify all of the labels to use the correct parameters.
    Label('Hello, my name is', 200, 140, fill='white', size=35, bold=True)
    Label(name, 200, 250, border='black', size=75, bold=True,
          fill=gradient(color1, color2, color3, start='top'))

nameTag('Panda', 'mediumSeaGreen', 'limeGreen', 'white')

