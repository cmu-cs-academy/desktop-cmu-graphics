import pygame
import wyvern


class Button(object):
    def __init__(self, modal):
        self.modal = modal
        self.centerX = self.modal.width / 2
        self.padding = 10
        if self.modal.textBox:
            self.top = self.modal.textBox.top + self.modal.textBox.height + self.padding
        else:
            self.top = self.modal.dividerY + self.modal.textYMargin
        self.bottom = self.modal.height - self.padding
        self.height = self.bottom - self.top
        self.width = self.height * 1.2
        self.left = self.centerX - (self.width / 2)
        self.right = self.centerX + (self.width / 2)
        self.baseColor = (179, 153, 89, 255)
        self.hoverColor = (191, 179, 128, 255)
        self.color = self.baseColor
        self.font = 'Arial'
        self.textSize = 15
        self.text = 'OK'

    def draw(self, ctx):
        ctx = wyvern.save(ctx)

        # Draw the rectangle
        ctx = wyvern.set_source_rgba(ctx, *self.color)
        ctx = wyvern.rectangle(ctx, self.left, self.top, self.width, self.height)
        ctx = wyvern.fill(ctx)

        # Draw the label
        ctx = wyvern.select_font_face(ctx, self.font)
        ctx = wyvern.set_font_size(ctx, self.textSize)
        ctx = wyvern.set_source_rgba(ctx, 255, 255, 255, 255)
        _, _, textWidth, textHeight, _, _ = wyvern.text_extents(ctx, self.text)
        yPadding = (self.height - textHeight) / 2
        xPadding = (self.width - textWidth) / 2
        ctx = wyvern.move_to(ctx, self.left + xPadding, self.bottom - yPadding)
        ctx = wyvern.text_path(ctx, self.text)
        ctx = wyvern.fill(ctx)

        ctx = wyvern.restore(ctx)

    def contains(self, x, y):
        xInBounds = self.left <= x <= self.right
        yInBounds = self.top <= y <= self.bottom
        return xInBounds and yInBounds

    def onMouseMove(self, pos):
        if self.contains(*pos):
            self.color = self.hoverColor
        else:
            self.color = self.baseColor

    def onMousePress(self, pos):
        if self.contains(*pos):
            self.modal.execute()


class TextBoxModal(object):
    def __init__(self):
        self.title = 'title'

        self.centerX = 200
        self.width = 400
        self.top = 0
        self.left = self.centerX - (self.width / 2)
        self.right = self.left + self.width

        self.inputHeight = 70

        self.textXMargin = 15
        self.textYMargin = 18
        self.betweenLineMargin = 8
        self.textSize = 20
        self.shadowShift = 2

        self.active = True
        # can't make a surface whose dimensions are zero
        self.measureCtx = wyvern.ImageSurface(100, 100).canvas
        self.dividerY = (
            self.drawPrompt(self.measureCtx, simulate=True) + self.textYMargin
        )
        self.button = Button(self)

        self.mouseIsDown = False

        pygame.display.set_caption(self.title)
        pygame.init()

        self.run()

    def get_height(self):
        return (self.dividerY - self.top) + self.inputHeight

    height = property(get_height)

    def redrawAll(self, screen, wyvern_surface, ctx):
        self.draw(ctx)
        data_string = wyvern_surface.data
        print(data_string)
        pygame_surface = pygame.image.frombuffer(
            data_string, (int(self.width), int(self.height)), 'RGBA'
        )
        screen.blit(pygame_surface, (0, 0))

    def draw(self, ctx):
        ctx = wyvern.save(ctx)

        self.drawBox(ctx)
        self.drawPrompt(ctx)
        if self.textBox:
            self.textBox.draw(ctx)
        self.button.draw(ctx)

        ctx = wyvern.restore(ctx)

    def drawDivider(self, ctx):
        ctx = wyvern.set_source_rgba(ctx, 204, 204, 204, 255)
        ctx = wyvern.move_to(ctx, self.left, self.dividerY)
        ctx = wyvern.line_to(ctx, self.right, self.dividerY)
        ctx = wyvern.set_line_width(ctx, 1)
        ctx = wyvern.stroke(ctx)

    def drawBox(self, ctx):
        ctx = wyvern.set_source_rgba(ctx, 255, 255, 255, 255)
        ctx = roundedrec(ctx, self.left, self.top, self.width, self.height, 0, 0)
        ctx = wyvern.fill(ctx)

        self.drawDivider(ctx)

    def drawPrompt(self, ctx, simulate=False):
        ctx = wyvern.select_font_face(ctx, 'Arial')
        ctx = wyvern.set_font_size(ctx, self.textSize)

        promptWords = self.prompt.split()

        currTop = self.top + self.textYMargin
        currLeft = self.left + self.textXMargin

        _, _, _, lineHeight, _, _ = wyvern.text_extents(ctx, '|')

        for word in promptWords:
            word = word + ' '
            _, _, textWidth, textHeight, xAdvance, yAdvance = wyvern.text_extents(
                ctx, word
            )

            if currLeft + xAdvance > self.width:
                currLeft = self.left + self.textXMargin
                currTop += lineHeight + self.betweenLineMargin

            ctx = wyvern.new_path(ctx)
            ctx = wyvern.move_to(ctx, currLeft, currTop + lineHeight)

            if not simulate:
                ctx = wyvern.text_path(ctx, word)
                ctx = wyvern.set_source_rgba(ctx, 0, 0, 0, 255)
                ctx = wyvern.fill(ctx)

            currLeft += xAdvance

        return currTop + lineHeight

    def onStep(self):
        if self.textBox:
            self.textBox.onStep()

    def execute(self):
        if self.textBox:
            print(''.join(self.textBox.buf), end='')
        self.running = False

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
        lastMousePosition = None
        while self.running:
            self._msPassed += clock.tick(self._refreshDelay)
            tickHadMouseDownEvent = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.button.onMousePress(event.pos)

                    if self.textBox:
                        if self.textBox.contains(*event.pos):
                            self.textBox.focus()
                        else:
                            self.textBox.active = False
                            self.cursorPos = None

                        if self.textBox.active:
                            lastMousePosition = event.pos
                            self.textBox.anchorPos = None
                            self.textBox.cursorPos = self.textBox.cursorPosFromCoord(
                                event.pos[0]
                            )
                            tickHadMouseDownEvent = True
                            self.mouseIsDown = True
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    lastMousePosition = event.pos
                    self.mouseIsDown = False
                elif event.type == pygame.MOUSEMOTION and event.buttons == (0, 0, 0):
                    self.button.onMouseMove(event.pos)
                    lastMousePosition = event.pos
                elif event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                    # On drag
                    lastMousePosition = event.pos
                    tickHadMouseDownEvent = True
                    self.mouseIsDown = True
                    if self.textBox:
                        self.textBox.onMouseDrag(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if self.textBox:
                        self.textBox.onKeyPress(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    if self.textBox:
                        self.textBox.onKeyRelease(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    self.running = False

            if (
                self._msPassed > math.floor((1000 / self._stepsPerSecond))
                or abs(self._msPassed - math.floor((1000 / self._stepsPerSecond))) < 10
            ):
                self._msPassed = 0
                self.onStep()
                if self.textBox and self.mouseIsDown and not tickHadMouseDownEvent:
                    self.textBox.onMouseDrag(lastMousePosition)

            self.redrawAll(screen, wyvern_surface, ctx)
            pygame.display.flip()

        pygame.display.quit()
        pygame.quit()


def main():
    request = json.loads(input())
    TextBoxModal(request['title'], request['prompt'], request['getInput'])


if __name__ == '__main__':
    main()
