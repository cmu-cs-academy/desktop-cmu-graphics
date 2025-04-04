def drawImages(reference):
    Image(reference, 0, 0)
    Image(reference, 0, 200, width=400)
    Image(reference, 300, 100, rotateAngle=45, align='center', width=175, height=175)

# Drawing an image referenced by path, scaling, and rotating
drawImages('sample.jpg')

# -

app.group.clear()

# Drawing a PIL image, scaling, and rotating
from PIL import Image as PILImage
PILSampleImage = PILImage.open('sample.jpg')
sample = CMUImage(PILSampleImage)
drawImages(sample)

# -

assertRaises(
    lambda: drawImages(PILSampleImage),
    'TypeError: The first argument to drawImage or Image should be a string or CMUImage, but you passed a PIL image. Did you forget to wrap a PIL image with CMUImage?'
)
assert getImageSize('sample2.png') == (400, 200)