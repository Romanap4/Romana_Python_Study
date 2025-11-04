# for loops = iterate a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

# ITERATING OVER A RANGE FUNCTION

# range function; the second number is exclusive
# x --> counter
# for x in range(1, 11):
#     print(x)

# reversed function --> use to count backwards
# for x in reversed(range(1, 11)):
#     print(x)

# this is printed outside of the for loop
# print("HAPPY NEW YEAR!")

# adding a step
# for x in range(1, 11, 2):
#     print(x)

# ITERATING OVER A STRING

# credit_card = "1234-5678-9012-3456"

# the counter (x) will hold our current position
# for x in credit_card:
#     print(x)

# USEFUL KEYWORDS --> continue and break; they can be used in for and while loops

# using continue to skip over an iteration
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

# using break to escape the loop entirely
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)
