# A. White
# December 12, 2018
# Calculating the length of a ladder. 
# File: ladder.py

import math
 
def main():
# this is an introduction
    print("This is a program that determines the length of a ladder")
    print("required to reach a given height when leaned against a house.")
    # this is an input
    angle = eval(input("Enter the angle of the ladder: "))
    height = eval(input("Enter the height that you want the ladder to reach: "))
    radians = math.pi / 180 * angle
    length = round(abs((height) / math.sin (radians)) , 2)

    # this is an output
    print("The length of your ladder is", length,".")
main()
