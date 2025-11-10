# Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case)

line = input("Enter a line/lines to turn into lowercase: ")
running = True

while running:
    print(line.lower())
    line = input("Enter another line/lines to turn into lowercase: ")
    if line == "":
        running = False
