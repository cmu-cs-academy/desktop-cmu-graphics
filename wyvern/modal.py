import math

### ZIPFILE VERSION ###
# import libs.pygame_loader as pygame

### END ZIPFILE VERSION ###
### PYPI VERSION ###
import wyvern
import pygame

### END PYPI VERSION ###
import json


def roundedrec(ctx, x, y, w, h, radius_x=5, radius_y=5):
    # from mono moonlight aka mono silverlight
    # test limits (without using multiplications)
    # http://graphics.stanford.edu/courses/cs248-98-fall/Final/q1.html
    ARC_TO_BEZIER = 0.55228475
    if radius_x > w - radius_x:
        radius_x = w / 2
    if radius_y > h - radius_y:
        radius_y = h / 2

    # approximate (quite close) the arc using a bezier curve
    c1 = ARC_TO_BEZIER * radius_x
    c2 = ARC_TO_BEZIER * radius_y

    ctx = wyvern.new_path(ctx)
    ctx = wyvern.move_to(ctx, x + radius_x, y)
    ctx = wyvern.rel_line_to(ctx, w - 2 * radius_x, 0.0)
    ctx = wyvern.rel_curve_to(ctx, c1, 0.0, radius_x, c2, radius_x, radius_y)
    ctx = wyvern.rel_line_to(ctx, 0, h - 2 * radius_y)
    ctx = wyvern.rel_curve_to(
        ctx, 0.0, c2, c1 - radius_x, radius_y, -radius_x, radius_y
    )
    ctx = wyvern.rel_line_to(ctx, -w + 2 * radius_x, 0)
    ctx = wyvern.rel_curve_to(ctx, -c1, 0, -radius_x, -c2, -radius_x, -radius_y)
    ctx = wyvern.rel_line_to(ctx, 0, -h + 2 * radius_y)
    ctx = wyvern.rel_curve_to(
        ctx, 0.0, -c2, radius_x - c1, -radius_y, radius_x, -radius_y
    )
    ctx = wyvern.close_path(ctx)
    return ctx


keyNameMap = {
    pygame.K_TAB: 'tab',
    pygame.K_RETURN: 'enter',
    pygame.K_BACKSPACE: 'backspace',
    pygame.K_DELETE: 'delete',
    pygame.K_ESCAPE: 'escape',
    pygame.K_SPACE: 'space',
    pygame.K_RIGHT: 'right',
    pygame.K_LEFT: 'left',
    pygame.K_UP: 'up',
    pygame.K_DOWN: 'down',
}

shiftMap = {
    '1': '!',
    '2': '@',
    '3': '#',
    '4': '$',
    '5': '%',
    '6': '^',
    '7': '&',
    '8': '*',
    '9': '(',
    '0': ')',
    '[': '{',
    ']': '}',
    '/': '?',
    '=': '+',
    '\\': '|',
    "'": '"',
    ',': '<',
    '.': '>',
    '-': '_',
    ';': ':',
    '`': '~',
}


class KeyHoldData(object):
    def __init__(self):
        self.isDown = False
        self.timer = None
        self.delay = 400


