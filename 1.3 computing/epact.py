# A. White
# December 12, 2018
# Prompts user of a four-digit year and then outputs the value.
# File: epact.py

def main():

    import math
        
    print("This program prompts you to put in a four-digit year and then it will output the value.")
	
    year = eval(input("Enter a four-digit year: "))
    C = year//100
    epact = (8 + (C//4)- C +((8*C + 13)//25)+ 11 *(year%19)) %30
	
    print("The value of the epact is: ", epact, ".")
    
main()
