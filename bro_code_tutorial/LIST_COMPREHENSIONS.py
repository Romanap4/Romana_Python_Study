# List comprehensions = A concise way to create lists in Python
#                       Compact and easier to read than traditional loops
#                       [expression for value in iterable if condition] --> formula

# doubles = []
# for x in range (1, 11):
#     doubles.append(x * 2)

# print(doubles)

# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1, 11)]
# squares = [z ** 2 for z in range (1, 11)]               # or z * z

# print(doubles)
# print(triples)
# print(squares)

# fruits = ["apple", "orange", "banana", "coconut"]
# fruits = [fruit.upper() for fruit in fruits ]           # to make it shorter: ˇ

# fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]

# print(fruits)

# fruits = ["apple", "orange", "banana", "coconut"]
# fruit_chars = [fruit[0] for fruit in fruits ]  

# print(fruit_chars)

# numbers = [1, -2, 3, -4, 5, -6, 8, -7]
# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num < 0]
# even_nums = [num for num in numbers if num % 2 == 0]     # check if the number is even
# odd_nums = [num for num in numbers if num % 2 == 1]      # check if the number is odd

# print(positive_nums)
# print(negative_nums)
# print(even_nums)
# print(odd_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)
