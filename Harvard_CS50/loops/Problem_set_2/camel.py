# Implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user's input will indeed be in camel case. 

camel_name = input("Enter a name in camel case: ")
snake_name = ""

for letter in camel_name:
    if letter.isupper():
        snake_name += "_" + letter
    else:
        snake_name += letter

print(snake_name.lower())
