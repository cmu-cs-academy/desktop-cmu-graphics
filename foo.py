from cmu_graphics import *

def redrawAll(app):
	drawRect(100, 100, app.width - 200, 200, fill='blue')

def onKeyPress(app, key):
	app.width += 10

runApp()
