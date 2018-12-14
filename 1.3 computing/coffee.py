# A. White
# December 12, 2018
# Calculating the price of coffee.
# File: coffee.py

def main():
  n = float(input("Enter the number of pounds: "))
  coffee_cost = 10.5 * n
  shipping_cost = (0.86 * n) + 1.50 
  total = coffee_cost + shipping_cost
  print("Total cost, including shipping: ",total)
main()
