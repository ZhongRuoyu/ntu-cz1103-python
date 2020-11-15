from sense_hat import SenseHat
from time import sleep, time
sense = SenseHat()

b = (0, 0, 0)
w = (255, 255, 255)
r = (255, 0, 0)
g = (0, 255, 0)

board = [[r, r, r, b, b, b, b, r],
         [r, b, b, b, b, b, b, r],
         [b, b, b, b, g, r, b, r],
         [b, r, r, b, r, r, b, r],
         [b, b, b, b, b, b, b, b],
         [b, r, b, r, r, b, b, b],
         [b, b, b, r, b, b, b, r],
         [r, r, b, b, b, r, r, r]]

y = 2  # y coordinate of marble
x = 2  # x coordinate of marble
board[y][x] = w  # a white marble

board_1D = sum(board, [])  # convert to 1-dimension list
print(board_1D)  # for code debugging
sense.set_pixels(board_1D)  # display it

# This function checks the pitch value and the x coordinate
# to determine whether to move the marble in the x-direction.
# Similarly, it checks the roll value and y coordinate to
# determine whether to move the marble in the y-direction.


def move_marble(pitch, roll, x, y):
    new_x = x  # assume no change to start with
    new_y = y  # assume no change to start with
    if 1 < pitch < 179 and x != 0:
        new_x -= 1  # move left
    elif 359 > pitch > 179 and x != 7:
        new_x += 1  # move right
    if 1 < roll < 179 and y != 7:
        new_y += 1  # move up
    elif 359 > roll > 179 and y != 0:
        new_y -= 1  # move down
    new_x, new_y = check_wall(x, y, new_x, new_y)
    return new_x, new_y


def check_wall(x, y, new_x, new_y):
    if board[new_y][new_x] != r:
        return new_x, new_y
    elif board[new_y][x] != r:
        return x, new_y
    elif board[y][new_x] != r:
        return new_x, y
    else:
        return x, y

def GetCurrentPosition():
    for y in range(8):
        for x in range(8):
            if (board[y][x] == g):
                return x, y

def SetNewPosition(xy):
    x_orig, y_orig = xy
    from random import randint
    while True:
        x, y = randint(0, 7), randint(0, 7)
        if ((board[y][x] != r) and (board[y][x] != g)):
            break
    board[y_orig][x_orig] = b
    board[y][x] = g

game_over = False
timer = 0

while not game_over:
    if ((time() - timer) >= 10):
        SetNewPosition(GetCurrentPosition())
        timer = time()
    pitch = sense.get_orientation()['pitch']
    roll = sense.get_orientation()['roll']
    board[y][x] = b
    x, y = move_marble(pitch, roll, x, y)
    if (board[y][x] == g):
        game_over = True
    board[y][x] = w
    sense.set_pixels(sum(board, []))
    sleep(0.05)

sense.show_message('yay!!')
