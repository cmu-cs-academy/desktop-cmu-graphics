import math

### ZIPFILE VERSION ###
# import libs.pygame_loader as pygame
# import libs.cmu_graphics_helpers_loader as cmu_graphics_helpers

### END ZIPFILE VERSION ###
### PYPI VERSION ###
# import pygame

### END PYPI VERSION ###
from cmu_graphics_helpers import wyvern
import json

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

# winit's logical_key.to_text() already returns the human-readable
# character (e.g. 'a', '1', '\t' for tab), so most translation from
# pygame keycodes is no longer needed. Only named (non-printable) keys
# need remapping.
NAMED_KEY_MAP = {
    '\t': 'tab',
    '\r': 'enter',
    '\x08': 'backspace',
    '\x7f': 'delete',
    '\x1b': 'escape',
    ' ': 'space',
}

def nowMs():
    import time
    return time.monotonic() * 1000

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
        self.cursorTimer = nowMs()
        self.blinkDelay = 400
        self.font = ('Arial', wyvern.FontWeight.NORMAL, wyvern.FontSlant.NORMAL)
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
        self.cursorTimer = nowMs()

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
            ctx.rectangle(self.left, self.top, self.width, self.height)
            ctx.set_source_rgba(0.7, 0.7, 0.7, 1.0)
            ctx.set_line_width(1)
            ctx.stroke()
        else:
            ctx.round_rectangle(self.left, self.top, self.width, self.height, 3, 3)
            ctx.set_source_rgba(0.9, 0.6, 0.4, 1.0)
            ctx.set_line_width(3)
            ctx.stroke()

        clipYMargin = 10
        ctx.save()
        ctx.rectangle(
            self.left + self.padding,
            self.top - clipYMargin,
            self.width - 2 * self.padding,
            self.top + self.height + 2 * clipYMargin,
        )
        ctx.clip()

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
            ctx.set_source_rgba(1.0, 0.85, 0.7)
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
        ctx.set_source_rgba(0.0, 0.0, 0.0, 1.0)
        ctx.fill()
        ctx.restore()

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
        ctx.save()
        ctx.select_font_face(*self.font)
        ctx.set_font_size(self.textSize)
        _, _, _, _, xAdvance, _ = ctx.text_extents(text)
        ctx.restore()
        return xAdvance

    def contains(self, x, y, checkYOnly=False):
        xInBounds = self.left < x < self.left + self.width
        yInBounds = self.top < y < self.top + self.height
        return (xInBounds or checkYOnly) and (yInBounds)

    def onStep(self):
        if nowMs() - self.cursorTimer > self.blinkDelay:
            self.cursorActive = not self.cursorActive
            self.cursorTimer = nowMs()
        for key in self.keysHeldData:
            data = self.keysHeldData[key]
            if data.timer is None and data.isDown:
                data.timer = nowMs()
                data.delay = 400
            elif (
                data.timer is not None
                and nowMs() - data.timer > data.delay
            ):
                data.timer = nowMs()
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

    def onKeyPress(self, key, modifiers):
        if not self.active:
            return

        k = NAMED_KEY_MAP.get(key)

        if k is None and len(key) == 1:
            # printable character — winit already applies shift for us,
            # but we replicate the old shiftMap only for symbols that
            # to_text() might not shift consistently across platforms
            if 'control' in modifiers or 'meta' in modifiers:
                return
            if self.anchorPos is not None:
                self.onBackSpace()
            self.buf.insert(self.cursorPos, key)
            self.cursorPos += 1
        else:
            if k == 'left':
                self.onKeyLeft()
            elif k == 'right':
                self.onKeyRight()
            elif k == 'backspace':
                self.onBackSpace()
            elif k == 'up':
                self.anchorPos = None
                self.cursorPos = 0
            elif k == 'down':
                self.anchorPos = None
                self.cursorPos = len(self.buf)
            elif k == 'enter':
                self.modal.execute()
            if k not in self.keysHeldData:
                self.keysHeldData[k] = KeyHoldData()
            self.keysHeldData[k].isDown = True
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

    def onKeyRelease(self, key, modifiers):
        namedKey = NAMED_KEY_MAP.get(key)
        if namedKey is not None and namedKey in self.keysHeldData:
            data = self.keysHeldData[namedKey]
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
        self.baseColor = (0.7, 0.6, 0.35, 1.0)
        self.hoverColor = (0.75, 0.7, 0.5, 1.0)
        self.color = self.baseColor
        self.font = ('Arial', wyvern.FontWeight.NORMAL, wyvern.FontSlant.NORMAL)
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
        dividerY = self.drawPrompt(self.measureCtx, simulate=True)
        self.dividerY = dividerY + self.textYMargin
        self.textBox = TextBox(self) if getInput else None
        self.button = Button(self)

        self.mouseIsDown = False
        self.lastMousePosition = None
        self.running = True

        print(vars(wyvern))
        wyvern.run(self.on_event)

    def get_height(self):
        return (self.dividerY - self.top) + self.inputHeight

    height = property(get_height)

    def draw(self, ctx):
        ctx.save()

        self.drawBox(ctx)
        self.drawPrompt(ctx)
        if self.textBox:
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
        ctx.set_source_rgba(1.0, 1.0, 1.0, 1.0)
        ctx.round_rectangle(self.left, self.top, self.width, self.height, 0, 0)
        ctx.fill()

        self.drawDivider(ctx)

    def drawPrompt(self, ctx, simulate=False):
        ctx.select_font_face('Arial', wyvern.FontWeight.NORMAL, wyvern.FontSlant.NORMAL)
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
                ctx.set_source_rgba(0.0, 0.0, 0.0, 1.0)
                ctx.fill()

            currLeft += xAdvance

        return currTop + lineHeight

    def onStep(self):
        if self.textBox:
            self.textBox.onStep()
            if self.mouseIsDown and self.lastMousePosition:
                self.textBox.onMouseDrag(self.lastMousePosition)

    def execute(self):
        if self.textBox:
            print(''.join(self.textBox.buf), end='')
        # self.running = False
        # # There's no explicit "close window" call exposed from wyvern.run
        # # yet, so print + os._exit is the simplest way to terminate cleanly
        # # once the parent process has read stdout.
        # import os
        # os._exit(0)

    def on_event(self, event, surface):
        ctx = surface.canvas

        if event.event_type == 'step':
            self.onStep()

        elif event.event_type == 'init' or event.event_type == 'redraw':
            self.draw(ctx)

        elif event.event_type == 'mouse_press':
            pos = (event.mouse.x, event.mouse.y)
            if event.mouse.button == 0:  # left button
                self.button.onMousePress(pos)
                if self.textBox:
                    if self.textBox.contains(*pos):
                        self.textBox.focus()
                    else:
                        self.textBox.active = False
                    if self.textBox.active:
                        self.lastMousePosition = pos
                        self.textBox.anchorPos = None
                        self.textBox.cursorPos = self.textBox.cursorPosFromCoord(pos[0])
                        self.mouseIsDown = True

        elif event.event_type == 'mouse_release':
            if event.mouse.button == 0:
                self.lastMousePosition = (event.mouse.x, event.mouse.y)
                self.mouseIsDown = False

        elif event.event_type == 'mouse_move':
            pos = (event.mouse.x, event.mouse.y)
            self.button.onMouseMove(pos)
            if not self.mouseIsDown:
                self.lastMousePosition = pos

        elif event.event_type == 'key_press':
            if self.textBox:
                self.textBox.onKeyPress(event.key.key, event.key.modifiers)

        elif event.event_type == 'key_release':
            if self.textBox:
                self.textBox.onKeyRelease(event.key.key, event.key.modifiers)


def main():
    request = json.loads(input())
    TextBoxModal(request['title'], request['prompt'], request['getInput'])


if __name__ == '__main__':
    main()