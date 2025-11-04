# while loop = execute some code WHILE some condition remains true
# useful for verifying user input

# name = input("Enter your name: ")

# USING CONDITIONAL STATEMENTS:
# it will execute once; if skipped, we continue with the rest of the program

# if name == "":
#     print("You did not enter your name")
# else:
#     print(f"Hello {name}")

# USING WHILE LOOPS (allows you to continually prompt the user until they enter a name in this case):
# the welcome message is printed after exiting the loop
# you need a way to escape the loop to avoid infinite loop;
# (in this case it's reassigning the "name" variable with user input and reprompting the user to enter something)

# EXAMPLE 1
# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")

# print(f"Hello {name}")

#EXAMPLE 2
# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# EXAMPLE 3
# food = input("Enter a food you like (q to quit): ")

# using the "not" logical operator to let the user quit after pressing "q"
# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# print("bye")

# EXAMPLE 4
num = int(input("Enter a number between 1-10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1-10: "))

print(f"Your number is {num}")
