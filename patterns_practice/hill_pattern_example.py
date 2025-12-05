# we will need 3 triagnle patterns to make a hill pattern:
# 1) decreasing triangle printing space
# 2) increasing right-sided triangle printing stars
# 3) increasing triangle printing stars

n = 5
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    for j in range(i + 1):
        print("*", end=" ")

    print()

# output doesn't have a peak; we need one less column
# by changing the condition in one of the nested loops from (i + 1) to (i), it will print one less column
