# Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise return their sum. --> version 1

# given 1:

number1 = 20
number2 = 30

if number1 * number2 <= 1000:
    print(number1 * number2)
else:
    print(number1 + number2)

# given 2:

number3 = 40
number4 = 30

if number3 * number4 <= 1000:
    print(number3 * number4)
else:
    print(number3 + number4)
