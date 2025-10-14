# logical operators = used on conditional statements (such as if statements)

#               and = checks two or more conditions if True
#                or = checks if at least one condition is True
#               not = True if condition is False, and vice versa

# temp = 25

# if temp > 0 and temp < 30:
#     print("The temperature is good")
# else:
#     print("The temperature is bad")

# temp = 20

# if temp <= 0 or temp >= 30:
#     print("The temperature is bad")
# else:
#     print("The temperature is good")

temp = 20
sunny = True

if not sunny:                 # you can use just the boolean, without the equation
    print("It is cloudy outside")
else:
    print("It is sunny outside")
