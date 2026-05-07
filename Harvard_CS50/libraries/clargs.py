# sys is a module that allows us to take arguments at the command line
# argv is a list within the sys module that records what the user typed on the command line

# import sys

# print("hello, my name is", sys.argv[1])

# Type "python clargs.py Manyan" in the terminal
# The index of the entered argument is [1] because the file name is at the [0] index of the argv list

# If nothing is typed in the terminal, the error "list index out of range" pops up
# This is how to prevent that from happening

# import sys

# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# To be even more defensive

# import sys

# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])

# Keeping the error checking separete from the remainder of the code

# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print("hello, my name is", sys.argv[1])

# Using the built-in function of sys called exit() allows us to exit the program if an error was introduced by the user
# Doing this ensures that the program will never execute the final line of code and trigger an error

# SLICE
# slice is a command that allows us to take a list and tell the interpreter where we want the interpreter to consider the start and the end of the list

# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")

# for arg in sys.argv:
#     print("hello, my name is", arg)

# slice can be used to ensure that the program will ignore the first element of the list where clargs.py is currently being stored

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

# This way we tell the interpreter to start the list at [1] and go to the end, using the [1:] argument
