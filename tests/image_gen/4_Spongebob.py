# background
Rect(0, 250, 400, 150, fill='sandyBrown')
Rect(0, 0, 400, 250, fill='skyBlue')

# Spongebob's arms
Line(90, 200, 70, 250, fill=rgb(255, 250, 95), lineWidth=10)
Line(70, 245, 100, 260, fill=rgb(255, 250, 95), lineWidth=10)
Line(310, 215, 360, 215, fill=rgb(255, 250, 95), lineWidth=10)

# sleeves
Circle(100, 210, 20, fill='white', border='black')
Circle(300, 210, 20, fill='white', border='black')

# body
Polygon(100, 250, 85, 70, 105, 45, 295, 45,
        315, 70, 300, 250, fill=rgb(255, 250, 95))
Circle(105, 65, 20, fill=rgb(255, 250, 95))
Circle(295, 65, 20, fill=rgb(255, 250, 95))

# clothes
Rect(100, 250, 200, 10, fill='white')
Rect(100, 260, 200, 40, fill=rgb(190, 125, 95))
Polygon(190, 250, 200, 260, 190, 280, 200, 290, 210,
        280, 200, 260, 210, 250, fill='red')

# eyelashes
Line(145, 105, 130, 85, lineWidth=4)
Line(155, 105, 155, 77, lineWidth=4)
Line(175, 105, 185, 85, lineWidth=4)

Line(255, 105, 270, 85, lineWidth=4)
Line(245, 105, 245, 77, lineWidth=4)
Line(225, 105, 215, 85, lineWidth=4)

# smile
Oval(205, 185, 130, 50)
Oval(205, 185, 120, 40, fill=rgb(255, 250, 95))
Rect(140, 160, 130, 25, fill=rgb(255, 250, 95))

# legs
Line(160, 300, 160, 350, fill=rgb(255, 250, 95), lineWidth=10)
Line(240, 300, 240, 350, fill=rgb(255, 250, 95), lineWidth=10)

# eyes
Circle(160, 130, 40, fill='white', border='black')
Circle(240, 130, 40, fill='white', border='black')
Circle(170, 130, 17)
Circle(230, 130, 17)
Circle(170, 130, 15, border=rgb(130, 190, 235), borderWidth=7)
Circle(230, 130, 15, border=rgb(130, 190, 235), borderWidth=7)

# nose
Oval(200, 160, 32, 40, fill=rgb(255, 250, 95), border='black')
Rect(180, 170, 30, 30, fill=rgb(255, 250, 95))

# shoes
Oval(140, 360, 35, 20)
Line(160, 350, 160, 370, lineWidth=10)

Oval(260, 360, 35, 20)
Line(240, 350, 240, 370, lineWidth=10)

# spots
Oval(105, 90, 15, 30, fill=rgb(205, 190, 115))
Oval(290, 80, 15, 20, fill=rgb(205, 190, 115))
Oval(295, 160, 15, 25, fill=rgb(205, 190, 115))
Oval(270, 230, 20, 25, fill=rgb(205, 190, 115))
Oval(120, 210, 20, 35, fill=rgb(205, 190, 115))
Oval(155, 225, 15, 20, fill=rgb(205, 190, 115))

def drawFryCooking():
    Line(360, 240, 360, 150, fill='darkSlateGrey', lineWidth=10)
    Rect(340, 100, 40, 50, fill='darkSlateGrey')
    Line(349, 125, 371, 125, fill='skyBlue', lineWidth=30, dashes=(1, 9))

def drawJellyFishing():
    Line(360, 240, 360, 150, fill='sandyBrown', lineWidth=10)
    Oval(360, 125, 40, 50, fill='grey', opacity=20)
    Oval(335, 125, 80, 50, fill='grey', opacity=20)
    Oval(360, 125, 40, 50, fill=None, border='sandyBrown', borderWidth=7)

def drawConfused():
    Oval(355, 220, 80, 100, fill='white', border='black')
    Polygon(325, 190, 280, 200, 320, 220)
    Polygon(330, 193, 285, 200, 320, 218, fill='white')
    Label('?', 355, 220, size=50)

def drawActivity(activity):
    # Draw an appropriate item using the helper functions depending on
    # the activity.
    if (activity == 'fry-cooking'):
        drawFryCooking()
    elif (activity == 'jelly-fishing'):
        drawJellyFishing()
    else:
        drawConfused()

