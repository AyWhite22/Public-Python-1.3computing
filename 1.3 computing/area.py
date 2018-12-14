# A. White
# December 12, 2018
# Calculating the volume and surface area of a sphere.
# File: area.py

def main():
  PI = 3.14
  radius = float(input("Please enter the radius of the sphere: "))
  sa = 4 * PI * radius * radius
  Volume = (4/3) * PI * radius * radius * radius

  print("The surface area of the sphere is...", sa, "units squared.")
  print("The volume of the sphere is...", Volume, "units cubed.")
main()
