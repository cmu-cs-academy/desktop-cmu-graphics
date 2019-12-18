# The rocketShip function below has parameters which will determine what
# is drawn, but some of them have yet to be used...
def rocketShip(planetColor, isEngineOn, isOnPlanet):
    # space
    Rect(0, 0, 400, 400)
    Star(70, 100, 3, 5, fill='lightGrey')
    Star(25, 325, 3, 5, fill='lightGrey')
    Star(375, 275, 3, 5, fill='lightGrey')
    Star(325, 50, 3, 5, fill='lightGrey')
    Star(270, 185, 3, 6, fill='lightGrey')

    # rocket body
    Polygon(199, 205, 201, 205, 200, 180, fill='gold')
    Oval(200, 275, 50, 150, fill=gradient('gainsboro', 'darkGrey', start='right'))
    Rect(185, 335, 30, 20)
    Line(185, 335, 215, 335, fill='gold')

    # window
    Circle(200, 240, 15,
           fill=gradient('powderBlue', 'lightCyan', 'powderBlue',
                         start='right-top'), border='grey', borderWidth=4)

    # supports
    Polygon(185, 270, 165, 305, 160, 355, 175, 320, 185, 310, fill='maroon')
    Polygon(215, 270, 235, 305, 240, 355, 225, 320, 215, 310, fill='maroon')
    Line(200, 336, 200, 350, fill='maroon', lineWidth=3)

    # The fire should only be shown when isEngineOn is True.
    ### (HINT: Set a property using isEngineOn to hide or show the fire.)
    Polygon(190, 335, 180, 360, 190, 355, 200, 370, 210, 355, 220, 360, 210,
            335, fill=gradient('yellow', 'orange', 'red', start='top'),
            visible=isEngineOn)
    # The planet should only be shown when isOnPlanet is True.
    # The planet should also be set by planetColor.
    Circle(200, 1000, 650, fill=planetColor, visible=isOnPlanet)

rocketShip('grey', False, False)


# -
# The rocketShip function below has parameters which will determine what
# is drawn, but some of them have yet to be used...
def rocketShip(planetColor, isEngineOn, isOnPlanet):
    # space
    Rect(0, 0, 400, 400)
    Star(70, 100, 3, 5, fill='lightGrey')
    Star(25, 325, 3, 5, fill='lightGrey')
    Star(375, 275, 3, 5, fill='lightGrey')
    Star(325, 50, 3, 5, fill='lightGrey')
    Star(270, 185, 3, 6, fill='lightGrey')

    # rocket body
    Polygon(199, 205, 201, 205, 200, 180, fill='gold')
    Oval(200, 275, 50, 150, fill=gradient('gainsboro', 'darkGrey', start='right'))
    Rect(185, 335, 30, 20)
    Line(185, 335, 215, 335, fill='gold')

    # window
    Circle(200, 240, 15,
           fill=gradient('powderBlue', 'lightCyan', 'powderBlue',
                         start='right-top'), border='grey', borderWidth=4)

    # supports
    Polygon(185, 270, 165, 305, 160, 355, 175, 320, 185, 310, fill='maroon')
    Polygon(215, 270, 235, 305, 240, 355, 225, 320, 215, 310, fill='maroon')
    Line(200, 336, 200, 350, fill='maroon', lineWidth=3)

    # The fire should only be shown when isEngineOn is True.
    ### (HINT: Set a property using isEngineOn to hide or show the fire.)
    Polygon(190, 335, 180, 360, 190, 355, 200, 370, 210, 355, 220, 360, 210,
            335, fill=gradient('yellow', 'orange', 'red', start='top'),
            visible=isEngineOn)
    # The planet should only be shown when isOnPlanet is True.
    # The planet should also be set by planetColor.
    Circle(200, 1000, 650, fill=planetColor, visible=isOnPlanet)

rocketShip('salmon', True, False)


# -
# The rocketShip function below has parameters which will determine what
# is drawn, but some of them have yet to be used...
def rocketShip(planetColor, isEngineOn, isOnPlanet):
    # space
    Rect(0, 0, 400, 400)
    Star(70, 100, 3, 5, fill='lightGrey')
    Star(25, 325, 3, 5, fill='lightGrey')
    Star(375, 275, 3, 5, fill='lightGrey')
    Star(325, 50, 3, 5, fill='lightGrey')
    Star(270, 185, 3, 6, fill='lightGrey')

    # rocket body
    Polygon(199, 205, 201, 205, 200, 180, fill='gold')
    Oval(200, 275, 50, 150, fill=gradient('gainsboro', 'darkGrey', start='right'))
    Rect(185, 335, 30, 20)
    Line(185, 335, 215, 335, fill='gold')

    # window
    Circle(200, 240, 15,
           fill=gradient('powderBlue', 'lightCyan', 'powderBlue',
                         start='right-top'), border='grey', borderWidth=4)

    # supports
    Polygon(185, 270, 165, 305, 160, 355, 175, 320, 185, 310, fill='maroon')
    Polygon(215, 270, 235, 305, 240, 355, 225, 320, 215, 310, fill='maroon')
    Line(200, 336, 200, 350, fill='maroon', lineWidth=3)

    # The fire should only be shown when isEngineOn is True.
    ### (HINT: Set a property using isEngineOn to hide or show the fire.)
    Polygon(190, 335, 180, 360, 190, 355, 200, 370, 210, 355, 220, 360, 210,
            335, fill=gradient('yellow', 'orange', 'red', start='top'),
            visible=isEngineOn)
    # The planet should only be shown when isOnPlanet is True.
    # The planet should also be set by planetColor.
    Circle(200, 1000, 650, fill=planetColor, visible=isOnPlanet)

rocketShip('salmon', True, True)

