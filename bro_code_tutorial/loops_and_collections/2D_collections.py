# 2d list = [list1, list2, list3]
# you can also make a list of tuples, a tuple of tuples (2d tuple), or a tuple of sets

fruits =     ["apple", "oragne", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

# inner lists don't need a name:
# groceries = [["apple", "oragne", "banana", "coconut"],
#              ["celery", "carrots", "potatoes"],
#              ["chicken", "fish", "turkey"]]
groceries = [fruits, vegetables, meats]

# print(groceries[0])
# returns an entire row, the list at that index

# works similarly to coordinates, you need the index of the list and the element within the list
# print(groceries[1][2])

# ITERATING --> a single for loop iterates over the rows; use a nested loop to iterate over the elements
# for collection in groceries:
#     print(collection)

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()

# EXERCISE - making a phone keypad

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
