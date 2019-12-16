# background
Rect(0, 0, 400, 400, fill='lightGreen')

def drawRoad(startX, startY, endX, endY):
    Line(startX, startY, endX, endY, fill=rgb(142, 137, 131), lineWidth=4)

def drawRiver(centerX, centerY, width, height):
    Oval(centerX, centerY, width, height,
         fill=gradient('dodgerBlue', 'royalBlue', start='left-top'))
    Oval(centerX, centerY, width - 30, height - 30, fill='lightGreen')

# lake and rivers
Oval(10, 300, 100, 150, fill=gradient('dodgerBlue', 'royalBlue', start='left-top'))
drawRiver(400, 0, 450, 320)
drawRiver(400, 400, 350, 350)

# roads
drawRoad(35, 110, 100, 110)
drawRoad(100, 110, 100, 265)
drawRoad(100, 110, 155, 170)
drawRoad(155, 170, 345, 170)
drawRoad(345, 170, 405, 205)
drawRoad(35, 110, 35, 35)
drawRoad(0, 35, 220, 35)
drawRoad(220, 35, 255, -5)
drawRoad(-5, 180, 185, 335)
drawRoad(185, 335, 405, 335)
drawRoad(100, 265, 60, 360)
drawRoad(60, 360, 60, 405)
drawRoad(295, 405, 295, 80)
drawRoad(295, 80, 220, 35)
drawRoad(295, 80, 405, 80)

def onMousePress(mouseX, mouseY):
    # Draw a pushpin.
    Circle(mouseX, mouseY, 2)
    Line(mouseX, mouseY, mouseX, mouseY - 20)
    Circle(mouseX, mouseY - 20, 5, fill='crimson')



# -
# background
Rect(0, 0, 400, 400, fill='lightGreen')

def drawRoad(startX, startY, endX, endY):
    Line(startX, startY, endX, endY, fill=rgb(142, 137, 131), lineWidth=4)

def drawRiver(centerX, centerY, width, height):
    Oval(centerX, centerY, width, height,
         fill=gradient('dodgerBlue', 'royalBlue', start='left-top'))
    Oval(centerX, centerY, width - 30, height - 30, fill='lightGreen')

# lake and rivers
Oval(10, 300, 100, 150, fill=gradient('dodgerBlue', 'royalBlue', start='left-top'))
drawRiver(400, 0, 450, 320)
drawRiver(400, 400, 350, 350)

# roads
drawRoad(35, 110, 100, 110)
drawRoad(100, 110, 100, 265)
drawRoad(100, 110, 155, 170)
drawRoad(155, 170, 345, 170)
drawRoad(345, 170, 405, 205)
drawRoad(35, 110, 35, 35)
drawRoad(0, 35, 220, 35)
drawRoad(220, 35, 255, -5)
drawRoad(-5, 180, 185, 335)
drawRoad(185, 335, 405, 335)
drawRoad(100, 265, 60, 360)
drawRoad(60, 360, 60, 405)
drawRoad(295, 405, 295, 80)
drawRoad(295, 80, 220, 35)
drawRoad(295, 80, 405, 80)

def onMousePress(mouseX, mouseY):
    # Draw a pushpin.
    Circle(mouseX, mouseY, 2)
    Line(mouseX, mouseY, mouseX, mouseY - 20)
    Circle(mouseX, mouseY - 20, 5, fill='crimson')



# -
# background
Rect(0, 0, 400, 400, fill='lightGreen')

def drawRoad(startX, startY, endX, endY):
    Line(startX, startY, endX, endY, fill=rgb(142, 137, 131), lineWidth=4)

def drawRiver(centerX, centerY, width, height):
    Oval(centerX, centerY, width, height,
         fill=gradient('dodgerBlue', 'royalBlue', start='left-top'))
    Oval(centerX, centerY, width - 30, height - 30, fill='lightGreen')

# lake and rivers
Oval(10, 300, 100, 150, fill=gradient('dodgerBlue', 'royalBlue', start='left-top'))
drawRiver(400, 0, 450, 320)
drawRiver(400, 400, 350, 350)

# roads
drawRoad(35, 110, 100, 110)
drawRoad(100, 110, 100, 265)
drawRoad(100, 110, 155, 170)
drawRoad(155, 170, 345, 170)
drawRoad(345, 170, 405, 205)
drawRoad(35, 110, 35, 35)
drawRoad(0, 35, 220, 35)
drawRoad(220, 35, 255, -5)
drawRoad(-5, 180, 185, 335)
drawRoad(185, 335, 405, 335)
drawRoad(100, 265, 60, 360)
drawRoad(60, 360, 60, 405)
drawRoad(295, 405, 295, 80)
drawRoad(295, 80, 220, 35)
drawRoad(295, 80, 405, 80)

def onMousePress(mouseX, mouseY):
    # Draw a pushpin.
    Circle(mouseX, mouseY, 2)
    Line(mouseX, mouseY, mouseX, mouseY - 20)
    Circle(mouseX, mouseY - 20, 5, fill='crimson')

onMousePress(200, 200)

