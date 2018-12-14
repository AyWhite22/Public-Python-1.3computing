# File: usersum.py
# December 12, 2018 
# A program to sum a series of numbers given by the user
# A. White

def main():

    import math

    # This is an introduction
    print("This is a program to sum a series of numbers given by you.")

    # This is an input
    numbers = eval(input("How many numbers would you like to be summed? "))
    v = 0
    for i in range(numbers):
        x = eval(input("Enter number: "))
        v = x + v

    # This is an output
    print("The sum of your", numbers, "numbers is", v,".")
    
main() 
