# sky
Rect(0, 0, 400, 325, fill=gradient('powderBlue', 'honeydew', start='top'))

# background grass
Line(220, 325, 210, 290, fill='forestGreen')
Line(222, 325, 220, 287, fill='green')
Line(227, 325, 235, 291, fill='green')
Line(225, 325, 227, 295, fill='forestGreen')
Oval(223, 326, 12, 8, fill=rgb(60, 117, 54))

# bee
Oval(242.5, 75, 5, 10, fill=rgb(224, 255, 255), rotateAngle=30)
Oval(244.5, 80, 5, 10, fill=rgb(224, 255, 255), rotateAngle=90)
Circle(232, 74, 4)
Oval(236, 80, 10, 15, rotateAngle=-30)
Oval(238, 83, 9, 2, fill='gold', rotateAngle=-30)
Oval(236, 80, 11, 2, fill='gold', rotateAngle=-30)
Oval(234, 77, 9, 2, fill='gold', rotateAngle=-30)
Polygon(241, 85, 239, 87, 243, 89)

wormDown = Line(25, 322, 75, 322, fill='mediumVioletRed', lineWidth=6)
wormUp = Star(55, 333, 20, 6, fill=None, border='mediumVioletRed',
              borderWidth=6, roundness=80, visible=False)
# flower
Line(275, 325, 275, 165, fill=rgb(112, 166, 74), lineWidth=6)
Star(275, 165, 50, 12, fill=gradient('paleVioletRed', rgb(242, 191, 255)),
     roundness=50)
Star(275, 165, 50, 12, fill=gradient(rgb(209, 157, 193), rgb(242, 191, 255)),
     roundness=50, rotateAngle=15)
Circle(275, 165, 25, fill='sienna')
Oval(290, 250, 20, 40, fill=rgb(112, 166, 74), rotateAngle=45)
Oval(260, 230, 20, 40, fill=rgb(112, 166, 74), rotateAngle=-45)

# grass
Rect(0, 325, 400, 75, fill=rgb(60, 117, 54))
Line(100, 325, 92, 285, fill='green')
Line(102, 325, 100, 290, fill='forestGreen')
Line(105, 325, 106, 295, fill='green')
Line(107, 325, 115, 287, fill='forestGreen')
Oval(103, 325, 12, 6, fill=rgb(60, 117, 54))

def onMousePress(mouseX, mouseY):
    # Switch between wormDown and wormUp by hiding wormDown and showing wormUp.
    wormDown.visible = False
    wormUp.visible = True
def onMouseRelease(mouseX, mouseY):
    # Switch between wormDown and wormUp by showing wormDown and hiding wormUp.
    wormDown.visible = True
    wormUp.visible = False
    # Move the worm to the right.
    wormDown.centerX += 15
    wormUp.centerX += 15

onMousePress(200, 200)
onMouseRelease(200, 200)
onMousePress(200, 200)


# -
# sky
Rect(0, 0, 400, 325, fill=gradient('powderBlue', 'honeydew', start='top'))

# background grass
Line(220, 325, 210, 290, fill='forestGreen')
Line(222, 325, 220, 287, fill='green')
Line(227, 325, 235, 291, fill='green')
Line(225, 325, 227, 295, fill='forestGreen')
Oval(223, 326, 12, 8, fill=rgb(60, 117, 54))

# bee
Oval(242.5, 75, 5, 10, fill=rgb(224, 255, 255), rotateAngle=30)
Oval(244.5, 80, 5, 10, fill=rgb(224, 255, 255), rotateAngle=90)
Circle(232, 74, 4)
Oval(236, 80, 10, 15, rotateAngle=-30)
Oval(238, 83, 9, 2, fill='gold', rotateAngle=-30)
Oval(236, 80, 11, 2, fill='gold', rotateAngle=-30)
Oval(234, 77, 9, 2, fill='gold', rotateAngle=-30)
Polygon(241, 85, 239, 87, 243, 89)

wormDown = Line(25, 322, 75, 322, fill='mediumVioletRed', lineWidth=6)
wormUp = Star(55, 333, 20, 6, fill=None, border='mediumVioletRed',
              borderWidth=6, roundness=80, visible=False)
# flower
Line(275, 325, 275, 165, fill=rgb(112, 166, 74), lineWidth=6)
Star(275, 165, 50, 12, fill=gradient('paleVioletRed', rgb(242, 191, 255)),
     roundness=50)
