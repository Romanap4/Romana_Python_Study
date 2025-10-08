# indexing = acessing elements of a sequence using [] (indexing operator)
#            [start : end : step]
# computers always start with 0, that's why the first index is 0
# the ending index is exclusive - it's not included; the starting index is inclusive

credit_number = "1234-5678-9012-3456"

# print(credit_number[4])
# print(credit_number[0:4])   # [:4] - 0 can be omitted; Python assumes the staring index is the beginning of the string
# print(credit_number[5:9])
# print(credit_number[5:])    # [5:] - Python assumes you need everything up to the end of the string
# print(credit_number[-1])    # use negative numbers if you need the characters at the end of the string

# print(credit_number[::2])   # step - counts the characters by a given step; [::] gives everything from the beginning to the end

# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")

credit_number = credit_number[::-1] # this will reverse the string
print(credit_number)

# EXERCISE

# email slicer exercise

email = input("Enter your email: ")

index = email.index("@")             # index function - returns the first instance of a character

# username = email[:index]
# domain = email[index + 1:]           # +1 because we wanted to omit the "@" sign

# for less lines of code (but it's also less readable):

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]


print(f"Your username is {username} and domain is {domain}")

       

