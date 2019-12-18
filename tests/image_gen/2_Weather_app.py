app.background = gradient('azure', rgb(0, 205, 255), rgb(0, 205, 255),
                          start='left-top')

# background and text
Label('Pittsburgh', 200, 110, fill='white', size=35)
Label('Sunny', 200, 145, fill='white', size=20)
Label('12:05', 200, 10, fill='white', size=15)
Label('47%', 350, 10, fill='white', size=15)
Rect(372, 5, 23, 10, fill=None, border='white')
Rect(372, 5, 11, 10, fill='white')
Star(50, 345, 20, 8, fill='yellow', roundness=20)
Star(150, 345, 20, 8, fill='yellow', roundness=20)
Star(250, 345, 20, 8, fill='yellow', roundness=20)
Star(350, 345, 20, 8, fill='yellow', roundness=20)
Oval(360, 350, 25, 20, fill='gray')
Oval(370, 350, 25, 20, fill='gray')
Oval(365, 345, 20, 20, fill='gray')
Label('1PM', 50, 315, fill='white', size=16)
Label('2PM', 150, 315, fill='white', size=16)
Label('3PM', 250, 315, fill='white', size=16)
Label('4PM', 350, 315, fill='white', size=16)
Line(0, 300, 400, 300, fill='white')

# units toggle
unitLabel = Label('C', 40, 280, fill='goldenrod', bold=True)
unitCircle = Group(
    Circle(40, 280, 8, fill='white'),
    unitLabel
    )
unitBase = Group(
    Rect(40, 270, 20, 20, fill='goldenrod'),
    Circle(40, 280, 10, fill='goldenrod'),
    Circle(60, 280, 10, fill='goldenrod'),
    unitCircle
    )

temperatures = Group(
    Label(24, 350, 285, fill='white', size=16),
    Label(32, 380, 285, fill='white', size=16),
    Label(24, 200, 210, fill='white', size=70),
    Label(25, 50, 380, fill='white', size=18),
    Label(27, 150, 380, fill='white', size=18),
    Label(28, 250, 380, fill='white', size=18),
    Label(30, 350, 380, fill='white', size=18)
    )
temperatures.isCelsius = True

def changeUnits(temp, isCelsius):
    # Changes the units of the temperature from Celsius to Fahrenheit or back
    # using the formula: celsius = fahrenheit * 9/5 + 32.
    if (isCelsius == True):
        newTemp = rounded(temp.value * (9 / 5) + 32)
    else:
        newTemp = rounded((temp.value - 32) * (5 / 9))

    # Return newTemp.
    return newTemp
def onMousePress(mouseX, mouseY):
    # Checks to see if the toggle was clicked.
    if (unitBase.hits(mouseX, mouseY) == True):
        # Change the units of each temperature.
        for temp in temperatures.children:
            temp.value = changeUnits(temp, temperatures.isCelsius)
        # Toggles the label and the custom property.
        if (unitLabel.value == 'C'):
            unitLabel.value = 'F'
            unitCircle.centerX += 20
            temperatures.isCelsius = False
        else:
            unitLabel.value = 'C'
            unitCircle.centerX -= 20
            temperatures.isCelsius = True



# -
app.background = gradient('azure', rgb(0, 205, 255), rgb(0, 205, 255),
                          start='left-top')

# background and text
Label('Pittsburgh', 200, 110, fill='white', size=35)
Label('Sunny', 200, 145, fill='white', size=20)
Label('12:05', 200, 10, fill='white', size=15)
Label('47%', 350, 10, fill='white', size=15)
Rect(372, 5, 23, 10, fill=None, border='white')
Rect(372, 5, 11, 10, fill='white')
Star(50, 345, 20, 8, fill='yellow', roundness=20)
Star(150, 345, 20, 8, fill='yellow', roundness=20)
Star(250, 345, 20, 8, fill='yellow', roundness=20)
Star(350, 345, 20, 8, fill='yellow', roundness=20)
Oval(360, 350, 25, 20, fill='gray')
Oval(370, 350, 25, 20, fill='gray')
Oval(365, 345, 20, 20, fill='gray')
Label('1PM', 50, 315, fill='white', size=16)
Label('2PM', 150, 315, fill='white', size=16)
Label('3PM', 250, 315, fill='white', size=16)
Label('4PM', 350, 315, fill='white', size=16)
Line(0, 300, 400, 300, fill='white')

# units toggle
unitLabel = Label('C', 40, 280, fill='goldenrod', bold=True)
unitCircle = Group(
    Circle(40, 280, 8, fill='white'),
    unitLabel
    )
unitBase = Group(
    Rect(40, 270, 20, 20, fill='goldenrod'),
    Circle(40, 280, 10, fill='goldenrod'),
    Circle(60, 280, 10, fill='goldenrod'),
    unitCircle
    )

