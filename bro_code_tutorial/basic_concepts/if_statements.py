# if =   do some code only IF some condition is True
# elif = else if
#        Else do something else

# be careful with the order of the statements; they will be executed in order
# any code under the statement should be indented

# +++++ EXAMPLE 1 +++++

# age = int(input("Enter your age: "))

# if age >= 100:
#     print("You are too old to sign up")
# elif age >= 18:
#     print("You are now signed up!")
# elif age < 0:
#     print("You haven't been born yet")
# else:
#     print("You must be 18+ to sign up")

# +++++ EXAMPLE 2 ++++++

# response = input("Would you like food? (Y/N): ")

# use "==" to check if two values are equal, comparison operator; "=" is the assignment operator
# if response == "Y":
#     print("Have some food!")
# else:
#     print("No food for you!")

# +++++ EXAMPLE 3 +++++

# name = input("Enter your name: ")

# if name == "":
#     print("You did not type in your name!")
# else:
#     print(f"Hello {name}")

# +++++ USING BOOLEANS WITH IF STATEMENTS ++++++
# a boolean variable can be used in place of a condition
# condition would evaluate to be true or false

for_sale = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")

online = False

if online:
    print("The user is online")
else:
    print("The user is offline")
