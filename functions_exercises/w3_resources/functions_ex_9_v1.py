# write a function that takes a number as a parameter and checks whether the number is prime or not --> version 1

number = input("Enter a number to check: ")
y = [y != number and y != 1 for y in number]
    
def is_it_prime(number, y):
    if number % y == 0:
        print("This number is not a prime number")
    else:
        print("This number is a prime number")

is_it_prime(number, y)
