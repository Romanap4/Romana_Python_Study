# we need two hill patterns to make a diamond pattern:
# 1) hill pattern
# 2) reverse hill pattern
# the rows are doubline, so we need to run the code for both parts of the pattern along with the outer loop and nested loops
# to get a diamond pattern, change the condition of the outer loop to print one less row

n = 5
for i in range(n - 1):
    for j in range(i, n):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    for j in range(i + 1):
        print("*", end=" ")

    print()

for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")
    
    for j in range(i, n - 1):
        print("*", end=" ")

    for j in range(i, n):
        print("*", end=" ")

    print()

