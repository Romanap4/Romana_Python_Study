# positive divisors sum = number 
# (positive divisors + number) / 2 = number 

number = input()

def is_perfect_number(number, x, y):
    if number == x * y and number == x + y and (x + y + number) / 2 == number:
        print("This number is perfect")


