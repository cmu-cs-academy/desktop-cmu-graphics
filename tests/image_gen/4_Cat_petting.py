app.background = 'powderBlue'

# armchair cushion and back
Oval(300, 150, 800, 250, fill=gradient('fireBrick', 'darkRed', start='top'))
Oval(300, 335, 1000, 275, fill=gradient('fireBrick', 'maroon', start='bottom'))
Line(40, 225, 30, 400, fill='darkRed', lineWidth=20, opacity=40)

# armchair arm
Rect(25, 155, 40, 245, fill='fireBrick', border='darkRed', align='right-top')
Circle(45, 155, 60, fill=gradient('fireBrick', 'maroon'), border='darkRed',
       align='right')

# body
Oval(150, 250, 500, 200,
     fill=gradient('sandyBrown', rgb(210, 135, 85), start='top'), align='left')

# legs
Circle(50, 250, 15, fill='white')
Rect(50, 225, 125, 30, rotateAngle=-10,
     fill=gradient('sandyBrown', rgb(215, 145, 85), start='left'))
Circle(155, 365, 15, fill='white')
Rect(150, 325, 120, 30, rotateAngle=-25,
     fill=gradient('sandyBrown', rgb(215, 145, 85), start='left'))

# ears
Oval(140, 130, 80, 50, fill='sandyBrown', rotateAngle=50)
Oval(135, 130, 50, 30, fill='salmon', rotateAngle=50)
Oval(255, 130, 80, 50, fill='sandyBrown', rotateAngle=130)
Oval(260, 130, 50, 30, fill='salmon', rotateAngle=130)

# face
Oval(200, 200, 200, 190, fill='sandyBrown')

# mouth
Oval(185, 235, 35, 30, fill=None, border='black')
Oval(215, 235, 35, 30, fill=None, border='black')

# eyes
Circle(165, 185, 30, fill='azure')
Circle(235, 185, 30, fill='azure', border='black')
Circle(170, 190, 20, fill='powderBlue')
Circle(230, 190, 20, fill='powderBlue')
Circle(172, 195, 10)
Circle(228, 195, 10)

leftEyelid = Circle(165, 185, 30, fill=None, border='sienna')
rightEyelid = Circle(235, 185, 30, fill=None, border='sienna')
eyelidCover = Rect(200, 240, 140, 25, fill='sandyBrown', align='bottom')

# nose
RegularPolygon(200, 225, 10, 3, fill='salmon')

# whiskers
Line(170, 220, 90, 200, lineWidth=1)
Line(175, 225, 85, 225, lineWidth=1)
Line(170, 230, 90, 250, lineWidth=1)
Line(230, 220, 310, 200, lineWidth=1)
Line(225, 225, 315, 225, lineWidth=1)
Line(230, 230, 310, 250, lineWidth=1)

def onMouseRelease(mouseX, mouseY):
    # Show the eyes by changing the height and bottom of the eyelidCover.
    # Then, change the eyelid's fills.
    eyelidCover.height = 25
    eyelidCover.bottom = 240
    leftEyelid.fill = None
    rightEyelid.fill = None

    # Add a heart centered at mouseX, mouseY using two ovals.
    Oval(mouseX - 3, mouseY, 20, 12, fill='red', rotateAngle=35)
    Oval(mouseX + 3, mouseY, 20, 12, fill='red', rotateAngle=-35)

def onMouseDrag(mouseX, mouseY):
    # Hide the eyes using the eyelids and reset the eyelidCover's height and
    # bottom.
    eyelidCover.height = 50
    eyelidCover.bottom = 240
    leftEyelid.fill = 'sandyBrown'
    rightEyelid.fill = 'sandyBrown'


onMouseDrag(280, 300)
onMouseDrag(370, 350)
onMouseDrag(330, 320)
onMouseDrag(50, 130)
onMouseDrag(200, 200)


# -
app.background = 'powderBlue'

# armchair cushion and back
Oval(300, 150, 800, 250, fill=gradient('fireBrick', 'darkRed', start='top'))
Oval(300, 335, 1000, 275, fill=gradient('fireBrick', 'maroon', start='bottom'))
Line(40, 225, 30, 400, fill='darkRed', lineWidth=20, opacity=40)

# armchair arm
Rect(25, 155, 40, 245, fill='fireBrick', border='darkRed', align='right-top')
Circle(45, 155, 60, fill=gradient('fireBrick', 'maroon'), border='darkRed',
       align='right')

# body
Oval(150, 250, 500, 200,
     fill=gradient('sandyBrown', rgb(210, 135, 85), start='top'), align='left')

# legs
Circle(50, 250, 15, fill='white')
Rect(50, 225, 125, 30, rotateAngle=-10,
     fill=gradient('sandyBrown', rgb(215, 145, 85), start='left'))
Circle(155, 365, 15, fill='white')
Rect(150, 325, 120, 30, rotateAngle=-25,
     fill=gradient('sandyBrown', rgb(215, 145, 85), start='left'))

# ears
Oval(140, 130, 80, 50, fill='sandyBrown', rotateAngle=50)
Oval(135, 130, 50, 30, fill='salmon', rotateAngle=50)
Oval(255, 130, 80, 50, fill='sandyBrown', rotateAngle=130)
Oval(260, 130, 50, 30, fill='salmon', rotateAngle=130)

# face
Oval(200, 200, 200, 190, fill='sandyBrown')

# mouth
Oval(185, 235, 35, 30, fill=None, border='black')
Oval(215, 235, 35, 30, fill=None, border='black')