drawActivity('nothing')


# -
# background
Rect(0, 250, 400, 150, fill='sandyBrown')
Rect(0, 0, 400, 250, fill='skyBlue')

# Spongebob's arms
Line(90, 200, 70, 250, fill=rgb(255, 250, 95), lineWidth=10)
Line(70, 245, 100, 260, fill=rgb(255, 250, 95), lineWidth=10)
Line(310, 215, 360, 215, fill=rgb(255, 250, 95), lineWidth=10)

# sleeves
Circle(100, 210, 20, fill='white', border='black')
Circle(300, 210, 20, fill='white', border='black')

# body
Polygon(100, 250, 85, 70, 105, 45, 295, 45,
        315, 70, 300, 250, fill=rgb(255, 250, 95))
Circle(105, 65, 20, fill=rgb(255, 250, 95))
Circle(295, 65, 20, fill=rgb(255, 250, 95))

# clothes
Rect(100, 250, 200, 10, fill='white')
Rect(100, 260, 200, 40, fill=rgb(190, 125, 95))
Polygon(190, 250, 200, 260, 190, 280, 200, 290, 210,
        280, 200, 260, 210, 250, fill='red')

# eyelashes
Line(145, 105, 130, 85, lineWidth=4)
Line(155, 105, 155, 77, lineWidth=4)
Line(175, 105, 185, 85, lineWidth=4)

Line(255, 105, 270, 85, lineWidth=4)
Line(245, 105, 245, 77, lineWidth=4)
Line(225, 105, 215, 85, lineWidth=4)

# smile
Oval(205, 185, 130, 50)
Oval(205, 185, 120, 40, fill=rgb(255, 250, 95))
Rect(140, 160, 130, 25, fill=rgb(255, 250, 95))

# legs
Line(160, 300, 160, 350, fill=rgb(255, 250, 95), lineWidth=10)
Line(240, 300, 240, 350, fill=rgb(255, 250, 95), lineWidth=10)

# eyes
Circle(160, 130, 40, fill='white', border='black')
Circle(240, 130, 40, fill='white', border='black')
Circle(170, 130, 17)
Circle(230, 130, 17)
Circle(170, 130, 15, border=rgb(130, 190, 235), borderWidth=7)
Circle(230, 130, 15, border=rgb(130, 190, 235), borderWidth=7)

# nose
Oval(200, 160, 32, 40, fill=rgb(255, 250, 95), border='black')
Rect(180, 170, 30, 30, fill=rgb(255, 250, 95))

# shoes
Oval(140, 360, 35, 20)
Line(160, 350, 160, 370, lineWidth=10)

Oval(260, 360, 35, 20)
Line(240, 350, 240, 370, lineWidth=10)

# spots
Oval(105, 90, 15, 30, fill=rgb(205, 190, 115))
Oval(290, 80, 15, 20, fill=rgb(205, 190, 115))
Oval(295, 160, 15, 25, fill=rgb(205, 190, 115))
Oval(270, 230, 20, 25, fill=rgb(205, 190, 115))
Oval(120, 210, 20, 35, fill=rgb(205, 190, 115))
Oval(155, 225, 15, 20, fill=rgb(205, 190, 115))

def drawFryCooking():
    Line(360, 240, 360, 150, fill='darkSlateGrey', lineWidth=10)
    Rect(340, 100, 40, 50, fill='darkSlateGrey')
    Line(349, 125, 371, 125, fill='skyBlue', lineWidth=30, dashes=(1, 9))

def drawJellyFishing():
    Line(360, 240, 360, 150, fill='sandyBrown', lineWidth=10)
    Oval(360, 125, 40, 50, fill='grey', opacity=20)
    Oval(335, 125, 80, 50, fill='grey', opacity=20)
    Oval(360, 125, 40, 50, fill=None, border='sandyBrown', borderWidth=7)

def drawConfused():
    Oval(355, 220, 80, 100, fill='white', border='black')
    Polygon(325, 190, 280, 200, 320, 220)
    Polygon(330, 193, 285, 200, 320, 218, fill='white')
    Label('?', 355, 220, size=50)

def drawActivity(activity):
    # Draw an appropriate item using the helper functions depending on
    # the activity.
    if (activity == 'fry-cooking'):
        drawFryCooking()
    elif (activity == 'jelly-fishing'):
        drawJellyFishing()
    else:
        drawConfused()