Star(275, 165, 50, 12, fill=gradient(rgb(209, 157, 193), rgb(242, 191, 255)),
     roundness=50, rotateAngle=15)
Circle(275, 165, 25, fill='sienna')
Oval(290, 250, 20, 40, fill=rgb(112, 166, 74), rotateAngle=45)
Oval(260, 230, 20, 40, fill=rgb(112, 166, 74), rotateAngle=-45)

# grass
Rect(0, 325, 400, 75, fill=rgb(60, 117, 54))
Line(100, 325, 92, 285, fill='green')
Line(102, 325, 100, 290, fill='forestGreen')
Line(105, 325, 106, 295, fill='green')
Line(107, 325, 115, 287, fill='forestGreen')
Oval(103, 325, 12, 6, fill=rgb(60, 117, 54))

def onMousePress(mouseX, mouseY):
    # Switch between wormDown and wormUp by hiding wormDown and showing wormUp.
    wormDown.visible = False
    wormUp.visible = True
def onMouseRelease(mouseX, mouseY):
    # Switch between wormDown and wormUp by showing wormDown and hiding wormUp.
    wormDown.visible = True
    wormUp.visible = False
    # Move the worm to the right.
    wormDown.centerX += 15
    wormUp.centerX += 15

onMousePress(200, 200)


# -
# sky
Rect(0, 0, 400, 325, fill=gradient('powderBlue', 'honeydew', start='top'))

# background grass
Line(220, 325, 210, 290, fill='forestGreen')
Line(222, 325, 220, 287, fill='green')
Line(227, 325, 235, 291, fill='green')
Line(225, 325, 227, 295, fill='forestGreen')
Oval(223, 326, 12, 8, fill=rgb(60, 117, 54))

# bee
Oval(242.5, 75, 5, 10, fill=rgb(224, 255, 255), rotateAngle=30)
Oval(244.5, 80, 5, 10, fill=rgb(224, 255, 255), rotateAngle=90)
Circle(232, 74, 4)
Oval(236, 80, 10, 15, rotateAngle=-30)
Oval(238, 83, 9, 2, fill='gold', rotateAngle=-30)
Oval(236, 80, 11, 2, fill='gold', rotateAngle=-30)
Oval(234, 77, 9, 2, fill='gold', rotateAngle=-30)
Polygon(241, 85, 239, 87, 243, 89)

wormDown = Line(25, 322, 75, 322, fill='mediumVioletRed', lineWidth=6)
wormUp = Star(55, 333, 20, 6, fill=None, border='mediumVioletRed',
              borderWidth=6, roundness=80, visible=False)
# flower
Line(275, 325, 275, 165, fill=rgb(112, 166, 74), lineWidth=6)
Star(275, 165, 50, 12, fill=gradient('paleVioletRed', rgb(242, 191, 255)),
     roundness=50)
Star(275, 165, 50, 12, fill=gradient(rgb(209, 157, 193), rgb(242, 191, 255)),
     roundness=50, rotateAngle=15)
Circle(275, 165, 25, fill='sienna')
Oval(290, 250, 20, 40, fill=rgb(112, 166, 74), rotateAngle=45)
Oval(260, 230, 20, 40, fill=rgb(112, 166, 74), rotateAngle=-45)

# grass
Rect(0, 325, 400, 75, fill=rgb(60, 117, 54))
Line(100, 325, 92, 285, fill='green')
Line(102, 325, 100, 290, fill='forestGreen')
Line(105, 325, 106, 295, fill='green')
Line(107, 325, 115, 287, fill='forestGreen')
Oval(103, 325, 12, 6, fill=rgb(60, 117, 54))

def onMousePress(mouseX, mouseY):
    # Switch between wormDown and wormUp by hiding wormDown and showing wormUp.
    wormDown.visible = False
    wormUp.visible = True
def onMouseRelease(mouseX, mouseY):
    # Switch between wormDown and wormUp by showing wormDown and hiding wormUp.
    wormDown.visible = True
    wormUp.visible = False
    # Move the worm to the right.
    wormDown.centerX += 15
    wormUp.centerX += 15

onMousePress(200, 200)
onMouseRelease(200, 200)
onMousePress(200, 200)
onMouseRelease(200, 200)

