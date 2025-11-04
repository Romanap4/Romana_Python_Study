# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:
# the type of the inner and outer loop depend on the situation (they can be any combination of while and for loops)

# print statements end with a newline character (\n); "end_""" puts the numbers in the same line; you can choose a space or a different symbol as well
# "print()" prints a new line
# the code within the outer loop will be repeated 3 times in this case
# for x in range(3):
#     for y in range(1, 10):
#         print(y, end="")
#     print()

# EXERCISE --> printing a rectangle made out of a chosen symbol

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end = "")
    print()
