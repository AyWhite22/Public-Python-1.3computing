# A. White
# December 12, 2018
# Calculating a slope.
# File: slope.py

def main():
  print("This program calculates slope.")
  
  #Prompting for: points
  x1 = eval(input("First x-point: "))
  x2 = eval(input("Second x-point: "))
  y1 = eval(input("First y-point: "))
  y2 = eval(input("Second y-point: "))

  #Calculating: Slope
  slope = (y2 - y1) / (x2 - x1)
  
  #Output
  print("The slope is:", slope, ".")

main()
