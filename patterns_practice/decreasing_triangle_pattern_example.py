n = 5
for i in range(n):
    for j in range(i, n):
        print("*", end=" ")
    print()

# to get the columns to print a decreasing number of stars, add i as the start condition
# the first column runs from 0 to 5, the second from 1 to 5, the third from 2 to 5 and so on...
