# indexing = acessing elements of a sequence using [] (indexing operator)
#            [start : end : step]
# computers always start with 0, that's why the first index is 0
# the ending index is exclusive - it's not included; the starting index is inclusive

credit_number = "1234-5678-9012-3456"

# print(credit_number[4])

# getting the first 4 characters of the string:
# print(credit_number[0:4])
# print(credit_number[:4]) --> Python assumes the starting position will be the beginning of the string

# getting the next 4 characters of the string:
# print(credit_number[5:9])

# getting the last 12 characters:
# print(credit_number[5:]) --> Python assumes you need everything up to the end of the string

# use negative numbers if you need the characters at the end of the string:
# print(credit_number[-1])    

# STEP --> counts the characters by a given step
# [::] returns every character from the beginning to the end
# getting every other character:
# print(credit_number[::2])

# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

# to reverse the string:
# credit_number = credit_number[::-1]
# print(credit_number)

# EXERCISE --> email slicer

email = input("Enter your email: ")

# INDEX FUNCTION - returns the first instance of a character
index = email.index("@")

# username = email[:index]
# domain = email[index + 1:]
# +1 because we wanted to omit the "@" sign

# for less lines of code (but it's also less readable):

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your username is {username} and domain is {domain}")