# eyes
Circle(165, 185, 30, fill='azure')
Circle(235, 185, 30, fill='azure', border='black')
Circle(170, 190, 20, fill='powderBlue')
Circle(230, 190, 20, fill='powderBlue')
Circle(172, 195, 10)
Circle(228, 195, 10)

leftEyelid = Circle(165, 185, 30, fill=None, border='sienna')
rightEyelid = Circle(235, 185, 30, fill=None, border='sienna')
eyelidCover = Rect(200, 240, 140, 25, fill='sandyBrown', align='bottom')

# nose
RegularPolygon(200, 225, 10, 3, fill='salmon')

# whiskers
Line(170, 220, 90, 200, lineWidth=1)
Line(175, 225, 85, 225, lineWidth=1)
Line(170, 230, 90, 250, lineWidth=1)
Line(230, 220, 310, 200, lineWidth=1)
Line(225, 225, 315, 225, lineWidth=1)
Line(230, 230, 310, 250, lineWidth=1)

def onMouseRelease(mouseX, mouseY):
    # Show the eyes by changing the height and bottom of the eyelidCover.
    # Then, change the eyelid's fills.
    eyelidCover.height = 25
    eyelidCover.bottom = 240
    leftEyelid.fill = None
    rightEyelid.fill = None

    # Add a heart centered at mouseX, mouseY using two ovals.
    Oval(mouseX - 3, mouseY, 20, 12, fill='red', rotateAngle=35)
    Oval(mouseX + 3, mouseY, 20, 12, fill='red', rotateAngle=-35)

def onMouseDrag(mouseX, mouseY):
    # Hide the eyes using the eyelids and reset the eyelidCover's height and
    # bottom.
    eyelidCover.height = 50
    eyelidCover.bottom = 240
    leftEyelid.fill = 'sandyBrown'
    rightEyelid.fill = 'sandyBrown'


onMouseDrag(50, 150)


# -
app.background = 'powderBlue'

# armchair cushion and back
Oval(300, 150, 800, 250, fill=gradient('fireBrick', 'darkRed', start='top'))
Oval(300, 335, 1000, 275, fill=gradient('fireBrick', 'maroon', start='bottom'))
Line(40, 225, 30, 400, fill='darkRed', lineWidth=20, opacity=40)

# armchair arm
Rect(25, 155, 40, 245, fill='fireBrick', border='darkRed', align='right-top')
Circle(45, 155, 60, fill=gradient('fireBrick', 'maroon'), border='darkRed',
       align='right')

# body
Oval(150, 250, 500, 200,
     fill=gradient('sandyBrown', rgb(210, 135, 85), start='top'), align='left')

# legs
Circle(50, 250, 15, fill='white')
Rect(50, 225, 125, 30, rotateAngle=-10,
     fill=gradient('sandyBrown', rgb(215, 145, 85), start='left'))
Circle(155, 365, 15, fill='white')
Rect(150, 325, 120, 30, rotateAngle=-25,
     fill=gradient('sandyBrown', rgb(215, 145, 85), start='left'))

# ears
Oval(140, 130, 80, 50, fill='sandyBrown', rotateAngle=50)
Oval(135, 130, 50, 30, fill='salmon', rotateAngle=50)
Oval(255, 130, 80, 50, fill='sandyBrown', rotateAngle=130)
Oval(260, 130, 50, 30, fill='salmon', rotateAngle=130)

# face
Oval(200, 200, 200, 190, fill='sandyBrown')

# mouth
Oval(185, 235, 35, 30, fill=None, border='black')
Oval(215, 235, 35, 30, fill=None, border='black')

# eyes
Circle(165, 185, 30, fill='azure')
Circle(235, 185, 30, fill='azure', border='black')
Circle(170, 190, 20, fill='powderBlue')
Circle(230, 190, 20, fill='powderBlue')
Circle(172, 195, 10)
Circle(228, 195, 10)

leftEyelid = Circle(165, 185, 30, fill=None, border='sienna')
rightEyelid = Circle(235, 185, 30, fill=None, border='sienna')
eyelidCover = Rect(200, 240, 140, 25, fill='sandyBrown', align='bottom')

# nose
RegularPolygon(200, 225, 10, 3, fill='salmon')

# whiskers
Line(170, 220, 90, 200, lineWidth=1)
Line(175, 225, 85, 225, lineWidth=1)
Line(170, 230, 90, 250, lineWidth=1)
Line(230, 220, 310, 200, lineWidth=1)
Line(225, 225, 315, 225, lineWidth=1)
Line(230, 230, 310, 250, lineWidth=1)

def onMouseRelease(mouseX, mouseY):
    # Show the eyes by changing the height and bottom of the eyelidCover.
    # Then, change the eyelid's fills.
    eyelidCover.height = 25
    eyelidCover.bottom = 240
    leftEyelid.fill = None
    rightEyelid.fill = None

    # Add a heart centered at mouseX, mouseY using two ovals.
    Oval(mouseX - 3, mouseY, 20, 12, fill='red', rotateAngle=35)
    Oval(mouseX + 3, mouseY, 20, 12, fill='red', rotateAngle=-35)

def onMouseDrag(mouseX, mouseY):
    # Hide the eyes using the eyelids and reset the eyelidCover's height and
    # bottom.
    eyelidCover.height = 50
    eyelidCover.bottom = 240
    leftEyelid.fill = 'sandyBrown'
    rightEyelid.fill = 'sandyBrown'


onMouseRelease(200, 200)

