# Correctness tests for containsShape for groups

g = Group(
    Rect(50, 150, 100, 100),
    Star(250, 175, 75, 5, fill='blue'),
    # test nested groups
    Group(
        Circle(175, 125, 50, fill='green'),
        Group(
            Circle(265, 275, 50, fill='yellow'),
            Arc(300, 325, 100, 100, 0, 120, fill='salmon'),
        ),
    ),
    Rect(125, 225, 100, 100, fill='orange'),
    Rect(225, 75, 50, 50, fill='purple'),
    Rect(275, 75, 50, 50, fill='pink'),
    db = "points"
)
si = Polygon(20, 300, 170, 300, 38, 375, 90, 205, 130, 370, 35, 225, fill='magenta')
g.add(si)

def checkPoint(x, y, inGroup):
    c = Circle(x, y, 10, fill='lightGreen' if inGroup else 'red')
    if inGroup:
        assert g.containsShape(c)
    else:
        assert not g.containsShape(c)


checkPoint(275, 100, True)
checkPoint(150, 200, False)
checkPoint(175, 175, False)
checkPoint(140, 160, True)
checkPoint(225, 225, False)
checkPoint(250, 175, True)
checkPoint(230, 140, False)
checkPoint(180, 200, False)
checkPoint(225, 275, True)
checkPoint(225, 305, False)
checkPoint(300, 300, True)
checkPoint(340, 300, False)
checkPoint(90, 205, True)
checkPoint(170, 300, True)

# these two should have the same behavior
checkPoint(90, 320, False)
assert not si.containsShape(Circle(90, 320, 10, fill='red'))