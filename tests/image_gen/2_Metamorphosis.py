app.background = 'skyBlue'

# Stores the current phase that the butterfly is in.
app.phase = 'caterpillar'

# tree
Rect(300, 0, 100, 400, fill=gradient('sienna', 'brown', start='left'))
Oval(-50, 420, 800, 500, fill=None,
     border=gradient('sienna', 'brown', start='top'), borderWidth=60)
Star(0, 80, 60, 6, fill=gradient('green', 'limeGreen'), roundness=50,
     rotateAngle=-20)
Line(10, 105, 50, 190, fill='sienna', lineWidth=25)

egg = RegularPolygon(290, 280, 20, 8, fill=gradient('papayaWhip', 'burlyWood'))

caterpillar = Group(
    RegularPolygon(40, 105, 15, 6, fill=gradient('darkGreen', 'green', 'yellow',
                                                 start='right-top')),
    RegularPolygon(50, 125, 15, 6, fill=gradient('darkGreen', 'green', 'yellow',
                                                 start='right-top')),
    RegularPolygon(60, 145, 15, 6, fill=gradient('darkGreen', 'green', 'yellow',
                                                 start='right-top')),
    RegularPolygon(70, 165, 15, 6, fill=gradient('darkGreen', 'green', 'yellow',
                                                 start='right-top')),
    Circle(40, 100, 2),
    Polygon(53, 98, 53, 115, 62, 117, 62, 132, 73, 138, 73, 154, 83, 157,
            fill=gradient('darkGreen', 'green', start='right-top'))
    )
caterpillar.opacity = 0

cacoon = Polygon(130, 250, 150, 275, 155, 315, 130, 335, 105, 315, 110, 275,
                 fill=gradient('limeGreen', 'darkGreen', 'black'), opacity=0)

butterfly = Group(
    Polygon(175, 85, 70, 5, 115, 115, 175, 95, 235, 115, 275, 5),
    Polygon(175, 100, 125, 125, 145, 155, 175, 100, 205, 155, 225, 125),
    Line(175, 85, 170, 71, fill='teal'),
    Line(175, 85, 180, 71, fill='teal'),

    # wing patterns
    Polygon(175, 90, 90, 30, 100, 55,
            fill=gradient('lime', 'darkGreen', start='right')),
    Polygon(175, 92, 105, 70, 120, 95,
            fill=gradient('lime', 'darkGreen', start='right')),
    Polygon(160, 115, 135, 130, 145, 140, fill=None, borderWidth=3,
            border=gradient('lime', 'darkGreen', start='left')),

    Polygon(175, 90, 260, 30, 250, 55,
            fill=gradient('lime', 'darkGreen', start='left')),
    Polygon(175, 92, 245, 70, 230, 95,
            fill=gradient('lime', 'darkGreen', start='left')),
    Polygon(190, 115, 215, 130, 205, 140, fill=None, borderWidth=3,
            border=gradient('lime', 'darkGreen', start='right')),

    # body and decoration
    Oval(175, 95, 9, 30, fill='teal'),
    Circle(145, 155, 4, fill='teal'),
    Circle(205, 155, 4, fill='teal'),
    )
butterfly.rotateAngle = 10
butterfly.opacity = 0

def onKeyHold(keys):
    # If 'space' is held, progresses the life cycle forward.
    if ('space' in keys):
        # In each phase of the butterfly's life, the opacities of the two
        # appropriate shapes (or groups) should increase or decrease by 2.
        # Decrease the egg opacity and increase the caterpillar opacity.
        if (app.phase == 'caterpillar'):
            egg.opacity -= 2
            caterpillar.opacity += 2
        # Decrease the caterpillar opacity and increase the cacoon opacity.
        if (app.phase == 'cacoon'):
            caterpillar.opacity -= 2
            cacoon.opacity += 2
        if ((app.phase == 'butterfly') and (butterfly.opacity < 100)):
            # Decrease the cacoon opacity and increase the butterfly opacity.
            cacoon.opacity -= 2
            butterfly.opacity += 2

        # Changes the phases.
        if ((caterpillar.opacity == 100) and (app.phase == 'caterpillar')):
            app.phase = 'cacoon'
        if ((cacoon.opacity == 100) and (app.phase == 'cacoon')):
            app.phase='butterfly'

