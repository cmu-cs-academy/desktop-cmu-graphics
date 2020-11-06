import sys
from cmu_graphics import *

def centerCrop(frame):
    width, height = frame.size
    centerX = width // 2
    centerY = height // 2
    return frame.crop(
        (centerX - 200, centerY - 200, centerX + 200, centerY + 200)
    )

def getCameraFrame():
    getFrameErrored = False

    try:
        _, frame = app.cam.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
    except:
        getFrameErrored = True

    if getFrameErrored:
        raise Exception('Unable to capture frame from camera')

    return centerCrop(frame)

def drawBlock(frame, row, col, blockSize):
    totalR, totalG, totalB = 0, 0, 0
    pixelCount = 0
    for x in range(col * blockSize, (col+1) * blockSize):
        for y in range(row * blockSize, (row+1) * blockSize):
            r, g, b = frame.getpixel((x, y))
            totalR += r
            totalG += g
            totalB += b
            pixelCount += 1

    circleRadius = blockSize // 2
    circleX = (col * blockSize) + circleRadius
    circleY = (row * blockSize) + circleRadius
    averageRGB = rgb(totalR // pixelCount,
                  totalG // pixelCount,
                  totalB // pixelCount)
    Circle(circleX, circleY, circleRadius, fill=averageRGB)

def frameToPoints(frame, blockSize):
    numBlocks = 400 // blockSize
    for row in range(numBlocks):
        for col in range(numBlocks):
            drawBlock(frame, row, col, blockSize)

def drawText(linesList):
    lineHeight = 30
    lineX = 200 - ((len(linesList) * lineHeight) // 2)
    for line in linesList:
        Label(line, 200, lineX, align='center', size=20)
        lineX += lineHeight

def loadLibraries():
    import cv2
    from PIL import Image
    globals()['cv2'] = cv2
    globals()['Image'] = Image

def startCamera():
    app.cam = cv2.VideoCapture(0)
    app.stepsPerSecond = 5

def onStep():
    if app.mode == 'running':
        app.group.clear()
        frame = getCameraFrame()
        frameToPoints(frame, 16)

def loadModules():
    import cv2
    from PIL import Image
    globals()['cv2'] = cv2
    globals()['Image'] = Image

def start():
    try:
        loadModules()
        app.mode = 'running'
        startCamera()
    except:
        drawText([
            'This program requires OpenCV and PIL.',
            'These are third party libraries which can',
            'be installed by running the command',
            'printed to the console in the application',
            '"Command Prompt".' if sys.platform == 'win32' else '"Terminal".',
        ])
        if sys.platform == 'win32':
            print('"%s" -m pip install opencv-python pillow' % sys.executable)
        else:
            print('sudo "%s" -m pip install opencv-python pillow' % sys.executable)
        app.mode = 'helpText'

start()

cmu_graphics.loop()
