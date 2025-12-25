# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program into reusable separate files

# use to get a list of all available modules within the standard Python library
# print(help("modules"))
# use the name of the module to get a list of all the variables and functions found within that module
# print(help("math"))

# different ways to import
# use import and the module name to include a module:
# import math
# giving the module an alias:
# import math as m
# importing something specific from a module; there might be name conflicts when using this way:
# from math import pi

# use to access a variable or a function:
# print(math.pi)
# print(m.pi)
# no need to use the module name when using the third way of importing
# print(pi)

# e is an exponential constant
# from math import e

# e from the math module got reassigned a new value
# a, b, c, d, e = 1, 2, 3, 4, 5

# print(e**a)
# print(e**b)
# print(e**c)
# print(e**d)
# print(e**e)

# to be more explicit and avoid mistakes:
# print(math.e**a)
# print(math.e**b)
# print(math.e**c)
# print(math.e**d)
# print(math.e**e)

# CREATING A MODULE:
# right-click project folder --> new --> Python file --> name it

# importing the module you created; now you have access to everything within the module:
import modules_creation

result = modules_creation.pi
result = modules_creation.square(3)
result = modules_creation.cube(3)
result = modules_creation.circumference(3)
result = modules_creation.area(3)

print(result)
