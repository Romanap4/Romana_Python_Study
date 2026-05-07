# Creating a function to determine if a number is even or odd

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
main()

# The statement is_even(x) works without an operator because the function returns a boolean value of True or False back to the main() function

# "Pythonic" programming - ways of programming that are sometimes only seen in Python

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False

main()

# The return code is almost like a sentence in English - a unique way of coding only seen in Python
# The code can be shortened further

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main()

# The program will evaluate what's happening within n % 2 == 0 as either True or False and simply return that to the main() function