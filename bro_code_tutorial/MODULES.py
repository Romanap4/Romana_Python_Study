# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program into reusable separate files

# print(help("modules"))                     # use to get a list of all available modules
# print(help("math"))                        # use the name of the module to get a list of all the variables and functions

# different ways to import 
# import math                                # use import and the module name to include a module 
# import math as m                           # giving the module an alias 
# from math import pi                        # there might be name conflicts when using this way   


# print(math.pi)                             # use to access a variable or a function
# print(m.pi)
# print(pi)                                  # no need for module name 

# from math import e                         # e is an exponential constant

# a, b, c, d, e = 1, 2, 3, 4, 5              # e from the math module got reassigned a new value       

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
# right-click folder --> new --> Python file --> name it 

import modules_creation

result = modules_creation.pi
result = modules_creation.square(3)
result = modules_creation.cube(3)
result = modules_creation.circumference(3)
result = modules_creation.area(3)

print(result)
