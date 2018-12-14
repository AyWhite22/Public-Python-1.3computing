# A. White
# December 12, 2018
# Calculating the area of a triangle 
#using the given lengths of three sides.
# File: triangle.py

import math
 
def main():
# this is an introduction
    print("This is a program that calculates the area of a triangle using the given lengths of three sides.")

    # this is an input
    a = eval(input("Enter the first length: "))
    b = eval(input("Enter the Second length: "))
    c = eval(input("Enter the third length: "))
    sides = (a + b + c) / 2
    area = math.sqrt(sides*(sides - a)*(sides - b)*(sides - c))

    # this is an output
    print("The area of your triangle", area,"units squared.")
main()
