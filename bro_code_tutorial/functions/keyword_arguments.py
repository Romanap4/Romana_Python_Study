# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional, 2. default, 3. KEYWORD, 4. arbitrary

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")

# when sending arguments to a function, you can turn positional arguments into keyword arguments
# hello("Hello", title="Mr.", last="Choi", first="Minho")

# when mixing positional and keyword arguments, make sure the positional arguments come first
# you can use keyword arguments for clarification
# hello("Hello", title="Mr.", last="John", first="James")

# "end" is a keyword argument found within a built-in print function
# for x in range(1, 11):
#     print(x, end=" ")

# "separate" is a keyword argument also found within the print function
# print("1", "2", "3", "4", "5", sep="-")

# EXERCISE - create a function to generate a phone number

# the order of parameters doesn't matter, but it's good to be consistent
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=385, area=1, first=414, last=3333)

print(phone_num)
