from sense_hat import SenseHat
from time import sleep

s = SenseHat()

g = (0, 255, 0)
y = (255, 255, 0)
b = (0, 0, 0)
image_pixels = [b, b, b, b, b, b, b, b,
                b, b, b, y, b, b, b, b,
                b, b, y, y, y, b, b, b,
                b, y, b, y, b, y, b, b,
                b, b, b, y, b, b, b, b,
                b, b, b, y, b, b, b, b,
                b, b, b, y, b, b, b, b,
                b, b, b, b, b, b, b, b]
s.set_pixels(image_pixels)

while (True):
    sleep(1)
    for item in range(0, len(image_pixels)):
        if (image_pixels[item] == y):
            image_pixels[item] = g
        elif (image_pixels[item] == g):
            image_pixels[item] = y
        s.set_pixels(image_pixels)
