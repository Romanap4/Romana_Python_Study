# Creating our own function
def hello(to):
    print("Hello,", to)

# Output using our own function
name = input("What's your name? ")
hello(name)

# Creating a function and telling the interpreter that the function takes a single parameter - a variable called "to"
# When you call the hello(name), the computer passes the "name" into the hello() function as "to"; the names don't have to match

# A default value can be added to hello()

# Creating our own function
def hello(to="world"):
    print("Hello,", to)

# Output using our own function
name = input("What's your name? ")
hello(name)

# Output without passing the expected arguments
hello()

# A main function can be created and the hello function can be moved down; make sure to call the main function at the end of the program

def main():
    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()

# Creating our own function
def hello(to="world"):
    print("Hello,", to)

main()


