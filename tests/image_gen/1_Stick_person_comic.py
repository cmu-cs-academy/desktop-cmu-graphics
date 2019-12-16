### There is a lot of code here, so look for the yellow highlighted lines
### to find where you need to add your code.

Line(200, 0, 200, 400)
Line(0, 200, 400, 200)

# left-top panel
Label('THE TALE OF', 100, 75, fill='lightSkyBlue', size=20, italic=True,
      bold=True)
Label('A PROGRAMMER', 100, 125, fill='lightSkyBlue', size=20, italic=True,
      bold=True)
# right-top panel
# Drawing order: speech bubble, computer, stick person 1, stick person 2

# Draw the speech for the top right corner using a label.
Label('I do not get your code', 300, 40, font='monospace')
Oval(300, 40, 175, 50, fill=None, border='black')
Line(320, 65, 340, 90)
Line(330, 65, 340, 90)

Rect(200, 120, 10, 50, fill='grey', border='black')
Rect(200, 175, 25, 10, fill='grey', border='black')

Rect(242, 150, 16, 50, fill='lightSkyBlue', border='black')
Line(255, 155, 215, 170)
Circle(250, 135, 15, fill='white', border='black')
Circle(244, 135, 2)

Line(340, 140, 310, 130)
Line(310, 130, 340, 110)
Rect(332, 135, 16, 65, fill='lightGreen', border='black')
Circle(340, 120, 15, fill='white', border='black')
Circle(334, 120, 2)

# left-bottom panel
# Drawing order: speech bubble, computer, stick person 1, stick person 2

# Draw the speech for the bottom left corner using a label.
Label('Neither do I', 100, 240, font='monospace')
Oval(100, 240, 120, 50, fill=None, border='black')
Line(80, 265, 70, 290)
Line(90, 265, 70, 290)

Rect(0, 320, 10, 50, fill='grey', border='black')
Rect(0, 375, 25, 10, fill='grey', border='black')

Rect(42, 350, 16, 80, fill='lightSkyBlue', border='black')
Circle(50, 335, 15, fill='white', border='black')
Circle(56, 335, 2)

Rect(132, 335, 16, 80, fill='lightGreen', border='black')
Circle(140, 320, 15, fill='white', border='black')
Circle(134, 320, 2)

# right-bottom panel
# Drawing order: speech bubble, computer, stick person 1, stick person 2

# Draw the speech for the bottom right corner using a label.
Label('But it works!!', 300, 240, font='monospace')
Oval(300, 240, 150, 50, fill=None, border='black')
Line(280, 265, 270, 290)
Line(290, 265, 270, 290)

Rect(200, 320, 10, 50, fill='grey', border='black')
Rect(200, 375, 25, 10, fill='grey', border='black')

Line(250, 360, 215, 325)
Line(250, 360, 285, 325)
Rect(242, 350, 16, 80, fill='lightSkyBlue', border='black')
Circle(250, 335, 15, fill='white', border='black')
Line(245, 335, 260, 335, lineWidth=3, dashes=(3, 8))

Line(340, 320, 340, 400)
Rect(332, 335, 16, 80, fill='lightGreen', border='black')
Circle(340, 320, 15, fill='white', border='black')
Line(330, 320, 350, 320, dashes=(5, 7))

# This test case is intentionally left blank.

