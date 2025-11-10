# Write a Python program to construct the following pattern, using a nested for loop --> version 1

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# Set the value of 'n' to 5 (this will determine the number of lines in the pattern)
n = 5

# Iterate through the range of numbers from 0 to 'n' (exclusive)
for i in range(n):
    # Iterate through the range of numbers from 0 to 'i' (exclusive) for each 'i' in the outer loop
    for j in range(i):
        # Print '*' followed by a space without a new line (end="" ensures printing in the same line)
        print('* ', end="")
    # Move to the next line after printing '*' characters for the current 'i'
    print('')

# Iterate through the range of numbers from 'n' down to 1 (inclusive), decreasing by 1 in each iteration
for i in range(n, 0, -1):
    # Iterate through the range of numbers from 0 to 'i' (exclusive) for each 'i' in the outer loop
    for j in range(i):
        # Print '*' followed by a space without a new line (end="" ensures printing in the same line)
        print('* ', end="")
    # Move to the next line after printing '*' characters for the current 'i'
    print('')
