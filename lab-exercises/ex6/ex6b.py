from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

b = (0, 0, 0)
w = (255, 255, 255)

board = [[b, b, b, b, b, b, b, b],
         [b, b, b, b, b, b, b, b],
         [b, b, b, b, b, b, b, b],
         [b, b, b, b, b, b, b, b],
         [b, b, b, b, b, b, b, b],
         [b, b, b, b, b, b, b, b],
         [b, b, b, b, b, b, b, b],
         [b, b, b, b, b, b, b, b]]

y = 2  # y coordinate of marble
x = 2  # x coordinate of marble
board[y][x] = w  # a white marble

board_1D = sum(board, [])  # convert to 1-dimension list
print(board_1D)  # for code debugging
sense.set_pixels(board_1D)  # display it
