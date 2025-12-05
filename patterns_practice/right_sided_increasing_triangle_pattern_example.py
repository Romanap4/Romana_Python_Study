# this patern is built from two triangles:
# 1) decreasing triangle printing space
# 2) increasing triangle printing stars
# since the number of rows is the same, the outer loop will be the same as in the previous exercises

n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")

    for j in range(i + 1):
        print("*", end=" ")

    print()

# first row --> i is 0, the upper nested loop prints 5 spaces and the second nested loop prints 1 star
# second row --> i becomes 1, the upper nested loop prints 4 spaces and the second nested loop prints 2 stars
# this continues until the entire pattern is printed
# print() is linked to rows in the outer loop, it doesn't repeat with every nested loop
# each print statement prints two characters --> a space and a space or a character (star) and a space
# all of the print statements have to have the same number of characters
