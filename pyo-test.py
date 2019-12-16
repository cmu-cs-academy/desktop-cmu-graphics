from cmu_graphics import *
from pyo import *

app.stepsPerSecond = 5
app.nextRadius = 0

Rect(0, 0, 400, 400)

s = Sound(notes=["A4", "C4"])

# Displays the final waveform
# sp = Scope(h1+h2+h3+h4+h5+h6, mul=f)

def onMousePress(x, y):
    s.play()

def onMouseRelease(x, y):
    s.pause()

def onStep():
    if (app.nextRadius < 200):
        # Increases the radius by 5.
        app.nextRadius += 5

        # Define these variables to generate new random values for the next
        # circle. Borders are less than 50 and dash values are less than 100.
        redGreen = randrange(0, 256)
        newBorderWidth = randrange(0, 50)
        dashWidth = randrange(0, 100)
        dashSpace = randrange(0, 100)


        # Draws the next circle with the values generated above.
        Circle(200, 200, app.nextRadius, fill=None,
               border=rgb(redGreen, 255 - redGreen, 255),
               borderWidth=newBorderWidth, dashes=(dashWidth, dashSpace))


cmu_graphics.loop()











# from cmu_graphics import *
# from pyo import *

# app.stepsPerSecond = 5
# app.nextRadius = 0

# Rect(0, 0, 400, 400)

# s = Server().boot()
# s.start()
# s.amp = 0.1
# f = Adsr(attack=.01, decay=.1, sustain=1, release=.5, dur=5, mul=1)

# # Sets fundamental frequency
# freq = 200

# # Approximates a triangle waveform by adding odd harmonics with
# # amplitude proportional to the inverse square of the harmonic number.
# h1 = Sine(freq=freq, mul=1).out()
# h2 = Sine(freq=freq*3, phase=0.5, mul=1./pow(3,2))
# h3 = Sine(freq=freq*5, mul=1./pow(5,2))
# h4 = Sine(freq=freq*7, phase=0.5, mul=1./pow(7,2))
# h5 = Sine(freq=freq*9, mul=1./pow(9,2))
# h6 = Sine(freq=freq*11, phase=0.5, mul=1./pow(11,2))

# m = Mix([h1, h2, h3, h4, h5, h6], mul=f).out()
# d = Delay(m, delay=[.15,.2], feedback=.5, mul=.4).out()

# # Displays the final waveform
# # sp = Scope(h1+h2+h3+h4+h5+h6, mul=f)

# def onMousePress(x, y):
#     f.play()

# def onMouseRelease(x, y):
#     f.stop()

# def onStep():
#     if (app.nextRadius < 200):
#         # Increases the radius by 5.
#         app.nextRadius += 5

#         # Define these variables to generate new random values for the next
#         # circle. Borders are less than 50 and dash values are less than 100.
#         redGreen = randrange(0, 256)
#         newBorderWidth = randrange(0, 50)
#         dashWidth = randrange(0, 100)
#         dashSpace = randrange(0, 100)


#         # Draws the next circle with the values generated above.
#         Circle(200, 200, app.nextRadius, fill=None,
#                border=rgb(redGreen, 255 - redGreen, 255),
#                borderWidth=newBorderWidth, dashes=(dashWidth, dashSpace))


# cmu_graphics.loop()
# s.stop()
