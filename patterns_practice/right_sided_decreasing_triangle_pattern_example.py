# the number of rows is the same as in the square pattern, so the outer loop will remain the same

n = 5
for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")

    for j in range(i, n):
        print("*", end=" ")

    print()

