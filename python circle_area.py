import math

# Ask the user for the radius
radius = input("Enter the radius of the circle: ")

# Convert input to float
radius = float(radius)

# Calculate the area
area = math.pi * radius ** 2

# Print the result
print("The area of the circle is " + str(area))
