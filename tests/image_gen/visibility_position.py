r1 = Rect(100, 0, 200, 200, fill='orange')
r2 = Rect(100, 100, 200, 200, fill='green', visible=False)

c1 = Circle(100, 180, 60, fill='blue')
c2 = Circle(200, 180, 60, fill='cyan')
c3 = Circle(300, 180, 60, fill='navy')
g = Group(c1, c2, c3)

r3 = Rect(100, 200, 200, 200, fill='yellow')

# -
r2.visible = True

# -
r2.visible = False

# -
r2.visible = True
r1.visible = False

# -
r1.visible = True
g.visible = False

# -
g.visible = True

# -
c1.visible = False

# -
c1.visible = True
c2.visible = False

# -
c2.visible = True
c3.visible = False

# -
c3.visible = True

# -
x = 50
a = Circle(x, 370, 30)
b = Circle(x, 370, 10, fill="red")
c = Circle(x, 370, 5, fill="green")
a.visible = False
b.visible = False
a.visible = True
b.visible = True

x += 50
a = Circle(x, 370, 30)
b = Circle(x, 370, 10, fill="red")
c = Circle(x, 370, 5, fill="green")
a.visible = False
b.visible = False
b.visible = True
a.visible = True

x += 50
a = Circle(x, 370, 30)
b = Circle(x, 370, 10, fill="red")
c = Circle(x, 370, 5, fill="green")
b.visible = False
a.visible = False
b.visible = True
a.visible = True

x += 50
a = Circle(x, 370, 30)
b = Circle(x, 370, 10, fill="red")
c = Circle(x, 370, 5, fill="green")
b.visible = False
a.visible = False
a.visible = True
b.visible = True
