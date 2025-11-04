# name = input("Enter your full name: ")
# phone_num = input("Enter your phone number: ")

# LENGTH FUNCTION --> returns the length of a string (the number of characters); returns an integer
# result = len(name)

# FIND METHOD --> returns the first occurence of a given character (position); starts at index 0
# result = name.find("M")

# REVERSE FIND METHOD --> returns the last occurence of a given character
# result = name.rfind("a")
# if Python (rfind method) cannot find a given character, it will return -1 result

# reassigning the result to the name variable to overwrite it ˇˇ

# CAPITALIZE FUNCTION --> capitalizes the first character in a string
# name = name.capitalize()

# UPPER METHOD --> turns all of the characters in a string into uppercase
# name = name.upper()

# LOWER METHOD --> turns all of the characters in a string into lowercase
# name = name.lower()

# ISDIGIT METHOD --> returns either True or False (if the string contains only digits)
# result = name.isdigit()

# ISALPHA METHOD --> returns either True or False (if the string contains only alphabetical characters)
# result = name.isalpha()

# COUNT METHOD --> counts the number of a given character in a string; returns an integer
# result = phone_num.count("-")

# REPLACE METHOD --> replaces any occurence of a given character with another
# phone_num = phone_num.replace("-", "")

# print(result)
# print(name)
# print(phone_num)

# HELP FUNCTION --> "str" means string, use to get a full list of available string methods
# print(help(str))

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