onKeyHolds(['space'], 50)


# -
app.background = 'skyBlue'

# Stores the current phase that the butterfly is in.
app.phase = 'caterpillar'

# tree
Rect(300, 0, 100, 400, fill=gradient('sienna', 'brown', start='left'))
Oval(-50, 420, 800, 500, fill=None,
     border=gradient('sienna', 'brown', start='top'), borderWidth=60)
Star(0, 80, 60, 6, fill=gradient('green', 'limeGreen'), roundness=50,
     rotateAngle=-20)
Line(10, 105, 50, 190, fill='sienna', lineWidth=25)

egg = RegularPolygon(290, 280, 20, 8, fill=gradient('papayaWhip', 'burlyWood'))

caterpillar = Group(
    RegularPolygon(40, 105, 15, 6, fill=gradient('darkGreen', 'green', 'yellow',
                                                 start='right-top')),
    RegularPolygon(50, 125, 15, 6, fill=gradient('darkGreen', 'green', 'yellow',
                                                 start='right-top')),
    RegularPolygon(60, 145, 15, 6, fill=gradient('darkGreen', 'green', 'yellow',
                                                 start='right-top')),
    RegularPolygon(70, 165, 15, 6, fill=gradient('darkGreen', 'green', 'yellow',
                                                 start='right-top')),
    Circle(40, 100, 2),
    Polygon(53, 98, 53, 115, 62, 117, 62, 132, 73, 138, 73, 154, 83, 157,
            fill=gradient('darkGreen', 'green', start='right-top'))
    )
caterpillar.opacity = 0

cacoon = Polygon(130, 250, 150, 275, 155, 315, 130, 335, 105, 315, 110, 275,
                 fill=gradient('limeGreen', 'darkGreen', 'black'), opacity=0)

butterfly = Group(
    Polygon(175, 85, 70, 5, 115, 115, 175, 95, 235, 115, 275, 5),
    Polygon(175, 100, 125, 125, 145, 155, 175, 100, 205, 155, 225, 125),
    Line(175, 85, 170, 71, fill='teal'),
    Line(175, 85, 180, 71, fill='teal'),

    # wing patterns
    Polygon(175, 90, 90, 30, 100, 55,
            fill=gradient('lime', 'darkGreen', start='right')),
    Polygon(175, 92, 105, 70, 120, 95,
            fill=gradient('lime', 'darkGreen', start='right')),
    Polygon(160, 115, 135, 130, 145, 140, fill=None, borderWidth=3,
            border=gradient('lime', 'darkGreen', start='left')),

    Polygon(175, 90, 260, 30, 250, 55,
            fill=gradient('lime', 'darkGreen', start='left')),
    Polygon(175, 92, 245, 70, 230, 95,
            fill=gradient('lime', 'darkGreen', start='left')),
    Polygon(190, 115, 215, 130, 205, 140, fill=None, borderWidth=3,
            border=gradient('lime', 'darkGreen', start='right')),

    # body and decoration
    Oval(175, 95, 9, 30, fill='teal'),
    Circle(145, 155, 4, fill='teal'),
    Circle(205, 155, 4, fill='teal'),
    )
butterfly.rotateAngle = 10
butterfly.opacity = 0

def onKeyHold(keys):
    # If 'space' is held, progresses the life cycle forward.
    if ('space' in keys):
        # In each phase of the butterfly's life, the opacities of the two
        # appropriate shapes (or groups) should increase or decrease by 2.
        # Decrease the egg opacity and increase the caterpillar opacity.
        if (app.phase == 'caterpillar'):
            egg.opacity -= 2
            caterpillar.opacity += 2
        # Decrease the caterpillar opacity and increase the cacoon opacity.
        if (app.phase == 'cacoon'):
            caterpillar.opacity -= 2
            cacoon.opacity += 2
        if ((app.phase == 'butterfly') and (butterfly.opacity < 100)):
            # Decrease the cacoon opacity and increase the butterfly opacity.
            cacoon.opacity -= 2
            butterfly.opacity += 2

        # Changes the phases.
        if ((caterpillar.opacity == 100) and (app.phase == 'caterpillar')):
            app.phase = 'cacoon'
        if ((cacoon.opacity == 100) and (app.phase == 'cacoon')):
            app.phase='butterfly'

onKeyHold(['space'])


