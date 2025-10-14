# arithemtic operators

friends = 10

# friends = friends + 1       # addition
# friends += 1                                 #augmented assingment operator
# friends = friends - 2       # subtraction
# friends -= 2
# friends = friends * 3       # multiplication
# friends *= 3
# friends = friends / 2       # division
# friends /= 2
# friends = friends ** 2      # exponentiation
# friends **= 2
# remainder = friends % 3      # modulus

# print(friends)
# print(remainder)

# built-in math related functions

x = 3.14
y = 4                                                # -4 for abs function
z = 5

# result = round(x)                                  # round function
# result = abs(y)                                    # absolute value function (distance from 0 as a whole number)
# result = pow(4, 3)                                 # power function (base value, power)
# result = max(x, y, z)                              # max function, finds maximum value
# result = min(x, y, z)                              # min function, finds minimum value

# print(result)

import math                                          # importing the math module

x = 9
y = 9.1
z = 9.9

# finding useful constants
# print(math.pi)
# print(math.e)
# result = math.sqrt(x)                              # square root function
# result = math.ceil(y)                              # ceiling function, always rounds a floating point number up
# result = math.floor(z)                             # floor function, always rounds a floating point number down

# print(result)

# EXERCISES

# circumference of a circle

# radius = float(input("Enter the radius of a circle: "))

# circumference = 2 * math.pi * radius

# print(f"The circumference is: {round(circumference, 2)}cm")

# area of a circle

# radius = float(input("Enter the radius of a circle: "))

# area = math.pi * pow(radius, 2)

# print(f"The area of the circle is: {round(area, 2)}cm^2")

# hypothenuse calculator

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C = {c}")
