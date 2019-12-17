app.background = rgb(200, 170, 130)
app.stepsPerSecond = 1

app.step = 0
app.time = 10

# shelves
Rect(0, 105, 400, 10, fill=rgb(230, 200, 160))
Rect(0, 215, 400, 10, fill=rgb(230, 200, 160))
Rect(0, 330, 400, 70, fill='gainsboro')

# timer
clock = Group(
    Circle(310, 345, 40, fill='white', border='black'),
    Line(310, 345, 310, 320, fill='red', lineWidth=3),
    Circle(310, 345, 3, fill='red')
    )
timer = Label('You have ' + str(app.time) + ' seconds', 310, 270, size=14,
              bold=True)
Label('to finish shopping!', 310, 290, size=14, bold=True)

# produce
orange = Group(
    Circle(80, 75, 30, fill='orange'),
    Star(80, 50, 4, 7, fill='olive')
    )
orange.name = 'orange'

apple = Group(
    Oval(190, 75, 50, 60, fill='red'),
    Oval(210, 75, 50, 60, fill='red'),
    Oval(207, 44, 8, 15, fill='green', rotateAngle=60)
    )
apple.name = 'apple'

pear = Group(
    Circle(320, 80, 25, fill='yellowGreen'),
    Circle(320, 60, 15, fill='yellowGreen'),
    Rect(320, 40, 6, 9, fill='olive', align='top')
    )
pear.name = 'pear'

milk = Group(
    Rect(55, 155, 50, 60, fill='white'),
    Rect(55, 197, 50, 8, fill='skyBlue'),
    Polygon(55, 155, 105, 155, 100, 140, 60, 140, fill='skyBlue'),
    Rect(60, 133, 40, 7, fill='white')
    )
milk.name = 'milk'

bread = Group(
    Rect(160, 175, 80, 40, fill='peru'),
    Circle(160, 195, 20, fill='peru'),
    Circle(240, 195, 20, fill='peru'),
    Polygon(170, 175, 180, 175, 175, 190, fill='wheat'),
    Polygon(230, 175, 220, 175, 225, 190, fill='wheat'),
    Polygon(195, 175, 205, 175, 200, 190, fill='wheat')
    )
bread.name = 'bread'

eggs = Group(
    Oval(320, 195, 15, 20, fill='white'),
    Oval(300, 195, 15, 20, fill='white'),
    Oval(340, 195, 15, 20, fill='white'),
    Polygon(285, 195, 355, 195, 350, 215, 290, 215, fill='gainsboro')
    )
eggs.name = 'eggs'

produce = Group(orange, apple, pear, milk, bread, eggs)

def drawGroceryList():
    produceNames = [ 'orange', 'apple', 'pear', 'milk', 'bread', 'eggs' ]

    # Loop over the produce names and add a label to the grocery list group.
    for i in range(len(produceNames)):
        if (i % 2 == 0):
            grocery = Label(produceNames[i], 75, 10 * i + 330, size=12)
        else:
            grocery = Label(produceNames[i], 160, 10 * (i - 1) + 330, size=12)
        groceryList.add(grocery)
# grocery list
Polygon(20, 410, 40, 280, 200, 280, 220, 410, fill='white', border='black')
Label('Shopping List', 120, 300, size=16)
Line(120, 320, 120, 400, fill='lightBlue', lineWidth=160, dashes=(2, 17))
groceryList = Group()
drawGroceryList()

def onMousePress(mouseX, mouseY):
    # See if the user clicked on a grocery item. If so, remove
    # the item from the grocery list and the produce group.
    target = produce.hitTest(mouseX, mouseY)
    if (target != None):
        for item in groceryList.children:
            if (item.value == target.name):
                groceryList.remove(item)
        produce.remove(target)
def onStep():
    app.time -= 1
    timer.value = 'You have ' + str(app.time) + ' seconds'
    clock.rotateAngle += 36
    if (app.time <= 0):
        app.stop()

onMousePress(200, 200)
onMousePress(320, 200)
app.paused = True


