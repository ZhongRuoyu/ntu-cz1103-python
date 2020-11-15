from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)

#--- function get_color() ---------------------------
def get_color(color):
    no_of_try = 0
    while True:
        no_of_try += 1
        if (no_of_try <= 3):
            color_str = input("Enter the value of the " + color + \
                " color for message (0 to 255): ")
        else:
            print("Three tries failed. Value set to 0 by default.")
            return 0
        try:
            color_int = int(color_str)
            if (0 <= color_int <= 255):
                return color_int
            else:
                print("Please enter a value between 0 and 255 (inclusive).")
        except:
            print("Please enter an integer value.")
    

#---------------------------------------------------
r_int = get_color("red")
g_int = get_color("green")
b_int = get_color("blue")
msg_color = (r_int, g_int, b_int)
sense.show_message("I got it!", text_colour=msg_color)