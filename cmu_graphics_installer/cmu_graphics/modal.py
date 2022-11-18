import math
### ZIPFILE VERSION ###
import libs.cairo_loader as cairo
import libs.pygame_loader as pygame
### END ZIPFILE VERSION ###

import sys
import json
import os

def roundedrec(ctx,x,y,w,h,radius_x=5,radius_y=5):
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

    ctx.new_path()
    ctx.move_to(x + radius_x, y)
    ctx.rel_line_to(w - 2 * radius_x, 0.0)
    ctx.rel_curve_to(c1, 0.0, radius_x, c2, radius_x, radius_y)
    ctx.rel_line_to(0, h - 2 * radius_y)
    ctx.rel_curve_to(0.0, c2, c1 - radius_x, radius_y, -radius_x, radius_y)
    ctx.rel_line_to(-w + 2 * radius_x, 0)
    ctx.rel_curve_to(-c1, 0, -radius_x, -c2, -radius_x, -radius_y)
    ctx.rel_line_to(0, -h + 2 * radius_y)
    ctx.rel_curve_to(0.0, -c2, radius_x - c1, -radius_y, radius_x, -radius_y)
    ctx.close_path()

keyNameMap = { pygame.K_TAB: 'tab', pygame.K_RETURN: 'enter', pygame.K_BACKSPACE: 'backspace',
               pygame.K_DELETE: 'delete', pygame.K_ESCAPE: 'escape', pygame.K_SPACE: 'space',
               pygame.K_RIGHT: 'right', pygame.K_LEFT: 'left', pygame.K_UP: 'up', pygame.K_DOWN: 'down'}

