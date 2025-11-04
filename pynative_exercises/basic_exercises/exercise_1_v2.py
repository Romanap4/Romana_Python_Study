# Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise return their sum. --> version 2

# given 1:

number1 = 20
number2 = 30

def product_or_sum_1():
    if number1 * number2 <= 1000:
        return number1 * number2
    else:
        return number1 + number2

# given 2:

number3 = 40
number4 = 30

def product_or_sum_2():
    if number3 * number4 <= 1000:
        return number3 * number4
    else:
        return number3 + number4

print(product_or_sum_1())
print(product_or_sum_2())
