# Iterables = An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop

# LISTS
# numbers = [1, 2, 3, 4, 5]

# the name of the current element in the iterable should be descriptive of what we're iterating over
# for number in numbers:
#     print(number)

# keyword "end" within the print function replacing a newline
# iterating backwards:
# for number in reversed(numbers):
#     print(number, end=" ")

# TUPLES
# numbers = (1, 2, 3, 4, 5)

# for number in numbers:
#     print(number)

# SETS

# sets are not reversible
# fruits = {"apple", "orange", "banana", "coconut"}

# for fruit in fruits:
#     print(fruit)

# STRINGS

# name = "Manyan Romajana"

# for character in name:
#     print(character, end=" ")

# DICTIONARIES

my_dictionary = {"A": 1, "B": 2, "C": 3}

# iterating over a dictionary returns the keys, but not the values
# for key in my_dictionary:
#     print(key)

# returns values; using the built-in values method
# for value in my_dictionary.values():
#     print(value)

# to get the key and the value, use the built-in items method
for key, value in my_dictionary.items():
#     print(key, value)
# we can reformat the output:
    print(f"{key} = {value}")
