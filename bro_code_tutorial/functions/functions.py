# function = a block of reusable code
#            place () after the function name to invoke it
# without functions, you'd have to repeat the code a few times or place it within a loop

# defining a function ('def' and a unique function name):
# any code that belongs to a function is indented underneath
# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}!")
# adding a parameter to a function; temporary variable used within a function
#     print(f"You are {age} years old!")
#     print("Happy birthday to you!")
#     print()

# invoking a function
# happy_birthday()
# using arguments to send data directly to a function (values or variables)
# you need a matching set of arguments and parameters; order matters
# these are called positional arguments
# happy_birthday("Manyan", 34)
# happy_birthday("Wednesday", 15)
# happy_birthday("Chan", 28)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}!")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("Manyan", 42.50, "01/01")

# return = statement used to end a function and send a result back to the caller
# the returned value can be assigned to a variable

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

# after resolving a function, it becomes whatever is returned
# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(divide(1, 2))

# using the return statement you can return some data back to the place in which you called a function
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("manyan", "blabla")

print(full_name)
