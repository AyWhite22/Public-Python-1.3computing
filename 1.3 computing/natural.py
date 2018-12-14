# A. White
# December 12, 2018
# Calculating the sum for the first natural numbers.
# File: natural.py

def main():
    #this is the introduction.
    print("This program calculates the first natural numbers.")
    n = eval(input("Enter a natural number"))
    #this is the input.
    t = 0
    a = 1

    for i in range(n):
        t = t + a
        a = a + 1

    print("The sum of the first natural numbers are: ", t)

main()
        