drawActivity('singing')


# -
# background
Rect(0, 250, 400, 150, fill='sandyBrown')
Rect(0, 0, 400, 250, fill='skyBlue')

# Spongebob's arms
Line(90, 200, 70, 250, fill=rgb(255, 250, 95), lineWidth=10)
Line(70, 245, 100, 260, fill=rgb(255, 250, 95), lineWidth=10)
Line(310, 215, 360, 215, fill=rgb(255, 250, 95), lineWidth=10)

# sleeves
Circle(100, 210, 20, fill='white', border='black')
Circle(300, 210, 20, fill='white', border='black')

# body
Polygon(100, 250, 85, 70, 105, 45, 295, 45,
        315, 70, 300, 250, fill=rgb(255, 250, 95))
Circle(105, 65, 20, fill=rgb(255, 250, 95))
Circle(295, 65, 20, fill=rgb(255, 250, 95))

# clothes
Rect(100, 250, 200, 10, fill='white')
Rect(100, 260, 200, 40, fill=rgb(190, 125, 95))
Polygon(190, 250, 200, 260, 190, 280, 200, 290, 210,
        280, 200, 260, 210, 250, fill='red')

# eyelashes
Line(145, 105, 130, 85, lineWidth=4)
Line(155, 105, 155, 77, lineWidth=4)
Line(175, 105, 185, 85, lineWidth=4)

Line(255, 105, 270, 85, lineWidth=4)
Line(245, 105, 245, 77, lineWidth=4)
Line(225, 105, 215, 85, lineWidth=4)

# smile
Oval(205, 185, 130, 50)
Oval(205, 185, 120, 40, fill=rgb(255, 250, 95))
Rect(140, 160, 130, 25, fill=rgb(255, 250, 95))

# legs
Line(160, 300, 160, 350, fill=rgb(255, 250, 95), lineWidth=10)
Line(240, 300, 240, 350, fill=rgb(255, 250, 95), lineWidth=10)

# eyes
Circle(160, 130, 40, fill='white', border='black')
Circle(240, 130, 40, fill='white', border='black')
Circle(170, 130, 17)
Circle(230, 130, 17)
Circle(170, 130, 15, border=rgb(130, 190, 235), borderWidth=7)
Circle(230, 130, 15, border=rgb(130, 190, 235), borderWidth=7)

# nose
Oval(200, 160, 32, 40, fill=rgb(255, 250, 95), border='black')
Rect(180, 170, 30, 30, fill=rgb(255, 250, 95))

# shoes
Oval(140, 360, 35, 20)
Line(160, 350, 160, 370, lineWidth=10)

Oval(260, 360, 35, 20)
Line(240, 350, 240, 370, lineWidth=10)

# spots
Oval(105, 90, 15, 30, fill=rgb(205, 190, 115))
Oval(290, 80, 15, 20, fill=rgb(205, 190, 115))
Oval(295, 160, 15, 25, fill=rgb(205, 190, 115))
Oval(270, 230, 20, 25, fill=rgb(205, 190, 115))
Oval(120, 210, 20, 35, fill=rgb(205, 190, 115))
Oval(155, 225, 15, 20, fill=rgb(205, 190, 115))

def drawFryCooking():
    Line(360, 240, 360, 150, fill='darkSlateGrey', lineWidth=10)
    Rect(340, 100, 40, 50, fill='darkSlateGrey')
    Line(349, 125, 371, 125, fill='skyBlue', lineWidth=30, dashes=(1, 9))

def drawJellyFishing():
    Line(360, 240, 360, 150, fill='sandyBrown', lineWidth=10)
    Oval(360, 125, 40, 50, fill='grey', opacity=20)
    Oval(335, 125, 80, 50, fill='grey', opacity=20)
    Oval(360, 125, 40, 50, fill=None, border='sandyBrown', borderWidth=7)

def drawConfused():
    Oval(355, 220, 80, 100, fill='white', border='black')
    Polygon(325, 190, 280, 200, 320, 220)
    Polygon(330, 193, 285, 200, 320, 218, fill='white')
    Label('?', 355, 220, size=50)

def drawActivity(activity):
    # Draw an appropriate item using the helper functions depending on
    # the activity.
    if (activity == 'fry-cooking'):
        drawFryCooking()
    elif (activity == 'jelly-fishing'):
        drawJellyFishing()
    else:
        drawConfused()

drawActivity('huh?')

