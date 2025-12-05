n = 5
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

# for this pattern we need the row number plus one star
# set the inner loop to run to (i + 1)
# the remaining program remains the same as for the square
