# A. White
# December 12, 2018
# Calculating a program
#that approximates the value
#of pi by summing the terms of this series:
#4/1- 4/3 + 4/5 - 4/7 + 4/9- 4/11.
# File: approxpi.py

def main():
    import math
    print("This program calculates the square root based off of the ")
    print("Newton's Method.")

    x = eval(input("What would you like to square root"?))
    guess = eval(input("/nHow many times would you like this to loop to improve the guess?"))

    for i in range(guess):
        top = guess + x / guess
        final_x = float(top) / 2

    close = final_x - math.sqrt(x)
    close_two = math.sqrt(x)

    print("The guess is", final_x, "which is",  close,"away from", close_two)
main()
    
