r1 = Rect(100, 0, 200, 200, fill='orange')
r2 = Rect(110, 10, 200, 200, fill='green', visible=False)
r3 = Rect(180, 80, 200, 200, fill='orange')


r1.visible = False
r2.visible = True

# -

a = Rect(50, 250, 50, 50, fill='black', visible=False)
b = Rect(60, 260, 50, 50, fill='red', visible=False)

a.visible=True
b.visible=True


# -

a = Rect(100, 250, 50, 50, fill='black', visible=False)
b = Rect(110, 260, 50, 50, fill='red', visible=False)

b.visible=True
a.visible=True


# -

a = Rect(150, 250, 100, 100, fill='black')
c = Rect(170, 270, 100, 100, fill='pink')
b = Rect(160, 260, 100, 100, fill='red')

c.toFront()
b.visible = False
b.visible = True
