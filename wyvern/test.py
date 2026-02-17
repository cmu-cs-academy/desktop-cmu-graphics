import wyvern


class Cursor(wyvern.App):
    def mouse_moved(self, x, y):
        self.canvas.clear()
        self.canvas.draw_circle(x, y, 30)


wyvern.run(Cursor)
