app.background = gradient('skyBlue', 'lightBlue', 'skyBlue', start='top')

# fallen snow
Oval(60, 360, 300, 200, fill=gradient('white', 'snow', 'white'))
Oval(180, 400, 300, 200, fill=gradient('white', 'snow', 'white'))
Oval(350, 380, 300, 200, fill=gradient('white', 'snow', 'white'))

# snowman arms
Line(100, 220, 120, 210, fill='saddleBrown')
Line(60, 220, 40, 210, fill='saddleBrown')
Line(114, 212, 116, 205, fill='saddleBrown')
Line(47, 212, 50, 205, fill='saddleBrown')

# head and body
Circle(80, 195, 20, fill=gradient('white', 'snow', 'white'))
Circle(80, 220, 25, fill=gradient('white', 'snow', 'white'))
Circle(80, 245, 30, fill=gradient('white', 'snow', 'white'))

# buttons
Circle(80, 220, 5)
Circle(80, 245, 5)

# face
RegularPolygon(80, 200, 5, 3, fill='orange')
Circle(75, 190, 3)
Circle(85, 190, 3)
Rect(80, 185, 20, 30, fill=gradient('black', 'gray', start='top'),
     align='bottom')
Rect(80, 185, 30, 10, align='bottom')
RegularPolygon(94, 173, 6, 3, fill='green')
Circle(89, 177, 3, fill='red')

def onMousePress(mouseX, mouseY):
    # Define the random variables to be used to create a new snowflake.
    radius = randrange(6, 13)
    points = randrange(8, 21)
    roundness = randrange(0, 81)
    opacity = randrange(60, 101)
    # Use the variables to create a new snowflake.
    Star(mouseX, mouseY, radius, points, fill=gradient('white', 'snow', 'white'),
         roundness=roundness, opacity=opacity)

onMousePress(200, 100)


# -
app.background = gradient('skyBlue', 'lightBlue', 'skyBlue', start='top')

# fallen snow
Oval(60, 360, 300, 200, fill=gradient('white', 'snow', 'white'))
Oval(180, 400, 300, 200, fill=gradient('white', 'snow', 'white'))
Oval(350, 380, 300, 200, fill=gradient('white', 'snow', 'white'))

# snowman arms
Line(100, 220, 120, 210, fill='saddleBrown')
Line(60, 220, 40, 210, fill='saddleBrown')
Line(114, 212, 116, 205, fill='saddleBrown')
Line(47, 212, 50, 205, fill='saddleBrown')

# head and body
Circle(80, 195, 20, fill=gradient('white', 'snow', 'white'))
Circle(80, 220, 25, fill=gradient('white', 'snow', 'white'))
Circle(80, 245, 30, fill=gradient('white', 'snow', 'white'))

# buttons
Circle(80, 220, 5)
Circle(80, 245, 5)

# face
RegularPolygon(80, 200, 5, 3, fill='orange')
Circle(75, 190, 3)
Circle(85, 190, 3)
Rect(80, 185, 20, 30, fill=gradient('black', 'gray', start='top'),
     align='bottom')
Rect(80, 185, 30, 10, align='bottom')
RegularPolygon(94, 173, 6, 3, fill='green')
Circle(89, 177, 3, fill='red')

def onMousePress(mouseX, mouseY):
    # Define the random variables to be used to create a new snowflake.
    radius = randrange(6, 13)
    points = randrange(8, 21)
    roundness = randrange(0, 81)
    opacity = randrange(60, 101)
    # Use the variables to create a new snowflake.
    Star(mouseX, mouseY, radius, points, fill=gradient('white', 'snow', 'white'),
         roundness=roundness, opacity=opacity)



# -
app.background = gradient('skyBlue', 'lightBlue', 'skyBlue', start='top')

# fallen snow
Oval(60, 360, 300, 200, fill=gradient('white', 'snow', 'white'))
Oval(180, 400, 300, 200, fill=gradient('white', 'snow', 'white'))
Oval(350, 380, 300, 200, fill=gradient('white', 'snow', 'white'))

# snowman arms
Line(100, 220, 120, 210, fill='saddleBrown')
Line(60, 220, 40, 210, fill='saddleBrown')
Line(114, 212, 116, 205, fill='saddleBrown')
Line(47, 212, 50, 205, fill='saddleBrown')

# head and body
Circle(80, 195, 20, fill=gradient('white', 'snow', 'white'))
Circle(80, 220, 25, fill=gradient('white', 'snow', 'white'))
Circle(80, 245, 30, fill=gradient('white', 'snow', 'white'))

# buttons
Circle(80, 220, 5)
Circle(80, 245, 5)

# face
RegularPolygon(80, 200, 5, 3, fill='orange')
Circle(75, 190, 3)
Circle(85, 190, 3)
Rect(80, 185, 20, 30, fill=gradient('black', 'gray', start='top'),
     align='bottom')
Rect(80, 185, 30, 10, align='bottom')
RegularPolygon(94, 173, 6, 3, fill='green')
Circle(89, 177, 3, fill='red')

def onMousePress(mouseX, mouseY):
    # Define the random variables to be used to create a new snowflake.
    radius = randrange(6, 13)
    points = randrange(8, 21)
    roundness = randrange(0, 81)
    opacity = randrange(60, 101)
    # Use the variables to create a new snowflake.
    Star(mouseX, mouseY, radius, points, fill=gradient('white', 'snow', 'white'),
         roundness=roundness, opacity=opacity)

onMousePress(200, 100)

