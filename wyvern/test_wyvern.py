import math

### ZIPFILE VERSION ###
# import libs.pygame_loader as pygame

### END ZIPFILE VERSION ###
### PYPI VERSION ###
import wyvern
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

    def redrawAll(self, screen, wyvern_surface, ctx):
        ctx = self.draw(ctx)
        data_string = wyvern_surface.data
        pygame_surface = pygame.image.frombuffer(
            data_string, (int(self.width), int(self.height)), 'RGBA'
        )
        screen.blit(pygame_surface, (0, 0))

    def draw(self, ctx):
        ctx = wyvern.save(ctx)

        ctx = wyvern.new_path(ctx)
        ctx = wyvern.move_to(ctx, 50, 50)
        ctx = wyvern.set_source_rgb(ctx, 0.0, 0.0, 0.0)
        ctx = wyvern.select_font_face(
            ctx, 'Tahoma', wyvern.FontWeight.NORMAL, wyvern.FontSlant.NORMAL
        )
        ctx = wyvern.set_font_size(ctx, 20)
        ctx = wyvern.text_path(ctx, 'test')
        ctx = wyvern.set_line_width(ctx, 2)
        ctx = wyvern.set_line_join(ctx, wyvern.LineJoin.ROUND)
        ctx = wyvern.arc(ctx, 75, 100, 20, 0, 2 * math.pi)
        ctx = wyvern.fill(ctx)
        ctx = wyvern.arc(ctx, 125, 100, 20, 0, 2 * math.pi)
        ctx = wyvern.arc(ctx, 175, 100, 20, 0, 3 * math.pi / 4)
        ctx = wyvern.set_source_rgb(ctx, 1.0, 0.0, 0.5)
        ctx = wyvern.arc(ctx, 175, 100, 20, math.pi, 3 * math.pi / 4)
        # ctx = wyvern.move_to(ctx, 200, 50)
        ctx = wyvern.rectangle(ctx, 200, 50, 20, 20)
        ctx = wyvern.stroke(ctx)

        ctx = wyvern.move_to(ctx, 50, 150)
        ctx = wyvern.select_font_face(
            ctx, 'Arial', wyvern.FontWeight.BOLD, wyvern.FontSlant.ITALIC
        )
        ctx = wyvern.text_path(ctx, 'test')
        ctx = wyvern.fill(ctx)

        # ctx = wyvern.move_to(ctx, 75, 200)
        ctx = wyvern.set_source_rgb(ctx, 0.5, 0.0, 1.0)
        ctx = wyvern.curve_to(ctx, 75, 200, 175, 250, 275, 200)
        # ctx = wyvern.set_dash(ctx, [7, 7])
        ctx = wyvern.stroke(ctx)

        ctx = wyvern.rectangle(ctx, 50, 300, 100, 50)
        ctx = wyvern.fill_preserve(ctx)
        # ctx = wyvern.clip(ctx)
        ctx = wyvern.arc(ctx, 200, 300, 20, math.pi, 3 * math.pi / 4)
        ctx = wyvern.stroke(ctx)

        # ctx = wyvern.rotate(ctx, math.pi / 4)
        # ctx = wyvern.translate(ctx, 400, -400)
        ctx = wyvern.rectangle(ctx, 50, 400, 100, 50)
        ctx = wyvern.transform(ctx, 0, 1, 1, 0, 0, 0)
        ctx = wyvern.stroke(ctx)

        gradient = wyvern.Gradient.LinearGradient(300, 300, 400, 400)

        # Add color stops (offset, r, g, b, alpha)
        ctx = wyvern.add_color_stop_rgba(ctx, 0.0, 1.0, 0.0, 0.0, 1.0)  # Start: Red
        ctx = wyvern.add_color_stop_rgba(ctx, 0.5, 0.0, 1.0, 0.0, 1.0)  # Middle: Green
        ctx = wyvern.add_color_stop_rgba(ctx, 1.0, 0.0, 0.0, 1.0, 1.0)  # End: Blue

        ctx = wyvern.set_source_gradient(ctx, gradient)
        ctx = wyvern.rectangle(ctx, 300, 300, 100, 100)
        ctx = wyvern.fill(ctx)

        gradient = wyvern.Gradient.RadialGradient(475, 100, 100)

        # Add color stops (offset, r, g, b, alpha)
        ctx = wyvern.add_color_stop_rgba(ctx, 0.0, 1.0, 0.0, 0.0, 1.0)  # Start: Red
        ctx = wyvern.add_color_stop_rgba(ctx, 0.5, 0.0, 1.0, 0.0, 1.0)  # Middle: Green
        ctx = wyvern.add_color_stop_rgba(ctx, 1.0, 0.0, 0.0, 1.0, 1.0)  # End: Blue

        ctx = wyvern.set_source_gradient(ctx, gradient)
        ctx = wyvern.arc(ctx, 475, 100, 100, 0, 2 * math.pi)
        ctx = wyvern.fill(ctx)

        ctx = wyvern.restore(ctx)
        # NEW
        return ctx

    def run(self):
        self._msPassed = 0
        self._refreshDelay = 60
        self._stepsPerSecond = 30

        clock = pygame.time.Clock()

        # Make antialiasing possible
        screen = pygame.display.set_mode((int(self.width), int(self.height)))
        wyvern_surface = wyvern.ImageSurface(int(self.width), int(self.height))
        ctx = wyvern_surface.canvas

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

            self.redrawAll(screen, wyvern_surface, ctx)
            pygame.display.flip()

        pygame.display.quit()
        pygame.quit()


def main():
    SandboxModal()


if __name__ == '__main__':
    main()
