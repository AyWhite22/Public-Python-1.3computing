# A. White
# December 12, 2018
# Calculating the sum for the first natural numbers.
# File: approxpi.py

import math

def main():
    import math

# this is an introduction.
    print("This is a program that approximates the value of pi by summing the terms.")

# this is an iput.
    n = eval(input("How many terms would you like to sum?"))
    x = 0
    for i in range(n):
        x = x + 4.0 * (-1) ** i/ (2 * i + 1)
        print(x)
main()
