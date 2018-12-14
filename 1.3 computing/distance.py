# A. White
# December 12, 2018
# Calculating the distance between two points.
# File: distance.py

import math
 
def main():
# this is an introduction
    print("This is a program that calculates a distance of 2 points.")

    # this is an input
    x1 = eval(input("Enter the first x-point: "))
    x2 = eval(input("Enter the Second x-point: "))
    y1 = eval(input("Enter the first y-point: "))
    y2 = eval(input("Enter the second y-point "))
    distance = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)

    # this is an output
    print("The distance of the two coordinates is...", distance, ".")
main()
