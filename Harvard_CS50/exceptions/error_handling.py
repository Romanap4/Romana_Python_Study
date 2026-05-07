# Error handling is an effective strategy to fix potential runtime errors
# TRY

# try and except are ways of testing out user input before something goes wrong

# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")

# Best practice is to try the fewest lines of code possible that we are concerned could fail

# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")

# print(f"x is {x}")

# In the case above, a NameError where x is not defined will occur, in case the user doesn't input an integer
# Examining the order of operations, if it takes an incorrectly inputted character and attempts to assign it as an integer, that assingnment of a value to x will fail
# As a result, there is no x to print on our final line of code

# ELSE
# There is another way to catch these errors

# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

# If the user doesn't cooperate, we can simply end the program
# Using a loop, we can prompt the user to enter a value for x repeatedly

# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break

# print(f"x is {x}")

# If the user supplies the correct input, we can break from the loop and print the output
# If a user inputs something incorrectly, they will be asked for input again

# CREATING A FUNCTION TO GET AN INTEGER

# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break
#     return x

# main()

# This code can be improved

# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x

# main()

# Additional option

# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")

# main()

# PASS
# the code can be built in a way that the user doesn't get warned about the error, but just prompted again instead

# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             pass

# main()

# In this case, the code will still function, but it will not repeatedly inform the user of their error
# In some cases you'll want to be clear to the user what error is being produced, while in others you might decide that you simpy want to ask them for input again

# Improving the implementation of the get_int() function
# This way we are passing in a prompt that the user sees when asked for input, instead of relying upon x being in both the main() and get_int() functions

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()
