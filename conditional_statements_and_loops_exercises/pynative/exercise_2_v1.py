# Write a Python code to print the following number pattern using a loop. --> version 1
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

for x in range(1, 6):
    for y in range(x):
        y += 1
        print(y, end=" ")
    print()
