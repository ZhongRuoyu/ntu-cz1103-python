from sense_hat import SenseHat
from random import randint
from time import sleep

s = SenseHat()

r = (255, 0, 0) # Red
g = (0, 255, 0) # Green
o = (0, 0, 0) # Blank

img_green = [o, o, o, o, o, o, o, o,
             o, o, o, g, o, o, o, o,
             o, o, g, g, g, o, o, o,
             o, g, o, g, o, g, o, o,
             o, o, o, g, o, o, o, o,
             o, o, o, g, o, o, o, o,
             o, o, o, g, o, o, o, o,
             o, o, o, o, o, o, o, o] # Up arrow in green
img_red = [o, o, o, o, o, o, o, o,
           o, o, o, r, o, o, o, o,
           o, o, r, r, r, o, o, o,
           o, r, o, r, o, r, o, o,
           o, o, o, r, o, o, o, o,
           o, o, o, r, o, o, o, o,
           o, o, o, r, o, o, o, o,
           o, o, o, o, o, o, o, o] # Up arrow in red
img_countdown = [
    [o, o, o, o, o, o, o, o,
     o, o, o, r, o, o, o, o,
     o, o, r, r, o, o, o, o,
     o, o, o, r, o, o, o, o,
     o, o, o, r, o, o, o, o,
     o, o, o, r, o, o, o, o,
     o, o, r, r, r, o, o, o,
     o, o, o, o, o, o, o, o], # Number 1
    [o, o, o, o, o, o, o, o,
     o, o, o, r, r, o, o, o,
     o, o, r, o, o, r, o, o,
     o, o, o, o, o, r, o, o,
     o, o, o, o, r, o, o, o,
     o, o, o, r, o, o, o, o,
     o, o, r, r, r, r, o, o,
     o, o, o, o, o, o, o, o], # Number 2
    [o, o, o, o, o, o, o, o,
     o, o, r, r, r, r, o, o,
     o, o, o, o, r, o, o, o,
     o, o, o, r, o, o, o, o,
     o, o, o, o, r, o, o, o,
     o, o, o, o, o, r, o, o,
     o, o, r, r, r, o, o, o,
     o, o, o, o, o, o, o, o] # Number 3
]

directions = {
      0: {'x': 0, 'y': 1, 'z': 0},
     90: {'x': -1, 'y': 0, 'z': 0},
    180: {'x': 0, 'y': -1, 'z': 0},
    270: {'x': 1, 'y': 0, 'z': 0}
} # 4 directions; can be randomly chosen by function GetNewRotation(rotation)


def CompareDirection(reference): # compare device orientation with reference direction
    acceleration = s.get_accelerometer_raw()
    returnValue = True # True by default; changed when not satisfied
    for key in acceleration: # compare three components, respectively
        if (abs(acceleration[key] - reference[key]) > 0.5):
            returnValue = False
            break # no need to continue if fail in one direction
    return returnValue # True if success; False if fail

def GetNewTimeout(timeout): # return a new timeout based on current timeout
    newTimeout = round(timeout * 0.8, 1) # return 80% of current timeout (rounded). If unchanged, reduce by 0.1
    if (newTimeout != timeout):
        return newTimeout
    else:
        newTimeout -= 0.1
        return newTimeout

def GetNewRotation(rotation): # get new direction; guaranteed to be different from current direction
    newRotation = randint(0, 3) * 90
    while (newRotation == rotation):
        newRotation = randint(0, 3) * 90
    return newRotation

def ShowDebugMsg(): # for debug use. Display acceleration in console
    acceleration = s.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    print("x = " + str(round(x, 2)) +
        ";\ny = " + str(round(x, 2)) +
        ";\nz = " + str(round(z, 2)) +
        ";\ntimeout = " + str(timeout) + "\n\n")


# initialise variables
timeout = 1.0
score = 0
rotation = 0

# main loop body
while (True):
    for i in range(0,3):
        s.set_pixels(img_countdown[2 - i]) # img_countdown [2] to [0] represent numbers 3 to 1 respectively
        sleep(0.8)
    s.clear() # clears display
    rotation = GetNewRotation(rotation) # obtain a new random direction
    s.set_rotation(rotation) # set the new random direction
    s.set_pixels(img_red) # set image
    sleep(timeout)
    ShowDebugMsg() # for debug use
    if (CompareDirection(directions[rotation])): # success
        score += 1
        for i in range(0, 3): # flash success message in green
            s.clear()
            sleep(0.2)
            s.set_pixels(img_green)
            sleep(0.2)
    else: # fail
        for i in range(0, 3): # flash fail message in red
            s.clear()
            sleep(0.2)
            s.set_pixels(img_red)
            sleep(0.2)
        break # quit loop
    timeout = GetNewTimeout(timeout) # get new timeout for next loop
    sleep(0.8) # sleep for a short while before next loop

s.show_message("Score: " + str(score)) # display final score
