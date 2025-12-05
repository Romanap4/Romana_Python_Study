# write a function to check whether a number falls within a given range --> version 2

def is_in_range():
    if number in range(1, 101):
        return f"The number {number} is in range 1-100"
    else:
        return f"The number {number} is not in range 1-100"
    
number = float(input("Enter a number: "))
print(is_in_range())
