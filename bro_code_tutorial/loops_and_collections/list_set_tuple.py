# collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable, Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# LIST

# fruits = ["apple", "orange", "banana", "coconut"]

# DIR FUNCTION --> use the dir function to list the different attributes and methods that are available to the collection
# print(dir(fruits))
# HELP FUNCTION --> use the help function to get an in-depth description of each of the methods and attributes
# print(help(fruits))
# LENGTH FUNCTION --> use the length function to return the number of elements in a list
# print(len(fruits))
# IN OPERATOR --> use the in operator to find if a value is within a collection
# print("apple" in fruits)

# INDEX OPERATOR --> it can be used with lists, much like with strings; returns the value at a certain index
# print(fruits[0])
# print(fruits[:3])
# print(fruits[::2])
# print(fruits[::-1])

# ITERATING OVER A LIST
# for fruit in fruits:
#     print(fruit)

# reassigning one of the values using the index operator
# fruits[0] = "pineapple"

# for fruit in fruits:
#     print(fruit)

# APPEND METHOD --> use the append method to add an element to the end of the list
# fruits.append("pineapple")
# REMOVE METHOD --> use the remove method to remove an element from the list
# fruits.remove("apple")
# INSERT METHOD --> use the insert method to insert a value at a given index
# fruits.insert(0, "pineapple")
# SORT METHOD --> use the sort method to sort a list in alphabetical order
# fruits.sort()
# REVERSE METHOD --> use the reverse method to reverse a list
# fruits.reverse()
# CLEAR METHOD --> use the clear method to clear the list
# fruits.clear()
# INDEX METHOD --> use the index method to return the index of an element
# print(fruits.index("apple"))
# COUNT METHOD --> use the count method to count the amount of times an element is found within a list
# print(fruits.count("banana"))

# use sort and then reverse to sort the list in reverse alphabetical order

# print(fruits)

# SET = good for working with constants (e.g. you need to find if a color is within a set)

# fruits = {"apple", "orange", "banana", "coconut"}

# DIR FUNCTION --> use the dir function to list the different attributes and methods that are available to the set
# print(dir(fruits))
# HELP FUNCTION --> use the help function to get an in-depth description of each of the methods and attributes
# print(help(fruits))
# LENGTH FUNCTION --> use the length function to return the number of elements in a set
# print(len(fruits))
# IN OPERATOR --> use the in operator to find if a value is within a collection
# print("pineapple" in fruits)

# indexing can't be used because sets are unordered; this will result in an error
# print(fruits[0])

# ADD METHOD --> use the add method to add an element to a set
# fruits.add("pineapple")
# REMOVE METHOD --> use the remove method to ramove an element from the set
# fruits.remove("apple")
# POP METHOD --> use the pop method to remove whatever element is first; it's going to be random
# fruits.pop()
# CLEAR METHOD --> use the clear method to clear the set
# fruits.clear()

# print(fruits)

# TUPLE

# fruits = ("apple", "orange", "banana", "coconut", "coconut")

# DIR FUNCTION --> use the dir function to list the different attributes and methods that are available to the collection
# print(dir(fruits))
# HELP FUNCTION --> use the help function to get an in-depth description of each of the methods and attributes
# print(help(fruits))
# LENGTH FUNCTION --> use the length function to return the number of elements in a set
# print(len(fruits))
# IN OPERATOR --> use the in operator to find if a value is within a collection
# print("pineapple" in fruits)

# INDEX METHOD --> use the index method to return the index of an element
# print(fruits.index("apple"))
# COUNT METHOD --> use the count method to count the amount of times an element is found within a list
# print(fruits.count("coconut"))

# ITERATING OVER A TUPLE
# for fruit in fruits:
#     print(fruit)

# print(fruits)

# EXERCISE - shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")

# end= --> replaces the newline character at the end of the line with some other character
