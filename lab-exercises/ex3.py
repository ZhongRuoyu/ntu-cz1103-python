def GetColourValue(colour):
    print()
    while True:
        try:
            prompt = "Please enter the " + colour + " value: "
            value = int(input(prompt))
            if (0 <= value <= 255):
                break
        except:
            print("Error. Please provide an integer", colour, "value between 0 and 255. Please try again.")
    return value

def GetSpeed():
    print()
    while True:
        try:
            value = float(input("Now, please enter the scroll speed (larger than 0) of your message: "))
            if (value > 0):
                break
        except:
            print("Error. Please provide a positive value. Please try again.\n")
    return value

from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
r_txt, g_txt, b_txt, r_bg, g_bg, b_bg, speed = 0, 0, 0, 0, 0, 0, 0
firstRun = True

while (firstRun == True or input("\nDo you wish to continue? Type N to quit. ") != "N"):
    firstRun = False
    print("Please enter the Red, Green and Blue values (integers between 0 and 255) of the colour you want to display your message in.")
    r_txt = GetColourValue("Red")
    g_txt = GetColourValue("Green")
    b_txt = GetColourValue("Blue")
    
    print()
    print("Now, please enter the Red, Green and Blue values (integers between 0 and 255) of the background colour.")
    r_bg = GetColourValue("Red")
    g_bg = GetColourValue("Green")
    b_bg = GetColourValue("Blue")

    for attemptCount in range(0,3):
        
        if ((r_txt, g_txt, b_txt) != (r_bg, g_bg, b_bg)):
            break
        
        print("Error. The colours cannot be the same for the text and the background. Please try again.")
        
        print("Please enter the Red, Green and Blue values (integers between 0 and 255) of the colour you want to display your message in.")
        r_txt = GetColourValue("Red")
        g_txt = GetColourValue("Green")
        b_txt = GetColourValue("Blue")
        
        print("Now, please enter the Red, Green and Blue values (integers between 0 and 255) of the background colour.")
        r_bg = GetColourValue("Red")
        g_bg = GetColourValue("Green")
        b_bg = GetColourValue("Blue")
    
    else:
        print("\nThree attempts failed. Quitting... ")
        exit()

    speed = GetSpeed()
    
    print("\nDisplaying your message...")
    sense.show_message("This is fun!", text_colour = (r_txt, g_txt, b_txt), back_colour = (r_bg, g_bg, b_bg), scroll_speed = speed)
    print("Done.")

print("Thank you for using.")