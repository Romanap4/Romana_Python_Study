# conditional expressions = A one-line shortcut for the if-else statement (ternary operator in other programming languages)
#                           Print or assign one of two values based on a condition
#                           X if condition else Y (formula)

num = 5
a = 6
b = 7
age = 13
temperature = 10
user_role = "guest"

# print("Positive" if num > 0 else "Negative")

# result = "EVEN" if num % 2 == 0 else "ODD"
# print(result)

# max_num = a if a > b else b
# min_num = a if a < b else b
# print(max_num)
# print(min_num)

# status = "Adult" if age >= 18 else "Child"
# print(status)

# weather = "Hot" if temperature > 20 else "Cold"
# print(weather)

access_level = "Full access" if user_role == "admin" else "Limited access"
print(access_level)