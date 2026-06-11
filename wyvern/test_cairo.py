import math

### ZIPFILE VERSION ###
# import libs.pygame_loader as pygame

### END ZIPFILE VERSION ###
### PYPI VERSION ###
import cairo
import pygame

### END PYPI VERSION ###


class SandboxModal(object):
    def __init__(self):
        self.centerX = 300
        self.width = 600
        self.top = 0
        self.left = self.centerX - (self.width / 2)
        self.right = self.left + self.width

        self.height = 600

        self.textXMargin = 15
        self.textYMargin = 18
        self.betweenLineMargin = 8
        self.textSize = 20
        self.shadowShift = 2

        self.active = True

        pygame.display.set_caption('test')
        pygame.init()

        self.run()

    def redrawAll(self, screen, cairo_surface, ctx):
        self.draw(ctx)
        data_string = cairo_surface.get_data()
        pygame_surface = pygame.image.frombuffer(
            data_string, (int(self.width), int(self.height)), 'RGBA'
        )
        screen.fill((255, 255, 255))
        screen.blit(pygame_surface, (0, 0))

    def draw(self, ctx):
        ctx.save()

        ctx.new_path()
        ctx.move_to(50, 50)
        ctx.set_source_rgb(0.0, 0.0, 0.0)
        ctx.select_font_face(
            'Tahoma', cairo.FONT_WEIGHT_NORMAL, cairo.FONT_SLANT_NORMAL
        )
        ctx.set_font_size(20)
        ctx.text_path('test')
        ctx.set_line_width(2)
        ctx.set_line_join(cairo.LINE_JOIN_ROUND)
        ctx.arc(75, 100, 20, 0, 2 * math.pi)
        ctx.fill()
        ctx.set_line_join(cairo.LINE_JOIN_BEVEL)
        ctx.arc(125, 100, 20, 0, 2 * math.pi)
        # ctx.stroke()
        ctx.arc(175, 100, 20, 0, 3 * math.pi / 4)
        # ctx.stroke()
        ctx.arc(175, 100, 20, math.pi, 3 * math.pi / 4)
        # ctx.move_to(200, 50)
        ctx.rectangle(200, 50, 20, 20)
        ctx.stroke()

        ctx.move_to(50, 150)
        ctx.select_font_face('Arial', cairo.FONT_WEIGHT_BOLD, cairo.FONT_SLANT_ITALIC)
        ctx.text_path('test')
        ctx.fill()

        # ctx = wyvern.move_to(ctx, 75, 200)
        ctx.curve_to(75, 200, 175, 250, 275, 200)
        # ctx.set_dash([7, 7])
        ctx.stroke()

        ctx.rectangle(50, 300, 100, 50)
        # ctx.clip()
        ctx.fill_preserve()
        ctx.arc(200, 300, 20, math.pi, 3 * math.pi / 4)
        ctx.stroke()

        # ctx.rotate(math.pi / 4)
        # ctx.translate(400, -400)
        ctx.transform(cairo.Matrix(0, 1, 1, 0, 0, 0))
        ctx.rectangle(50, 400, 100, 50)
        ctx.stroke()

        gradient = cairo.LinearGradient(300, 300, 400, 400)

        # Add color stops (offset, r, g, b, alpha)
        gradient.add_color_stop_rgba(0.0, 1.0, 0.0, 0.0, 1.0)  # Start: Red
        gradient.add_color_stop_rgba(0.5, 0.0, 1.0, 0.0, 1.0)  # Middle: Green
        gradient.add_color_stop_rgba(1.0, 0.0, 0.0, 1.0, 1.0)  # End: Blue

        ctx.set_source(gradient)
        ctx.rectangle(300, 300, 100, 100)
        ctx.fill()

        gradient = cairo.RadialGradient(475, 100, 0, 475, 100, 100)

        gradient.add_color_stop_rgba(0.0, 1.0, 0.0, 0.0, 1.0)  # Start: Red
        gradient.add_color_stop_rgba(0.5, 0.0, 1.0, 0.0, 1.0)  # Middle: Green
        gradient.add_color_stop_rgba(1.0, 0.0, 0.0, 1.0, 1.0)  # End: Blue

        ctx.set_source(gradient)
        ctx.arc(475, 100, 100, 0, 2 * math.pi)
        ctx.fill()

        ctx.restore()

    def run(self):
        self._msPassed = 0
        self._refreshDelay = 60
        self._stepsPerSecond = 30

        clock = pygame.time.Clock()

        # Make antialiasing possible
        screen = pygame.display.set_mode((int(self.width), int(self.height)))
        cairo_surface = cairo.ImageSurface(
            cairo.FORMAT_ARGB32, int(self.width), int(self.height)
        )
        ctx = cairo.Context(cairo_surface)

        self.running = True
        while self.running:
            self._msPassed += clock.tick(self._refreshDelay)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if (
                self._msPassed > math.floor((1000 / self._stepsPerSecond))
                or abs(self._msPassed - math.floor((1000 / self._stepsPerSecond))) < 10
            ):
                self._msPassed = 0

            self.redrawAll(screen, cairo_surface, ctx)
            pygame.display.flip()

        pygame.display.quit()
        pygame.quit()


def main():
    SandboxModal()


if __name__ == '__main__':
    main()
