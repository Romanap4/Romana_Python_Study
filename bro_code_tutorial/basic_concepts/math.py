# ++++++++++++ ARITHMETIC OPERATORS +++++++++++++++

friends = 10

# ADDITION
# friends = friends + 1
# augmented assingment operator (+=, -=, *=, /=)
# friends += 1

# SUBTRACTION
# friends = friends - 2
# friends -= 2

# MULTIPLICATION
# friends = friends * 3
# friends *= 3

# DIVISION
# friends = friends / 2
# friends /= 2

# EXPONENTIATION
# friends = friends ** 2
# friends **= 2

# MODULUS --> % is the modulus operator, it gives us the remainder of any division
# remainder = friends % 3

# print(friends)
# print(remainder)

# ++++++++++++ BUILT-IN MATH RELATED FUNCTIONS +++++++++++++++++

x = 3.14
y = 4
# y = -4 for the absolute value function
z = 5

# ROUND FUNCTION --> rounds the number to the nearest whole integer
# result = round(x)

# ABSOLUTE VALUE FUNCTION --> returns the distance from zero as a whole number
# result = abs(y)

# POWER FUNCTION (base value, exponent) --> raises the base to a given power
# result = pow(4, 3)

# MAX FUNCTION --> finds the maximum value between various values
# result = max(x, y, z)

# MIN FUNCTION --> finds the minimum value between various values
# result = min(x, y, z)

# print(result)

import math
# importing the math module --> it contains useful constants and functions

x = 9
y = 9.1
z = 9.9

# FINDING USEFUL CONSTANTS
# print(math.pi)
# print(math.e)

# SQUARE ROOT FUNCTION --> returns the square root of a value
# result = math.sqrt(x)

# CEILING FUNCTION --> always rounds a floating point number up
# result = math.ceil(y)

# FLOOR FUNCTION --> always rounds a floating point number down
# result = math.floor(z)

# print(result)

# +++++++++ EXERCISES +++++++++++

# CIRCUMFERENCE OF A CIRCLE

# radius = float(input("Enter the radius of a circle: "))
# circumference = 2 * math.pi * radius
# print(f"The circumference is: {round(circumference, 2)}cm")

# AREA OF A CIRCLE

# radius = float(input("Enter the radius of a circle: "))
# area = math.pi * pow(radius, 2)
# print(f"The area of the circle is: {round(area, 2)}cm^2")

# HYPOTHENUSE CALCULATOR

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C = {c}")
