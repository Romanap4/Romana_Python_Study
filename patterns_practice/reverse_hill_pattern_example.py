# to make this pattern, we need three triangles:
# 1) increasing space triangle
# 2) decreasing right-sided star triangle
# 3) decreasing star triangle
# the number of the rows is the same, so the outer loop remains the same

n = 5
for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")
    
    for j in range(i, n - 1):
        print("*", end=" ")

    for j in range(i, n):
        print("*", end=" ")

    print()

