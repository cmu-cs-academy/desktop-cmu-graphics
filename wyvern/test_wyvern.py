import math

import wyvern
import pygame
from io import BytesIO
import os
import ssl
import urllib.request


def webrequestget(path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',
    }
    request = urllib.request.Request(path, headers=headers)
    # This is the October 2025 certifi cacert.pem
    cafile_path = os.path.join(os.path.dirname(__file__), 'cacert.pem')
    context = ssl.create_default_context(cafile=cafile_path)
    response = urllib.request.urlopen(request, context=context)
    return response


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

    def loadImageFromStringReference(self, reference):
        if reference.startswith('http'):
            # reference is a url
            try:
                response = webrequestget(reference)
                image = pygame.image.load(BytesIO(response.read()))
            except Exception:
                Exception('Failed to load image data')
        else:
            # reference is a path
            image = pygame.image.load(reference)
        return image

    def wyvernImageFromPygameSurface(self, pygameSurface):
        a = pygame.image.tobytes(pygameSurface, 'RGBA')
        width, height = pygameSurface.get_size()
        return (bytearray(a), width, height, 4 * width)

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

        image = self.loadImageFromStringReference(
            'https://academy.cs.cmu.edu/static/media/project_10.472f439f.jpg'
        )
        params = self.wyvernImageFromPygameSurface(image)

        ctx = wyvern.set_source_image(ctx, *params, 400, 400)

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
