# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# DIR FUNCTION --> use the dir function to list the different attributes and methods that are available to the collection
# print(dir(capitals))
# HELP FUNCTION --> use the help function to get an in-depth description of each of the methods and attributes
# print(help(capitals))

# to get one of the values from a ditionary, you need to get the key
# print(capitals.get("China"))
# GET METHOD --> use to check if a key is within our dictionary:
# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# UPDATE METHOD --> use the update method to insert a new or update an existing {key:value} pair
# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# POP METHOD --> use the pop method to remove a {key:value} pair
# capitals.pop("China")
# POP ITEM METHOD --> use the pop item method to remove the latest {key:value} pair; no need to pass in a key
# capitals.popitem()
# CLEAR METHOD --> use the clear method to clear the dictionary
# capitals.clear()

# print(capitals)

# KEYS METHOD --> use the keys method to get all of the keys within a dictionary, but not the values
# keys is an object which resembles a list
# keys = capitals.keys()
# print(keys)

# ITERATING KEYS
# for key in capitals.keys():
#     print(key)

# VALUES METHOD --> use the values method to get all of the values within a dictionary
# values = capitals.values()
# print(values)

# ITERATING VALUES
# for value in capitals.values():
#     print(value)

# ITEMS METHOD --> the items method returns a dictionary object which resembles a 2D list of tuples
# items = capitals.items()
# print(items)

# ITERATING OVER EVERY KEY: VALUE PAIR
# for key, value in capitals.items():
#     print(f"{key}: {value}")

# EXERCISE - concession stand program
# dictionary {key:value}

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
# if the user selection is not within the menu as a key, the get method will return None

# print(cart)
# printed to test the program

print("-------YOUR ORDER-------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
# using the get method to get the value associated with a key

print()
print(f"Total is: ${total:.2f}")
