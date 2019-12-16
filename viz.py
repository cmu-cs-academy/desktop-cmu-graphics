### PACKAGES ###
import csv
from cmu_graphics import *


### HELPERS ###
def readCSV(filename):
    lst = []
    with open(filename, encoding='ISO-8859-1') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            lst.append(row)
    return lst


app.activeLoc = 0
app.activeYear = 0
app.features = ['coal', 'petro', 'gas']
app.location = ['Africa', 'Asia & Oceania','Europe', 'North America']
app.data = dict()
app.year=[1980, 1990, 2000, 2010]
app.maxData = [0, 0, 0]
### DATA ###
def processData():
    petro_file = readCSV('data/petro.csv')[1:]
    gas_file = readCSV('data/gas.csv')[1:]
    coal_file = readCSV('data/coal.csv')[1:]

    for i in range(len(app.location)):
        loc = app.location[i]
        app.data[loc] = []
        for j in range(len(app.year)):
            coal = round(float(coal_file[i][j+1]))
            petro = round(float(petro_file[i][j+1]))
            gas = round(float(gas_file[i][j+1]))
            dataByYear = [coal, petro, gas]
            app.data[loc].append(dataByYear)

            for i in range(3):
                app.maxData[i] = max(app.maxData[i], dataByYear[i])

processData()


## POLYGON TRANSITION BY ELLIOT (Modified) ##

app.time = 0

# Stores the next final position.
app.targetDist = [ ]

# If you want to change position and size, just change these.
app.cx = 200
app.cy = 220
app.maxDist = 150
app.numPoints = 3

# background polygon
q = Polygon(fill='aliceBlue', border='black', borderWidth=2)
p = Polygon(fill='dodgerBlue', opacity=90)
p.stable = False # If the polygon matches the current target position.

# app.scale = []
# def generateScale():
#     for i in range(len(app.year)):
#         petro = 0
#         gas = 0
#         coal = 0
#         for loc in app.location:
#             coal += app.data[loc][i][0]
#             petro += app.data[loc][i][1]
#             gas += app.data[loc][i][2]
#         app.scale.append([round(coal/4), round(petro/4), round(gas/4)])

# generateScale()

def getRandomDistance():
    '''
    Fills the targetDist list with 6 random distances.
    '''
    app.targetDist = [ ]
    for i in range(app.numPoints):
        app.targetDist.append(randrange(5, app.maxDist))

def distFromData(indicator):
    app.targetDist = [ ]
    if (not indicator):
        app.activeYear += 1
    app.activeYear %= 4
    loc = app.location[app.activeLoc]
    data = app.data[loc][app.activeYear]
    for i in range(len(app.features)):
        app.targetDist.append((data[i] / (app.maxData[i])) * app.maxDist)

def init():
    distFromData(True)
    # getRandomDistance()
    # Draw two full hexagons (background+main poly) and the background lines.
    for i in range(app.numPoints):
        x, y = getPointInDir(app.cx, app.cy, i * 360 / app.numPoints, app.maxDist)
        p.addPoint(x, y)
        q.addPoint(x, y)
        Line(app.cx, app.cy, x, y, lineWidth=1, opacity=30)
        p.toFront()
init()

def onStep():
    # Let the polygon sit in it's stable form for 1 second before transitioning.
    if p.stable == True:
        app.time += 1
        if (app.time == 30):
            app.time = 0
            # getRandomDistance()
            distFromData(False)
            p.stable = False
        update()

    else:
        lst = [ ]
        numStable = 0
        # For each point in the polygon.
        for i in range(app.numPoints):
            # Get the distance from the center to the current polygon point
            dist1 = distance(app.cx, app.cy, p.pointList[i][0], p.pointList[i][1])
            dist2 = app.targetDist[i] - dist1
            # If we are close to the target, just make the final jump to it.
            if abs(dist2) < 1:
                dist = app.targetDist[i]
                numStable += 1
            else:
                # Move partway to target for smooth motion.
                dist = dist1 + (dist2 / 15)

            # Get the point at the correct distance and angle from the center.
            x, y = getPointInDir(app.cx, app.cy, i * 360 / app.numPoints, dist)
            lst.append([ x, y ])

        # After lst is filled, set p.pointList to it to update the polygon's points.
        p.pointList = lst
        if (numStable == app.numPoints):
            p.stable = True

