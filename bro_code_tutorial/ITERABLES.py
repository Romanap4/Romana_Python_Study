# Iterables = An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop

# LISTS
# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number)

# for number in reversed(numbers):                        # iterating backwards
#     print(number, end=" ")                              # keyword "end" within the print function replacing a newline

# TUPLES
# numbers = (1, 2, 3, 4, 5)

# for number in numbers:
#     print(number)

# SETS

# fruits = {"apple", "orange", "banana", "coconut"}       # sets are not reversible

# for fruit in fruits:
#     print(fruit)

# STRINGS

# name = "Manyan Romajana"

# for character in name:
#     print(character, end=" ")

# DICTIONARIES

my_dictionary = {"A": 1, "B": 2, "C": 3}

# for key in my_dictionary:                               # iterating over a dictionary returns the keys, but not the values
#     print(key)

# for value in my_dictionary.values():                    # returns values
#     print(value)

for key, value in my_dictionary.items():
#     print(key, value)
    print(f"{key} = {value}")                             # reformatting
