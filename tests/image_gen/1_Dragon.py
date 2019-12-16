Rect(0, 0, 400, 400, fill='lightSkyBlue')

# back ceiling shadows
Polygon(0, 130, 25, 255, 40, 175, 55, 200, 70, 140, 95, 215, 125, 105, 145, 140,
        170, 50, 200, 155, 220, 50, 240, 55, 250, 50, 285, 180, 305, 90,
        320, 105, 350, 60, 400, 200, 400, 0, 0, 0, opacity=20)

# ceiling
Polygon(70, 0, 50, 160, 10, 0,
        fill=gradient('darkGrey', 'lightBlue', 'silver', start='left'))
Polygon(-10, 0, 25, 240, 45, 0,
        fill=gradient('darkGrey', 'lightBlue', 'silver', start='left'))
Polygon(55, 0, 90, 180, 130, 0,
        fill=gradient('darkGrey', 'lightBlue', 'silver', start='left'))
Polygon(110, 0, 145, 110, 175, 0,
        fill=gradient('darkGrey', 'lightBlue', 'silver', start='left'))
Polygon(170, 0, 200, 140, 215, 0,
        fill=gradient('darkGrey', 'lightBlue', 'silver', start='left'))
Polygon(215, 0, 235, 45, 255, 0,
        fill=gradient('darkGrey', 'lightBlue', 'silver', start='left'))
Polygon(265, 0, 320, 85, 366, 0,
        fill=gradient('darkGrey', 'lightBlue', 'silver', start='left'))
Polygon(250, 0, 285, 159, 312, 0,
        fill=gradient('darkGrey', 'lightBlue', 'silver', start='left'))
Polygon(340, 0, 399, 172, 440, 0,
        fill=gradient('darkGrey', 'lightBlue', 'silver', start='left'))

# ground
Rect(0, 330, 400, 70, fill=gradient('sandyBrown', 'bisque', start='top'))

# egg
Oval(170, 280, 200, 240, fill=gradient('cyan', 'deepSkyBlue', 'blue'))
Polygon(78, 235, 91, 247, 109, 229, 132, 257, 159, 230, 186, 262, 202, 241, 226,
        261, 244, 244, 270, 267, 272, 130, 69, 143, fill='lightSkyBlue')

# fire
fireYellow = Polygon(213, 150, 245, 160, 275, 170, 248, 175, 270, 192,
                     240, 195, 242, 223, 227, 203, 223, 177,
                     fill=gradient('lightYellow', 'yellow', start='left'),
                     opacity=80, visible=False)
fireOrange = Polygon(213, 150, 245, 160, 292, 158, 275, 170, 250, 167, 270, 190,
                     295, 190, 280, 200, 240, 193, 250, 215, 267, 223, 244, 220,
                     237, 205, 220, 220, 227, 180,
                     fill=gradient('white', 'orange', 'orangeRed', start='left'),
                     opacity=80, visible=False)
fireRed = Polygon(213, 150, 245, 160, 275, 150, 303, 145, 280, 155, 248, 175,
                  285, 177, 310, 190, 280, 185, 240, 182, 240, 182, 255, 200,
                  280, 200, 290, 225, 272, 210, 250, 210, 235, 195, 230, 222,
                  220, 195, 223, 177,
                  fill=gradient('darkRed', 'red', start='right'),
                  opacity=80, visible=False)

# back wing
Polygon(126, 121, 140, 111, 163, 154, 174, 154, 170, 195, 114, 178,
        fill=gradient('blue', 'midnightBlue', start='bottom'))
# stomach
Oval(185, 204, 60, 120, fill=gradient('cyan', 'violet', 'violet', start='right'),
     rotateAngle=-10)
# back body
Oval(170, 205, 50, 120, fill=gradient('darkBlue', 'blue', start='left'),
     rotateAngle=5)
# back horn
Polygon(150, 112, 140, 105, 150, 105, 168, 108, 185, 110, 185, 123,
        fill=gradient('blue', 'midnightBlue'))
# head
Circle(190, 140, 30, fill=gradient('darkBlue', 'blue', 'blue', start='left'))
mouthClosed = Oval(220, 153, 45, 35,
                   fill=gradient('blue', 'blue', 'royalBlue', start='left'),
                   rotateAngle=20)

# eye
Polygon(190, 128, 202, 128, 208, 140, 196, 138, fill='white')
Circle(199, 133, 5, fill=gradient('cyan', 'blue'))
Circle(201, 133, 2, fill='white')
# nose
Circle(230, 150, 3, fill=gradient('black', 'midnightBlue'))
# ear
Polygon(166, 130, 150, 128, 140, 130, 150, 142, 160, 145, 167, 143,
        fill=gradient('blue', 'cyan', start='left'), border='midnightBlue')
# wings
Polygon(160, 230, 163, 220, 170, 195, 145, 178, 125, 145, 125, 120,
        132, 107, 110, 115, 93, 130, 77, 160, 70, 190, 84, 247, 117, 265,
        155, 260, fill=gradient('blue', 'midnightBlue'), border='midnightBlue',
        borderWidth=5)
Polygon(95, 242, 83, 192, 90, 162, 105, 135, 98, 160, 103, 193, 125, 250, 117,
        265, fill=gradient('cyan', 'darkViolet', start='right'))
Polygon(133, 255, 115, 195, 108, 165, 110, 145, 115, 162, 123, 178, 137, 195,
        150, 203, 140, 255, fill=gradient('cyan', 'darkViolet', start='right'))
# horn
Polygon(185, 123, 163, 113, 152, 112, 142, 118, 132, 120, 120, 115, 120, 127,
        130, 133, 140, 130, 130, 128, 166, 130,
        fill=gradient('midnightBlue', 'blue', start='left'),
        border='midnightBlue')

# egg
Polygon(80, 235, 90, 250, 110, 230, 135, 250, 160, 230, 185, 265, 205, 240, 225,
        260, 245, 245, 270, 270, 165, 335,
        fill=gradient('cyan', 'deepSkyBlue', 'blue'))
Line(90, 250, 165, 335, fill='blue', lineWidth=1)
Line(135, 300, 120, 320, fill='blue', lineWidth=1)
Line(125, 315, 135, 320, fill='blue', lineWidth=1)
Line(120, 285, 155, 260, fill='blue', lineWidth=1)


# filter
Oval(200, 200, 1200, 600, fill=gradient('white', 'black', 'black', 'black'),
     opacity=30)

txt = Label('merp', 170, 50, size=50, font='monospace')

def onMousePress(mouseX, mouseY):
    # Makes fire visible.
    fireRed.visible = True
    fireOrange.visible = True
    fireYellow.visible = True
    txt.value = 'RAWR'

def onMouseRelease(mouseX, mouseY):
    # Makes fire invisible.
    fireYellow.visible = False
    fireOrange.visible = False
    fireRed.visible = False
    txt.value = 'merp'

# This test case is intentionally left blank.