### MY CODE ###
Label('Energy Consumption (1980-2010)', 200, 20, size=20,
      font='courier', bold=True, fill='darkBlue')

Label('Coal', 200, 55, size=15, font='courier')
x2, y2 = getPointInDir(70, 295, 240, 15) # 50 - 35
Label('Gas', x2, y2, size=15, font='courier')
x3, y3 = getPointInDir(330, 295, 120, 15)
Label('Petro', x3, y3, size=15, font='courier')

app.buttonX = 100
app.buttonY = 340
app.button = []

def createLocButton():
    x = app.buttonX
    y = app.buttonY
    for i in range(len(app.location)):
        if (i == 2):
            y += 30
            x = app.buttonX
        if (i == app.activeLoc):
            dotColor, txtColor = 'skyBlue', 'black'
        else:
            dotColor, txtColor = 'lightGray', 'lightGray'
        b = Label(app.location[i], x+15, y, size=14,fill=txtColor,\
                  bold=True, font='courier', align='left')
        b.Circ = Circle(x, y, 8, fill=dotColor)
        app.button.append(b)
        x = b.right + 30
        x = b.right + 30

createLocButton()

legend = Group()
app.legendX = 20
app.legendY = 80

def createLegend():

    loc = app.location[app.activeLoc]
    data = app.data[loc][app.activeYear]

    coal = Label('Coal(Mmt):', app.legendX, app.legendY, size=13, font='courier', align='left')
    coal.data = Label(data[0], app.legendX+90, app.legendY, size=13, font='courier', align='left')
    petro = Label('Petro(Mmt):', app.legendX, app.legendY+20, size=13, font='courier', align='left')
    petro.data = Label(data[1], app.legendX+90, app.legendY+20, size=13, font='courier', align='left')
    gas = Label('Gas(bcm):', app.legendX, app.legendY+40, size=13, font='courier', align='left')
    gas.data = Label(data[2], app.legendX+90, app.legendY+40, size=13, font='courier', align='left')
    legend.add(coal)
    legend.add(petro)
    legend.add(gas)
    legend.visible = False
    for c in legend.children:
        c.data.visible = False


createLegend()

def update():
    for i in range(len(app.button)):
        if (i == app.activeLoc):
            dotColor, txtColor = 'skyBlue', 'black'
        else:
            dotColor, txtColor = 'lightGray', 'lightGray'
        b = app.button[i]
        b.Circ.fill = dotColor
        b.fill = txtColor

    for i in range(len(app.year)):
        color = 'silver'
        if (i==app.activeYear):
            color = 'royalBlue'
        Time.children[i].fill = color

    loc = app.location[app.activeLoc]
    data = app.data[loc][app.activeYear]

    for i in range(len(legend.children)):
        legend.children[i].data.value = data[i]

Time = Group()
def createBar(x, y):
    # color = ['paleTurquoise', 'lightSkyBlue', 'dodgerBlue', 'royalBlue']
    for i in range(4):
        color = 'silver'
        if (i == app.activeYear): color = 'royalBlue'
        block = Group(Rect(x, y+i*53, 12, 50, fill=color),
                      Label(app.year[i], x-20, y+i*55, font='courier', \
                      bold=True, fill=color))
        Time.add(block)
createBar(360, 60)

def onMousePress(mouseX, mouseY):
    for i in range(len(app.button)):
        b = app.button[i]
        # This part could have been a lot better with children hit test.
        if (b.hits(mouseX, mouseY) or b.Circ.hits(mouseX, mouseY)):
            app.activeLoc = i
            app.activeYear = 0
            distFromData(True)
            update()
    for i in range(len(app.year)):
        if (Time.children[i].hits(mouseX, mouseY)):
            app.activeYear = i
            update()

def onMouseMove(mouseX, mouseY):
    if p.hits(mouseX, mouseY):
        legend.visible = True
        for c in legend.children:
            c.data.visible = True
    else:
        legend.visible = False
        for c in legend.children:
            c.data.visible = False

### CALL CMU GRAPHICS ###
cmu_graphics.loop()
