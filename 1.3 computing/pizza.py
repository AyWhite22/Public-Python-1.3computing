# A. White
# December 12, 2018
# Calculating the volume and surface area of a sphere.
# File: pizza.py

#imported the math 
import math
#defining variables and returning a value to the reader.
def pizzaArea():
  intDiam = int(input('What is the diameter of the whole pizza(in inches)? '))
  radius = intDiam/2
  area = math.pi * radius * radius
  return area
#defining variables and returning the answer to the reader.  
def costPerInch():
  area = pizzaArea()
  fltprice = float(input("What is the price of the pizza? "))
  ans = fltprice/area
  return ans
  
def main():
#used the rounding function ".2f". 
    ans = costPerInch()
    print("The cost per square inch is $ %.2f" %ans )
    
main()
