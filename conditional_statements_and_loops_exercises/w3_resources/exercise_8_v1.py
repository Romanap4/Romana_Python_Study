# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5

for number in range(0, 7):
    if number == 3 or number == 6:
        continue
    else:
        print(number, end=" ")
