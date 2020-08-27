import os
import shutil

pygame_loader_path = '../../cmu_graphics/libs/pygame_loader'
our_images_path = './images'

pygame_images = ['pygame_icon.bmp', 'pygame_icon.icns', 'pygame_icon.svg', 'pygame_icon.tiff', 'pygame.ico']
extension_to_image = dict()
for file in os.listdir(our_images_path):
    extension = file.split('.')[-1]
    extension_to_image[extension] = file

for path, dirs, files in os.walk(pygame_loader_path):
    for image in pygame_images:
        if image in files:
            image_path = path + os.sep + image
            extension = image.split('.')[-1]
            our_image_path = our_images_path + os.sep + extension_to_image[extension]
            shutil.copy(our_image_path, image_path)
            print('copied', our_image_path, 'to', image_path)
