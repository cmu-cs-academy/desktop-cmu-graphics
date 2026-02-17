from wyvern import App


class CircleApp(App):
    def init(self):
        self.cx = self.width / 2
        self.cy = self.height / 2
        self.speed = 100

    def mouse_pressed(self, x, y):
        self.cx = x
        self.cy = y
        self.draw()

    def tick(self, dt):
        self.cx += self.speed * dt
        self.draw()

    def draw(self):
        self.canvas.clear()
        self.canvas.draw_circle(self.cx, self.cy, 20)


CircleApp()
