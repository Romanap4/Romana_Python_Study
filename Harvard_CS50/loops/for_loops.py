# If a variable in Python doesn't have a significance, other than storing a value one time, _ can be used to represent it

for _ in range(3):
    print("meow")

# A different approach

print("meow\n" * 3, end="")

# Textual representation of the Super Mario game
# This way the column size can be modified without any hard coding

def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()

# Printing a row horizontally

def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()

# Implementing both rows and columns in the code
# An outer loop addresses each row in the square
# An inner loop prints a brick in each row
# A print statement that prints a blank line

def main():
    print_square(3)

def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in a row
        for j in range(size):

            # Print brick
            print("#", end="")

        # Print blank line
        print()

main()

# Further abstraction of the code

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()
