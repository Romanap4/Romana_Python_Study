# Write a Python code to print the following number pattern using a loop. --> sample solution 1
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

row_number = 5

for i in range(1, row_number + 1):
    print(*range(1, i + 1))
