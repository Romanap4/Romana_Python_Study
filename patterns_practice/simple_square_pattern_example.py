# printing is done row by row, left to right
# empty space is built by printing spaces
# rows need to be printed entirely, no skipping

# STEP 1: decide on the size; the outer loop determines the number of rows

# taking input from user:
# n = int(input("Number of rows: "))

# if the size is given in the question, assign it:
# n = 5

# if you're writing a function, pass it as a parameter:
# def pattern (n):

# STEP 2: pattern program --> use loops

# to print n stars:

# use multiplication in the print statement:
# n = 5
# print("*" * n)

# use a loop (range function with a for loop in this example):
# n = 5
# for j in range(n):
#     print("*")
# the loop will run from 0 to less than n
# to print the stars in the same line:
# for j in range(n):
#     print("*", end="")
# the loop runs 5 times and prints 5 stars
# to print 5 rows and get a square pattern, insert this set of code inside another loop which will print the row 5 times

# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()

# insert a print statement as the last statement of the outer loop to go to the next line after the whole row is printed

# the code is executed starting with the outer loop which holds the number of rows; it starts with 0
# then we enter the inner loop which holds the number of columns; it starts with 0 and runs until less than n
# once printing all the columns is finished, the control goes back to the outer loop which then increments by 1
# this repeats for each row, until i is less than n; then we exit from the outer loop
