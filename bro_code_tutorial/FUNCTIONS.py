# function = a block of reusable code
#            place () after the function name to invoke it

# def happy_birthday(name, age):                                  # defining a function (def and a unique function name)
#     print(f"Happy birthday to {name}!")                         # adding a parameter to a function; temporary variable used within a function
#     print(f"You are {age} years old!")
#     print("Happy birthday to you!")
#     print()

# happy_birthday()                                                # invoking a function
# happy_birthday("Manyan", 34)                                    # using arguments to send data directly to a function (values or variables)
# happy_birthday("Wednesday", 15)                                 # positional arguments
# happy_birthday("Chan", 28)                                      # you need a matching set of arguments and parameters; order matters

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}!")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("Manyan", 42.50, "01/01")

# return = statement used to end a function and send a result back to the caller

# def add(x, y):
#     z = x + y
#     return z

# def subtract(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def divide(x, y):
#     z = x / y
#     return z

# print(add(1, 2))                                    # after resolving a function, it becomes whatever is returned
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(divide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("manyan", "blabla")

print(full_name)
