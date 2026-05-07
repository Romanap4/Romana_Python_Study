# Implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user's input will be formatted as `x y z`, with one space between `x` and `y` and one space between `y` and `z` wherein:
# `x` is an integer
# `y` is `+`, `-`, `*`, or `/`
# `z` is an integer
# Assume that, if `y` is `/`, then `z` will not be `0`.

expression = input("Expression: ")
x, y, z = expression.split(" ")

if y == "+":
    result = int(x) + int(z)
elif y == "-":
    result = int(x) - int(z)
elif y == "*":
    result = int(x) * int(z)
else:
    result = int(x) / int(z)

print(float(result))
