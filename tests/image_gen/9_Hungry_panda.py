# ears
Circle(100, 100, 40)
Circle(300, 100, 40)

# body
Circle(200, 400, 175)

# face
Circle(200, 200, 125, fill='white')

# eyes
Oval(250, 170, 60, 80, rotateAngle=-30)
Oval(150, 170, 60, 80, rotateAngle=30)
Circle(160, 160, 15, fill='white')
Circle(240, 160, 15, fill='white')
Circle(160, 160, 5)
Circle(240, 160, 5)

# nose
Oval(200, 200, 50, 30)

# mouth
mouth = Circle(200, 250, 30, fill='lightCoral')
Rect(170, 215, 70, 35, fill='white')
Line(170, 250, 230, 250, fill='lightCoral', lineWidth=5)

# bamboo eaten label
Label('Amount of Bamboo Eaten:', 150, 25, size=25)

# Define the bamboo eaten counter.
### Fix Your Code Here ###
counter = Label(0, 320, 25, size=25)
# bamboo
bamboo = Line(190, 265, 100, 410,
              fill=gradient('oliveDrab', 'darkOliveGreen', 'darkGreen'),
              lineWidth=20)

# full cheek
fullCheek = Oval(275, 250, 60, 70, fill='white', border='black', borderWidth=3,
                 visible=False)
Rect(240, 212, 40, 70, fill='white')

def onMousePress(mouseX, mouseY):
    # Change the visibility of the mouth and fullCheek and remove a bit of bamboo.
    ### Place Your Code Here ###
    mouth.visible = False
    fullCheek.visible= True
    bamboo.x1 = 170
    bamboo.y1 = 295
    # Then, add one to the bamboo count.
    ### Place Your Code Here ###
    counter.value += 1
def onMouseRelease(mouseX, mouseY):
    # Change the visibility of the mouth and fullCheek back and move the
    # bamboo to the panda's mouth.
    mouth.visible = True
    fullCheek.visible = False
    bamboo.x1 = 190
    bamboo.y1 = 265

onMousePress(200, 100)
onMouseRelease(200, 100)
onMousePress(250, 100)
onMouseRelease(250, 100)
onMousePress(200, 100)
onMouseRelease(200, 100)
onMousePress(250, 100)
onMouseRelease(250, 100)
onMousePress(250, 100)
onMouseRelease(250, 100)


# -
# ears
Circle(100, 100, 40)
Circle(300, 100, 40)

# body
Circle(200, 400, 175)

# face
Circle(200, 200, 125, fill='white')

# eyes
Oval(250, 170, 60, 80, rotateAngle=-30)
Oval(150, 170, 60, 80, rotateAngle=30)
Circle(160, 160, 15, fill='white')
Circle(240, 160, 15, fill='white')
Circle(160, 160, 5)
Circle(240, 160, 5)

# nose
Oval(200, 200, 50, 30)

# mouth
mouth = Circle(200, 250, 30, fill='lightCoral')
Rect(170, 215, 70, 35, fill='white')
Line(170, 250, 230, 250, fill='lightCoral', lineWidth=5)

# bamboo eaten label
Label('Amount of Bamboo Eaten:', 150, 25, size=25)

# Define the bamboo eaten counter.
### Fix Your Code Here ###
counter = Label(0, 320, 25, size=25)
# bamboo
bamboo = Line(190, 265, 100, 410,
              fill=gradient('oliveDrab', 'darkOliveGreen', 'darkGreen'),
              lineWidth=20)

# full cheek
fullCheek = Oval(275, 250, 60, 70, fill='white', border='black', borderWidth=3,
                 visible=False)
Rect(240, 212, 40, 70, fill='white')

def onMousePress(mouseX, mouseY):
    # Change the visibility of the mouth and fullCheek and remove a bit of bamboo.
    ### Place Your Code Here ###
    mouth.visible = False
    fullCheek.visible= True
    bamboo.x1 = 170
    bamboo.y1 = 295
    # Then, add one to the bamboo count.
    ### Place Your Code Here ###
    counter.value += 1
def onMouseRelease(mouseX, mouseY):
    # Change the visibility of the mouth and fullCheek back and move the
    # bamboo to the panda's mouth.
    mouth.visible = True
    fullCheek.visible = False
    bamboo.x1 = 190
    bamboo.y1 = 265

onMousePress(100, 100)


# -
# ears
Circle(100, 100, 40)
Circle(300, 100, 40)

# body
Circle(200, 400, 175)

# face
Circle(200, 200, 125, fill='white')

# eyes
Oval(250, 170, 60, 80, rotateAngle=-30)
Oval(150, 170, 60, 80, rotateAngle=30)
Circle(160, 160, 15, fill='white')
Circle(240, 160, 15, fill='white')
Circle(160, 160, 5)
Circle(240, 160, 5)

# nose
Oval(200, 200, 50, 30)

# mouth
mouth = Circle(200, 250, 30, fill='lightCoral')
Rect(170, 215, 70, 35, fill='white')
Line(170, 250, 230, 250, fill='lightCoral', lineWidth=5)

# bamboo eaten label
Label('Amount of Bamboo Eaten:', 150, 25, size=25)

# Define the bamboo eaten counter.
### Fix Your Code Here ###
counter = Label(0, 320, 25, size=25)
# bamboo
bamboo = Line(190, 265, 100, 410,
              fill=gradient('oliveDrab', 'darkOliveGreen', 'darkGreen'),
              lineWidth=20)

# full cheek
fullCheek = Oval(275, 250, 60, 70, fill='white', border='black', borderWidth=3,
                 visible=False)
Rect(240, 212, 40, 70, fill='white')

def onMousePress(mouseX, mouseY):
    # Change the visibility of the mouth and fullCheek and remove a bit of bamboo.
    ### Place Your Code Here ###
    mouth.visible = False
    fullCheek.visible= True
    bamboo.x1 = 170
    bamboo.y1 = 295
    # Then, add one to the bamboo count.
    ### Place Your Code Here ###
    counter.value += 1
def onMouseRelease(mouseX, mouseY):
    # Change the visibility of the mouth and fullCheek back and move the
    # bamboo to the panda's mouth.
    mouth.visible = True
    fullCheek.visible = False
    bamboo.x1 = 190
    bamboo.y1 = 265

onMousePress(200, 100)
onMouseRelease(200, 100)

