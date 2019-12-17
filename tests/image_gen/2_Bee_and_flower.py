def beeAndFlower(backgroundColor, flowerColor):
    # The function currently ignores its parameters and always draws the same
    # image. Use the function parameters to replace hardcoded colors below!

    # background
    Rect(0, 0, 400, 400, fill=backgroundColor)

    # flower stem and petals
    Oval(197, 350, 85, 200, fill=rgb(75, 155, 100))
    Star(200, 125, 225, 25, fill=flowerColor, roundness=80)
    Star(200, 125, 275, 24, fill=flowerColor, roundness=60)

    # bee body and stripes
    Oval(80, 150, 100, 60,
         fill=gradient('gold', 'gold', 'gold', 'gold', 'black', 'gold', 'black',
                       'gold', 'black', 'gold', start='right'))

    # bee eye and wings
    Circle(110, 140, 3)
    Oval(80, 112, 40, 75, fill=gradient('gainsboro', 'dimGrey', start='top'),
         opacity=60)

beeAndFlower(rgb(75, 20, 130), gradient('aqua', 'blue', 'forestGreen'))


# -
def beeAndFlower(backgroundColor, flowerColor):
    # The function currently ignores its parameters and always draws the same
    # image. Use the function parameters to replace hardcoded colors below!

    # background
    Rect(0, 0, 400, 400, fill=backgroundColor)

    # flower stem and petals
    Oval(197, 350, 85, 200, fill=rgb(75, 155, 100))
    Star(200, 125, 225, 25, fill=flowerColor, roundness=80)
    Star(200, 125, 275, 24, fill=flowerColor, roundness=60)

    # bee body and stripes
    Oval(80, 150, 100, 60,
         fill=gradient('gold', 'gold', 'gold', 'gold', 'black', 'gold', 'black',
                       'gold', 'black', 'gold', start='right'))

    # bee eye and wings
    Circle(110, 140, 3)
    Oval(80, 112, 40, 75, fill=gradient('gainsboro', 'dimGrey', start='top'),
         opacity=60)

beeAndFlower(rgb(75, 20, 130), gradient('aqua', 'blue', 'forestGreen'))


# -
def beeAndFlower(backgroundColor, flowerColor):
    # The function currently ignores its parameters and always draws the same
    # image. Use the function parameters to replace hardcoded colors below!

    # background
    Rect(0, 0, 400, 400, fill=backgroundColor)

    # flower stem and petals
    Oval(197, 350, 85, 200, fill=rgb(75, 155, 100))
    Star(200, 125, 225, 25, fill=flowerColor, roundness=80)
    Star(200, 125, 275, 24, fill=flowerColor, roundness=60)

    # bee body and stripes
    Oval(80, 150, 100, 60,
         fill=gradient('gold', 'gold', 'gold', 'gold', 'black', 'gold', 'black',
                       'gold', 'black', 'gold', start='right'))

    # bee eye and wings
    Circle(110, 140, 3)
    Oval(80, 112, 40, 75, fill=gradient('gainsboro', 'dimGrey', start='top'),
         opacity=60)

beeAndFlower(rgb(75, 20, 130), gradient('aqua', 'blue', 'forestGreen'))

