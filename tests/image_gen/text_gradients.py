l = Label('Hi', 50, 50, size=50, fill=gradient('red', 'blue', start='left-top'))

Label('Hi', l.right + 50, 50, size=50, rotateAngle=180, fill=gradient('red', 'blue', start='left-top'))


Label('Hello, world!', 200, 175, size=60, db='bbox center', fill=gradient('red', 'orange'))
Label('Hello, world!', 200, 200, size=60, rotateAngle=135, db='bbox center', fill=gradient('red', 'orange'))
Label('Hello, world!', 200, 250, size=60, rotateAngle=180, db='bbox center', fill=gradient('red', 'orange'))

Label('Hello, world!', 200, 300, size=60, rotateAngle=195, db='bbox center',
    fill='orange', border=gradient('green', 'blue', start='bottom'),
    borderWidth=2)
