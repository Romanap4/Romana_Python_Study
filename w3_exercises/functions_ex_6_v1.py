# write a function to check whether a number falls within a given range --> version 1

number = float(input("Enter a number: "))

def is_in_range(number):
    if number in range(1, 101):
        print(f"The number {number} is in range 1-100")
    else:
        print(f"The number {number} is not in range 1-100")

is_in_range(number)
