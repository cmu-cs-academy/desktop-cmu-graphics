app.background = 'black'
Polygon(30, 250, 370, 250, 600, 320, -200, 320, fill='lightGrey')
Rect(0, 320, 400, 80, fill='slateGray')

# back drums
Oval(110, 230, 70, 10, border='lightGrey', borderWidth=3,
     fill=gradient('darkRed', 'fireBrick', 'darkRed', start='left'))
Rect(110, 200, 70, 60,
     fill=gradient('darkRed', 'fireBrick', 'darkRed', start='left'), align='center')
Oval(110, 170, 70, 10, fill='grey', border='silver', borderWidth=3)
Oval(290, 230, 70, 10, border='lightGrey', borderWidth=3,
     fill=gradient('darkRed', 'fireBrick', 'darkRed', start='left'))
Rect(290, 200, 70, 60,
     fill=gradient('darkRed', 'fireBrick', 'darkRed', start='left'), align='center')
Oval(290, 170, 70, 10, fill='grey', border='silver', borderWidth=3)

# bass drums
Line(200, 200, 140, 300, fill=rgb(50, 50, 50), lineWidth=5)
Line(200, 200, 260, 300, fill=rgb(50, 50, 50), lineWidth=5)
outerBass = Circle(200, 240, 60, fill='grey', border='darkRed', borderWidth=10)
innerBass = Circle(200, 240, 58, fill='grey', border='silver', borderWidth=8)

# hit hats
Line(50, 300, 60, 290, fill=rgb(50, 50, 50), lineWidth=3)
Line(70, 300, 60, 290, fill=rgb(50, 50, 50), lineWidth=3)
Line(60, 290, 60, 150, fill=rgb(50, 50, 50), lineWidth=3)
leftHitHat = Oval(65, 150, 70, 30, fill=gradient('gold', 'goldenrod'),
                  border='darkGoldenrod', rotateAngle=45)

Line(330, 300, 340, 290, fill=rgb(50, 50, 50), lineWidth=3)
Line(350, 300, 340, 290, fill=rgb(50, 50, 50), lineWidth=3)
Line(340, 290, 340, 150, fill=rgb(50, 50, 50), lineWidth=3)
rightHitHat = Oval(340, 150, 70, 30, fill=gradient('gold', 'goldenrod'),
                   border='darkGoldenrod', rotateAngle=-45)

# light
Polygon(100, 0, 300, 0, 400, 330, 0, 330, fill='white', opacity=15)

def onMousePress(mouseX, mouseY):
    # Change the radii of the basses.
    innerBass.radius += 10
    outerBass.radius += 10
    # Change the angle of the hi-hats.
    leftHitHat.rotateAngle = -45
    rightHitHat.rotateAngle = 45
def onMouseRelease(mouseX, mouseY):
    # Change the radii of the basses.
    innerBass.radius -= 10
    outerBass.radius -= 10
    # Change the angle of the hi-hats.
    leftHitHat.rotateAngle = 45
    rightHitHat.rotateAngle = -45

onMousePress(200, 100)
onMouseRelease(200, 100)


# -
app.background = 'black'
Polygon(30, 250, 370, 250, 600, 320, -200, 320, fill='lightGrey')
Rect(0, 320, 400, 80, fill='slateGray')

# back drums
Oval(110, 230, 70, 10, border='lightGrey', borderWidth=3,
     fill=gradient('darkRed', 'fireBrick', 'darkRed', start='left'))
Rect(110, 200, 70, 60,
     fill=gradient('darkRed', 'fireBrick', 'darkRed', start='left'), align='center')
Oval(110, 170, 70, 10, fill='grey', border='silver', borderWidth=3)
Oval(290, 230, 70, 10, border='lightGrey', borderWidth=3,
     fill=gradient('darkRed', 'fireBrick', 'darkRed', start='left'))
Rect(290, 200, 70, 60,
     fill=gradient('darkRed', 'fireBrick', 'darkRed', start='left'), align='center')
Oval(290, 170, 70, 10, fill='grey', border='silver', borderWidth=3)

# bass drums
Line(200, 200, 140, 300, fill=rgb(50, 50, 50), lineWidth=5)
Line(200, 200, 260, 300, fill=rgb(50, 50, 50), lineWidth=5)
outerBass = Circle(200, 240, 60, fill='grey', border='darkRed', borderWidth=10)
innerBass = Circle(200, 240, 58, fill='grey', border='silver', borderWidth=8)