# -
app.background = 'skyBlue'

# Stores the current phase that the butterfly is in.
app.phase = 'caterpillar'

# tree
Rect(300, 0, 100, 400, fill=gradient('sienna', 'brown', start='left'))
Oval(-50, 420, 800, 500, fill=None,
     border=gradient('sienna', 'brown', start='top'), borderWidth=60)
Star(0, 80, 60, 6, fill=gradient('green', 'limeGreen'), roundness=50,
     rotateAngle=-20)
Line(10, 105, 50, 190, fill='sienna', lineWidth=25)

egg = RegularPolygon(290, 280, 20, 8, fill=gradient('papayaWhip', 'burlyWood'))

caterpillar = Group(
    RegularPolygon(40, 105, 15, 6, fill=gradient('darkGreen', 'green', 'yellow',
                                                 start='right-top')),
    RegularPolygon(50, 125, 15, 6, fill=gradient('darkGreen', 'green', 'yellow',
                                                 start='right-top')),
    RegularPolygon(60, 145, 15, 6, fill=gradient('darkGreen', 'green', 'yellow',
                                                 start='right-top')),
    RegularPolygon(70, 165, 15, 6, fill=gradient('darkGreen', 'green', 'yellow',
                                                 start='right-top')),
    Circle(40, 100, 2),
    Polygon(53, 98, 53, 115, 62, 117, 62, 132, 73, 138, 73, 154, 83, 157,
            fill=gradient('darkGreen', 'green', start='right-top'))
    )
caterpillar.opacity = 0

cacoon = Polygon(130, 250, 150, 275, 155, 315, 130, 335, 105, 315, 110, 275,
                 fill=gradient('limeGreen', 'darkGreen', 'black'), opacity=0)

butterfly = Group(
    Polygon(175, 85, 70, 5, 115, 115, 175, 95, 235, 115, 275, 5),
    Polygon(175, 100, 125, 125, 145, 155, 175, 100, 205, 155, 225, 125),
    Line(175, 85, 170, 71, fill='teal'),
    Line(175, 85, 180, 71, fill='teal'),

    # wing patterns
    Polygon(175, 90, 90, 30, 100, 55,
            fill=gradient('lime', 'darkGreen', start='right')),
    Polygon(175, 92, 105, 70, 120, 95,
            fill=gradient('lime', 'darkGreen', start='right')),
    Polygon(160, 115, 135, 130, 145, 140, fill=None, borderWidth=3,
            border=gradient('lime', 'darkGreen', start='left')),

    Polygon(175, 90, 260, 30, 250, 55,
            fill=gradient('lime', 'darkGreen', start='left')),
    Polygon(175, 92, 245, 70, 230, 95,
            fill=gradient('lime', 'darkGreen', start='left')),
    Polygon(190, 115, 215, 130, 205, 140, fill=None, borderWidth=3,
            border=gradient('lime', 'darkGreen', start='right')),

    # body and decoration
    Oval(175, 95, 9, 30, fill='teal'),
    Circle(145, 155, 4, fill='teal'),
    Circle(205, 155, 4, fill='teal'),
    )
butterfly.rotateAngle = 10
butterfly.opacity = 0

def onKeyHold(keys):
    # If 'space' is held, progresses the life cycle forward.
    if ('space' in keys):
        # In each phase of the butterfly's life, the opacities of the two
        # appropriate shapes (or groups) should increase or decrease by 2.
        # Decrease the egg opacity and increase the caterpillar opacity.
        if (app.phase == 'caterpillar'):
            egg.opacity -= 2
            caterpillar.opacity += 2
        # Decrease the caterpillar opacity and increase the cacoon opacity.
        if (app.phase == 'cacoon'):
            caterpillar.opacity -= 2
            cacoon.opacity += 2
        if ((app.phase == 'butterfly') and (butterfly.opacity < 100)):
            # Decrease the cacoon opacity and increase the butterfly opacity.
            cacoon.opacity -= 2
            butterfly.opacity += 2

        # Changes the phases.
        if ((caterpillar.opacity == 100) and (app.phase == 'caterpillar')):
            app.phase = 'cacoon'
        if ((cacoon.opacity == 100) and (app.phase == 'cacoon')):
            app.phase='butterfly'

onKeyHolds(['space'], 150)

