# user input is received in the concole window, where we receive output as well
# input function is used to accept the input

name = input("Enter your name: ")
age = int(input("Enter your age: "))                           #typecasting was originally in a separate line of code
age = age + 1

print(f"Hello {name}")
print(f"You are {age} years old")

# to use any kind of math with user input, cast it as an integer or floating point number

#EXERCISES

# mad libs game --> there is a story, users get to submit nouns, verbs and adjectives within the story

adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective3 = input("Enter an adjective: ")

print(f"Today I went to a {adjective1} shop.")
print(f"In an exhibit, I saw {noun}")
print(f"{noun} was {adjective2} and {verb}ing")
print(f"I was {adjective3}")

# calculating the volume of a rectangle

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
print(f"Your total is: ${round(total, 2)}") # built-it total function, truncates the number to a chosen number of decimal places
