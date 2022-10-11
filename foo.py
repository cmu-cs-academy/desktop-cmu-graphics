from cmu_graphics import *
import random

app.stepsPerSecond = 2
app.steps = 0

def onStep():
	Circle(random.randrange(0, app.width), random.randrange(0, app.height), random.randrange(10, 30), fill=random.choice(['red', 'green', 'blue', 'orange', 'purple']))

def onMousePress(x, y):
	print(x / 0)

cmu_graphics.run()