# -
app.background = rgb(200, 170, 130)
app.stepsPerSecond = 1

app.step = 0
app.time = 10

# shelves
Rect(0, 105, 400, 10, fill=rgb(230, 200, 160))
Rect(0, 215, 400, 10, fill=rgb(230, 200, 160))
Rect(0, 330, 400, 70, fill='gainsboro')

# timer
clock = Group(
    Circle(310, 345, 40, fill='white', border='black'),
    Line(310, 345, 310, 320, fill='red', lineWidth=3),
    Circle(310, 345, 3, fill='red')
    )
timer = Label('You have ' + str(app.time) + ' seconds', 310, 270, size=14,
              bold=True)
Label('to finish shopping!', 310, 290, size=14, bold=True)

# produce
orange = Group(
    Circle(80, 75, 30, fill='orange'),
    Star(80, 50, 4, 7, fill='olive')
    )
orange.name = 'orange'

apple = Group(
    Oval(190, 75, 50, 60, fill='red'),
    Oval(210, 75, 50, 60, fill='red'),
    Oval(207, 44, 8, 15, fill='green', rotateAngle=60)
    )
apple.name = 'apple'

pear = Group(
    Circle(320, 80, 25, fill='yellowGreen'),
    Circle(320, 60, 15, fill='yellowGreen'),
    Rect(320, 40, 6, 9, fill='olive', align='top')
    )
pear.name = 'pear'

milk = Group(
    Rect(55, 155, 50, 60, fill='white'),
    Rect(55, 197, 50, 8, fill='skyBlue'),
    Polygon(55, 155, 105, 155, 100, 140, 60, 140, fill='skyBlue'),
    Rect(60, 133, 40, 7, fill='white')
    )
milk.name = 'milk'

bread = Group(
    Rect(160, 175, 80, 40, fill='peru'),
    Circle(160, 195, 20, fill='peru'),
    Circle(240, 195, 20, fill='peru'),
    Polygon(170, 175, 180, 175, 175, 190, fill='wheat'),
    Polygon(230, 175, 220, 175, 225, 190, fill='wheat'),
    Polygon(195, 175, 205, 175, 200, 190, fill='wheat')
    )
bread.name = 'bread'

eggs = Group(
    Oval(320, 195, 15, 20, fill='white'),
    Oval(300, 195, 15, 20, fill='white'),
    Oval(340, 195, 15, 20, fill='white'),
    Polygon(285, 195, 355, 195, 350, 215, 290, 215, fill='gainsboro')
    )
eggs.name = 'eggs'

produce = Group(orange, apple, pear, milk, bread, eggs)

def drawGroceryList():
    produceNames = [ 'orange', 'apple', 'pear', 'milk', 'bread', 'eggs' ]

    # Loop over the produce names and add a label to the grocery list group.
    for i in range(len(produceNames)):
        if (i % 2 == 0):
            grocery = Label(produceNames[i], 75, 10 * i + 330, size=12)
        else:
            grocery = Label(produceNames[i], 160, 10 * (i - 1) + 330, size=12)
        groceryList.add(grocery)
# grocery list
Polygon(20, 410, 40, 280, 200, 280, 220, 410, fill='white', border='black')
Label('Shopping List', 120, 300, size=16)
Line(120, 320, 120, 400, fill='lightBlue', lineWidth=160, dashes=(2, 17))
groceryList = Group()
drawGroceryList()

def onMousePress(mouseX, mouseY):
    # See if the user clicked on a grocery item. If so, remove
    # the item from the grocery list and the produce group.
    target = produce.hitTest(mouseX, mouseY)
    if (target != None):
        for item in groceryList.children:
            if (item.value == target.name):
                groceryList.remove(item)
        produce.remove(target)
def onStep():
    app.time -= 1
    timer.value = 'You have ' + str(app.time) + ' seconds'
    clock.rotateAngle += 36
    if (app.time <= 0):
        app.stop()

