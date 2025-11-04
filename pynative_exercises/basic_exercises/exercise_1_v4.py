# Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise return their sum. --> version 2

# given 1:
# number1 = 20
# number2 = 30

# # given 2:
# number1 = 40
# number2 = 30

def product_or_sum(number1, number2):
    if number1 * number2 <= 1000:
        print(number1 * number2)
    else:
        print(number1 + number2)

product_or_sum(20, 30)
product_or_sum(30, 40)
