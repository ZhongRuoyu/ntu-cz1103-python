import math, random

DIGITCOUNT = 4

def Generate():
    x = [random.randint(0, 9) for i in range(0, DIGITCOUNT)]
    for i in range(0, len(x)):
        for j in range(0, i):
            while (x[i] == x[j]):
                x[i] = random.randint(0, 9)
    return x

def PromptForInput():
    while (True):
        try:
            strInput = input("Please input " + str(DIGITCOUNT) + " digits: ").strip()
            intInput = int(strInput)
            if (intInput < 0):
                raise ValueError("Only non negative value allowed.")
            if (len(strInput) != DIGITCOUNT):
                raise ValueError("Only " + str(DIGITCOUNT) + "digits allowed.")
            break
        except:
            print("Error. Please check your input and try again.")
    x = []
    for i in range(0, DIGITCOUNT):
        x.insert(0, intInput % 10)
        intInput = math.floor(intInput / 10)
    return x

def Bull(x, guess):
    bull = 0
    for i in range(0, DIGITCOUNT):
        if (x[i] == guess[i]):
            bull += 1
    return bull

def Cow(x, guess):
    cow = 0
    for i in range(0, DIGITCOUNT):
        try:
            if (x.index(guess[i]) != i):
                cow += 1
        except:
            pass
    return cow

x = Generate()
guess = []
attemptCount = 0

while (guess != x):
    guess = PromptForInput()
    attemptCount += 1
    bull = Bull(x, guess)
    cow = Cow(x, guess)
    print("Result: " + str(bull) + "A (Bulls) & " + str(cow) + "B (Cows).")

print("Congratulations! You win.")
print("Attempts count:", attemptCount)
