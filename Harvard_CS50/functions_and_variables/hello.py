# multiple ways to format the output

# string concatenating:
name = input("What's your name? ")
print("Hello, " + name)

# passing multiple arguments to the print function (a space between the arguments is added automatically):
name = input("What's your name? ")
print("Hello,", name)

# using the "end" keyword argument:
name = input("What's your name? ")
print("Hello, ", end="")
print(name)

# using "escape" characters to print quotation marks:
print("Hello, \"friend\"")

# formatting strings or string interpolation:
name = input("What's your name? ")
print(f"Hello, {name}")
