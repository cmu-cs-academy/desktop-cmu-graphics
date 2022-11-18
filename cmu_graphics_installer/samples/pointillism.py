from cmu_graphics import *
import sys

# This function takes in a frame (a PIL image) and crops it so the center
# of the cropped 400 by 400 image is the center of the orginal image
def centerCrop(frame):
    # frame.size is the width and height of the frame in pixels
    width, height = frame.size
    centerX = width // 2
    centerY = height // 2

    # The PIL image crop function takes in a (left, top, right ,bottom)
    # bounding box
    return frame.crop(
        (centerX - 200, centerY - 200, centerX + 200, centerY + 200)
    )

# This function uses OpenCV to grab a frame from your computer's camera
# and crops it to canvas size.
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

# Given the row and column of one of our circle, calculate the average
# color of the image in that area, then draw a circle with that color
def drawBlock(frame, row, col, blockSize):
    totalR, totalG, totalB = 0, 0, 0
    pixelCount = 0

    # These nested loops loop over every pixel in the current circle's area
    for x in range(col * blockSize, (col+1) * blockSize):
        for y in range(row * blockSize, (row+1) * blockSize):
            r, g, b = frame.getpixel((x, y))
            totalR += r
            totalG += g
            totalB += b
            pixelCount += 1

    # Calculate the average color across all pixels
    averageRGB = rgb(totalR // pixelCount,
                  totalG // pixelCount,
                  totalB // pixelCount)

    # And draw the circle
    circleRadius = blockSize // 2
    circleX = (col * blockSize) + circleRadius
    circleY = (row * blockSize) + circleRadius
    Circle(circleX, circleY, circleRadius, fill=averageRGB)

# This function takes in a frame (a PIL image) and a "block size" describing
# the size of the circles to draw. If the blockSize was 200, we would split
# the screen into four 200x200 blocks, and draw four circles
def frameToPoints(frame, blockSize):
    numBlocks = 400 // blockSize
    for row in range(numBlocks):
        for col in range(numBlocks):
            drawBlock(frame, row, col, blockSize)

# A helper function for drawing text centered on the screen
def drawText(linesList):
    lineHeight = 30
    # lineY starts out at the center (200) minus half the height of our
    # whole block of text
    lineY = 200 - ((len(linesList) * lineHeight) // 2)
    for line in linesList:
        # Create a label for each line, and move lineY down so the next
        # line is drawn lower
        Label(line, 200, lineY, align='center', size=20)
        lineY += lineHeight

# Turns on the user's webcam, begins capturing video, and sets how many frames
# to process per second
def startCamera():
    app.cam = cv2.VideoCapture(0)
    app.stepsPerSecond = 5

# While we're running, clear the current drawing, get a frame from the camera,
# and draw that frame as a set of circles
def onStep():
    if app.mode == 'running':
        app.group.clear()
        frame = getCameraFrame()
        frameToPoints(frame, 16)

# This function loads the third party libraries OpenCV and Pillow, and adds
# them to the global namespace so we can use them in other functions.
def loadModules():
    global cv2, Image
    import cv2
    from PIL import Image

# Try to load the necessary third party libraries and start the application
# If loading the libraries fails, print a message about installation
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

cmu_graphics.run()