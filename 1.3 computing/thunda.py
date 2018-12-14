# A. White
# December 12, 2018
# Computes how far a lightning strike is.
# File: moleweight.py

#defining the script.
def main():
#asking reader how many seconds it took for the thunder to be heard. 
    time = eval(input("What is the time (in seconds) elapsed between the flash and thunder? "))
#defining variables and the expressions used to create the variables.
    sound = 1100*time
    ans = sound/5280
#telling the reader the answer.
    print("The distance to a lightening strike is ", ans , "miles")
main()
