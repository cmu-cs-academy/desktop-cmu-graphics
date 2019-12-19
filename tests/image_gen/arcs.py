a = Arc(50, 100, 100, 200, 45, 135, db='all')

# -
a = Arc(50, 100, 100, 200, 45, 135, db='all')

a.rotateAngle = 90

# -
a = Arc(50, 100, 100, 200, 45, 135, db='all')

a.width = 300

# -
a = Arc(50, 100, 100, 200, 45, 135, db='all')
a.sweepAngle = 20

# -
a = Arc(50, 100, 100, 200, 45, 135, db='all')
a.rotateAngle += 20

Arc(350, 350, 100, 50, 0, 270, border='red', fill='blue')

Arc(250, 350, 100, 50, 0, 270, border='red', fill='blue', db='all')

# Verify that the line join at the center doesn't get too big
Arc(300, 60, 80, 80, 0, 345, borderWidth=4, fill=None, border='green')
