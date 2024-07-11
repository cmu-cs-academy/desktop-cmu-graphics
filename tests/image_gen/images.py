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
sample = CMUImage(PILImage.open('sample.jpg'))
drawImages(sample)

# -

app.group.clear()

# Drawing a PIL image, scaling, and rotating
from PIL import Image as PILImage
sample = PILImage.open('sample.jpg')
drawImages(sample)
