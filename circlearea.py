# Program to calculate the area of circle based on its radius
import math

radius = float(input("Enter circle's radius in cm : "))

area = math.pi * pow(radius, 2)

print("Area of circle with radius " + str(radius) + " cm is " + str(round(area, 2)) + " square cm")
