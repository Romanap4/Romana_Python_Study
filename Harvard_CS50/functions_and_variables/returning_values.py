# A function passing a value back after performing an action is called a return value

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()

# x is passed to square(); the calculation of x * x is returned back to the main() function