class TextBox(object):
    def __init__(self, modal):
        self.modal = modal
        self.height = 25
        self.cursorActive = True
        self.cursorTimer = pygame.time.get_ticks()
        self.blinkDelay = 400
        self.font = 'Arial'
        self.textSize = 15
        self.padding = 4
        self.textAnchor = [
            self.left + self.padding,
            self.top + self.height - ((self.height - self.textSize) / 2),
        ]
        self.textOffset = 0
        self.active = True
        self.buf = []
        self.cursorPos = 0
        self.anchorPos = None
        self.keysHeldData = dict()

    def focus(self):
        self.active = True
        self.cursorActive = True
        self.cursorTimer = pygame.time.get_ticks()

    def get_left(self):
        return self.modal.left + self.modal.textXMargin

    left = property(get_left)

    def get_top(self):
        return self.modal.dividerY + self.modal.textYMargin

    top = property(get_top)

    def get_width(self):
        return self.modal.width - (2 * self.modal.textXMargin)

    width = property(get_width)

    def draw(self, ctx):
        if not self.active:
            ctx = wyvern.rectangle(ctx, self.left, self.top, self.width, self.height)
            ctx = wyvern.set_source_rgba(ctx, 179, 179, 179, 255)
            ctx = wyvern.set_line_width(ctx, 1)
            ctx = wyvern.stroke(ctx)
        else:
            ctx = roundedrec(ctx, self.left, self.top, self.width, self.height, 3, 3)
            ctx = wyvern.set_source_rgba(ctx, 230, 153, 102, 255)
            ctx = wyvern.set_line_width(ctx, 3)
            ctx = wyvern.stroke(ctx)

        clipYMargin = 10
        ctx = wyvern.save(ctx)
        ctx = wyvern.rectangle(
            ctx,
            self.left + self.padding,
            self.top - clipYMargin,
            self.width - 2 * self.padding,
            self.top + self.height + 2 * clipYMargin,
        )
        ctx = wyvern.clip(ctx)

        cursorX = (
            self.textAnchor[0]
            + self.getTextWidth(''.join(self.buf[: self.cursorPos]))
            + self.textOffset
        )
        maxCursorX = self.left + self.width - self.padding
        minCursorX = self.left + self.padding
        cursorX = max(min(cursorX, maxCursorX), minCursorX)
        cursorTop = self.top + ((self.height - self.textSize) / 2) - 2
        cursorBottom = self.textAnchor[1] + 2

        if self.active and self.anchorPos is not None:
            anchorX = (
                self.textAnchor[0]
                + self.getTextWidth(''.join(self.buf[: self.anchorPos]))
                + self.textOffset
            )
            left = min(cursorX, anchorX)
            right = max(cursorX, anchorX)
            ctx = wyvern.set_source_rgba(ctx, 255, 217, 179)
            ctx = wyvern.rectangle(
                ctx, left, cursorTop, right - left, cursorBottom - cursorTop
            )
            ctx = wyvern.fill(ctx)

        elif self.active and self.cursorActive:
            ctx = wyvern.set_source_rgba(ctx, 0, 0, 0, 255)
            ctx = wyvern.set_line_width(ctx, 1)
            ctx = wyvern.move_to(ctx, cursorX, cursorBottom)
            ctx = wyvern.line_to(ctx, cursorX, cursorTop)
            ctx = wyvern.stroke(ctx)

        ctx = wyvern.move_to(
            ctx, self.textAnchor[0] + self.textOffset, self.textAnchor[1]
        )
        ctx = wyvern.select_font_face(ctx, self.font)
        ctx = wyvern.set_font_size(ctx, self.textSize)
        ctx = wyvern.text_path(ctx, ''.join(self.buf))
        ctx = wyvern.set_source_rgba(ctx, 0, 0, 0, 255)
        ctx = wyvern.fill(ctx)
        ctx = wyvern.restore(ctx)
        # NEW
        return ctx

    def cursorPosFromCoord(self, x):
        if x <= self.textAnchor[0] + self.getTextWidth('') + self.textOffset:
            return 0

        for i in range(len(self.buf)):
            lowerX = (
                self.textAnchor[0]
                + self.getTextWidth(''.join(self.buf[:i]))
                + self.textOffset
            )
            upperX = (
                self.textAnchor[0]
                + self.getTextWidth(''.join(self.buf[: i + 1]))
                + self.textOffset
            )
            if lowerX - 5 < x <= upperX - 5:
                return i

        return len(self.buf)

    def getTextWidth(self, text):
        if len(text) <= 0:
            return 0
        ctx = self.modal.measureCtx
        ctx = wyvern.save(ctx)
        ctx = wyvern.select_font_face(ctx, self.font)
        ctx = wyvern.set_font_size(ctx, self.textSize)
        _, _, _, _, xAdvance, _ = wyvern.text_extents(ctx, text)
        ctx = wyvern.restore(ctx)
        return xAdvance

    def contains(self, x, y, checkYOnly=False):
        xInBounds = self.left < x < self.left + self.width
        yInBounds = self.top < y < self.top + self.height
        return (xInBounds or checkYOnly) and (yInBounds)

    def onStep(self):
        if pygame.time.get_ticks() - self.cursorTimer > self.blinkDelay:
            self.cursorActive = not self.cursorActive
            self.cursorTimer = pygame.time.get_ticks()
        for key in self.keysHeldData:
            data = self.keysHeldData[key]
            if data.timer is None and data.isDown:
                data.timer = pygame.time.get_ticks()
                data.delay = 400
            elif (
                data.timer is not None
                and pygame.time.get_ticks() - data.timer > data.delay
            ):
                data.timer = pygame.time.get_ticks()
                data.delay = 50
                if key == 'backspace':
                    self.onBackSpace()
                elif key == 'left':
                    self.onKeyLeft()
                elif key == 'right':
                    self.onKeyRight()
        self.resetTextOffset()

    def onKeyLeft(self):
        if self.anchorPos is not None:
            self.cursorPos = min(self.anchorPos, self.cursorPos)
            self.anchorPos = None
        else:
            self.cursorPos = max(0, self.cursorPos - 1)

    def onBackSpace(self):
        if self.anchorPos is not None:
            lower = min(self.anchorPos, self.cursorPos)
            upper = max(self.anchorPos, self.cursorPos)
            del self.buf[lower:upper]
            self.cursorPos = lower
            self.anchorPos = None
        else:
            if self.cursorPos == 0:
                return
            self.buf = self.buf[: self.cursorPos - 1] + self.buf[self.cursorPos :]
            self.cursorPos = max(0, self.cursorPos - 1)

    def onKeyRight(self):
        if self.anchorPos is not None:
            self.cursorPos = max(self.cursorPos, self.anchorPos)
            self.anchorPos = None
        else:
            self.cursorPos = min(self.cursorPos + 1, len(self.buf))

    def onKeyPress(self, keyCode, modifier):
        if not self.active:
            return
        # Punctuation, space, numbers, and letters
        if 31 < keyCode < 127:
            key = chr(keyCode)
            if modifier & pygame.KMOD_SHIFT:
                key = shiftMap.get(key, key).upper()

            if (modifier & pygame.KMOD_CTRL) or (modifier & pygame.KMOD_LMETA):
                return

            if self.anchorPos is not None:
                self.onBackSpace()
            self.buf.insert(self.cursorPos, key)
            self.cursorPos += 1
        else:
            key = keyNameMap.get(keyCode, None)
            if key == 'left':
                self.onKeyLeft()
            elif key == 'right':
                self.onKeyRight()
            elif key == 'backspace':
                self.onBackSpace()
            elif key == 'up':
                self.anchorPos = None
                self.cursorPos = 0
            elif key == 'down':
                self.anchorPos = None
                self.cursorPos = len(self.buf)
            elif key == 'enter':
                self.modal.execute()
            if key not in self.keysHeldData:
                self.keysHeldData[key] = KeyHoldData()
            self.keysHeldData[key].isDown = True
            self.resetTextOffset()

    def resetTextOffset(self):
        maxCursorX = self.left + self.width - self.padding
        minCursorX = self.left + self.padding
        cursorX = (
            self.textAnchor[0]
            + self.getTextWidth(''.join(self.buf[: self.cursorPos]))
            + self.textOffset
        )
        if cursorX > maxCursorX:
            self.textOffset -= cursorX - maxCursorX
        elif cursorX < minCursorX:
            self.textOffset += minCursorX - cursorX

    def onKeyRelease(self, keyCode, mod):
        key = keyNameMap.get(keyCode, None)
        if key is not None and key in self.keysHeldData:
            data = self.keysHeldData[key]
            data.isDown = False
            data.delay = 400
            data.timer = None

    def onMouseDrag(self, pos):
        if self.active and self.cursorPos is not None:
            if self.contains(*pos, checkYOnly=True):
                if self.anchorPos is None:
                    self.anchorPos = self.cursorPos
                self.cursorPos = self.cursorPosFromCoord(pos[0])


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

        return ctx

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
    def __init__(self, title, prompt, getInput):
        self.title = title
        self.prompt = prompt

        self.centerX = 200
        self.width = 400
        self.top = 0
        self.left = self.centerX - (self.width / 2)
        self.right = self.left + self.width

        self.inputHeight = 100 if getInput else 70

        self.textXMargin = 15
        self.textYMargin = 18
        self.betweenLineMargin = 8
        self.textSize = 20
        self.shadowShift = 2

        self.active = True
        # can't make a surface whose dimensions are zero
        self.measureCtx = wyvern.ImageSurface(100, 100).canvas
        dividerY, ctx = self.drawPrompt(self.measureCtx, simulate=True)
        self.dividerY = dividerY + self.textYMargin
        self.measureCtx = ctx
        self.textBox = TextBox(self) if getInput else None
        self.button = Button(self)

        self.mouseIsDown = False

        pygame.display.set_caption(self.title)
        pygame.init()

        self.run()

    def get_height(self):
        return (self.dividerY - self.top) + self.inputHeight

    height = property(get_height)

    def redrawAll(self, screen, wyvern_surface, ctx):
        ctx = self.draw(ctx)
        data_string = wyvern_surface.data
        pygame_surface = pygame.image.frombuffer(
            data_string, (int(self.width), int(self.height)), 'RGBA'
        )
        screen.blit(pygame_surface, (0, 0))

    def draw(self, ctx):
        ctx = wyvern.save(ctx)

        ctx = self.drawBox(ctx)
        _, ctx = self.drawPrompt(ctx)
        if self.textBox:
            ctx = self.textBox.draw(ctx)
        ctx = self.button.draw(ctx)

        ctx = wyvern.restore(ctx)
        # NEW
        return ctx

    def drawDivider(self, ctx):
        ctx = wyvern.set_source_rgba(ctx, 204, 204, 204, 255)
        ctx = wyvern.move_to(ctx, self.left, self.dividerY)
        ctx = wyvern.line_to(ctx, self.right, self.dividerY)
        ctx = wyvern.set_line_width(ctx, 1)
        ctx = wyvern.stroke(ctx)
        # NEW
        return ctx

    def drawBox(self, ctx):
        ctx = wyvern.set_source_rgba(ctx, 255, 255, 255, 255)
        ctx = roundedrec(ctx, self.left, self.top, self.width, self.height, 0, 0)
        ctx = wyvern.fill(ctx)

        ctx = self.drawDivider(ctx)
        # NEW
        return ctx

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

        return currTop + lineHeight, ctx

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
