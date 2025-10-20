# Write a function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument
# --> version 1
# FACTORIAL FUNCTION EXISTS!!

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)
    
x = int(input("Enter a number to calculate the factorial: "))

print(factorial(x))
