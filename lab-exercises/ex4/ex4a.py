from sense_hat import SenseHat
from random import randint

s = SenseHat()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
blank = (0, 0, 0)

s.clear()
s.set_pixel(randint(0, 7), randint(0, 7), red)
s.set_pixel(randint(0, 7), randint(0, 7), green)
s.set_pixel(randint(0, 7), randint(0, 7), blue)
s.set_pixel(randint(0, 7), randint(0, 7), yellow)
