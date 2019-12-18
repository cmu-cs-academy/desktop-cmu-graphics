app.background = gradient('deepSkyBlue', 'lightSkyBlue', start='top')

Rect(0, 150, 400, 250, fill=gradient('forestGreen', 'limeGreen', start='bottom'))

# traffic light
Line(200, 75, 200, 65)
Line(0, 50, 200, 65)
Line(400, 50, 200, 65)
Rect(175, 75, 50, 100, fill='orange')
redLight = Circle(200, 100, 20, fill='red')
greenLight = Circle(200, 150, 20, fill='gray')
msg = Label('Stop!', 200, 350, size=20, bold=True)

# road
Rect(0, 200, 400, 100)
Line(0, 250, 400, 250, fill='yellow', lineWidth=3, dashes=True)

# car
car = Polygon(0, 211, 3, 210, 12, 210, 15, 211, 30, 211, 33, 210, 45, 210, 48, 220,
              48, 230, 45, 240, 33, 240, 30, 239, 15, 239, 12, 240, 3, 240, 0, 239,
              fill=gradient('royalBlue', 'mediumBlue'))
frontWindow = Polygon(40, 215, 42, 225, 40, 235, 30, 234, 30, 216)
backWindow = Rect(5, 215, 5, 20)
top = Polygon(10, 215, 30, 216, 30, 234, 10, 235, fill=None, border='black',
              borderWidth=1)

def moveCar(leftPosition):
    car.left = leftPosition
    frontWindow.left = leftPosition + 30
    backWindow.left = leftPosition + 5
    top.left = backWindow.right

def changeLight(redFill, greenFill, msgValue):
    redLight.fill = redFill
    greenLight.fill = greenFill
    msg.value = msgValue

def onKeyPress(key):
    # Changes the color of the light.
    if (key == 'enter'):
        if (msg.value == 'Go!'):
            changeLight('red', 'gray', 'Stop!')
        else:
            changeLight('gray', 'green', 'Go!')

def onKeyHold(keys):
    # Move the car forward or back to the starting point according to the
    # light color while the game is playing.
    if (msg.value != 'Car wins!'):
        if ('space' in keys):
            if (redLight.fill == 'red'):
                moveCar(0)
            else:
                moveCar(car.left + 3)
                if (car.right > 400):
                    msg.value = 'Car wins!'
                    msg.fill = car.fill

onKeyPress('enter')
onKeyHolds(['space'], 20)
onKeyPress('enter')
onKeyHolds(['space'], 20)


# -
app.background = gradient('deepSkyBlue', 'lightSkyBlue', start='top')

Rect(0, 150, 400, 250, fill=gradient('forestGreen', 'limeGreen', start='bottom'))

# traffic light
Line(200, 75, 200, 65)
Line(0, 50, 200, 65)
Line(400, 50, 200, 65)
Rect(175, 75, 50, 100, fill='orange')
redLight = Circle(200, 100, 20, fill='red')
greenLight = Circle(200, 150, 20, fill='gray')
msg = Label('Stop!', 200, 350, size=20, bold=True)

# road
Rect(0, 200, 400, 100)
Line(0, 250, 400, 250, fill='yellow', lineWidth=3, dashes=True)

# car
car = Polygon(0, 211, 3, 210, 12, 210, 15, 211, 30, 211, 33, 210, 45, 210, 48, 220,
              48, 230, 45, 240, 33, 240, 30, 239, 15, 239, 12, 240, 3, 240, 0, 239,
              fill=gradient('royalBlue', 'mediumBlue'))
frontWindow = Polygon(40, 215, 42, 225, 40, 235, 30, 234, 30, 216)
backWindow = Rect(5, 215, 5, 20)
top = Polygon(10, 215, 30, 216, 30, 234, 10, 235, fill=None, border='black',
              borderWidth=1)

def moveCar(leftPosition):
    car.left = leftPosition
    frontWindow.left = leftPosition + 30
    backWindow.left = leftPosition + 5
    top.left = backWindow.right

def changeLight(redFill, greenFill, msgValue):
    redLight.fill = redFill
    greenLight.fill = greenFill
    msg.value = msgValue

def onKeyPress(key):
    # Changes the color of the light.
    if (key == 'enter'):
        if (msg.value == 'Go!'):
            changeLight('red', 'gray', 'Stop!')
        else:
            changeLight('gray', 'green', 'Go!')

def onKeyHold(keys):
    # Move the car forward or back to the starting point according to the
    # light color while the game is playing.
    if (msg.value != 'Car wins!'):
        if ('space' in keys):
            if (redLight.fill == 'red'):
                moveCar(0)
            else:
                moveCar(car.left + 3)
                if (car.right > 400):
                    msg.value = 'Car wins!'
                    msg.fill = car.fill

onKeyPress('enter')
onKeyHolds(['space'], 20)


# -
app.background = gradient('deepSkyBlue', 'lightSkyBlue', start='top')

Rect(0, 150, 400, 250, fill=gradient('forestGreen', 'limeGreen', start='bottom'))

# traffic light
Line(200, 75, 200, 65)
Line(0, 50, 200, 65)
Line(400, 50, 200, 65)
Rect(175, 75, 50, 100, fill='orange')
redLight = Circle(200, 100, 20, fill='red')
greenLight = Circle(200, 150, 20, fill='gray')
msg = Label('Stop!', 200, 350, size=20, bold=True)

# road
Rect(0, 200, 400, 100)
Line(0, 250, 400, 250, fill='yellow', lineWidth=3, dashes=True)

# car
car = Polygon(0, 211, 3, 210, 12, 210, 15, 211, 30, 211, 33, 210, 45, 210, 48, 220,
              48, 230, 45, 240, 33, 240, 30, 239, 15, 239, 12, 240, 3, 240, 0, 239,
              fill=gradient('royalBlue', 'mediumBlue'))
frontWindow = Polygon(40, 215, 42, 225, 40, 235, 30, 234, 30, 216)
backWindow = Rect(5, 215, 5, 20)
top = Polygon(10, 215, 30, 216, 30, 234, 10, 235, fill=None, border='black',
              borderWidth=1)

def moveCar(leftPosition):
    car.left = leftPosition
    frontWindow.left = leftPosition + 30
    backWindow.left = leftPosition + 5
    top.left = backWindow.right

def changeLight(redFill, greenFill, msgValue):
    redLight.fill = redFill
    greenLight.fill = greenFill
    msg.value = msgValue

def onKeyPress(key):
    # Changes the color of the light.
    if (key == 'enter'):
        if (msg.value == 'Go!'):
            changeLight('red', 'gray', 'Stop!')
        else:
            changeLight('gray', 'green', 'Go!')

def onKeyHold(keys):
    # Move the car forward or back to the starting point according to the
    # light color while the game is playing.
    if (msg.value != 'Car wins!'):
        if ('space' in keys):
            if (redLight.fill == 'red'):
                moveCar(0)
            else:
                moveCar(car.left + 3)
                if (car.right > 400):
                    msg.value = 'Car wins!'
                    msg.fill = car.fill

onKeyPress('enter')

