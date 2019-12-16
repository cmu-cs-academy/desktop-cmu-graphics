app.background = 'black'

# background stars
Star(320, 50, 2, 5, fill='white')
Star(230, 115, 3, 5, fill='white')
Star(380, 315, 2, 5, fill='white')
Star(150, 190, 2, 5, fill='white')
Star(285, 290, 3, 5, fill='white')
Star(50, 325, 2, 5, fill='white')
Star(210, 375, 2, 5, fill='white')
Star(10, 25, 2, 5, fill='white')

# moon
Circle(50, 100, 30, fill=gradient('black', 'grey', start='left'))
Circle(40, 80, 3, fill=rgb(50, 50, 50))
Circle(65, 85, 4, fill=rgb(85, 85, 85))
Circle(70, 110, 3, fill=rgb(85, 85, 85))
Circle(40, 115, 4, fill=rgb(45, 45, 45))
Circle(45, 95, 4, fill=rgb(55, 55, 55))
Circle(60, 100, 4, fill=rgb(75, 75, 75))
Circle(30, 95, 3, fill=rgb(15, 15, 15))

# trails
trail1 = Line(0, 0, 0, 0, fill='blue', lineWidth=5)
trail2 = Line(0, 0, 0, 0, fill='lime', lineWidth=5)
trail3 = Line(0, 0, 0, 0, fill='red', lineWidth=5)

# fighters
fighter1 = Circle(-10, -10, 5, fill=gradient('lightGrey', 'grey'))
fighter2 = Circle(-10, -10, 5, fill=gradient('lightGrey', 'grey'))
fighter3 = Circle(-10, -10, 5, fill=gradient('darkGrey', 'grey'))

def moveFighter(fighter, newX, newY):
    fighter.centerX = newX
    fighter.centerY = newY

def moveTrail(fighter, trail):
    trail.x1 = trail.x2
    trail.y1 = trail.y2

    trail.x2 = fighter.centerX
    trail.y2 = fighter.centerY

def onMouseMove(mouseX, mouseY):
    # Move each fighter to the end of the previous fighter's trail.
    ### (HINT: The first fighter follows the mouse!)
    ### (HINT: Use the 1st trail's x1 and y1 to move the 2nd trail.)
    ### (HINT: Use the 2nd trail's x1 and y1 to move the 3rd trail.)
    moveFighter(fighter1, mouseX, mouseY)
    moveFighter(fighter2, trail1.x1, trail1.y1)
    moveFighter(fighter3, trail2.x1, trail2.y1)

    # Move each trail to follow the fighter.
    moveTrail(fighter1, trail1)
    moveTrail(fighter2, trail2)
    moveTrail(fighter3, trail3)

# This test case is intentionally left blank.

