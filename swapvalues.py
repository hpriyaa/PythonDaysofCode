# Program to swap variable values

# Taking User Input
a = input("Enter 1st variable value : ")
b = input("Enter 1st variable value : ")

print("Input received. \nValues entered are a-> " + a + " b-> " + b)

# Using a 3rd temp variable
temp = b
b = a
a = temp

# Printing Swapped Values
print("\nSwapped Values are a-> " + a + " b-> " + b)