# hit hats
Line(50, 300, 60, 290, fill=rgb(50, 50, 50), lineWidth=3)
Line(70, 300, 60, 290, fill=rgb(50, 50, 50), lineWidth=3)
Line(60, 290, 60, 150, fill=rgb(50, 50, 50), lineWidth=3)
leftHitHat = Oval(65, 150, 70, 30, fill=gradient('gold', 'goldenrod'),
                  border='darkGoldenrod', rotateAngle=45)

Line(330, 300, 340, 290, fill=rgb(50, 50, 50), lineWidth=3)
Line(350, 300, 340, 290, fill=rgb(50, 50, 50), lineWidth=3)
Line(340, 290, 340, 150, fill=rgb(50, 50, 50), lineWidth=3)
rightHitHat = Oval(340, 150, 70, 30, fill=gradient('gold', 'goldenrod'),
                   border='darkGoldenrod', rotateAngle=-45)

# light
Polygon(100, 0, 300, 0, 400, 330, 0, 330, fill='white', opacity=15)

def onMousePress(mouseX, mouseY):
    # Change the radii of the basses.
    innerBass.radius += 10
    outerBass.radius += 10
    # Change the angle of the hi-hats.
    leftHitHat.rotateAngle = -45
    rightHitHat.rotateAngle = 45
def onMouseRelease(mouseX, mouseY):
    # Change the radii of the basses.
    innerBass.radius -= 10
    outerBass.radius -= 10
    # Change the angle of the hi-hats.
    leftHitHat.rotateAngle = 45
    rightHitHat.rotateAngle = -45



# -
app.background = 'black'
Polygon(30, 250, 370, 250, 600, 320, -200, 320, fill='lightGrey')
Rect(0, 320, 400, 80, fill='slateGray')

# back drums
Oval(110, 230, 70, 10, border='lightGrey', borderWidth=3,
     fill=gradient('darkRed', 'fireBrick', 'darkRed', start='left'))
Rect(110, 200, 70, 60,
     fill=gradient('darkRed', 'fireBrick', 'darkRed', start='left'), align='center')
Oval(110, 170, 70, 10, fill='grey', border='silver', borderWidth=3)
Oval(290, 230, 70, 10, border='lightGrey', borderWidth=3,
     fill=gradient('darkRed', 'fireBrick', 'darkRed', start='left'))
Rect(290, 200, 70, 60,
     fill=gradient('darkRed', 'fireBrick', 'darkRed', start='left'), align='center')
Oval(290, 170, 70, 10, fill='grey', border='silver', borderWidth=3)

# bass drums
Line(200, 200, 140, 300, fill=rgb(50, 50, 50), lineWidth=5)
Line(200, 200, 260, 300, fill=rgb(50, 50, 50), lineWidth=5)
outerBass = Circle(200, 240, 60, fill='grey', border='darkRed', borderWidth=10)
innerBass = Circle(200, 240, 58, fill='grey', border='silver', borderWidth=8)

# hit hats
Line(50, 300, 60, 290, fill=rgb(50, 50, 50), lineWidth=3)
Line(70, 300, 60, 290, fill=rgb(50, 50, 50), lineWidth=3)
Line(60, 290, 60, 150, fill=rgb(50, 50, 50), lineWidth=3)
leftHitHat = Oval(65, 150, 70, 30, fill=gradient('gold', 'goldenrod'),
                  border='darkGoldenrod', rotateAngle=45)

Line(330, 300, 340, 290, fill=rgb(50, 50, 50), lineWidth=3)
Line(350, 300, 340, 290, fill=rgb(50, 50, 50), lineWidth=3)
Line(340, 290, 340, 150, fill=rgb(50, 50, 50), lineWidth=3)
rightHitHat = Oval(340, 150, 70, 30, fill=gradient('gold', 'goldenrod'),
                   border='darkGoldenrod', rotateAngle=-45)

# light
Polygon(100, 0, 300, 0, 400, 330, 0, 330, fill='white', opacity=15)

def onMousePress(mouseX, mouseY):
    # Change the radii of the basses.
    innerBass.radius += 10
    outerBass.radius += 10
    # Change the angle of the hi-hats.
    leftHitHat.rotateAngle = -45
    rightHitHat.rotateAngle = 45
def onMouseRelease(mouseX, mouseY):
    # Change the radii of the basses.
    innerBass.radius -= 10
    outerBass.radius -= 10
    # Change the angle of the hi-hats.
    leftHitHat.rotateAngle = 45
    rightHitHat.rotateAngle = -45


