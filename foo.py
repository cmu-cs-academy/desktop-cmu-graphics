from cmu_graphics import *


app.i = 0
fonts = ('serif', 'sans-serif', 'cursive', 'fantasy', 'monospace')

l = Label('Test Text', 200, 200, size=50, font='serif')

def onKeyPress(key):
	app.i += 1
	app.i %= len(fonts)
	l.font = fonts[app.i]

cmu_graphics.run()