temperatures = Group(
    Label(24, 350, 285, fill='white', size=16),
    Label(32, 380, 285, fill='white', size=16),
    Label(24, 200, 210, fill='white', size=70),
    Label(25, 50, 380, fill='white', size=18),
    Label(27, 150, 380, fill='white', size=18),
    Label(28, 250, 380, fill='white', size=18),
    Label(30, 350, 380, fill='white', size=18)
    )
temperatures.isCelsius = True

def changeUnits(temp, isCelsius):
    # Changes the units of the temperature from Celsius to Fahrenheit or back
    # using the formula: celsius = fahrenheit * 9/5 + 32.
    if (isCelsius == True):
        newTemp = rounded(temp.value * (9 / 5) + 32)
    else:
        newTemp = rounded((temp.value - 32) * (5 / 9))

    # Return newTemp.
    return newTemp
def onMousePress(mouseX, mouseY):
    # Checks to see if the toggle was clicked.
    if (unitBase.hits(mouseX, mouseY) == True):
        # Change the units of each temperature.
        for temp in temperatures.children:
            temp.value = changeUnits(temp, temperatures.isCelsius)
        # Toggles the label and the custom property.
        if (unitLabel.value == 'C'):
            unitLabel.value = 'F'
            unitCircle.centerX += 20
            temperatures.isCelsius = False
        else:
            unitLabel.value = 'C'
            unitCircle.centerX -= 20
            temperatures.isCelsius = True



# -
app.background = gradient('azure', rgb(0, 205, 255), rgb(0, 205, 255),
                          start='left-top')

# background and text
Label('Pittsburgh', 200, 110, fill='white', size=35)
Label('Sunny', 200, 145, fill='white', size=20)
Label('12:05', 200, 10, fill='white', size=15)
Label('47%', 350, 10, fill='white', size=15)
Rect(372, 5, 23, 10, fill=None, border='white')
Rect(372, 5, 11, 10, fill='white')
Star(50, 345, 20, 8, fill='yellow', roundness=20)
Star(150, 345, 20, 8, fill='yellow', roundness=20)
Star(250, 345, 20, 8, fill='yellow', roundness=20)
Star(350, 345, 20, 8, fill='yellow', roundness=20)
Oval(360, 350, 25, 20, fill='gray')
Oval(370, 350, 25, 20, fill='gray')
Oval(365, 345, 20, 20, fill='gray')
Label('1PM', 50, 315, fill='white', size=16)
Label('2PM', 150, 315, fill='white', size=16)
Label('3PM', 250, 315, fill='white', size=16)
Label('4PM', 350, 315, fill='white', size=16)
Line(0, 300, 400, 300, fill='white')

# units toggle
unitLabel = Label('C', 40, 280, fill='goldenrod', bold=True)
unitCircle = Group(
    Circle(40, 280, 8, fill='white'),
    unitLabel
    )
unitBase = Group(
    Rect(40, 270, 20, 20, fill='goldenrod'),
    Circle(40, 280, 10, fill='goldenrod'),
    Circle(60, 280, 10, fill='goldenrod'),
    unitCircle
    )

temperatures = Group(
    Label(24, 350, 285, fill='white', size=16),
    Label(32, 380, 285, fill='white', size=16),
    Label(24, 200, 210, fill='white', size=70),
    Label(25, 50, 380, fill='white', size=18),
    Label(27, 150, 380, fill='white', size=18),
    Label(28, 250, 380, fill='white', size=18),
    Label(30, 350, 380, fill='white', size=18)
    )
temperatures.isCelsius = True

def changeUnits(temp, isCelsius):
    # Changes the units of the temperature from Celsius to Fahrenheit or back
    # using the formula: celsius = fahrenheit * 9/5 + 32.
    if (isCelsius == True):
        newTemp = rounded(temp.value * (9 / 5) + 32)
    else:
        newTemp = rounded((temp.value - 32) * (5 / 9))

    # Return newTemp.
    return newTemp
def onMousePress(mouseX, mouseY):
    # Checks to see if the toggle was clicked.
    if (unitBase.hits(mouseX, mouseY) == True):
        # Change the units of each temperature.
        for temp in temperatures.children:
            temp.value = changeUnits(temp, temperatures.isCelsius)
        # Toggles the label and the custom property.
        if (unitLabel.value == 'C'):
            unitLabel.value = 'F'
            unitCircle.centerX += 20
            temperatures.isCelsius = False
        else:
            unitLabel.value = 'C'
            unitCircle.centerX -= 20
            temperatures.isCelsius = True

onMousePress(50, 280)
onMousePress(50, 280)

