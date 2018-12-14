# A. White
# December 12, 2018
# Calculating the volume and surface area of a sphere.
# File: moleweight.py

#defining the script.
def main():
#telling the reader what the script does.
    print("This program determines the molecular weight of a hydrocarbon.")
    h = 1.00794
    c = 12.0107
    o = 15.9994
#asking reader to input the amount of molecules that are there.
    hnum = eval(input("How many hydrogen atoms are there? "))
    cnum = eval(input("How many carbon atoms are there? "))
    onum = eval(input("How many oxygen atoms are there? "))
#telling the computer the expression used to solve the molecular weight.
    ans = (h*hnum) + (c*cnum) + (o*onum)
#telling the computer to say this and tell the reader the answer.
    print("The molecular weight of the hydrocarbon is ", ans)
main()