onMousePress(200, 200)
onMousePress(320, 200)
app.paused = True


# -
app.background = rgb(200, 170, 130)
app.stepsPerSecond = 1

app.step = 0
app.time = 10

# shelves
Rect(0, 105, 400, 10, fill=rgb(230, 200, 160))
Rect(0, 215, 400, 10, fill=rgb(230, 200, 160))
Rect(0, 330, 400, 70, fill='gainsboro')

# timer
clock = Group(
    Circle(310, 345, 40, fill='white', border='black'),
    Line(310, 345, 310, 320, fill='red', lineWidth=3),
    Circle(310, 345, 3, fill='red')
    )
timer = Label('You have ' + str(app.time) + ' seconds', 310, 270, size=14,
              bold=True)
Label('to finish shopping!', 310, 290, size=14, bold=True)

# produce
orange = Group(
    Circle(80, 75, 30, fill='orange'),
    Star(80, 50, 4, 7, fill='olive')
    )
orange.name = 'orange'

apple = Group(
    Oval(190, 75, 50, 60, fill='red'),
    Oval(210, 75, 50, 60, fill='red'),
    Oval(207, 44, 8, 15, fill='green', rotateAngle=60)
    )
apple.name = 'apple'

pear = Group(
    Circle(320, 80, 25, fill='yellowGreen'),
    Circle(320, 60, 15, fill='yellowGreen'),
    Rect(320, 40, 6, 9, fill='olive', align='top')
    )
pear.name = 'pear'

milk = Group(
    Rect(55, 155, 50, 60, fill='white'),
    Rect(55, 197, 50, 8, fill='skyBlue'),
    Polygon(55, 155, 105, 155, 100, 140, 60, 140, fill='skyBlue'),
    Rect(60, 133, 40, 7, fill='white')
    )
milk.name = 'milk'

bread = Group(
    Rect(160, 175, 80, 40, fill='peru'),
    Circle(160, 195, 20, fill='peru'),
    Circle(240, 195, 20, fill='peru'),
    Polygon(170, 175, 180, 175, 175, 190, fill='wheat'),
    Polygon(230, 175, 220, 175, 225, 190, fill='wheat'),
    Polygon(195, 175, 205, 175, 200, 190, fill='wheat')
    )
bread.name = 'bread'

eggs = Group(
    Oval(320, 195, 15, 20, fill='white'),
    Oval(300, 195, 15, 20, fill='white'),
    Oval(340, 195, 15, 20, fill='white'),
    Polygon(285, 195, 355, 195, 350, 215, 290, 215, fill='gainsboro')
    )
eggs.name = 'eggs'

produce = Group(orange, apple, pear, milk, bread, eggs)

def drawGroceryList():
    produceNames = [ 'orange', 'apple', 'pear', 'milk', 'bread', 'eggs' ]

    # Loop over the produce names and add a label to the grocery list group.
    for i in range(len(produceNames)):
        if (i % 2 == 0):
            grocery = Label(produceNames[i], 75, 10 * i + 330, size=12)
        else:
            grocery = Label(produceNames[i], 160, 10 * (i - 1) + 330, size=12)
        groceryList.add(grocery)
# grocery list
Polygon(20, 410, 40, 280, 200, 280, 220, 410, fill='white', border='black')
Label('Shopping List', 120, 300, size=16)
Line(120, 320, 120, 400, fill='lightBlue', lineWidth=160, dashes=(2, 17))
groceryList = Group()
drawGroceryList()

def onMousePress(mouseX, mouseY):
    # See if the user clicked on a grocery item. If so, remove
    # the item from the grocery list and the produce group.
    target = produce.hitTest(mouseX, mouseY)
    if (target != None):
        for item in groceryList.children:
            if (item.value == target.name):
                groceryList.remove(item)
        produce.remove(target)
def onStep():
    app.time -= 1
    timer.value = 'You have ' + str(app.time) + ' seconds'
    clock.rotateAngle += 36
    if (app.time <= 0):
        app.stop()