shiftMap = { '1':'!', '2':'@', '3':'#', '4':'$', '5':'%', '6':'^', '7':'&', '8':'*',
             '9':'(', '0':')', '[':'{', ']':'}', '/':'?', '=':'+', '\\':'|', '\'':'"',
             ',':'<', '.':'>', '-':'_', ';':':', '`':'~' }

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
        self.font = ('Arial', cairo.FONT_WEIGHT_NORMAL, cairo.FONT_SLANT_NORMAL)
        self.textSize = 15
        self.padding = 4
        self.textAnchor = [
            self.left + self.padding,
            self.top + self.height - ((self.height - self.textSize) / 2)
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

    def get_left(self): return self.modal.left + self.modal.textXMargin
    left = property(get_left)
    def get_top(self): return self.modal.dividerY + self.modal.textYMargin
    top = property(get_top)
    def get_width(self): return self.modal.width - (2 * self.modal.textXMargin)
    width = property(get_width)

    def draw(self, ctx):
        if not self.active:
            ctx.rectangle(self.left, self.top, self.width, self.height)
            ctx.set_source_rgba(0.7, 0.7, 0.7, 1.0)
            ctx.set_line_width(1)
            ctx.stroke()
        else:
            roundedrec(ctx, self.left, self.top, self.width, self.height, 3, 3)
            ctx.set_source_rgba(0.9, 0.6, 0.4, 1.0)
            ctx.set_line_width(3)
            ctx.stroke()

        clipYMargin = 10
        ctx.save()
        ctx.rectangle(self.left + self.padding, self.top - clipYMargin, self.width - 2 * self.padding, self.top + self.height + 2 * clipYMargin)
        ctx.clip()

        cursorX = self.textAnchor[0] + self.getTextWidth(''.join(self.buf[:self.cursorPos])) + self.textOffset
        maxCursorX = self.left + self.width - self.padding
        minCursorX = self.left + self.padding
        cursorX = max(min(cursorX, maxCursorX), minCursorX)
        cursorTop = self.top + ((self.height - self.textSize) / 2) - 2
        cursorBottom = self.textAnchor[1] + 2

        if self.active and self.anchorPos is not None:
            anchorX = self.textAnchor[0] + self.getTextWidth(''.join(self.buf[:self.anchorPos])) + self.textOffset
            left = min(cursorX, anchorX)
            right = max(cursorX, anchorX)
            ctx.set_source_rgba(1.0, .85, .7)
            ctx.rectangle(left, cursorTop, right - left, cursorBottom - cursorTop)
            ctx.fill()

        elif self.active and self.cursorActive:
            ctx.set_source_rgba(0.0, 0.0, 0.0, 1.0)
            ctx.set_line_width(1)
            ctx.move_to(cursorX, cursorBottom)
            ctx.line_to(cursorX, cursorTop)
            ctx.stroke()

        ctx.move_to(self.textAnchor[0] + self.textOffset, self.textAnchor[1])
        ctx.select_font_face(*self.font)
        ctx.set_font_size(self.textSize)
        ctx.text_path(''.join(self.buf))
        ctx.set_source_rgba(0.0,0.0,0.0,1.0)
        ctx.fill()
        ctx.restore()

    def cursorPosFromCoord(self, x):
        if x <= self.textAnchor[0] + self.getTextWidth('') + self.textOffset:
            return 0

        for i in range(len(self.buf)):
            lowerX = self.textAnchor[0] + self.getTextWidth(''.join(self.buf[:i])) + self.textOffset
            upperX = self.textAnchor[0] + self.getTextWidth(''.join(self.buf[:i+1])) + self.textOffset
            if lowerX - 5 < x <= upperX - 5:
                return i

        return len(self.buf)

    def getTextWidth(self, text):
        ctx = self.modal.measureCtx
        ctx.save()
        ctx.select_font_face(*self.font)
        ctx.set_font_size(self.textSize)
        _, _, _, _, xAdvance, _ = ctx.text_extents(text)
        ctx.restore()
        return xAdvance

    def contains(self, x, y, checkYOnly = False):
        xInBounds = (self.left < x < self.left + self.width)
        yInBounds = (self.top < y < self.top + self.height)
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
            elif (data.timer is not None
                  and pygame.time.get_ticks() - data.timer > data.delay):
                data.timer = pygame.time.get_ticks()
                data.delay = 50
                if key == 'backspace': self.onBackSpace()
                elif key == 'left': self.onKeyLeft()
                elif key == 'right': self.onKeyRight()
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
            if self.cursorPos == 0: return
            self.buf = self.buf[:self.cursorPos-1] + self.buf[self.cursorPos:]
            self.cursorPos = max(0, self.cursorPos - 1)

    def onKeyRight(self):
        if self.anchorPos is not None:
            self.cursorPos = max(self.cursorPos, self.anchorPos)
            self.anchorPos = None
        else:
            self.cursorPos = min(self.cursorPos + 1, len(self.buf))

    def onKeyPress(self, keyCode, modifier):
        if not self.active: return
        # Punctuation, space, numbers, and letters
        if 31 < keyCode < 127:
            key = chr(keyCode)
            if (modifier & pygame.KMOD_SHIFT):
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
        cursorX = self.textAnchor[0] + self.getTextWidth(''.join(self.buf[:self.cursorPos])) + self.textOffset
        if cursorX > maxCursorX:
            self.textOffset -= (cursorX - maxCursorX)
        elif cursorX < minCursorX:
            self.textOffset += (minCursorX - cursorX)

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
                if self.anchorPos is None: self.anchorPos = self.cursorPos
                self.cursorPos = self.cursorPosFromCoord(pos[0])

class Button(object):
    def __init__(self, modal):
        self.modal = modal
        self.centerX = self.modal.width / 2
        self.padding = 10
        self.top = self.modal.textBox.top + self.modal.textBox.height + self.padding
        self.bottom = self.modal.height - self.padding
        self.height = self.bottom - self.top
        self.width = self.height * 1.2
        self.left = self.centerX - (self.width / 2)
        self.right = self.centerX + (self.width / 2)
        self.baseColor = (0.7, 0.6, .35, 1.0)
        self.hoverColor = (0.75, 0.7, 0.5, 1.0)
        self.color = self.baseColor
        self.font = ('Arial', cairo.FONT_WEIGHT_NORMAL, cairo.FONT_SLANT_NORMAL)
        self.textSize = 15
        self.text = 'OK'

    def draw(self, ctx):
        ctx.save()

        # Draw the rectangle
        ctx.set_source_rgba(*self.color)
        ctx.rectangle(self.left, self.top, self.width, self.height)
        ctx.fill()

        # Draw the label
        ctx.select_font_face(*self.font)
        ctx.set_font_size(self.textSize)
        ctx.set_source_rgba(1.0, 1.0, 1.0, 1.0)
        _, _, textWidth, textHeight, _, _ = ctx.text_extents(self.text)
        yPadding = (self.height - textHeight) / 2
        xPadding = (self.width - textWidth) / 2
        ctx.move_to(self.left + xPadding, self.bottom - yPadding)
        ctx.text_path(self.text)
        ctx.fill()

        ctx.restore()

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
    def __init__(self, title, prompt):
        self.title = title
        self.prompt = prompt

        self.centerX = 200
        self.width = 400
        self.top = 0
        self.left = self.centerX - (self.width / 2)
        self.right = self.left + self.width

        self.inputHeight = 100

        self.textXMargin = 15
        self.textYMargin = 18
        self.betweenLineMargin = 8
        self.textSize = 20
        self.shadowShift = 2

        self.active = True
        self.measureCtx = cairo.Context(cairo.ImageSurface(cairo.FORMAT_ARGB32, 0, 0))
        self.dividerY = self.drawPrompt(self.measureCtx, simulate = True) + self.textYMargin
        self.textBox = TextBox(self)
        self.button = Button(self)

        self.mouseIsDown = False

        pygame.display.set_caption(self.title)
        pygame.init()

        self.run()

    def get_height(self): return (self.dividerY - self.top) + self.inputHeight
    height = property(get_height)

    def redrawAll(self, screen, cairo_surface, ctx):
        self.draw(ctx)
        data_string = cairo_surface.get_data()
        pygame_surface = pygame.image.frombuffer(data_string, (int(self.width), int(self.height)), 'RGBA')
        screen.blit(pygame_surface, (0,0))

    def draw(self, ctx):
        ctx.save()

        self.drawBox(ctx)
        self.drawPrompt(ctx)
        self.textBox.draw(ctx)
        self.button.draw(ctx)

        ctx.restore()

    def drawDivider(self, ctx):
        ctx.set_source_rgba(0.8, 0.8, 0.8, 1.0)
        ctx.move_to(self.left, self.dividerY)
        ctx.line_to(self.right, self.dividerY)
        ctx.set_line_width(1)
        ctx.stroke()

    def drawBox(self, ctx):
        ctx.set_source_rgba(1.0,1.0,1.0,1.0)
        roundedrec(ctx, self.left, self.top, self.width, self.height, 0, 0)
        ctx.fill()

        self.drawDivider(ctx)

    def drawPrompt(self, ctx, simulate=False):
        ctx.select_font_face('Arial', cairo.FONT_WEIGHT_NORMAL, cairo.FONT_SLANT_NORMAL)
        ctx.set_font_size(self.textSize)

        promptWords = self.prompt.split()

        currTop = self.top + self.textYMargin
        currLeft = self.left + self.textXMargin

        _, _, _, lineHeight, _, _ = ctx.text_extents('|')

        for word in promptWords:
            word = word + ' '
            _, _, textWidth, textHeight, xAdvance, yAdvance = ctx.text_extents(word)

            if currLeft + xAdvance > self.width:
                currLeft = self.left + self.textXMargin
                currTop += lineHeight + self.betweenLineMargin

            ctx.new_path()
            ctx.move_to(currLeft, currTop + lineHeight)

            if not simulate:
                ctx.text_path(word)
                ctx.set_source_rgba(0.0,0.0,0.0,1.0)
                ctx.fill()

            currLeft += xAdvance

        return currTop + lineHeight

    def onStep(self):
        self.textBox.onStep()

    def execute(self):
        print(''.join(self.textBox.buf), end='')
        self.running = False

    def run(self):
        self._msPassed = 0
        self._refreshDelay = 60
        self._stepsPerSecond = 30

        clock = pygame.time.Clock()

        # Make antialiasing possible
        screen = pygame.display.set_mode((int(self.width),int(self.height)))
        cairo_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, int(self.width), int(self.height))
        ctx = cairo.Context(cairo_surface)

        self.running = True
        lastMousePosition = None
        while self.running:
            self._msPassed += clock.tick(self._refreshDelay)
            tickHadMouseDownEvent = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.button.onMousePress(event.pos)

                    if self.textBox.contains(*event.pos):
                        self.textBox.focus()
                    else:
                        self.textBox.active = False
                        self.cursorPos = None

                    if self.textBox.active:
                        lastMousePosition = event.pos
                        self.textBox.anchorPos = None
                        self.textBox.cursorPos = self.textBox.cursorPosFromCoord(event.pos[0])
                        tickHadMouseDownEvent = True
                        self.mouseIsDown = True
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    lastMousePosition = event.pos
                    self.mouseIsDown = False
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.button.onMouseMove(event.pos)
                    lastMousePosition = event.pos
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    # On drag
                    lastMousePosition = event.pos
                    tickHadMouseDownEvent = True
                    self.mouseIsDown = True
                    self.textBox.onMouseDrag(event.pos)
                elif event.type == pygame.KEYDOWN:
                    self.textBox.onKeyPress(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self.textBox.onKeyRelease(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    self.running = False

            if (self._msPassed > math.floor((1000 / self._stepsPerSecond)) or
                abs(self._msPassed - math.floor((1000 / self._stepsPerSecond))) < 10):
                self._msPassed = 0
                self.onStep()
                if self.mouseIsDown and not tickHadMouseDownEvent:
                    self.textBox.onMouseDrag(lastMousePosition)

            self.redrawAll(screen, cairo_surface, ctx)
            pygame.display.flip()

        pygame.display.quit()
        pygame.quit()

def main():
    request = json.loads(input())
    TextBoxModal(request['title'], request['prompt'])

if __name__ == '__main__':
    main()
