# user input is received in the console window, where we receive output as well
# input function is used to accept the input
# user input is always a string

name = input("Enter your name: ")
# when ran, the program is paused in the console window until something is typed in and "Enter" is hit
# the input received should be stored inside of a variable (like "name" in the above example); then it can be used for something
age = int(input("Enter your age: "))
# typecasting the input into an integer (or a float) to be able to perform mathematical operations with it; input can be typecast directly
age = age + 1

print(f"Hello {name}")
print(f"You are {age} years old")

# to use any kind of math with user input, cast it as an integer or floating point number

# EXERCISES

# mad libs game --> think of a story, users get to submit nouns, verbs and adjectives within the story

adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter an adjective: ")

print(f"Today I went to a {adjective1} shop.")
print(f"In an exhibit, I saw {noun}")
print(f"{noun} was {adjective2} and {verb}ing")
print(f"I was {adjective3}")

# calculating the volume of a rectangle (or lenght * width for the area)

length = float(input("Enter the lenght of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))
height = float(input("Enter the height of a rectangle: "))

volume = length * width * height

print(f"The volume is: {volume}cm^3")

# shopping cart program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
# built-it round function, truncates the number to a chosen number of decimal places
print(f"Your total is: ${round(total, 2)}")
