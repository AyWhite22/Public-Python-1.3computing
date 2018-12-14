# A. White
# December 12, 2018
# Calculating the sum for the first natural numbers.
# File: cubedn.py

import math

def main():
    print("This is a program to find the sum of the cubes of the first n natural numbers.")

    n = eval(input("What would you like to find the sum of?"))
    t = 0
    a = 1

    for i in range(n):
        t = t + a **3
        a = a + 1

    print("The sum of the first natural numbers are: ", t)

main()
