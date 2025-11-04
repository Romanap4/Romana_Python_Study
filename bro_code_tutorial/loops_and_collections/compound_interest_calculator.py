# Python compund interest calculator

principle = 0
rate = 0
time = 0

# while principle <= 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("Principle can't be less than or equal to zero")

# while rate <= 0:
#     rate = int(input("Enter the interest rate: "))
#     if rate <= 0:
#         print("Interest rate can't be less than or equal to zero")

# while time <= 0:
#     time = float(input("Enter the time in years: "))
#     if time <= 0:
#         print("Time can't be less than or equal to zero")

# print(principle)
# print(rate)
# print(time)

# ANOTHER WAY TO WRITE THE PROGRAM --> it would allow the user to enter values that are equal to 0
# nothing happens because we never enter the While loops, it goes straight to the results (the condition is false from the beginning)

# while principle < 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle < 0:
#         print("Principle can't be less than zero")

# while rate < 0:
#     rate = int(input("Enter the interest rate: "))
#     if rate < 0:
#         print("Interest rate can't be less than zero")

# while time < 0:
#     time = float(input("Enter the time in years: "))
#     if time < 0:
#         print("Time can't be less than zero")

# A DIFFERENT VARIATION using boolean values; works the same, but the user is allowed to enter values equal to zero

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break

while True:
    rate = int(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero")
    else:
        break

# the formula to calculate compound interest:
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
