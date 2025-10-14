# *args    = allows you to pass multiple non-key arguments (packing into a tuple)
# **kwargs = allows you to pass multiple keyword arguments (packing into a dictionary)
#            * unpacking operator
#            1. positional, 2. default, 3. keyword, 4. ARBITRARY (varying amount of arguments)

# def add(a, b):                 # this function can't be used to pass more than 2 parameters
#     return a + b
# print(add(1, 2))

# def add(*args):                # using the unpacking operator and packing the arguments into a tuple
#     print(type(args))          # args is a tuple, you can use the built-in methods or iterate over it

# def add(*args):                # the name of the parameter can be changed ("*nums" for example); unpacking operator is important
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# print(add(1, 2, 3, 4))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
# display_name("Dr.", "John", "Michael", "Wick", "III")

# def print_address(**kwargs):   # checking the type (it's a dictionary)
#     print(type(kwargs))

# def print_address(**kwargs):
#     for value in kwargs.values():
#         print(value)

# def print_address(**kwargs):
#     for key in kwargs.keys():
#         print(key)

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(street="123 Fake St.",
#               apt = "100",
#               city="Detroit",
#               state="MI",
#               zip="54321")

# EXERCISE - print a shipping label

# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     for value in kwargs.values():
#         print(value, end= " ")

# to format the address differently:
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

#     print(f"{kwargs.get('street')}, {kwargs.get('apt')}")      # using single quotes to be clear on where the f-string ends
    if "apt" in kwargs:                                          # in case there is no apt
        print(f"{kwargs.get('street')}, {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('zip')}")

# positional arguments have to come before keyword arguments; it doesn't work the other way around

shipping_label("Dr.", "John", "Wick", "III",
               street="123 Fake St.",
               pobox = "PO box #1001",
               apt="#100",
               city="Detroit",
               state="MI",
               zip="54321")
