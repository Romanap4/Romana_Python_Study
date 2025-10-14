# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

#STRINGS

word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")

# REVERSE:

# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")

# SETS (LISTS and TUPLES would behave the same)

# students = {"Wednesday", "Enid", "Pugsley"}

# student = input("Enter the name of a student: ")

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} was not found")

# REVERSE:

# if student not in students:
#     print(f"{student} was not found")
# else:
#     print(f"{student} is a student")

# DICTIONARIES:

# grades = {"Wednesday": "A",
#           "Enid": "B",
#           "Pugsley": "C",
#           "Roland": "D"}

# student = input("Enter the name of a student: ")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

email = "blibla@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")
