from PIL import Image
import random

image = Image.open('Image1.jpg')

# Saves pixels in an array
pixel_map = image.load()

width, height = image.size
pepper_amount = 3000

while True:
    rand_col = random.randint(1, 3999)
    rand_row = random.randint(1, 5999)

    if(pepper_amount != 0):
        pixel_map[rand_col, rand_row] = (255,255,255)
        pepper_amount -= 1
    else:
        break

image.show()