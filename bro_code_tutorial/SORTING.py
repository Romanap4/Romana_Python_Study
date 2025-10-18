# SORTING IN PYTHON .sort() or sorted()
# Lists[], Tuples(), Dictionaries{"":""}, Objects

# ++++++++++++ LISTS ++++++++++++++

# fruits = ["banana", "orange", "apple", "coconut"]
# numbers = [3, 1, 5, 2, 4]

# sorts in alphabetical order
# fruits.sort()
# to reverse the order:
# fruits.sort(reverse=True)
# sorts in ascending order
# numbers.sort()
# sorts in descending order
# numbers.sort(reverse=True)

# print(fruits)
# print(numbers)

# ++++++++++++ TUPLES ++++++++++++++

# fruits = ("banana", "orange", "apple", "coconut")

# typecasting the result into a tuple
# fruits = tuple(sorted(fruits))
# to reverse the order
# fruits = tuple(sorted(fruits, reverse=True))

# print(fruits)

# +++++++++++ DICTIONARIES +++++++++++

# fruits = {"banana": 105, 
#           "orange": 73, 
#           "apple": 72, 
#           "coconut": 354}

# calling the items method and typecasting into a dictionary
# fruits = dict(sorted(fruits.items()))
# to reverse, pass a keyword argument that's a lambda function; items() method returns a tuple during each iteration
# key --> index [0], value --> index [1]
# fruits = dict(sorted(fruits.items(), key=lambda item: item[0], reverse=True))
# sorting the dictionary by value
# fruits = dict(sorted(fruits.items(), key=lambda item: item[1]))
# sorting dictionary by value in reverse order
# fruits = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))

# print(fruits)

# ++++++++++++++ OBJECTS ++++++++++++

class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

# magic method represent --> creates a string representation of an object when printing it
    def __repr__(self):
        return f"{self.name}: {self.calories}"

fruits = [Fruit("banana", 105), 
          Fruit("apple", 72), 
          Fruit("orange", 73),
          Fruit("coconut", 354)]

# to sort by name
# fruits = sorted(fruits, key=lambda fruit: fruit.name)
# to sort in reverse order by name
# fruits = sorted(fruits, key=lambda fruit: fruit.name, reverse=True)
# to sort by calories
# fruits = sorted(fruits, key=lambda fruit: fruit.calories)
# to sort by calories in reverse order
fruits = sorted(fruits, key=lambda fruit: fruit.calories, reverse=True)


print(fruits)
