# name = input("Enter your full name: ")
# phone_num = input("Enter your phone number: ")

# result = len(name)          # length function = returns the length of a string (the number of characters); returns an integer
# result = name.find("M")     # find method = returns the first occurence of a given character (position); starts at index 0
# result = name.rfind("a")    # reverse find method = returns the last occurence of a given character
# if Python (rfind method) cannot find a given character, it will return -1 result
# name = name.capitalize()    # capitalize function = capitalizes the first character in a string
# name = name.upper()         # upper method = turns all of the characters in a string into uppercase
# name = name.lower()         # lower method = turns all of the characters in a string into lowercase
# result = name.isdigit()     # isdigit method = returns either True or False (if the string contains only digits)
# result = name.isalpha()     # isalpha method = returnd either True or False (if the string contains only alphabetical characters)
# result = phone_num.count("-")  # count method = counts the number of a given character in a string; returns an integer
# phone_num = phone_num.replace("-", "")  # replace method = replaces any occurence of a given character with another

# print(result)
# print(name)
# print(phone_num)

# print(help(str))                # help function = "str" means string, use to get a full list of available string methods

# EXERCISE

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")
