# collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable, Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# LIST

# fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits))                  # use the dir function to list the different methods that are available to the collection
# print(help(fruits))                 # use the help function to get a description of each of the methods and attributes
# print(len(fruits))
# print("apple" in fruits)            # use the in operator to find if a value is within a collection

# print(fruits[0])                    # you can use the index operator, like with strings
# print(fruits[:3])
# print(fruits[::2])
# print(fruits[::-1])

# for fruit in fruits:
#     print(fruit)

# fruits[0] = "pineapple"

# for fruit in fruits:
#     print(fruit)

# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")       # use the insert method to insert a value at a given index
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("banana"))

# print(fruits)

# SET = good for working with constants (e.g. you need to find if a color is within a set)

# fruits = {"apple", "orange", "banana", "coconut"}
# print(dir(fruits))                   # use to display all of the different attributes and methods of a set
# print(help(fruits))                  # use to display an in-depth description of these methods
# print(len(fruits))
# print("pineapple" in fruits)

# print(fruits[0])                     # indexing can't be used because sets are unordered

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()                         # pop method removes whatever element is first; it's random
# fruits.clear()

# print(fruits)

# TUPLE

# fruits = ("apple", "orange", "banana", "coconut", "coconut")
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# print(fruits.index("apple"))
# print(fruits.count("coconut"))
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
